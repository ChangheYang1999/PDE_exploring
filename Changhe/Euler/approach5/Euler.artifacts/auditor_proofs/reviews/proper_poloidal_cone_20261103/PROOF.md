# Proper poloidal zero cones, canonical pressure and the missing rank equation

Status: CONFIRMED at the exact scopes A553-A555, after complete source comparison and postread. The constructions are singular tails, never full smooth profiles.

## 1. Precise statements and notation

Fix 2/5<c<1/2, p=(1-c)/c in(1,3/2), a=1-2c=c(p-1), Jx=(-x2,x1,0), A=cI-omega J and L=(1-c)I+omega J for any finite real omega. Let D=R3 minus{0}. Spherical coordinates are r,theta,phi, z=cos(theta), s=sin(theta), w=1-z^2.

The first result constructs a smooth vector field V on D, homogeneous of degree-p and axisymmetric with no azimuthal component, such that

    div V=0, LV+DV Ax=0, W=curl V, V.W=0,
    P2=partial_i partial_j Gamma*(V_i V_j), Gamma=1/(4pi r),
    -Delta P2=partial_i partial_j(V_i V_j),
    S=P2-|V|^2/2, W.grad S=0,
    Z=DV V+grad P2, div Z=0, Z.W+V.curl Z=0.          (1)

Here P2 is the actual global canonical pressure, with no added harmonic function, is smooth on D and has degree-2p. The equation for P2 holds distributionally across0. The field k=(Ax).V and its gradient E=-aV+Ax cross W vanish on a proper open equatorial cone; V and W are nonzero there. With a suitable choice of V the deficit S has a regular equatorial zero, with grad S=-V/f and f(exp(tA)x)=exp(t)f(x), Wf=0 on that sheet. Nevertheless Z is explicitly nonzero, and V is singular at0. The statements in (1) do NOT include the actual-profile consequence

    grad k cross grad S=0 on {W!=0}.                (2)

The second result is a local obstruction to adding (2). Let I be an interval compactly inside(-1,1). Let R,H in C1(I), H'=(2-p)R, and let u in C1(I) satisfy the pressure equation of the poloidal field r^-p[R e_r+H e_theta/s] in distributions. Put h=u-(R^2+H^2/w)/2. Suppose that a nonzero constant-H interval has an endpoint b in I, with H=H0!=0 up to that endpoint, and (2) holds near b wherever W!=0. Then H cannot depart from H0 at b. No canonical normalization or global assumption is needed for this local statement.

Consequently a globally C1 axisymmetric poloidal homogeneous tail with actual Poisson and (2) has no open cone where E=0 and V!=0. Indeed a nonzero constant plateau cannot end before a pole, and continuity at the poles then forces its constant to be0. This applies to the actual natural tail of a globally helicity-free target profile, if that tail is axisymmetric and poloidal. In particular it excludes the A534 mu1 sheet within this additional symmetry class. It does not prove cone propagation for a general tail.

## 2. Poloidal construction and smoothness

Choose H in C_c^infinity((-1,1)) and set

    R=H'/(2-p),
    V_H=r^-p[R e_r+(H/s)e_theta].                   (3)

It vanishes near both axes, so the spherical formula is smooth in Cartesian coordinates on D. Direct spherical differentiation gives

    div V_H=r^-p-1[(2-p)R-H']=0,
    W_H=r^-p-1[-(p-1)H/s+sR']e_phi.                 (4)

The velocity is poloidal and its curl azimuthal, so V_H.W_H=0. Homogeneity gives DV_H x=-pV_H, vector axisymmetry gives DV_H Jx=JV_H, and 1-c=cp proves LV_H+DV_H Ax=0. Both the velocity and its eventual pressure have the twisted homogeneities for every omega.

Since (Jx).V_H=0,

    k=c r^(1-p)R,
    E=r^-p[-aR e_r-csR'e_theta].                    (5)

If H=1 on a central band, then R=R'=0 there and

    V_H=r^-p e_theta/s,
    W_H=-(p-1)r^-p-1 e_phi/s.                       (6)

Thus k=E=0, with V_H,W_H both nonzero. A nonconstant transition of H makes R nonzero somewhere, hence E nonzero by its radial component.

A particular smooth cutoff can be specified by eta(q)=exp(-1/q) for q>0 and0 otherwise, theta0(q)=eta(q)/(eta(q)+eta(1-q)), and H(z)=theta0((1/4-z^2)/(1/4-1/16)). It equals1 for |z|<=1/4 and0 for |z|>=1/2. The denominator is positive for every real q.

## 3. Canonical pressure and the exact scalar compatibility

The tensor F=V_H tensor V_H is locally integrable at0 because 2p<3, and is O(r^-2p) at infinity. For fixed x!=0 the remote second-derivative Newton kernel has magnitude O(|y|^-3), so its product with F is integrable at infinity. Near y=x the principal value and the distributional local term -delta_ij delta0/3 in partial_i partial_j Gamma are defined by Taylor subtraction of the smooth tensor. This gives a canonical P_H, not a choice of an angular solution up to a homogeneous harmonic addition.

Testing this convolution proves -Delta P_H=partial_i partial_j F_ij in distributions on all R3. The stress and pressure are locally integrable at0; their differentiated sources need not be functions there. On D elliptic regularity gives smoothness. Scaling the distributional kernel gives degree-2p, and rotation covariance gives axisymmetry. Thus

    P_H=r^-2p u_H(z).

Every axisymmetric scalar is annihilated by the azimuthal W_H. This proves W_H.grad S=0. The vector Z_H=DV_H V_H+grad P_H is poloidal and axisymmetric; its curl is azimuthal. Poisson and div V_H=0 give div Z_H=0. Both Z_H.W_H and V_H.curl Z_H therefore vanish separately. No full expansion beyond this one force has been constructed.

For completeness, no axisymmetric pressure can make (6) a profile on a whole central band. There

    Z_r=r^-2p-1[-1/w-2p u],
    Z_theta=r^-2p-1[-z/s^3-s u'].                    (7)

If the radial component vanished, u=-1/(2p w), and the polar component would be -(p-1)r^-2p-1 z/(p s^3), which is nonzero for z!=0. Thus the nonlinear equation fails. This remains true for every omega because the linear part already vanishes.

## 4. The exact pressure equation and a local regular zero

In the spherical orthonormal frame M=r^(p+1)DV_H is

    [ -pR,     -sR'-H/s,             0;
      -pH/s,    (p-1)R-zH/w,         0;
       0,        0,                 R+zH/w ].        (8)

Its trace square has the decomposition

    tr(M^2)=T'+Q,
    T=2pHR+zH^2/w,
    Q=(2p-1)[2(p-1)R^2+H^2/w].                      (9)

For example the cross-derivative part is2pHR'; differentiating2pHR contributes2p(2-p)R^2+2pHR'. Differentiating zH^2/w contributes(1+z^2)H^2/w^2+2(2-p)zHR/w. Subtraction leaves exactly the two positive terms in Q.

Write kappa=2p(2p-1) in(2,6) and L_kappa u=(w u')'+kappa u. The pressure equation is

    L_kappa u_H=-T'-Q.                              (10)

On the plateau H=1 it reduces to

    L_kappa u=-2p/w-2z^2/w^2.                       (11)

Taking local initial data u(0)=1/2,u'(0)=d!=0 gives a unique analytic solution near0. Then h=u-1/(2w) has h(0)=0,h'(0)=d. This is an exact local regular S-zero with Poisson, but this particular locally chosen pressure is not yet shown to be canonical. It yields grad S=-d r^-2p-1 e_theta on the equator.

The local integrating factor presents no maximum-principle contradiction. Put beta=(p-1)/(2p) and

    f(z)=-integral_0^z |h(q)|^-beta/(1-q^2)dq.

It is continuous and strictly decreasing because h has a simple zero and beta<1. Off that zero grad f=|S|^-beta V, with no residual radial factor since2p beta=p-1. The weak identity div(|S|^beta grad f)=div V=0 extends across the zero using its smooth flux V. The potential has no interior extremum. This explains why a local Harnack theorem alone supplies no global vanishing.

## 5. An elementary Green kernel for the canonical pressure

Let y_kappa solve L_kappa y=0, regular at z=1 with value1. With x=(1-z)/2 the series y=sum b_n x^n has

    b0=1, b_(n+1)=[n(n+1)-kappa]b_n/(n+1)^2.        (12)

It converges for |x|<1 and depends continuously on kappa in[2,6] at z=0 with all derivatives needed here. At kappa2 it is z; at kappa6 it is(3z^2-1)/2.

There is no nonzero solution regular at both endpoints for2<kappa<6. To verify this without a special-function value, the Legendre polynomials P_n satisfy L_(n(n+1))P_n=0, as follows by differentiating Rodrigues' polynomial formula. Integration by parts against a regular global solution Y gives

    [kappa-n(n+1)] integral_-1^1 Y P_n=0.

The boundary terms vanish since w=0 and the derivatives are bounded. No n(n+1) is between2 and6. The P_n span the polynomials, so uniform polynomial approximation to continuous Y forces integral Y^2=0. This proves the claim and uniqueness in (10).

The values y_kappa(0) and y_kappa'(0) cannot be0: odd or even reflection respectively would give a regular global solution. Their continuous dependence on kappa and the two endpoint polynomials therefore imply

    A0=y(0)<0, B0=y'(0)>0.                          (13)

Let y_L(z)=y(-z), y_R(z)=y(z), and D0=w(y_L y_R'-y_L' y_R)=2A0B0<0. The Green kernel is

    G(z,q)=y_L(min(z,q))y_R(max(z,q))/D0.            (14)

Its value is continuous and w(q)[G_z(q+,q)-G_z(q-,q)]=1. It is regular at each appropriate endpoint and therefore is the inverse of L_kappa. At z=0,q>0,

    G(0,q)=y(q)/(2B0).

It is even in q. Hence G(0,q) is uniformly negative near q=0, and uniformly positive on some closed interval I contained in(0,1), separated from both endpoints and0. The latter follows from y(1)=1. Its one-sided q derivatives are bounded near0 and its derivatives bounded on I. For compactly supported H, (10) gives

    u_H(0)=integral G_q(0,q)T(q)dq-integral G(0,q)Q(q)dq.  (15)

Only one integration by parts is used. G is continuous and locally Lipschitz across q0, so the derivative jump does not introduce an omitted boundary term.

## 6. Two separated pulses tune a global regular zero

Choose a fixed even smooth chi supported in(-2,2), equal1 on[-1,1], and nonconstant. Let H_b(z)=chi(z/delta). For small delta its support lies in the negative-G band and is disjoint from I. The first term of (15) is O(1), because integral |H_b H_b'| is independent of delta and integral H_b^2 is O(delta). The positive Q contribution satisfies

    -integral GQ>=C_p delta^-1 integral |chi'|^2,

where C_p>0. Indeed the R^2 coefficient is2(2p-1)(p-1)/(2-p)^2 and -G has a positive lower bound. Thus u_b(0) tends to positive infinity. Fix delta such that h_b(0)=u_b(0)-1/2>0. The forcing in (10) is even, so uniqueness gives u_b even and u_b'(0)=0.

Choose a nonconstant smooth psi supported in(-1,1), q0 interior to I, and H_f(z)=psi((z-q0)/epsilon). With epsilon small the first term of (15) again is O(1), but G is positive and the R^2 contribution to the second term tends to negative infinity. Fix epsilon such that u_f(0)<0. Its source lies to the right of the entire central band. Formula(14) then gives u_f(z)=C_f y_L(z) on that band, and exactly

    u_f'(0)=alpha0 u_f(0), alpha0=-B0/A0>0.          (16)

This is the pressure induced by the distant velocity pulse, not a harmonic term added to the pressure by choice.

Since the supports of H_b,H_f and their derivatives are disjoint, the corresponding velocities are pointwise disjoint. Set

    lambda^2=h_b(0)/[-u_f(0)]>0, H=H_b+lambda H_f.

Then the stresses add with coefficients1,lambda^2 and canonical linearity gives u_H=u_b+lambda^2u_f exactly. In the central band H=1 and the kinetic coefficient is1/(2w). Hence

    h(0)=u_H(0)-1/2=0,
    h'(0)=lambda^2 alpha0 u_f(0)=-alpha0 h_b(0)<0.   (17)

There is a smaller band whose only h-zero is0. On that sheet

    V=r^-p e_theta, W=-(p-1)r^-p-1 e_phi,
    grad S=-h'(0)r^-2p-1 e_theta.

The nonzero function f_star(r)=r^(p+1)/h'(0) gives grad S=-V/f_star, f_star(exp(tA)x)=exp(t)f_star(x), and Wf_star=0. The sheet is tangent to Ax and W and normal to V. Equation(7) now gives the explicit residual Z_r=-(1+p)r^-2p-1 at z=0. This proves the exact canonical construction, without any numerical root finding.

## 7. The rank obstruction at the edge of a nonzero plateau

We prove the second statement at the C1 velocity scope stated in Section1. The matrix (8) is continuous and the pressure equation has continuous right-hand side. Since w>0 and u in C1, the distributional ODE makes u in C2 locally. Divergence gives H'=(2-p)R, so H in C2.

Direct differentiation of k=c r^(1-p)R and S=r^-2p h shows that (2) is equivalent to

    (p-1)R h'-2p R'h=0                              (18)

wherever W!=0. At an endpoint b of a constant plateau H=H0!=0, continuity gives R(b)=R'(b)=0. Formula(4) makes W(b) nonzero, so W remains nonzero on a neighborhood. In this neighborhood (18) holds.

Suppose the plateau ends at b, so every interval immediately to that side contains points with R!=0. We show h(b)=h'(b)=h''(b)=0. The last derivative exists at b even though it need not exist everywhere. Put e=(R^2+H^2/w)/2. Its first derivative is

    e'=R R'+HH'/w+zH^2/w^2.

As z approaches b, R=o(|z-b|), R'->0 and H'=(2-p)R=o(|z-b|). The first two terms therefore have derivative0 at b, while the final term is differentiable. Thus

    e(b)=H0^2/(2w_b), e'(b)=bH0^2/w_b^2,
    e''(b)=H0^2[1/w_b^2+4b^2/w_b^3].               (19)

Since u in C2, h in C1 has a second derivative at b and its second-order Peano expansion there.

If h(b)!=0, (18) is a regular first-order linear equation R'=beta(h'/h)R near b. Uniqueness and R(b)=0 extend the plateau, a contradiction. If the first nonzero h-jet has order j=1 or2, the Peano expansion gives h(z)=C(z-b)^j+o(|z-b|^j), C!=0, on the one-sided interval. It has no zero there after shrinking. Integration of the same linear equation gives either R identically0 or

    R=C1 |h|^beta, beta=(p-1)/(2p), C1!=0.

The latter has magnitude comparable to |z-b|^(j beta). But j beta<1, whereas R=o(|z-b|). It is impossible. The identically zero case again extends the plateau. Hence all three h-jets vanish.

At b, the actual pressure equation evaluated with R=R'=0 is

    (w u')'+kappa u=-H0^2[2p/w_b+2b^2/w_b^2].

Substitute u=e, u'=e', u''=e'' at b from the vanishing h-jets and (19). Rearrangement gives

    H0^2[(2p^2+p+1)/w_b+4b^2/w_b^2]=0.              (20)

Every coefficient is positive and H0!=0. This contradiction rules out the proposed departure. The proof takes the edge of a constant plateau directly; it does not assume a bounded integration constant across infinitely many components of {R!=0}.

For a global C1 axisymmetric poloidal V, an open E=0 cone with V nonzero contains a latitude interval where R=0 and H=H0!=0. Extend it to the maximal constant-H interval in(-1,1). Neither endpoint can be interior by (20), so H is constant throughout(-1,1). Continuity of V at each pole gives H=s V_theta->0 there, forcing H0=0. This is impossible. Actual natural tails have the required C1 velocity, pressure regularity and rank identity by A530,A531,A533,A534,A539. Their axisymmetric poloidal hypothesis is an extra assumption. No symmetry of the original full profile is inferred.

## 8. Comparison with CO28 and limitations

The complete CO28 source and LIT144-LIT145 were read. The source rank-scope note was also read. The exact Stokes-stream-function family in CO28 corresponds to H=-(2-p)G, R=beta_source. Its smoothness follows from G(1)=G(-1)=0 and smooth divisibility by1-z^2. The broad beta_source assumptions guarantee k=0 on the stated cone and nonzero wherever beta_source!=0; they do not guarantee that no other zero cone occurs. The word exactly requires an additional condition on beta_source.

CO28's Legendre truncations and finite differences are explicitly numerical observations; they were not rerun or promoted to a proof here. Sections5-6 independently establish the relevant existence claim with the actual canonical pressure for every target c and every omega. The list of tested leading conditions is incomplete for an actual globally helicity-free profile: (2) is confirmed, and Section7 proves that every nonzero poloidal plateau example here violates it somewhere. Thus the source phrase all known second-order tail conditions is not justified.

The construction still rigorously separates the canonical Poisson, scalar first-integral and mixed-helicity conditions from the rank condition. It is neither an Euler profile nor a formal completion, and it supplies no counterexample to the campaign conjecture. The new local rank obstruction is limited to poloidal axisymmetric tails; no nonaxisymmetric or azimuthally swirling propagation theorem is claimed. Existing configured-model source comparison and continued team-file exchange are used; no new client, computation or formal build was used.
