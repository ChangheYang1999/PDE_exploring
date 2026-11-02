"""Reduce the declared historical R13 base rows. No policy or engine imports."""
import collections
import json

from review_record_tools_004 import (
    OUT, Evidence, error_counts, normalize, row_metadata_ok, rows, sha, wdl,
)


def main(ev):
    receipt = OUT / "final-gate-20261031T233546260787Z/inspection.json"
    raw = ev.capture(receipt)
    ev.check(sha(raw) == "3c06e23be7a4944fd25b3a8b20c2820fbd1c3c4c826ebe69ac4f155979473c6e",
             "Completed final gate receipt")
    gate = json.loads(raw)
    read = ev.retained_map(
        OUT / "final-gate-20261031T233546260787Z/inputs.json",
        "31523d876f0443867d30fcbfab3620d77e9577811db92c207cab324d373c7b15",
    )
    ev.check(not gate["problems"] and gate["audit_completed_without_findings"],
             "Parent numerical audit succeeded")
    joined = {(r["opponent"], r["scenario"], r["candidate_side"]): r
              for r in gate["joined_conditions"]}
    cache, base, all_rows, pool_results = {}, {}, [], {}
    conflicts, duplicates, candidate_specs, worse_rows = [], [], collections.Counter(), []
    for pool, references in gate["base_membership_refs"].items():
        table, refs = {}, {}
        for item in references:
            key, ref = tuple(item["condition"]), item["ref"]
            if ref["path"] not in cache:
                cache[ref["path"]] = rows(read(ref["path"]))
            row = cache[ref["path"]][ref["line"] - 1]
            candidate, actual, value = normalize(row)
            ev.check(actual == key and value is not None and row_metadata_ok(row),
                     f"Base exact condition/metadata {pool}:{ref['line']}")
            ev.check(key not in table, f"Unique base key {pool}:{ref['line']}")
            if value is None:
                continue
            table[key], refs[key] = value, dict(ref, candidate=candidate)
            candidate_specs[candidate] += 1
            all_rows.append(row)
            if key in base:
                record = {"condition": list(key), "earlier": list(base[key]),
                          "later": list(value), "pool": pool, "ref": refs[key]}
                (duplicates if base[key] == value else conflicts).append(record)
            else:
                base[key] = value
        keys = set(table)
        ev.check(keys == {tuple(k) for k in gate["pool_tables"][pool]["conditions"]},
                 "Exact pool keys " + pool)
        comparison = {}
        for tag in ("af5", "g1", "v29"):
            values = {key: tuple(joined[key]["values"][tag]) for key in keys}
            comparison[tag] = {
                "wdl": wdl(values, keys),
                "worse_than_base": sum(values[k][0] < table[k][0] for k in keys),
                "better_than_base": sum(values[k][0] > table[k][0] for k in keys),
                "same_outcome": sum(values[k][0] == table[k][0] for k in keys),
            }
        pool_results[pool] = {
            "conditions": len(keys), "base_wdl": wdl(table, keys),
            "comparisons": comparison,
        }
        for key in sorted(keys):
            if joined[key]["values"]["af5"][0] < table[key][0]:
                worse_rows.append({
                    "pool": pool, "condition": list(key), "base": list(table[key]),
                    "af5": joined[key]["values"]["af5"], "base_ref": refs[key],
                    "af5_ref": joined[key]["refs"]["af5"],
                })
    errors = error_counts(all_rows)
    ev.check(not any(errors.values()), "Base rows report errors")
    ev.check(not conflicts, "Conflicting base observations across pool memberships")
    ev.check(len(base) == 804 and len(all_rows) == 846, "Base denominators")
    membership = {
        "base_wdl": [sum(row["base_wdl"][i] for row in pool_results.values())
                     for i in range(3)],
        "comparisons": {
            tag: {
                "wdl": [sum(row["comparisons"][tag]["wdl"][i]
                            for row in pool_results.values()) for i in range(3)],
                "worse_than_base": sum(row["comparisons"][tag]["worse_than_base"]
                                       for row in pool_results.values()),
                "better_than_base": sum(row["comparisons"][tag]["better_than_base"]
                                        for row in pool_results.values()),
            } for tag in ("af5", "g1", "v29")
        },
    }
    valid_counts = not ev.problems
    count_problem_count = len(ev.problems)
    source_report = ev.source_checks(all_rows)
    source_findings = ev.problems[count_problem_count:]
    return {
        "status": "COUNTS_VERIFIED" if valid_counts else "COUNT_AUDIT_FINDINGS",
        "count_reduction_valid": valid_counts,
        "all_reported_sources_match_captured_current_bytes": not source_findings,
        "current_source_comparison_findings": source_findings,
        "base_candidate_spec_memberships": dict(candidate_specs),
        "pool_results": pool_results, "membership_totals": membership,
        "unique_base_wdl": wdl(base, set(base)),
        "unique_conditions": len(base), "pool_memberships": len(all_rows),
        "duplicate_memberships": duplicates, "conflicts": conflicts,
        "base_errors": errors, "sources": source_report,
        "af5_worse_than_base_memberships": worse_rows,
        "af5_worse_distinct_conditions": len({tuple(row["condition"]) for row in worse_rows}),
        "af5_worse_distinct_specs": len({row["condition"][0] for row in worse_rows}),
        "identity_scope": (
            "The exact historical R13 base files include frozen best_v9e and explicit "
            "lead.v18/lead.v19 specifications. This reduction authenticates their retained "
            "records and reports current-source comparisons; it does not newly prove "
            "their behavioral equivalence to one current best_v9e entrypoint."
        ),
        "denominator_scope": (
            "Membership totals count overlapping pools repeatedly. They are not 846 "
            "distinct games. The af5 versus g1 recommendation does not require this "
            "historical-base identity equivalence."
        ),
    }


if __name__ == "__main__":
    evidence = Evidence("historical-base", __file__)
    try:
        result = main(evidence)
    except Exception as error:
        evidence.check(False, type(error).__name__ + ": " + str(error))
        result = {"status": "INCOMPLETE_REVIEW", "count_reduction_valid": False,
                  "error_type": type(error).__name__}
    print(json.dumps(evidence.seal(result) | {
        key: result.get(key) for key in (
            "status", "count_reduction_valid", "membership_totals",
            "unique_base_wdl", "af5_worse_distinct_conditions", "af5_worse_distinct_specs",
            "all_reported_sources_match_captured_current_bytes",
        )
    }, indent=2))
