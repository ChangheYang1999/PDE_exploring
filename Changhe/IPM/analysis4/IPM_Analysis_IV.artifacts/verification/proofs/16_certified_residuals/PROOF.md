# Certified finite residuals from an independent Cartesian implementation

## Statement and parameters

Use exactly

\[
c=4076476460239181/2251799813685248,\quad
\delta=1824676646553933/4076476460239181,\quad
\gamma=1-\delta,
\]

and f_1(theta)=sin(theta). These are the stored rational parameter and a single-mode leading profile, not Candidate 007's ten-mode density. Let rho_N, psi_N, chi_N be the first N terms of the unique nonresonant pure recursion. Let

\[
\mathcal R_N=(cX+u_N)\cdot\nabla\rho_N-\rho_N,
\qquad u_N=(-\partial_y\psi_N,\partial_x\psi_N).
\]

The following strict bounds are certified on the indicated circle r=R:

| N | R | Lower bound for $\sup_\theta|R^{-\gamma}\mathcal R_N|$ | Upper bound |
|---:|---:|---:|---:|
| 10 | 1 | 2.3629e-5 | 2.4340e-5 |
| 10 | 2 | 1.0920e-6 | 1.1249e-6 |
| 10 | 4 | 5.0055e-8 | 5.1558e-8 |
| 10 | 8 | 2.2818e-9 | 2.3503e-9 |
| 20 | 1 | 6.7799e-9 | 7.1880e-9 |
| 20 | 2 | 1.4081e-11 | 1.4931e-11 |
| 20 | 4 | 2.9011e-14 | 3.0762e-14 |
| 20 | 8 | 5.9416e-17 | 6.3003e-17 |

The machine-readable certificate also encloses its first angular derivative, R^(1-gamma) times each Cartesian derivative, and R^(-gamma)(rho_{N+1}-rho_N). These are finite-order statements. In particular, they do not prove convergence of the infinite series at this rational parameter, or a uniform exterior bound from only one circle.

## Independent recurrence and interval induction

The program `../../code/cartesian_arb_residuals.py` stores a homogeneous field as an exact rational radial exponent and complex Fourier coefficients enclosed by Arb balls at 512-bit precision. It implements the two Cartesian derivatives directly. For a mode r^q exp(ik theta), these derivatives shift frequency by plus or minus one, with coefficients (q-k)/2 and (q+k)/2 and the corresponding factors of i for the y derivative. Products are ordinary finite convolution.

Starting from the exact leading sine, it computes every next density by the ordered Cartesian products u_i dot grad rho_j. The stream follows from the Cartesian x derivative of that density and the exact nonzero Poisson divisors. The potential is independently reconstructed by descending substitution through the exact Cartesian potential-to-density basis. Velocity for the next order is then differentiated from that potential.

All parameters entering the divisions are exact rational numbers, and all relevant divisors are nonzero through order 21. Arb's inclusion arithmetic therefore propagates enclosures of the exact formal coefficients by induction. S1 symmetry and finite support, proved in topic 01, justify projection to the correct Fourier modes; a numerical ball containing zero is used only as a consistency check, not as a proof that an unwanted mode vanishes. The same distinction applies to the recomputed zero residual checks.

At each of the 21 orders, the program independently checks enclosure consistency of the original potential identities, the Poisson equation and the stationary coefficient. All coefficient balls are retained as exact dyadic midpoint and radius data in `verification/reference_sin_residuals_coefficients.json`. The summary includes its SHA256 and both implementation hashes.

## The actual residual

The recurrence cancels every stationary coefficient through N identically. Consequently the actual residual of the finite potential is exactly

\[
\mathcal R_N(r,\theta)=\sum_{n=N+1}^{2N}r^{1-n\delta}E_n(\theta),\qquad
E_n(\theta)=\sum_{i+j=n,\ i,j\le N}(u_i\cdot\nabla\rho_j)(1,\theta)
\]

where each homogeneous pair is evaluated on the unit circle to extract its angular coefficient. The code constructs those coefficients from Cartesian fields, then multiplies by z^(n-1), z=R^(-delta), to obtain R^(-gamma) mathcal R_N. No fitted velocity is introduced. The first remaining coefficient also passes the independent identity E_{N+1}=N(c-1)f_{N+1}.

First angular derivatives multiply mode k by ik. Weighted first Cartesian derivatives use the same Cartesian operators before the radial evaluation. Each quantity is thus an explicitly enclosed finite real trigonometric polynomial.

## From a grid to a rigorous supremum bound

For a real trigonometric polynomial h(theta)=c_0+2 Re sum_{k>=1}c_k exp(ik theta), coefficient enclosures give

\[
\|h'\|_\infty\le D:=2\sum_{k\ge1} k|c_k|.
\]

Evaluate h with interval arithmetic at the M=2048 equally spaced points on the full circle. Every angle is within pi/M of one grid point. Hence

\[
\max_j |h(2\pi j/M)|\le\|h\|_\infty
\le\max_j |h(2\pi j/M)|+\pi D/M.
\]

Taking lower endpoints for the left bound and upper endpoints for the right bound proves the enclosure. All trigonometric evaluation, coefficient norms and the correction use Arb arithmetic. The displayed decimal endpoints are checked strictly outside the corresponding certified interval bounds by `../../code/certified_residual_table.py`.

## Comparison with the numerical experiments

`../../code/residual_comparison.py` compares all density and stream coefficient enclosures through order 21 with the retained numerical checkpoint subset. It also reproduces the numerical report's original angular grids for N=10 and N=20. That report used an older product routine which retained one trailing zero sine coefficient; its grid sizes are 512 and 664. The current routine drops that zero and would use 648 points at N=20, so blindly applying the current grid does not reproduce the old sampled maximum.

The numerical values are sampled maxima, and the implementation's description of Arb spot checks is not supported by its evaluation code. The full-circle bounds above are separate validated computations. The comparison inflates legacy checkpoint radii printed to ten significant decimal digits by a factor 1+1e-9 to dominate their possible decimal rounding loss.

## Dependencies and scope

The exact mathematical ingredients are topic 01's Cartesian identities, pure recurrence, support and generic potential invertibility, plus the elementary grid Lipschitz bound. The numerical dependency is python-flint's Arb inclusion arithmetic. This is validated computation with retained coefficients and implementation hashes, not a formal proof-assistant certificate or an infinite-series convergence result.
