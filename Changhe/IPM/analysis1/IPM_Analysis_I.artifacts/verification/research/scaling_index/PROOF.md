# Scaling, source functionals and conditional index bookkeeping

Date: 2026-10-20. Status: CONFIRMED for the conditional statements below after independent derivation and actual Claude Opus 5.5 review with two exchanges. The identities below have explicit regularity and graph-domain hypotheses. No global IPM Fredholm assertion is proved here.

## Setting and claims

Use the canonical full-plane inverse of PROMPT.md, with sigma[rho]=psi[rho]_{xy}(0), c_l[rho]=(1+sigma[rho])/3 and

F(rho)=(c_l[rho] X+U[rho]) dot grad(rho)-rho.

Densities have the required even-x, odd-y parity, sublinear growth and strong center factorization rho=x^2 y a with a continuous at zero. Suppose additionally that the canonical inverse, the indicated spatial derivatives and parameter derivatives exist in the spaces in which they are used. At a fixed background write V=c_l X+U[rho], epsilon=F(rho), Gamma h=U[h]+sigma[h] X/3 and

Lh=V dot grad(h)-h+Gamma h dot grad(rho).

The following statements are proved below.

1. For positive a, rho_a(X)=a rho(X/a) satisfies F(rho_a)(X)=a F(rho)(X/a), sigma[rho_a]=sigma[rho] and J(rho_a)=a^(-2)J(rho), where J(rho) is its center factor at zero. If this dilation curve is differentiable in the relevant graph spaces and its derivative is K=rho-X dot grad(rho), then LK=epsilon-X dot grad(epsilon), sigma[K]=0 and J(K)=-2J(rho). The trace identity for K requires this differentiability or an equivalent trace hypothesis.
2. At a positive-axis zero P=(x_*,0) of V, assuming local C^2 regularity of rho, C^1 regularity of h and C^1 regularity of their velocities, put mu=partial_y V_2(P), g=rho_y(P), g'=rho_xy(P). Then

   partial_y Lh(P)=(mu-1)h_y(P)+g partial_y Gamma[h]_2(P)+g' Gamma[h]_1(P).

   If extra derivatives are used below they are assumed to exist. At an exact profile with g nonzero, mu=1. For the subsequent scaling-mode source identity assume V is C^2 near P. In that case the scaling mode satisfies the required zero source functional.
3. If a closed, densely defined L has a Banach graph domain D, is Fredholm from D to a Banach forcing space Y, and J is a continuous nonzero functional on D, then restricting to D_0=ker J decreases the Fredholm index by exactly one. This is conditional on Fredholmness of the operator with its specified global domain. It proves neither its initial index nor Fredholmness along a homotopy.
4. A precise lower bound for an unnormalized two-norm contraction constant follows from K only if K belongs to the high and low domains and its image belongs to both forcing spaces. Its size cannot be declared greater than one without validated norms.

## Exact scaling and its differentiation

The stream function psi_a(X)=a^2 psi(X/a) obeys -Delta psi_a=partial_x rho_a. Its velocity is U_a(X)=a U(X/a). This velocity has the correct parity and is sublinear at infinity, so uniqueness of the canonical inverse identifies it with U[rho_a]. Its center velocity derivative and hence sigma are unchanged. Since grad(rho_a)(X)=grad(rho)(X/a), direct substitution into F proves the covariance. Direct substitution into rho=x^2 y a_factor proves J(rho_a)=a^(-2)J(rho).

The C^1 dilation-curve hypothesis is a substantive graph-norm assumption. Dilation need not even be norm-continuous on a general large Holder space, and mere membership of rho and X dot grad(rho) does not automatically replace this assumption. If the dilation curve is C^1 in a domain where F is differentiable, differentiating its covariance at a=1 gives LK=epsilon-X dot grad(epsilon). Continuity of sigma and J in that domain gives the two scalar identities. Alternatively suppose K=rho-X dot grad(rho) is itself admissible for the canonical inverse and U-X dot grad(U) has its required parity, sublinear growth and differentiability. The Poisson identity for psi_K=2psi-X dot grad(psi), followed by canonical uniqueness, identifies U[K]=U-X dot grad(U). Direct spatial differentiation then gives LK=epsilon-X dot grad(epsilon) without graph-norm differentiation. This alternative still needs sigma[K]=0 and the center trace of K to be established from their actual hypotheses, and K must belong to the operator domain before this becomes an operator identity.

Bare continuous center factorization does not automatically put K in the same trace space. For example, let chi be a smooth radial cutoff equal to one near zero and consider the kinematic density

rho=x^2 y [1+chi(r) r^(1/10) sin(r^(-1/5))]

near zero, with its smooth sublinear continuation outside a small disc. The oscillatory correction is C^{2,alpha} for some positive alpha, but its factor is merely continuous. To check this, each derivative of order j<=3 is bounded by C r^(3+1/10-j(1+1/5)); the bounds for j=2 and j=3 are C r^(7/10) and C r^(-1/2). Splitting a pair of points at distance comparable with their smaller radius and using the derivative bound in the close case proves a positive Holder modulus for the second derivative (for example alpha=1/4). Its factor under K includes -r partial_r[r^(1/10)sin(r^(-1/5))], whose cosine term is of size r^(-1/10). Hence K/(x^2 y) has no continuous center trace. This is an ambient regularity counterexample, not an exact IPM solution or an exclusion. The hypotheses of an exact profile might give additional structure, but that would require proof.

The prompt's P_infty condition only strengthens the center factor near zero. It does not by itself assert C^{m+1,alpha} regularity at the positive-axis source. Therefore the phrase “in particular every P_infty solution” cannot justify K membership in a high source space without a separate global regularity hypothesis.

## The source functional

Parity gives rho_x(P)=h_x(P)=0, V_2(x,0)=Gamma[h]_2(x,0)=0 and partial_y V_1(P)=0. Evaluate the difference quotient in y at P. Since V_1(P+(0,y))=o(y), its product with h_x divided by y tends to zero. The V_2 h_y term divided by y tends to mu h_y(P), and h/y tends to h_y(P). The quotient of Gamma[h] dot grad(rho) tends to g partial_y Gamma[h]_2(P)+g' Gamma[h]_1(P), using rho_x(P+(0,y))/y tending to rho_xy(P). This proves the displayed functional with only C^1 regularity of h, including the g' term.

For an exact profile, compare the first y jets in V dot grad(rho)=rho at P. They are mu g and g, so mu=1 if g is nonzero. This comparison requires only C^1 first jets, not an illegitimate second differentiation of the equation.

For the scaling mode, differentiation of U[rho_a]=a U[rho](X/a) gives Gamma K=U-X dot grad(U), since sigma[K]=0. Write w(x)=V_1(x,0) and mu(x)=partial_y V_2(x,0). At x_*, U_1=-c_l x_* and U_{1x}=w'-c_l, hence

Gamma[K]_1(P)=-x_* w'(x_*).

Differentiating the second component in y gives partial_y Gamma[K]_2(P)=-x_* mu'(x_*). The exact axis equation is w g'=(1-mu)g. Divide it by x-x_* and take the limit as x tends to x_*. Since g' is continuous, w(x)/(x-x_*) tends to w'(x_*), and [1-mu(x)]/(x-x_*) tends to -mu'(x_*), this gives

w'(x_*)g'(x_*)+g(x_*)mu'(x_*)=0.

Incompressibility gives w'+mu=2c_l, so w'(x_*)=2c_l-1. Substitution into the source functional gives partial_y LK(P)=0, consistent with LK=0 for an exact solution. For a trial, epsilon and its derivatives appear instead; these exact-solution identities cannot simply be imposed on the trial.

## Center forcing trace

If h also has continuous factor h=x^2 y b, both its canonical velocity and the background canonical velocity are C^1 at zero, and Lh itself has a continuous x^2 y factor, then J(Lh)=0. This trace identity does not require differentiating a or b. Rescale X by lambda and divide the densities by lambda^3. Their continuous factors give uniform local convergence to J(rho)x^2 y and J(h)x^2 y. The velocities divided by lambda converge in C^1 locally to their linear terms. Integration by parts against compact test functions therefore gives the distributional cubic limit of Lh. For V this term is [2(1-2c_l)+(4c_l-1)-1]J(h)x^2 y=0. For Gamma h its linear matrix is diag(-2sigma[h]/3,4sigma[h]/3), so its action on J(rho)x^2 y is also zero. Since the assumed continuous factor of Lh identifies that cubic limit with J(Lh)x^2 y, its trace must be zero. The premise that Lh has this factor is essential for the named trace to exist.

## What a transport formula would need

Let T_V=V dot grad-1. Assume c_l>1/2 and mu=1 at P, so both source eigenvalues are positive. Suppose a specified domain Omega has a global backward flow, every point under consideration converges to P backwards, and the integral

R_V f(X)=integral_0^infinity exp(t) f(Phi_{-t}X) dt

and its required derivatives converge in the stated topology. A change of variables in this integral gives T_V R_V f=f. If q_V=lim_{t to infinity} exp(t)[Phi_{-t}X]_2 exists with the needed regularity, the flow semigroup identity gives q_V(Phi_s X)=exp(s)q_V(X), hence T_V q_V=0. If also the center traces exist and J(q_V) is nonzero, subtracting J(R_V f)q_V/J(q_V) imposes J=0 without changing the forcing.

These are conditional formulas. If q_V(X) is nonzero and the trajectory asymptotics and source differentiability justify the first-order limit, then exp(t) f(Phi_{-t}X) tends to f_y(P) q_V(X). Thus convergence already imposes f_y(P)=0; it is not a mild assumption or an independent proof of the global cokernel dimension. Further local and global decay must be proved. No blanket absence of eigenvalue resonances is assumed or asserted here. Local attraction backwards, mu=1, and a single source jet do not establish convergence globally, membership at the saddle origin, behavior on invariant axes or separatrices, nor the conditions at infinity. The one-dimensional kernel and cokernel of the linear source box theorem in ../source_transport/PROOF.md cannot be counted as global dimensions without these extra facts. The order-zero coupling is not automatically compact, as the earlier counterexample shows. No justified transport index or Fredholm homotopy is presently supplied by these formulas.

## Codimension-one Fredholm restriction

Use the graph domain D as the domain Banach space. A continuous nonzero J is surjective onto the scalars, so D_0 has codimension one and is closed. If J is nonzero on ker L, choose k in ker L with J(k)=1. For every u in D, u-J(u)k belongs to D_0 and has the same image. Thus L(D_0)=L(D), while the kernel dimension decreases by one. Its range remains closed and the index decreases by one.

If J vanishes on ker L, define ell on L(D) by ell(Lu)=J(u). This is well-defined. It is continuous: L induces a bounded bijection D/ker L to its closed range, with bounded inverse by the Banach inverse theorem, and J descends continuously to that quotient. It is nonzero because J is nonzero on D. Then L(D_0)=ker ell inside L(D), a closed codimension-one subspace. The kernel dimension is unchanged, the cokernel dimension increases by one, and the index again decreases by one. This also proves Fredholmness of the restriction.

If a norm-continuous family of Fredholm operators connects T_V to L on fixed Banach domain and forcing spaces, its index is constant. This standard local-stability assertion requires Fredholmness along the whole family; it is not a consequence of a model threshold, principal symbol, or sampled finite matrix. If the domain itself varies, a specified continuous identification is additionally needed. No such global homotopy is proved here.

## The unnormalized contraction lower bound

Define new, unnormalized spaces X^u,E^u, forcing spaces Y_H^u,Y_L^u and low domains D_h^u. Assume afresh all the operator hypotheses of ../two_norm_scheme/PROOF.md in these new spaces, with constants K_H,K_L,C_B,eta, including the continuous embedding Y_H^u into Y_L^u. No inverse estimate on a normalized domain is being extended by implication. In the displayed bounds below X,E,Y_H,Y_L abbreviate these new unnormalized spaces. Assume K is nonzero, belongs to X^u and D^u_{h=0}, and LK belongs to Y_H^u (hence Y_L^u). The notation D^u_{h=0} is the low operator domain at increment zero; it is not the kernel of the center functional from the preceding section. Then the high solution of Lu=LK equals K by low injectivity, so

K_H >= ||K||_X/||LK||_{Y_H},
K_L >= ||K||_E/||LK||_{Y_L}.

The bilinear estimate applied to (K,K) gives

C_B >= ||B(K,K)||_{Y_L}/(||K||_E ||K||_X).

If LK is nonzero, multiplying yields

K_L C_B K_H eta >= eta ||B(K,K)||_{Y_L}/(||LK||_{Y_H} ||LK||_{Y_L}).

If LK=0, low injectivity already fails for nonzero K. The identity LK=epsilon-X dot grad(epsilon) gives a possible numerical diagnostic. It supplies no validated numerical ratio without all three relevant norms and eta. Descriptions such as “residual size” and “size one” cannot replace the strict inequality needed to rule out contraction.

## Scope

This note confirms exact algebra subject to stated regularity, and conditional functional-analytic bookkeeping. The global Fredholm index, homotopy, K membership for every admissible profile, and a numerical lower bound exceeding one remain OPEN. It excludes neither a nearby P_2 solution nor a solution with smooth center factor.

## Review record

Actual model claude-opus-5-5 reviewed this note in scaling_source_index and scaling_source_index_followup (../../notes/reviews/). The follow-up accepted all five resolutions and withdrew its proposed blanket nonresonance requirement and its proposed replacement of graph-norm differentiability by mere membership. Its optional convergence discussion does not replace this note's explicit integral-convergence hypothesis: C^1 and f_y(P)=0 alone need not give an integrable modulus. The stronger hypotheses written above are retained.
