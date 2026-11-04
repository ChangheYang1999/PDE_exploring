# Analytic central vorticity traces and the missing Euler equation

Status: CONFIRMED as local analytic reconstructions and explicit Euler-failure tests, A746-A748. No global Euler profile or general smooth elliptic Cauchy solution is constructed.

## 1. Statement and coordinate conventions

Fix R>0 and an open h interval I with r=R+h>0. Use the Euclidean coordinates

    x=(r cos theta,-r sin theta,z),
    metric=r^2 dtheta^2+dh^2+dz^2,
    positive volume=r dtheta dh dz.

Let u(h) be real analytic and nowhere zero on I, and let w(theta,h) be any real analytic2pi-periodic function. Then an open neighborhood of S1 times I times{0} admits a real analytic V such that

    div V=0, V.curl V=0,
    V(theta,h,0)=u(h) partial_h,
    curl V(theta,h,0)=w(theta,h) partial_theta.

There is a real analytic first integral q of curl V with q_h=u on the central cylinder. On every compact smaller h interval the neighborhood has a positive uniform transverse width. The constructed vorticity also satisfies

    W^theta=w+O(z^2), W^h=O(z^2), W^z=-z w_theta+O(z^2),

with locally uniform analytic remainders. Thus actual curl, incompressibility and zero helicity do not determine higher transverse terms from this central first jet.

For0<c<1/2, omega!=0, rho<0, integer m>=3 and beta!=0, the choice

    u=-cR+(rho-c)h, w=h^m sin^2(theta+beta h)

on a small interval about0 gives an actual periodic orbit Gamma={h=z=0} of B=(cI-omega J)x+V, where J(x,y,z)=(-y,x,0). Its Floquet exponents are0,rho,3c-rho. On Gamma V!=0 and W=DW=0, while every point of Gamma lies in the closure of{W!=0}. Nevertheless [B,W]+(1+c)W is nonzero somewhere in every sufficiently small tube, so no pressure makes this V an Euler profile.

## 2. Analytic existence with an explicit first-order reduction

Choose an analytic primitive Q0 of u and set

    L=1-r z w/u.

It is positive on a sufficiently small variable-width neighborhood of the central cylinder. Consider

    div(L grad q)=0,
    q(theta,h,0)=Q0(h), q_z(theta,h,0)=0.              (1)

Since L and r are nonzero there, the equation is equivalent to

    q_zz=-q_hh-r^-1 q_h-r^-2 q_thetatheta
           -(L_z/L)q_z-(L_h/L)q_h
           -L_theta/(r^2 L)q_theta.                  (2)

Every coefficient is analytic. To check the exact Cauchy-theorem hypothesis without an implicit mixed-order system, introduce the four unknowns(q,a,b,v) with initial values(Q0,0,u,0) and solve

    partial_z q=v,
    partial_z a=partial_theta v,
    partial_z b=partial_h v,
    partial_z v=-partial_h b-r^-1 b-r^-2 partial_theta a
                  -(L_z/L)v-(L_h/L)b-L_theta/(r^2 L)a.   (3)

This is a first-order system solved for every z derivative, with analytic dependence on the unknowns and their first tangential derivatives only. Subtract the analytic initial data, extended independently of z, to reduce to zero initial data. The analytic Cauchy theorem gives a unique analytic local solution. The differences a-partial_theta q and b-partial_h q have zero z derivative and zero initial value, so they vanish. Consequently q solves(2) and(1).

This uses precisely the first-order normal-form theorem, not any smooth elliptic Cauchy existence statement. The actual manuscript Gantumur, Math580 Lecture Notes2, Theorem18 on printed pages9-10, its higher-order discussion on page11 and real-analytic specialization on page14 were read. The manuscript and extracted passages are retained in verification. The theorem supplies convergence of the analytic solution, not merely a formal Taylor series. No broad claim about other mixed-order systems is needed.

On overlapping sufficiently small central charts, uniqueness with the same Cauchy data makes the analytic germs agree. Periodic translates in theta have the same data and coefficients and therefore agree. The germs patch around S1 times I times{0}; compactness gives a uniform positive width on each smaller compact cylinder. Real coefficients and data make the solution real by complex conjugation and uniqueness. Shrinking once more keeps q_h nonzero locally along the central cylinder.

## 3. Exact curl and the first transverse jet

Set V=L grad q. Equation(1) gives div V=0. Since curl grad q=0,

    W=curl V=grad L cross grad q,
    V.W=0, W.grad q=0.                               (4)

At z=0, grad q=u partial_h and L=1,L_h=L_theta=0,L_z=-r w/u. In the positive orthonormal frame(e_theta,e_h,e_z), one has e_z cross e_h=-e_theta. Thus grad L cross grad q=r w e_theta=w partial_theta. This verifies the trace and its sign in the stated negative-angle coordinates.

More explicitly, the contravariant components are

    W^theta=(L_h q_z-L_z q_h)/r,
    W^h=(L_z q_theta-L_theta q_z)/r,
    W^z=(L_theta q_h-L_h q_theta)/r.                  (5)

The initial data imply q_theta=q_z=q_thetaz=q_hz=0 on z=0. Also L_zz=0 and L_h=L_theta=0 there. Differentiating(5) once in z gives

    partial_z W^theta=0,
    partial_z W^h=0,
    partial_z W^z=-w_theta.

Together with the trace these give the claimed first jet. Analyticity gives the locally uniform O(z^2) remainders. These terms are exact derivatives of the actual analytic solution; no truncated series is substituted into the equations.

## 4. A flat periodic carrier circle that fails Euler

Take the u,w in Section1. On z=0 the affine part of B is omega partial_theta+cr partial_h+cz partial_z, because physical rotation J equals minus partial_theta. Hence

    B|_(z=0)=omega partial_theta+rho h partial_h.     (6)

The central cylinder is invariant. Gamma is a periodic B orbit of period2pi/|omega|. The velocity has value-cR partial_h on Gamma and is nonzero. Since L-1=O(z h^m), its spatial gradient is O((|h|+|z|)^m); grad q is bounded on a small compact cylinder. Thus W=O((|h|+|z|)^m), and analyticity implies W=DW=0 on Gamma for m>=3. Points with small nonzero h and nonzero sin(theta+beta h) approach every point of Gamma, and their central W is nonzero.

The coordinate derivative matrix of B along Gamma is diagonal. Indeed B^theta=omega+Lq_theta/r^2 has zero first derivatives there. The central trace gives B^h_h=rho; B^h_z=L_z u+q_hz=-r w, which is0 on Gamma. All central derivatives of B^z in theta,h vanish. Equation(2) on z=0 gives q_zz=-u'-u/r, so

    B^z_z=c+q_zz=c-u'(0)-u(0)/R=3c-rho.

The remaining diagonal entry in the angular direction is0. The coordinate basis returns after one period, so the Floquet exponents are exactly0,rho,3c-rho. This calculation is for the actual derivative cocycle along Gamma, not only a formal matrix model.

Put kappa=1+c. Any Euler profile with this carrier must satisfy [B,W]=-kappa W. On z=0 both B and W are tangent to the cylinder, W=w partial_theta and B^theta=omega is constant. Therefore

    ([B,W]+kappa W)^theta
      =omega w_theta+rho h w_h+kappa w
      =h^m[(m rho+kappa)f+(omega+rho beta h)f'],       (7)

where f=sin^2(theta+beta h). If m rho+kappa!=0, evaluate at a phase with f=1,f'=0. Otherwise use a phase with f'!=0; omega+rho beta h is not identically0 on any h interval. Thus(7) is not identically0 near Gamma, proving the stated pressure-independent Euler failure. No pressure normalization or boundary behavior is involved in this local counterexample.

## 5. Further checked restriction: central Euler transport can be matched

There is a useful strengthening of the scope test away from h=0. Fix rho<0 and omega!=0, take

    p=-kappa/rho>0, beta=-omega/rho,
    u=-cR+(rho-c)h,
    w=h^p f(theta+beta log h),

on any small positive h interval where u!=0, with a nonzero real analytic periodic f. This w is analytic on that interval. The construction gives an actual analytic incompressible helicity-free V with the same first transverse vorticity jet as in Section3. Now(6) and

    omega w_theta+rho h w_h+kappa w=0

make the full central vorticity-transport residual vanish on z=0. Its h and z components also vanish there because W^h=W^z=B^z=0 identically on the central cylinder and B^theta is constant.

This still does not produce Euler off the cylinder. From the exact central derivatives,

    partial_z B^h=-r w,
    partial_z B^theta=0,
    partial_z W^theta=partial_z W^h=0,
    partial_z W^z=-w_theta,

differentiate the theta component of R=[B,W]+kappa W at z=0. All tangential derivatives of the last three identities are0 in the appropriate component. The only surviving term is

    partial_z R^theta=-r w w_h.                      (8)

For the chosen p>0 and a nonzero periodic f, w w_h is not identically0. Otherwise, at each positive h the periodic function f would satisfy f(pf+beta f')=0. Integration over one period gives p integral f^2=0, a contradiction. Hence the necessary Euler equation fails at first transverse order somewhere, although it holds exactly on the central cylinder. This refinement illustrates why checking only central transport and the curl first jet is insufficient. It gives no extension through h=0 and no global profile.

## 6. Dependencies and limits

The existence step uses the analytic first-order noncharacteristic Cauchy theorem at the explicit scope(3). Everything else follows from coordinate divergence, curl, exact analytic differentiation and the Euler bracket identity. The source proof, original theorem manuscript and hashes are retained in the team records. The theorem permits varying neighborhood widths; no control as h tends to0 is inferred for a logarithmic phase.

LIT111-LIT115 rule out an exact prescribed three-dimensional vorticity. The present construction rules out extending that obstruction to its central trace or first transverse jet without using further equations. It does not refute any of those exact-ansatz results. It imposes neither the full Euler equation nor the global Euler rank identity, and it is not an entire decaying field. The W2 obstruction and the main conjecture remain OPEN. The complete current source, independent proof and retained primary Cauchy theorem passages were reread at final audit. Continuing configured-model comparison uses existing working files; the direct audit verdict is A746-A748.
