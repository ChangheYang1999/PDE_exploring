# Offline refit review

Registered 2026-10-29T21:40:24.048252+00:00, before running the controls. Capture the current producer transfer.fit_field, TailConstraints and refit_start source bytes. Use only selected definitions, with CPU tensors and explicit small fixture models, so no production worker or GPU is launched.

Check the reported zero-parameter failure in actual TailConstraints.expand with a degree-six mode layout. At valid fixed parameters check zero maps to zero coefficients, the parameter entries are unchanged, the fixed/free layouts agree, and coefficient linearity has relative error <=2e-13. Test actual fit_field on a manufactured finite-dimensional field with the proposed fixed-parameter expansion; require exact vector layout and relative field error <=2e-12. Deliberately return the parameter entries twice and require the layout control to fail. These are implementation controls, not a complete qualification of an actual fitted campaign start.

The lead 21:39:31 self-refit control remains necessary. Actual source/output files, post-gauge starts, parameter history and per-shell accuracy are checked separately when available. No JavaScript/TypeScript, servers/listeners, RLScience, remote compute or other-side writes. One CPU35 computation at low priority, with all numerical libraries restricted to one thread.
