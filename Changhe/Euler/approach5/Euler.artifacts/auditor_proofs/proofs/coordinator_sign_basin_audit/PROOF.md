# Coordinator sign-changing basin package: exact scope audit

Status: independently checked, A367-A371. None of these results proves nonexistence in the target interval. Read Sections1-3 for exact identities and reduced countertests, then Sections4-8 for the measure and decay conclusions.

## 1. Exact profile and measure hypotheses

Let 2/5<c<1/2 and omega be any finite real number. Let U in C2(R3;R3), P in C1(R3) satisfy

    div U=0,
    (1-c)U+(Ay+U).grad U+omega JU+grad P=0,
    U(y)->0 uniformly as |y|->infinity,
    J(y1,y2,y3)=(-y2,y1,0), A=cI-omega J.

Set B=Ay+U, Omega=curl U, a=1-2c, kappa=1+c, d=3c, k=(1-c)/c. Let Phi be the complete B flow, Psi_t=Phi_-t and Gamma the complete volume-preserving Omega flow. A048-A049 prove the last completeness and recurrence assertions for this class. Put

    H0=P-p_infinity+|U|2/2+Ay.U,
    q=U.B, h=U.Omega,

with the unique pressure constant p_infinity in A031 and A277. The verified inputs are

    a U+grad H0=B cross Omega,
    BH0=-a q, Omega H0=-a h,
    [B,Omega]=-kappa Omega,
    Phi_t Gamma_s=Gamma_(s exp(kappa t)) Phi_t,
    det D Phi_t=exp(dt),
    E(R)=integral_B_R |U|2 <= C R^(5-2/c), R>=1,
    integral_Q |H0(Phi_t y)|2 dy <= C_Q exp(-2at)         (1)

for every bounded measurable Q. The last two statements use the actual Euler pressure and decay. Adding a nonzero constant to H0 destroys the last estimate.

When an invariant probability nu is used, it is a GIVEN compactly supported full-Phi-flow-invariant probability with nu(B!=0,Omega!=0)=1, a backward Oseledets splitting with exponents (a,0,-kappa), directions Eu,span(B),span(Omega), and unstable conditional measures absolutely continuous with respect to length on C1 unstable plaques. These hypotheses make the three directions independent nu-almost everywhere. At C2 they are extra measure hypotheses. A308 supplies the measures and almost-everywhere coverage in the C-infinity class, not at the bare C2 baseline. Ergodicity is unnecessary for the averaging arguments.

## 2. Euler identities and nonrotating consequence, A367

Applying the bracket to H0 gives

    -a Bh+a Omega q=a kappa h,
    Bh+kappa h=Omega q,
    div(hB-qOmega)=(d-kappa)h=-a h.                    (2)

These identities require no sign or integrability of h. They are not a homogeneous scalar equation for h. With G=H0-ac|y|2/2,

    BG=-a(U+cy).B=-a(|B|2+omega Jy.B).

For every compactly supported B-invariant probability mu, integrate BG=0. A smooth cutoff equal to1 near the invariant compact support justifies differentiating this otherwise noncompact observable. Therefore

    integral (|B|2+omega Jy.B) dmu=0.                  (3)

If omega=0, such a probability is carried by {B=0}. If the stated vortical probabilities cover almost every point of {Omega!=0}, no nonempty vortical set can exist, because each of those probabilities gives full mass to B!=0. Openness then gives Omega=0 everywhere. Div U=0 makes the components harmonic, and boundedness with decay gives U=0. This deduction uses coverage, so the package does not give a new C2 coverage theorem. The earlier nonrotating A037 theorem has a different, stronger proof.

For a periodic carrier orbit gamma of period T, the same derivative identity yields

    integral_0^T |B(gamma(t))|2 dt
       =-omega integral_gamma Jy.dy.                 (4)

Finally, in the product coordinates y=Gamma_tau Psi_r gamma(s), commutation and Omega H0=-a h imply the exact oriented integral

    H0(Phi_t y)-H0(Phi_(t-r) gamma(s))
       =-a integral_0^(tau exp(kappa t))
          h(Gamma_sigma Phi_(t-r) gamma(s)) d sigma.  (5)

A signed volume cancellation of h does not cancel (5). Neither Gamma-invariance of nu nor vanishing of integrated Omega derivatives against nu has been proved or used.

## 3. Exact local and tail countertests, A368-A369

### 3.1 Local cylindrical saddle

Fix additionally omega!=0, R>0, b!=0 and w real. On the open cylindrical domain r>0 set

    U_r=-r/2+aR2/(2r),
    U_theta=b(r-R2/r),
    U_z=z+w,
    H=[b(b-omega)+a/4]r2-[2b2+a2/2]R2 log r
        -a(z+w)2/2,
    P=H-|U|2/2-Ay.U.                                  (6)

Here the subscript denotes orthonormal cylindrical components. Direct differentiation gives div U=-1+1=0 and Omega=2b e_z. Thus

    B_r=a(R2/r-r)/2,
    B_theta=(b-omega)r-bR2/r,
    B_z=kappa z+w.

The radial derivative in (6) gives

    aU_r+H_r=2b(b-omega)r-2b2R2/r=2bB_theta.

Also aU_theta=-2bB_r and aU_z+H_z=0. These are precisely aU+grad H=B cross Omega. To recover the original PDE use

    grad(Ay.U)=A^T U+(Ay.grad)U+(Ay) cross curl U,
    (U.grad)U=grad(|U|2/2)-U cross curl U,
    aI+A^T=(1-c)I+omega J.

This verifies the full local equation with the pressure in (6), without relying on the source's symbolic script.

The circle r=R,z=-w/kappa has angular carrier speed -omega. Its backward-flow normal exponents are a and -kappa. The exact backward equations, as long as the trajectory stays in the domain r>0, are

    r(t)2-R2=exp(at)(r(0)2-R2),
    z(t)+w/kappa=exp(-kappa t)(z(0)+w/kappa).

The full stable set of the circle within that domain is r=R. Its invariant probability has zero entropy, and this stable cylinder has zero three-dimensional volume. Helicity is h=2b(z+w), takes both signs on the cylinder, and equals 2bcw/kappa on the periodic circle. For w!=0 it is therefore nonzero on that circle. The model is singular on the excluded axis, grows at infinity and has nonrecurrent vertical vortex lines. It is not a complete global profile or an attracting positive-volume basin example. In particular some trajectories with r(0)<R reach the excluded axis in finite backward time; no completeness was claimed for them.

### 3.2 Sign-changing formal tail for every omega

For lambda and mu nonzero define on R3 minus {0}

    V=r^-k [2lambda cos(theta)/(2-k) e_r
             -lambda sin(theta) e_theta
             +mu sin(theta)cos(theta) e_phi].          (7)

The poloidal part is r^-k[lambda e_z+k lambda cos(theta)e_r/(2-k)]. The toroidal part is also a smooth Cartesian vector field off0, since sin(theta)e_phi=(-y2,y1,0)/r. Thus both pole singularities are removable.

The spherical divergence is zero because

    (2-k)[2lambda cos(theta)/(2-k)]
      +(sin(theta))^-1 d_theta[-lambda sin(theta)2]=0.

The curl is

    curl V=r^(-k-1)[mu(3cos(theta)2-1)e_r
       +(k-1)mu sin(theta)cos(theta)e_theta
       +lambda k(3-k)sin(theta)/(2-k)e_phi].            (8)

Taking its dot product with (7) yields exactly

    V.curl V=4lambda mu r^(-2k-1)cos(theta)3/(2-k),      (9)

which changes sign. Homogeneity and rotational equivariance imply

    (Ay.grad)V=-ckV-omega JV.

As ck=1-c, the linear tail equation holds. With tau=Az.V and the preceding gradient identity, it is equivalent to

    aV+(curl V) cross Az+grad tau=0,
    tau=r^(1-k)cos(theta)
         [2c lambda/(2-k)-omega mu sin(theta)2].       (10)

This proves the stated differential tail countertest for every omega, including0. It gives no nonlinear profile or globally smooth extension. It is consistent with the separate positive-helicity tail in A362: tail equations alone impose neither a universal positive sign nor a universal sign change.

Under the Dini scattering theorem, every compact invariant support lies in the compact core K. Indeed boundedness of Phi_t y for all t on that support gives exp(-tA)Phi_t y->0. Thus the off-core terminal scalar tau composed with S cannot simply be evaluated as a prescribed finite scalar on supp nu.

## 4. Short vortex averages and null-set transfer, A370

For ell>0 define the compactly supported probability

    m_ell=(1/(2ell)) integral_(-ell)^ell (Gamma_s)_*nu ds.

It is absolutely continuous with an L1 density rho_ell. Here is the full change-of-variables justification. Insert a short Psi-time average using invariance of nu. Disintegrate nu along unstable plaques gamma with conditional density f_gamma(s)ds. On each plaque consider

    F_gamma(s,r,tau)=Gamma_tau Psi_r gamma(s).

Its three derivative columns are independent for almost every s of positive conditional weight, for every finite r,tau. Pull them back by the invertible derivatives D Gamma_tau and D Psi_r; they become nonzero multiples of gamma',B,Omega. Equivalently their absolute determinant is exp(ar)|alpha(gamma')|, where alpha=(B cross Omega).dy. A countable inverse-function cover of the set with nonzero determinant and Tonelli show that each plaque-time-vortex pushforward is absolutely continuous. The remaining parameters have zero weighted measure. Integrating the plaque disintegration proves the assertion. Compact support follows from continuity of Gamma on the compact time interval and compact supp nu. No uniform density estimate follows from this argument.

For a Gamma-invariant volume-null Borel set N,

    nu(N)=m_ell(N)=0.                                  (11)

This transfers the exceptional set of an invariant almost-everywhere statement, including two-sided vortex recurrence, to nu. It does not transfer an arbitrary volume-null set, nor assert that nu is Gamma-invariant.

For every nonnegative Borel observable F and S=ell exp(kappa t),

    M_S(F):=integral F dm_S
      =integral F(Phi_t y)rho_ell(y)dy
      =exp(-dt) integral F(x)rho_ell(Psi_t x)dx.        (12)

This follows directly from commutation, invariance of nu, and the volume Jacobian. It is valid with infinite nonnegative integrals; bounded signed functions follow by splitting signs.

The density hypothesis rho_ell in L-infinity is an EXTRA hypothesis for the quantitative claims of this section. Under it, (1) gives

    M_S(H0^2)<=C S^(-2a/kappa).                         (13)

The bounded profile gives |Phi_t y|<=C_Q exp(ct) for y in a bounded Q. Changing variables and using E(R) yields

    integral_Q |U(Phi_t y)|2 dy
      <=exp(-dt) E(C_Q exp(ct))
      <=C_Q exp(-2(1-c)t).

Hence

    M_S(|U|2)<=C S^(-2(1-c)/kappa).                     (14)

For either squared observable with beta the exponent in (13) or (14), its unnormalized vortex integral I_S(z) satisfies

    integral I_S dnu<=C S^(1-beta).

Markov at S=2^n and summability of C2^(-n epsilon), followed by Borel-Cantelli and monotonicity of I_S, prove

    I_S(z)=O_(z,epsilon)(S^(1-beta+epsilon))            (15)

for nu-almost every z and each epsilon>0. Here 1-beta>0 in the stated c interval. The estimate with epsilon=0, or an individual lower occupation rate, is not supplied.

## 5. Escape, occupation and the exponent comparison, A370

Let M=||U||_infinity and R>M/c. On the exterior of Q=B_R,

    d_t |Phi_t y|>=c|Phi_t y|-M.

Thus points outside Q escape and Q is forward invariant for Psi. The points of Q never leaving Q under Phi form

    K_R=intersection_(t>=0) Psi_t Q.

Its volume is zero since the nested sets Psi_t Q have volume exp(-dt)|Q|. All other points escape to infinity. With only rho_ell in L1, dominated convergence in (12) therefore gives

    M_S(F)->0                                         (16)

for every bounded continuous F vanishing at infinity. A smooth compact F equal to1 near supp nu satisfies (16), although it equals1 everywhere on that support. This is a direct demonstration that such long-vortex means do not identify values on supp nu.

For every finite-volume measurable E, if rho_ell is bounded, (12) gives

    integral nu(dz) integral_(-S)^S 1_E(Gamma_s z)ds
      <=C |E| S^(1-d/kappa)=C |E| S^(a/kappa).         (17)

A matching lower bound requires additional information. The package's stated sufficient conditions are: nu is carried by a compact topological attractor Lambda for Psi; rho_ell>=b>0 almost everywhere on a neighborhood N of Lambda; E is a compact positive-volume subset of its topological basin. Attractor trapping and compactness give a common t_E after which Psi_t E lies in N. Formula (12) then gives the lower bound b|E|exp(-dt), and multiplying by2S gives the matching exponent. This is an averaged assertion with those explicit conditions.

Even an independently proved individual occupation lower bound of order S^(a/kappa-epsilon), combined with (15) for H0^2, would force a zero Hopf ratio only if

    1-2a/kappa<a/kappa,

or c<2/7. Using |U|2 instead gives 2(1-c)>3c, or c<2/5. These are algebraic thresholds outside the target interval. This calculation does not apply the present energy theorem below its established range. No pointwise lower bound is inferred from (17), recurrence, or a dimension count.

For completeness the conservative Hopf ratios can be justified by the following complete time change. Put f=(1+|y|2)^((k+2)/2). A048 gives |Gamma_tau y|<=C_y(1+|tau|)^(c/kappa), hence f(Gamma_tau y)<=C_y(1+|tau|), because (k+2)c=kappa. Thus the new time integral of 1/f along either infinite Gamma semiorbit diverges logarithmically. The field fOmega is complete. Its invariant measure is f^-1dy, finite because k+2>3; invariance follows from div(f^-1 fOmega)=0 and completeness. For integrable observables F and g>0 almost everywhere, the time-changed observables fF and fg are integrable with respect to that finite measure. Birkhoff followed by division on the invariant components gives the original vortex ratio. For h in L1, the identity integral_E h dy=0 on every invariant measurable E is equivalent to conditional expectation of fh onto the invariant sigma-algebra being zero. The h ratio is then zero; nothing analogous follows for |h| or H0^2. The exceptional sets in these ratio assertions are Gamma-invariant and can be transferred to nu by (11). The preceding bound proves the required time-change completeness without Dini decay or an assumed bound on Omega at infinity.

## 6. Dini high-power bounds and the exact saturation, A371

Assume in addition the full Dini derivative condition of A209-A210,

    integral_1^infinity sup_(|y|>=r)||DU(y)|| dr/r<infinity.

It supplies |U(y)|<=C(1+|y|)^-k. For exterior y, the lower radial growth and (1) give

    |BH0(Phi_t y)|<=C |Phi_t y|^(1-k).

The time integral to infinity converges uniformly on compact exterior sets because k>1 and |Phi_t y|>=b|y|exp(ct), after choosing the exterior radius large enough. Thus H0(Phi_t y) has a continuous limit on that exterior. Fatou and (1) show that the limit has zero L2 norm on each bounded exterior set. Continuity makes it identically zero. Integrating BH0 now gives

    H0(y)=a integral_0^infinity (U.B)(Phi_t y)dt,
    |H0(y)|<=C(1+|y|)^(-a/c).                          (18)

Continuity on the compact interior extends the bound there; H0 is globally bounded and tends to0. The normalization from Section1 is essential.

For p>0, radial integration of (18), |Phi_t Q| contained in B_(C_Q exp(ct)), and the Jacobian give

    integral_Q |H0(Phi_t y)|^p dy <=
        C_Q exp(-pa t)               if pa<d,
        C_Q(1+t)exp(-dt)             if pa=d,
        C_Q exp(-dt)                 if pa>d.         (19)

For |U|^p replace pa by p(1-c). There is no endpoint improvement hidden by increasing p.

Indeed take the backward-invariant ball Q from Section5. It obeys Q subset Phi_t Q for every t>=0. For every nonnegative locally integrable F,

    integral_Q F(Phi_t y)dy
       =exp(-dt) integral_(Phi_t Q)F(x)dx
       >=exp(-dt) integral_Q F(x)dx.                  (20)

If the last integral is positive, no upper bound C exp(-eta t) with eta>d is possible. This lower bound is a spatial average over Q; turning it into an m_ell-average would additionally require a density lower bound. It rigorously accounts for the core contribution in (19), without proving a nonzero core observable exists in any hypothetical Euler profile.

## 7. What is not established

No helicity sign theorem, no H0=0 assertion on a general invariant support, and no nonexistence theorem for arbitrary rotation follows. The local model is not an attractor with a positive-volume basin. The formal tail is not a nonlinear global profile. General nonuniform SRB conditionals give L1 smearing only; the bounded-density rate is conditional. Our separate regular-support smearing proposal investigates when the extra density hypothesis can be proved. It is not silently assumed here. The C2 coverage question remains open.

## 8. Sources and verification

The four complete coordinator result proofs and their exact question and answer are snapshotted and hashed in the team records. Their algebra was independently reconstructed above; no numerical or symbolic computation was needed. Foundational dependencies are A031, A040, A048-A049, A207, A277, A287, A308 and the Dini scattering results A209-A210, with their exact scopes retained. The coordinator's question is an input list, not a new proof of these dependencies. Collaboration uses the existing configured-model coordinator agent and its recorded package; the external referee's package does not itself attest a model model. No new model client or delegated process was launched.
