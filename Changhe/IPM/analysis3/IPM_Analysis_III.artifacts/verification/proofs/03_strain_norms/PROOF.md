# Direct bounds for the raw central strain

Status: analytical estimates proved below. These bound c by correction norms. They do not supply an estimate of c by the linearized forcing without an additional inverse argument.

## 1. A local weighted moment

Let 1<=p<=infinity, R>0, and let h be measurable on the disk B_R. Define

    M_{p,R}(h)=||h/r^3||_{L^p(B_R)}.

For 1<p<infinity let p'=p/(p-1). Whenever this norm is finite,

    |c_near[h]| <= C_p R^{2/p'} M_{p,R}(h),
    c_near[h]=(1/pi)integral_{B_R} h sin(3theta)/r^3 dX,
    C_p=(1/pi)[sqrt(pi) Gamma((p'+1)/2)/Gamma((p'+2)/2)]^{1/p'}.
                                                                    (1)

At p=1 the bound is M_{1,R}/pi. At p=infinity it is 2R^2 M_{infinity,R}/pi. In particular

    |c_near[h]| <= R M_{2,R}(h)/sqrt(2pi).                (2)

Proof: apply Holder to h/r^3 and sin(3theta). The angular integral over a full circle is 2sqrt(pi) Gamma((q+1)/2)/Gamma((q+2)/2) for q=p'; this follows by reducing to four quarter periods and using u=sin^2 theta in the beta integral. The radial integral is R^2/2. The limiting p=1 and p=infinity constants follow from the essential supremum one and the angular absolute integral four. This proof also gives absolute convergence.

For an unweighted L^2 exterior correction,

    |c_far[h]| <= ||h||_{L^2(r>R)}/(2sqrt(pi)R^2),         (3)

because the squared L^2 norm of sin(3theta)/(pi r^3) on r>R is 1/(4pi R^4). A profile growing like r^k is not an unweighted L^2 function. Such a tail cannot be inserted into (3).

## 2. Boundedness on the diagnostic weighted Hilbert space

Fix L>0 and k<1/2. Set

    w(r)=L^6 r^{-6}(1+r^2/L^2)^{3/2-k},
    ||h||_X^2=integral [|h|^2+r^2|grad h|^2]w(r)dX.

Here X is the real space of functions with Cartesian weak first derivatives and finite displayed norm. Reflection conditions may be imposed as a closed subspace. Define c by its absolute density-kernel integral. Then

    |c[h]| <= ||h||_{L^2(w)}/[L^2 sqrt(pi(1-2k))],        (4)
    |c[h]| <= ||h||_X/[L^2 sqrt(11pi(1-2k))].             (5)

The scalar in (5) is an explicit upper bound, not asserted to be optimal. No pointwise origin jet is needed to define this continuous extension of c.

For (4), weighted Cauchy-Schwarz applies because

    integral [sin(3theta)/(pi r^3)]^2 / w(r) dX
       =1/[pi L^4(1-2k)].

The angular integral is pi. Substituting u=r^2/L^2 in the radial integral gives integral_0^infinity (1+u)^{k-3/2}du=1/(1/2-k), proving the formula. In particular the integral defining c converges absolutely for every h in X.

To improve the constant, let

    a(r)=(1/pi)integral_0^{2pi} h(r,theta)sin(3theta)dtheta.

On compact annuli the usual polar weak derivative formulas and Fubini's theorem apply. Orthogonal projection onto sin(3theta) yields

    ||h||_X^2 >= pi integral_0^infinity [10a(r)^2+(ra'(r))^2]w(r)r dr.   (6)

The coefficient ten is one from h and nine from its angular derivative. Also c[h]=integral a(r)/r^2 dr. The same weighted Cauchy-Schwarz calculation proves both integral |a|/r^2 and integral |a'|/r finite. Integration by parts with smooth cutoffs at zero and infinity therefore gives

    integral a'/r dr = integral a/r^2 dr = c[h].          (7)

For completeness, take cutoffs in log r with uniformly bounded logarithmic derivative. Their derivative error is bounded by a fixed constant times integral |a|/r^2 over the two escaping annuli, which tends to zero. All remaining terms converge absolutely. This justifies (7) without presupposing classical endpoint values.

Combine the two equal integrals as

    c[h]=(1/11)integral r^{-2}(10a+ra')dr.

At each r, the squared dual norm of the coefficient vector (10,1) for the quadratic form 10a^2+(ra')^2 is 100/10+1=11. Apply Cauchy-Schwarz using (6). The remaining scalar integral is

    integral_0^infinity r^{-4}/[w(r)r]dr=1/[L^4(1-2k)].

This proves (5).

## 3. Relation to the canonical derivative

For locally C^{2,alpha} densities with vanishing jets through degree two, sublinear tails and the canonical velocity, the integral equals psi_xy(0) by proof 01. Formula (5) extends that quantity continuously to X. A pointwise normalization J(h)=lim h/(x^2y) is a different functional and is not made continuous by boundedness of c.

On any space where Lh is defined, (5) yields |c[h]|<=C_X ||h||_X. The further inequality |c[h]|<=C||Lh||_Y does not follow. In particular a rank-one inverse formula using c is legitimate on X as a bounded functional only when the remainder of the operator, its inverse and the coefficient vector also have compatible domains and ranges.

## Dependencies and scope

The sole analytic ingredients are the kernel in proof 01, Holder and Cauchy-Schwarz inequalities, elementary beta integrals, and Fourier projection on a circle. The numerical value of L or k has not been used. The restriction k<1/2 is necessary for the displayed full-plane dual integral; other tail spaces can have different thresholds. Neither a positive local adjoint gap nor a global inverse has been established here.
