# Exact analytic nonsymmetric tail germs and global pressure constraints

Status: CONFIRMED at A590-A592 after the complete independent postread. The full349-line answer, its question and the actual coordinator check have been read. This constructs local tail fields on an equatorial angular band, not global tails and not full Euler profiles.

## 1. Statements and regularity

Let p>1, c=1/(p+1), omega be any finite real number, t=omega/c, a=1-2c=c(p-1), beta=(p-1)/(2p), Jx=(-x2,x1,0), A=cI-omega J. A twisted tail on a spiral-invariant domain has

    V(exp(sA)x)=exp(-(1-c)s)exp(-omega sJ)V(x),
    P2(exp(sA)x)=exp(-2(1-c)s)P2(x).

Set W=curl V, S=P2-|V|^2/2 and k=(Ax).V. The five conditions are div V=0, V.W=0, -Delta P2=partial_i partial_j(V_iV_j) distributionally on the stated domain, W.grad S=0, and grad k cross grad S=0 on {W!=0}. On a proper domain the pressure condition means the local Poisson equation. It does not assert agreement with the canonical pressure of any as-yet unconstructed global extension.

For every such p and omega there are real analytic nonaxisymmetric fields satisfying these conditions on a full periodic equatorial band D_delta={x!=0: |x3|/|x|<delta}. They have a regular zero of S where V and W are nonzero and grad S=-epsilon V. The radial velocity has zero azimuthal mean at every latitude of the band.

For global Cartesian C1,alpha tails on D=R3 minus{0}, with any fixed0<alpha<1, the global pressure is unique at1<p<3/2. It is C2,alpha locally and agrees with the canonical pressure. Every nonzero global tail has strictly negative spherical mean S. At omega0, global k0 and only regular scalar zeros force V0. These are global constraints, not proofs that the constructed band continues globally.

The new existence argument imports the classical analytic Cauchy-Kovalevskaya theorem for systems solved for the pure second derivative normal to analytic Cauchy data. All of its analytic and noncharacteristic hypotheses are checked below. The primary author notes Tsogtgerel Gantumur, Math580 Lecture Notes2: The Cauchy-Kovalevskaya theorem (October3,2011), Theorem18 and Corollary20, printed9-11, have been read in full at those statements and proofs. The higher-order form here excludes every pure second normal derivative on the right after matrix inversion; no cross-unknown ambiguity in the printed corollary is used. No formal-series truncation or numerical residual is used as existence evidence.

## 2. Geometry at a regular scalar zero

Homogeneity gives DV Ax=-[(1-c)I+omega J]V and hence

    E=grad k=-aV+Ax cross W,
    Ax.grad k=-ak,
    Ax.grad S=-2(1-c)S.

In a small neighborhood of a regular zero of S contained in {W!=0}, use S as one coordinate. Rank makes k=q(S) with q C1. The two scalar homogeneities give s q'(s)=beta q(s); therefore q(0)=0 and q(s)=C_plus/minus |s|^beta on the two sides. Since0<beta<1, bounded q' forces both constants to vanish. Thus k=E=0 throughout this neighborhood.

Crossing Ax cross W=aV with grad S, using W.grad S=0 and scalar homogeneity, gives grad S cross V=(S/beta)W. Hence grad S and V are linearly dependent on the zero set. Around a specified point where V!=0 and grad S!=0, shrink the neighborhood to preserve both. Their proportionality there is nonzero. No conclusion that the azimuthal or radial components vanish follows.

## 3. The exact angular equations

Let r=|x|, z=cos theta, w=1-z^2 and chi=phi+t log r. Work on |z|<1 and impose

    V=r^-p [tF e_r+(H/sqrt w)e_theta+(F/sqrt w)e_phi],
    P2=r^-2p u, S=r^-2p h,
    alpha=1/w+t^2, d=(2-p)t,
    e=(alpha F^2+H^2/w)/2, u=h+e.

All functions depend on z,chi and are2pi periodic in chi. In particular k=0. Write D0=F_z+H_chi/w. Direct differentiation gives

    W=r^(-p-1)[-D0 e_r+(p-1)F/sqrt w e_theta
                  +(-(p-1)H+twD0)/sqrt w e_phi].

Thus Ax cross W=aV identically, so V.W=0 too. The remaining equations are

    A0=H_z-alpha F_chi-dF=0,
    B0=2p h(F_z+H_chi/w)
                   -(p-1)(F h_z+H h_chi/w)=0,
    P0=L0(h+e)+tr(M^2)=0,
    L0 v=(w v_z)_z+alpha v_chichi+t(1-4p)v_chi+2p(2p-1)v.

Indeed div V=-r^(-p-1)A0 and W.grad S=r^(-3p-2)B0. The scalar radial derivative is r partial_r=-2p+t partial_chi on r^-2p functions, which, combined with angular Laplacian, gives Delta(r^-2p v)=r^(-2p-2)L0 v.

For completeness the exact matrix M=r^(p+1)DV in orthonormal spherical input/output frames is

    [ -ptF+t^2 F_chi,       -t sqrt(w) F_z-H/sqrt(w),  (tF_chi-F)/sqrt(w) ]
    [ (-pH+tH_chi)/sqrt(w),  tF-H_z-zH/w,              (H_chi-zF)/w       ]
    [ (-pF+tF_chi)/sqrt(w), -F_z-zF/w,                 tF+(F_chi+zH)/w   ].

This is checked entry by entry: the radial column differentiates coefficients with r partial_r=-p+t partial_chi; the theta column uses partial_theta=-sqrt(w)partial_z and partial_theta e_r=e_theta, partial_theta e_theta=-e_r; the phi column uses partial_phi e_r=sqrt(w)e_phi, partial_phi e_theta=z e_phi, and partial_phi e_phi=-sqrt(w)e_r-z e_theta. Consequently tr(M^2) uses only first derivatives. Once A0=0, div div(V tensor V)=tr(DV^2), so P0 is precisely local Poisson. No second derivative is silently assumed for a general tail in stating that distributional identity.

## 4. A convergent periodic analytic construction

Solve partial_z A0=0, partial_z B0=0 and P0=0. Their coefficient matrix for the pure normal derivatives(H_zz,F_zz,h_zz) is

    [ 1, 0,          0         ]
    [ 0, 2p h,      -(p-1)F    ]
    [ H, w alpha F,  w         ].

The determinant is w[2p h+(p-1)alpha F^2]. All other terms are analytic in z, the unknowns and derivatives of total order at most2 with at most one z-derivative, provided w>0 and that determinant is nonzero. The analytic system is therefore in the standard Cauchy-Kovalevskaya normal form after matrix inversion.

Choose0<epsilon<(p-1)(1+t^2)/(2p), and prescribe on z0

    F=sin chi, H=0, h=epsilon(cos^2 chi-1/4),
    F_z=0, H_z=(1+t^2)cos chi+d sin chi, h_z=0.

The initial A0 and B0 vanish. The determinant factor there equals

    (3/2)p epsilon
      +[(p-1)(1+t^2)-2p epsilon]sin^2 chi>0.

Thus every point of the analytic Cauchy circle has a convergent analytic solution. Analytic uniqueness makes overlapping local solutions agree; compactness gives a common positive band width and periodicity. The determinant remains nonzero on a smaller common band by continuity. Since the solved equations make A0 and B0 constant in z, their zero Cauchy values imply A0=B0=0 throughout that band. This checks the undifferentiated constraints, not merely their z-derivatives.

At r1,z0,chi=pi/3, the data give F=sqrt(3)/2, H=h=h_z=0, h_chi=-sqrt(3)epsilon/2. Therefore

    V=(sqrt(3)/2)(t e_r+e_phi),
    grad S=-epsilon V,
    W=(p-1)(sqrt(3)/2)e_theta!=0.

This is a regular scalar zero with the required nonzero alignment. The transformation (F,H,h)(z,chi) to(-F,-H,h)(z,chi+pi) preserves A0,B0,P0 and the data. The matrix M changes sign while tr(M^2) and e do not. Analytic uniqueness therefore makes F,H antiperiodic under chi->chi+pi and h periodic under that shift. Thus the chi-means of F and the radial component tF vanish at every latitude. Since F is initially sin chi, it continues to take both signs at every latitude after decreasing the band width. Nonaxisymmetry is exact for every omega, including0. No finite angular Fourier support is claimed away from the Cauchy circle.

The scalar functions and spherical frames combine into real analytic Cartesian fields on D_delta: r>0, sin theta>0 there, log r is analytic locally and periodicity removes the angular branch choice. The linear spiral fixes z and chi and rotates the frame, so homogeneity is exact.

## 5. A separate local plateau and its failure at the poles

Setting R=F=0 and H=H0!=0 in the general divergence-free angular field gives a meridional plateau. Its pressure scalar obeys

    (w h')'+2p(2p-1)h
      =-H0^2[(2p^2+p+1)/w+4z^2/w^2].

One can check this from the displayed M with F0,H constant: tr(M^2)=H0^2[2p/w+2z^2/w^2], while e=H0^2/(2w), (w e')'=H0^2[1/w+2z^2/w^2], and 2p(2p-1)e=p(2p-1)H0^2/w. Their sum is the stated forcing. Analytic ODE data h(z0)=0,h'(z0)!=0 give a local regular zero and nonzero vortex there. But |V|=|H0|r^-p/sqrt(w) diverges at the poles. This is not a global tail.

## 6. Global forced pressure and its strict mean

Now assume1<p<3/2 and global Cartesian V in C1,alpha locally on D. Distributional divergence-free mollification proves partial_i partial_j(V_iV_j)=tr(DV^2). The right side is C0,alpha, so local elliptic regularity makes P2 C2,alpha. If V is merely C1, the asserted C2,alpha gain would require an extra premise; the actual tails supply C1,alpha for every alpha<1.

On the unit sphere the pressure operator is

    L_t=Delta_S2+t^2 partial_phi^2
                     +t(1-4p)partial_phi+2p(2p-1).

It acts on Y_lm with eigenvalue

    2p(2p-1)-l(l+1)-t^2 m^2+i t(1-4p)m.

If tm!=0 its imaginary part is nonzero. Otherwise zero would require l(l+1)=2p(2p-1), strictly between2 and6, impossible. The operator is uniformly elliptic for each fixed finite t; its spherical harmonic expansion gives an inverse, with high-frequency denominators of quadratic size and no low-frequency kernel. Elliptic regularity then gives the unique global pressure for the continuous Holder source. Equivalently Fredholm index0 and trivial kernel give existence and uniqueness.

The canonical stress pressure exists here: |V|^2 is integrable at0 since2p<3, the far kernel is integrable with this decay, and the local principal-value cancellation is justified by C1 regularity. Kernel covariance gives its exact twisted homogeneity. It solves the same Poisson equation, hence equals the unique pressure just found. Local Cauchy pressure need not match this global choice. Removing nonaxisymmetric harmonic pressure ambiguity does not remove forced nonaxisymmetric modes.

Write Rv=integral_S2 |V.n|^2 and Tv=integral_S2 |V_T|^2. The independent radial annular test in the team records gives

    integral_S2 S=-[(3p-2)Rv+(p+1)Tv]/(2p).

It uses only global Poisson, divergence-free velocity and twisted homogeneity. Both coefficients are positive for p>1, so this mean is negative for nonzero V; if S is identically zero, V0. There is no pointwise sign conclusion.

## 7. A global regular-node argument when omega is zero

Suppose p>1, omega0, global k0, global C1,alpha V, div V0 and W.grad S0; assume scalar h on the sphere is C1 with empty zero set or every zero regular. The radial component then vanishes. The divergence-free tangential field has a global C2,alpha stream function psi with F=w psi_z and H=psi_chi: the closed one-form F dz/w+H dchi is intrinsically exact on S2. Pole regularity is part of the Cartesian assumption.

The scalar equation gives

    grad_S2 psi.grad_S2 h=beta^-1 h Delta_S2 psi.

Away from h0, this says div_S2(|h|^-beta grad psi)=0. If there are no zeros, test by psi on the whole sphere. Otherwise compactness and the regular-zero hypothesis give |grad h| bounded below near its zeros and uniformly bounded lengths of nearby level curves. On |h|=epsilon the displayed scalar equation gives |partial_n psi|<=C epsilon. Integrating the weighted equation against psi over {|h|>epsilon}, its boundary term has absolute value<=C epsilon^(1-beta). Since beta<1 and the regular-node weight is locally integrable, letting epsilon decrease to0 gives integral |h|^-beta |grad psi|^2=0. Thus V0.

This is a restricted global statement. Local k0 at one regular zero is insufficient for it. Any real analytic global continuation of the band construction would have k0 everywhere by the identity theorem; for omega0 it would therefore require at least one critical scalar zero. No continuation is constructed. The stronger controlled-node/global-rank argument is treated separately; it does not turn these local germs into global examples.

## 8. Verdict scope

The analytic band construction is convergent and satisfies every stated local equation. It rules out a contradiction from those local equations alone at a regular zero. It does not rule out arguments using pole regularity, global pressure, nodal continuation or the full profile equation. No global nonsymmetric tail, all-mode symmetry theorem, finite-mode exclusion or full rotating profile has been obtained. No new numerical or symbolic computation is needed: all matrix entries and determinants used here are independently derived above. Source numerical residual checks are not used as proof.
