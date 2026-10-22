# Independent-check variable repair

The first full independent checker passed its per-column, per-vector and interval tests but failed the final aggregate comparison because the top-level loop variable a had overwritten the producer dictionary. No output_audit.json was written. The original check.py and failure record are retained. check_v2.py changes the producer object name and its dictionary references only. A fresh complete run is required; no earlier unfinished run is accepted. This change has no effect on the exact arithmetic or scope.
