# Exact center-strain certificates for the saved native-source representation

Status: CONFIRMED independent derivation and separate exact integer checking of seven saved states; manufactured controls pass. Actual Opus5.5 requests249/251 returned no written audit. This checks finite serialized fields. A negative mismatch at finitely many beta values is not an exclusion of a root between them, a fold, or a global profile.

## 1. Representation and precise scope

Let beta>0 be the profile exponent. For a source block choose b>0, L>0, an integer K>=1, a clamped B-spline basis B_j of degree p with knots k_j in[0,1], and coefficient arrays c_nj. Inactive coefficients in modes n are set to zero for j<floor(n/2), as specified by the saved representation. Define

    z=(1+r²/L²)^(-1/(2b)), t=1-z, eta=-y/r,
    C_n(t)=sum_j c_nj B_j(t),
    rho_n=1 for n even, rho_n=r/sqrt(r²+L²) for n odd,
    Omega=x z^(b+1) sum_(n=0)^(K-1) C_n(t) T_n(eta) rho_n.

All arrays, knots and scalar parameters below are treated as the exact real values of their recorded binary floating-point numbers. The certificate includes the frozen knots used by the independent evaluator. It does not claim that these binary knots equal the ideal real-number powers in a nominal grid recipe. No fitted code or saved inverse matrix is used.

The source is O(r^(-1/b)) at infinity and O(r) at0. Its relative whole-plane velocity is defined by the kernel difference K(X-Y)-K(-Y), with K obtained from -Delta Psi=Omega and U=(-Psi_y,Psi_x). This difference converges absolutely at infinity. The derivative giving the center strain converges absolutely at both0 and infinity for the stated representation. An additive velocity constant does not affect this derivative; no affine harmonic strain is included.

For K<=3, absent modes are zero. The exact strain is

    c=Psi_xy(0)=-bL/4 sum_j (c_1j-c_3j) (k_(j+p+1)-k_j)/(p+1).       (1)

For the native-source transport velocity V=V_self+lambda V_seed, each block retains its own b,L,K,p,knots and arrays. Its strain is c_mix=c_self+lambda c_seed. Hence

    m=c_mix-1-beta/2.                                                (2)

Formula(2) is linear in each frozen coefficient block. It gives an exact rational number when its input binary numbers are interpreted exactly. A rational enclosure strictly below0 proves the stored field fails the center-strain condition.

## 2. Whole-plane derivation and sign

The kernel convention gives

    Psi_xy(0)=(1/pi) int_(R²) x y Omega(x,y)/(x²+y²)² dxdy.

In polar coordinates this is (1/pi)int cos²(phi)sin(phi) times the radial divided source, dr dphi. Orthogonality of the Chebyshev trigonometric functions gives

    (1/pi) int_0^(2pi) cos²(phi)sin(phi) T_n(-sin(phi))dphi
         =-1/4 for n=1, +1/4 for n=3, and0 otherwise.

For example the n=1 integral is -int cos²(phi)sin²(phi)/pi=-1/4, fixing the sign. The n=3 identity follows from T_3(q)=4q³-3q. Higher modes vanish by trigonometric orthogonality. The radial factors for the odd surviving modes satisfy the exact identity

    z^(b+1) [r/sqrt(r²+L²)] dr = bL dt.

Indeed dr/dt=bL² z^(-2b-1)/r and sqrt(r²+L²)=L z^(-b). Substitution proves

    c=-bL/4 int_0^1 [C_1(t)-C_3(t)]dt.

The integral of a degree-p normalized B-spline over its whole support is (k_(j+p+1)-k_j)/(p+1). This follows from the usual derivative identity for the degree-(p+1) B-splines by integration and telescoping; equivalently induction in the defining Cox-de Boor recursion gives the same support-length formula. Every support here lies in[0,1]. Summing proves(1). This is an exact full-plane moment, with no artificial outer boundary.

## 3. Center equations and a certificate

For fields differentiable at the center, with Theta=a x²+O(|X|³), Omega=q x+O(|X|²), the moving field has W(0)=0 and DW(0)=diag(beta-c_mix,beta+c_mix). The constant limits of the divided defining residuals are

    R_F(0)=-2 m a,
    R_G(0)=(beta-c_mix+1)q-2a.                                      (3)

For the defining unforced B2 field use c_self instead of c_mix in(3); write m_self=c_self-1-beta/2. The corresponding limits are R_F,self=-2m_self a and R_G,self=(beta-c_self+1)q-2a. Thus either nonzero mismatch, together with a!=0, contradicts the corresponding thermal equation. The native-source sum is a forced diagnostic; it must not be called the inverse of the unknown vorticity alone. For a finite representation with only the needed low-order jets, (3) remains a direct leading-coefficient diagnostic even if higher Cartesian smoothness has not been proved. No regularity certification is inferred from the center check.

A certificate stores the source archive hash, active coefficient arrays and frozen knot values, exact rational values of(1)-(3), and rational decimal bounds. A separate checker reloads the original archive, checks its hash and schema, reconstructs the active blocks and knots, and verifies every equality and inequality using integer arithmetic. Imported values alone are not proof; the derivation above supplies the soundness implication. Numerical B-spline integration and angular quadrature are supplementary manufactured controls.

## 4. Limits

A mismatch certifies failure of this literal serialized field at its own beta and lambda. It gives no bound on optimization error, no continuity statement for the exact solution branch, no exclusion over a beta interval and no fold theorem. Source and unknown blocks must not be silently evaluated in the same retied basis when their recorded geometries differ. The source coefficient, center strain, temperature amplitude and residuals are all reported, rather than using a strain projection that changes the field under audit.

Written UTC 2026-10-21T11:27:30.515654+00:00, before certificate code.
