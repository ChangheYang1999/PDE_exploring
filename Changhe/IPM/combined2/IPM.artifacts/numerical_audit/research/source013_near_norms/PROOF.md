# Whole-plane near norms and Fourier-moment inputs

This argument is written before the consumer. It applies the accepted complete-cover theorem in ../source013_near_cover/PROOF.md and NR-25 of the theory team's THEORY_NEW_RESULTS.md. It does not reopen those results or assert that the required numerical blocks are complete.

## Exact statement and hypotheses

Fix c = 4076476460239181/2251799813685248, Candidate 007 and correction C2-N1-013 with the exact source identity in ../source013_near_source/PROOF.md. Write psi = partial_y chi_007 + phi_013, u = (-partial_xy psi, partial_xx psi), and

    g(X) = (4 u(X).X - c)/(1 + 4 |X|^2),
    L = log(8)/(2 sqrt(pi)), R_c = sqrt(8),
    a(X) = g(X) erfc(log(|X|/R_c)/L)/2 for X != 0,
    a(0) = g(0).

The admitted source and complete-cover theorem show that a is Schwartz. Let L4 = Delta^2, L5 = grad Delta^2 and L6 = Delta^3. In the order5 energy, sum the two component squares. Let P be the fixed 561-panel partition of [1/4096,10000] in the actual near deployment manifest. For i = 0,...,4, block n_i consists exactly of indices congruent to i modulo5. Its size is respectively 113,112,112,112,112.

Assume the following evidence, with the same source and cutoff throughout.

1. Every block has its complete admitted result under ../source013_near_admission/CHUNK_PROOF_v01.md, a successful matching finite execution receipt, and an independently adopted actual-result review. All actual chunk records and their successful receipts, original owner installation, complete owner result and successful owner receipt remain authenticated dependencies. Each block's original source-to-coefficient containment and complete source-majorant premises remain explicit.
2. The origin result and its independent actual review enclose the three L_j energies on |X| <= 1/4096. The exterior result and its independent actual review enclose them on |X| >= 10000. Both records include their primary identities, containing intersections, exact geometry and successful applicable execution evidence. The failed larger origin requests remain failed; only their explicitly reviewed completed primary stage may be reused.
3. All five block assignments exhaust P exactly once, every interval endpoint matches the accepted partition, and the two endpoint radii agree. Every interval is nonnegative and rational. Each result, method, review and execution is checked against the bytes and SHA256 bound in the actual application request, with no reliance on a mutable status note.

For j = 4,5,6 let E_j^- and E_j^+ be the sums of all seven regional lower and upper endpoints. Define the full ordered Cartesian tensor norm

    D_j = ||D^j a||_2,
    |D^j a(X)|^2 = sum_(i_1,...,i_j in {1,2})
                    |partial_(i_1)...partial_(i_j) a(X)|^2.

Then E_j^- <= D_j^2 <= E_j^+. For any exact outward decimal endpoints d_j^- and d_j^+ satisfying

    0 <= d_j^- <= d_j^+,
    (d_j^-)^2 <= E_j^- <= E_j^+ <= (d_j^+)^2,

one has d_j^- <= D_j <= d_j^+. These are whole-plane norms; no individual block is identified with a regional Cartesian tensor energy.

Use the nonunitary Fourier transform a_hat(zeta) = integral exp(-i X.zeta) a(X) dX, and define

    M4(a) = (2 pi)^(-2) integral |zeta|^4 |a_hat(zeta)| d zeta,
    T_p(a;v) = (2 pi)^(-2) integral_(|zeta|>v)
                              |zeta|^p |a_hat(zeta)| d zeta.

This normalization is exactly NR-25. It represents the same D_j as the unitary convention used by the regional theorem. If 0 < pi_- <= pi is a containing lower endpoint, then

    M4(a)^2 <= min((d_4^+ d_6^+ + (d_5^+)^2)/(2 pi_-),
                  d_4^+ d_6^+/pi_-).

For p = 21/10, every v > 0 and m in {4,5,6}, put

    H_m(v) = (E_m^+ / (4 pi_- (m - 31/10)))^5
             * v^(31 - 10m).

This is a nonnegative rational for rational v and pi_-. Then

    T_(21/10)(a;v)^10 <= H_m(v).

Consequently any nonnegative rational t_m with t_m^10 >= H_m(v) is a containing upper, and min_(m=4,5,6) t_m is also a containing upper. Evaluate the two exact thresholds v = mu/2 and v = 3mu/4 for the explicitly requested rational values of mu. This produces Fourier-tail inputs, not a complete near price or an invariant-ball inequality.

## Application of the accepted theorems

The five residue classes partition the complete middle annulus. The origin disk, middle annulus and infinite exterior cover the plane up to circles of area zero. The complete-cover theorem therefore gives the bounds E_j^- <= D_j^2 <= E_j^+. The exact square comparisons and monotonicity of the nonnegative square root give the norm bounds. No local integration-by-parts identity is used.

NR-25(iii) gives M4(a)^2 <= (D4 D6 + D5^2)/(2 pi) and <= D4 D6/pi. Both expressions increase with every displayed derivative norm and decrease with pi. Substitution gives the claimed two rational upper bounds. The formula remains valid when a derivative norm is zero: the s=2 inequality of NR-25(ii), followed by V tending to zero or infinity, gives the same zero bound. Equivalently, vanishing D4 or D6 for a Schwartz function implies a_hat = 0 almost everywhere off the measure-zero origin, so a = 0.

NR-25(i) applies because m > 31/10 for each m in {4,5,6}. Squaring its upper bound, replacing D_m^2 by E_m^+ and pi by pi_-, and then taking the fifth power gives H_m(v). The exponent is exactly 10(p+1-m) = 31-10m, an integer. All replacements preserve the inequality because the quantities are nonnegative and pi_- is positive. The tenth-power comparison is therefore entirely rational; no fractional-power floating evaluation is required. Taking the minimum of three separately valid uppers preserves validity.

## Exact display and execution checks

For a nonnegative rational x, a decimal grid of step 10^(-d), and an integer n >= 2, let k be the largest integer with k^n <= floor(x * 10^(nd)). Then k/10^d <= x^(1/n) < (k+1)/10^d. Integer root bracketing and the defining power comparisons are checked explicitly. Norm lower endpoints may be moved down one grid step when equality occurs; upper endpoints use k+1. This proves every displayed square or tenth-power bound, including exact powers and zero. A containing interval for pi is produced with the already used ball-arithmetic backend and its positive exact lower endpoint is retained. Synthetic fixtures test the arithmetic and malformed evidence; they cannot supply physical energies.

The consumer must reject missing, duplicated or reordered blocks, a wrong source or cutoff, a changed accepted plan, incorrect endpoint radii, absent actual reviews, unsuccessful receipts, inconsistent exact block totals, and changed dependency bytes. It verifies the complete original block manifests and their archived chunk records through the already accepted admission contract. It rehashes immutable inputs after reading. All outputs and any temporary copied metadata stay in this agent, and every published path is relative.

One finite application is run only through the accepted one-child execution gate, on core50, nice19 and one thread. No JavaScript/TypeScript, servers or listeners, RLScience or other clusters, remote or paid compute, GPU, Lean/Lake, foreign writes or signals, commits, pushes or online posts are authorized. Preparation and actual execution are distinct review stages. A timeout or failed check remains recorded and gives no admitted whole-plane value.

## Dependencies and scope

The exact-source, local energy and complete-cover premises are in ../source013_near_source/PROOF.md, ../source013_near_cover/PROOF.md and its APPLICATION_PROOF_v01.md, ../source013_near_endpoints/PROOF.md and CORRELATED_EXTERIOR_PROOF_v01.md, and ../source013_near_admission/PROOF.md and CHUNK_PROOF_v01.md. Fourier moments use the already accepted NR-25, audited in AT-890 to AT-892. Execution uses the separately accepted finite preparation gates.

This is a conditional application theorem. Until all seven regional records and their actual reviews are present, the whole-plane near energies, M4 and Fourier tails remain OPEN. Even completed moment inputs do not establish the other near estimates, global background inequalities, far constants, full inverse, invariant ball or stationary existence theorem.
