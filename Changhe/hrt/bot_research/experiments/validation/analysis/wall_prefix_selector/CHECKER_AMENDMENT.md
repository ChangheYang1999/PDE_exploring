# Before-call checker amendment

Recorded 2026-10-31T21:05:51.328513+00:00. No O decision or new game has run. The original185-pin declaration and checker remain unchanged.

Source inspection found that protocol151's value serializer, reused by the new checker, supports functions and dataclasses but not arbitrary nested policy objects or bound methods. L contains PersistentFactoryModel, whose bound H policy has its own state. Calling the original state comparison would therefore reject valid data. This is a checker-domain gap identified before execution, not an observed strategy failure.

The version-two checker uses policy_value_snapshot.py. Its canonical values include dictionaries, ordered sequences, sets, dataclasses, function defaults and closure values, bound method functions and owners, and all instance fields of local policy/engine objects. Unsupported types and cycles fail closed. Shared module globals, alias identity and process clocks remain outside scope. Equality means equality of these logical value trees, not Python object identity or a universal environmental-state equivalence.

Fixtures instantiate fresh O objects without decision calls. Corresponding G and L initial logical state trees match. Changing L's nested model round or its bound H owner's switched field, or G's trace, changes the result. A cyclic list is rejected. The exact expected input shapes and per-round action/state requirements are unchanged. This amendment pins the new serializer and version-two checker before any game. The original game manifests still pin O, its full source/data closure and the initial method; the amendment supplements the independent checker. No rule, opponent, hypothesis, game source, final candidate orD input changes.
