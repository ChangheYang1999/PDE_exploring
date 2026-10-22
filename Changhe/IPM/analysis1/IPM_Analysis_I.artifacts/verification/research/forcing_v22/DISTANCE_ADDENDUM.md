# A negative lower endpoint for a nonnegative distance

Written 2026-10-21T09:49:34.300021+00:00 before changing the assertion.
The first full-polynomial check of rows19000 through24999 stopped before
writing its output at row20999. Its dmin is exactly -2^(-1074), and its
dmax is3706595488910857/9223372036854775808<231/8000. This row is inside.
The distance itself is nonnegative, but a valid outward enclosure of a
distance may have a negative lower endpoint. Requiring dmin>=0 was an
unnecessary assertion in the verifier, not a hypothesis of the cutoff
proof or a defect in this data row. This is the only negative dmin in
all43949 rows. The failed command and offending data are retained.

Replace that assertion by dmin<=dmax, dmax>=0, dmin<r_out. The physical
distance is in[max(0,dmin),dmax]. The inside branch gives exactly tau=1
and vanishing first four derivatives. On a nonconstant row the formulas
already use max(0,(dmin-r_in)/h) and max(dmin,r_in), so their bounds are
unchanged by clipping the distance below at zero. No estimate is weakened.

The previous source is retained as check_cutoff_exact_nonnegative_d0.py.
The only source change is the assertion just described. The four completed
chunks covering rows0 through18999 remain valid with the stronger original
assertion. Remaining chunks will use the amended assertion; the final
audit checks the exact source difference and complete row coverage.
