# Scope clarification for the common selection cutoff

Recorded 2026-10-30T05:37:50.911728+00:00, before final selection or entropy.

The qualified common driver checks the declared selected_at_utc against 2026-10-30T12:23:31Z. It does not establish when a producer record actually cleared, and load_preparation does not check prepared_utc against the cutoff. The sentence in COMMON_ORCHESTRATION_v1.md saying that a late-clearing endpoint is refused therefore states an intended selection requirement, not an independently implemented provenance guard.

Before sealing the actual preparation, the verifier must capture and check each selected endpoint's checkpoint, end record, admitted wrapper decision, reference bindings and actual clearance evidence. The lead's branch-selection rule, including P1's special replacement test and exclusion inheritance for continuations, must be checked then. Selection and immutable preparation must both actually occur by the cutoff; neither may be backdated. If a later endpoint is not eligible at that time, use the eligible endpoint chosen under the registered rule or leave the slot OPEN.

This is a limitation of automatic admission, not a change of the cutoff, scientific thresholds or planned state convention. The fixture in artifacts/common_selection_scope_v1/audit.json uses labelled simulated future times; its execution time is the real date above. No final candidate or entropy is produced.
