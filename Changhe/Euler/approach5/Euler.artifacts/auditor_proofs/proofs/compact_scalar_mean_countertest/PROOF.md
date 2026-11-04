# A compact scalar countertest for the present Bernoulli mean bounds

Audit 2026-11-03T00:58:24Z. A329: CONFIRMED at the exact independent-field scope below. This is not an Euler counterexample.

## 1. Statement and established geometry

Fix 2/5<=c<1/2 and finite real omega. Set a=1-2c, kappa=1+c and d=3c. Use the confirmed A242-A243 smooth global independent fields B,W,U0, where

    B=(cI-omega J)y+U0, div B=d, div U0=div W=0,
    [B,W]=-kappa W,

U0 is compactly supported, W is nowhere zero and has derivatives O(|y|^(-1/c-j)), and both flows Phi and Gamma are complete. The backward B flow has a compact regular transitive attractor K with basin D=R3 minus a proper smooth line. The W flow is recurrent almost everywhere. These geometric facts depend on the explicit construction and its stated external classification inputs in the team records; they are not reproved from scratch here. In this model W is demonstrably different from curl U0.

There are smooth compactly supported H,g,h,R such that H=1 near K and

    BH=-ag, WH=-ah, R=H-g,
    Bh+kappa h=Wg, 2ah+div(hB+RW)=0.                   (1)

The scalar h has both strict signs in D, and for every Borel set I,

    integral_(D intersect H^-1(I)) h_plus
      = integral_(D intersect H^-1(I)) h_minus <infinity. (2)

For every 1<=p<d/a and T>=0,

    ||sup_(t>=T) exp(at)|H(Phi_t .)||_Lp(R3)
         <=C_p exp(-(d/p-a)T).                         (3)

Thus the renormalized scalar converges to0 almost everywhere through all real future times, although H equals1 on K. For p=2 its future error rate is at least exp(-cT) in the specified c range. Every p in A292's established interval p<2(1-c)/a is included. None of these facts identifies the scalars with actual Euler velocity, helicity or pressure.

## 2. Construct the functions and check all scalar equations

Choose a smooth compact cutoff chi equal to1 near K. Pick x in D outside its support and a smooth compact bump f in a small ball about x, disjoint from that support, with Wf(x)!=0. Such a bump is a linear coordinate with a nonzero W derivative times a cutoff equal to1 at x. Set H=chi+f and define g,h,R by(1). All are compactly supported, including the products with the noncompact vector fields, because derivatives of H vanish off a compact set.

The commutator gives

    Bh=-(BWH)/a=-(WBH-kappa WH)/a=Wg-kappa h.

Since WH=-ah and d+a=kappa,

    2ah+div(hB+RW)
       =Bh+(d+2a)h+WH-Wg
       =Bh+kappa h-Wg=0.

This correctly transforms R along with H. It does not keep a fixed physical P-|U0|2/2, which would fail the gauge test A322.

## 3. Signs and bandwise cancellation

Integration by parts on a ball containing supp H gives integral h=0. There is no boundary term since H is zero near that sphere, and div W=0. The function h is not identically zero, so continuity forces both strict signs on open sets. Removing the null proper line leaves nonempty open strict-sign subsets in D.

For bounded continuous phi put G(s)=integral_0^s phi(v)dv. Then G(H) is C1 and compactly supported because G(0)=0. Integrating W G(H) gives integral phi(H)h=0. The finite signed pushforward H_*(h dy) annihilates all bounded continuous functions and is therefore the zero finite Borel measure. Consequently the positive and negative pushforward measures agree on every Borel I. This proves(2), with finiteness because h is compactly supported. It assumes neither regular level boundaries nor a smooth basin boundary.

A326's same-level recurrence refinement is also satisfied: any recurrent point of a strict-sign open set yields a common open interval of H values with both h signs. This fact adds no missing Euler coupling.

## 4. Exact norm and all-time supremum

Liouville's formula gives det D Phi_t=exp(dt). Therefore, for every finite p>=1,

    ||H composed Phi_t||_p=exp(-dt/p)||H||_p.           (4)

Let E be the union of Phi_-s(supp H), 0<=s<=1. It is compact. For integer n>=0 and n<=t<=n+1,

    |H(Phi_t y)|<=||H||_infinity 1_E(Phi_n y).

Let N=floor T. Bounding the p-th power of a supremum by the sum over all integer intervals n>=N and applying(4) to 1_E yields

    integral sup_(t>=T) exp(apt)|H(Phi_t y)|^p dy
      <=||H||_infinity^p |E| exp(ap)
                     sum_(n>=N) exp((ap-d)n)
      <=C_p^p exp(-(d-ap)T).

The geometric series converges exactly for p<d/a, proving(3). The supremum is measurable by continuity and rational-time approximation. Its nonnegative values decrease with T and their integrals tend to0. Thus their limit is0 almost everywhere, giving all-real-time convergence without an exceptional-time problem.

The comparison with the true Bernoulli estimates is exact:

    d/2-a=7c/2-1 >= c for c>=2/5,
    2(1-c)/a <= d/a for c>=2/5.

The second inequality is equality at c=2/5, but A292 uses a strict p interval, so no endpoint claim is added. In particular the local unrenormalized square estimate follows from(4) and d>=2a.

## 5. The coefficient formula and singular invariant probabilities

The compact scalar forcing R satisfies BH=-aH+aR. For p<d/a, Minkowski and(4) applied to R show

    ||integral_0^infinity exp(at)|R(Phi_t .)|dt||_p
       <=||R||_p integral_0^infinity exp((a-d/p)t)dt <infinity.

Integrate the differential equation for exp(at)H(Phi_t y), then use(3). On a full-volume set,

    H(y)+a integral_0^infinity exp(at)R(Phi_t y)dt=0.

Thus its asymptotic coefficient is zero. Compact full invariance of K and det D Phi_t=exp(dt)>1 imply |K|=0. For every invariant probability supported on K, integral H2=1 instead. There is no contradiction: ambient-volume convergence cannot be assigned to a singular probability without a separate transfer. The proposed SRB smearing transfer uses a different absolutely continuous measure and long vortex averages, so is consistent with this example.

## 6. What the countertest establishes

The presently proved reduced scalar identities, band cancellation and local transported Lp mean bounds do not by themselves distinguish this H from a true Bernoulli scalar on the independent-field geometry. This is a precise failure of that reduced list of premises, not a proof that every scalar argument must fail. The actual definitions g=U0.B, h=U0.W and R=P-|U0|2/2, the normal Lamb component and the nonlocal pressure remain additional constraints. The full Euler momentum equation and W=curl U0 fail in the model. No target profile or nonexistence result follows.

The entire submitted LIT71 proof and the relevant A242-A244 geometry statements were read. All displayed estimates were independently derived above. No computation is an input. The immutable submitted proof and its hash are in the team records.
