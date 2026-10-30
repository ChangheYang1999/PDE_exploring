# Exact potential rank at radii 25 and 50

## Statement and hypotheses

Fix c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma,
p_j=(3+gamma-j delta)/2, S=1+r^2, t=r^2/S, v=1/S, and
H_m=Re(x+iy)^(2m). The old potential space V has dimension 1922, with the
exact selected generator shapes in ../optimizer_quotient_audit/source/
N1_013_quot_exact.json. Its complete independence proof and exact quotient
identities are in ../optimizer_quotient_audit/PROOF.md. Its elements are
finite sums H_m S^(p_j-m) P_jm(t), with polynomial P_jm and j=0,...,7.

For either R=25 or R=50, adjoin the 252 potentials

 G_jmN=H_m S^(p_j-m) [R^2/(R^2+r^2)]^4
                         P_N(2r^2/(R^2+r^2)-1),
 j=1,2,3, m=9,...,15, N=0,...,11,

where P_N is the Legendre polynomial normalized by P_N(1)=1.
The resulting potential space has dimension 2174. The actual generator
shapes of candidate 016, respectively 017, are exactly these two bases.
Their fitted coefficients do not enter this rank statement. The new
density generators -partial_y Delta G have Fourier support contained in
{17,19,...,31}, and the family has a nonzero mode 17 generator.

This theorem concerns potential rank and a density frequency witness.
Density injectivity is the separate T4-322 theorem awaiting Opus review.
No PDE inverse, coercivity constant, lower singular-value bound, optimizer
minimum or stationarity follows from the present theorem.

## Complete proof of potential independence

Angular orthogonality separates m. For fixed m a potential relation is
sum_j v^(-p_j) Q_j(v)=0, where each Q_j is rational and analytic at v=0.
For distinct j,k in {0,...,7}, p_j-p_k=(k-j)delta/2 is noninteger, as
verified in exact arithmetic for all 28 pairs. If some Q_j is nonzero,
its Taylor series has a finite least power v^e_j with integer e_j>=0.
The numbers e_j-p_j are distinct. Dividing by their unique least power
and taking v down to zero leaves a single nonzero coefficient, a
contradiction. Thus all rational Q_j vanish separately.

In one fixed block (j,m), put a=R^2-1>0 and L=1+a v. The new factor is

 A_mN(v)=R^8 (1-v)^m v^4 P_N(2(1-v)/L-1)/L^4.

At v0=-1/a, t0=1-v0=R^2/a is nonzero. The leading coefficient of P_N
is 2^(-N) binom(2N,N). Hence the pole of A_mN has order 4+N and its
Laurent coefficient is

 C_mN=R^8 v0^4 binom(2N,N) t0^(m+N) / a^(4+N),

which is nonzero. Lower polynomial terms have strictly smaller pole
order. In a nonzero relation, the new term with largest N has a pole
that no smaller N or old polynomial factor can cancel. Descending in N
eliminates all new coefficients; the independently proved old basis has
no remaining relation. This argument applies to both positive values
of a, proving dimension 1922+3*7*12=2174. The auxiliary negative pole is
used only in a rational identity. No noninteger physical prefactor is
analytically continued through that pole.

## Density frequency witness

The Laplacian preserves angular frequency cos(2m theta); -partial_y maps
it into sine frequencies 2m-1 and 2m+1. For the unit generator with
j=1,m=9,N=0, expand at the origin:

 G=H_9 [1+(p_1-9-4/R^2)r^2+O(r^4)].

Since Delta H_9=0, Delta(r^2 H_9)=4*19 H_9 and
-partial_y H_9=18 Im(x+iy)^17, its first density term is

 4*19*18*(p_1-9-4/R^2) Im(x+iy)^17.

This rational coefficient is nonzero for both radii. The checker also
recovers it from an independent Cartesian rational-field differentiation
of the single exact generator. This proves occurrence in the basis; it
does not assert nonzero total mode 17 in every fitted coefficient vector.

## Independent verification

The own finite calculation builds the Legendre factors by their three-term
recurrence, obtains the exact numerator at v0 and checks the formula for
all 84 pairs (m,N) at each radius. The peer uses Rodrigues' formula and a
different substituted polynomial construction. Compare every Laurent
coefficient, all old and new generator shapes, all branch exponents and
the explicit density witness. Recheck the old 1922-dimensional basis
certificate and all of its source hashes. Freeze the peer result, proof,
code and referenced data, and compare its R25 witnesses with N4-248.
The present comparison executes only own code. Exact JSON witnesses and
all dependency hashes are retained alongside this proof.
