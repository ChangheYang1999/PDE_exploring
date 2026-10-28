# The local moment, frozen representer and bounded central strain

This audits the fixed theory author draft in `evidence/lead_snapshot.md`. It proves the
moment and representer formulas and certifies the displayed constants. The
bordering identity is conditional on an actual operator domain, specified
below. It does not prove the missing edge estimate or a global inverse.

## Definitions and hypotheses

Let k=1615536043799051/9007199254740992, ell=1/k, A=2ell-1,
D=4ell-1=2A+1, and b0=ell+1. Let P be the class of real functions even in x
and odd in y. Put V0=(-Ax,Dy) and T0=V0.grad-1.

For 5/2<a<9/2, 0<=b<3/2, a+b>4, put sigma=a+b-4 and
w_ab=|x|^(-2a)|y|^(-2b). Write R=L2_P(w_ab),
D_R={u in R:V0.grad u in R}, and G=L2(exp(-2sigma t)dt).
The space Z_O consists of

    h=x^2 y beta(log r)+u,
    beta(t)=J+integral_{-infinity}^t v(s)ds,
    (J,v,u) in R x G x D_R,

with squared norm |J|^2+||v||_G^2+||u||_R^2+||V0.grad u||_R^2.
The target F consists of x^2 y gamma(log r)+f, with gamma in G and f in R,
and the squared sum norm. Proof 20 proves uniqueness of these decompositions,
closedness, and the inverse of T0 selected by J=0, provided
kappa=b0+aA-bD>0. We use those results at exactly that scope.

For densities for which the integral converges, define

    c[h]=(1/pi) integral h(X) sin(3theta) r^(-3)dX,
    c_<[h]=the same integral over r<1,
    c_>[h]=the same integral over r>1.

For the abstract spaces below this is an integral extension, not an assertion
that every representative has a classical derivative at the origin.

## The local moment and the signs of the boundary fluxes

Let 1<=p<infinity and let Q={|x|<Rx, |y|<2R}. Suppose V is C1 on a
neighborhood of its closure, is tangent to both coordinate axes, and
has div V=2ell. Put w=|x|^(-ap)|y|^(-bp). Let h and
f=(V.grad-1)h belong to Lp(Q,w), with the derivative understood
distributionally on the quadrants. Let phi(y) be1 on |y|<=R,
2-|y|/R on R<|y|<2R, and0 outside. Define

    kappa_w=1+2ell/p-a V1/x-b V2/y.

The ratios extend continuously to the relevant axes by C1 tangency.
The renormalized transport identity is

    integral kappa_w |h|^p w phi
      =-integral f |h|^(p-2)h w phi
        +Flux_in/p-integral |h|^p w V2 phi'/p.           (1)

For p=1 use sign(h), set to0 where h=0. For smooth functions the identity
follows by differentiating |h|^p and using

    div(V w phi)=p(kappa_w-1)w phi+w V2 phi'.

There is no flux through the axes. To justify this for the stated graph
domain, first cut off where |x| or |y| is less than epsilon. The derivative
of each cutoff along V is bounded uniformly, because V1=O(x), V2=O(y).
Its integral against |h|^p w tends to0 by absolute continuity. Apply the
one-dimensional chain rule in C1 flow coordinates on the remaining compact
subsets, or local smooth approximation of that identity. This proves the
renormalization step also for p=1. Finally approximate the sides |x|=Rx
from inside by cutoffs chi_delta(x). In (1) their contribution is

    Flux_in=-lim_{delta->0} integral |h|^p w phi V1 chi_delta'.

The limit exists because the other terms converge to finite integrals. It
agrees with the weighted transport trace on noncharacteristic sides.
When V1/x<=0, chi_delta' has the opposite sign to x, so Flux_in<=0.
This definition avoids presupposing an unweighted classical trace of h.

If also V2/y>=0, Delta=essinf_Q kappa_w>0 and
Vhat=esssup_{R<|y|<2R}V2/y is finite, define

    N=(integral |h|^p w phi)^(1/p),
    Fp=||f||_Lp(Q,w phi), Hs=||h||_Lp({R<|y|<2R},w).

Dropping the nonpositive flux and using |V2 phi'|<=2Vhat on the shell gives
Delta N^p<=Fp N^(p-1)+(2Vhat/p)Hs^p. If
N>Fp/Delta+(2Vhat/(p Delta))^(1/p)Hs, then
N^(p-1)(Delta N-Fp)>(2Vhat/p)Hs^p, a contradiction. Thus

    ||h||_Lp({|x|<Rx,|y|<R},w)
      <=N<=Fp/Delta+(2Vhat/(p Delta))^(1/p)Hs.           (2)

For V0, Delta=1+2ell/p+aA-bD and Vhat=D. The shell term is essential in
this local argument. Its norm is not made small by taking the box small.
The grid values in the submitted draft are not certified by this proof.

## The frozen adjoint representer

Let omega=(1/pi)sin(3theta)r^(-3)1_{r<1}. Proof 20 gives

    T0_R^(-1)f(X)=-integral_0^infinity e^(-s)f(Phi_s X)ds,
    Phi_s(x,y)=(x e^(-As),y e^(Ds)).

The integral converges in R with norm at most||f||_R/kappa. The functional
c_< is bounded on R with norm C_R, where

    C_R^2=2[9 B(a+1/2,b+3/2)-24 B(a+1/2,b+5/2)
              +16 B(a+1/2,b+7/2)]/[pi^2(2a+2b-4)].

Consequently duality and Fubini, first on finite s intervals and then by
absolute integrability bounded by C_R ||f|| exp(-kappa s), yield

    c_<[T0_R^(-1)f]=integral f(Y) phi_R(Y)dY,
    phi_R(Y)=-integral_0^infinity e^(-(A+2)s)
                         omega(Y1 e^(As),Y2 e^(-Ds))ds. (3)

Here the Jacobian is e^(-(D-A)s)=e^(-(A+1)s). The dual element phi_R lies
in L2(w_ab^(-1)), with norm at most C_R/kappa. It solves

    [-V0.grad-(A+2)]phi_R=omega

on the quadrants in the distributional sense: pair with T0 of a compact
smooth test and use (3) and the inverse property. Its support is contained
in the forward hull of the unit disk. That hull lies in
{|x|<1, |x|^D |y|^A<1}. Neither boundedness at the origin nor positivity
of this signed full-plane representer is needed for (3).

For h in Z_O, J=0, and T0h=x^2 y gamma(log r)+f, Proof 20 gives
v=gamma/D and
u=T0_R^(-1)[f+(A+D)x^2 y cos^2(theta)gamma(log r)/D]. Therefore

    c_<[h]=integral [f+(A+D)x^2 y cos^2(theta)gamma(log r)/D] phi_R dX
           +(1/(8D))integral_{-infinity}^0(1-e^(2s))gamma(s)ds. (4)

Both terms are absolutely convergent dual pairings in the stated spaces.
This is the submitted representer formula; it is not a bounded angular
solution of the separate homogeneous adjoint problem of proof 14.

## Explicit frozen constants and the combined norm

Set

    C_v=1/[8 sqrt(sigma(sigma+1)(sigma+2))],
    C_ang^2=2 B((9-2a)/2,(3-2b)/2),
    C_F=C_R/kappa,
    C_gamma=C_v/D+C_R(A+D)C_ang/(D kappa),
    C_c0=sqrt(C_F^2+C_gamma^2).

The inverse formula, the triangle inequality and Cauchy-Schwarz give

    |c_<[h]|<=|J|/8+C_F||f||_R+C_gamma||gamma||_G.

For J=0 the last two terms are at most C_c0||T0h||_F. Independent
384-bit Arb evaluation from the exact original k gives the certified bounds

    a=7/2,b=6/5: C_F<0.0027316, C_gamma<0.0136875,
                 C_c0<0.013958;
    a=17/4,b=0:  C_c0<0.017231.

Longer enclosures, including every intermediate constant, are in
`evidence/check.json`. The submitted value0.0172306 is a rounded
approximation; it is smaller than the true C_c0 and is not an upper bound.

Let mu(0)=0 be continuous piecewise affine, with positive-side breakpoints
3/2,7/4,3,4,5,6,7,8,9,10 and consecutive slopes
(4,17,28,27,25,18,4,-10,-17,-19,-20)/16. Put W=e^(mu(log r)).
Cauchy-Schwarz and integral_0^(2pi)sin^2(3theta)dtheta=pi give

    |c_>[h]|<=C_far ||h 1_{r>1}||_L2(W),
    C_far^2=I/pi, I=integral_0^infinity e^(-4t-mu(t))dt.  (5)

On each finite interval [l,u], with slope m and mu(l) known, the contribution
is e^(-4l-mu(l))(1-e^(-(4+m)(u-l)))/(4+m). The final half-line has the
same formula with the parenthesis replaced by1. Every exponent and endpoint
is an exact rational. Independent interval arithmetic proves

    0.23521843509529822746<I<0.23521843509529822747,
    0.27362812959108157464<C_far<0.27362812959108157465.

More generally mu(t)>=-M_- t for t>=0 gives
C_far<=[pi(4-M_-)]^(-1/2), if M_-<4. The normalization mu(0)=0 is needed.

Take any fixed smooth radial chi1,1 on r<=1 and0 on r>=2. Define

    Z_cap={h in L2_P(W):chi1 h in Z_O},
    ||h||_Zcap^2=||chi1 h||_ZO^2+||h||_L2(W)^2.

This is a Hilbert space. A Cauchy sequence converges in both displayed
Hilbert factors, and both limits agree as local distributions, since Z_O
embeds continuously in L2 on compact annuli and locally in distributions at
0. Thus the multiplication constraint remains closed. J is a bounded
coordinate, and (5) with the local bound of proof 20 gives

    |c[h]|<=sqrt(1/64+C_v^2+C_R^2+C_far^2)||h||_Zcap.    (6)

For a=7/2,b=6/5 this constant lies strictly between
0.31209282223719315977 and0.31209282223719315978. Hence0.312093 and0.31210
are valid upper bounds; the submitted0.3120928 is only a rounded
approximation. For a=17/4,b=0 a valid upper bound is0.359253.
The annular unit-strain sequence of proof 29 cannot tend to0 in this space,
by (6). That is the precise distinction from the radial Lfix graph.

## Conditional rank-one bordering, with target membership

Let rho be the exact normalized modal trial, Gbar=X.grad rho and
Lfix=V.grad-1+U[.] .grad rho. Its tail is r^k Theta plus terms
O(r^(2k-1)); the differentiated versions of these bounds hold. Let
Phi=chi_inf r^k Theta and KP=chi_inf r^k log r Theta, where chi_inf is
smooth, vanishes near0, and equals1 for all sufficiently large r. Let chi0
be smooth, compact, and equal1 near0. Put

    Y={f in L2_P(W):chi1 f in F},
    gfar=(1-chi0)Gbar-k Phi,
    yKP=Lfix KP+(c[KP]/3)chi0 Gbar-ell Phi.              (7)

Then gfar and yKP belong to Y. At infinity the terms remaining in (7) are
O(r^(2k-1)(1+log r)); their squared weighted radial integral converges
because4k<5/4. Phi and KP are not in L2(W), because2k-5/4+1>-1.
Near0, KP vanishes and U[KP]=c[KP](-x,y)+O(r^3). The leading cubic
coupling cancels exactly against c[KP]Gbar/3, leaving a function of the form x^2 y a(X), with a=O(r^2), even in both
coordinates, smooth away from0 with uniformly bounded second derivatives
on a small punctured disk. These bounds follow directly from the inner
finite angular expansion; C2 regularity at the point0 is not asserted. Such a
function belongs locally to F: take gamma(log r)=a(0,r) and subtract
x^2 y gamma. The remainder is O(x^4 y), since the even coefficient with those derivative bounds
obeys |a(x,y)-a(0,r)|<=C x^2. Its angular integral is finite for a<9/2,
b<3/2, and its radial integral is finite for a+b<6. The gamma term is in
G since sigma<2. Compact annuli are treated with the same axis subtraction.
This verifies the anisotropic membership, beyond the far power counting.

To state an operator theorem, let X be a Banach operator domain continuously
embedded in Z_cap, and assume explicitly that

    Lren h0=Lfix h0+(c[h0]/3)chi0 Gbar

is bounded from X to Y. Neither this hypothesis nor closedness of a proposed
variable-coefficient realization follows merely from the definition of
Z_cap. They are among the edge/domain questions left open in the theory author draft.
For h=h0+q KP the exact identity is

    Lh=Lren h0+q(ell Phi+yKP)
                +(c[h0]+q c[KP])(k Phi+gfar)/3.

Since Phi is not in Y, this belongs to Y exactly when

    d q=-k c[h0], d=3ell+k c[KP],                       (8)

provided Lren h0 is in Y. If d!=0, the constrained space is the closed
graph of the bounded scalar map q=-k c[h0]/d. Under its identification
with X the reduced operator is

    Lred=Lren+c[.] zeta, zeta=(ell gfar-k yKP)/d in Y.   (9)

A bounded rank-one perturbation preserves Fredholmness and index. If
Lren is invertible, (9) is invertible exactly when
1+c[Lren^(-1)zeta]!=0; solve for c[h0] in the equation to obtain this
condition and the usual rank-one inverse. The condition d!=0 alone
concerns (8); it does not certify invertibility of (9).

The physical total strain is

    c[h]=(3ell/d)c[h0].                                (10)

Consequently the bound obtained from a reduced inverse is

    |c[h]|<=(3ell/|d|) C_cap ||Lred^(-1)|| ||Lh||_Y.     (11)

The factor in (11) cannot be discarded for an arbitrary signed tail or
cutoff. For the present tail it can be bounded by1, as verified next.

## A simple certified denominator for the actual tail

Let s3=integral sin(3theta)Theta(theta)dtheta. Exact trigonometric projection
of Phi_m=cos^2(theta)sin(theta)cos(2m theta) gives coefficients
(1/4,1/8,-1/8,-1/8) for m=0,1,2,3, and0 thereafter. Thus the exact original
far coefficients A_m0, their common endpoint t+, and the certified scalar
repair z of proof 04 give

    s3/pi=e^((3-k)t+)[A_00/4+A_10/8-A_20/8-A_30/8+z/4].

Independent Arb recomputation proves

    37.63077494715565<s3/pi<37.63077494715567.

For any smooth0<=chi_inf<=1 supported in r>=R>=1,

    0<=c[KP]=(s3/pi)integral chi_inf(r)r^(k-2)log r dr
      <=(s3/pi)R^(k-1)[log R/(1-k)+1/(1-k)^2].

In particular d>=3ell>0 and3ell/d<=1. Even the absolute-value sufficient
test at R=1 holds, since k(s3/pi)/(1-k)^2<10.022251<3ell. Thus R=1
already suffices for this denominator certificate. There is no need to
estimate the entire angular L1 norm or to use a discontinuous cutoff.
The transition interval is covered by0<=chi_inf<=1. This denominator
certificate is independent of the still-open edge estimate and inverse.

## Scope corrections

A continuous cubic jet does not by itself force an anisotropic weight.
The weight obstruction in proof 22 applies to the specified coercive
product/conic L2 mechanism. It is not a theorem about every Banach space
with a continuous J; sufficiently strong isotropic Sobolev spaces also
have continuous point jets.

A scalar estimate |c[h]|<=C||Lh|| does not logically require a full inverse
bound for L. It can hold on a noninjective operator when c annihilates its
kernel. The exact dual criterion is developed in proof 32. Accordingly the
absence of a global inverse is not by itself a proof that no separate
strain estimate is possible.

Dependencies: topics01,04,20,22,29 and the exact modal construction.
No source-point theorem, finite section, or numerical grid is used here.
