# Verification record

Checked at 2026-10-28T01:29:05Z.

Run `python3 code/check_direction_maximum.py` from the artifacts root. The program uses exact rational arithmetic to check the finite moment identity for n=1,...,50 and SymPy polynomial arithmetic to check the Jacobi identities for n=1,...,12. It then uses Arb at 160 bits to sum 50000 Fourier terms. Since 0<P_n<=3/5 and |cos(2n phi)-(-1)^n|<=2, the omitted tail is bounded by 1/(5 pi N^2). These checks corroborate the analytic proof; they do not replace its all-n argument.

The axis finite part agrees with the independent direct geometric quadrature in code/explore_finite_part.py. Results are in data/direction_maximum_checks.json.
