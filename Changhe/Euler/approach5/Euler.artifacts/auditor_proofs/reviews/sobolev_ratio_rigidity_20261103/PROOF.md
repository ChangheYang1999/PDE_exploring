# A critical transverse energy condition for a flat tail ratio

## 1. Statement, notation and scope

Let 0<c<1/2, omega be any finite real number, Jx=e3 cross x, A=cI-omega J, X(x)=Ax, a=1-2c, b=2-2c, eta=a/b and m=1/c>2. Fix x0!=0, a sufficiently small smooth flowbox G for X, and its central orbit segment Gamma. Let V and S be smooth and satisfy

    div V=0, X.grad V=-(1-c)V-omega JV,
    X.grad S=-bS, k=X.V=0,
    grad k=X cross curl V-aV, (curl V).grad S=0.      (1)

Assume S vanishes on Gamma, is strictly negative off Gamma and is infinitely flat at x0. The ratio R=|V|²/(-S) is smooth off Gamma and orbit invariant. In a smooth transverse disk through x0, assume its restriction has a Wloc^(1,2) extension to the whole disk and satisfies

    0<r_-<=R<=r_+<infinity almost everywhere.        (2)

Then these hypotheses are incompatible. A continuous extension of R is not assumed. In particular the result holds if R belongs to Wloc^(1,s) for any one s>2, or is Lipschitz. The proof is local and uses no pressure equation. Section10 extends the result to either fixed strict scalar sign and gives an equivalent punctured-disk condition in terms of the Dirichlet energy of log R.

## 2. The potential and its flat gradient

Put H=-S. From(1), X cross curl V=aV. Cross this equation on the left with grad S, use (curl V).grad S=0 and X.grad S=-bS, and obtain

    grad H cross V=eta^(-1)H curl V,
    curl(H^(-eta)V)=0, X.(H^(-eta)V)=0.           (3)

The norm of the one-form is sqrt(R)H^(1/2-eta), with 1/2-eta>0. On the transverse disk it tends to zero to every order. Its circulation around a circle therefore tends to zero. Closedness makes that period independent of the circle radius, so it is zero. The punctured flowbox has one fundamental circular period, hence a single-valued potential phi exists there and is constant along X.

Use Psi(t,y)=exp(tA)n(y), where n is a sphere chart transverse to X and n(0)=x0, and write phi(Psi(t,y))=u(y). Radial integration gives a limit u(0); circular arc integration identifies the limits from different directions. The extension is C1, smooth off zero, and for every N

    |u(y)-u(0)|+|Du(y)|<=C_N |y|^N.              (4)

Only the positive upper ratio bound and flatness were used here. The value assigned to R at the puncture never enters this construction.

## 3. Exact equation on the transverse disk

The pullback metric is exp(2ct)g(y), with

    g00=|An|², g0i=An.partial_i n,
    gij=partial_i n.partial_j n.

Let mu=sqrt(det g), B^ij=g^ij for transverse indices and z^j=g^0j. Then B is smooth positive definite. The scalar H equals exp(-bt)h(y), while the contravariant components of V=H^eta grad phi carry the factor exp(-(a+2c)t)=exp(-t). The volume factor is exp(3ct). Therefore div V=0 and the ratio identity are

    partial_i(mu h^eta B^ij u_j)+(3c-1)mu h^eta z^j u_j=0,
    R=h^(2eta-1)|Du|_B²,
    h^eta=R^(-tau)|Du|_B^(m-2), tau=(m-2)/2.     (5)

Use smooth isothermal coordinates for B inverse and write B=lambda^(-2)I there. Transform mu as a density and z as a vector. Equation(5) becomes

    div(w |Du|^(m-2)Du)+w d.(|Du|^(m-2)Du)=0,
    w=mu lambda^(-m)R^(-tau), d=(3c-1)lambda²z.  (6)

The Sobolev chain rule and(2) give w in Wloc^(1,2), bounded above and bounded away from zero. The geometric drift d is smooth. The equation holds weakly across zero: its flux and lower-order term in(5) are smooth geometric factors times components of the flat V, whose inner-circle flux tends to zero faster than any power. This proof of weak extension does not assume differentiability of the divided potential at higher order.

## 4. Difference quotients at the critical exponent

We now work on a compact smaller disk, with u in C1 and C2 away from zero, positive bounded w in W1,2 and Lipschitz d. Put v=Du, T(v)=|v|^(m-2)v and B0(v)=|v|^((m-2)/2)v. For a small translation h write delta u=u(x+h)-u(x), delta v=v(x+h)-v(x), and sigma=|v(x+h)|+|v(x)|. The power-map inequalities imply

    delta T.delta v>=c sigma^(m-2)|delta v|²,
    |delta T|<=C sigma^(m-2)|delta v|,
    |delta B0|²<=C sigma^(m-2)|delta v|².          (7)

Test the difference of(6) and its translate with chi² delta u, where chi is a compact cutoff. Let E_h=integral chi² sigma^(m-2)|delta v|². Since v is bounded, |delta u|<=C|h|. The W1,2 translation inequality gives

    ||delta w||2+||delta(wd)||2<=C|h|.           (8)

It follows first for smooth approximations by integrating derivatives along segments and applying Minkowski, and then by W1,2 convergence. The product wd is in W1,2 since d is Lipschitz and w is bounded.

The leading term is bounded below by c E_h. The cutoff error containing delta T is at most C|h|E_h^(1/2). The coefficient-gradient error is bounded by C||delta w||2 E_h^(1/2): use |T(v)|/sigma^((m-2)/2)<=sigma^(m/2) and bounded v. The coefficient-cutoff error is at most C|h| ||delta w||1. The drift difference splits into w_h d_h.delta T and delta(wd).T(v); after multiplication by chi² delta u these are bounded by C|h|E_h^(1/2) and C|h| ||delta(wd)||1. Thus

    E_h<=C|h|E_h^(1/2)+C|h|²<=E_h/2+C'|h|².

The last inequality is Young's inequality. From(7), the difference quotients of B0(Du) are bounded in L2. Their weak limits represent the distributional coordinate derivatives, so B0(Du) belongs to Wloc^(1,2). No pointwise bound on Dw, nor a derivative of the divided drift, is used.

## 5. The first-order equation

Set F=|Du|^((m-2)/2)(u_x-i u_y). It is continuous, bounded locally and Wloc^(1,2). Off zero divide(6) by w, giving

    div(|Du|^(m-2)Du)+beta.(|Du|^(m-2)Du)=0,
    beta=grad log w+d in Lloc^2.                 (9)

At points with Du!=0 rotate coordinates so Du=(r,0). If h_ij is the Hessian, then (m-1)h11+h22=-r beta1 almost everywhere. The exact derivatives are

    F_z=(r^((m-2)/2)/2)[(m/2)h11-h22-i(m/2+1)h12],
    F_barz=(r^((m-2)/2)/2)[(m/2)h11+h22+i(m/2-1)h12].

The real and imaginary homogeneous ratios are (m-2)/(3m-2) and (m-2)/(m+2). Hence

    |F_barz|<=kappa|F_z|+b0|F|,
    kappa=(m-2)/(m+2)<1, b0=C_m|beta| in Lloc^2. (10)

At a punctured zero of Du, the C1 map B0 has derivative zero, so DF=0 there. This covers every point except a null set. To split(10), put D=kappa|F_z|+b0|F| and, where the denominators are nonzero, set

    mu0=kappa F_barz conjugate(F_z)/(D|F_z|),
    nu=b0 F_barz conjugate(F)/(D|F|).

Use zero for each undefined factor. Then

    F_barz=mu0 F_z+nu F, |mu0|<=kappa, |nu|<=b0. (11)

All zero cases follow by multiplying the two coefficients back by F_z and F. Thus the split is valid measurably without a chosen phase at a zero.

## 6. Uniformization and the exact critical norm

Extend mu0 by zero from a smaller disk. The measurable Riemann mapping theorem gives a quasiconformal homeomorphism chi with chi_barz=mu0 chi_z and Jacobian Jchi=(1-|mu0|²)|chi_z|²>0 almost everywhere. We use the classical area formula, null-set preservation in both directions, local Holder bounds and Sobolev chain rule for this map and its inverse.

Let zeta=chi(z) and f(zeta)=F(z). The composition is continuous, bounded locally and Wloc^(1,2). One direct justification of its energy regularity is to approximate the continuous F both uniformly and in W1,2 by smooth functions on a slightly larger compact disk. The area formula and distortion bound |Dchi_inverse|_op²<=K Jchi_inverse give bounded W1,2 energies of the compositions; uniform convergence identifies the weak limit. The same estimate for differences gives convergence in the energy norm and the chain rule.

For F=f composed with chi, the complex chain rule gives

    F_barz-mu0 F_z
      =f_barzeta(chi(z)) conjugate(chi_z)(1-|mu0|²).

Thus f_barzeta=beta0 f with

    beta0(chi(z))=nu(z)/[conjugate(chi_z(z))(1-|mu0(z)|²)].

The area formula yields the exact identity

    integral_(chi(D0)) |beta0|²
       =integral_D0 |nu|²/(1-|mu0|²)
       <=(1-kappa²)^(-1)integral_D0 |nu|².        (12)

It is understood on corresponding smaller domains D0. Values on exceptional null sets can be assigned arbitrarily. No bound on the derivative of chi is needed. This is the critical two-dimensional cancellation on which the endpoint argument rests.

## 7. The critical multiplier and a holomorphic mass bound

Choose a round disk D' centered at zeta0=chi(0), compactly contained in the image domain. Extend beta0 from D' by zero and take a Cauchy transform psi. The L2 Cauchy and Beurling estimates give psi in W1,2(D') and psi_barzeta=beta0. The actual Baratchart-Borichev-Chaabi manuscript supplies, with proofs, the following precise facts on a bounded Lipschitz disk:

    exp(|psi|) belongs to every finite Lr;
    f exp(-psi) belongs to W1,t for every 1<=t<2,

with the weak product and chain rules. Their Lemma8.3 follows by extension to a compactly supported W1,2 function and the Trudinger-Moser inequality, using r|psi|<=epsilon|psi|²+C. Proposition8.4 proves continuity of the exponential product by smooth approximation, finite-power exponential integrability and Holder's inequality. Both complete proofs on printed pages33-34 were checked. Applying the proposition with f in W1,2 gives

    Holo=f exp(-psi), (Holo)_barzeta=0

weakly. Weyl's lemma makes Holo holomorphic. Neither psi nor exp(-psi) is asserted bounded or continuous.

The Holder bound for chi inverse and the flatness of F transfer flatness pointwise to f: for every N, |f(zeta)|<=C_N|zeta-zeta0|^N near zeta0. Since exp(-psi) belongs to L2(D'),

    integral_(B_r(zeta0)) |Holo|²
       <=C_N² r^(2N) integral_D' exp(-2 Re psi). (13)

If Holo were nonzero with leading Taylor order j, angular orthogonality of its convergent Taylor series would give a lower bound C r^(2j+2) for that same integral. Taking N>j+1 contradicts(13). Hence Holo, f and F vanish near the center. Almost-everywhere vanishing becomes pointwise because f and F are continuous. Then Du=0, contrary to(5), H>0 and R>0 on the punctured disk. This proves the critical theorem in Section1.

## 8. The separate supercritical argument in LIT237

If R belongs to W1,s for some s>2, then w does too and beta in(9) belongs to Ls. Sections4-5 remain valid. Alternatively to Sections6-7, extend mu0 and nu by zero and choose 2<delta<s sufficiently close to2 that kappa||Beurling||_delta<1. Solve (I-mu0 Beurling)g=nu in Ldelta by Neumann inversion. Its Cauchy transform psi is bounded and continuous. Then F exp(-psi) is W1,2 and solves the homogeneous Beltrami equation, so Stoilow factorization and the inverse Holder bound contradict any finite holomorphic zero order. This is exactly the first-order mechanism on Guo-Kar pages8-10.

The original nonlinear quantitative theorem's condition involving max(m,2) is not needed here: the nonlinear-gradient regularity was proved directly, and the first-order inversion uses only s>2. Thus both LIT237 and LIT238 are confirmed separately, with the critical theorem containing the supercritical one.

## 9. Source and functional caveats

The analytic source for the critical exponential rules is Laurent Baratchart, Alexander Borichev and Slah Chaabi, Pseudo-holomorphic functions at the critical exponent, arXiv:1309.3079v2. Its header is dated19 March2015 and its internal first-page date is18 June2018. Both are retained. The title page, pages8-9 including Lemma3.1 and its proof, and complete Lemma8.3 and Proposition8.4 on pages33-34 were read. No unrelated Hardy-space result is used.

The endpoint proof does not silently extend a bounded exponential factorization. It first uniformizes the principal Beltrami coefficient while F still has W1,2 regularity, and only then uses a possibly unbounded W1,2 exponential and the holomorphic mass estimate. Taking an unbounded exponential before uniformization would leave only W1,t, t<2, and would require a separate justification for the usual Stoilow theorem.

The additional quasiconformal inputs in Section6 are the standard measurable Beltrami, area and composition facts, explicitly stated as dependencies. The exact transformed coefficient norm and all applications of those facts are reconstructed here. No computation or formal build was used.

## 10. Same-sign and finite-energy formulations

First, the entire proof works when S is strictly positive off Gamma. Set H=|S|; the cross-product identity in(3) is unchanged for either constant sign. All later equations depend on H alone. No assertion is made for a changing sign or an accumulating zero set.

Second, since the actual R is smooth on the punctured disk and lies between positive constants, its W1,2-extension hypothesis is equivalent to

    integral_(0<|y|<rho) |D log R(y)|² dy < infinity            (14)

for one sufficiently small rho. One implication is the bounded-derivative Sobolev chain rule for log on [r_-,r_+]. Conversely(14) bounds the punctured integral of |DR|² by r_+² times(14). The bounded function R is in L2 on the full disk. To see that its punctured derivatives are the full weak derivatives, test the integration-by-parts formula with a cutoff that vanishes on B_epsilon and equals one outside B_(2epsilon). The term containing its derivative is bounded by C||R||infinity epsilon and tends to zero; the term containing DR converges by its L2, hence local L1, integrability. Thus the extension is W1,2. Assigning any value at zero is harmless.

Therefore any hypothetical isolated flat k=0 germ with a fixed scalar sign and a ratio bounded above and below must have infinite transverse Dirichlet energy of log R in every neighborhood of the central orbit. This is a necessary condition, not an assertion that the Euler equation controls that energy.

For clarity, the condition permits bounded ratios with no limit at the puncture. On 0<r<exp(-2), the radial scalar

    R(r)=2+(1/2)sin(log(log(1/r)))

lies between3/2 and5/2, has no limit as r tends to zero, and satisfies |R'(r)|<=1/[2r log(1/r)]. Its transverse Dirichlet integral is bounded by a constant times integral_0^rho dr/[r log²(1/r)], which is finite. Hence it has a W1,2 extension despite no continuous extension. This is a functional illustration only, not an Euler tail.

## 11. Verdict and unresolved assumptions

The difference-quotient regularity, supercritical theorem, exact critical transformation, critical multiplier argument and resulting local exclusion are confirmed. The same-sign and logarithmic-energy formulations in Section10 are additional independently checked consequences. Both complete submitted proofs and this independent proof were read in full.

The original proposals are from the a second model the external referee (a second model) agent; comparison is requested through the existing configured model agents, whose provider runtime remains unattested. There is no inference that the needed positive ratio bounds or finite Dirichlet energy follow from bare decay, the local pressure equation or smoothness of the numerator and denominator. The unrestricted common-flat case and the full arbitrary-helicity, all-rotation campaign conjecture remain open.
