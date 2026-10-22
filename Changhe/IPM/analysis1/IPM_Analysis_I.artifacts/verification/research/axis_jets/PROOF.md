# Axis transport jets and endpoint compatibility

Topic58. Independent audit of J3-J7 in the lead's global_flow note. The algebraic obstructions below concern the transport part of the linearization. They are not an obstruction to the coupled IPM operator or to a profile. This proof precedes its executable checks.

## 1. Geometry, traces and hypotheses

Let rho be even in x and odd in y, U=(-psi_y,psi_x), -Delta psi=rho_x, and V=c_l X+U. Put c_str=psi_xy(0). Assume the normalization c_l=(1+c_str)/3. Whenever the required derivatives exist, parity and divergence give

    V1(x,y)=w(x)+w2(x)y²+..., V2(x,y)=mu(x)y+...,
    w'(x)+mu(x)=2c_l.

At the normalized center, DV(0)=diag(-A,D), where A=2c_l-1 and D=4c_l-1=2A+1. We assume A>0. Fix L>0 with w(L)=0 and w'(L)=A_P>0. On the segment 0<x<L suppose w<0, w has no other zero, and w is C3 up to both endpoints. For the local exponent statements C2 suffices near L, and mu=2c_l-w' is C1. At zero use odd w=-Ax+O(x³) and mu=D+O(x²).

For a sufficiently regular parity perturbation h, write b(x)=h_y(x,0) and f(x)=(V.grad h-h)_y(x,0). Differentiating once in y gives the exact equation

    T b := w b'+(mu-1)b=f.                                  (1)

Indeed V1_y(x,0)=V2(x,0)=h_x(x,0)=0. This derivation needs the indicated classical derivatives, or an explicitly specified continuous trace realization. No trace theorem for an arbitrary weighted completion is being asserted.

If the underlying density is an exact solution and g(x)=rho_y(x,0), then Tg=0. If g(L) is nonzero, evaluation at L implies mu(L)=1, hence A_P=2c_l-1=A. This is conditional on nonzero g(L); positivity at L does not follow from normalization at zero alone.

## 2. The P-row and its norm

Suppose b is C1 at L. Then (1) gives

    f(L)=(mu(L)-1)b(L).                                     (2)

The same follows if b is continuous at L and w b' tends to zero there. At an exact profile with g(L) nonzero, T cannot be onto a forcing class that contains a function with f(L) nonzero, if every solution in its domain has this regularity. This is an algebraic failure of surjectivity, independent of the size of a numerical residual.

There is a necessary normalization in any quantitative version. Let X,Y be specified normed spaces of b and f, with bounded evaluation functionals e_X,e_Y at L, e_X nonzero. If S:Y->X is a bounded right inverse of T and m=mu(L)-1 is nonzero, then (2) says e_Y=m e_X S. Therefore

    ||S|| >= ||e_Y||/(|m| ||e_X||).                          (3)

For m=0 and e_Y nonzero there is no right inverse. If both evaluation norms equal one, (3) reduces to 1/|m|. Merely saying that evaluation is bounded does not justify that numerical constant. For example on scalar spaces with T b=m b, ||b||_X=epsilon |b| and ||f||_Y=|f|, the inverse norm equals epsilon/|m|, while both evaluations are bounded. This refutes an unconditional norm lower bound independent of the chosen norms.

For the full linearization, define W[h]=U[h]+(c[h]/3)X with c[h]=psi[h]_xy(0). If g=rho_y and g'=rho_xy, parity gives at P=(L,0)

    (L_full h)_y(P) = m b(L)+g(L) partial_y U2[h](P)
       +g'(L) U1[h](P)+(c[h]/3)(g(L)+L g'(L)).               (4)

Each term follows by differentiating W[h].grad rho once. Thus (2) cannot be used to give an inverse pole for the coupled operator. The required coupling traces and their domain are separate questions.

## 3. The center coefficient

Let h=beta x²y+o(r³), with grad h=beta grad(x²y)+o(r²). Under V=(-Ax,Dy)+O(r³),

    V.grad h-h = (-2A+D-1) beta x²y+o(r³)=o(r³).             (5)

Thus the cubic forcing coefficient for this transport realization must vanish. The homogeneous cubic coefficient is a normalization. For a base density rho=x²y+o(r³), the coupling term has the same cancellation: its linear velocity is diag(-2c[h]/3,4c[h]/3)X, whose action on x²y is zero. This does not establish solvability at higher orders or at P.

## 4. Homogeneous solutions and what normalization removes

For x on either side of L, write s=x-L. Since w=A_P s+O(s²), mu-1=m+O(s),

    (mu-1)/w=m/(A_P s)+O(1).

Every nonzero homogeneous solution of (1) on that side is

    b(x)=C |s|^delta exp(E_P(x)), delta=-m/A_P,              (6)

where E_P has a finite limit and bounded derivative. If 0<delta<1 the zero extension at P is continuous and is not C1 for C nonzero. The derivative of the leading term is C delta sign(s)|s|^(delta-1) times a nonzero limiting factor; the bounded logarithmic derivative of that factor cannot cancel it.

At zero, the same equation gives b'/b=2/x+O(x). Hence a homogeneous solution on the connected inner interval has

    b(x)=C_0 x² exp(E_0(x)), E_0(x)->0.                     (7)

A prescribed coefficient lim b/x² fixes C_0. In particular a zero coefficient removes the inner homogeneous mode. The claim that normalization at zero does not remove it is false if it refers to this inner interval. What remains true is that normalization at zero does not control a separate outer homogeneous branch glued by zero at P when only continuity is required and delta>0. Such a branch vanishes on x<=L, is nonzero on x>L, and does not meet a C1 domain at P when delta<1. The domain must therefore be stated before any kernel count.

For sufficiently differentiable coefficients and a Taylor solution at P, coefficient comparison gives diagonal denominators

    m+n A_P, n=0,1,2,... .                                 (8)

The order n coefficient also contains lower Taylor coefficients. Formula (8) alone does not imply an analytic solution or convergence of a formal Taylor series.

## 5. The normalized inner inverse at m=0

Assume now mu(L)=1, so A_P=A. Define the positive homogeneous solution H on (0,L) by H/x²->1 at zero. Formula (7) constructs it. Near L, (mu-1)/w=(A-w')/w is bounded, because w is C2 and w'(L)=A. Consequently H extends with a positive finite value H_L and a bounded derivative at L.

Variation of constants gives the unique solution with b/x²->0 at zero,

    b(x)=H(x) integral_0^x f(t)/(w(t)H(t)) dt, 0<x<L.       (9)

For example f=O(x4) makes the integrand O(x) near zero, so the integral exists and b/x² tends to zero. This is a formula on the open interval. To conclude a finite endpoint value one also needs convergence at L. A sufficient condition is the Dini condition

    integral_(L-epsilon)^L |f(t)|/(L-t) dt < infinity.        (10)

Since H tends to a positive number and w is comparable to -(L-t), (10) gives absolute convergence in (9). Positive Hoelder vanishing |f(t)|<=C(L-t)^alpha with alpha>0 suffices. If f is C1 and f(L)=0, then f/w has a finite limit f'(L)/A. The equation b'=f/w-((mu-1)/w)b then gives a continuous derivative at L. A global extension beyond P or a growth condition at infinity requires further work.

Continuity and f(L)=0 alone do not imply (10), nor a bounded b. Here is an explicit counterexample consistent with the center and P slopes. Take L=1 and any A>0, and set

    w=A x(x²-1)/(1+x²), mu-1=A-w', H=x²/(1+x²).             (11)

Direct differentiation gives w'(0)=-A, w'(1)=A and w H'+(A-w')H=0. On a left neighborhood of 1 let

    f(x)=1/log(e/(1-x)).

Multiply this by a nonnegative smooth cutoff equal to zero near zero and one near 1, and define f(1)=0. The forcing is continuous, is O(x4) at zero, and satisfies f(1)=0. But near 1,

    f/(w H) ~ -2/[A(1-x) log(e/(1-x))].

Its integral diverges to minus infinity: substituting u=log(e/(1-x)) gives integral du/u. Thus (9) is unbounded. J7 is underspecified as to its target space. Its open-interval formula is valid. This example refutes an endpoint or bounded-inverse interpretation whose only endpoint assumption is continuous f(P)=0.

A precise weighted bound can be stated without pretending it is finite. For positive weights u,v on (0,L), put ||b||_u=sup|b|/u and ||f||_v=sup|f|/v. Then (9) implies

    ||b||_u <= M(u,v)||f||_v,
    M(u,v)=sup_(0<x<L) |H(x)|/u(x)
                        integral_0^x v(t)/|w(t)H(t)| dt.    (12)

This is a bound only when the displayed integrals for each x and the supremum are finite. In the full weighted measurable class the constant is sharp, because w<0 and the kernel has one sign: f=v has norm one and gives ||b||_u=M(u,v), even if the supremum over spatial points is not attained. No sharpness claim is made for an arbitrary smaller domain with extra regularity. Finiteness of M does not in general require v to be Dini at L if u is allowed to diverge there; condition (10) concerns a finite endpoint value.

For model (11), choose u=x² and v=x4(1-x²). The normalized integral has constant

    M = sup_(0<x<1) [x²/2+x4/2+x6/6]/[A(1+x²)] = 7/(12A).  (13)

Indeed v/|w H|=x(1+x²)²/A. The bracketed quotient is increasing in x: writing z=x², its derivative is (2z³+6z²+6z+3)/(6(1+z)²)>0. For the polynomial forcing f=v, the resulting rational b is smooth on the closed interval, and its weighted norm is exactly7/(12A). Its spatial maximum is achieved only at the endpoint after extension, but the supremum norm has that value also on the open interval. This explicit example verifies (12), not an inverse bound for the numerical profile.

## 6. Conditional block estimate

Let X=X_r direct-sum X_J and Y=Y_r direct-sum Y_J, both with sum norms and a specified realization, and suppose the operator matrix is

    T = [ T_r B ; 0 T_J ].

Specify domains D_r in X_r and D_J in X_J. Assume two-sided inverses T_r^-1:Y_r->D_r and T_J^-1:Y_J->D_J, bounded in the stated X norms by M_r,M_J. Assume B:D_J->Y_r satisfies ||BJ||_Y_r<=b_*||J||_X_J. The zero lower-left block, and hence preservation of the remainder space under the operator, is a hypothesis. It does not hold for the coupling merely because it holds for transport. For f=(f_r,f_J), solving gives J=T_J^-1 f_J and r=T_r^-1(f_r-BJ). Hence

    ||r||+||J|| <= M_r||f_r||+(1+M_r b_*)M_J||f_J||,
    ||T^-1|| <= max(M_r,(1+M_r b_*)M_J).                    (14)

This proves J6 under these block hypotheses. For an extension E and jet operator T_J, the expression B=T E-E T_J is a legitimate off-diagonal block only if it maps into the stated remainder space and the projections give the displayed matrix. The required extension, commutator bound, compatible jet inverse and source-to-remainder norm are not proved by (14). C4,nu velocity regularity alone cannot be used as an estimate of six classical normal derivatives.

## 7. Verdict scope and verification plan

The trace identities, algebraic compatibility, conditional norm bound, Frobenius exponents with the stated C2 hypotheses, center cancellation and block estimate are proved above. The unconditional numerical inverse lower bound, the statement that center normalization never removes an inner homogeneous mode, and the endpoint version of J7 with only continuous f(P)=0 are refuted as written. The corrected formula (9) is valid on the open interval and reaches P under the stated extra condition. No numerical-profile jet inverse, global realization or PDE endpoint follows.

Executable evidence will check the exact Taylor coefficients, all normalizations, rational model (11), the increasing kernel bound, and the polynomial forcing whose solution has weighted supremum norm (13). Any numerical illustrative constant will be computed by Arb and a separate mpmath.iv path, with exact endpoint comparisons. Actual Opus5.5 review and source hashes will be retained.
