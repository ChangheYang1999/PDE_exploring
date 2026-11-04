# Residual errors and the scope of the Chen-Hou and Zhang sources

## Reading coverage and exact claim

The retained actual manuscripts are Chen and Hou, arXiv:2608.15174v1, all seven pages, and Zhang, arXiv:2306.09515v5, Proposition2.3, its proof and the immediately related remarks on pages20-26. The first file prints arXiv date15August2026 and internal date18August2026. The Zhang file prints arXiv date12October2023 and internal date5October2023. These are recorded as printed. The final 2025 Zhang journal text was not obtained or read in this audit.

This review proves the error decomposition below, checks its conditional power counting, and identifies a narrow sign error in one Chen-Hou footnote. It does not certify or refute the full computer-assisted blowup construction or Zhang's full dimension-reduction theorem. The sector implication itself has a [standalone proof](auditor_proofs/proofs/sector_maximum/PROOF.md).

## Exact nonlocal decomposition

Work on the upper half-plane with the stated homogeneous stream-function boundary condition. Let T(g)=grad_perp(-Delta)^(-1)g denote the chosen linear Biot-Savart operator. Suppose omega_bar, theta_bar and an approximate stream function phi_N have enough regularity for the following classical derivatives, and suppose phi_N obeys the boundary and growth normalization making T((-Delta)phi_N)=grad_perp phi_N. Define

    epsilon=omega_bar-(-Delta)phi_N,
    u_N=grad_perp phi_N,
    u_exact=T(omega_bar), u_error=T(epsilon).

Linearity then gives u_exact=u_N+u_error. This normalization premise matters: an arbitrary harmonic addition to phi_N cannot simply be ignored.

For fixed real constants c_l,c_omega,c_theta let

    F1=-(c_l x+u_exact).grad omega_bar
       +partial_x theta_bar+c_omega omega_bar,
    F_(i+1)=partial_i[-(c_l x+u_exact).grad theta_bar
                        +c_theta theta_bar], i=1,2.

Define F_j^loc by replacing u_exact with u_N. Subtraction and the product rule give exactly

    F1-F1^loc=-u_error.grad omega_bar,
    F_(i+1)-F_(i+1)^loc
       =-partial_i u_error.grad theta_bar
        -u_error.grad partial_i theta_bar.              (4)

Thus epsilon is a Poisson residual, not any of the displayed transport residuals. A numerical comparison of their raw point values is not an estimate of (4). Conversely, the algebraic distinction alone supplies no small bound for (4); it needs a verified operator estimate and derivative bounds.

For explicit conditional powers, suppose for r>=R0>=1 and some alpha<0 there are finite constants with

    |grad omega_bar|<=C r^(alpha-1),
    |grad theta_bar|<=C r^(2alpha),
    |D2 theta_bar|<=C r^(2alpha-1),
    |u_error|<=C r^(alpha+1), |D u_error|<=C r^alpha.

Multiplication in (4) proves |F1-F1^loc|<=C' r^(2alpha) and |F_(i+1)-F_(i+1)^loc|<=C' r^(3alpha). Chen-Hou report alpha in [-0.343,-0.342]. The exponents follow from these premises; the source's constants, global operator bounds, weighted estimates and full numerical certificate have not been independently reproduced here.

## The local scaling sign in Chen-Hou footnote2

On page2, equation(2.7) defines

    F1^loc=-(c_l x+u_N).grad omega_bar
             +partial_x theta_bar+c_omega omega_bar.

If omega_bar=r^alpha g(theta), then x.grad omega_bar=alpha omega_bar. Consequently the correct reduction is

    F1^loc=(c_omega-c_l alpha)omega_bar
              -u_N.grad omega_bar+partial_x theta_bar. (5)

The second sentence of footnote2 instead prints the coefficient c_l alpha-c_omega in this expression. It has the wrong sign relative to the defining equation. The PDF image, not only the text extraction, was inspected and shows the same sign. The immediately preceding equality for c_l x.grad omega_bar-c_omega omega_bar is correct; it is its substitution into F1^loc that misses a minus sign.

For a direct algebraic countertest set u_N=0, theta_bar=0, c_l=1 and c_omega=0 with any nonzero homogeneous omega_bar of degree alpha!=0 on an annulus. The definition gives -alpha omega_bar; the printed reduction gives +alpha omega_bar. This countertest concerns the substitution identity and need not solve the coupled profile PDE.

The absolute value of the near-canceling coefficient is unchanged by this correction. Equations(2.4), (2.7), the nonlocal decomposition(4), and the conditional power bounds are unaffected. No failure of a certified stability estimate follows from this isolated printed identity. It would also be unjustified to treat this limited review as certifying the complete blowup proof.

## Numerical sector plots and rounded zeros

Chen-Hou report maxima of grid vorticity values in200 angular sectors. Their figure exhibits a decreasing diagnostic and challenges a visual inference of angular increase made from a perspective plot. No grid data were recomputed in this audit. Neither finite sector maxima nor the perspective plot prove a continuum statement about r->sup W(r,theta), nor establish a hypothesis for an unknown exact limiting profile.

The source's distinction between an exact ODE zero and a rounded approximate value is also mathematically sound. For any epsilon!=0, f(t)=epsilon sin t is nonzero and has isolated zeros while satisfying f'+f=epsilon(cos t+sin t). The right side can be arbitrarily small. By contrast f'+f=0 with an exact zero forces f=0 by uniqueness. Dropping the forcing before applying exact uniqueness is invalid. A rounded grid value is not an exact zero of a function satisfying the homogeneous equation.

The clarification explicitly discusses stability around an approximate profile and does not establish an exact stationary self-similar profile nearby. Its report of certified bounds elsewhere is not an independent proof of those bounds in this audit.

## Campaign scope and evidence

Zhang Proposition2.3 uses upper-half-plane Boussinesq forcing, reflection and boundary conditions, globally bounded profile derivatives, specific quadrant velocity signs and an angular-maximum hypothesis. Its parameters imply alpha<-1 and c_l=1-alpha>2. The elementary exact sector exclusion is confirmed at those explicit hypotheses. Nothing in this review derives those hypotheses from decaying whole-space rotating Euler or supplies a target counterexample.

The actual manuscript files, extracted text, submitted literature scope note and a rendered page2 image are in verification. Hashes pin the reviewed bytes. All seven Chen-Hou pages and all of Zhang Proposition2.3 and its proof were read. The source interpretation and new sign correction have been shared through the existing configured-model/literature agent files, without contacting authors or making any online post. This is an independent mathematical and scope audit, not a statement that a model or journal has endorsed its conclusions.
