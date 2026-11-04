# A Dini error in the normalized quarter-pressure inequality

Status: CONFIRMED A2692-A2694; scope OPEN A2695. Complete source and independent reconstruction read; existing coordinator comparison completed.

## 1. Exact statement and notation

Let V be C2(B_R;R3) and P be C1(B_R), with B_R centered at zero. Suppose

    div V=0, -Delta P=tr((DV)^2) in distributions,
    V(0)=DV(0)=P(0)=0.

Let delta:(0,R)->[0,delta0] be measurable, where 0<=delta0<1/4. Assume

    integral_0^R delta(r)dr/r<infinity,
    P(x)>=[1/4-delta(|x|)]|V(x)|^2 for 0<|x|<R.       (1)

Then V=P=0 on the whole ball. The hypothesis is pointwise in x, apart from the explicitly measurable radial error. No pressure upper bound or pointwise convergence of delta is assumed. A separate exact C2 example below shows that a uniform limit P/|V|^2 ->1/4 alone does not imply this conclusion. It does not prove necessity of the Dini condition for every possible modulus.

## 2. The center identity and a bounded weighted quotient

Put E=|V|^2 and T=V tensor V+P I. Incompressibility and the Poisson equation give div div T=0. Since T is C1, its divergence is continuous. Mollification on a compactly larger subball and passage to the limit give zero flux of div T through each centered sphere.

With normalized sphere averages, put

    e=<E>, v=<(V.n)^2>, pbar=<P>, A=v+pbar.

The radial flux identity is

    rA'=e-3v.                                         (2)

The tangential divergence integrates to zero. There is no center charge. Taylor expansion gives e,v=O(r^4), and pressure normalization gives A(0)=0. Therefore

    A(r)=integral_0^r[e(s)-3v(s)]ds/s=O(r^4).

Moreover A>=v+(1/4-delta0)e>=0. Define measurable k,q and a locally absolutely continuous w by

    k=4pbar-(1-4delta)e>=0,
    q=16delta/(1-4delta),
    w(r)=exp(integral_r^R q(s)ds/s).

The Dini condition and delta0<1/4 give 1<=w<=C and a finite positive limit w0 at zero. Set G=A/r^4 and F=wG. Since

    A=v+(1/4-delta)e+k/4,
    q(1/4-delta)=4delta,

differentiation almost everywhere gives the exact identity

    F'=-w[(7+q)v+(1+q/4)k]/r^5<=0.                    (3)

Thus F is nonnegative, bounded at zero and nonincreasing with radius. Its limit L at zero is finite, and

    integral_0^r1 (v+k)dr/r^5<infinity                 (4)

for every r1<R. This argument allows measurable spikes in delta.

## 3. Reduction to a tangential quadratic

If L=0, monotonicity gives F=A=0 at every radius. The positive lower bound for A gives e=0, so V=0. Then P>=0 by (1), while pbar=0, and continuity gives P=0.

Suppose L>0. Write Q(x)=(1/2)D2V(0)[x,x]. If Q=0, then e,v=o(r^4), and (2) integrated from zero gives A=o(r^4). Bounded w would force L=0. Thus Q is nonzero.

C2 Taylor expansion gives V_epsilon(x)=epsilon^-2 V(epsilon x) ->Q in C2 on compact sets. In particular v(r)/r^4 tends to <(Q(n).n)^2>. A positive limit would make (4) diverge like integral dr/r. Hence this limit is zero, and continuity and homogeneity give x.Q(x)=0 everywhere. Divergence freedom passes to Q.

## 4. The pressure limit despite a nonconvergent pointwise error

The pointwise nonnegative defect

    K(x)=4P(x)-[1-4delta(|x|)]E(x)

has sphere average k. It satisfies

    |4P-E|<=K+4delta(|x|)E.                            (5)

For fixed b>0, polar integration and (4) give

    integral_B_b epsilon^-4 K(epsilon x)dx
      =4pi epsilon^-7 integral_0^(epsilon b) k(s)s^2 ds
      <=4pi b^7 integral_0^(epsilon b) k(s)ds/s^5 ->0.

The second term in (5), using e(s)<=Cs^4, is at most

    C epsilon^-7 integral_0^(epsilon b) delta(s)s^6 ds
      <=C_b integral_0^(epsilon b) delta(s)ds/s ->0.

Consequently P_epsilon=epsilon^-4 P(epsilon x) converges to |Q|^2/4 in L1 locally. No pointwise convergence of delta, fourth pressure derivative or subsequence has been used. Passing the exactly rescaled Poisson equation to distributions yields

    Delta|Q|^2/4+tr((DQ)^2)=0.                         (6)

## 5. The three-dimensional quadratic contradiction

From x.Q=0 and quadratic homogeneity,

    (DQ)^T x=-Q, DQ x=2Q, x cross curl Q=-3Q.

Since curl Q is linear, Q=x cross Mx for some real matrix M. The identity div Q=-x.curl(Mx)=0 forces M symmetric. In an oriented orthonormal eigenbasis write

    Q=(A yz,B xz,C xy), A+B+C=0.

The three coefficients of (6) give B^2+C^2+4BC=0 and its cyclic counterparts. Using A+B+C=0, these are A^2=-2BC, B^2=-2AC and C^2=-2AB. Their product is (ABC)^2=-8(ABC)^2, so ABC=0 and all three coefficients vanish. This contradicts nonzero Q. Thus L>0 is impossible, and Section 3 proves the full-ball conclusion.

## 6. Exact non-Dini countertest and its regularity

Fix R<exp(-1). With rho=sqrt(x^2+y^2) and t=log(1/rho), define off the axis

    V=[rho/t](-y,x,0), E=rho^4/t^2,
    P(rho)=integral_0^rho s^3/log(1/s)^2 ds,

and extend V=P=0 to the axis. For j<=2, Cartesian derivatives of V off the axis are O(rho^(2-j)/t). Successive difference quotients at the axis establish all derivatives through order two there, and those derivatives are zero and continuous. Hence V is C2 with V=DV=D2V=0 on the axis. The radial pressure integral is C1 and vanishes there.

The azimuthal speed is a=rho^2/t. Direct cylindrical differentiation gives div V=0, acceleration -a^2 e_rho/rho and grad P=a^2 e_rho/rho. Thus stationary Euler and the distributional Poisson equation hold, including across the axis.

Substitution s=rho exp(-u) gives

    P/E=F0(t)=integral_0^infinity exp(-4u)[t/(t+u)]^2 du.

Set delta_*(r)=1/4-F0(log(1/r)). It is positive, continuous and increasing in r, and bounded above on (0,R) by a constant less than 1/4. Since rho<=|x|, it supplies the full-ball inequality (1). Furthermore

    t[1-(1+u/t)^(-2)] ->2u,
    0<=t[1-(1+u/t)^(-2)]<=2u.

Dominated convergence gives t delta_*(exp(-t)) ->1/8. The Dini integral therefore diverges. Nevertheless the deficit at any nonzero-velocity point x is at most delta_*(|x|), so P/E tends uniformly to 1/4 near zero.

The field is not a similarity profile for any c in (0,1/2) or any omega. Axisymmetry cancels the rotation generator. After subtracting its stationary equation the residual is (1+c+c/t)V, which has nonzero circulation on each small circle and cannot be a single-valued pressure gradient. No global decay assertion follows.

## 7. Dependencies and audit boundary

All seven submitted source sections were read. The proof above uses the C1 stress flux, the exact integrating factor, a nonnegative defect, C2 Taylor expansion, the elementary symmetric-matrix classification and a direct logarithmic example. It does not use a pending theorem as a premise.

The example only refutes a bare endpoint-ratio-limit inference in the C2 class. It does not refute a smooth version, prove the sharp modulus for all errors or produce an actual tail. Existing configured model file comparison is completed in the final section; actual provider runtime is independently unattested. No computation or new client was run.

## 8. Completed existing coordinator comparison

The full ten-item coordinator comparison and both wording points D1-D2 have been read, along with the complete supplied check log. The source hash matches the independent snapshot. Items 1-6 agree with Sections 1-5, including the bounded measurable deficit, absence of a pointwise limit assumption, exact cancellation by q, and L1 pressure blow-up. Items 7-9 agree with the exact stationary log swirl and its all-omega profile failure; the numerical quadratures in the supplied log are supplemental and are not the proof of the limit. Item 10 and D1-D2 correctly preserve the whole-ball lower bound, Dini integral and C2 scope. The independent proof needs no numerical output.

No discrepancy was found. The example is stationary Euler but is not a similarity profile; it disproves replacement of the Dini condition by the bare endpoint-ratio limit in the stated C2 class. It does not show that every non-Dini modulus admits a counterexample. Existing configured model file collaboration is completed for this result; actual provider runtime remains independently unattested.
