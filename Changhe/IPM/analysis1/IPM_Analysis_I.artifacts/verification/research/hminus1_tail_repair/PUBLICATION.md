# Exact normalized tail repair with a homogeneous H^{-1} residual

Read PROOF.md together with mandatory ADDENDUM.md. The separately dated
verdict.json records whether the full audit has closed. This note alone
is not a verification verdict.

For the exact normalized modal trial rho0 and its exact k, set

 a1=2k-1, a2=3k-2, d=k-2, a3=4k-3.

Both original-input methods prove 0<k<1/4 and the strict intervals

| Exponent | Lower endpoint | Upper endpoint |
| --- | --- | --- |
| k | 0.17936052 | 0.17936054 |
| a1 | -0.641279 | -0.641278 |
| a2 | -1.461919 | -1.461918 |
| d | -1.820640 | -1.820639 |
| a3 | -2.282558 | -2.282557 |

For every T>=max(exp(tplus),L,1), explicit finite angular counterterms at
a1,a2,d, multiplied by a polynomial radial cutoff, give a new trial rhoT.
A compact annular correction sets its canonical strain change to exactly
zero. Its density is unchanged on r<=T. The new trial satisfies the
kinematic P2 requirements with c_l=1/k and center factor one, but has not
been proved stationary.

Its true canonical residual epsilonT obeys, for each fixed T,

 epsilonT=O(r^(4k-3)(1+log r)^12),
 ||epsilonT||_(dot H^-1)<=||r epsilonT||_2<infinity.

The finite constant and onset radius depend on T. There is no numerical
ceiling or smallness claim for either norm. The negative norm is the dual
of compactly supported smooth tests with gradient L2 norm at most one.
Odd angular parity gives an explicit L2 tangential vector field whose
divergence is epsilonT. The residual is integrable and its total integral
is zero automatically.

In the weighted factor norm with W=(1+(r/L)^2)^((k-3)/2), the distance obeys

 ||(rhoT-rho0)/(x^2 y W)||_infty
   <= C1 T^(k-1)+C2 T^(2k-2)+Cd T^(-2) -> 0.

C1<0.334616 was independently enclosed in topic105. C2 and Cd are finite
exact expressions from the two new angular rows and are unevaluated.
The correction is not in unweighted L2 because its nonzero a1 row is the
same as in105. Its difference from the105trial at the same T is in L2.

These cancellations are sufficient. The nonzero coefficients that would
make both new cancellations necessary have not been proved here. The
leading r^k angular profile remains unchanged, so the proved separation
from X3 remains. E rhoT is still outside dot H^-1. No full linear inverse,
nonlinear closing inequality, exact stationary profile or decisive
endpoint follows.
