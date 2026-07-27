#!/usr/bin/env python3
"""Validate a game analytics metric specification in JSON or YAML."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


PRODUCT_REQUIRED = {
    "name",
    "archetype",
    "lifecycle_stage",
    "timezone",
    "identity_unit",
    "north_star",
}
METRIC_REQUIRED = {
    "id",
    "name",
    "domain",
    "question",
    "definition",
    "formula",
    "entity",
    "grain",
    "window",
    "dimensions",
    "source_events",
    "owner",
    "freshness",
    "status",
}
VALID_STATUSES = {"draft", "proposed", "approved", "deprecated"}
VALID_EVENT_STATUSES = {
    "proposed",
    "approved",
    "implemented",
    "validated",
    "official",
    "deprecated",
}
VALID_DELIVERY_LANES = {"real_time", "telemetry", "both"}
RATE_PATTERN = re.compile(
    r"(率|占比|ratio|rate|retention|conversion|ctr|cvr|share)", re.IGNORECASE
)
RETENTION_PATTERN = re.compile(r"(留存|retention|survival)", re.IGNORECASE)
MONEY_PATTERN = re.compile(
    r"(收入|流水|金额|成本|付费|ltv|arpu|arppu|arpdau|roi|roas|cac|cpi|"
    r"revenue|bookings|cost|spend|gmv)",
    re.IGNORECASE,
)
ID_PATTERN = re.compile(r"^[a-z][a-z0-9_]*$")
ROI_PATTERN = re.compile(r"(?<![a-z])roi(?![a-z])|投资回报", re.IGNORECASE)
ROAS_PATTERN = re.compile(r"roas|广告支出回报", re.IGNORECASE)
LTV_PATTERN = re.compile(
    r"(?<![a-z])ltv(?![a-z])|生命周期价值|lifetime\s*value", re.IGNORECASE
)
REVENUE_TOKEN = re.compile(
    r"(revenue|bookings|gmv|收入|流水|回收|广告收入|变现)", re.IGNORECASE
)
SPEND_TOKEN = re.compile(
    r"(spend|cost|投放|消耗|成本|投入|investment)", re.IGNORECASE
)
CONTRIBUTION_TOKEN = re.compile(
    r"(margin|contribution|profit|net of|扣除|毛利|利润|净贡献)", re.IGNORECASE
)
HORIZON_PATTERN = re.compile(
    r"(d\s*\d+|day\s*\d+|第\s*\d+\s*天|\d+\s*日|\d+\s*天|week\s*\d+|"
    r"horizon|时间跨度|观察窗)",
    re.IGNORECASE,
)
MATURITY_PATTERN = re.compile(
    r"(realized|actual|observed|predicted|prediction|forecast|projected|"
    r"extrapolat|已实现|实测|实际|预测|预估|外推|拟合)",
    re.IGNORECASE,
)
BENCHMARK_PROVENANCE = (
    "source",
    "region",
    "genre",
    "platform",
    "cohort_date",
    "definition",
)


def load_spec(path: Path) -> dict[str, Any]:
    suffix = path.suffix.lower()
    text = path.read_text(encoding="utf-8-sig")
    if suffix == ".json":
        value = json.loads(text)
    elif suffix in {".yaml", ".yml"}:
        try:
            import yaml  # type: ignore
        except ImportError as exc:
            raise RuntimeError(
                "YAML validation requires PyYAML; use JSON or install PyYAML."
            ) from exc
        value = yaml.safe_load(text)
    else:
        raise ValueError("Only .json, .yaml, and .yml files are supported.")
    if not isinstance(value, dict):
        raise ValueError("The top-level specification must be an object.")
    return value


def blank(value: Any) -> bool:
    return value is None or value == "" or value == []


def validate(spec: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    product = spec.get("product")
    if not isinstance(product, dict):
        return ["product must be an object."], warnings

    missing_product = sorted(
        key for key in PRODUCT_REQUIRED if key not in product or blank(product[key])
    )
    if missing_product:
        errors.append(
            "product is missing required fields: " + ", ".join(missing_product)
        )

    north_star = product.get("north_star", [])
    if isinstance(north_star, str):
        north_star_ids = [north_star]
    elif isinstance(north_star, list) and all(
        isinstance(item, str) for item in north_star
    ):
        north_star_ids = north_star
    else:
        errors.append("product.north_star must be a metric ID or a list of metric IDs.")
        north_star_ids = []

    events_value = spec.get("events", [])
    if not isinstance(events_value, list):
        errors.append("events must be a list when provided.")
        events_value = []
    event_names: set[str] = set()
    for index, event in enumerate(events_value):
        label = f"events[{index}]"
        if not isinstance(event, dict):
            errors.append(f"{label} must be an object.")
            continue
        name = event.get("name")
        if not isinstance(name, str) or not name.strip():
            errors.append(f"{label}.name is required.")
            continue
        if name in event_names:
            errors.append(f"Duplicate event name: {name}")
        event_names.add(name)
        for field in ("owner", "authoritative_source"):
            if blank(event.get(field)):
                warnings.append(f"{label} ({name}) should define {field}.")
        for field in ("event_version", "entity", "schema_status", "delivery_lane"):
            if blank(event.get(field)):
                warnings.append(
                    f"{label} ({name}) should define {field} for a governed event contract."
                )
        schema_status = event.get("schema_status")
        if schema_status is not None and schema_status not in VALID_EVENT_STATUSES:
            errors.append(
                f"{label} ({name}): schema_status must be one of "
                f"{sorted(VALID_EVENT_STATUSES)}."
            )
        delivery_lane = event.get("delivery_lane")
        if delivery_lane is not None and delivery_lane not in VALID_DELIVERY_LANES:
            errors.append(
                f"{label} ({name}): delivery_lane must be one of "
                f"{sorted(VALID_DELIVERY_LANES)}."
            )
        properties = event.get("properties")
        if properties is not None:
            if not isinstance(properties, list):
                errors.append(f"{label} ({name}): properties must be a list.")
            else:
                property_names: set[str] = set()
                for property_index, prop in enumerate(properties):
                    property_label = f"{label}.properties[{property_index}]"
                    if not isinstance(prop, dict):
                        errors.append(f"{property_label} must be an object.")
                        continue
                    property_name = prop.get("name")
                    if not isinstance(property_name, str) or not property_name.strip():
                        errors.append(f"{property_label}.name is required.")
                        continue
                    if property_name in property_names:
                        errors.append(
                            f"Duplicate property name in {label} ({name}): {property_name}"
                        )
                    property_names.add(property_name)
                    for field in ("type", "cardinality", "data_classification"):
                        if blank(prop.get(field)):
                            warnings.append(
                                f"{property_label} ({property_name}) should define {field}."
                            )

    metrics_value = spec.get("metrics")
    if not isinstance(metrics_value, list) or not metrics_value:
        errors.append("metrics must be a non-empty list.")
        return errors, warnings

    metric_ids: set[str] = set()
    for index, metric in enumerate(metrics_value):
        label = f"metrics[{index}]"
        if not isinstance(metric, dict):
            errors.append(f"{label} must be an object.")
            continue

        metric_id = str(metric.get("id", "")).strip()
        display = metric_id or label
        missing = sorted(
            key for key in METRIC_REQUIRED if key not in metric or blank(metric[key])
        )
        if missing:
            errors.append(f"{display} is missing required fields: {', '.join(missing)}")

        if metric_id:
            if not ID_PATTERN.fullmatch(metric_id):
                errors.append(
                    f"{display}: id must use lowercase letters, digits, and underscores."
                )
            if metric_id in metric_ids:
                errors.append(f"Duplicate metric id: {metric_id}")
            metric_ids.add(metric_id)

        if metric.get("status") not in VALID_STATUSES:
            errors.append(
                f"{display}: status must be one of {sorted(VALID_STATUSES)}."
            )

        for list_field in ("dimensions", "source_events", "aliases"):
            value = metric.get(list_field)
            if value is not None and not isinstance(value, list):
                errors.append(f"{display}: {list_field} must be a list.")

        source_events = metric.get("source_events", [])
        if isinstance(source_events, list) and event_names:
            unknown = sorted(
                event
                for event in source_events
                if isinstance(event, str) and event not in event_names
            )
            if unknown:
                errors.append(
                    f"{display}: source_events not declared in events: "
                    + ", ".join(unknown)
                )

        name_and_id = f"{metric.get('name', '')} {metric_id}"
        formula = str(metric.get("formula", ""))
        definition = str(metric.get("definition", ""))
        window = str(metric.get("window", ""))

        if RATE_PATTERN.search(name_and_id):
            if not any(token in formula for token in ("/", "÷", " per ", " over ")):
                warnings.append(
                    f"{display}: rate/share metric formula should expose a denominator."
                )
            zero_policy = " ".join(
                str(metric.get(key, ""))
                for key in ("zero_denominator_policy", "data_policy", "definition")
            )
            if not re.search(
                r"(零分母|zero.denominator|null|undefined)", zero_policy, re.I
            ):
                warnings.append(f"{display}: define a zero-denominator policy.")

        if RETENTION_PATTERN.search(name_and_id):
            retention_text = f"{definition} {window}"
            if not re.search(
                r"(cohort|队列|同期|新增|激活|注册|anchor|exact|rolling|bracket|"
                r"自然日|第\s*\d+\s*天|day\s*\d+)",
                retention_text,
                re.IGNORECASE,
            ):
                warnings.append(
                    f"{display}: retention metric should define cohort anchor and type."
                )

        if MONEY_PATTERN.search(name_and_id):
            if blank(product.get("currency")):
                warnings.append(
                    f"{display}: product.currency is recommended for monetary metrics."
                )
            basis = " ".join(
                str(metric.get(key, ""))
                for key in ("monetary_basis", "definition", "formula")
            )
            if not re.search(
                r"(gross|net|bookings|revenue|流水|收入|毛额|净额|成本|spend|margin)",
                basis,
                re.IGNORECASE,
            ):
                warnings.append(
                    f"{display}: define the monetary/revenue or cost basis."
                )

        formula_and_definition = f"{formula} {definition}"
        horizon_text = f"{name_and_id} {window} {definition}"

        if ROI_PATTERN.search(name_and_id) and not ROAS_PATTERN.search(name_and_id):
            revenue_over_spend = (
                REVENUE_TOKEN.search(formula)
                and SPEND_TOKEN.search(formula)
                and any(token in formula for token in ("/", "÷"))
            )
            if revenue_over_spend and not CONTRIBUTION_TOKEN.search(
                formula_and_definition
            ):
                warnings.append(
                    f"{display}: revenue divided by spend is ROAS, not ROI. "
                    "Rename it, or state the contribution/profit basis if ROI is intended."
                )

        if ROAS_PATTERN.search(name_and_id) or ROI_PATTERN.search(name_and_id):
            if not HORIZON_PATTERN.search(horizon_text):
                warnings.append(
                    f"{display}: ROAS/ROI needs an explicit horizon (for example d7, d30)."
                )

        if LTV_PATTERN.search(name_and_id):
            if not HORIZON_PATTERN.search(horizon_text):
                warnings.append(
                    f"{display}: LTV needs an explicit horizon; unbounded LTV is not measurable."
                )
            maturity_text = " ".join(
                str(metric.get(key, ""))
                for key in ("estimation", "estimation_method", "maturity", "definition")
            )
            if not MATURITY_PATTERN.search(maturity_text):
                warnings.append(
                    f"{display}: label LTV as realized or predicted, and record the "
                    "model, censoring, and backtest error when predicted."
                )

        benchmark = metric.get("benchmark", metric.get("benchmarks"))
        if not blank(benchmark):
            if not isinstance(benchmark, dict):
                warnings.append(
                    f"{display}: benchmark must carry provenance "
                    f"({', '.join(BENCHMARK_PROVENANCE)}), not a bare value."
                )
            else:
                missing_provenance = [
                    key for key in BENCHMARK_PROVENANCE if blank(benchmark.get(key))
                ]
                if missing_provenance:
                    warnings.append(
                        f"{display}: benchmark is missing provenance: "
                        + ", ".join(missing_provenance)
                    )

        if blank(metric.get("direction")):
            warnings.append(f"{display}: direction/interpretation is recommended.")
        if "filters" not in metric:
            warnings.append(
                f"{display}: define exclusions or explicitly use an empty filters list."
            )

    missing_north_star = sorted(set(north_star_ids) - metric_ids)
    if missing_north_star:
        errors.append(
            "product.north_star references undefined metric IDs: "
            + ", ".join(missing_north_star)
        )

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path, help="Path to JSON/YAML metric spec")
    parser.add_argument(
        "--strict", action="store_true", help="Treat warnings as validation failures"
    )
    args = parser.parse_args()

    try:
        spec = load_spec(args.spec)
        errors, warnings = validate(spec)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARNING: {item}")

    print(f"Validation summary: {len(errors)} error(s), {len(warnings)} warning(s).")
    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
