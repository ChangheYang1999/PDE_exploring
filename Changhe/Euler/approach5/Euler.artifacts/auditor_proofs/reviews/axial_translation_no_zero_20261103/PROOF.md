# Axial translation invariance, velocity zeros and full annuli

## 1. Exact local statement and notation

Let 0<c<1/2 and omega be any finite real number. Write J(x,y,z)=(-y,x,0), X=(cI-omega J)x, p=(1-c)/c>1, d=p-1, tau=omega/c, A0=1+tau², alpha=d/A0, beta=d tau/A0, a=1-2c, b=2(1-c), and q=b/a=2p/d>2. Let G be a product of connected open intervals in the one-to-one coordinates(log rho,theta,z), rho>0, theta=phi+tau log rho. Its angular interval is I.

Suppose V,P2 are smooth on G and, setting W=curl V, k=X.V and S=P2-|V|²/2, satisfy

    partial_z V=0, div V=0,
    X.grad V=-(1-c)V-omega JV, X.grad P2=-bP2,
    -Delta P2=tr((DV)²),
    grad k cross grad S=0 wherever W!=0.             (1)

If V3 is nonzero somewhere, then S=0 everywhere and V is nowhere zero on G. Helicity, scalar transport, full momentum and decay are not hypotheses. If one also assumes W.grad S=0, the conclusion that V is either identically zero or nowhere zero holds without any assumption on V3, by the planar theorem A1401-A1404.

The following proof treats arbitrarily many accumulating components and retains smoothness. Sections8-10 give additional full-annulus consequences; they do not remove axial translation invariance.

## 2. Affine axial dependence kills each scalar constant separately

Put u=V3. The first two components of W are (u_y,-u_x). If W vanishes, horizontal grad u=0; the vertical component of velocity homogeneity then forces u=0. Thus u!=0 implies W!=0.

Homogeneity gives X.grad k=-ak and X.grad S=-bS. On a small connected box with u and k nonzero, grad k cannot vanish because its X contraction is nonzero. Rank gives

    grad S=(qS/k)grad k, hence S=D|k|^q              (2)

for one real constant D. Since partial_z V=0, both |V|² and tr((DV)²) are independent of z. Thus Delta S is independent of z. Write k=n(x,y)+m(x,y)z, where m=cu!=0, n=(cx-omega Jx).V_horizontal. At fixed x,y put t=k and

    D0=grad n-(n/m)grad m, E0=Delta n-(n/m)Delta m.

All these derivatives are horizontal. Then

    grad_h k=(t/m)grad m+D0, partial_z k=m,
    Delta k=(t/m)Delta m+E0.

Differentiating(2) gives

    Delta S=Dq |t|^(q-2)(A2 t²+A1 t+Astar),
    A2=Delta m/m+(q-1)|grad m|²/m²,
    A1=E0+2(q-1)grad m.D0/m,
    Astar=(q-1)(|D0|²+m²)>0.                       (3)

For fixed sign of t, this expression is a linear combination of powers with distinct exponents q,q-1,q-2, while Delta S has exponent zero. Independence follows, for example, by writing t=sign(t)exp(r) and successively applying the operators partial_r minus the other exponents. Since q>2, the coefficient Dq Astar must be zero, so D=0. Each constant is eliminated on its own component. At a horizontal point with u!=0, the affine k has at most one axial zero; continuity therefore gives S=0 throughout {u!=0}.

## 3. Global pressure independence and the angular system

The Poisson equation implies Delta(partial_z P2)=0. On the nonempty open set {u!=0}, S=0 and partial_z V=0 imply partial_z P2=0. A harmonic function has an interior convergent power series, obtained from its Poisson representation on a slightly larger ball. Its zero propagates across overlapping balls along any path in connected G. Thus partial_z P2=0 everywhere.

Vector homogeneity now gives smooth angular functions R,T,N,s with

    V=rho^(-p)(R e_rho+T e_phi+N e3),
    S=rho^(-2p)s, P2=rho^(-2p)(E/2+s),
    K=R-tau T, L=tau R+T,
    E=(K²+L²)/A0+N²,
    L'=alpha K+beta L,
    W=rho^(-p-1)[N'e_rho+(pN-tau N')e_phi+Z e3],
    Z=-K'+beta K-alpha L,
    k=c rho^(-d)K+cz rho^(-p)N.                    (4)

Here N is nonzero somewhere, and s=0 wherever N!=0. The two horizontal components of W vanish together exactly when N=N'=0.

The third component of grad k cross grad S is affine in z. At each vortical angular point it is zero throughout the open z interval, so its constant coefficient is zero, even when z=0 lies outside G. That coefficient is a nonzero radial factor times -dK s'+2p sK'. Therefore

    K s'-q sK'=0                                  (5)

on the open vortical set. On every open irrotational interval, N=0, K'=beta K-alpha L and L'=alpha K+beta L. The velocity and the forced linear pressure ODE below have analytic solutions with their actual endpoint data. Every derivative of the defect in(5) vanishes at an internal endpoint in the closure of the open vortical set. The analytic extension from that endpoint therefore makes the defect identically zero on the interval. Every proper irrotational interval has such an endpoint, and the entire I is not irrotational since N is nonzero somewhere. Continuity covers the residual set. Thus(5) holds on all I without a component-count assumption.

## 4. Pressure equation and endpoint form

Let L_p f=A0 f''-4p tau f'+4p²f. The planar block of rho^(p+1)DV is

    M=[[tau R'-pR,R'-T],[tau T'-pT,T'+R]].

The third column of DV is zero. In tr((DV)²) the third row consequently contributes nothing, although it contributes to |DV|². Reusing the independently verified horizontal expansion A1403, Poisson is

    Q+L_p(N²/2)+L_p s=0,
    Q=KK''+(K')²+c1KK'+c2LK'+c3K²+c4KL+c5L²,
    c1=-2tau(2p+1)/A0, c2=-(p+1)/A0,
    c3=(2p²tau²+5p²+2p tau²-2p+1)/A0²,
    c4=tau(p-5)(p-1)/A0²,
    c5=(2p(p+1)+4tau²)/A0²>0.                     (6)

At K=0 and N=s=s'=s''=0 with N flat from one side, the equation becomes

    (K')²-((p+1)/A0)LK'+c5L²=0.                   (7)

Its discriminant is ((p+1)(1-7p)-16tau²)/A0²<0. Thus K'=L=0. The sign is strict for every real omega and every allowed c.

## 5. Vanishing of K and N on the nonzero-scalar closure

On a component J0 of {s!=0}, N=0 and(5) says K'=(s'/(qs))K. Therefore K is identically zero or nowhere zero on J0. In the latter case s=D|K|^q for one nonzero constant D. J0 is proper, since N!=0 somewhere supplies an open zero interval for s, so J0 has an endpoint theta0 inside I. At theta0, s=0 implies K=0. The fixed power relation and q>2 give s=s'=s''=0; every derivative of N also vanishes there. Equation(7) gives L=K'=0.

Inside this component near the endpoint put

    F=K²/2+A0s, J1=F'+(c1/2)K²+c2LK-4p tau s.

Since q>2, F>=K²/4>=0 and |s|<=C F after shrinking only this component. Equation(6) gives

    J1'=-[(c3-c2alpha)K²+(c4-c2beta)KL+c5L²+4p²s]. (8)

All of F,J1,L vanish at the endpoint. Orient t>=0 into the component. Variation of constants in the L equation and Cauchy-Schwarz give |L(t)|²<=Ct integral_0^t F. Integration of(8), followed by the definition of J1, gives

    |F'(t)|<=C(F(t)+integral_0^t F), t<=1.

The nonnegative Y=F+integral_0^t F satisfies Y(0)=0 and Y'<=C1Y, so exp(-C1t)Y is nonincreasing and Y=0. This contradicts K!=0. Orientation reversal changes no estimate.

Consequently K=N=0 on {s!=0}, and every derivative of K,N vanishes on its relative closure C in I. The complement I minus C is a nonempty open set containing {N!=0}.

## 6. Zero extension across an arbitrary closed set

On C, divergence gives L'=beta L. At a boundary point of C, all derivatives of s vanish by continuity from the complementary open set. Equation(6), with all K,N derivatives zero, gives c5L²=0 there. Thus L=0 on the boundary. Differentiating L'=alpha K+beta L inductively makes every L derivative zero on that boundary as well.

Define ell=L on C and ell=0 outside C. For each j define ell_j=L^(j) on C and zero outside. These are continuous since every boundary jet is zero. At an interior point their derivative relation is immediate. At a boundary point x, either a nearby point y lies in C, in which case the usual difference quotient of smooth L^(j) applies and tends to zero, or y lies outside C and ell_j(y)=ell_j(x)=0. Thus ell_j is differentiable there with derivative zero. Induction proves ell smooth and ell'=beta ell everywhere. It vanishes on a nonempty open interval, so the explicit linear solution ell(theta)=ell(theta1)exp(beta(theta-theta1)) gives ell=0 on all I.

Thus L=0 on C. Equation(6) implies L_p s=0 on {s!=0}, then on C by continuity, and also on its complement where s is identically zero. The constant-coefficient ODE holds throughout I and has zero data on a nonempty open interval. Uniqueness gives s=0 everywhere. This argument does not assume a regular boundary, finitely many intervals or analyticity of the original field.

## 7. Nonnegative flux rules out a velocity zero

With s=0 put

    F=(K²+A0N²)/2>=0,
    J2=F'+(c1/2)K²+c2LK-2p tau N².

Equation(6) becomes

    J2'=-[(c3-c2alpha)K²+(c4-c2beta)KL+c5L²+2p²N²]. (9)

At a velocity zero K=L=N=0, one has F=J2=0, regardless of K' and N'. On either side, variation of constants gives |L(t)|²<=Ct integral_0^t F. Equation(9) and its definition then give the same |F'|<=C(F+integral F) as above, since K²+N²<=C F. Nonnegativity forces F=L=0 on a short interval on each side. The velocity zero set is therefore both open and closed in I. A zero would make V identically zero, contrary to N being nonzero somewhere. This proves the local theorem.

## 8. Exact angular mean identity on a full annulus

Now assume the fields are smooth on a full cylindrical annulus r0<rho<r1, z0<z<z1, all phi modulo2pi, where 0<r0<r1, with the same axial independence and homogeneity. Whenever P2 is also independent of z, write its angular factor as E/2+s as above. All angular functions are2pi-periodic. Then the exact identity is

    integral_0^(2pi) s
      =-(1/(2p)) integral_0^(2pi)
                   [(3p-1)R²+(p+1)T²+pN²].       (10)

Here is a direct derivation independent of the coefficient polynomial. Since div V=0, tr((DV)²)=div((V.grad)V). The horizontal nonlinear acceleration is rho^(-2p-1) times

    B_rho=-pR²+L R'-T²,
    B_phi=-dRT+L T'.

Its divergence has angular factor -2p B_rho+tau B_rho'+B_phi'. The vertical acceleration has no z dependence and contributes zero to this divergence. Since L'=dR, integration by parts gives

    integral B_rho=-(2p-1)integral R²-integral T²,
    integral tr(M²)=2p integral[(2p-1)R²+T²].

The angular average of L_p(E/2+s) is4p² integral(E/2+s). Combining with Poisson and E=R²+T²+N² gives(10). All its coefficients are positive because p>1. Thus every nonzero field with these properties has strictly negative mean S factor, and in particular cannot have S=0 identically.

## 9. Full-annulus exclusion of any axial component

On a full annulus assume exactly(1), without initially requiring P2 independent of z. If N is nonzero somewhere, remove one angular spiral which does not remove that point. In the coordinates(log rho,theta,z), the remaining domain is a one-to-one product box whose angular interval has length2pi. Section1 applies there and gives S=0 and partial_z P2=0. Continuity extends both identities over the removed spiral, so they hold on the full annulus. Equation(10) then makes R=T=N=0, a contradiction.

Therefore every full-annulus solution of(1) has V3 identically zero. This conclusion needs neither helicity zero nor W.grad S=0. With the latter transport hypothesis, the planar theorem additionally gives that V is identically zero or nowhere zero. This is a local annular statement, not a theorem that general three-dimensional profiles must be axially independent.

## 10. Nonrotating annular classification with scalar transport

Suppose further omega=0 and W.grad S=0 on the full annulus. Section9 gives N=0. If W is nonzero somewhere, harmonic continuation gives P2 independent of z and the component argument A1404 shows that K=R is either nowhere zero or identically zero. But L=T and T'=dR have periodic angular factors, so integral R=0. A continuous nowhere-zero R on the circle has a fixed sign and cannot have zero mean. Thus R=0 and T is a constant. The field is exactly the pure azimuthal velocity Astar rho^(-p)e_phi (including the zero constant).

If W is identically zero, the linear system is R'=-dT, T'=dR. Its nonzero solutions have the form

    R=A cos(dtheta)+B sin(dtheta),
    T=A sin(dtheta)-B cos(dtheta).

They are2pi-periodic only if d is a positive integer. For the campaign interval2/5<c<1/2 one has0<d<1/2, so this branch is zero. Therefore, in that interval and at omega=0, every full-annulus solution of the stated necessary system with scalar transport has pure azimuthal velocity. This class does contain the nonzero local exact solutions A1405 and so does not imply local nonexistence. No pressure uniqueness beyond the stated equations is claimed.

## 11. Audit evidence and limits

All nine LIT235 source sections and all eleven independent sections were read. The source and hash are pinned under verification. The horizontal rational certificate from A1403 is reused; no new computation or formal build was needed. Sections8-10 are additional exact consequences, submitted for comparison through the existing configured model agents; provider runtime remains unattested. There was no new model client or delegated agent. Genuine axial dependence changes the Poisson source and destroys the independent-powers step. The unrestricted common-flat case and the whole-space conjecture remain open.
