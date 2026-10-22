# The impulse of a compact residual and its large-radius leading term

Written 2026-10-21T08:24Z, before computation. This packet verifies the lead's proposed boundary formula and a conditional asymptotic for the already constructed configurations of packet135. It does not compute a nonzero coefficient for an actual reference, exclude changes of the exterior, or decide the B2 problem.

## 1. Notation and boundary identity

Let beta be real with 3beta != 2. Let Psi and Theta be smooth on a neighborhood of a closed disk D_r, in Cartesian coordinates X=(x,y). Use the relative stream convention

    V=(-Psi_y,Psi_x), W=beta X+V, Omega=-Delta Psi,
    f=(W.grad+1)Omega-Theta_x,
    t=W.gradTheta-(beta-2)Theta.

The stream can be shifted by a constant without changing these fields. In a B2 application its velocity is the relative velocity, so its gradient vanishes at the moving center. Write p=Psi_x, q=Psi_y and n for the outward unit normal.

**Proposition A.** For these arbitrary smooth fields, without assuming either transport equation,

    integral_Dr [x f+t/(3beta-2)]
      = integral_boundaryDr [ (x Omega+Theta/(3beta-2)) W.n
           -x Theta n_x-pq n_x-(q^2-p^2)n_y/2
           +(1-3beta)(Psi n_x-x partial_n Psi) ] ds.       (1)

If t=0, this is the asserted boundary formula for the residual impulse integral x f. If f is compactly supported, its value is independent of r once the disk contains the support. An added constant in Psi changes the displayed flux integral by a constant times integral n_x=0, so the identity is independent of that remaining stream constant.

**Proof.** The constant divergence div W=2beta gives

    x f=div(x W Omega-x Theta e_x)
          +(1-3beta)x Omega-V_1 Omega+Theta.             (2)

There are two elementary divergence identities:

    x Omega=div(Psi e_x-x grad Psi),
    V_1 Omega=div(pq,(q^2-p^2)/2).                       (3)

For the second, differentiate the right side and use p_y=q_x: the result is q Delta Psi, which equals (-q)(-Delta Psi). Finally

    t=div(W Theta)-(3beta-2)Theta.                       (4)

Substitution of (3) and (4) in (2), followed by the divergence theorem, gives (1). All fields are smooth on a bounded disk, so no decay or boundary-limit hypothesis is used. This proves Proposition A.

## 2. Hypotheses for the exterior construction

Fix beta>2, s=1/beta and m=1-2s. Fix one reference from packet126, including its finite length, shift, anisotropy, disk and cutoff choices. Let its relative fields be Psi_*,V_*,Omega_*,Theta_*, with exact t_*=0. Fix the radial cutoffs of135:

    0<=chi,rho<=1,
    chi=0 on r<=1, chi=1 on r>=2,
    rho=0 on r<=5, rho=1 on r>=8.

For each sufficiently large gluing radius R, packet135 gives a fixed-point e=e_R, odd in z_1 and zero on |z|<5, with a norm bound uniform in R. Its canonical subtracted potential Qe satisfies -Delta Qe=e and vanishes to first order at0. Set

    v[e]=grad^perp(chi Qe), b[e]=-Delta(chi Qe)-e,
    delta=R^(-s), omega_R(z)=R^s Omega_*(Rz),
    v_R(z)=R^(s-1)V_*(Rz), theta_R(z)=R^(-m)Theta_*(Rz),
    g_R(z)=R^(2s) f_*(Rz),
    w_e=beta z+delta v_R+delta^2 v[e].

Extend theta_e by theta_R on |z|<=1; outside it solves the exact thermal equation for w_e with the reference trace. The fixed point satisfies

    (w_e.grad+1)e=rho[-g_R+partial_1(theta_e-theta_R)
                              -delta v[e].grad omega_R].       (5)

The actual new vorticity and temperature are

    Omega_Rnew(Rz)=R^(-s)omega_R(z)+R^(-2s)(e+b[e])(z),
    Theta_Rnew(Rz)=R^m theta_e(z).

These equations include the compact compensator b[e]; omitting it would give the wrong residual near the cutoff. Packet135 supplies the uniform estimates on each fixed scaled annulus 1<=|z|<=8:

    |v_R|+|grad omega_R|+|v[e]|+|b[e]|<=C,
    |grad(theta_e-theta_R)|<=C delta^2,                (6)

where C depends on the fixed reference but not R. The function b[e] is supported in 1<=|z|<=2. Both corrections vanish on |z|<1. In detail,135 equation(V) gives ||theta_e-theta_R||_(-m;2,alpha)<=C delta^2||e||_(s;1,alpha), and e belongs to one fixed bounded strong ball. On the compact annulus1<=|z|<=8 this weighted norm controls the ordinary C1 norm. The difference is zero on B1, so its L1(B8) norm is also O(delta^2). The potential estimates(I) give the uniform bounds for v[e] and b[e], and the fixed-reference symbols give that for grad omega_R. No extra assumption on the temperature difference is required here.

The fixed reference has homogeneous leading fields

    Psi_hom=-B r^(2-s)cos(theta)H(theta)^p,
    H=cos^2(theta)+eta sin^2(theta), p=(1-s)/2,
    V_hom=grad^perp Psi_hom, Omega_hom=-Delta Psi_hom,
    Theta_hom=r^m A(theta).                           (7)

Here B>0 and eta>0 are fixed. Its finite vertical shift affects the lower terms but not (7). The required asymptotics, with derivatives on every compact annulus away from0, are

    R^(s-1)V_*(Rz)->V_hom(z),
    R^s Omega_*(Rz)->Omega_hom(z),
    R^(-m)Theta_*(Rz)->Theta_hom(z).                  (8)

The temperature limit is in C1. It follows from the exact thermal equation and the all-order velocity symbols, as explained below. The reference vorticity has the stronger expansion

    Omega_*=Omega_hom+O_sym(r^(-s-1)),                (9)

and f_* has the global bound |f_*(X)|<=C(1+|X|)^(-2s). These are consequences of the shifted anisotropic reference and its exact transported temperature, rather than extra hypotheses on a general unknown B2 profile.

## 3. The asymptotic statement and proof

Let f_R be the full residual of the135 configuration with gluing radius R. It is smooth and supported in |X|<=8R. Define

    I(R)=integral_R2 x f_R(X)dX,
    g_hom=V_hom.grad Omega_hom-partial_x Theta_hom
          =r^(-2s) g_ang(theta),
    m1=integral_0^(2pi) cos(theta) g_ang(theta)dtheta,
    C_rho=integral_0^8 (1-rho(r)) r^(2-2s)dr.

**Theorem B.** Under the fixed-reference construction above,

    I(R)=R^(3-2s)[C_rho m1+O(R^(-s))] as R->infinity.       (10)

The positive finite constant C_rho depends only on the fixed cutoff. If m1!=0 for this actual reference, then every sufficiently large R has I(R)!=0. Such a configuration cannot be repaired into a B2 profile by a compact modification that preserves the exact thermal equation and the exterior relative drift and temperature. This last assertion follows from142; it is a fixed-exterior obstruction only.

**Proof of the scaled residual identity.** The scaling exponents m-1=-2s and W(Rz)=R w_e(z) give

    R^(2s)f_R(Rz)
       =(1-rho)[g_R+delta v[e].grad omega_R
                       -partial_1(theta_e-theta_R)]
         +(w_e.grad+1)b[e].                          (11)

Indeed, before substituting (5), the reference contributes g_R, the changed velocity contributes delta v[e].grad omega_R, the changed temperature contributes -partial_1(theta_e-theta_R), and the source plus compensator contributes (w_e.grad+1)(e+b[e]). Equation (5) cancels the rho multiple. Formula (11) also holds for |z|<1, where e,b[e],v[e] and theta_e-theta_R are zero. For |z|>8 every term on the right vanishes.

The compensator has zero affine moments for a direct reason. Since -Delta Qe=e,

    b[e]=-Delta[(chi-1)Qe].                          (12)

The bracket is smooth and compactly supported in |z|<=2. Two integrations by parts give integral z_1 b[e]=0. The vanishing first jet of Qe is needed elsewhere in the relative-gauge construction, but is not required for this particular moment identity. Since div w_e=2beta,

    integral z_1(w_e.grad+1)b[e]
        =(1-3beta)integral z_1 b[e]
                    -integral(delta v_R,1+delta^2 v[e]_1)b[e]
        =O(delta).                                  (13)

All integrals in (13) are over the fixed compact annulus1<=|z|<=2, and (6) makes the bound uniform. Likewise the other two correction terms in (11), multiplied by z_1 and integrated, are O(delta) and O(delta^2). Their supports inside |z|<=8 stay away from0. Therefore the change of variables X=Rz gives

    I(R)/R^(3-2s)=integral z_1(1-rho)g_R(z)dz+O(delta). (14)

To identify the limit, split the reference residual into

    f_*=(beta X.grad+1)Omega_*+V_*.gradOmega_*-Theta_*,x.

The dilation operator annihilates Omega_hom. Its action on the remainder in (9) is O(r^(-s-1)); after scaling by R^(2s) this tends to0 on each fixed punctured annulus, since s<1. Formula (8) then gives g_R->g_hom locally there. The global residual estimate also gives |g_R(z)|<=C|z|^(-2s), uniformly for all large R and all z!=0. For example, R^(2s)(1+R|z|)^(-2s)<=|z|^(-2s). The resulting majorant |z_1||z|^(-2s) is integrable on |z|<=8: its radial integral is bounded by a constant times integral_0^8 r^(2-2s)dr, finite since s<1/2. Dominated convergence applies in (14). Polar coordinates separate the limit into C_rho m1, proving (10). Since rho=0 on[0,5], C_rho>0. If m1!=0, the nonzero limit gives a fixed sign for I(R) for large R. The exact impulse invariance of142 proves the final conditional obstruction.

For clarity, the reference temperature assertions used above do not follow merely from its loose polynomial bound in126. Write tau=log r and A_r(theta)=r^(-m)Theta_*(r,theta). Its exact equation is

    partial_tau A_r+b partial_theta A_r
       =-m (V_*.e_r/r) A_r/(beta+V_*.e_r/r),
    b=(V_*.e_theta/r)/(beta+V_*.e_r/r).

For large r the denominator is bounded below by beta/2. The coefficients and every cylindrical derivative are O(r^(-s)), integrable in tau. The angular characteristic flow and its inverse have uniformly bounded derivatives of every fixed order, by differentiating their ODEs and using the integrable coefficients. The scalar integrating factor has the same property. Thus A_r has uniform angular derivatives and converges to a smooth A; the equation also bounds its radial logarithmic derivatives. In particular the reference has the required C1 homogeneous temperature limit and grad Theta_*=O(r^(-2s)). Combining this with the velocity and vorticity symbols yields the global residual bound after enlarging C on a fixed disk. This verifies rather than assumes the extra reference properties used in the proof. This also gives the rate in(10), as follows. The integral of an O(exp(-s tau)) coefficient from tau to infinity is O(exp(-s tau)). Applied to the angular characteristic and amplitude equations, including each fixed number of differentiated equations, this gives

    r^(-m)Theta_*(r,theta)=A(theta)+O_Cj(r^(-s))

for every fixed j. Radial logarithmic derivatives follow from the same PDE. Consequently

    Theta_*=Theta_hom+O_symbol(r^(m-s)),
    V_*=V_hom+constant+O_symbol(r^(-s)),
    f_*=g_hom+O_symbol(r^(-3s)).                     (15)

For the last line, the shifted vorticity dilation remainder is O(r^(-1-s)); the constant-velocity term acting on the leading vorticity has that same order. The cross terms V_hom.grad(O_symbol(r^(-1-s))) and O_symbol(r^(-s)).grad Omega_hom are O(r^(-1-2s)); the remaining product terms decay faster. The temperature-gradient remainder is O(r^(m-s-1))=O(r^(-3s)). Since1+s>3s for s<1/2, every displayed remainder is O(r^(-3s)). Fix a radius M beyond which(15) holds. On M/R<=|z|<=8,

    |g_R(z)-g_hom(z)|<=C R^(-s)|z|^(-3s).

Its weighted integral against z_1(1-rho) is bounded by C R^(-s) integral_0^8 r^(2-3s)dr, finite because3s<3. On |z|<M/R, boundedness of f_* on B_M gives integral |z_1 g_R|=O(R^(2s-3)); homogeneity gives the same estimate for integral |z_1 g_hom|. Since3-2s>s, these inner contributions are O(R^(-s)). Combining with(14) proves the claimed O(R^(-s)) rate. Constants may depend on the single fixed reference and cutoffs; no uniformity as its parameters change is claimed.

## 4. Angular reduction for the anisotropic reference

**Proposition C.** For (7),

    m1=-integral_0^(2pi) A(theta)[(3-2s)cos^2(theta)-1]dtheta.  (15)

**Proof.** Psi_hom is even in y. Its vorticity is also even in y; V_hom,1 is odd and V_hom,2 even in y. Hence V_hom.grad Omega_hom is odd in y. Its cosine angular moment vanishes by reflection theta->-theta. No y symmetry of the actual shifted reference temperature is assumed.

In polar coordinates partial_x(r^m A)=r^(m-1)[m cos(theta) A-sin(theta) A']. Multiply by cos(theta) and integrate on a complete circle. Integration by parts of the A' term gives the weight m cos²+(cos theta sin theta)'=(m+2)cos²-1. Since m+2=3-2s, the negative derivative contribution is exactly (15).

Positivity of A alone does not determine this integral: its weight takes both signs. Nor does a calculation on an arbitrary angular function establish a value for the transported A of an actual fixed reference. A numerical nonzero value for one reference would be evidence for that reference. A genericity statement would require an additional parameter-dependence argument.

## 5. Scope and dependencies

Proposition A is a bounded-domain divergence identity and is valid even when the thermal residual is nonzero, with its explicit correction term. Theorem B depends on the complete fixed-reference exterior construction of135 and on the shifted anisotropic reference of126, including the all-order estimates. Compact stream changes preserve the canonical relative gauge only under the stated hypotheses. The theorem does not apply to R-dependent reference choices without new uniform bounds. Its coefficient m1 has not been evaluated for an actual reference here.

Packet142 supplies the exact compact impulse invariance. Every formula specific to the asymptotic, the compensator moment, the scaling and the angular reduction is derived above. Planned controls: independent symbolic divergence and scaling checks, exact or refined numerical angular controls, bounded-domain manufactured flux tests, and a complete actual Claude Opus5.5 audit. No formal Lean build is authorized.

Rate refinement written 2026-10-21T08:30:15.396641+00:00, after checking135 equation(V); the original proof sent for208 review is preserved in verification/exterior_impulse_controls_20261021T0827Z/PROOF_before_rate_refinement.md. Follow-up209 explicitly audits the new rate and support estimates.

Verification update 2026-10-21T08:36:25.022169+00:00: own exact and manufactured checks passed. Actual Claude Opus5.5 review210 returned a complete written confirmation of the rate and compact-stream sign lemma; its qualifications were independently checked.208 timed out without a returned model or audit;209 returned actual claude-opus-5-5 but no written audit. Neither is counted as confirmation.
