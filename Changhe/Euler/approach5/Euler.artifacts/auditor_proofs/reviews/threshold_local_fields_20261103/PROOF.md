# Local fields at and below strain-ratio thresholds

Status: CONFIRMED for the explicit local-field statements below. This audits Theory Agent C C63, source SHA256 296301a13e3ea3a5b6100d32c058613150fe010d8e74162d152ff6122a948a9e, retained in the team records. These are not common-flat-point fields or global Euler profiles.

## 1. Exact local equations and claims

Fix 0<c<1/2, omega real, Jx=e3 cross x, A=cI-omega J, X=Ax and L=(1-c)I+omega J. Set a=1-2c, b=2(1-c), eta=a/b and q=b/a. Thus a>0, b-a=1, q>2 and q-1=1/a. For smooth V,S on an open set avoiding the origin write

    W=curl V, E=|V|^2, P=S+E/2, k=X.V, M=sym DV,
    div V=0, k=0, X.grad V=-LV, X.grad S=-bS,
    grad k=X cross W-aV, W.grad S=0,
    -Delta P=tr((DV)^2).                                  (L)

The derivative convention is (DV)_ij=partial_j V_i. Matrix norms are Frobenius norms. These equations include the local pressure equation. They do not include global decay or the flat-point assumptions: a flowbox about an orbit Gamma with S=0 on Gamma, S<0 off Gamma, and infinite-order vanishing of V,S at its central point. On S<0 put H=-S and R=E/H.

There are two families. First, for every omega there are explicit fields satisfying (L), with S<0, E>0, W!=0, R constant and

    |M|^2=(1+4omega^2)|W|^2/(2a^2),
    |grad E|=sqrt(b^2+4omega^2)|W||V|/a.                     (1)

For omega=0 these fields attain the first-jet threshold |M|^2=|W|^2/(2a^2) and grad log R=0. Second, for omega=0 and every mu>0 there are analytic local fields satisfying (L), with S<0, V!=0, W!=0, |M|^2<mu|W|^2 and tr((DV)^2)<0 on a ball. The statements and constructions are proved directly below; numerical checks are not needed.

## 2. The constant-ratio fields for every omega

Use cylindrical coordinates rho>0, theta, z=x3 and their oriented orthonormal frame e_r,e_theta,e3. On a ball avoiding the axis choose a smooth branch of theta. Set

    sigma=c^2+omega^2,
    gamma=1+ac/sigma, nu=a omega/sigma,
    u=A0 rho^(-gamma) exp(nu theta), A0 real and nonzero,
    V=u(omega e_r+c e_theta),
    P=-sigma gamma u^2/[2(gamma^2+nu^2)], S=P-E/2.           (2)

Since gamma>1, these are smooth, indeed real-analytic on a chosen local branch, and u never vanishes. The algebraic relations

    c nu=omega(gamma-1),
    c(gamma-1)+omega nu=a,
    c gamma+omega nu=1-c

follow immediately from sigma=c^2+omega^2. Cylindrical differentiation gives

    div V=(u/rho)[omega(1-gamma)+c nu]=0,
    W=(u/rho)[c(1-gamma)-omega nu]e3=-(au/rho)e3,
    E=sigma u^2, k=0, X cross W=aV.

The scalar derivative Xu=-(c gamma+omega nu)u=-(1-c)u and the frame derivatives Xe_r=-omega e_theta, Xe_theta=omega e_r give XV=-LV. Also X(u^2)=-b u^2, hence XS=-bS. Since S is independent of z and W is parallel to e3, WS=0. Thus every first-order identity in (L) holds.

In the moving orthonormal frame the full derivative matrix is

    DV=(u/rho)[[-omega gamma, omega nu-c, 0],
               [-c gamma, c nu+omega, 0],
               [0, 0, 0]].

Its trace is zero and its planar determinant is -sigma gamma u^2/rho^2. Therefore tr((DV)^2)=2sigma gamma u^2/rho^2. Meanwhile

    Delta(u^2)=4(gamma^2+nu^2)u^2/rho^2.

Substitution in (2) proves -Delta P=tr((DV)^2), completing the check of (L), including pressure rather than only pointwise kinematic data.

Finally

    S=-sigma u^2(gamma^2+nu^2+gamma)/[2(gamma^2+nu^2)]<0,
    R=2(gamma^2+nu^2)/(gamma^2+nu^2+gamma).

This is constant. Since gamma>1, gamma^2+nu^2>gamma, and hence 1<R<2 and P<0 throughout the domain.

## 3. Exact strain and energy-gradient identities

The diagonal entries of M are -omega gamma u/rho and omega gamma u/rho. Its one off-diagonal pair equals [omega nu-c(1+gamma)]u/(2rho). Thus

    |M|^2=(u/rho)^2[4omega^2 gamma^2+(omega nu-c(1+gamma))^2]/2.

Let Z=omega nu-c(1+gamma)+2i omega gamma. Using sigma=(c-i omega)(c+i omega) and 2c+a=1 gives

    Z=-(c-i omega)(1+2i omega)/(c+i omega).

The quotient (c-i omega)/(c+i omega) has modulus one, since c>0. Hence |Z|^2=1+4omega^2. Comparing with |W|^2=a^2u^2/rho^2 proves the first identity in (1).

Next grad u=(u/rho)(-gamma e_r+nu e_theta), so

    |grad E|=2E sqrt(gamma^2+nu^2)/rho,
    |W||V|=aE/(sqrt(sigma)rho).

The identity

    sigma(gamma^2+nu^2)=sigma+2ac+a^2=(1-c)^2+omega^2

proves the second part of (1). It also follows that tr((DV)^2)=[1+4omega^2-a^2]|W|^2/(2a^2)>0 for this family. The strictly negative stress examples in Section5 are a different family.

## 4. The zero-rotation endpoint

If omega=0, then nu=0 and gamma=(1-c)/c. Formula (2) defines fields on every open set avoiding the axis, without choosing theta, and

    V=cA0 rho^(-(1-c)/c)e_theta,
    R=2gamma/(gamma+1)=b,
    grad log R=0, |M|^2=|W|^2/(2a^2).

Because H is a positive constant times u^2,

    grad log H=2grad log|u|=-2gamma e_r/rho,
    |grad log H|=b/(c rho).

The absolute value in log|u| is needed when A0<0; writing log u there is only a notational slip in the submitted proof, not a restriction on the theorem. Since X=cx,

    b/|X|<=|grad log H|,
    sqrt(2)|M||X|>=|V|,

and equality in either holds exactly at z=0. Indeed |M|=|u|/(sqrt(2)rho), |V|=c|u|, and |x|>=rho with equality precisely there.

At mu0=1/(2a^2), the constants from C62 are theta=eta(1+sqrt(2mu0))=eta(1+1/a)=1 and theta1=a sqrt(2mu0)=1. If e=grad log E and h=grad log H, then e=h, so e.h=|h|^2 everywhere; the other C62 inequality b/|X|<=theta1|h| is equality at z=0. Thus the endpoint directional obstruction is realized by actual fields satisfying (L).

For c<=1/3, q<=4 and mu0=(q-1)^2/2<=9/2. The sharp matrix constant of LIT294 in this range is C(mu)=1+sqrt(2mu), giving C(mu0)=q. Formula (1) gives |grad E|=q|W||V|, so its endpoint eta C(mu0)=1 is attained by these fields. No such claim is made here for the other branch of the matrix constant when c>1/3.

## 5. Analytic local fields with arbitrarily small positive ratio

Let omega=0, t=z/rho and m=-(1-c)/c. Then m+1=-a/c, m-1=-1/c and q(m+1)=2m=-b/c. Let g>0 be an analytic function on an interval I. Define on rho>0, t in I

    Psi=rho^(m+1)g(t),
    V=rho^m g(t)e_theta=Psi grad theta,
    S=-Psi^q=-rho^(2m)g(t)^q,
    P=rho^(2m)F(t), F=g^2/2-g^q.                         (3)

Here grad theta=e_theta/rho is a globally defined vector field off the axis even though theta need not be a single-valued scalar. Axisymmetry and azimuthal velocity give div V=0 and x.V=0. Homogeneity gives XV=cmV=-(1-c)V and XS=2cmS=-bS. Also W=grad Psi cross grad theta, so WS=0. Directly, if v=rho^m g(t),

    W=-v_z e_r+(v_r+v/rho)e3,
    x cross W=-(z v_z+rho v_r+v)e_theta=-(m+1)V.

Thus X cross W=-c(m+1)V=aV and every first-order equation of (L) holds for arbitrary positive g.

The stress is particularly simple: (V.grad)V=-(v^2/rho)e_r, so

    tr((DV)^2)=div((V.grad)V)
               =rho^(2m-2)(2t g g'-2m g^2).

For any real exponent d and smooth F,

    Delta(rho^d F(z/rho))
       =rho^(d-2)[(1+t^2)F''-(2d-1)tF'+d^2F].

This follows by differentiating twice in rho, adding rho^(-1)partial_rho, and then differentiating twice in z. Hence the pressure equation is exactly

    (1+t^2)F''-(4m-1)tF'+4m^2F+2t g g'-2m g^2=0,
    F=g^2/2-g^q.                                          (4)

The coefficient of g'' is (1+t^2)(g-q g^(q-1)). At g=1 it is (1+t^2)(1-q), which is nonzero since q>2. Thus near any t0>0 and the initial data

    g(t0)=1, g'(t0)=-1/(c t0),

(4) is an analytic ordinary differential equation g''=Phi(t,g,g'). Analytic local existence supplies a solution; shrink its interval to keep g>0. This is an actual analytic solution of the full local equations (L), not just formal Taylor data.

At x*=(1,0,t0), v=1, v_r=m-t0g'=1 and v_z=-1/(c t0). The only derivative entries are DV_(r,theta)=-v/rho, DV_(theta,r)=v_r, DV_(theta,3)=v_z. Therefore

    |M|^2=[(v_r-v/rho)^2+v_z^2]/2=1/(2c^2 t0^2),
    |W|^2=(v_r+v/rho)^2+v_z^2=4+1/(c^2 t0^2),
    |M|^2/|W|^2=1/(2+8c^2 t0^2),
    tr((DV)^2)=|M|^2-|W|^2/2=-2.

Given any mu>0, choose t0>0 with 2+8c^2t0^2>1/mu. The ratio is then strictly below mu at x*. By continuity a smaller ball avoids the axis and has S<0, V!=0, W!=0, |M|^2<mu|W|^2 and tr((DV)^2)<0 throughout. This proves the second family asserted in Section1.

## 6. Consequences, dependencies and limits

Section5 shows that the small-ratio exclusions of C61, C62 and LIT294, for positive mu, cannot be deduced from (L) at an arbitrary point with S<0. Their common-flat-point hypotheses are essential to those deductions. Section4 gives a stronger endpoint method test than arbitrary first jets: for omega=0, the pressure equation and all of (L) hold on a neighborhood, R is constant, and the threshold ratio is attained. For every delta>0, a direction Z with Z(log H)>0 then satisfies

    Z(log R+delta log H)=delta Z(log H)>0.

Consequently the desired opposite directional sign is impossible there, for every mu>=mu0. For general omega the constant-ratio family gives this obstruction when mu>=(1+4omega^2)/(2a^2); it does not settle the intervening interval for nonzero omega.

The full C63 source, both supplied verification scripts and both complete logs were read. The numerical scripts use high-precision evaluation and a finite Taylor approximation; their names do not make them exact proof certificates. Their small residuals are supplementary checks only and were not used to prove analytic existence, identities or universal parameter ranges. No source script or new computation was executed in this audit. The first family also independently verifies the earlier C56(e2) dependency over the enlarged range0<c<1/2. The only existence input for Section5 is the local analytic ODE theorem with explicitly nonvanishing highest-derivative coefficient.

None of these examples belongs to the common-flat class: S<0 everywhere on its domain, and the first family is singular at the axis. They supply no profile smooth on all space, no global decay theorem, no counterexample to the campaign conjecture, and no endpoint sharpness result with a common flat point. Those conclusions remain OPEN. The submitted phrase realizing the pointwise data of C62 is understood as realizing their endpoint mechanism e=h and the indicated inequalities; it is not a claim to realize every arbitrary matrix chosen in that remark.
