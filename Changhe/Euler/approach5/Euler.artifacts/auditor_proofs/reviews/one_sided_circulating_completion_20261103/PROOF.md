# A one-sided radial rate for excluding a negative scalar completion

Status: local one-sided-rate theorem CONFIRMED A2611-A2612, with complete comparison A2613. Unrestricted extensions remain OPEN A2614.

## 1. Exact hypotheses and conclusion

Fix 0<c<1/2, any finite omega, Jx=e3 cross x, X=Ax with A=cI-omega J, L=(1-c)I+omega J, a=1-2c, b=2(1-c), eta=a/b and kappa=1-2eta=c/(1-c)>0. Let sigma:D_R->R3 minus {0} be a smooth section transverse to X, with x0=sigma(0) and a finite flowbox Phi(y,s)=exp(sA)sigma(y). Let Gamma be the central orbit.

Suppose V is smooth, infinitely flat on Gamma, nonzero off it, and satisfies div V=0, X.V=0 and DV X=-LV. Put W=curl V. Suppose a smooth positive radial f(r) on the punctured disc is flat in value and

    sigma^*(V.dx)=f(r)zeta(y),
    c1 f(r)<=|V(sigma(y))|<=c2 f(r),
    zeta.e_theta>=d0>0,

for fixed positive constants, with zeta smooth off zero. Define Y=(zeta2,-zeta1) and Y_r=Y.e_r. Suppose a nonnegative q, integrable on each [r,R] with r>0, satisfies

    (-div Y)_+/Y_r<=q(r), Q(r)=integral_r^R q(t)dt,
    kappa log(1/f(r))-Q(r) -> +infinity.                (1)

Take the outer circle strictly inside all smooth domains. The subscript + denotes the positive part of a real number. Then no smooth scalar S near x0 satisfies

    X.grad S=-bS, W.grad S=0,
    S<0 off Gamma, S=0 on Gamma,
    -Delta(S+|V|^2/2)=tr((DV)^2).                        (2)

No upper bound on the positive part of div Y or the whole derivative D zeta is required. No trace sign, full-profile assertion or uniformity in omega is included.

## 2. The exact inward integration sign

Assume (2), H=-S and E=|V|^2. Differentiating X.V=0 gives (DV)^T X=-A^T V, so

    X cross W=(DV)^T X-DV X=(L-A^T)V=aV.

Using X.grad H=-bH and W.grad H=0 gives

    a grad H cross V=grad H cross(X cross W)=bH W,
    curl(H^(-eta)V)=0.

Thus on the punctured section, with F=f(H composed sigma)^(-eta)>0, one has d(F zeta)=0, or div(FY)=0. The radial speed is Y_r=zeta.e_theta>=d0. Starting at any r>0 the forward trajectory stays away from zero, continues on each compact annulus and reaches the outer circle in finite time at most (R-r)/d0. Smoothness on compact annuli suffices; no centre completeness or global uniform speed upper bound is needed.

Along the trajectory parameterized by increasing radius,

    d(log F)/dr=-(div Y)/Y_r.

Writing y_R for its exit point and integrating from the initial radius to R gives

    log F(y)=log F(y_R)+integral_r^R (div Y)/Y_r dt
             >=log F(y_R)-Q(r).                         (3)

The plus sign before the inward integral is essential. The positive smooth F on the outer circle has minimum m>0, so F(y)>=m exp(-Q(r)). There is no required upper bound on F.

## 3. Uniform dominance and flatness

Solving for H and using the lower velocity bound yields

    H(sigma(y))/E(sigma(y))
      <=m^(-1/eta)c1^(-2) f(r)^(1/eta-2) exp(Q(r)/eta)
      =C exp(-[kappa log(1/f(r))-Q(r)]/eta).             (4)

Condition (1) forces this ratio to zero uniformly in angle. Both H and E obey X.grad H=-bH and X.grad E=-bE; the second identity follows by skew-symmetry of J. Hence H/E is invariant along the finite flowbox. Its inverse coordinates are continuous and have bounded derivatives on a smaller compact box. As x tends to x0, its section coordinate y tends to zero. Thus (4) implies H<=E/4 on a small ball off Gamma, with both sides zero on Gamma.

Since V is infinitely flat at x0, E is flat in value there. The inequality 0<=H<=E/4 proves the same for H. Smooth Taylor expansion then makes every derivative of H vanish at x0. No separate flatness assumption on S or comparison of its derivatives with those of E is needed.

## 4. The local stress contradiction

Set P=E/2-H and T=V tensor V+P I. In the small ball,

    (E/4)I<=T<=(3E/2)I, div div T=0.

The latter equation is exactly (2) plus div div(V tensor V)=tr((DV)^2), using div V=0. The tensor is smooth and infinitely flat at x0.

Translate x0 to zero. Let A0(r) be the normalized spherical average of n.T(rn)n, B0(r) that of tr T(rn)-n.T(rn)n, and e(r) that of E(rn). The divergence theorem on the whole ball gives zero flux of div T. Averaging div(Tn)=n.div T+[tr T-n.Tn]/r, with the angular divergence integrating to zero, gives

    A0'(r)=[B0(r)-2A0(r)]/r.

There is no missing centre term since T is smooth there. The tensor bounds give A0>=e/4 and B0<=3e<=12A0, so (r^(-10)A0)'<=0. Thus A0(r)>=(r/r1)^10 A0(r1) for 0<r<r1. Flatness forces A0(r1)=0. Positivity and continuity force E=0 on every small sphere, and V=0 on a ball, contradicting the nonzero field off Gamma. This proves the theorem.

## 5. Relation to accumulated variation and exact threshold scope

If |D zeta|<=q0(r) and integral_r^R q0<=K0+K1 log(R/r), then |div Y|<=sqrt(2)|D zeta|. With q=sqrt(2)q0/d0, Q=O(1+log(1/r)). Value-flatness of f means log(1/f(r))/log(1/r) tends to infinity: for every N, its lower limit is at least N using f<=C_N r^N. Thus (1) follows and recovers the logarithmic criterion.

More generally limsup Q/log(1/f)<kappa implies (1), because a fixed positive margin times log(1/f) tends to infinity. Equality of that limsup is neither excluded nor automatically covered; only the actual difference in (1) decides applicability. The theorem does not claim the coefficient is sharp.

The smaller-amplitude sparse-carrier versions verified in the companion circulating_direction_completion proof have the required definite direction and Q=O(log(1/r)). Its Section5 proves the normalized derivative bound by integrating O(1/elln) over the disjoint width-O(elln) annuli. The fixed metric, bump and positive amplitude precede any chosen envelope. That application retains those hypotheses and does not apply indiscriminately to every original amplitude or carrier.

## 6. Verification and boundaries

All six source sections were read. The closedness sign, inward integral, lower bound on F, exact kappa, flowbox transfer and entire stress argument have been reconstructed here without a numerical computation. The logarithmic theorem is not a premise of the main result; it is a corollary. The sparse-carrier application uses the separate explicitly stated construction estimates.

The indefinite-direction case, failure of the quantitative rate, other scalar signs and zero sets, and unrestricted rotating-profile nonexistence remain open. The existing coordinator comparison is complete. No formal verification is claimed.

The full eleven-item coordinator comparison, its four wording points and its concluding consistency check were read. All four source and independent proofs agree. The inverse-flowbox Lipschitz transfer and shrinking of the outer circle are explicit here; only a lower bound on F is needed. The sparse application retains a smaller fixed positive amplitude chosen before the envelope. The comparison is pinned in the team records. The existing configured model agent supplied this comparison through files; actual provider execution is independently unattested. No client or extra agent was started. No gap was found in the stated conditional theorem.
