# Flat-point exclusion with a full-disk critical ratio

## 1. Statement and hypotheses

Fix 0<c<1/2 and any finite real omega. Let Jx=e3 cross x, A=cI-omega J, X=Ax, a=1-2c, b=2-2c, eta=a/b, gamma=1-2eta=c/(1-c), and m=1/c. Thus eta is in (0,1/2), gamma is in (0,1) and m>2. On a smooth X-flowbox G about x0!=0, suppose V and S are smooth and satisfy

    div V=0, DV X=-((1-c)I+omega J)V,
    X.grad S=-bS, X.V=0, (curl V).grad S=0.             (1)

Write the coordinates as x=Psi(t,z)=exp(tA)n(z), with z in a full transverse disk D and Psi(0,0)=x0. Assume there is R0 in Wloc^(1,2)(D) with constants 0<r_-<=r_+<infinity such that, almost everywhere on the full disk,

    r_-<=R0<=r_+, |V(n(z))|^2=R0(z)|S(n(z))|.          (2)

Assume V has infinite value vanishing order at x0: for each positive integer N there are C_N and a neighborhood on which |V(x)|<=C_N|x-x0|^N. Then V=S=0 near x0.

The zero set of S may be arbitrary and S may change sign. No Poisson or angular symmetry assumption is needed. Equation (1) already imposes important additional constraints; in particular its contraction identity will imply V.curl V=0. The assertion is not a theorem for arbitrary Euler tails. The full-disk extension in (2) is an explicit extra hypothesis.

By continuity, (2) implies r_-|S|<=|V|^2<=r_+|S| pointwise on the section. Both quantities scale as exp(-bt), so this comparison holds throughout a smaller flowbox. Their zero sets agree. The comparison also makes S value-flat at x0.

## 2. Removal for the normalized quotient

We first prove a separate local lemma. Let v,s be smooth on an open subset of R3 and suppose |v|^2<=M|s|. Define beta=|s|^(-eta)v off {s=0}, extended by zero. Put rho=1/2-eta=gamma/2. Then beta is continuous and belongs to Wloc^(1,t) for every 1<=t<1/(1-rho). If its classical curl vanishes off {s=0}, its distributional curl vanishes everywhere.

The external scalar input is Ghisi-Gobbino, arXiv:1107.2694v2, Theorem 2.3: for smooth real f and 0<theta<1, either continuous root |f|^theta or sign(f)|f|^theta is in Wloc^(1,t) for t<1/(1-theta). More generally its hypothesis is C^(k,alpha) regularity of f with k+alpha=1/theta, which smoothness supplies on compact sets. Its statement and slicing proof were checked in A1541; the source's final displayed estimate has an exponent typo already isolated there. No new proof of this external theorem is claimed here.

Apply the theorem to s with theta=rho and to each v_i with theta=gamma. Set

    h_s=|s|^(rho-1)|Ds|, h_i=|v_i|^(gamma-1)|Dv_i|

on the respective nonzero sets, with value zero on their zero sets. The chain rule off zeros and the Sobolev level-set property imply h_s in local L^t for t<1/(1-rho), and h_i in local L^t for t<1/(1-gamma). A smooth scalar derivative is zero almost everywhere on its zero set, so these conventions do not omit a derivative term.

For epsilon>0 use the smooth beta_e=(s^2+epsilon^2)^(-eta/2)v. On {s!=0,v!=0} the product rule and comparison give

    |D beta_e| <= |s|^(-eta)|Dv|+eta|s|^(-eta-1)|v||Ds|
                <= C sum_i h_i+C h_s.                    (3)

Indeed |s|^(-eta)<=M^eta|v|^(-2eta) and the component inequalities |v|^(-2eta)<=|v_i|^(-2eta) bound the first term almost everywhere. The second is at most eta sqrt(M)|s|^(rho-1)|Ds|. On {v=0}, Dv=0 almost everywhere. On {s=0}, v=0 and the other regularized term contains the factor sv. Thus (3) holds almost everywhere on the full domain, independently of epsilon. Its right side lies in each indicated L^t because rho<gamma.

The limit beta is continuous since |beta|<=sqrt(M)|s|^rho. Splitting |s|<=epsilon and |s|>epsilon proves a uniform error at most C epsilon^rho: in the second region use 1-(1+x)^(-eta/2)<=C x for x=(epsilon/|s|)^2. Weak compactness for 1<t<1/(1-rho), together with uniform convergence, identifies beta as a W1,t limit. Local finite measure supplies t=1. Its derivatives are classical off {s=0} and zero almost everywhere on that set by the Sobolev level-set property. This proves distributional removal of classical zero curl without a condition on the geometry of the zero set.

A further estimate is

    |beta|<=M^eta|v|^gamma.                               (4)

It follows from |s|>=|v|^2/M and includes zeros. Thus value flatness of v implies value flatness of beta. No derivative of |v|^2/|s| was estimated or asserted to exist in this lemma.

## 3. A potential before taking transverse coordinates

Set W=curl V and k=X.V. Direct differentiation, using DV X from (1), gives

    grad k=X cross W-aV.

Since k=0, X cross W=aV. Cross this equality on the left with grad S. The vector triple product and (1) yield

    grad S cross V=(b/a)S W=eta^(-1)S W.                 (5)

For S!=0, equation (5) gives curl(|S|^(-eta)V)=0, for either sign of S. Section 2 and the upper comparison extend this form by zero to a continuous distributionally closed beta on a full ball. Mollify in a slightly larger ball, integrate each smooth closed form radially from x0, and fix the value there. Uniform convergence of the forms gives locally uniform convergence of their potentials and gradients. Hence a C1 potential phi exists with Dphi=beta on the full ball.

Since beta.X=0 everywhere, X.phi=0. Shrinking the flowbox inside the ball gives phi(Psi(t,z))=u(z), with u in C1 on the full transverse disk. The inverse metric has a positive definite transverse principal block, so Du=0 if and only if beta=0, equivalently V=0 and S=0. Off this critical set, S!=0 and phi, hence u, is smooth. Equation (4) gives |Du(z)|<=C_N|z|^N for every N.

This construction has no period or boundary-integral assumption. It precedes the coordinate reduction and therefore does not discard an irregular zero interface.

## 4. The exact full-disk equation

The metric in these coordinates is exp(2ct)g(z). Put mu=sqrt(det g), B=(g^ij) for the two transverse indices and zeta=(g^ti). Here B is smooth positive definite. Let h(z)=|S(n(z))|. Homogeneity and a+2c=1 show that the contravariant components of V=|S|^eta grad phi have factor exp(-t), while the volume density has factor exp(3ct). Thus div V=0 gives

    partial_i(mu h^eta B^ij u_j)
       +(3c-1)mu h^eta zeta^j u_j=0.                    (6)

This is a full-disk weak identity. Its flux and lower term are smooth coordinate components of the original smooth V, so no cutoff around a zero set is necessary.

Off zeros, (2) is h R0=h^(2eta)|Du|_B^2. With tau=eta/gamma=(m-2)/2, this gives

    h^eta Du=R0^(-tau)|Du|_B^(m-2)Du                   (7)

almost everywhere. Both sides are zero on the critical set, so (7) is a full-disk identity. In smooth isothermal coordinates for B inverse, write B=lambda^(-2)I and transform mu as a density and zeta as a vector. Equation (6) becomes

    div(w |Du|^(m-2)Du)+w d.(|Du|^(m-2)Du)=0,
    w=mu lambda^(-m)R0^(-tau), d=(3c-1)lambda^2 zeta.   (8)

The smooth geometry and (2) give w in Wloc^(1,2), bounded above and away from zero on compact subdisks; d is smooth. Composition with r^(-tau) is a valid Sobolev chain rule since its derivative is bounded on [r_-,r_+]. Smooth coordinate changes preserve these properties and all value-flat estimates. Existence of smooth local isothermal coordinates is an explicit classical geometric input.

## 5. Nonlinear-gradient energy through an arbitrary critical set

We prove the needed planar lemma under the weaker geometric requirement that d be locally Lipschitz. Let u be C1, smooth on {Du!=0}, and solve (8) weakly, with positive bounded w in Wloc^(1,2). Write v=Du, T(v)=|v|^(m-2)v and B_m(v)=|v|^((m-2)/2)v. The power-map inequalities give

    delta T.delta v >= c_m sigma^(m-2)|delta v|^2,
    |delta T|<=C_m sigma^(m-2)|delta v|,
    |delta B_m|^2<=C_m sigma^(m-2)|delta v|^2,

where sigma=|v(x+h)|+|v(x)|. Subtract the equation and its translate and test with chi^2 delta u on a compact smaller disk. The test is admissible by C1 approximation. Put E_h=integral chi^2 sigma^(m-2)|delta v|^2. Local boundedness of v gives |delta u|<=C|h|, and Sobolev translation estimates give

    ||delta w||_2+||delta(wd)||_2<=C|h|.

The main term is at least c E_h. The cutoff and principal coefficient errors are bounded by C|h|E_h^(1/2) and C||delta w||_2 E_h^(1/2); for the latter use |T(v)|/sigma^((m-2)/2)<=sigma^(m/2), with zero assigned if sigma=0. The coefficient-cutoff error is C|h| ||delta w||_1. The drift splits into a delta T term bounded by C|h|E_h^(1/2) and a delta(wd) term bounded by C|h| ||delta(wd)||_1. Young's inequality therefore gives E_h<=C|h|^2. The last power-map estimate and the difference-quotient criterion prove B_m(Du) in Wloc^(1,2).

This step uses the full weak equation and bounded Du. It requires no measure, topology or boundary regularity of {Du=0}.

## 6. The first-order inequality includes the critical set

Define F=|Du|^((m-2)/2)(u_x-i u_y). It is continuous, locally bounded and Wloc^(1,2) by Section 5. Let beta0=grad log w+d in local L2. On {Du!=0}, division of (8) by w is legitimate almost everywhere. Rotate coordinates so Du=(r,0) and write h_ij for the Hessian. Then

    (m-1)h11+h22=-r(beta0)_1,
    F_z=r^((m-2)/2)[(m/2)h11-h22-i(m/2+1)h12]/2,
    F_barz=r^((m-2)/2)[(m/2)h11+h22+i(m/2-1)h12]/2.

Eliminating h22 gives the absolute real and imaginary principal ratios (m-2)/(3m-2) and (m-2)/(m+2). The remaining terms are bounded by C_m|beta0||F|. Thus

    |F_barz|<=kappa|F_z|+b0|F|,
    kappa=(m-2)/(m+2)<1, b0=C_m|beta0| in local L2.     (9)

These inequalities are invariant under the chosen oriented rotation. On the critical set F=0, and DF=0 almost everywhere there by the W1,2 level-set property. Consequently (9) holds almost everywhere on the full disk, including a critical set of positive measure. Equation (4) makes F infinitely value-flat at the center.

## 7. The critical scalar similarity argument

We repeat the precise endpoint mechanism, already confirmed in A1446-A1448. Split (9) measurably as F_barz=mu0 F_z+nu F with |mu0|<=kappa and |nu|<=b0. If D=kappa|F_z|+b0|F|, take

    mu0=kappa F_barz conjugate(F_z)/(D|F_z|),
    nu=b0 F_barz conjugate(F)/(D|F|),

and set an undefined coefficient to zero. Multiplication back proves the equality in every zero case as well.

Extend mu0 by zero from a smaller disk and apply the measurable Beltrami theorem to obtain a quasiconformal chi with chi_barz=mu0 chi_z. Its area formula, local Holder continuity for chi and its inverse, and Sobolev composition rule are explicit external inputs. Let f=F composed with chi inverse. It is continuous, bounded and Wloc^(1,2): smooth approximations of F converge uniformly and in W1,2, and the distortion-area inequality controls the energies of the compositions. The complex chain rule gives

    f_barzeta=B0 f,
    B0(chi(z))=nu(z)/[conjugate(chi_z(z))(1-|mu0(z)|^2)].

Changing variables gives the exact critical identity on corresponding domains

    integral |B0|^2 d zeta=integral |nu|^2/(1-|mu0|^2) dz
                         <=(1-kappa^2)^(-1)integral |nu|^2. (10)

Take a round disk about chi(0) inside the image, extend B0 by zero from it and let psi be its Cauchy transform. The local L2 Cauchy derivative estimate gives psi in W1,2 and psi_barzeta=B0. Baratchart-Borichev-Chaabi, arXiv:1309.3079v2, Lemma 8.3 and Proposition 8.4, printed pages 33-34, provide exp(|psi|) in every finite L^r and the weak exponential product rule in W1,t for all t<2. Their complete proofs were checked for A1447. They follow by two-dimensional exponential integrability and Sobolev approximation; no bounded multiplier is being assumed.

It follows that H=f exp(-psi) is W1,t and H_barzeta=0 distributionally. Weyl's lemma makes H holomorphic. The inverse Holder bound for chi transfers infinite value flatness to f. Since exp(-psi) is L2, for every N

    integral_(B_r(chi(0))) |H|^2
       <=C_N r^(2N) integral exp(-2 Re psi).              (11)

The last integral is finite on the fixed disk. If H were nonzero with leading Taylor order j, its squared integral would be at least C r^(2j+2). Choosing N>j+1 contradicts (11). Hence H=f=F=0 near the center. Continuity upgrades almost-everywhere vanishing of f and F to pointwise vanishing. Thus Du=0 near zero.

## 8. Conclusion and the remaining extra condition

From the full-disk relation V=|S|^eta grad phi, Du=0 gives V=0 on a smaller flowbox. The lower bound in (2) then gives S=0. This proves Section 1 for arbitrary finite omega and arbitrary scalar zero sets.

The new removal statement applies to the normalized form beta, not to the ratio R0. A bounded ratio on a zero-deleted domain, or a finite formal integral of its classical gradient over that domain, need not provide the full-disk W1,2 extension required here when the deleted set is arbitrary. This theorem retains that extension as a hypothesis. It does not derive k=0, a ratio bound, ratio energy or flatness for a general profile.

## 9. Audit record

All eight submitted source sections and all nine sections of this reconstruction were read. The scalar root and earlier critical-ratio dependency proofs were reread at the required steps. The quotient domination, zero-set removal, full-disk flux, nonlinear-gradient estimate, critical-set extension and critical similarity application are CONFIRMED. The external root, isothermal, quasiconformal, Cauchy and exponential facts are named at their uses. There is no unverified numerical or formal step.

The submitting literature agent is a second model the external referee (a second model). Findings are exchanged through the existing team files with configured model agents; their actual provider runtime is not independently attested. No additional model client or agent was invoked. The campaign's unrestricted bare-decay conjecture remains OPEN.
