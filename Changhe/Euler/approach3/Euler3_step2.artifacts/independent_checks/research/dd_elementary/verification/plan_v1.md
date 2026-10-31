Registered 2026-10-29, before running this audit. Read actual execution timestamp from the result.

Capture dd_elementary.py and bind the frozen exact_matmul/fields_dd dependencies. Compare its returned pairs against 90-digit mpmath at exact binary64 h+l. Sample exponential inputs over [-700,700], trigonometric inputs over [-4096,4096], random low words, reduction boundaries and neighboring binary64 values. Include zero and very small arguments. Store all inputs, output words, reference decimal strings and errors.

Report the source's stated 1e-29 relative exponential and absolute sine/cosine self-test threshold without modifying it after results. Separately report exponential relative errors on outputs at least 1e-290 and relative errors on smaller outputs; this distinction does not turn a failed blanket claim into a pass. A finite sample is not an enclosure. Actual pressure-table argument coverage is a separate audit, to be bound to the final table code and the two named cases.
