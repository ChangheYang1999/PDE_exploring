# Flat periodic carriers: period, local backgrounds and transport countermodels

Status: CONFIRMED at A587-A589, with the explicit local/global scope below. The full coordinator check and all432 lines of the inner answer have been read. Existing outer model review is the coordinator's actual written check; the failed inner Bedrock request is not counted as a successful model consultation.

## 1. Exact setting and period consequence

Let0<c<1/2, a=1-2c, kappa=1+c, A=cI-omega J and Jq=(-q2,q1,0). A full profile means C2 velocity U and C1 single-valued pressure P, with div U=0 and

    (1-c)U+DU(Aq+U)+omega JU+grad P=0.

Put B=Aq+U, W=curl U, H=P+|U|^2/2+Aq.U and g=U.B. In the target interval2/5<c<1/2, the witness theorem A571 concerns global decaying helicity-free profiles and a selected nonconstant flat periodic B-orbit Gamma in the closure of {W!=0}, with U!=0, g0 and W=DW=0 there. Its normal rates are rho and mu=3c-rho, with rho<=-2a or rho>=2-c.

Every nonconstant periodic B-orbit in a local full profile, not just these witnesses, satisfies omega!=0 and T>=2pi/|omega|. By the Kelvin identity, its U-circulation is invariant under the carrier reparametrization and also multiplied by exp(-as); hence it is zero. For q'=B(q) this gives

    E+omega A_Gamma=0,
    E=integral_0^T |q'|^2dt>0,
    A_Gamma=integral_0^T Jq.q'dt.

Subtracting the mean of q and applying Cauchy-Schwarz and periodic Wirtinger gives |A_Gamma|<=T E/(2pi). This proves the claims and sign(A_Gamma)=-sign(omega). A_Gamma is twice the signed projected area, counted with multiplicity. In particular omega0 removes W2 from A571, leaving equilibrium witnesses. Equality requires a horizontal circle traversed with angular velocity -omega. This is the exact combination of A030 with A571; no new dynamical premise is added.

For a witness, the same energy-area identity also follows directly from g0: |B|^2=Aq.B=cq.B-omega Jq.B and the radial derivative integrates to zero.

## 2. Exact harmonic circle backgrounds

For omega!=0, R>0 and any real rho, put b=rho/2, k=c-b, mu=3c-rho and use cylindrical radius r. Define on r>0

    phi=k(z^2-r^2/2)-bR^2 log(r/R),
    U0=grad phi,
    P0=-a phi-|U0|^2/2-Aq.U0+C.

The cylindrical Laplacian of phi is2k-2k=0. The identity

    grad H+aU-B cross W
       =grad P+(1-c)U+DU B+omega JU

shows that this gives an analytic full local profile with W0. Direct differentiation gives

    U0=(-kr-bR^2/r)e_r+2kz e_z,
    B0=b(r-R^2/r)e_r-omega r e_theta+mu z e_z.

The circle r=R,z=0 has B0=-omega R e_theta, U0=-cR e_r, g0=0 and grad g0=rho U0. The radial derivative of B0 is2b=rho there, the vertical rate is mu, and the phase rate is zero. Its period is2pi/|omega|. The rates and the stated covector law follow either from this diagonal variational system in its rotating frame or by direct differentiation. These profiles have no vorticity in the tube and fail the campaign's global decay assumptions.

## 3. A second-jet obstruction for this specific family

Suppose a full C2 profile has the same U derivatives through order2 as U0 at every point of that circle, and suppose rank grad H cross grad g=0 holds on its open vortical set near the circle, which lies in that set's closure. The rank premise is supplied by global helicity freedom and sublinearity through A413; it is not a theorem for arbitrary local germs.

Let K=grad H cross grad g. Momentum makes grad H=-aU+B cross W, so K is C1 even at the stated C2 velocity regularity. On the open vortical set both K and DK vanish. Continuity gives K=DK=0 at the circle. Their values there depend only on the indicated velocity jets: grad H uses U and DU; its derivative uses up to D2U; grad g and its derivative use the same orders. They therefore equal the jets of -a grad phi cross grad g0.

Here

    g0=(-kr-bR^2/r)b(r-R^2/r)+2k mu z^2.

At r=R one has phi_r=-cR, phi_z=2kz, (g0)_r=-2bcR and (g0)_z=4k mu z. Hence

    phi_r(g0)_z-phi_z(g0)_r
       =-4ckR(mu-b)z
       =-12cR k^2 z
       =-3cR(rho-2c)^2 z.

The normal derivative of K is nonzero unless rho=2c. The two witness ranges exclude that value. Consequently no such matching through order2 is possible. The source assumes C-infinity; C2 suffices with this explicit rank premise. In particular infinitely flat perturbations of this one background are excluded. Infinite flatness of W alone neither supplies a convergent harmonic background nor classifies all possible velocity jets.

## 4. Annular first integrals and the correct level map

On a regular H tube set x=H-h0 and write vol=dx wedge j(theta,x,y)dtheta wedge dy, W=w partial_theta+v partial_y. The absence of an x-component follows from WH=0. The actual curl identity div W=0 gives partial_theta(jw)+partial_y(jv)=0. If v(theta,x,0)=0, define

    F(theta,x,y)=integral_0^y j(theta,x,s)w(theta,x,s)ds.

Then F_y=jw and F_theta=-jv. It is periodic and single valued. Its annular differential equals contraction of j dtheta wedge dy with W. Thus regular vortex orbits are the connected regular level components of F; compact ones are circles. The tangency at y0 removes the possible annular flux obstruction. Completeness of the global vorticity flow does not prevent an orbit from exiting this local tube.

A Floquet rate supplies a linearization, not an exact nonlinear level map. If additionally Bx=b(x) throughout the tube, let zeta_t be that scalar flow. The exact leaf area law is

    Phi_t^*sigma_(zeta_t(x))=exp(3ct)/zeta_t'(x) sigma_x.

Combining it with [B,W]=-kappa W gives

    d_ann(F_(zeta_t(x)) composed with Phi_t)
        =exp(-at)/zeta_t'(x) d_ann F_x.

With F normalized to zero on an invariant reference cylinder, the additive constant vanishes. The special multiplier exp(-(a+rho)t) requires b(x)=rho x; it is not implied by the rate rho alone. These formulas preserve open level curves and do not force a closed one.

The finite first transverse term and analytic exclusion are already A559-A560. Their no-closed-vorticity-orbit premise is essential and is supplied by A014 only in the global class. The infinite-flatness conclusion on both invariant cylinders follows by Cauchy transport in the appropriate direction: if forward stable distance<=C exp(-eta t), then |W(q)|<=C_N exp((kappa+L-N eta)t); choose N large. On the unstable cylinder use backward time, with exponent L-kappa-N eta. These estimates do not control passage orbits that leave in both directions.

## 5. Explicit infinitely flat intrinsic countermodels

On S1 times(-delta,delta)^2 with coordinates(theta,x,y), period2pi and volume dx wedge dtheta wedge dy, let

    D=partial_theta+rho x partial_x+mu y partial_y,
    W=F_y partial_theta-F_theta partial_y,
    mu=3c-rho.

Then div D=3c, div W=0 and Wx=0. Differentiating in theta and y shows that DF=(mu-kappa)F implies [D,W]=-kappa W.

Write Q(s)=1-cos s. In the positive witness range rho>=2-c, mu<0, set b=-mu/rho>0, s=(mu-kappa)/rho, and

    F=x^s exp[-1/(x^(2b)y^2)] Q(theta-log x/rho)

for x>0,y!=0, with zero extension elsewhere. The two arguments x^b y and theta-log x/rho are D-invariant, so the required equation holds. At fixed x the amplitude strictly increases with |y|. Positive levels are graphs of |y| over proper angular intervals because Q vanishes on a ray, where W also vanishes. No regular level is a circle.

In the negative range rho<=-2a, mu>0, set b=-rho/mu>0, s=(mu-kappa)/mu>0, and

    F=y^s exp[-1/(x^2y^(2b))] Q(theta-log y/mu)

for y>0,x!=0, with zero extension elsewhere. Now x y^b and theta-log y/mu are invariant. On a fixed x annulus use tau=theta-log y/mu. The amplitude A_x(y) has

    A_x'(y)=A_x(y)/y [s+2b/(x^2y^(2b))]>0.

Every positive level is a graph in y over a proper tau interval; zero rays are curves of stationary points. There are again no closed nonstationary W-orbits.

Each derivative is a finite sum of monomials in possibly negative powers of x,y times bounded derivatives of Q and the same exponential. The estimate exp(-1/z^2)<=C_N |z|^N, with arbitrarily large N, absorbs those powers uniformly on a small box. Both zero extensions are C-infinity and flat to every order on both coordinate cylinders. Nonzero points approach every point of the central circle. In particular smoothness, Holder or Dini bounds for derivatives do not restore the missing finite leading term in the annular argument.

These are intrinsic transport examples. They do not satisfy the full Euclidean profile equation.

## 6. Their explicit failure of incompressibility for the associated velocity

Set beta_form=-(1/a)i_D i_W vol. Since i_W vol is closed, Cartan's formula and div D-kappa=-a give

    d beta_form=i_W vol,
    L_D beta_form=-a beta_form,
    L_W beta_form=0.

Assign H=x and g=-rho x/a; then DH=-ag, WH=Wg=0 and dH wedge dg0. A direct contraction gives

    beta_form=F dx+(rho/a)d(xF).

In the product metric the associated velocity one-form beta_form-dx/a is (F-1/a)dx+(rho/a)d(xF). Its divergence is

    (1+2rho/a)F_x+(rho/a)x Delta F.

On a zero ray of Q, Q'=0,Q''=1 and F_x=0. For the first example Delta F=A[1+1/(rho^2x^2)]>0, where A is its positive amplitude. For the second it is A_x(y)[1+1/(mu^2y^2)]>0. At x!=0 the divergence is therefore nonzero. The Euclidean relation B=Aq+U is also absent. Thus the examples refute a closure from the listed intrinsic identities alone; they do not refute a proof using the full Euclidean relations.

## 7. Scope of the remaining normal form

On a contractible vortical box with g=G(H-h0)!=0, A482 gives x=H-h0, f'/f=1/G and

    U=f grad psi-grad x/a,
    B psi=0, Bx=-aG,
    W=f' grad x cross grad psi,
    f Delta psi+f' grad x.grad psi-Delta x/a=0.

The converse requires all three scalar equations and B=Aq+U. It follows because B cross W=a f grad psi, so grad x=-aU+B cross W and the reconstructed P solves momentum. C3 scalar unknowns with sufficiently smooth f ensure C2 U; merely C2 scalar data generally give only C1 velocity. No gluing or nonlinear solvability theorem follows from this reduction. The general rotating flat periodic witness remains OPEN.
