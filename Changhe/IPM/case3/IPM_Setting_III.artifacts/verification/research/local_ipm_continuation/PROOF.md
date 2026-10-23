# Local continuation away from a possible singular point and symbol bounds

Date: 2026-10-20. Status: CONFIRMED by independent proof, fifteen exact identity checks at 2026-10-20T16:09:49Z, the lead's actual Opus 5.5 full audit at 16:20Z, and the independent referee cont1 audit returned at 16:25Z. The dependency and scope clarifications below were checked at 2026-10-20T16:27:00.883432+00:00. This is a regularity implication for an exact profile. It is neither existence nor nonexistence.

## 1. Exact local statement

Let D be an open disk in the plane and let (varrho,u) be smooth on D times (t_*,0), with smoothness on every closed time interval ending before zero. Suppose

    varrho_t+u.grad varrho=0,
    div u=0,  curl u=-partial_1 varrho.                         (1)

Assume

    sup_(t_*<t<0) (||varrho(t)||_Linfty(D)+||u(t)||_Linfty(D))<infinity,
    integral_(t_*)^0 ||grad varrho(t)||_Linfty(D) dt<infinity.  (2)

Then for every disk D' compactly contained in D and every integer k>=0, all spatial derivatives of varrho and u through order k are uniformly bounded on D' for t sufficiently close to zero. Constants can depend on D', k, the bounds in (2), and the smooth solution at a fixed time before zero.

The statement is local. No decay, integrability, boundary condition, or uniform global gradient bound is assumed. Only the local div-curl equations and the transport equation are used. It is not an application of an Euler theorem without checking its equations. The conclusion concerns spatial bounds. It does not assert a time-continuous extension of u at zero: varrho=0 and u(t,Z)=(sin(1/t),0) satisfy (1)-(2) but have no velocity limit. Both norms in the sum in (2) are bounded individually; a product bound would be insufficient.

## 2. Consequence for an exact Setting III profile

Assume the complete primary hypotheses, including exact transport, the canonical velocity, smoothness on every compact subset of the plane, and

    |rho(X)|+(1+|X|)|grad rho(X)| <= C(1+|X|)^gamma,
    0<gamma<1, ell>1.

Put p=1/ell. The already established ../far_field_holder/PROOF.md, Sections 3-4, gives

    |rho(X)|+|U(X)| <= C(1+|X|)^p.                           (3)

Under these hypotheses the conclusion of the local theorem is

    |D^k rho(X)|+|D^k U(X)| <= C_k (1+|X|)^(p-k)           (4)

for every nonnegative integer k, after changing the constant on a fixed compact set. Thus the symbol hypothesis Hsym used in the conditional Fredholm realization follows from the exact primary assumptions. No hypothesis about other equilibria, strict sign, or the global source basin is used in this implication.

Moreover the leading angular density Theta_0 is smooth, the scaled densities and velocities converge in C^k on every compact annulus for every k, and

    ||r^(-p)rho(r,.)-Theta_0||_C^k(S1) <= C_k r^(p-1).     (5)

This does not construct an exact profile, prove the simple-kernel hypothesis, remove Hdyn from the conditional index theorem, or justify a numerical profile by small residuals.

## 3. Elementary analytic facts used below

We fix q=4 throughout. The following usual local analytic facts are the only elliptic or interpolation inputs.

(a) For a smooth compactly supported vector field F on the plane,

    ||D F||_4 <= C (||div F||_4+||curl F||_4).             (6)

Indeed Fourier transformation expresses each derivative as a sum of order-zero Riesz multipliers applied to div F and curl F. Their L4 boundedness is the Calderon-Zygmund theorem. The same bound applies after taking any integer number of derivatives. It is not an Linfty Riesz-transform bound.

(b) On disks with radii in a fixed positive compact interval, Morrey's inequality gives

    [f]_C^(1/2) <= C ||D f||_4.                            (7)

The homogeneous version follows by subtracting the mean, applying Poincare's inequality and the usual W1,4 embedding. Constants are uniform in those radii.

(c) On the same disks, for m>=1 and 0<=j<=m, the bounded-domain Gagliardo-Nirenberg inequality gives

    ||D^j f||_(4m/j)
      <= C ||f||_infty^(1-j/m)
                 (||D^m f||_4+||f||_infty)^(j/m),         (8)

with j=0 interpreted as Linfty. A bounded extension from a ball to the plane, followed by the usual interpolation inequality, proves this form; the lower-order term handles constants. The estimate applies componentwise to tensors.

(d) If H is harmonic on a disk, its kth derivatives on a smaller concentric disk have L4 norm at most C_k times a negative power of the gap times ||H||_4 on the larger disk. This follows by differentiating the mean-value formula with a smooth radial averaging kernel supported within the gap.

All uses of (6)-(8) below are on smooth functions at t<0. Uniform estimates are obtained before taking a limit in time.

## 4. A change of variables with outward transport

It suffices to prove estimates on a smaller concentric disk after translating the center of D to zero. Translations here are changes of coordinates for a local evolution equation, not profile symmetries.

Take t0<0 close enough to zero, and define

    lambda(t)=1+sqrt(-t),
    lambda'=-1/(2sqrt(-t)), h=-lambda'/lambda>0,
    R(Y,t)=varrho(lambda(t)Y,t), V(Y,t)=u(lambda(t)Y,t),
    b(Y,t)=lambda^(-1)V(Y,t)+h(t)Y,
    Omega=grad_Y^perp R=(-R_2,R_1).                        (9)

Choose all Y-disks in a fixed disk whose lambda(t)-dilate lies in D for t0<t<0. They can be chosen to contain the desired smaller physical disk. Then

    R_t+b.grad R=0,
    div b=2h, div V=0, curl V=-Omega_2,
    Omega_t+h Omega+b.grad Omega=lambda^(-1)DV Omega.     (10)

The last equality follows from differentiating the first and using the two-dimensional identity J M^T J^(-1)=(tr M)I-M, with J the positive quarter-turn matrix. In particular Omega is a transported gradient, not the scalar curl of V. Only its second component occurs in curl V.

Let M bound |V|. On every circle of radius r>=r_min>0,

    b.Y >= lambda^(-1)|Y|[-M+|Y|/(2sqrt(-t))]>0           (11)

once t0 is sufficiently close to zero. Thus transport points outward on all the boundaries used below. Every radial nonincreasing cutoff supported in that radial region satisfies b.grad psi<=0. This sign is the reason that the cutoff transport term can be discarded.

Write

    K(t)=||Omega(t)||_Linfty(B_outer).

It is integrable in time by (2), since lambda is bounded and all transformed points lie in D. Both V and R are uniformly bounded there. All ensuing constants can absorb those two uniform bounds.

## 5. A weighted div-curl estimate with no gradient in the remainder

Let 0<=psi<=1 be a smooth compactly supported cutoff in B_outer, and let d=max(1,||D psi||_infty). Set

    T=||psi^6 D^2 V||_4,
    B=||psi^5 D V||_4,
    L=||psi^4 V||_4,
    F=||psi^6 D Omega||_4.

Apply (6) to psi^6 partial_j V and use div V=0 and curl V=-Omega_2. Differentiating the cutoff gives

    T <= C F+C d B.                                      (12)

For clarity, the weighted interpolation needed to close (12) does not introduce ||Omega||_infty in the remainder. Integrate one derivative by parts in integral psi^20 |DV|^4, componentwise. Derivatives falling on DV are bounded by

    C integral (psi^4|V|)(psi^6|D^2V|)(psi^5|DV|)^2
       <= C L T B^2.

Derivatives falling on psi are bounded by C d L B^3. Hence, if B is nonzero,

    B^2 <= C L T+C d L B,
    B <= C L^(1/2)T^(1/2)+C d L.

Young's inequality in (12) absorbs half of T, yielding

    ||psi^6 D^2V||_4
        <= C||psi^6 D Omega||_4+C d^2||psi^4 V||_4.       (13)

The result is trivial when B=0. The velocity bound makes the final factor uniformly bounded. This precise remainder avoids requiring K(t)^q to be integrable.

## 6. Differentiated gradient energy

Put F_ij=partial_j Omega_i. Differentiating (10), including the hY part of b, gives

    F_t+b.grad F+2h F
      =lambda^(-1)[DV F+(Omega.grad)DV-F DV].             (14)

The coefficient is 2h, not h. Multiplication by psi^24 |F|^2 F and integration gives, for Z=||psi^6 F||_4^4,

    Z'+6h Z-int (b.grad psi^24)|F|^4
       <= C||DV||_Linfty(supp psi) Z
            +C K ||psi^6 D^2V||_4 Z^(3/4).              (15)

The term 6h is 4*(2h)-div b. The transport boundary term on the left is nonnegative by (11). Substitute (13), use uniform boundedness of V, and apply Young's inequality with K left outside it. This gives

    Z' <= C(||DV||_Linfty(supp psi)+K)Z+C K d^8.          (16)

Only K, rather than a higher power of K, occurs in the inhomogeneous term.

## 7. A local logarithmic estimate with the radius loss recorded

Choose nested radii r_m increasing to r_* strictly inside B_outer, with

    r_(m+1)-r_m=c 2^(-m), m>=0,

and radial cutoffs psi_m equal to one on B_(r_m), supported in B_(r_(m+1)), nonincreasing, and with ||D psi_m||<=C2^m. Write Z_m=||psi_m^6 D Omega||_4^4.

For a query in B_(r_(m+1)), decompose V into a local Biot-Savart field and a harmonic remainder using one fixed cutoff of curl V that is one on a larger fixed disk containing B_(r_*). The local Biot-Savart field has Linfty norm at most C K, because its velocity kernel has size C/|z| and is integrable on bounded disks. The harmonic remainder and its first derivatives on B_(r_*) are bounded by C(||V||_infty+K), using (d).

The derivative of the local Biot-Savart field is a mean-zero degree-minus-two kernel with a bounded contact term. Let delta_m be a fixed small multiple of r_(m+2)-r_(m+1). In |z|<delta_m its density equals -Omega_2, and (7) bounds its Holder seminorm by

    H_m=C||D Omega||_L4(B_(r_(m+2))).

At a query X subtract Omega_2(X) on a query-centered circle. In |z|<epsilon the resulting integral is bounded by C H_m epsilon^(1/2). In epsilon<|z|<C it is bounded by C K log(C/epsilon). Choose

    epsilon=min(delta_m/2,(e+H_m)^(-2),epsilon_fixed).

The first bound is then uniform, and log(1/epsilon)<=C(m+1)+2log(e+H_m). The contact and harmonic terms contribute only C(1+K). Therefore

    ||DV||_Linfty(B_(r_(m+1)))
      <= C(1+K)[m+1+log(e+Z_(m+2))].                    (17)

There is no log(e+K) in (17): the Holder seminorm in the small disk is controlled by D Omega alone. All radii stay bounded below, so the homogeneous Morrey constant is uniform. There is no use of a nonexistent Linfty bound for a Riesz transform.

## 8. Closing the nested logarithmic inequalities

Integrate (16) for psi_m and substitute (17). The initial Z_m are uniformly bounded at t0, and integral K is finite. Thus, after increasing a constant d0>1, define

    Y_m=e+Z_m+d0^(m+1).

There are d>1 and a nonnegative integrable function a(t)=C(1+K(t)) such that

    Y_m(t) <= d^(m+1)
       +int_(t0)^t a(s)Y_m(s)log Y_(m+2)(s) ds.          (18)

The added d0^(m+1) absorbs both the m+1 in (17) into the logarithm and the cutoff cost 2^(8m) in (16). The larger d absorbs the finite integral of K and the initial norm.

Let the right side of (18) be X_m(t). Then Y_m<=X_m, X_m(t0)=d^(m+1), and

    beta_m(t):=log X_m(t)
       <=(m+1)log d+int_(t0)^t a(s)beta_(m+2)(s) ds.      (19)

For each fixed t<0, smoothness on the compact transformed disk throughout [t0,t] implies beta_m(s)<=C_t(m+1) for all s<=t. Indeed Z_m is bounded by the unweighted smooth norm independently of m, and the only other m dependence in X_m is exponential times a linear factor.

Iterating (19) N times for m=0 yields

    beta_0(t) <= log d sum_(j=0)^(N-1) (2j+1)A(t)^j/j!
       + C_t(2N+1)A(t)^N/N!,
    A(t)=int_(t0)^t a(s) ds.

The last term tends to zero for each fixed t. The full series equals (1+2A)e^A. Since A(t) stays bounded as t increases to zero, beta_0 and Z_0 are uniformly bounded. Consequently

    sup_(t0<t<0) ||D^2 R(t)||_L4(B_(r_0))<infinity.        (20)

There is no passage to t=0 before eliminating the smooth-but-not-uniform remainder. This order of limits is essential.

The bounded R values and a usual interpolation or Poincare estimate bound DR in L4 on a slightly smaller disk. Thus R is uniformly W2,4 there. Morrey embedding bounds DR uniformly and with exponent 1/2. Interior div-curl estimates applied to V then give uniform W2,4 and hence uniform C1,1/2 for V on another smaller disk. Since all choices above can be made around any compactly contained disk, these conclusions hold on every such disk.

## 9. Higher derivatives by a second, linear nested estimate

We now have uniform DR and DV bounds on compactly contained disks. We prove by induction that R and V have uniformly bounded Wk,4 norms on every such disk, for every integer k>=2.

Assume the assertion through k-1, and choose nested concentric disks B_(r_m) increasing to a disk strictly inside one where all lower norms are bounded. Differentiate R_t+b.grad R=0 k times and integrate |D^k R|^4 on the sharp disk B_(r_m). The boundary flux is nonnegative by (11). The dilation contributes (4k-2)h times the energy on the left, also nonnegative. The remaining commutator is

    lambda^(-1) sum_(i=1)^k C_(k,i) D^i V D^(k-i+1) R.   (21)

For 1<i<k use (8) with m=k-1 on DV and DR. The two interpolation parameters are (i-1)/(k-1) and (k-i)/(k-1), which sum to one; their Lebesgue exponents have reciprocals summing to 1/4. Holder's and Young's inequalities, together with the uniform DR and DV bounds, give

    ||(21)||_L4(B_(r_m))
       <= C_k[1+||D^k V||_L4(B_(r_m))
                   +||D^k R||_L4(B_(r_m))].              (22)

The terms i=1 and i=k satisfy the same estimate directly. The interpolation constants are uniform in m because the radii lie in a fixed positive compact interval.

To estimate D^k V, take a cutoff chi_m of curl V, equal to one on an intermediate disk between r_m and r_(m+1), supported inside B_(r_(m+1)), with derivatives of order j bounded by C_j delta_m^(-j). Let V_loc be its Biot-Savart velocity. Although this velocity is not compactly supported, its curl is compactly supported and smooth. Its first derivatives are the Calderon-Zygmund transforms of that curl. Taking k-1 further derivatives gives the extension of (6) needed here:

    ||D^k V_loc||_4 <= C_k||D^(k-1)(chi_m curl V)||_4
       <= C_k||D^k R||_L4(B_(r_(m+1)))+C_k delta_m^(-N_k).

Here curl V=-R_1. Every differentiated-cutoff term contains at most k-1 derivatives of R, bounded by the induction hypothesis. The undifferentiated V_loc has a uniform Linfty bound from the already uniform curl V. The harmonic difference V-V_loc is bounded on the intermediate disk, and (d) estimates its kth derivative. Hence, for a fixed D_k>1,

    ||D^k V||_L4(B_(r_m))
       <= C_k||D^k R||_L4(B_(r_(m+1)))+C_k D_k^m.        (23)

The coefficient of the next-disk high norm is independent of the gap. The gap occurs only in the known lower-order remainder.

Set E_m=1+||D^k R||_L4(B_(r_m))^4. Equations (22)-(23) and Young's inequality give

    E_m' <= C_k(E_m+E_(m+1)+D_k^(4m)).                   (24)

Remove the first term by an integrating factor. Increase d>1 to absorb all initial norms and the integrated last term. On the finite time interval this gives

    F_m(t) <= d^(m+1)+C int_(t0)^t F_(m+1)(s) ds.        (25)

For each fixed t<0, the F_m(s), s<=t, are bounded independently of m by smoothness on the limiting compact disk. Iteration of (25) N times leaves a remainder at most M_t[C(t-t0)]^N/N!, which tends to zero. The initial terms sum to

    d^(m+1) exp(d C(t-t0)).

This is uniform as t increases to zero. It proves the kth derivative estimate for R, and (23) proves it for V on a slightly smaller disk. At each order k use a fresh chain of nested disks inside a disk where the order-(k-1) bounds already hold. For any fixed k only finitely many such shrinkings are needed, and the starting disk can be chosen to leave a prescribed compact target disk inside the final one. The induction applies for every k. Sobolev embedding then gives uniform bounds for all spatial derivatives. This completes the local theorem.

## 10. Application to the physical similarity solution

For the exact profile set alpha=1/(ell-1), beta=ell/(ell-1), tau=-t, and

    varrho(t,Z)=alpha tau^alpha rho(Z tau^(-beta)),
    u(t,Z)=alpha tau^alpha U(Z tau^(-beta)).               (26)

The chain-rule verification in ../physical_scaling/PROOF.md shows that (26) satisfies (1), with no factor missing in the curl equation. On every compact physical disk separated from zero, (3) gives uniform bounds for varrho and u. The original gradient hypothesis gives there, for small tau,

    |grad_Z varrho(t,Z)| <= C tau^(alpha-beta*gamma)
       =C tau^(-kappa),
    kappa=(gamma-p)/(1-p)<1.                              (27)

The y-axis growth lemma gives gamma>=p, hence kappa>=0; only kappa<1 is needed for integrability. This is time integrable even when it grows as tau decreases. The local theorem therefore bounds every spatial derivative of varrho and u on every compact annulus away from zero.

Let R=tau^(-beta). For Z on the unit annulus,

    D_X^k rho(RZ)=alpha^(-1)tau^(-alpha+k beta)
                                      D_Z^k varrho(t,Z).

Since alpha/beta=p, this is bounded by C_k R^(p-k). The same computation applies to U. A finite cover of a fixed annulus and smoothness on the remaining compact profile region prove (4).

The earlier ../far_field_holder/PROOF.md, Sections 3-4, gives uniform convergence of the scaled densities and velocities on compact annuli. Their newly proved uniform bounds in every higher derivative imply convergence in C^k by local interpolation, for each k. The limit density |Z|^p Theta_0 is consequently smooth away from zero, so Theta_0 is smooth.

Finally write rho(r,theta)=r^p f(s,theta), U=r^p u(s,theta), s=log r. Exact transport gives

    partial_s f
      =-r^(p-1)[p u_r f+u_theta partial_theta f]
                         /[ell+r^(p-1)u_r].              (28)

Every angular derivative of f and u is uniformly bounded by (4), and the denominator is bounded away from zero for large r. Hence ||partial_s f||_C^k<=C_k exp(-(1-p)s). Integration from s to infinity proves (5). This gives a rate for the density, not by itself a full polyhomogeneous expansion or a second velocity coefficient.

## 11. Dependencies, provenance, and limitations

The local argument was reconstructed for the IPM gradient system. The expanding-coordinate and nested logarithmic strategy was prompted by a direct reading of Sections 5 and Appendix A of Dongho Chae and Jorg Wolf, "Localized non blow-up criterion of the Beale-Kato-Majda type for the 3D Euler equations," arXiv:1711.06415v2. That paper's Euler theorem is not invoked as an IPM theorem. Here the local logarithmic bound is obtained by an explicit kernel split and Morrey's inequality, and the higher-order step uses a separate linear nested estimate. In particular (14) retains the second dilation term.

The source-read record is ../../evidence/primary_sources/successful_reads_20261020.json. Standard analytic dependencies (Calderon-Zygmund L4 boundedness, Morrey, bounded-domain interpolation, and harmonic mean-value estimates) are stated in Section 3. The profile application also depends on the independently established p-growth and canonical far-field convergence, and the exact physical chain rule. No numerical state has been assumed to satisfy exact transport.

The counterexample in ../far_field_derivative_caveat/PROOF.md fails transport. It therefore does not contradict this implication; it demonstrates why the use of the full time-dependent transport system in Sections 4-9 is necessary.

The dependency chain is inverse and origin estimates, then ../far_field/PROOF.md for the continuous density limit and uniform angular-flow Jacobian, then ../far_field_holder/PROOF.md for uniform annular Holder control and passage through the inverse, and finally the present physical argument. The Holder proof uses only the original first-derivative growth bound, the kernel cancellation and its first derivative, and the exact angular Jacobian. It never uses this local theorem or higher symbol estimates, so there is no circularity. The continuous-limit file alone does not prove (3); supplying only that file to cont1 caused its correctly identified citation gap.

The cont1 proof and answer are in ../../../analysis/referee/cont1/. Its independent reconstruction checked the local argument, with an optional L4 extension not needed here. A transcription error in its displayed (A2) writes a product of the two norms instead of their sum; its proof uses individual uniform bounds, as explicitly stated in (2) here. The counterexample varrho=0, u=(1/t,0) shows why the product cannot replace the sum. This correction does not change the present theorem. The completed mathematical audit, the independent exact checks and the dependency audit justify CONFIRMED for the present statement. It supplies neither a smooth candidate nor a full-class NO endpoint.
