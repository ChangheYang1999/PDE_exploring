# Local scope of the next pressure scalar

Status: CONFIRMED A661-A664 after complete source and independent-proof postreads. This extends the local obstruction A650 and records what the next identities do on irrotational sets and scalar zeros. It excludes no general interface class.

## 1. Setting and dependencies

Let2/5<c<1/2, omega real, p=(1-c)/c, d=p-1 in(0,1/2), a=1-2c=cd, b(x)=(cI-omega J)x, q=2p/d, n=3p+1=3d+4 and nu=n/d=2q-1. On a punctured local domain use V,P2 with the five leading tail identities, their twisted homogeneities and actual regularity V in C1,alpha and W2,s locally for every alpha<1 and finite s, P2 in C2,alpha. Define

    W=curl V, k=b.V, S=P2-|V|2/2, Pi=P2+|V|2/2,
    Z=DV V+grad P2, C=curl Z,
    H2=Pi+b.Z=V.grad k-aS, S1=p1-V.Z.

The letter C in this section is a field, not a scalar constant. The necessary next equations are

    div Z=0, -Delta p1=2 tr(DV DZ),
    dk wedge dS1+dH2 wedge dS=0 on{W!=0},
    W.grad S1+C.grad S=0.                                  (1)

For actual global HF/natural profiles, A647-A648 and A653-A655 supply p1 and these identities for every target c, including c3/7, and every finite omega. No differentiated correction convergence is assumed. In the local analytic band below, p1 may instead be any distributional solution of the smooth Poisson equation satisfying the rank in(1), with no homogeneity premise.

Dependencies are the complete independent proofs for A617, A647-A650 and A653-A655, ordinary local elliptic regularity, and the calculus shown below. All claims are local except when expressly applied to the actual limits.

## 2. Integrating rank where k is nonzero

On a small vortical patch with k!=0, b.grad k=-ak!=0, so k is a submersion. Leading rank gives S=f(k), and its homogeneity gives f(k)=D|k|q. The first rank in(1) then reads

    dk wedge d[S1-f'(k)H2]=0.

In submersion coordinates a continuous scalar with this identity distributionally is independent of the two level coordinates. Equivalently its multiple of dk is a continuous closed form with a C1 local primitive. Hence S1=f'(k)H2+g(k). From H2=V.grad k-aS and Z=DV V+grad P2,

    p1=2V.grad P2-a f'(k)f(k)+g(k).

Absorb the displayed one-variable term into g. Thus rank is equivalent to

    p1=2V.grad P2+g(k).                                   (2)

If p1 has the actual degree -n, homogeneity gives g(k)=E|k|nu. Otherwise g is an arbitrary one-variable function at this stage. These are small-patch statements; constants need not agree across distinct vortical components.

The transport equation in(1) adds nothing on this patch. Indeed the first helicity correction is

    V.C+Z.W=W.grad S=0.

This follows directly from C=DW V-DV W and V.W=0. The differentiated Bernoulli identity gives W.grad H2+C.grad k=-a(V.C+Z.W)=0. Applying W to S1=f'H2+g and using W.grad k=0, and applying C to S=f(k), gives W.grad S1+C.grad S=0. The calculation uses Sobolev product rules, or smooth analytic functions for the band below; it does not silently add an independent equation.

## 3. The specified analytic band

Use precisely the A617/A650 band, near r1,z0, on its vortical side z>0. Write w=1-z2,

    V=r^-p(R e_r+H e_theta/sqrt(w)), P2=r^-2p Q,
    H'=(1-d)R, R(0)=1,H(0)=0,R'(0)=0,
    S=-r^-2p R^q, k=c r^-d R.

These analytic initial data, and the leading pressure equation, fix the branch. The checked coefficients are

    R=1+[d(d-2)(d-1)/(2(d+2))]z2+O(z4),
    Q=-1/2-(1-d)z2/2+O(z4).

A650 computes the complete required fourth-order jets and shows that a homogeneous candidate

    p1=r^-n[-4pRQ-2HQ'+C0 R^nu]

has constant Poisson coefficient zero only at

    C0=-2(5d4+23d3+44d2+38d+16)/[(3d+4)(2d2+3d+4)].

At that value the residual -Delta p1-2tr(DV DZ) has z2 coefficient

    R2=4d(d-1)F7(d)/[(d+2)2(2d2+3d+4)]>0,               (3)
    F7=15d7+96d6+303d5+532d4+384d3-48d2-376d-96.

The exact sign is established by F7<=-96-(12245/64)d-48d2<0. The coordinator's residual uses the opposite sign, and agrees. These already checked data are inputs here; no new series computation is performed.

## 4. Nonhomogeneous p1 cannot repair this band

Rank first gives(2). It also forces p1 to be axisymmetric locally, since k_r=-dk/r is nonzero and the other quantities are axisymmetric. A distributional p1 solving the smooth Poisson equation on the analytic z>0 side is smooth there. In submersion coordinates g is therefore smooth on an interval of positive k values.

The interval can be chosen to include the interface values k=c r^-d for all r in a smaller open interval around1. Every such k is attained at positive z, so no boundary regularity of an initially given p1 is being assumed. Formula(2) with this smooth g itself supplies the one-sided extension to z0.

On that interface write K=c r^-d. Direct differentiation gives

    |grad k|2=d2 K2/r2,
    Delta k=chi K/r2, chi=-2d2(1-d)/(d+2).                (4)

For example Delta k/(K/r2)=d(d-1)+R''(0)=chi; k_z0 makes the first identity immediate. The prescribed smooth term in(2), and the Poisson source, both have radial degree -n-2. Restricting the Poisson equation to z0 and multiplying by r2 thus yields

    d2 K2 g''+chi K g'=L0 K^nu                           (5)

with a fixed coefficient L0. Its two homogeneous exponents are0 and

    beta=1-chi/d2=(4-d)/(d+2).

There is no repeated root and nu>beta>0. Hence

    g(K)=C0 c^-nu K^nu+A0+B0 K^beta.                    (6)

The particular coefficient is the same C0 as in Section3 because substituting its first term gives exactly that homogeneous candidate. The constant A0 is harmonic.

Substitute(6) throughout the positive side. The B0 term has Laplacian of radial degree -d beta-2, while the residual of the particular term has degree -n-2. These degrees are distinct. At any fixed sufficiently small positive z the latter residual is nonzero by(3). Two distinct powers of r cannot cancel on an open radial interval: dividing by one and differentiating in r makes the coefficient of the other vanish, then forces both to vanish. This is a contradiction.

Thus NO local p1, even nonhomogeneous or initially only distributional, can solve both the next Poisson equation and rank on this specified branch. The statement concerns neighborhoods meeting the specified interface; it is not a classification of other initial data, pressure levels or interfaces.

## 5. Irrotational components

On an open set W0, the leading kinematic identity grad k=-aV+b cross W gives V=-grad k/a and Delta k0. Thus V is a harmonic gradient and is smooth. The leading pressure equation gives Delta Pi0, so Z=grad Pi and C0. Consequently

    H2=-a Pi, Delta(p1+V.Z)=0.                           (7)

The last identity follows by differentiating the two harmonic gradient fields: Delta(V.Z)=2tr(DV DZ)=-Delta p1. There is no boundary term in an interior distributional identity. All first vorticity transport corrections vanish there.

The rank in(1) is not supplied on that open set. At a compact subset on which dk wedge dS is nonzero, the original scaled rank and its unscaled C1 convergence instead imply that the actual rescaled vorticity is identically zero there for every sufficiently large scaling time. No continuation of rank across an arbitrary irrotational component follows.

## 6. Regular and critical zeros of k

Suppose x0 is vortical, k(x0)=0 and dk(x0)!=0. Work in one small submersion box contained in W!=0. On its two connected sides the preceding homogeneous formulas give

    S=D_plusminus |k|q,
    S1=f_plusminus'(k)H2+E_plusminus |k|nu.              (8)

Constants are finite and fixed on each side of this box. H2 is continuous and bounded on a smaller box, q>6 and nu=2q-1>q-1. Therefore

    S1=O(|k|^(q-1)), S1=0 on{k0}, p1=V.Z there.         (9)

Continuity gives the statements on the zero surface. This uses the homogeneity of the actual p1; an arbitrary nonhomogeneous local pressure would allow an unprescribed g at k0.

If k is identically0 on an OPEN vortical patch, H2=-aS and the rank in(1) is identically zero. The transport correction may still restrict p1. No analogous estimate is established here at critical zeros of k. The A2 premise excludes the vortical k0 cases by A597, but A2 is not a consequence of these calculations.

## 7. Coordinate verification

The source gives full logarithmic-spherical formulas, with rho=log r, z=cos theta, chi=phi+t rho, t=omega/c and w=1-z2. A vector triple(A0,A1,A2) denotes r^-ell(A0 e_r+A1 e_theta/sqrt(w)+A2 e_phi/sqrt(w)). Derive its divergence using the spherical volume r2 sin(theta), its curl from the three standard spherical components, and its scalar derivative using partial_r chi=t/r, partial_theta z=-sqrt(w), partial_phi chi1. This gives respectively

    D_ell A=(2-ell)A0+t A0_chi-A1_z+A2_chi/w,
    C_ell A=(-A2_z-A1_chi/w,
              (ell-1)A2+A0_chi-t A2_chi,
              (1-ell)A1+t A1_chi+w A0_z),
    G_j f=(-j f+t f_chi,-w f_z,f_chi),
    T_(A,j)f=-j A0 f-A1 f_z+(t A0+A2/w)f_chi.

The dot product is A0 B0+(A1 B1+A2 B2)/w, and the cross triple is((A1 B2-A2 B1)/w,A2 B0-A0 B2,A0 B1-A1 B0). All these expressions have exactly the removed radial powers stated in the source. They reproduce its six vector/scalar corrections with b represented by r(c,0,-ctw).

In the rho,z,chi coordinates, d(r^-j f)=r^-j[-j f d rho+f_z dz+f_chi d chi]. Since d+n=4p, the two wedges in(1) have the same radial degree. Their three components are exactly

    c(-d K sigma_z+n sigma K_z)+2p(h j_z-j h_z)=0,
    c(-d K sigma_chi+n sigma K_chi)+2p(h j_chi-j h_chi)=0,
    c(K_z sigma_chi-K_chi sigma_z)+j_z h_chi-j_chi h_z=0,

where here K=R-tF, h=r^(2p)S, j=r^(2p)H2, sigma=r^n S1. These local symbols are distinct from the K in Section4 and the generic gradient subscript j above.

For zeta=(X,Y,T), direct covariant spherical differentiation of V along Z gives

    M0=X(-pR+tR_chi)-Y R_z-YH/w+T(R_chi-F)/w,
    M1=X(-pH+tH_chi)+Y(R-H_z-zH/w)+T(H_chi-zF)/w,
    M2=X(-pF+tF_chi)+Y(-F_z-zF/w)+T[R+(zH+F_chi)/w].

These are all three components, including the rotating frame terms. The pressure equation is L_n u1=-2 D_(3p+2) M, where

    L_j f=(w f_z)_z+(1/w+t2)f_chichi+t(1-2j)f_chi+j(j-1)f.

This checks the source coordinate supplement in full, on charts w>0. Distributional derivatives remain distributional when the actual corrections are not classically differentiable; Cartesian regularity, not the chart formulas alone, governs the axis. No extra mode truncation, axis symmetry or small-omega premise is introduced.

## 8. Verification and scope

The complete coordinator check and all three source proofs and the coordinate supplement were read. Sections2-7 were reconstructed analytically; the polynomial input is the already independently checked A650. No new computation or formal build was needed. Existing configured-model coordinator comparison is recorded; the inner model credential failure is not a response, and actual provider runtime is not independently attested. The focused resonance comparison remains pending.

This confirms one-germ exclusion at a stronger local pressure scope, and explains the exact limits of the next identities. General transmission, arbitrary scalar nodes, bare-decay derivative control and both unrestricted C2/C-infinity conjectures remain OPEN.
