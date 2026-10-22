# Interface terms in the scaling tangent of the stored modal trial

Date 2026-10-22T02:30:29.710683+00:00. This argument is written before the new exact numerical application. The theorem and application remain OPEN until independent arithmetic, actual model review and later own adjudication. No exactly joined trial is changed or refuted here.

## Statement and notation

Let rho be even in x, odd in y, smooth on finitely many circular regions, with smooth one-sided traces at their positive radii R_j. Assume rho and its piecewise first derivatives are O(r^3), O(r^2) at0 and O(r^k), O(r^(k-1)) at infinity, with k<1. Finite angular Fourier sums suffice below. Set D=x partial_x+y partial_y=r partial_r. A plus trace is from larger r, and [rho]_j=rho(R_j+)-rho(R_j-). The surface distribution delta_(r=R) acts by integration against arc length on that circle. Define K_pw=rho-D_pw rho, using the classical derivative separately in each open region. Define M=sum_j R_j [rho]_j delta_(r=R_j).

Use the canonical full-plane linear velocity U[h]=(-partial_y psi[h],partial_x psi[h]) with -Delta psi[h]=partial_x h, removing growing harmonic additions by the sublinear velocity convention, and let Sigma(h)=partial_xy psi[h](0). For compactly supported surface distributions this convention is understood by the same distributional inverse, evaluated away from their supporting circles. Near0 every term below is smooth enough to define Sigma. If rho=sum_(odd l>=1) F_l(r) sin(l theta), then F_l uses full-angle normalization1/pi.

The following exact assertions hold:

1. D rho=D_pw rho+M as distributions. Thus the derivative at lambda=1 of lambda^(-1)rho(lambda X) is D rho-rho=-K_pw+M. Unless every jump vanishes, rho is not W^(1,2)_loc across the interfaces and this scaling derivative is not the ordinary piecewise function -K_pw.
2. Sigma(rho)=integral_0^infinity r^(-2)F_3(r)dr, including for the piecewise rho. Consequently

   Sigma(K_pw)=sum_j [F_3]_j/R_j,  Sigma(M)=Sigma(K_pw),  Sigma(rho-D rho)=0.

3. Put eps_pw=(ell X+U[rho]).grad_pw rho-rho for any fixed real ell, and define the classical expression away from all interfaces

   L_rho h=(ell X+U[rho]).grad h-h+U[h].grad rho+(Sigma(h)/3)D rho.

   Then, on each open region,

   L_rho K_pw-(eps_pw-D_pw eps_pw)=U[M].grad rho+(Sigma(K_pw)/3)D rho.

   This interface correction is separate from any normalization defect. For a smooth joined rho, M=0 and Sigma(K)=0, so L_rho K=eps-D eps, with no requirement that the stored scalar ell obey an additional normalization equation. The result does not assert that the displayed interface correction is nonzero for every discontinuous rho.

For the literal stored modal trial, define all coefficients by their exact binary64 dyadics, both joins by the exact stored logarithmic knots a,b, and rho=r^3 cos^2(theta)sin(theta)sum_(m=0)^259 a_m(log r)cos(2m theta). The inner and outer exp-polynomial corrections are interpreted literally, not solved again from exact matching equations. The clamped degree-seven spline coefficients are S_mi. Write

 J_in,m=delta_(m0)+sum_j D_mj+Ei_m0-S_m0,
 J_out,m=sum_q Aout_mq+Eo_m0-S_m,last,
 P(z)=z_0/4+z_1/8-z_2/8-z_3/8.

Then the actual radial jumps have signs -J_in and +J_out, and

   Sigma(K_pw)=-exp(2a)P(J_in)+exp(2b)P(J_out).                 (1)

The new arithmetic application will check all520 exact modal jumps by two input/algorithm paths and enclose(1) independently with Arb and mpmath.iv. It must prove exclusion of zero before refuting Sigma(K_pw)=0 for these literal inputs. There is no asserted value before that calculation. The mathematical exactification that recomputes joining corrections is a different object and is excluded from this application.

## Proof of the distributional and regularity claims

Integrate a classical derivative against a compactly supported test function in each region. Boundary terms at a shared circle add to the outward jump times its outward unit normal. Hence grad rho=grad_pw rho+sum_j [rho]_j e_r delta_(r=R_j). Dotting with X gives assertion1. Differentiation of the scaling pullback is justified distributionally by changing variables in its pairing with a test function and differentiating that smooth compactly supported test function. The result is D rho-rho.

If a jump is not identically zero, its smooth angular trace is nonzero on an open arc. Choose a smooth test function in angle supported on this arc, with its sign aligned with a nonzero component of [rho]e_r. Multiply it by a radial test function supported in a tube of width epsilon about the circle and equal to1 on the circle. The singular part of the derivative has a nonzero pairing independent of epsilon. The pairing with the locally bounded piecewise derivative tends to0. If the weak derivative were an L2 function, its pairing with these tests would tend to0 by Cauchy-Schwarz because the tests have L2 norm O(sqrt(epsilon)). This is a contradiction. Positive smooth radial weights on a compact annulus are equivalent to ordinary L2 there, so the same obstruction applies to weighted weak-H1 norms used elsewhere in this run. A quadrature of piecewise classical derivatives cannot remove this singular part.

## Proof of the strain moment

For an angular sine mode F_l sin(l theta), direct differentiation gives its two source terms

 partial_x(F_l sin(l theta))=(F_l'-l F_l/r)sin((l+1)theta)/2
                            +(F_l'+l F_l/r)sin((l-1)theta)/2.

Derivatives here may be distributions. The n=2 source coefficient therefore is f_2=((F_1'-F_1/r)+(F_3'+3F_3/r))/2. Solving the radial equation of -Delta gives the coefficient of r^2 sin(2theta) near0 as Gamma_2=(1/4)integral r^(-1)f_2(r)dr. This formula follows by the two fundamental solutions r^2 and r^(-2), whose Wronskian is -4/r; the sublinear velocity convention removes the growing far homogeneous solution and the regular origin removes the singular one. If the source is not supported away from0, the omitted small-radius integrals are higher order, since F_l=O(r^3). Both far endpoint terms vanish because k<1.

Distributional integration by parts gives integral F_l'/r=integral F_l/r^2; the jump deltas are included. Thus Gamma_2=(1/2)integral F_3/r^2. Since r^2 sin(2theta)=2xy, Sigma=2Gamma_2 proves the moment formula. These integrals converge at0 and infinity by the stated hypotheses. Equivalently this argument can be carried out after smoothing in the radial variable and passing to the limit; the same boundary terms are retained.

For K_pw its third density mode is F_3-r F_3,pw'. On each radial interval its weighted integral is -integral(F_3/r)'_pw. Summing the endpoint contributions, with zero limits at0 and infinity, leaves sum_j [F_3]_j/R_j. The third radial coefficient of M is sum_j R_j[F_3]_j delta(r-R_j), because area integration is r dr dtheta. Applying the same moment formula gives Sigma(M)=sum_j [F_3]_j/R_j. This proves assertion2 and all signs and radial factors in it.

## Proof of the corrected identity

The canonical velocity is a homogeneous Fourier multiplier of degree zero. Its scaling covariance U[lambda^(-1)rho(lambda X)]=lambda^(-1)U[rho](lambda X) follows either by rescaling the defining Poisson equation and its canonical growth convention, or by the multiplier. It remains valid distributionally for rho and the compactly supported circular distributions above. Differentiating in lambda yields U[rho-D rho]=U[rho]-D U[rho]. Assertion1 therefore gives

   U[K_pw]=U[rho]-D U[rho]+U[M].

Away from the circles all quantities are classical. Write V=ell X+U[rho]. The elementary commutator D(V.grad rho)=(D V).grad rho+V.grad(D rho)-V.grad rho and D V=ell X+D U[rho] give, by direct substitution,

   (V.grad-1)(rho-D rho)+(U[rho]-D U[rho]).grad rho=eps_pw-D eps_pw.

Insert the preceding velocity identity and the specified PLUS strain term. This is assertion3. Neither this derivation nor Sigma(rho-D rho)=0 invokes an equality between ell and a moment of rho. For unjoined rho no global product of singular distributions in the nonlinear residual is asserted; the identity is explicitly classical on the open regions.

## Exact modal application and a source-level limitation

The identity cos^2(theta)sin(theta)=(sin(theta)+sin(3theta))/4 and sin(l theta)cos(2m theta)=[sin((l+2m)theta)+sin((l-2m)theta)]/2 show F_3=r^3 P(a). Evaluating the inner/outer formulas at their zero log coordinates and using the clamped spline endpoint values gives J_in,J_out exactly. Substituting their oriented jumps into sum[F_3]/R proves(1). Nonzero coefficient jumps imply a nonzero angular jump, since a nonzero finite cosine polynomial cannot vanish on the open set where cos^2(theta)sin(theta) is nonzero.

The inspected floating Trial class defines its joins by the stored knots. Its TrialGreen source forms partial_x rho from classical piecewise radial derivatives and integrates those sources on the three regions. It has no interface source layers. The corresponding ideal exact calculation therefore solves -Delta psi=partial_x,pw rho, whereas the canonical stored-density inverse includes sum[rho](e_r)_x delta_(r=R). These two conventions must not be identified without a correction. A further diagnostic is available: its source-only strain differs from the canonical one by

   Sigma_source-Sigma_canonical=-(1/4)sum_j([F_1]_j+[F_3]_j)/R_j.       (2)

Indeed integration by parts using classical derivatives on separate intervals gives integral F_l,pw'/r=integral F_l/r^2-sum_j[F_l]/R_j. The preceding n=2 projection proves(2). Here F_1=r^3(a_0/4-a_2/8). The two engines may also evaluate(2). This concerns the ideal source-only convention, not a certified error bound for every floating operation or saved diagnostic.

## Dependencies, verification and limits

The exact NPZ and exact hex JSON are retained inputs. Source snapshots and their original paths/hashes will identify the Trial and TrialGreen versions inspected. No numerical-lane module is imported or executed. One check uses Fraction.from_float on NPZ values and direct sums with Arb512; the other parses hexadecimal strings with integers, uses a separately derived full-angle Fourier coefficient construction, reversed exact sums and iv220. Each checks the clamped endpoints, shapes, joins, moments, interval endpoints and exact comparisons. Complete actual Claude Opus5.5 review, follow-up if needed and a later independent adjudication precede any FINAL verdict.

No claim is made that the exactly normalized and exactly joined canonical trial fails this scaling identity. This result neither supplies a physical global residual bound for the stored discontinuous representation nor transfers its floating X-norm or quotient to that canonical trial. It provides an interface-aware interpretation and, if zero is excluded in(1), a counterexample to the unqualified zero-strain assertion for the ordinary stored K_pw. It does not prove an exact kernel, a new inverse obstruction, nonlinear closure, nonexistence or any decisive PDE endpoint.
