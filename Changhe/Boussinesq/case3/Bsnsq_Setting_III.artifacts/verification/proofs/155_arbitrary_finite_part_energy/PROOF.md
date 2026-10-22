# Far-annulus conjugacies make finite-part energy arbitrarily negative

Status: CONFIRMED by the complete independent argument and the explicit dependency checks below. The initial proof was written before the controls or external-review requests. The conditional construction below supplies nonprofiles, not a B2 endpoint.

## 1. Statement, hypotheses and notation

Let beta>2, s=1/beta and m=1-2s. Put J(a,b)=(-b,a). Let smooth whole-plane fields Psi,Theta satisfy x-reflection parity, V=J gradPsi, V(0)=0, Omega=-DeltaPsi and W=beta X+V. Assume V is the canonical relative full-plane inverse ofOmega, V=o(r), and exact thermal transport holds:

    W.gradTheta=(beta-2)Theta.

Assume the disk energy E_L=int_(|X|<L)(|V|²/2+yTheta) has a finite power/log expansion with constant coefficient E_fp and remainder o(1). Also assume that on every fixed annulus away from0,

    R^(s-1)V(Rz) -> v_infinity(z)=J gradP(z) in C1,
    P(tz)=t^(2-s)P(z),  Omega_infinity=-DeltaP not identically0,  (1)
    |Theta(Rz)|<=C R^m.                                      (2)

P is smooth away from0 and odd in its first coordinate. The velocity limit is the actual leading field, not an added harmonic field. The leading expansion in150 implies(1)-(2) whenever its leading vorticity coefficient is nonzero; section6 checks this for the configurations of148.

Then compact smooth area-preserving conjugacies, supported in annuli tending to infinity, preserve the center, exact thermal transport, temperature signs, canonical inverse, and every exterior coefficient of the base fields, while their finite-part energies tend to negative infinity. Each individual change has compact support; there is no one bounded support containing the entire sequence.

If f=W.gradOmega+Omega-Theta_x is compact, each transformed residual is compact and its three affine moments are unchanged. If f is nonzero in a protected bounded set, the residual stays nonzero by taking the annulus beyond that set. Combining these deformations with154 gives every prescribed real E_fp, while preserving the base fields on that protected set and outside a sufficiently large fixed disk for the chosen target energy. No vorticity sign preservation or residual smallness is asserted.

## 2. Choose a compact Hamiltonian from the actual leading vorticity

Fix a nonnegative smooth radial function chi, supported in1<|z|<2 and positive on a nonempty annulus. Define

    h(z)=chi(|z|)Omega_infinity(z), H=J gradh.

Both are smooth and compactly supported away from0; h is odd. Let phi_t be the complete flow ofH. Compact smoothness gives a global smooth area-preserving diffeomorphism for every finite t. It commutes with x-reflection, fixes the disk|z|<=1 and the exterior|z|>=2, and preserves the intervening annulus. The last assertion follows because these two boundary neighborhoods are fixed and a diffeomorphism cannot carry a trajectory across them.

For a large scale R set delta=R^-s and

    h_R(X)=R^(2-s)h(X/R),
    H_R(X)=R^(1-s)H(X/R),
    Phi_(R,epsilon)(Rz)=R phi_(epsilon delta)(z).           (3)

Differentiating(3) inepsilon proves that it is precisely the flow ofH_R. It is the identity onB_R and outsideB_(2R). Define W_(R,epsilon)=Phi_*W, Theta_(R,epsilon)=Theta o Phi^-1 and V_(R,epsilon)=W_(R,epsilon)-beta X.

For completeness, the compact stream correction is

    Psi_(R,epsilon)-Psi
       =int_0^epsilon [W_(R,t).gradh_R-2beta h_R]dt.        (4)

Indeed the pushforward derivative is W_t.gradH_R-H_R.gradW_t. With divW_t=2beta this is J grad(W_t.gradh_R-2beta h_R). The stream in(4) is compact in the same annulus and zero near the material center. Its Laplacian correction has the canonical compact full-plane velocity J grad of that correction. Thus the chosen inverse and center subtraction are retained. The chain rule gives exact thermal transport. Reflection and all signs ofTheta are preserved. No finite-box inverse or harmonic strain is introduced.

## 3. Scaled kinetic-energy calculation

Write v_R(z)=R^(s-1)V(Rz). Fixepsilon, independent ofR. Since the time epsilon delta in(3) tends to0, the ordinary smooth compact-flow estimates give, uniformly on the fixed annulus,

    phi_(epsilon delta)(z)=z+epsilon delta H(z)+O(delta²),
    Dphi_(epsilon delta)=I+epsilon delta DH+O(delta²).

Their constants depend on fixedepsilon and finitely many derivatives ofH, not onR. On the bounded annulus v_R is uniformly bounded by(1). In material coordinates the exact transformed velocity is

    V_(R,epsilon)(R phi_(epsilon delta)(z))
      =R{Dphi_(epsilon delta)(beta z+delta v_R(z))
                                         -beta phi_(epsilon delta)(z)}.

Consequently, with

    B(z)=beta[DH(z)z-H(z)],

we have

    R^(s-1)V_(R,epsilon)(Phi_(R,epsilon)(Rz))
                    =v_R(z)+epsilon B(z)+O(delta).        (5)

Area preservation allows the kinetic difference to be integrated in the original z coordinates. Dividing it byR^(4-2s) and using(1),(5) gives

    Delta K/R^(4-2s) -> Q(epsilon)
             =epsilon A+epsilon² B_2/2,                 (6)
    A=int v_infinity.B, B_2=int |B|².

The integrals are ordinary compact integrals over1<|z|<2. No divergent kinetic integral is used. This is a limit at large support radius with a fixedepsilon, not an expansion that assumes arbitrarily largeepsilon is small.

## 4. A strictly negative limiting energy change

Put Lh=beta(z.gradh-2h). Direct differentiation gives B=J grad(Lh). Since h is compact and P is smooth on its support, integration by parts gives

    A=int gradP.grad(Lh)=int Omega_infinity Lh
     =-beta int h(z.gradOmega_infinity+4Omega_infinity)
     =-(4beta-1)int chi Omega_infinity²<0.                (7)

The last equality uses the homogeneity z.gradOmega_infinity=-s Omega_infinity and beta s=1. The last integral is strictly positive: the nonzero smooth homogeneousOmega_infinity is nonzero on an angular open set, andchi is positive on an annulus. Because A is nonzero, B_2>0 by the definition ofA. Choose the one fixed positive parameter

    epsilon_*=-A/B_2.

Then Q(epsilon_*)=-A²/(2B_2)<0. This choice need not be small; the actual dimensionless flow time epsilon_*R^-s still tends to0.

The potential-energy difference is simpler in the same material coordinates:

    Delta P=int [Phi_(R,epsilon)(Y)_2-Y_2]Theta(Y)dY.

On the support annulus, the displacement is O(Rdelta) andTheta is O(R^m). The area is O(R²), so

    |Delta P|=O(R^(4-3s))=o(R^(4-2s)).                    (8)

No temperature leading coefficient, integration by parts at infinity, or sign of the potential energy is needed. Equations(6)-(8) yield

    [E_fp(R,epsilon_*)-E_fp(base)]/R^(4-2s)
                           -> -A²/(2B_2)<0.              (9)

For eachR the new fields agree exactly with the base beyond2R. All divergent terms of the disk-energy expansion are unchanged, so the difference of finite parts is exactly the compact ordinary energy difference above. Since4-2s>0, (9) proves E_fp tends to negative infinity.

## 5. Affine moments and prescribed energies

Let deltaPsi and deltaTheta denote a fixed compact change above. The difference deltaf is compact. Oddness gives int deltaf=int y deltaf=0. The remaining compact integration by parts gives

    int x deltaf=(1-3beta)int x(-Delta deltaPsi)
                  -int delta(V_1Omega)+int deltaTheta=0.

Here x is harmonic and

    V_1Omega=partial_x(Psi_xPsi_y)
                      +partial_y((Psi_y²-Psi_x²)/2).

The difference of this divergence is compact, so its integral vanishes. Finally int deltaTheta=0 by area preservation and the invariant annulus. No separate integrability of the originalTheta orV is required. This rederives the compact-difference identity142/152.

For a target real number e, choose one finiteR beyond the prescribed protected set, so large that(9) gives E_fp(R,epsilon_*)<e. On this new configuration apply154 in two reflected disks disjoint from that protected set. Its exact compact twists have energy continuous in their parameter and tending to positive infinity. The intermediate value theorem gives some finite parameter with energy exactlye. The union of the annulus and the two twist disks is bounded for this chosen target. Therefore all configurations on this final continuous path agree with the original base outside one fixed larger disk, and on the protected set. In particular a retained point with nonzerof certifies that none becomes a profile. Existence of this scalar crossing asserts no ability to solve f=0.

## 6. Application to the signed zero-affine-moment constructions

Take148 with the polynomial core larger than the desired protected disk. Its references147 have the same exterior stream as126, whose leading vorticity is

    Omega_* =r^-s cos(theta)J(theta)+O_symbol(r^-1-s),
    J(theta)>0.

Although these references have negative vorticity inside, their exterior has the strict uniform lower bound kappa x r^-1-s on the right. The signed extension of135 uses one uniform strong-ball boundK over the parameter interval. If L is the gluing radius, its correction obeys the exact scaling formula

    Omega(Lz)=L^-s[omega_L(z)+L^-s(e+b[e])(z)],
    |e+b[e]|<=C_ax K |z_1| |z|^-1-s.

Taking the common L threshold larger so C_ax K L^-s<kappa/2 preserves strict positive vorticity in the exterior for every family member. This uses no positivity of the interior. All other choices in148 still work for every sufficiently largeL; thus its zero-moment selection can be made after imposing this threshold. By150 the actual leading angular limit exists, and this lower bound implies it is not zero. The leading stream from150 is homogeneous of degree2-s, with the nonresonant angular Poisson inverse of that angular vorticity; its full symbol remainder implies(1). The same packet gives(2), and150-151 give the finite energy expansion. These checks establish every new hypothesis needed above.

Protect the prescribed polynomial core, one nonzero-f point supplied by148, and its negative-vorticity point. The annulus in(3) is chosen beyond all of them, and the154 disks avoid them too. The resulting configurations have all of the following simultaneously: the original local normalization and center, exact thermal transport, canonical full-plane relative inverse, the same complete asymptotic coefficients as the148 base, nonnegative nontrivialTheta, sign-changingOmega, a nonzero compact residual with all affine moments0, and an arbitrarily prescribed real E_fp. OutsideZ_crit, their actual dipoleD is0 by148-150. In particular one can impose E_fp=0 as well. When beta is outsideZ_E, this fulfills151's necessary energy equality without fulfilling the vorticity PDE.

Every statement in this application depends on the precise already checked construction148 and its dependencies126,135,147,150,151. The deformation theorem in sections1-5 is independently proved under its own explicit hypotheses. No uniform residual bound, convergence to a profile, positive-vorticity profile, existence proof or full nonexistence endpoint follows.

Initial proof written UTC 2026-10-21T10:26:25.248586+00:00. Published 2026-10-21T10:38:11.243226+00:00. Independent controls and dependency audit complete. Three actualOpus5.5 requests returned no written audit; that availability limitation supplies no endorsement.

## 7. Verification evidence and review limitation

The proof above is analytic. Independent manufactured controls verify the dilation commutator, both energy scalings, the integration-by-parts coefficient, Cartesian and polar formulas for B, an independent centered-difference check of DH, the area Jacobian, and the actual nonlinear compact flow at five support radii. There are9 exact controls and9 numerical configurations, totaling45 flows. The manufactured nonzero temperature is not asserted to solve(T); these controls test energy algebra and scaling, not a B2 configuration or a certified numerical bound.

The first run integrated across the larger interval[1,2] and FAILED its finest quadrature tolerance. Its source, input and results are retained. Integrating on the exact bump support[11/10,19/10] with48,96,192 Gauss nodes resolves the flat endpoints: all tests pass, and the finest direct/IBP relative discrepancy is below8.65e-14. At R=10^18 the observed relative difference from the negative limiting energy is below3.58e-6. These are finite floating-point checks only. Canonical inversion for the deformed fields is proved by the compact stream formula, not by these numerical controls.

The application was checked against the actual126,135,147,148,150,151 and154 proofs, including135's exact scaling formula and uniform strong-ball norm. The positive exterior lower bound needed here uses only the common exterior, so148's interior negative-vorticity region causes no obstruction to it.

Actual model requests240,241,242 all returned model claude-opus-5-5 but no written audit text, with stop reason refusal and no written explanation. No model endorsement is claimed. Earlier152/154 written model reviews do not count as reviews of the new negative-energy lemma. The result is published for further team review with this limitation explicit. No decisive endpoint has been reached.
