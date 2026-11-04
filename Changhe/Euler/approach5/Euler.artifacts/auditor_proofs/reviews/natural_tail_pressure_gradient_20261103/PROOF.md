# The canonical pressure gradient under natural derivative decay

Status: the target profile pressure estimate and first velocity remainder are CONFIRMED in A516, with a separate configured-model moment proof. The wider static formulation is CONFIRMED in A785 after full independent scope review. The equilibrium-line calculation is recorded here, while A518 proves its rate conclusion for every vortical equilibrium by another argument. No derivative bound from velocity decay alone is obtained.

## 1. Exact statement

Let 0<c<1 and omega be any finite real number. Write J(y1,y2,y3)=(-y2,y1,0), A=cI-omega J, L=(1-c)I+omega J. Suppose U in C2(R3;R3), P in C1(R3) solve

    div U=0, LU+(DU)(Ay+U)+grad P=0.

Suppose there are finite C0,R0 and 0<k<3/2 such that

    |U(y)|<=C0 |y|^-k, |DU(y)|<=C0 |y|^(-k-1), |y|>=R0.   (1)

Then there are finite C1,R1, depending on this fixed profile and the stated parameters, such that

    |grad P(y)|<=C1 |y|^(-2k-1), |y|>=R1.                 (2)

There is a constant Pinf such that

    |P(y)-Pinf|<=C1 |y|^-2k.                              (3)

No bound on D2U at infinity, pressure Holder modulus, symmetry, helicity, smallness or uniformity of constants in omega is assumed. The pressure is the actual pressure in the equation. In the campaign interval 2/5<c<1/2, the confirmed natural bounds (1) have k=(1-c)/c in (1,3/2), so

    grad P=O(r^(1-2/c)), P-Pinf=O(r^(2-2/c)).              (4)

These natural bounds already follow from U->0 and |DU|=O(sqrt r), by A498, A476, A477 and A210. Using only bounded DU is a narrower sufficient hypothesis.

## 2. Canonical pressure and an exact spatial split

Set G=DU, F_ij=U_iU_j, Gamma=1/(4pi|x|), N=-Gamma. The divergence of the full momentum equation gives

    f=Delta P=-tr(G^2)=-partial_i partial_j F_ij.

Uniform decay makes U bounded and identifies the actual pressure gradient with the canonical one by A031, independently rederived in A500. In particular there is no nonconstant harmonic remainder. This normalization uses actual momentum, not the Poisson equation alone.

Let chi be smooth, equal to one on the unit ball and zero outside the radius-two ball, and set N_d=chi(./d)N for any d>0. The exact canonical gradient formula is

    grad P=grad N_d*f-partial_i partial_j grad(N-N_d)*F_ij. (5)

It follows distributionally by splitting the Newtonian kernel and integrating f=-partial_i partial_j F_ij twice by parts in the far part. The near kernel has L1 norm at most Cd and support in radius 2d. The far kernel is zero near zero, has L1 norm at most C/d, and satisfies the pointwise bound C|x|^-4 for |x|>=d. The convolutions are continuous under the present local regularity and boundedness. One can also verify independence of d by integrating against the smooth compact difference N_d-N_e. Thus (5) holds for every positive d, including d comparable to the evaluation radius. No d<=1 restriction belongs to the identity; that restriction was used only in earlier estimates with different hypotheses.

Fix |y|=R sufficiently large and choose d=R/8. On |z-y|<=2d one has 3R/4<=|z|<=5R/4. Therefore the near term is bounded by

    Cd sup_(|z-y|<=R/4)|f(z)| <= C R R^(-2k-2)
                                     = C R^(-2k-1).      (6)

For the far term split its integral into three regions. If |z-y|<R/2, then |z|>=R/2 and |F(z)|<=CR^-2k, so its contribution is at most

    (C/d) R^-2k <= C R^(-2k-1).                          (7)

If |z-y|>=R/2 and |z|<=2R, the kernel is at most CR^-4. Since 2k<3, (1) and compact boundedness imply

    E(2R):=integral_(|z|<=2R)|U(z)|^2 dz <= C R^(3-2k).

This region contributes at most C R^-4 E(2R)<=C R^(-2k-1). Finally, if |z|>2R, then |z-y|>=|z|/2 and its contribution is bounded by

    C integral_(2R)^infinity s^-4 s^-2k s^2 ds
       = C R^(-2k-1).                                   (8)

Together (6)-(8) prove (2). Every integral was absolutely bounded after the kernel split. Neither a singular-integral pointwise estimate on a merely bounded input nor an unspecified cancellation was used.

## 3. The pressure constant

The radial integral of (2) converges because k>0. Hence P(Rw) has a limit along each unit direction w, with error at most C R^-2k. The difference of P at two points on the radius-R sphere is bounded using a shortest spherical arc by

    pi R sup_(|y|=R)|grad P(y)| <= C R^-2k.

Thus all radial limits are the same Pinf, and convergence with (3) is uniform. This also proves that the pressure constant agrees with any previously established uniform limit. In the natural campaign range, H=P+|U|^2/2+(Ay).U has the same limit, since k>1 makes the last two terms vanish uniformly.

## 4. Consequence for an escaping vortical equilibrium line

Now assume 2/5<c<1/2, full C2/C1 equations, U->0, |DU|=O(sqrt r), and U.curl U=0 everywhere. Write a=1-2c and kappa=1+c. Let p satisfy B(p)=0 and W(p)!=0, where B=Ay+U and W=curl U. A478 gives U(p)=-Ap!=0. A468 and A496 give

    DB(p)^T U(p)=rho U(p), rho<=-a.

Let Gamma_tau(p) be its complete vortex line L. Completeness is A048. The bracket [B,W]=-kappa W and B(p)=0 give

    B(Gamma_tau p)=kappa tau W(Gamma_tau p).               (9)

The nonzero field W cannot vanish at a finite parameter time by uniqueness. The line cannot return periodically by A014. Its two halves L+ and L- are B-orbits with tau(t)=tau(0)e^(kappa t).

On L, helicity zero implies U.B=0; the Lamb identity gives grad H=-aU. On the regular connected H-level through p the rank identity A413 gives dg=-(rho/a)dH, g=U.B, and the covector transport law

    (B.grad)grad H=rho grad H-DB^T grad H.                 (10)

This applies to the whole line: it applies initially where U!=0, and its linear invertible transport along each half-line prevents U from reaching zero in finite B-time. Any finite nonzero vortex-parameter endpoint corresponds to finite B-time. The point p itself has U(p)!=0. Hence U is nonzero everywhere on L. Restricting (10) gives

    (B.grad)U=rho U-DB^T U,
    d/dt log|U|=rho-c-n.S n, n=U/|U|, S=sym DU.           (11)

Here and below a time origin is chosen at a fixed point of either half-line. Comparison with actual momentum yields the exact vector identity on L

    grad P=G^T U-(a+rho)U,
    n.grad P=|U|(n.S n-(a+rho)).                          (12)

Suppose one half-line is unbounded. Since r'=cr+U.y/r and U is bounded, every sufficiently large sphere is crossed only outward. Unboundedness implies r(t)->infinity. Integrating r'/r-c=O(1/r), with the exterior exponential lower bound, shows

    r(t) asymp e^(ct).

The natural derivative bound |S|<=Cr^(-1/c) is time-integrable along this orbit. Equation (11) therefore gives positive two-sided constants such that

    |U(y(t))| asymp e^((rho-c)t) asymp r(t)^((rho-c)/c).   (13)

By (4) and (12),

    |a+rho| <= C r^(-(2/c-1)-(rho-c)/c)+|S|.

If rho>c(1-(2/c-1))=-2(1-c), the right side tends to zero. Consequently

    rho=-a or rho<=-2(1-c).                              (14)

Thus a lower-window witness rho<=-2a with an escaping equilibrium vortex half-line must in fact satisfy rho<=-2(1-c). This conclusion remains conditional on the global derivative-growth screen that supplies the natural tail. It does not exclude all lower-window rates, does not establish escape of either half-line, and does not treat the periodic flat or irrotational equilibrium witnesses.

## 5. Dependencies, boundaries and scope

The pressure statement uses A031/A500 only to remove harmonic ambiguity and uses actual momentum to identify the Poisson source. Its rate proof otherwise uses only (1), the explicit kernels and absolute integrals. For k=3/2 this particular remote estimate gives R^-4 log R; for k>3/2 a compact-region contribution of order R^-4 can dominate. Neither extension is asserted in (2). There is no endpoint issue in the strict campaign interval.

The vortex-line corollary independently verifies the parts of Theory Agent B B31 it uses: (9)-(13). The regular-level rank and transport are the confirmed A413/A496 inputs. It does not rely on the proposed B32 classification of limiting measures or on the global geometry of the entire unstable sheet. No numerical or formal computation was needed.


## 6. Static canonical pressure and first velocity remainder

The static pressure lemma can be stated without Euler. For any divergence-free C2 field satisfying (1), take the canonical pressure with no harmonic addition. Splitting Gamma at d as above, now keeping its undifferentiated form, gives

    Pcan=(chi_d Gamma)*tr(G^2)+D_ij((1-chi_d)Gamma)*F_ij.

Both terms converge absolutely: the local kernel is integrable and the remote kernel is O(|x|^-3), integrable against the decaying tensor because k>0. Its distributional derivative is the gradient formula already used in Section 2. With d=R/8, the local term is bounded by CR^2 R^(-2k-2)=CR^-2k. In the remote term, |z|<=2R costs CR^-3 E(2R)<=CR^-2k; |z|>2R costs C integral_(2R)^infinity s^(-1-2k)ds=CR^-2k. Cutoff derivative terms in R/8<=|x|<=R/4 satisfy the same degree-minus-three bound. Therefore Pcan=O(r^-2k), directly fixing its zero limit. The gradient estimate and continuous representative follow from the continuous split convolutions. This is a static div-curl-pressure fact, not an Euler nonexistence result.

In the natural campaign setting of Section 4, put q=2k+1=2/c-1 and N=GU+grad P. The bounds already proved give |N|<=Cr^-q. Full momentum becomes

    LU+G Ay=-N.

For y!=0 and all sufficiently large s define Z_y(s)=exp(sL)U(exp(sA)y). Then

    Z_y'(s)=-exp(sL)N(exp(sA)y),
    |Z_y'(s)|<=C |y|^-q exp(-s),

since (1-c)-cq=-1. On compact annuli this is uniformly integrable. Thus Z_y(s) converges locally uniformly to a continuous V(y), with twisted homogeneity V(exp(tA)y)=exp(-tL)V(y). This V is the A210 leading tail, since the leading little-o formula there has this same limit. For large |y|, integrate from s=0 to infinity to obtain

    V(y)-U(y)=-integral_0^infinity exp(sL)N(exp(sA)y)ds,
    U(y)-V(y)=O(r^(1-2/c)).

Consequently, for k_H=(Ay).V,

    H-Pinf-k_H=O(r^(2-2/c)).

Indeed each of P-Pinf, |U|^2/2 and Ay.(U-V) has that bound. No derivative bound for this remainder follows just by differentiating the estimate. In particular it does not force a nonzero next coefficient when k_H or its gradient vanishes.

This section independently checks LIT131 Sections 1-5, received after Sections 1-5 of this reconstruction had been written. Both agents obtained the same proportional-radius cutoff argument. The exact source was read completely and pinned. The target profile consequence is now confirmed in A516 using the independent revised Theory Agent C C36 proof; the broader static scope is CONFIRMED in A785; focused configured-model comparison remains pending.
