# Quantitative estimates for the explicit higher-tail family

The exact statement, hypotheses and complete argument are in PROOF.md with
the mandatory ADDENDUM.md. Decimal claims require the current audit and final
review status. The two interval calculations and exact finite audit give:

| Quantity | Strict lower bound | Strict upper bound |
| --- | --- | --- |
| N2 | 108584.7279007 | 108584.7279010 |
| Nd | 1155559.679343 | 1155559.679346 |
| I2 | -172.0576928134 | -172.0576928131 |
| Id | 13733.56284156 | 13733.56284159 |
| C2 | 947.4716170716 | 947.4716170719 |
| Cd | 11225.91941794 | 11225.91941797 |

Here N2 and Nd are the sums of absolute cosine quotient coefficients;
I2 and Id are the sine-three coefficients. These are physical coefficients,
not boundary-scaled ones. For the exact topic106 family, the weighted factor
distance is at most

 .334616 T^(k-1) + 947.4716170719 T^(2k-2) + 11225.91941797 T^(-2).

This holds for every T>=max(R_b,L,1), with the fixed polynomial cutoff and
exact strain compensator. At T=10^4 the bound is below0.0005447363944098;
at T=10^6 it is below0.000004133363097054; at T=10^8 it is below
0.00000009115298566241. These are upper bounds, not measured distances.

On the disk of radius9, at T=10^4 the component bounds for velocity and
its derivatives of orders0,1,2,3 are respectively below
3.200333635869e-10, 1.303839629429e-10, 4.565633719208e-11,
and1.599922927245e-11. Every larger T obeys the same bounds.
The exact source certificate and density agreement imply
|partial_y F(rho_T,c0)(P)|>3.69e-7 for every T>=10^4.
P is the original source; it is not asserted to remain a source after repair.

The rough bounds at T=3000 do not meet the sufficient1e-8 source-jet test.
This does not assert failure of that test for the actual jets. No conclusion
for the interval R_b<=T<10^4 follows from these coarse constants alone.

All783 sine coefficients and782 quotient coefficients of H2 were computed,
with no angular truncation. Arb512 and iv180 used different source forms,
scalings, convolution arithmetic and quotient inversions. Exact audits tested
source equality, all quotient basis vectors, Fourier supports and signs,
normalization, inherited bounds, and strict public rounding. Interval overlap
is only a diagnostic. A rational Taylor bound independently checked
3412.96685816<R_b<3412.96685817.

The trial remains C4 at its center. The local residual-convergence argument
uses only C3 there. Center C6 was an overstatement in the earlier proof text
and is corrected by ADDENDUM.md.

This is an estimate and nonstationarity result for a specified family.
There is no global residual norm ceiling, inverse, neighborhood exclusion,
existence theorem, or decisive endpoint for the IPM task.
