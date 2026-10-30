# Sharp first-moment inequality with a homogeneous amplitude bound

## Exact theorem and scope

Let d>0, a=d+3, theta=d/(d+2) and nu=2(d+2)/(d+4). On R2 with
Lebesgue measure, define

    Jnu=integral_0^(2pi) |sin(phi)|^nu dphi
       =2 sqrt(pi) Gamma((nu+1)/2)/Gamma((nu+2)/2),
    C0=(d+4)Jnu/[4(d+2)],
    Csharp(d)=(d+2)/d * C0^((d+4)/(2(d+2))).

For every real measurable h satisfying

    ||h||2<=beta, |h(X)|<=H |X|^(-a) almost everywhere,

with finite beta,H>=0, its first moment is absolutely integrable and

    |integral y h(X)dX| <= Csharp(d) beta^theta H^(1-theta).     (1)

The constant is optimal for this homogeneous amplitude class, even if
h is required to be even in x and odd in y. For beta,H>0 equality is
attained by

    h_lambda(X)=sign(y) min(lambda |y|, H |X|^(-a)),
    lambda=[beta^2/(C0 H^(4/(d+4)))]^(1/nu).                  (2)

At X=0 set h_lambda=0. Sign reversal gives the negative extremum.
The same constant controls |integral X h| by rotational invariance.
Consequently (1) applies with q=-a and Hq(h)<=H, since
|h(X)|<=H(1+r)^q<=H r^q. Sharpness is asserted only for the larger
homogeneous amplitude class. No optimal-constant claim is made for
the weighted C1 class, in which the gradient is bounded as well.
In fact (2) generally has unbounded weighted gradient near the x axis
at large radius. The exponent in that smaller class is optimal by
T4-371, which is a separate fact. No inverse or existence follows.

## Absolute integrability

For any R>0, the disk part is at most sqrt(pi) beta R^2/2 by
Cauchy-Schwarz. Outside the disk the amplitude bound gives at most
4H R^-d/d. Thus the absolute first moment is finite. If beta=0 or
H=0 then h=0 almost everywhere and (1) follows. Assume both positive.

## Exact extremizer integrals

Write b=|sin(phi)|. For b>0 the two entries in (2) agree at

    R_phi=(H/(lambda b))^(1/(a+1)).

For r<R_phi the magnitude of h_lambda is lambda b r; for r>R_phi
it is H r^-a. The angles with b=0 form a null set. Radial integration
therefore gives

    integral_0^infty |h_lambda|^2 r dr
      =lambda^2 b^2 R_phi^4 [1/4+1/(2a-2)],
    integral_0^infty |y h_lambda| r dr
      =lambda b^2 R_phi^4 [1/4+1/(a-3)].

For example H^2 R_phi^(-2a+2)=lambda^2 b^2 R_phi^4 and
H b R_phi^(3-a)=lambda b^2 R_phi^4, by the crossing relation.
The angular exponent in each expression is
2-4/(a+1)=nu. Integration in phi yields

    ||h_lambda||2^2=C0 H^(4/(d+4)) lambda^nu,
    integral y h_lambda=D0 H^(4/(d+4)) lambda^(d/(d+4)),
    D0=(d+4)Jnu/(4d)=(d+2)C0/d.

Formula (2) makes the norm equal to beta. Eliminating lambda gives
D0 C0^(-theta/2) beta^theta H^(1-theta), exactly the right side of(1).
All integrals converge because d>0 and nu>0. The expression for Jnu
follows by quadrant symmetry and the substitution t=sin(phi)^2 in
the beta integral.

## Pointwise variational proof of optimality

For fixed X and lambda>0, the concave function

    t -> y t - t^2/(2lambda)

on the interval [-H r^-a,H r^-a] has its unique maximum at h_lambda(X).
Thus for every admissible h,

    y(h-h_lambda) <= (h^2-h_lambda^2)/(2lambda)

almost everywhere. Both sides are integrable by the preceding bounds.
After integration and using ||h||2<=||h_lambda||2=beta, it follows that
integral y h<=integral y h_lambda. Apply this to -h for absolute value.
Since h_lambda itself is admissible and attains equality, the constant
is optimal. Its dependence only on |y| and r proves S1 parity. Rotation
applies the same estimate to any component e dot integral X h; take e
in the direction of the moment to obtain the vector statement.

## Relation to the campaign

The independent split proof in T4-371 gives
Csplit=(d+2)/(2d) pi^(theta/2) 4^(1-theta). Formula(1) refines that
constant under the same amplitude implication from Hq, without
changing the Holder exponent or supplying an absent Hq budget.
For the campaign use d=1-1/c with
c=4076476460239181/2251799813685248. A numerical enclosure of Csharp
is supplementary; formula(1), its exact constant and proof are the
mathematical result. The endpoint projection mstar can be combined
with(1) only as a necessary weighted-budget constraint, not as a
stationary solution construction.

## Verification status

This argument was written and checked before the arithmetic script.
The script verifies the rational exponents and constant identities,
the two radial integration factors, and the beta-function constant
at the campaign d with Arb. No optimizer or sampled test is a proof
of the variational assertion. This new sharp-constant theorem is OPEN
pending independent Opus review. Dependencies: elementary polar
integration and pointwise concavity; T4-371 is needed only for the
comparison and the weighted-C1 exponent statement.
