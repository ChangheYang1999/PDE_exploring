# Local families around automatically compatible high harmonics

Status: PROVED after the independent review of17:52Z and admissionV511. The center hypothesis is required; no general response claim is made for every pair (h,Q).

## Statement

Let h>=2 and Q>2h be coprime positive integers with Q odd. Set delta=2h/Q, c=Q/(Q-2h) and M=Q+2h-2. Fix a finite set J of positive odd integers containing1. For real parameter vectors a=(a_j)_(j in J), put

    f_1(theta;a)=sum_(j in J) a_j sin(M j theta),
    a^0_1=1, a^0_j=0 for j!=1.

For the zero-gauge low-order recurrence and the unit homogeneous stream perturbation at orderQk, let sigma_k(a) be the affine response of the orderQ(k+1) compatibility coefficient. Assume

    s_0=inf_(k>=1)|sigma_k(a^0)|>0.

Then an open neighborhood U of a^0 in R^J and a finite R exist such that, for every a in U, there is a unique compatible tuned density and stream series with this leading profile. These series and a common potential converge on r>=R with every appropriately weighted derivative. Their coefficients and their sums on any slightly larger strict exterior depend real analytically on a. The leading profile and the exterior solution change sign. If h>=3 the potential is a pure-power series. If h=2 the potential may require its single orderQ logarithmic correction.

The neighborhood and radius are qualitative. This is openness in the stated fixed finite-dimensional lattice space, at a fixed delta. It does not assert openness in all odd sine profiles or under perturbation of delta. The center radius certificate is not automatically a radius certificate for the whole neighborhood.

## Automatic first compatibility

Let Lambda={plus or minus Mj : j in J}. Before the first resonance the signed-support induction gives

    supp f_n subset n Lambda+E_(n-1),
    E_l={-l,-l+2,...,l}, 1<=n<=Q.

Every element of Q Lambda is M times a sum of Q odd integers. This sum is odd and nonzero, so its modulus is at least1. Each frequency in Q Lambda+E_(Q-1) consequently has modulus at least

    M-(Q-1)=2h-1.

The first compatibility frequency is2h-3, strictly smaller. Its coefficient vanishes identically for every real or complex vector a. Thus compatibility imposes no additional equation on this lattice subspace. This argument bounds the entire possible support and does not use numerical cancellation.

## A uniform bound for every later response

Set B=M max J+1, a fixed even bandwidth bound. The coefficients through f_Q are homogeneous polynomials in a: their nonresonant divisors are fixed and nonzero, and the earlier stream orders contain no free harmonics. By the affine-response and compact-response theorems144 and149, every sigma_k(a) is a polynomial in a and

    sigma_k(a) -> sigma_infinity(a)

locally uniformly on finite complex parameter sets. To see the uniformity directly, use the compact response formula for k large enough that2hk-2>=BQ. This formula consists of finitely many additions, products and divisions involving the low coefficients and t_k=1/(2hk-2). Its denominators are independent of a and nonzero near t=0. On a fixed compact parameter set it is therefore jointly continuous in (t,a), and its limit at t=0 is a polynomial in a. Only finitely many indices precede this formula.

The assumed center bound gives |sigma_infinity(a^0)|>=s_0. Choose a small closed complex polydisk P centered at a^0 on which |sigma_infinity(a)|>=3s_0/4. Local uniform convergence gives K such that the difference from this limit is less than s_0/4 for every a in P and k>=K. Hence all these tail responses have modulus at least s_0/2. Shrink P to control the finitely many continuous functions sigma_k with k<K by the same lower bound. We have proved

    inf_(a in P,k>=1)|sigma_k(a)|>=s_0/2.

Pointwise continuity of the infinitely many responses alone would not prove this step. The locally uniform limit is essential.

## Tuning, convergence and parameter dependence

Tune each homogeneous stream coefficient successively using H_(Qk)=-R_k/sigma_k(a), where R_k is the compatibility residual with that new harmonic set to zero. The affine-response theorem, the automatic first compatibility and the uniform nonzero responses give existence and uniqueness of every coefficient. All these coefficients are holomorphic on the interior of P.

The leading Fourier norm is uniformly bounded on P. Its support has the fixed bound B, and all responses have the same lower bound s_0/2. The proof of the nonnegative majorant theorem145 applies with these common constants: it uses absolute values and triangle inequalities, which also hold for the complex coefficients. Its single geometric bound therefore controls every parameter in P. Choose R strictly beyond that bound. Each fixed weighted derivative multiplies coefficients by only a polynomial in the order and frequency, so the strict geometric ratio gives uniform convergence for every such derivative. One fixed strict R suffices, with derivative-dependent constants.

Uniform convergence on smaller parameter polydisks gives holomorphic dependence of each sum. Restriction to the real parameters gives the stated real analytic dependence. Absolute convergence of the products and the common-potential reconstruction justify the stationary IPM identities term by term. When h>=3 there is no exceptional common-potential exponent at an integer order. When h=2 the reconstruction permits the single finite logarithmic correction at orderQ. Its coefficient can vanish; this theorem does not claim otherwise. The special nonvanishing assertion for h2,Q9 is proved separately in228 and229.

## Sign changes

At the center, f_1(pi/(2M);a^0)=1 and f_1(3pi/(2M);a^0)=-1. Shrink U so these two values remain above1/2 and below-1/2. Both angles belong to the first quadrant because M>=7. The remaining density terms are uniformly smaller than the leading term for all sufficiently large radii, by the same uniform geometric bound. Enlarging R if needed, the exterior density takes both signs on every circle r>=R. In particular each resulting profile and solution is nonzero.

## Present specializations and scope

The center hypothesis has been fully certified for (h,Q)=(2,9), M11, in227 and for (2,7), M9, in233. The center (2,5), M7, is certified in241 and admitted inV504 after independent review. The proposed (3,13), M17, branch in242 has only a finite probe in progress. No specialization for that pair is admitted here until its full response bound is proved.

Dependencies: the support theorem201 and its elementary specialization231; affine response144; compact response149; majorant and potential reconstruction145; the separate center certificates when invoked. No generic irreducibility hypothesis is used.
