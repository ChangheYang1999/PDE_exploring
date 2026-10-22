# Forward-decay thresholds and the axis-mapping obstruction

Date 2026-10-22T03:15:17.947834+00:00. Written before the new exact checks. Status OPEN pending complete actual Claude Opus5.5 review and later independent adjudication. This checks the lead's2026-10-22T03:12 note, with an essential distinction between forward decay and invertibility in either time direction.

## Statement, parameters and dependencies

Let A>0, D=2A+1, b0=(A+3)/2. The frozen transport is T=-A x partial_x+D y partial_y-1. For the logarithmic space Y_(a,s) defined in anisotropic_frozen_transport_inverse, s>=0, set

 delta_Y=D(s-1/2)-A(a-1/2)-1,
 theta(s)=1/2+[D(s-1/2)-1]/A.

For the quadrant Euler-derivative space Z_(a,b,m) of quadrant_euler_axis_obstruction, a,b real and integer m>=0, set

 delta_Z=bD-aA-b0,
 phi(b)=(bD-b0)/A.

Then

 delta_Y<0 iff a>theta(s),
 theta(s)-5/2=(D/A)(s-3/2),                             (1)
 delta_Z<0 iff a>phi(b),
 phi(b)-5/2=(D/A)(b-3/2).                               (2)

Thus every forward-decaying Y weight has a>5/2 when s>=3/2, and every forward-decaying quadrant weight has a>5/2 when b>=3/2. Conversely, if s<3/2 (respectively b<3/2), a weight strictly below5/2 with delta_Y<0 (respectively delta_Z<0) exists. The precise quantified statement is that the set of ALL forward-decaying weights lies in{a>5/2} if and only if the indicated order is at least3/2. It is not a pointwise equivalence between a single inequality delta<0 and an order threshold.

The previously confirmed canonical-background test h of axis_weighted_nonlocal_mapping therefore has full IPM image outside every Y in the first forward-decaying regime. The same h has image outside every Z in the second regime, by quadrant_euler_axis_obstruction. These conclusions concern the image of that compact test, not an inverse on a smaller compatible domain. In addition, the canonical trial residual itself lies outside those spaces, by canonical_axis_residual. Its nonzero coefficient has already been independently enclosed; no new PDE numerics are needed here.

The phrase 'every frozen-invertible quadrant weight with b>=3/2' without a forward qualifier is FALSE. Indeed set a=0,b=3/2. Then delta_Z=5A/2>0, T is invertible on its maximal quadrant domain, and a<5/2. Invertibility in that example uses negative time. No full IPM mapping or inverse at those alternative weights is claimed.

For the actual dyadic modal parameter, A=2/k-1, D=4/k-1. At s=153/50 the exact theta(s) is computed by rational arithmetic and compared to directed decimal endpoints in two different exact arithmetic implementations. A decimal approximation of theta is not used as proof of (1).

## Proof of the algebra and the two obstructions

Since A>0, solving delta_Y<0 for a gives its first equivalence. Subtracting5/2 from theta and using D=2A+1 gives

 A(theta-5/2)=D(s-1/2)-1-2A=D(s-3/2).

The same computation gives

 A(phi-5/2)=Db-(A+3)/2-5A/2=D(b-3/2).

The positive multiplier D/A proves the thresholds, including equality of the threshold to5/2 at order3/2. The forward condition a>theta or a>phi is strict even at that order. If s<3/2, take a=(theta(s)+5/2)/2; it lies strictly between theta and5/2. The analogous choice with phi proves the converse. This establishes the set-containment statements exactly.

The accepted compact parity test h is supported away both axes, has zero center jet and zero canonical strain, belongs to every finite-weight Y or Z under discussion, and has full image g>=c x^2 on a rectangle0<x<x1,0<y1<=y<=y2. For any a>=5/2 the weighted zeroth square dominates a positive constant times integral_0^x1 x^(4-2a)dx=infinity. A fixed-y weight y^(-2b) has a positive lower bound there for every finite realb. This proves the mapping obstructions with no derivative assumptions on g. The canonical residual uses its own identical rectangle argument with Q>0. These lower bounds and their canonical hypotheses are proved in the respective parent results, and the inherited evidence is freshly rechecked here.

## Why 'forward inverse' cannot be shortened to 'inverse'

For completeness, the quadrant inverse can be reconstructed without any general operator theorem. Write u=log x,v=log y and F(u,v)=exp((1/2-a)u+(1/2-b)v)h(exp u,exp v). The zeroth norm becomes L2(du dv), while the Euler derivatives become partial_u+a-1/2 and partial_v+b-1/2. The squared full norm on Fourier transforms is the positive polynomial weight

 P_m(xi,eta)=sum_(i+j<=m)(xi^2+(a-1/2)^2)^i(eta^2+(b-1/2)^2)^j.

The transformed operator is -A partial_u+D partial_v+delta_Z. Its multiplier delta_Z+i(D eta-A xi) has reciprocal bounded by1/|delta_Z| whenever delta_Z!=0. Multiplication by this reciprocal maps every target into the maximal distributional domain, and multiplication back gives both inverse identities. Thus the model is invertible for either sign. The bound is sharp by target Fourier supports in arbitrarily thin strips about D eta=A xi. The displayed counterexample a=0,b=3/2 has delta_Z=5A/2>0; its inverse norm in the base space is2/(5A). This is a self-contained inverse proof for that counterexample, not reliance on the lead's summary.

There is also a negative-time regime in Y. Let c=-A(a-1/2)-1 and delta_minus=c-D/2=-Aa-b0. The group in log coordinates is S(t)F(u,y)=exp(c t)F(u-A t,exp(Dt)y). For t>=0, its negative-time action obeys

 ||S(-t)F||_(H^s)^2
 =exp((-2c+D)t) integral(1+xi^2+exp(-2Dt)eta^2)^s |Fhat(xi,eta)|^2
 <=exp(-2delta_minus t)||F||_(H^s)^2.

Here s>=0 and D>0. If delta_minus>0, the Bochner integral Rf=integral_0^infinity S(-t)f dt converges with norm at most1/delta_minus and is the inverse of T. The maximal-domain and strong-continuity proof is exactly the distributional pairing argument of anisotropic_frozen_transport_inverse, applied to the same group at negative time. Directly, d/dt S(-t)f=-T S(-t)f yields T Rf=f; on the maximal domain integration of S(-t)Th gives RTh=h, since S(-t)h tends to0. Therefore delta_Y<0 is a sufficient forward-inverse condition and is not an established iff criterion for all Y inverses. This negative-time observation does not classify the remaining parameter strip. For the actual k<1/2 one has A>3, so a=-1 yields delta_minus=(A-3)/2>0 for every s>=0, another explicit model counterexample to unrestricted wording.

## Scope and verification

Dependencies: anisotropic_frozen_transport_inverse (space and group realization), axis_weighted_nonlocal_mapping (one compact test and lower bound), quadrant_euler_axis_obstruction (quadrant extension), canonical_axis_residual (actual residual lower bound). The older conormal_saddle proof is consistent with the independent Fourier reconstruction above. No norm transfer, global full-operator inverse, nonlinear estimate, exclusion of an admissible profile or decisive PDE endpoint follows. Strong positive forward weights cannot simply be rescued by the frozen inverse; negative-time model weights require separate IPM analysis.

The exact check reads k from the binary NPZ with Fraction in one path and from hexadecimal JSON with integer/fmpq arithmetic in the other. Independent symbolic manipulation checks(1),(2), the counterexample and the negative-time exponent. Scalar checks supplement this complete informal proof; no computed finite sample substitutes for its quantifiers or its infinite-dimensional multiplier argument.
