# A transverse-pressure term missing from an asserted axis reduction

Status: CONFIRMED independent axis-limit calculation and exact counterexample, with 37 exact controls and two written actual Claude Opus5.5 reviews. The proof was written before the controls and refined after independent source and model checks. The claim concerns a particular published preprint equation, not existence or nonexistence in B2.

## 1. Source and precise statement

Source: Yaoming Shi, "2D Inviscid Boussinesq Equations and 3D Axisymmetric Euler Equations: (1) A Unification (Em), (2) Finite-Time Blow-Up of Two Unified (1+1)D Systems Rigorously Derived from (Em)", arXiv2603.26715v5, PDF datedJuly12,2026. The downloaded versioned PDF and extracted text are in verification/literature_20261021T0957Z, with retrieval metadata and SHA256. Here equation numbers refer exclusively to that version.

Write r,z for the paper's Cartesian meridian coordinates, rho=(r²+z²)^(1/2),theta=atan2(z,r). Use m in{1,2}, positive lambda,mu, and even smooth fields u,v,g,p,psi. Its full system(2.10), away from the axes with the smooth quotient extensions at them, is

    D u=(m²/2)uv,
    D v=v²-u²+p_r/r,
    D g=-g²-mu p_z/z,
    z g_z-r v_r+g-mv=0,
    v=psi+z psi_z, g=m psi+r psi_r,
    D=lambda partial_t-vr partial_r+gz partial_z.          (1)

Theorem2.11 asserts that evenness, hence first angular derivatives zero on both axes, implies on the horizontal axis

    lambda G_t=-G²+rho V G_rho-mu P_rho/rho,               (2)

which is its equation(2.28), and the closed apex identity

    lambda v_t=(mu-m²)/(mu+m) v²-mu/(mu+m)u² at0.          (3)

Claim: (2) and(3) do not follow from(1) and the stated evenness. A missing term in(2) is -mu P_thetatheta/rho² at theta0. A smooth even exact solution of(1) violates(3). This is a direct counterexample to the asserted general implication, irrespective of any later conditional background theorem.

## 2. The axis limit

For any smooth Cartesian pressure p(r,z), polar differentiation gives

    p_z/z=P_rho/rho+cot(theta)P_theta/rho².                (4)

For rho>0 fixed, evenness in z gives P_theta(rho,0)=0, but Taylor's theorem gives

    lim_(theta->0) cot(theta)P_theta(rho,theta)
                              =P_thetatheta(rho,0),
    P_thetatheta(rho,0)=rho² p_zz(rho,0)-rho p_r(rho,0).   (5)

It follows that the correct horizontal axis equation is

    lambda G_t=-G²+rho V G_rho
                     -mu[P_rho/rho+P_thetatheta/rho²].    (6)

The transverse convection vanishes because g z partial_z has a factor z and the fields are smooth. Its absence does not remove the pressure quotient, which has the finite generally nonzero extension p_zz. The paper's polar equation(2.14) explicitly contains -mu cot(theta)P_theta/rho². Setting P_theta=0 before taking the singular coefficient's limit is invalid.

As rho->0 along the horizontal axis, the missing term tends to -mu[p_zz(0)-p_rr(0)]. Evenness does not constrain these two second derivatives to be equal. Thus the apex does not fix this omission. More explicitly put Q=p_zz(0)-p_rr(0). At the apex the divergence relation gives g=mv and g_t=mv_t. Multiplying the v equation bymu and adding the g equation gives the correct identity

    lambda(mu+m)v_t=(mu-m²)v²-mu u²-mu Q.               (6a)

This is a direct identity of(1), with the pressure anisotropy Q still present. Formula(3) would require Q=0, an extra condition not supplied by parity.

## 3. An exact family refuting the closed apex formula

Let A(t) be any smooth real function and set throughout the whole(r,z)plane

    u=0, v=A(t), g=mA(t), psi=A(t),
    p=[lambda A'(t)-A(t)²]r²/2
                 -[lambda m A'(t)+m²A(t)²]z²/(2mu).      (7)

All five fields are smooth and even separately in r,z. The quotients p_r/r and p_z/z extend smoothly, being their displayed constant coefficients. The two stream relations hold since psi has no spatial derivatives, and the divergence relation is g-mv=0. The u equation is0=0. The v equation reads

    lambda A'=A²+(lambda A'-A²),

and the g equation reads

    lambda m A'=-m²A²+lambda m A'+m²A².

Hence every equation in(1) holds exactly, globally, for every A. Its polar first derivatives vanish at theta=0,pi/2,pi,-pi/2, satisfying the ridge-flat condition(2.15). No limiting or approximate solution is used.

Take A(t)=1 and mu!=m². Formula(3) then predicts0=(mu-m²)/(mu+m), false. For example m1,mu5/3 gives right side1/4; m2,mu16 gives2/3. These choices ofmu match the paper's(2.22) for its distinguished q=m+1. Lambda is irrelevant to this steady counterexample. Even when mu=m², choose A=1+t: (3) would force lambda=0 at each time, contradictinglambda>0. Thus the omission is not cured by choosingmu=m².

For constantA, the omitted quantity in(5) is

    P_thetatheta/rho²=A²(1-m²/mu).

It exactly supplies the discrepancy in(2). For generalA it is

    -(lambda m A'+m²A²)/mu-(lambda A'-A²),

again the difference p_zz-p_rr. This exhibits the missing degree of freedom explicitly.

These fields have linear physical velocity and quadratic pressure; they are not being offered as finite-energy or sublinear B2 fields. Theorem2.11 states an exact restriction of(2.10) from parity and does not impose a decaying pressure gauge that would rule out(7). Even a separately imposed decay class would not validate dropping the term in(4); such a class would require an additional proved identity p_zz=p_r/r on the whole axis.

## 4. What the source does and does not establish for B2

There is an independent scope obstruction even before this algebraic issue. Conjecture4.5 asks for a compatible full background; Theorem9.2 assumes such a background, its coefficient bounds and a weighted elliptic estimate. Theorem9.4 further assumes a gap exponent sigma in(C_lin,1) and full-interval remainder control. These are explicitly conditional, so they do not supply an unconditional full-plane profile. Theorem4.2 is itself stated for solutions of the reduced system(2.19); its Riccati apex formula follows from that reduced equation while such a smooth solution exists. The counterexample refutes the claimed derivation of the reduced equation from(Em), not that elementary reduced-equation implication or the conditional theorems as logical implications. For data(4.1), reduced-system Lemma4.1 gives u_c=0 and v_c=A/[1-At/(2(m+2))] on the lifespan of a smooth reduced solution. If its maximal smooth lifespan is T_*, this forces T_*<=2(m+2)/A. The formula alone does not prove absence of an earlier off-apex breakdown or T_*=2(m+2)/A. Thus the assertion of blow-up at exactly that time needs an additional continuation argument even in the reduced system. We do not adopt the first review's broader statement that the reduced ODE calculation itself is invalid.

Theorem5.2 constructs the branch U=0 for its reduced system(R0), with c1=33/14 and c2=8/5. In its Boussinesq variables(2.3), the buoyancy is r u². Thus the reduced U=0 branch has zero buoyancy on its horizontal axis. It specifies no off-axis buoyancy, and zero axis data alone do not exclude a nonzero transverse quadratic jet. It supplies no full-plane B2 profile; the separate parity argument below excludes the required quadratic jet for a full extension retaining the stated apex symmetries. Even accepting a reduced-system profile as proved would not repair its extension or the missing pressure term.

The Boussinesq ansatz in section2.1 has buoyancy odd in the force coordinate r and even in the transverse coordinate z, with both velocity reflections imposed. At the apex it cannot have the nonzero B2 quadratic transverse-temperature jet: after identifying the B2 transverse coordinate with z and its force coordinate withr, oddness inr forces the coefficient ofz² at(r,z)0 to vanish. This is about the paper's apex construction, not all possible translations or profiles of the original equations. No claim of equivalence between the two symmetry settings is made.

## 5. Other retrieved source scopes

The version3 of arXiv2201.06780, Y.Wang,C.-Y.Lai,J.Gomez-Serrano,T.Buckmaster, "Asymptotic self-similar blow-up profile for three-dimensional axisymmetric Euler equations using neural networks", May2023, explicitly imposes the half-plane x2>=0 and U2(x1,0)=0. Its vorticity uses curlU, opposite the task'sOmega convention; its length exponent is1+lambda. Its reported neural-network residuals andlambda1.917+-0.002 concern that wall setting. They are numerical evidence, not a certified full-plane B2 solution. No numerical method or source code from it was run here.

JiajieChen, arXiv2309.00150v2, "Remarks on the smoothness of the C^{1,alpha} asymptotically self-similar singularity in the 3D Euler and2D Boussinesq equations", September2023, Theorem2, concerns the half-plane with no-flow boundary, initial vorticityC_c^alpha and temperatureC_c^{1,alpha}, smooth only away from the distinguished point, and asymptotic self-similar singularity. Neither its domain nor its claimed regularity at that point is the target smooth full-plane B2 profile. It mentions a talk concerning boundary-free low-regularity progress; no theorem about B2 is supplied by that mention.

## 6. Dependencies, verdict and limits

The counterexample and axis-limit argument use only differentiation, Taylor's theorem and direct substitution into the exact printed equations. No PDE existence theorem or external inverse is assumed. The source-scope conclusions rely on the stated theorem hypotheses at the identified version. A full audit of every later reduced-system proof, every conditional estimate, or the two2023 papers is not claimed. Refuting the asserted axis closure does not refute B2 existence or prove nonexistence. The team endpoint remains OPEN.

Written UTC 2026-10-21T10:03:52.636446+00:00.

Rendered-source correction UTC 2026-10-21T10:05:52.377975+00:00: the PDF page10 equation(2.22) reads mu=m²(2q+m)/(2q-m²), not m²(2q+m²)/(2q-m²). Hence the distinguished m2 value is16, with predicted apex derivative2/3. The first exact control stopped on this transcription mismatch; no successful run was claimed. The counterexample for arbitrarymu was unaffected.

Scope refinement UTC 2026-10-21T10:07:53.866141+00:00: actualOpus235 agrees with the axis-limit/refutation and independently identifies the correctedmu16. Its valid zero-buoyancy objection is adopted: reducedU0 fixes only axis data. Its suggestion that Theorem4.2 itself has an invalid proof is not adopted; the theorem explicitly assumes the reduced system, and that conditional ODE deduction remains valid. A follow-up review has been requested on these distinctions with the previously omitted source sections.

Final audit UTC 2026-10-21T10:11:08.627759+00:00: returned_model claude-opus-5-5 confirmed for235 and236. The follow-up agrees with the corrected source scope and the exact Q identity; its lifespan refinement is adopted and independently verified from the printed Lemma4.1/Theorem4.2. No audit of the global reduced-profile construction or the conditional estimates is claimed.
