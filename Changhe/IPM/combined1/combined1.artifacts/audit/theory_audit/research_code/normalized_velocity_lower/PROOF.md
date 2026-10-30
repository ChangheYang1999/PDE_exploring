# The universal endpoint velocity obstruction survives normalization

Status: new theorem offered for independent review. This proof is written
before its finite symbolic and interval checks. It strengthens the domain
statement of T4-381; it does not assume that any test function is stationary.

## 1. Statement and notation

Let -5<q<-3, a=-q, and define

    H_q(h)=max{sup_X (1+|X|)^a |h(X)|,
               sup_X (1+|X|)^(a+1) |grad h(X)|}.

Use the canonical velocity U[h]=(psi_xy,-psi_xx), Delta psi=h, with
Biot-Savart kernel K and its derivative DK as in T4-335. For integrable
first moments put M[h]=integral X h(X) dX. The origin normalization is
c[h]=partial_y U2[h](0). Fix beta>0 and R0>0. Suppose E is a constant
such that

    |U[h](X)+DK(X)M[h]| <= E H_q(h)|X|^q,       |X|>=R0,    (1)

for every real smooth S1 function h satisfying H_q(h)<infinity,
||h||_2<=beta, c[h]=0, and integral |X h(X)| dX<infinity.
Here S1 means even in x and odd in y. Then

    E >= (a-1)/(2a(a-3)).                                  (2)

The same conclusion holds without the L2 restriction. Thus imposing the
origin normalization and an arbitrarily small positive L2 budget alone
cannot improve the universal constant below (2). This statement does
not impose the stationary equation or the full selected fractional X
ball, and draws no conclusion about estimates using those extra inputs.

## 2. A smooth normalized sequence

For R>=1 define

    f_R(x,y)=y (R^2+x^2+y^2)^(-(a+1)/2)/a.

This is smooth, S1, and has finite first absolute moment because a>3.
Its tail is f_R=r^(-a) sin(theta)/a+O_R(r^(-a-2)), with the analogous
bounds after two polar derivatives. Choose the smooth compact cutoff

    eta(s)=exp(1-1/(1-s)) for 0<=s<1, and eta(s)=0 for s>=1,
    b(x,y)=y eta(x^2+y^2).

Then b is smooth S1, supported in the closed unit disk, and b_y(0)=1.
Both f_R and b are pure first sine modes. The exact contact identity is

    c[g]=-g_y(0)/4+(1/pi) PV integral sin(3theta)g/r^3 dX.

The integral is zero on each centered annulus for a first sine mode.
Consequently c[f_R]=-R^(-a-1)/(4a), c[b]=-1/4, and

    k_R=f_R-R^(-a-1)b/a                                  (3)

has c[k_R]=0 exactly. This calculation retains the contact term.

The radial and angular gradient components of f_R are

    (R^2-a r^2)(R^2+r^2)^(-(a+3)/2) sin(theta)/a,
    (R^2+r^2)^(-(a+1)/2) cos(theta)/a.

Since |R^2-a r^2|/(R^2+r^2)<=a and a>1, their Euclidean norm is
at most (R^2+r^2)^(-(a+1)/2). Cauchy-Schwarz gives

    (1+r)/sqrt(R^2+r^2) <= sqrt(1+R^(-2)).

It follows that

    H_q(f_R) <= C_R=(1+R^(-2))^((a+1)/2),
    H_q(k_R) <= C_R+R^(-a-1)K_q/a,                         (4)

where K_q=H_q(b)<infinity. For a concrete bound, 0<=eta<=1 and
sup |eta'|=4/e<4, so |grad b|<=1+8/e<5 and K_q<=5*2^(a+1).
The amplitude component of H_q(f_R) is at most
(1/a)(1+R^(-2))^(a/2)<=C_R. Along the positive y-axis at infinity
the weighted gradient of k_R tends to one. Thus H_q(k_R)>=1, and
(4) proves H_q(k_R) tends to one as R tends to infinity.

The exact scaling f_R(X)=R^(-a) f_1(X/R) yields
||f_R||_2=R^(1-a)||f_1||_2. Equation (3) and the triangle inequality
therefore show ||k_R||_2 tends to zero. Every fixed beta>0 admits all
sufficiently large R. No lower bound on an admissible L2 radius is used.

## 3. Canonical velocity and conclusion

For h=F(r)sin(theta), the canonical mode-one potential is

    psi=-sin(theta)/2 [r^(-1) integral_0^r s^2 F(s)ds
                              +r integral_r^infinity F(s)ds].

For F(r)=r(R^2+r^2)^(-(a+1)/2)/a, its leading tail is r^q/a.
Integrating that leading term in the two exterior integrals gives

    psi=-m_R sin(theta)/(2pi r)
          +r^(q+2) sin(theta)/(a(q+1)(q+3))+O_R(r^q),       (5)

with controlled derivatives through order two and m_R=integral y f_R.
For example m_R=2pi R^(3-a)/(a(a-1)(a-3)); its precise value is not
needed for the limit. This follows by substituting u=r^2/R^2 in the
radial moment integral. The first term of (5) produces -DK M[f_R].
For the compact first sine mode b, the exterior potential equals its
mode-one dipole exactly, so U[b]+DK M[b]=0 when r>1. Equation (3)
therefore leaves the following limit unchanged:

    r^(-q)(U[k_R]+DK M[k_R]) tends, at theta=pi/4, to a vector
    of magnitude (a-1)/(2a(a-3)).                          (6)

For completeness, the homogeneous vector divided by r^q is

    (cos(theta)[1+(q-1)sin(theta)^2],
     -sin(theta)[1+(q-1)cos(theta)^2])/(a(q+3)).

Its magnitude at pi/4 is exactly the right side of (6).
Apply (1) to each sufficiently large R, then let r tend to infinity.
This gives E H_q(k_R)>=(a-1)/(2a(a-3)). Finally let R tend to infinity
and use H_q(k_R) to one. This proves (2).

## 4. Scope and dependencies

For the campaign q=1/c-4, the bound is 0.793036506422514088... .
The T4-380 critical constant for the fixed sharpw L2 radius is below
0.785064. If the endpoint inequality is based on a universal estimate
on the smooth normalized L2 class just specified, its obstruction
therefore persists. The T4-381 retained-error integral remains an
upper bound on what that particular CI can certify, with all its
reference and finite-radius hypotheses retained.

Dependencies are the canonical kernel and contact identity, the
mode-one Green formula, and T4-381's homogeneous differentiation.
The present proof rederives the normalized-domain extension. It does
not prove a stationary weighted budget, rule out smaller CI radii,
rule out a stationary-only constant, or provide an inverse estimate.
