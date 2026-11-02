# Verification evidence

The informal proof was written before the component check. The check
`experiments/validation/check_prefixed_v4.py` ran on four published development
openings, both player assignments, through round five. It compared the actual
opening wrapper with the existing lead `TimedBot` adapter, checked that the
target and its separate model each advance once per round, compared every
forecast with the submitted target actions, and required every action to be
accepted by the original engine.

`runs/validation/prefixed-v4-components-001.json` records all eight prefixes and
40 rounds passing at 2026-10-31T08:13:51.075875+00:00, runtime 5.055935 seconds.
The matching log retains progress; the receipt includes source hashes. These
are component checks, not completed games. Full-game evidence will be linked
only after strict accounting and original-engine replay audits.

Reproduction from the project root with the prescribed execution environment:

    .venv/bin/python -B -m bot_research.experiments.validation.check_prefixed_v4 --output bot_research/runs/validation/prefixed-v4-components-NEW.json
