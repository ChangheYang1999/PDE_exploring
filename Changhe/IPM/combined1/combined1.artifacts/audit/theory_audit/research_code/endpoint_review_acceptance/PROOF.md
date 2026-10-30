# Acceptance of the endpoint gradient and universal velocity reviews

Status: independent acceptance of the analytic review of T4-375 and the
independent derivation of the universal lower constant in T4-381 Sections
1 and2. The sharper delta-integral formula in381 Section3 and the smooth
normalized extension384 are separate review items.

## 1. Gradient theorem and proof

Let q<0, h in C1(R2), and

    H=max{sup (1+|X|)^(-q)|h(X)|,
          sup (1+|X|)^(1-q)|grad h(X)|}<infinity.

Assume b in C1(S1) and r^(-q)h(r,theta) tends to b(theta) uniformly
in theta. Then at every theta

    |b(theta)|<=H,
    sqrt(q^2 b(theta)^2+b'(theta)^2)<=H.                    (1)

Indeed h_R(X)=R^(-q)h(RX) converges uniformly on compact annuli to
f(X)=|X|^q b(arg X). Its gradient is bounded by
H(|X|+1/R)^(q-1). On a ball B(X0,epsilon) avoiding zero this gives
a Lipschitz constant H(|X0|-epsilon+1/R)^(q-1). Pass to the uniform
limit, differentiate the C1 function f at X0, and let epsilon tend
to zero. At unit radius grad f has polar components(qb,b'). The
amplitude assertion follows directly by taking the original limit.
This proof neither differentiates the asymptotic remainder nor assumes
that grad h has an asymptotic expansion.

For the stationary endpoint theorem335, retain all its canonical chart,
reference growth and remainder assumptions and its finite-H hypothesis.
Write c>1, gamma=1/c, delta=1-gamma, q=gamma-4 and

    b=(A+(m/pi)P)/(4c),
    B_j=min_t ||A+tP||_j/(4c),
    ||v||_0^2=integral v^2,
    ||v||_1^2=integral(q^2 v^2+v'^2),

where A,P are C1 on the full circle, P is nonzero and m=integral y h.
Integrating(1) gives H>=B_1/sqrt(2pi). For odd sine polynomials,
orthogonality gives

    (4cB_j)^2=pi[sum w_n a_n^2
                         -(sum w_n a_n p_n)^2/sum w_n p_n^2],

with w_n=1 for j=0 and w_n=q^2+n^2 for j=1. The weights imply
B_1>=sqrt(q^2+1)B_0 by comparing norms before taking the minima.

Let B_0>0, G>=g0>0 and E>0 be a valid velocity remainder constant.
In the registered CI351 all error terms are nonnegative, including
H E G r^(-delta)/D, D=1-c(q-delta)>0. Therefore its positive part
vanishes for r<=(E G B_1/(D B_0))^(1/delta). Bounding the remaining
positive part by B_0 gives the cap

    cap=B_0(E G B_1/(D B_0))^((q+1)/delta)/sqrt(-2q-2).     (2)

Since q+1<0, replacing G by g0 enlarges the cap. Solving cap>=beta
for E yields exactly T4-375(5). The cap concerns this particular
certificate, not the true solution distance. Finite starting radius
and the other error terms only reduce the certificate.

The frozen T2 review independently checks every step above, the exact
weighted projections, their direction of comparison and all stored
specialization values. Its Sections1(a)-(d) CONFIRM375 Sections1-4.
The original uniform endpoint theorem and its three-cutoff application
were already audited. Thus375 is now AUDITED.

## 2. Independent universal lower bound

Let -5<q<-3 and a=-q. Suppose the canonical velocity inequality

    |U[h]+DK M[h]|<=E H_q(h) r^q,   r>=R0,

holds for every real centrally odd C1 h of finite weighted norm H_q,
with a fixed R0>0. It also suffices to quantify over the S1 subclass.
Use the genuine C1 test h=y(1+r)^(q-1)/a. Its weighted amplitude is
at most1/a, and its weighted gradient is

    (1/a)sqrt[((1+q r)/(1+r))^2 sin(theta)^2+cos(theta)^2].

It is at most1 and tends to1 on the y-axis, so H_q(h)=1. The finite
moment is M=(0,m), where

    m=6pi/[a^2(a-1)(a-2)(a-3)].

For h=F(r)sin(theta), the canonical potential is

    psi=-sin(theta)/2 [r^(-1) integral_0^r s^2F(s)ds
                                      +r integral_r^infinity F(s)ds].

Here F=r^q/a+O(r^(q-1)). Replace the first integral by its total
minus its tail. Direct integration gives

    psi=-m sin(theta)/(2pi r)
       +r^(q+2)sin(theta)/(a(q+1)(q+3))+O(r^(q+1)).

The derivative bounds through order2 follow by differentiating these
explicit radial integrals. The first term has velocity -DK M. The
homogeneous remainder has velocity divided by r^q equal to

    (cos(theta)[1+(q-1)sin(theta)^2],
     -sin(theta)[1+(q-1)cos(theta)^2])/(a(q+3)).

At theta=pi/4 its norm is(a-1)/(2a(a-3)). Letting r tend to infinity
in the assumed inequality proves

    E>=(a-1)/(2a(a-3)).                                    (3)

The T2 review R4 derives this result independently with controlled
Green-function errors and a separate symbolic and numerical check.
It agrees with T4-381 Sections1-2, whose exact and interval checks
already exist. The analytic statement(3) is AUDITED in both directions.
It does not by itself assert that the test is normalized or stationary.
The separate normalized construction384 still awaits peer review.

## 3. Excluded review inferences and numerical scope

The finite-angle determinant lower bound of review R2 was independently
confirmed in380. It is valid at a point where(qP,P') is nonzero; at a
zero vector one instead uses sqrt(q^2 A^2+A'^2)/(4c). The review's
floating minimax agreement does not prove a saddle point, the exact
maximum of Phi, or that the pointwise necessary condition exhausts the
full minimax problem. Those implications are not accepted. Nothing in
375 or380 needs them.

The common crude cap in R4 must be rounded upward to1.2485e-6:
013 gives1.248414615...e-6, so a common bound1.2484e-6 is too small.
This repair changes no comparison with the fixed sharpw radius
1351/1024000000 or with any displayed family ceiling.

The proposed upper E<=1.749109 remains a separate audit. It is not
required for(3) or for comparing the lower constant with the critical
fixed-sharpw value below0.785064. The review was first frozen at the
real time in verification/manifest.json. Its prose claimed a writing
interval ending10:40Z while the observed clock was before10:20Z; that
future endpoint is not accepted as runtime evidence.
