# General-trace resonance: audit of proposed 3.71

Verifier result 163. Written 2026-10-21 before the supporting arithmetic audit. The frozen proposed statement and appendix are in verification/main.v1.src and app.v1.src. The finite functionals and constants were independently computed in results156-158. This audit verifies their use for an actual exterior profile and records local wording repairs in the synthesis.

## 1. Statement, parity and scope

Take (ell,K,M)=(3,5,2) or (5/2,9,4), p=1/ell, delta=1-p and s_i=p-i delta. Let Theta be a smooth real trace with the Setting III parities: Theta(-theta)=-Theta(theta) and Theta(pi-theta)=Theta(theta). Equivalently it has only positive odd sine modes. Define P_0=Theta and, for 1<=k<=K,

    P_k=(ell k delta)^(-1) sum_(i+j=k-1)
           [s_j (V_i[P_i])_r P_j+(V_i[P_i])_theta P_j'] .          (1)

Here V_i is the angular coefficient of the particular velocity produced by r^{s_i} times its argument. Set

    g[Theta]=-M [sin((M-1)theta)] P_K[Theta].                      (2)

This is a homogeneous polynomial functional of degree K+1 on the trace space. For a smooth exact exterior profile satisfying the canonical inverse and S^p hypotheses of 3.68, its actual density coefficient at degree s_k is P_k for k<=K, and g is the coefficient of the first possible resonant source. The S^p hypotheses are already proved for full primary profiles elsewhere. The finite functional can also be studied on traces for which no profile is known to exist.

The claims in proposed3.71(a)-(c) are correct with the proof repairs below: g depends on arbitrarily high Fourier modes, is locally Lipschitz in the stated weighted Fourier norm, and has the reported simple zeros for Theta=sin(theta)+epsilon sin(3theta). For an actual exterior profile as above, if g[Theta] is nonzero, its first stream and density logarithms are respectively

    (g/(2M))r^{-M}log(r)sin(Mtheta),
    -g/[2ell(M+2)] r^{p-M-2}log(r)
         [p cos(Mtheta)Theta+sin(Mtheta)Theta'].                   (3)

The second coefficient is not identically zero for a smooth nonzero Theta. Here report notation is M=2m, so its prefactor -g/[4ell(m+1)] is correct. No assertion constructs a profile, or excludes profiles that admit such logarithms.

## 2. Isolation of the actual radial coefficients

The previously audited expansion theorem gives density deficits D=k delta+2l, with k>=0 and l=0 or l>=2. A deficit is p minus the density homogeneity. The l>=2 terms account for one or more decaying harmonic velocities: the first such velocity has degree -3, so its first density interaction has deficit4. Multiplication adds deficits with the further delta from a density-induced velocity, giving the displayed semigroup. Smooth infinite angular support changes the coefficients, not these radial degrees.

For ell=3, K delta=10/3<4, so no mixed sector reaches the pure sectors k delta with k<=K. For ell=5/2, K delta=27/5. The only possible mixed offsets below this threshold have 2l=4; equality 4+k(3/5)=k'(3/5) would require k'-k=20/3, impossible for integers. All other offsets exceed the threshold. Thus none changes (1).

Before index K, s_i+1 is never a nonzero even integer in either case. In particular every even stream-mode divisor n^2-(s_i+1)^2 is nonzero. Also a decaying harmonic velocity degree -n-1 with positive even n cannot equal any s_i with i<K. At i=K, s_K=-M-1. These exact arithmetic facts justify the particular inverse in every occurrence in (1).

It remains to check that another mixed sector does not create an earlier logarithm. Up through the first density-log deficit M+2, a source at density deficit D could resonate only if |p+1-D| is a positive even integer. The finite semigroup arithmetic gives just D=K delta and frequency M in both cases. For ell=3 the mixed sector starts at the upper endpoint D=4. For ell=5/2 the mixed deficits at most6 are 4,23/5,26/5,29/5 and6, none of which has |p+1-D| a positive even integer. The pure deficits give only K. Thus the radial proof of the first-log statement applies to a general smooth trace.

## 3. The mode map and the high-frequency proof repair

For an input a_n sin(n theta) in a density of degree s_i, its x derivative has sine coefficients (s_i-n)a_n/2 at n+1 and (s_i+n)a_n/2 at n-1. Dividing the source coefficient G_j by j^2-(s_i+1)^2 gives stream coefficient H_j, and its polar velocity coefficients are -j H_j cos(jtheta) and (s_i+1)H_j sin(jtheta). At s_K=-M-1 the source at frequency M receives -M times the P_K coefficient at M-1 and zero times its coefficient at M+1. This proves (2).

For Theta=sin(theta)+epsilon sin(Ntheta), the coefficient of epsilon^e in P_k uses e copies of the high mode. In signed Fourier notation every frequency is aN+b, with |a|<=e, a congruent to e modulo2, and |b|<=2k+1-e. The bound counts the k+1-e low-mode inputs and at most k unit shifts from the derivative/inverse maps in the k bilinear interactions. Products add signed frequencies, and the sine reflection only identifies opposite signed frequencies.

When N>4K+4, two distinct signed pairs cannot give the same signed frequency: a nonzero multiple of N cannot equal a difference of bounded b values. Absolute frequencies coincide precisely when the pairs are identical or opposite. The original sentence claiming distinct pairs give distinct absolute frequencies is false, for example (1,0) and (-1,0). This does not affect rational dependence on N: the reflection and collection pattern is fixed after those unavoidable identifications. All finite recurrence operations then give rational functions of N.

For e=1, the parity information gives a=+1 or -1, so the absolute frequency is at least N-2K>M-1. The linear coefficient of g is therefore zero. Its quadratic coefficient is nonzero at N=101 in both cases, as the independent exact dual-algebra certificates156 verify, with the stated residues modulo1000003. A nonzero rational function has only finitely many zeros. Hence arbitrarily large odd N change g for all sufficiently small nonzero epsilon; no finite set of Fourier coefficients determines the functional.

This remains true even within traces positive on the upper half circle: |sin(Ntheta)|<=N sin(theta) for 0<theta<pi, by the finite geometric-sum formula, so |epsilon|<1/N preserves positivity. This observation is about the functional, not the realization of such a trace by a profile.

## 4. Continuity, exact constants and cancellation

Write ||f||_j=sum_(n>=0)(1+n)^j|a_n| for the relevant sine or cosine series, with the natural coefficient at zero for cosine series. Product-to-sum and 1+|n+-n'|<=(1+n)(1+n') give the product norm inequality; differentiation satisfies ||f'||_j<=||f||_(j+1).

Put q_i=|s_i+1| and B_i=max over positive even n of (n+q_i)/|n-q_i|. The maximum is among the neighboring even integers or n=2, since the ratio is increasing below q_i and decreasing above it. With

    L_i=B_i[(3/2)^K+1]/2,

both velocity components together have j-norm at most L_i||f||_j for 0<=j<=K. Indeed each source numerator is at most n+q_i, the two velocity numerators together contribute n+q_i, and the denominator is |n-q_i|(n+q_i). The upward input-output weight ratio is at most(3/2)^j and the downward ratio at most1.

For output level t=K-k and i+j=k-1, t<=K-i and t+1<=K-j. Therefore the constants C_0=1 and

    C_k=(ell k delta)^(-1)sum_(i+j=k-1)L_i(|s_j|+1)C_i C_j

give ||P_k||_(K-k)<=C_k||Theta||_K^(k+1). Splitting each bilinear difference and inducting gives the Lipschitz constant (k+1)C_k R^k, where R=max(||Theta||_K,||Phi||_K). Extraction (2) multiplies the final bound by M. Taking

    epsilon0=min(1, |g[sin(theta)]|/
                  [2M(K+1)C_K(2^K+1)^K])

gives the stated sign and half-magnitude persistence around A sin(theta), A nonzero. The exact positive radii and the lead's independent Opus5.5 recomputation match result157. They are conservative sufficient bounds, not a numerical candidate certificate.

For the two-mode trace, recurrence (1) implies degree at most k+1 in epsilon, not automatically exactly k+1. The computed nonzero leading coefficient in certificate158 proves that g has degree exactly K+1. The proposed integer polynomial for ell=3 is precisely a positive multiple of that full rational polynomial. Exact Sturm certificates give two simple real roots in (0,1) at ell=3 and four at ell=5/2, with the reported brackets and decimal labels. Result158 actually accounts for all real roots. Since sin(theta)+epsilon sin(3theta)=sin(theta)[1+epsilon(3-4sin^2(theta))], these traces are positive in the upper half circle at each root. The recurrence alone must not be cited as proving the exact degree or root counts; the explicit certificate does so.

## 5. The first density logarithm and its nonvanishing

The polar Laplacian gives -Delta[r^{-M}log(r)sin(Mtheta)]=2M r^{-M-2}sin(Mtheta), so the source coefficient g gives the first stream term in (3). Its logarithmic polar velocity is -(g/2)r^{-M-1}log(r)(cos(Mtheta),sin(Mtheta)). Acting on r^p Theta produces -(g/2)r^{p-M-2}log(r)[p cos(Mtheta)Theta+sin(Mtheta)Theta'].

The radial transport operator is ell r partial_r-1. At t=p-M-2 its diagonal factor is ell t-1=-ell(M+2). In the equation this operator equals -U.grad rho, so the highest-log coefficient is the second term in (3), with the displayed negative sign. No other term can cancel it: Section2 excludes an earlier stream log; only its product with the leading density reaches this density degree; products with lower densities and feedback through their inverse have strictly smaller degree. Harmonic velocities at that degree have no logarithm. This is the finite decreasing-degree argument, and uses no angular truncation.

If the bracket in (3) vanished, on each interval between consecutive zeros of sin(Mtheta) its solutions would be Theta=C|sin(Mtheta)|^(-p/M). Since p/M>0, boundedness at either endpoint forces C=0. Thus Theta vanishes on every such interval and everywhere by continuity, contrary to the hypothesis. The term is nonzero for a nonzero smooth trace when g is nonzero.

## Verdict and required local repairs

CONFIRMED: radial-sector isolation, the exact inverse and recurrence, high-mode dependence, Lipschitz constants and radii, polynomial transcription and root counts, and the general-trace first-log coefficient under the exact exterior hypotheses.

Required proof repairs: identify signed frequencies before passing to absolute frequencies, and explicitly use a=+-1 for the linear high-mode coefficient; change “degree k+1, so degree K+1” to “degree at most k+1, with the computed leading coefficient showing degree exactly K+1 for g”. Also specify both Setting III trace parities and retain the exact-profile hypotheses explicitly in part(d). These are local repairs and do not invalidate the certified functional conclusions. The literal distinct-absolute-frequency assertion is REFUTED. All other claims are conditional as stated above. No primary endpoint follows.

Dependencies: audited expansion theorem and canonical radial inverse; independent results156,157,158; elementary weighted Fourier algebra, scalar Laplacian and first-order ODE; exact finite coefficients and Sturm certificates. No producer code is executed for this audit.
