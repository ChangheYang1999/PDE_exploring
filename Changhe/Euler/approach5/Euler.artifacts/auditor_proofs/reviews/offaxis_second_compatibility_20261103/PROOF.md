# Two exact off-axis tests at the next pressure order

## 1. Exact setting and conclusions

Fix c=9/20, b=11/10, eta=1/11, kappa=21/11, r=7/10 and v=2/5. Use Cartesian coordinates centered at the point in question, with

    X=(cx+ry-vz,-rx+cy,1+vx+cz).

The rotation vector in this frame is (0,v,r), with magnitude sqrt(65)/10. The carrier value at the center is e3, so the center is off the rotation axis: a point on that axis would have its carrier parallel to the rotation vector. All claims below are for these fixed parameters.

Let H>0 and phi be smooth locally and suppose

    XH=-bH, Xphi=0, V=H^eta grad phi, div V=0,
    W=curl V, E=|V|^2, P2=H+E/2,
    -Delta P2=tr((DV)^2), Z=DV V+grad P2.

A full next scalar means a C1 function p1 satisfying

    Xp1=-(b+1)p1,
    W dot grad(p1-2V dot grad P2)=0,
    Delta p1=-2tr(DV DZ),

with the last equation initially allowed in distributions. These are local leading and next-scalar equations, not the global profile equation.

For n=3 or4 let w=x+iy, rho^2=x^2+y^2 and prescribe the leading transverse potential P=Re(w^n)/n. Put

    g=6b(5n-1)v/[8b eta(n-1)+12b(3n-1)+18c(n-1)],
    h33=b(b+c)+vg, t=-h33/2+eta g^2/6,
    T=diag(t-eta g^2/3,t), gvec=(g,0), vvec=(v,0),
    u=-(b+c)gvec-r J_T gvec+b vvec,
    d=-(b+2c)u-r J_T u+T vvec-h33 vvec,
    A3=eta g^3(2eta+3)/36, J_T(x,y)=(-y,x).

The earlier pressure jets are fixed by

    H(x,y,0)=1+gx+(x,y) dot T(x,y)/2
             -rho^2(d1 x+d2 y)/8+(A3/6)Re(w^3)+O(rho^4).

The exact pairs (g,C) are

    n=3: g=924/3085, C=-143250430598/8194330725,
    n=4: g=836/2865, C=-13913341268299/613843898400.

The definition of C is the unique real coefficient canceling the previous degree n-1 residual. Section3 checks that this definition agrees with these fractions.

For n=3 there exist analytic germs satisfying the full leading system and both next-scalar transports exactly, whose next-pressure residual is O(|(x,y,z)|^4). The residual has transverse order at least four along the central orbit arc. V and W have exactly that arc as common zero set, both of order2, with full relative vorticity support.

For n=4, no smooth leading-system germ with these earlier jets admits a full C1 next scalar, regardless of its higher Cauchy data. This is an obstruction for these specified jets only. General off-axis zeros, other phases, other earlier pressure jets and other parameters are not excluded.

## 2. Jets determined by transport and the leading equations

For a scalar F of weight d0, XF=-d0F, write its successive normal derivatives on z=0 as F_m. Differentiating the carrier equation m times gives

    (1+vx)F_(m+1)=-(d0+mc+T0)F_m+m v partial_x F_(m-1),
    T0=c(x partial_x+y partial_y)-r(-y partial_x+x partial_y).

For m=0 the final term is absent. This recurrence determines every normal jet from the section value. It is the recurrence used in the independent checker.

Incompressibility is equivalent to

    Delta phi+eta H^(-1)grad H dot grad phi=0.                 (1)

Its degree n-1 section equation fixes Delta_T f_(n+1), leaving two harmonic coefficients. The next section equation fixes Delta_T f_(n+2). The latter's harmonic part does not enter the degree-n residual: its transverse Hessian is contracted with the scalar transverse matrix B(0)=3t I, while its mixed and normal Hessians have higher transverse degree.

The quartic section pressure has two free harmonic coefficients. Its trace is fixed by the leading Poisson equation and transport. For n=3 the leading velocity is

    V0=(x^2-y^2,-2xy,0), E0=rho^4, tr((DV0)^2)=8rho^2.

Hence the degree-two part of Delta H is -16rho^2. For n=4 that degree-two part is zero. This includes the quadratic velocity stress; omitting it would change the n=3 calculation.

Consequently all free coefficients relevant to the degree-n test are four real numbers (alpha,beta,h,k), multiplying respectively

    Re(w^(n+1))/(n+1), Im(w^(n+1))/(n+1),
    Re(w^4)/24, Im(w^4)/24.

The first two belong to the potential and the last two to H. The exact polynomial right inverse of Delta_T used for the particular terms is specified in the team records: integrate twice in x and subtract successive twice-y-differentiated corrections. Its identity Delta_T I(q)=q is checked on each input. A different right inverse translates the four coordinates and does not change the existence or obstruction conclusion.

## 3. Exact residual, degree counting and coefficient certificate

Define p1=2V dot grad P2+C H^kappa phi. Homogeneity gives its first transport law. The identity

    W=eta H^(eta-1)grad H cross grad phi

gives the second. The residual is exactly

    R=Delta(C H^kappa phi)+Rlin+Rcub,
    Rlin=2H^eta[Hess phi:B+grad phi dot C_H],
    B=3Hess H+(eta/H)grad H tensor grad H,
    C_H=(2eta/H)Hess H grad H
        +[(eta/H)Delta H+(eta^2/H^2)|grad H|^2]grad H
        +grad Delta H,
    Rcub=Delta(V dot grad E)+2tr(DV D(DV V))+tr(DV Hess E).

To obtain Rlin, expand the original linear terms 2Delta(V dot grad H)+2tr(DV Hess H), substitute V=H^eta grad phi and use (1). The product rule gives the displayed tensor and vector coefficients. This is an identity of the full equations.

For n=3 the leading cubic contribution is 288P. Indeed DV0 V0=2rho^2(x,y,0), and the three terms of Rcub respectively give192P,48P,48P. For n=4 all cubic terms have degree at least3n-6=6, above the tested degree.

The previous test is unchanged by the four new coefficients. To verify its scalar C directly, put

    BT=3u-eta b gvec, B33=3h33+eta b^2,
    CH=2eta(T gvec-bu)+eta^2(g^2+b^2)gvec.

Identify transverse vectors with complex numbers. Its harmonic coefficient is

    R0=2[-3t(eta g+v)-(3/2)(n-1)d_C
         +eta g(n-1)(-h33-g^2/2)
         -2n(c-ir)BT_C+B33v+CH_C].

The chosen g makes Im R0=0, and C=-R0/[(2kappa-eta)g] gives exactly the fractions in Section1. The other angular band is canceled by A3, since its coefficient is

    (n-1)[12A3-eta g^3(1+2eta/3)]=0.

At degree n the residual depends affinely on (alpha,beta,h,k). A new pressure Hessian has degree2 and a new potential Hessian degree n-1, so their product has degree n+1. Products of two new pressure terms are higher still. In cubic velocity terms any free potential perturbation raises the leading degree above n. The recursions in Section2 fix traces linearly at this order. These degree bounds prove affine dependence without reliance on sample points.

All exact coefficient data are in the team records. The independent sparse-Fraction checker reconstructs the jets, including one extra potential degree so that divergence holds through n+1, and substitutes into the original expression

    2Delta(V dot grad H)+2tr(DV Hess H)
      +Delta(C H^kappa phi)+Rcub.

It compares every three-dimensional coefficient through degree n against the retained affine map at each baseline, all four basis perturbations, one mixed parameter vector and the n=3 solution. It also recomputes g,C, verifies every lower coefficient is zero and checks the matrix ranks by exact rational row reduction. Thirteen cases pass in3.4926275978796184 actual seconds on CPU55 with OMP1 and low priority. No source script is executed. The original source scripts, helper, plans, JSON and logs were fully read; their separate runtimes are94.27941740397364 and114.11295285401866seconds.

The certificate is exact finite algebra. Its soundness follows from the stated truncation degrees, the transport recurrence, the right-inverse identity and the affine-dependence argument. Importing JSON alone would not establish it.

## 4. Solvability and the invariant missing coefficient

For n=3 the four response polynomials are

    A Re(w^3)+B0 Im(w^3),
    -B0 Re(w^3)+A Im(w^3),
    12rho^2 x, 12rho^2 y,

where A=1274311810101/234885113000>0 and B0=7161/15425. The first two span the harmonic cubics because their determinant is A^2+B0^2>0. Applying Delta_T to the last two gives independent nonzero linear polynomials, so their span is complementary to the harmonic cubics. The four responses form a basis of all cubic polynomials. Thus every baseline is canceled by a unique vector; the exact vector in the JSON is checked by substitution into the original residual. Both matrix and augmented matrix have rank4.

For n=4 the responses are

    A Re(w^4)+B0 Im(w^4),
    -B0 Re(w^4)+A Im(w^4),
    18rho^4, 0,

where A=1010572231009/188132517000>0 and B0=4774/14325. Their range is exactly the span of Re(w^4), Im(w^4) and rho^4. The linear functional that adds the coefficients of x^3y and xy^3 annihilates this range. Its value on the baseline residual is

    -5299294616/615616875 != 0.

This exact nonzero value is reproduced for every checked parameter vector and is unchanged for every vector by the proven affine structure. The matrix has rank3 and its augmentation rank4. No choice of the four free jets cancels the degree-four residual.

## 5. Why a full C1 scalar has no additional free coefficient

For the nonexistence claim let a full C1 scalar be given. Its smooth Poisson source makes p1 smooth locally by elliptic regularity. Set tau=p1-2V dot grad P2 and theta=H^(-kappa)tau. The transport laws imply Xtheta=0 and W dot grad theta=0. In flowbox coordinates the latter is equivalent to

    {f,theta}=f_x theta_y-f_y theta_x=0

on the section. Indeed dH wedge dphi wedge dtheta evaluated on X and the two section directions is XH times this bracket, and XH=-bH never vanishes.

If a nonzero homogeneous polynomial Q_d commutes with P=Re(w^n)/n, write Q_d=rho^d q(angle). On each sector where cos(n angle)!=0 the bracket equation gives

    n cos(n angle) q'+dn sin(n angle) q=0.

Thus q is a constant multiple of cos(n angle)^(d/n), with the appropriate real branch on that sector. A simple zero of cosine forces d/n to be a nonnegative integer for a nonzero polynomial: otherwise its one-sided vanishing order is not an integer. Polynomial continuation fixes the constants across sectors. Therefore Q_d is a multiple of P^(d/n).

Subtract theta(0) before using this argument. It removes all possible homogeneous terms of degrees1 through n-1. The residual at the center is then

    theta(0) kappa(kappa-1)|grad H(0)|^2.

The remaining terms vanish there: Delta H(0)=0, grad phi and Hess phi vanish for n>=3, and the cubic velocity terms vanish. The coefficient is strictly positive, so theta(0)=0.

The degree-n part of theta is C times P; the previous degree n-1 residual determines the same unique C as in Section3. Subtracting C f preserves the exact bracket relation. The polynomial argument then removes degrees n+1 through2n-1. For n=4 this means

    theta-C phi=O(|(x,y,z)|^8)

in the full flowbox, by invariant transport. Its contribution to the Poisson residual starts at degree6, above degree4. Thus a full next scalar cannot supply another degree-four coefficient. Pressure coefficients beyond degree4 and potential coefficients beyond degree n+2 do not enter the reduced residual at degree n. The unused harmonic part of f_(n+2) is annihilated as in Section2. The obstruction in Section4 therefore applies to every smooth completion of the prescribed earlier jets.

## 6. Analytic realization for n=3

Choose the unique rational parameter vector that cancels the cubic residual. These section jets are realized by analytic solutions, not merely formal series. In the analytic carrier flowbox write phi=f(x,y), H=exp(-bs)h(x,y). The divergence equation (1) solves for f_yy. After using it, the leading Poisson equation is a second-order equation affine in the second derivatives of h and solves for h_yy. The two principal coefficients at the center are one, because H=1 and grad phi=0. The analytic noncharacteristic Cauchy theorem applies on a sufficiently small initial interval.

For completeness, the removal of third derivatives uses the identity

    Delta(H+|V|^2/2)+tr((DV)^2)
      =F2+H^(2eta)grad phi dot grad F0,
    F0=Delta phi+eta grad(log H) dot grad phi,

where

    F2=Delta H+(|grad phi|^2/2)Delta(H^(2eta))
       +2grad(H^(2eta)) dot(Hess phi grad phi)
       +H^(2eta)|Hess phi|^2
       -eta H^(2eta)grad phi dot grad(grad(log H) dot grad phi)
       +tr((DV)^2).

All terms of F2 involve at most second derivatives of f,h, and its dependence on Hess h is affine. Thus solving F0=F2=0 gives the original two equations. Prescribe analytic Cauchy data with the finite jets constructed above; the recursions in Section2 are exactly the traces forced by these equations. Higher Cauchy coefficients may be chosen freely. Similarity covariance propagates the equations from the section to the flowbox.

Define p1=2V dot grad P2+C H^kappa phi. Its transports hold exactly, and its residual vanishes through degree3. The residual has scalar weight3, since b+1+2c=3, so this order propagates along the central orbit. The analytic flowbox preserves the equivalent local distance estimates.

Finally |grad P|=rho^2 for n=3, and the higher potential terms contribute O(rho^3) to its gradient. Hence V vanishes only on the central orbit and has order2 there. Because X dot grad H=-bH and X dot grad phi=0, crossing grad phi with grad H is injective on X-perp. Thus W has the same zero set and order. The punctured flowbox is dense, giving full relative support. None of this asserts that the remaining higher residual vanishes.

## 7. Verdict scope

The complete five-section source, all source scripts and helper, all retained results, the earlier seven-section first-compatibility proof and this seven-section reconstruction were checked. The numerical work is exact rational polynomial verification, with analytic realization and higher-jet independence proved separately.

The n=3 finite compatibility and the n=4 obstruction at the fixed parameters are confirmed. A full next scalar for the n=3 family, general off-axis exclusion, global tails and global decaying profiles remain open. This is neither a global counterexample nor a proof of the unrestricted conjecture. Existing configured model agent collaboration continues through shared files; actual provider execution is independently unattested. No new model client or prohibited execution was used.
