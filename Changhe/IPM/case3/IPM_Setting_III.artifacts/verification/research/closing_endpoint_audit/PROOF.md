# Principal endpoint audit

Written 2026-10-22, shift9, and revised 2026-10-22T07:41:29.894781+00:00, before the final endpoint decision. This is a standalone proof of the structural safeguards used in that decision and an explanation of the evidence gate. It is not a proof of existence or nonexistence. The actual run end and final numerical record will be recorded separately.

## Statement and hypotheses

Let ell>1 and let rho be smooth on R^2, even in x and odd in y, with a=rho_y(0) nonzero and

    |rho(X)|+(1+|X|)|grad rho(X)| <= C(1+|X|)^gamma,  0<gamma<1.

Let U be the velocity with div U=0, curl U=-rho_x, the induced parities, and U=o(|X|). Assume, only for the exact-profile statements below,

    (ell X+U).grad rho=rho.

Write W=ell X+U, U=(-psi_y,psi_x), c=psi_xy(0), and p=1/ell. Then the canonical inverse is unique, c=1-ell, DW(0)=diag(2ell-1,1), the y-axis has no positive equilibrium of W, and rho(0,y)/y^p tends to a nonzero limit K of the sign of a. The residual spatial dilation preserves ell and a and gives an attainable reporting length L=(K/a)^(1/(1-p)) for every exact primary profile. None of these statements asserts that a profile exists.

## Canonical inverse and its gauge

For Z nonzero put

    K1(Z)=-z1*z2/(pi |Z|^4),
    K2(Z)=(z1^2-z2^2)/(2pi |Z|^4).

The canonical velocity is -rho(X)e2/2 plus the principal-value convolution K*rho, with the outer limit taken over disks centered at zero. At the singular point subtract rho(X). The angular mean of K vanishes, and smoothness gives local absolute integrability of K(X-Y)(rho(Y)-rho(X)). At infinity use central oddness of rho and evenness of K: on each centered annulus the integral of K(-Y)rho(Y) is zero. For |Y|>2|X|,

    |K(X-Y)-K(-Y)| <= C |X| |Y|^-3.

The remaining radial tail is bounded by C|X| integral_(2|X|)^infinity s^(gamma-2) ds. This is finite. Splitting at |X-Y|=|X|/2 and |Y|=2|X|, with the given gradient bound in the first region, proves U=O((1+|X|)^gamma). The unsubtracted exterior integral is not asserted to be absolutely convergent.

The distributional Hessian of -(2pi)^-1 log|Z| gives the contact term -rho e2/2 and the displayed K. Since -Delta[-(2pi)^-1 log|Z|]=delta_0, differentiation yields div U=0 and curl U=-rho_x. Localizing rho to a compact set near each query and differentiating the smooth exterior kernel proves local smoothness. Reflections give the velocity parities. The stream function exists globally because R^2 is simply connected; its additive constant is fixed by oddness in both variables.

Competing velocities are required to solve the same div-curl equations distributionally. Their difference is distributionally harmonic, hence smooth and harmonic, with sublinear growth. The Poisson disk formula bounds its derivative at any fixed point by C R^-1 times its supremum in a disk of radius R. Sublinear growth makes this tend to zero. The difference is therefore constant, and the two odd component parities make it zero. A term kappa xy in psi adds kappa(-x,y) to U and violates U=o(|X|) unless kappa=0.

## Origin relations and strain cancellation

Symmetry gives U(0)=0 and DU(0)=diag(-c,c). Differentiating exact transport in y at zero gives (ell+c)a=a. Since a is nonzero, c=1-ell. Thus the origin is a source with eigenvalues 2ell-1 and 1; the old x^2 y branch normalization is inapplicable.

For completeness write rho=sum_(k odd) b_k(r) sin(k theta). The sine-2 coefficient of rho_x is

    f2=(b1'-b1/r+b3'+3b3/r)/2.

The canonical radial Green formula for the sine-2 stream coefficient h2 is

    h2(r)=[r^-2 integral_0^r s^3 f2(s) ds
           +r^2 integral_r^infinity s^-1 f2(s) ds]/4.

The smooth canonical stream has this sine-2 coefficient: the possible r^-2 homogeneous term is excluded at the origin, and the r^2 term would add a nonzero xy strain, excluded by the sublinear velocity gauge. Because xy=(r^2/2)sin(2theta), this gives c=(1/2) integral_0^infinity f2(s)/s ds. Here b1/r tends to a at zero and to zero at infinity, while b3/r tends to zero at both ends. Integration by parts therefore gives

    c=-a/4+integral_0^infinity b3(s)/s^2 ds.

The last integral is absolutely convergent: b3=O(s^3) at zero and O(s^gamma) at infinity. An unintegrated two-dimensional strain integrand proportional to rho sin(3theta)/r^3 need not be absolutely integrable at zero, and omitting the -a/4 term is incorrect.

If rho=a y+b x^2 y+e y^3+O(r^5) and psi=cxy+q1 x^3 y+q2 xy^3+O(r^6), set A=2ell-1. Poisson and cubic transport give

    q1+q2=-b/3,  q1=-2Ab/(3a),  q2=-2e/a,
    e=(a-2A)b/6.

These are necessary exact identities. Their finite numerical defects must be evaluated independently rather than made tautological in both a generator and its checker.

## Global axis and remaining spatial scale

On the y-axis write G(y)=rho(0,y), v(y)=ell y+U2(0,y). Symmetry makes that axis invariant. Exact transport is vG'=G, with v(y)=y+O(y^3) and G(y)=a y+O(y^3). If v had a first positive zero y*, then on [epsilon,y*)

    G(y)=G(epsilon) exp(integral_epsilon^y 1/v(s) ds).

Consequently |G(y)|>=|G(epsilon)|>0. Continuity gives G(y*) nonzero, whereas v(y*)G'(y*)=G(y*) gives G(y*)=0. This contradiction proves v>0. The same formula shows G/a>0 and G'/a>0 on the whole positive axis. No sign off the axis is assumed.

The inverse bound gives v(y)=ell y+O(y^gamma), hence 1/v-p/y=O(y^(gamma-2)). Its integral converges at infinity, so G/y^p tends to K nonzero of the sign of a, with relative error O(y^(gamma-1)). The growth bound implies p<=gamma, equivalently ell>=1/gamma for the particular exponent in the hypothesis. The primary class quantifies over some gamma in(0,1).

The transformation rho_lambda(X)=lambda rho(X/lambda), U_lambda(X)=lambda U(X/lambda), psi_lambda(X)=lambda^2 psi(X/lambda) preserves the exact equations, canonical inverse, parities and class. Chain rules give

    D^m rho_lambda=lambda^(1-m)(D^m rho)(X/lambda),
    D^m U_lambda=lambda^(1-m)(D^m U)(X/lambda),
    D^m psi_lambda=lambda^(2-m)(D^m psi)(X/lambda).

The class allows its constant C to change under dilation. In fact C max(1,lambda) is a sufficient new constant for the displayed joint density-gradient bound. To see this let r=|X|, q=(1+r/lambda)/(1+r), and regard |rho(X/lambda)| and (1+r/lambda)|grad rho(X/lambda)| as the two nonnegative summands of the old bound. After division by (1+r)^gamma their multipliers are lambda q^gamma and q^(gamma-1). For lambda<=1 both are at most 1; for lambda>=1 both are at most lambda. This proves the stated sufficient bound.

Thus ell and a are invariant, K_lambda=lambda^(1-p)K, and L_lambda=lambda L for L=(K/a)^(1/(1-p)). Choosing lambda=1/L selects exactly one representative on each primary orbit. For trial densities with fixed ell, define

    R=(ell X+U).grad rho-rho,
    Nf=|(ell x+U1)rho_x|+|(ell y+U2)rho_y|+|rho|,
    Nv=|rho|+|x rho_x+y rho_y|+|U1 rho_x+U2 rho_y|.

These are the prompt's definitions, using the exact canonical U generated by the trial density. Each scalar term in these expressions scales by lambda at matched spatial points, so their pointwise ratios are invariant wherever defined. Fixed physical sample sets are not automatically matched under this transformation. Neither arbitrary a=1 nor arbitrary ell is a legitimate consequence of this symmetry. The argument does not classify arbitrary nonlinear transformations of the set of solutions.

## Meaning of the final endpoint gate

An exact primary profile would yield physical density alpha tau^alpha rho(Z/tau^beta), with alpha=1/(ell-1), beta=ell/(ell-1), tau=T-t. Its central vertical derivative is alpha a/tau. This conditional consequence concerns the stated sublinear class, which permits unbounded density at infinity; it does not establish blowup from bounded or compactly supported data.

A rigorous NO must exclude every profile under exactly the hypotheses above. Restricted shape exclusions, obstructions at finitely many polynomial degrees, extra sign or dynamical assumptions, and failed solvers do not do that. A numerical YES must satisfy all eight numerical requirements in PROMPT.md, including a reconstructible genuinely nondegenerate smooth-class candidate, independent canonical full-plane evaluation, origin and far-field checks, both pointwise residual normalizations, and convincing independent refinement. A tiny training-grid loss alone does not satisfy them. Finite arithmetic identities on stored floating-point operands are exact statements about those operands, not enclosures of an inverse integral or a nearby solution.

For the following auxiliary formulas assume g is locally C2, and for every compact horizontal interval I the vertical tails of sup_(x in I)(|g_x(x,t)|+|g_xx(x,t)|) are integrable. This permits the differentiations under the integral. The finite smooth trial representations in the cited hydrostatic audits are checked separately for these tails. Define Phi=integral_0^y t g_x(x,t)dt+y integral_y^infinity g_x(x,t)dt. Then Phi_y=integral_y^infinity g_x, Phi_yy=-g_x and Phi_x=V2. Thus the hydrostatic inverse V1=-integral_y^infinity g_x(x,t)dt and V2=integral_0^y t g_xx(x,t)dt+y integral_y^infinity g_xx(x,t)dt solves a vertical Poisson problem. It replaces -Delta psi=rho_x by an equation with only vertical second derivatives. Its residuals, center obstructions and smooth trial densities therefore do not supply a primary IPM candidate. Their use as large-slope diagnostics requires separate hypotheses for passage to that singular limit.

At each final observation the verifier must inspect the current saved evidence, state which endpoint conditions remain unfulfilled, and report UNRESOLVED if neither decisive endpoint has been established. This is a verdict on this run's evidence, not a proof that existence or nonexistence is unknowable. A final timestamp must be an actual observation, not the future scheduled deadline.

## Dependencies and verification scope

The derivations above were independently rechecked in shift 9 against the frozen prompt and the earlier independent proofs in inverse/, origin/, scaling/ and physical_scaling/. They require no candidate computation. Prior larger analytic results remain attached to their individual complete proof and verification records; this short closing proof does not replace or silently enlarge those audits. The final result file will record report hashes, outstanding numerical gates, actual returned model identifiers, and the real end time.
