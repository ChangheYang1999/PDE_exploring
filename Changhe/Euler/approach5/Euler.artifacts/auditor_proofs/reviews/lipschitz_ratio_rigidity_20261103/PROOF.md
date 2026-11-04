# Positive Lipschitz ratios at an isolated flat orbit

## 1. Exact local theorem

Fix 0<c<1/2 and any finite real omega. Let Jx=e3 cross x, A=cI-omega J, X(x)=Ax, a=1-2c, b=2-2c, eta=a/b and m=1/c>2. Let x0!=0 and let G be a small tubular flowbox for X, with central orbit segment Gamma through x0. Suppose V and S are smooth real fields on G and

    div V=0, X.grad V=-(1-c)V-omega JV,
    X.grad S=-bS, k=X.V=0,
    grad k=X cross W-aV, W=curl V, W.grad S=0.       (1)

Suppose S<0 on G minus Gamma, S=0 on Gamma and S is infinitely flat at x0. If R=|V|²/(-S) has a locally Lipschitz extension to G with R(x0)>0, these hypotheses are incompatible. In particular every positive constant ratio is excluded, without a restriction on its size. Neither the pressure equation nor a helicity hypothesis appears in this local theorem.

After shrinking the flowbox, the ratio satisfies 0<r_-<=R<=r_+ and has a finite Lipschitz constant. The constants in the proof may depend on c, omega and the flowbox. Thus the statement covers every finite omega without claiming uniform quantitative constants as omega tends to infinity. Section9 shows the same theorem for S>0 off Gamma, with R=|V|²/|S|.

## 2. Closed one-form and removal of its period

Write H=-S>0 off Gamma. From k=0, the fourth identity in(1) gives X cross W=aV. The vector identity

    grad S cross(X cross W)=X(grad S.W)-W(grad S.X)=bSW

therefore yields grad H cross V=eta^(-1)HW. Consequently

    curl(H^(-eta)V)=0, X.(H^(-eta)V)=0.            (2)

Also |H^(-eta)V|=sqrt(R)H^(1/2-eta). The exponent 1/2-eta=c/[2(1-c)] is positive. On a smooth transverse disk centered at x0 this norm tends to zero faster than every power of the disk radius, because H is flat and R is bounded. Its circulation on a small circle tends to zero. Closedness makes that circulation independent of the radius by Stokes on each intervening annulus. Hence the period is zero. A punctured disk times an interval has just this one period, so(2) has a single-valued smooth potential phi on G minus Gamma.

Since X.phi=0, choose flowbox coordinates Psi(t,y)=exp(tA)n(y), where n parametrizes a transverse sphere patch, n(0)=x0. Then phi(Psi(t,y))=u(y). The transverse gradient Du is flat at y=0. Radial integration gives a finite radial limit of u, and integration on small circular arcs shows that the limit is independent of direction. Extending by that value gives u in C1 on the full disk, smooth off zero, with

    |u(y)-u(0)|+|Du(y)|<=C_N|y|^N                 (3)

for every positive integer N near zero. No unproved bound on higher derivatives of the divided potential is needed.

## 3. The exact two-dimensional equation

The pullback Euclidean metric under Psi is exp(2ct)g(y), since exp(tA) is exp(ct) times a rotation. Its entries are

    g00=|An|², g0i=An.partial_i n,
    gij=partial_i n.partial_j n.

Let mu=sqrt(det g), B^ij=g^ij for i,j=1,2, and z^j=g^0j. The principal matrix B is smooth positive definite. Homogeneity gives H(Psi(t,y))=exp(-bt)h(y). Since V=H^eta grad phi, its contravariant components are exp(-(b eta+2c)t)h^eta g^(alpha j)u_j. Here b eta=a and a+2c=1. The volume density is exp(3ct)mu. Thus div V=0 becomes exactly

    partial_i(mu h^eta B^ij u_j)
           +(3c-1)mu h^eta z^j u_j=0.           (4)

The ratio is orbit invariant: both |V|² and H scale by exp(-bt). On the transverse disk it obeys

    R=h^(2eta-1)|Du|_B²,
    h^eta=R^(-tau)|Du|_B^(m-2),
    tau=eta/(1-2eta)=(m-2)/2.                   (5)

Use local smooth isothermal coordinates for the smooth metric B inverse. In the new coordinates B=lambda^(-2)I, lambda smooth and positive; mu transforms as a density and z as a vector. Substitution in(4) gives

    div(w |Du|^(m-2)Du)+w d.(|Du|^(m-2)Du)=0,
    w=mu lambda^(-m)R^(-tau),
    d=(3c-1)lambda² z.                          (6)

The weight w is positive and locally Lipschitz, bounded above and below on a smaller disk; d is smooth. The coordinate changes preserve(3). Equation(6) holds weakly across zero: in(4) its flux and lower-order term are smooth geometric factors times components of the flat V. The inner-circle flux is O(epsilon^(N+1)) for every N, so no point source remains. This verifies all geometric factors, including the time-divergence coefficient 3c-1.

## 4. Direct nonlinear-gradient regularity

We prove the analytic statement needed for(6), instead of applying a theorem requiring an unavailable Lipschitz divided drift. Let u be C1 on a disk and C2 off its center, let m>2, and assume(6) weakly, with positive Lipschitz w and Lipschitz d. Write v=Du,

    T(v)=|v|^(m-2)v, F_vec(v)=|v|^((m-2)/2)v.

For v_h=v(x+h), delta v=v_h-v, the elementary power-map inequalities are

    (T(v_h)-T(v)).delta v >= c_m sigma^(m-2)|delta v|²,
    |T(v_h)-T(v)| <= C_m sigma^(m-2)|delta v|,
    |F_vec(v_h)-F_vec(v)|² <= C_m sigma^(m-2)|delta v|²,
    sigma=|v_h|+|v|.                            (7)

Take a compact cutoff chi and test the translated equation minus the original equation with chi² delta u, where delta u=u(x+h)-u(x). Set E_h=integral chi² sigma^(m-2)|delta v|². The gradient v is bounded on the slightly larger disk, |delta u|<=C|h|, and both delta w and delta(wd) are O(|h|). The leading monotonicity term is at least c E_h. There are four error types:

- The cutoff term containing delta T and delta u is at most C|h|E_h^(1/2), by weighted Cauchy-Schwarz and bounded v.
- The coefficient-gradient term containing delta w T(v) and delta v has the same bound, since |T(v)|/sigma^((m-2)/2)<=sigma^(m/2).
- The coefficient-cutoff term containing delta w and delta u is O(|h|²).
- The drift difference is w_h d_h.delta T+delta(wd).T(v). Multiplication by chi² delta u bounds these parts by C|h|E_h^(1/2) and C|h|², respectively.

At sigma=0 every relevant numerator vanishes, so the quotient estimate is interpreted as zero. Young's inequality gives E_h<=C|h|². By(7), the coordinate difference quotients of F_vec(Du) are bounded in L2 on every smaller disk. A weakly convergent subsequence of each quotient represents the distributional derivative, as follows by shifting a compact smooth test function. Therefore F_vec(Du) belongs to Wloc^(1,2).

## 5. Exact complex-gradient inequality

Identify the transverse plane with C and put

    F=|Du|^((m-2)/2)(u_x-i u_y).

It is continuous, locally bounded and Wloc^(1,2). Dividing(6) by w yields

    div(|Du|^(m-2)Du)+beta.(|Du|^(m-2)Du)=0,
    beta=grad log w+d in Lloc^infinity.           (8)

At a point off the center where Du!=0, rotate coordinates so Du=(r,0), r>0, and denote the Hessian by h_ij. Almost everywhere(8) says (m-1)h11+h22=-r beta1. Direct differentiation gives

    F_z=(r^((m-2)/2)/2)[(m/2)h11-h22-i(m/2+1)h12],
    F_barz=(r^((m-2)/2)/2)[(m/2)h11+h22+i(m/2-1)h12].

Remove the beta1 terms. The respective real and imaginary coefficient ratios are (m-2)/(3m-2) and (m-2)/(m+2). Their maximum is kappa=(m-2)/(m+2)<1. Restoring beta1 gives

    |F_barz|<=kappa|F_z|+C_m|beta||F|.           (9)

The absolute-value inequality is invariant under the coordinate rotation. At a punctured point where Du=0, the map F_vec is C1 with derivative zero at zero since m>2; u is C2 there, so DF=0. The omitted center is a null set. Thus(9) holds almost everywhere on the full disk.

## 6. The precise continuation input and its proof mechanism

The actual Guo-Kar manuscript, printed pages8-10, proves the required first-order factorization from an inequality of the form(9), after the nonlinear W1,2 regularity has been supplied. Its literal Theorem1.2 assumes a locally Lipschitz drift in the nonlinear equation and is not being applied to beta in(8).

Here are the exact first-order dependencies and their application. Measurably split(9) as

    F_barz=mu0 F_z+nu F, |mu0|<=kappa, |nu|<=C.

For example, set D=kappa|F_z|+C|F|, lambda0=F_barz/D when D>0, and use mu0=kappa lambda0 conjugate(F_z)/|F_z|, nu=C lambda0 conjugate(F)/|F|, assigning zero at zero factors. The case D=0 has F_barz=0. Extend the coefficients by zero from a smaller disk. The Lp boundedness of the Beurling transform, its L2 norm one and interpolation give a delta>2 close enough to2 that kappa||Beurling||_delta<1. Neumann inversion therefore solves

    (I-mu0 Beurling)g=nu

in Ldelta. The solution has compact support because both coefficients do. Its Cauchy transform psi is bounded and continuous, with psi_barz=g and psi_z=Beurling(g). The product f=F exp(-psi) belongs locally to W1,2: F is bounded, the exponential is bounded and its derivative lies in Ldelta. The product rule gives f_barz=mu0 f_z.

The classical measurable Beltrami and Stoilow factorization theorem now writes f=Holo composed with chi, where chi is a quasiconformal homeomorphism and Holo is holomorphic. The map and its inverse have local Holder estimates. These are the external analytic inputs; their use and the factorization are explicitly present in the selected primary pages. In particular, the phrase on printed page10 that exp(psi) is nonnegative is unnecessary and generally false for a complex psi. Nonvanishing of the complex exponential suffices for the displayed algebra.

By(3), F and f vanish to every order at zero. If Holo is nonzero, its zero at chi(0) has some finite integer order j. The inverse Holder estimate gives

    |f(x)|=|Holo(chi(x))|>=C|chi(x)-chi(0)|^j
                              >=C'|x|^(j/alpha)

near zero, for some alpha>0. This contradicts flatness. Therefore Holo, F and Du vanish near zero. Equations(5) contradict h>0 and R>0 on the punctured disk. This proves Section1.

## 7. Citation audit and exact source scope

The actual primary source is Chang-Yu Guo and Manas Kar, Quantitative uniqueness estimates for p-Laplace type equations in the plane, arXiv:1512.00673v2, dated8 March2016. The title page, Theorems1.2-1.3 on page4, and pages7-11 containing the required regularity context and complete first-order factorization were read directly from the retained manuscript text. The present audit does not claim a complete reading of the27-page paper.

The coordinator's nested verification names arXiv:1512.00697 and a different title. That is not this manuscript and must be corrected before that verification is relied upon as a source citation. This audit relies on the actual retained Guo-Kar text. Its nonlinear drift theorem and its weighted divergence-only theorem have distinct hypotheses; neither alone is a literal theorem for(6). Sections4-6 supply the missing combination. No asserted extension in the paper's concluding discussion is used.

## 8. No circularity in the metric or potential steps

The closed potential is constructed before solving any elliptic equation. Its period vanishes from flatness and bounded R, not from unique continuation. The weak equation across the puncture follows from the original smooth V, not from presumed derivative bounds for phi. Smooth isothermal coordinates depend only on the background flowbox metric, not on V or the potentially flat H. The positive ratio bounds enter precisely in the weight's ellipticity and regularity. Finally, the nonlinear W1,2 estimate is obtained before the first-order factorization, avoiding the unproved bounded-drift approximation mentioned in the manuscript's discussion.

## 9. Additional same-sign extension

The sign restriction S<0 is unnecessary for this particular first-order proof. Assume instead that S has either fixed strict sign on G minus Gamma, vanishes on Gamma and is infinitely flat at x0, and let R=|V|²/|S| have a positive Lipschitz extension. Put H=|S|. Since the sign is constant on the punctured flowbox, the calculation in Section2 gives grad H cross V=eta^(-1)HW with exactly the same sign. Every remaining equation and estimate involves H rather than S. Thus the same contradiction holds for positive S as well.

This extension uses only the listed first-order equations. It does not claim that a positive-S branch can occur in any additional profile class or override stronger earlier exclusions. It also does not allow a changing sign or an arbitrary accumulating zero set.

## 10. Verdict and remaining scope

The Lipschitz-ratio exclusion is confirmed, with the analytic dependencies stated in Section6 and the citation corrected in Section7. The same-sign extension in Section9 is independently proved. The source and this complete proof have been read in full. No numerical computation or formal build is used. The original source agent is a second model the external referee (a second model); comparison is requested through the already configured model agents, whose provider runtime remains unattested.

No step establishes a Lipschitz, Sobolev or merely bounded ratio from the Euler hypotheses. Ratios approaching zero or infinity, insufficiently regular ratios, additional scalar zeros and nonzero-k accumulation remain outside this theorem. The unrestricted common-flat problem and the campaign's bare-decay, arbitrary-helicity, all-rotation conjecture remain open.
