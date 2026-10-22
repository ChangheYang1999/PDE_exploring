# A compact residual detected without boundary terms

Status: complete informal argument before implementation. Generic symbolic controls passed; written actual claude-opus-5-5 review188 CONFIRMED the initial theorem. Review189 CONFIRMED(8) and the corollary subject to exact thermal transport, which135 supplies globally. This dependency is explicit below and checked directly against135. Closing request190 returned actual claude-opus-5-5 but no written audit (refusal); it is not counted as confirmation. This is a detector for fixed configurations, not a B2 nonexistence theorem.

## Exact statement

Let O be an open subset of R², beta>2, k=beta-2, W=(W1,W2) smooth and Omega smooth. Suppose a smooth Theta satisfies W.gradTheta=kTheta on O. Define

    f=W.gradOmega+Omega-Theta_x,
    F=W.gradOmega+Omega,
    J=partial_x W2,
    D=(k-partial_x W1)F-W.gradF,
    Z=W1 F J+W2 D,
    E=J partial_y Z-Z partial_y J-k J D.                 (1)

For a test scalar h define the linear differential operators, with W fixed,

    d[h]=(k-partial_x W1)h-W.grad h,
    z[h]=W1 J h+W2 d[h],
    L_W h=J partial_y z[h]-(partial_y J)z[h]-k J d[h].   (2)

Then on O the exact identity is

    E=L_W f.                                          (3)

L_W has order at most2. Its coefficients depend polynomially on k and the derivatives of W through order2. No division by J, W1 or W2 occurs. Thus the identity holds on the symmetry axis and where any of these factors vanish.

Now take one fixed configuration of packet135, equivalently lead4.34. Its temperature equation holds on the whole plane, f is smooth and compactly supported in R0<=r<=8R, and the relative velocity W-beta X and Omega agree with those of a fixed analytic field Psi_L on the nonempty annulus R_ext<r<R. Packet124, equivalently lead4.32, proves that E for Psi_L is analytic and vanishes on no nonempty open set. Then

    I(W,Omega)=int_R² exp(-|X|²) |E(X)|² dX             (4)

is finite and strictly positive for this configuration, whereas it is0 for every smooth profile. Also supp E is contained in supp f. For any nonempty open ball B with compact closure inside that annulus and any nonnegative smooth chi compactly supported in B and positive on a nonempty open subset,

    I_chi=int chi |E|² >0.                             (5)

There is a finite C depending on k, W on B, and chi such that

    I_chi^(1/2) <= C ||f||_(H²(B)).                    (6)

This lower bound pertains to this fixed configuration and chosen ball. No constant uniform over reference choices or beta is asserted. A fixed-reference uniformity statement is proved separately below.

Finally the fixed positive measurement in(5) persists under sufficiently small changes of W in C² and of Omega in C³ on a compact neighborhood of supp chi, with beta fixed. It therefore excludes a neighborhood of the fixed stream in C⁵ on that compact set together with the center, when W is defined by the center-subtracted stream velocity. This is a local stability statement for an already nonprofile field, not a quantitative lower bound in a parameter-independent norm and not an exclusion of the admissible class.

## Proof of the residual identity

Write g=Theta_x. Differentiating the exact temperature equation in x gives

    (partial_x W1)g+W.grad g+J Theta_y=k g.

Therefore d[g]=J Theta_y. The temperature equation also gives

    z[g]=W1 J g+W2 J Theta_y=k J Theta.

Differentiating the latter identity in y and substituting d[g]=J Theta_y shows

    J partial_y z[g]-(partial_y J)z[g]-k J d[g]
      = k J ((partial_y J)Theta+J Theta_y)
        - k J (partial_y J)Theta-k J²Theta_y=0.

Since F=g+f and d,z,L_W are linear in their scalar argument, the left side of(1) equals L_W F=L_W g+L_W f=L_W f. This proves(3). Inspecting(2), d is first order, z first order, and partial_y z second order; the highest derivative of W comes from partial_y partial_x W1 or partial_y J. This proves the order and coefficient assertions. The calculation uses only differentiation and multiplication, so requires no integration by parts or nonvanishing assumption.

## Compact support, strict positivity and the norm bound

A differential operator with smooth coefficients cannot enlarge support: outside supp f there is a neighborhood on which f and all of its derivatives vanish, so(3) gives E=0. For the fixed smooth configuration, E is therefore compactly supported and bounded. This proves finiteness of(4).

On the annulus of exact agreement, E is the E of Psi_L because(1) uses only local derivatives of W and Omega, with the same center subtraction already included in the agreement hypothesis. The identity theorem and the already verified nonzero analytic Taylor coefficient of packet124 imply that E vanishes on no nonempty open subset there. If the integral in(5) were0, continuity and chi>0 on some open subset would force E=0 on that subset, a contradiction. Thus(5) is strictly positive, and the positive Gaussian weight gives(4)>0. The argument does not require computing a distant Taylor series at the annulus or analytically continuing the glued field. Only the reference analytic E is continued. The domain of analyticity is all of R², connected and containing both the center and the annulus; the analytic drift uses exactly the center subtraction of the configuration. In135, R0<R_ext<R, so the annulus is outside the exact inner disk.

Write L_W f=sum_(|alpha|<=2) c_alpha partial^alpha f. The coefficients have finite suprema on the compact closure of B. Multiplication by sqrt(chi), the triangle inequality in L², and Cauchy-Schwarz over the finite derivative list give

    ||sqrt(chi)L_W f||_L²
       <= ||sqrt(chi)||_infinity
          (sum ||c_alpha||_infinity²)^(1/2)
          (sum ||partial^alpha f||_L²(B)²)^(1/2).

This is(6), with the displayed finite constant. The zero-order coefficient is included. Strict positivity in(5) makes the resulting lower bound nonzero for this fixed f. No integration by parts or boundary term is present, and no signed cancellation can make a positive square integral vanish.

For an arbitrary smooth profile, (T) and (V) give f=0 and hence E=0 pointwise. Its integrals(4)-(5) are0, without any integrability assumption on the original profile fields: the integrand is the zero function.

## Uniformity when the reference is fixed

Fix beta,a0,R0 and one reference of135, with its fixed R_ext. This reference has exact thermal transport everywhere: t_*=W_*.gradTheta_*-kTheta_*=0. Packet135 preserves that equation globally for every R. Thus the one-residual identity(3), rather than only the general identity(8), applies on B. Choose once and for all a ball B with compact closure in r>R_ext, and a nonnegative smooth chi supported in B and positive on an open subset. Put R_B greater than both R_crit and sup_(X in B)|X|. For every gluing radius R>=R_B, property(i) of135 makes Psi_R, W_R, Omega_R and Theta_R exactly equal to the fixed reference on B. In particular

    E_R|_B=E_*|_B, f_R|_B=f_*|_B,
    int chi |E_R|² = int chi |E_*|² >0.                (9)

The positivity uses the same analytic obstruction because B lies in the analytic exterior of the reference. The coefficient bound C in(6) also depends only on the fixed W_* on B, so the lower bound for ||f_R||_H²(B) is uniform for R>=R_B. This does not assert a bound uniform as the reference, beta, R0 or B changes.

In fact the whole family tends to the fixed reference in C^infinity_loc as R->infinity: every fixed compact set is contained in B_R eventually, and all four fields agree there exactly. That reference is a nonprofile by124. Thus for a fixed reference the compact residual in135 does not leave every fixed compact set as the gluing radius grows; it retains the fixed nonzero residual on B. This fact follows from the literal agreement property, without any compactness estimate for the corrections. A family in which the reference changes is outside this corollary.

## Stability and its exact scope

Formula(1) is a polynomial in finite jets: derivatives of W through order2, derivatives of Omega through order3, and k. On a bounded set of such jets this polynomial is Lipschitz, as follows by telescoping each finite product, one factor at a time. Thus for a fixed compact K containing supp chi in its interior, there is a finite constant C_M on a sufficiently large bounded jet set such that

    ||E(W_tilde,Omega_tilde)-E(W,Omega)||_C0(K)
       <= C_M (||W_tilde-W||_C²(K)+||Omega_tilde-Omega||_C³(K)).

Since ||sqrt(chi) E||_L²>0, the triangle inequality shows that this norm remains positive whenever the right side times ||sqrt(chi)||_L² is less than half the original norm. The perturbed fields cannot be a profile. No temperature equation is required to apply this last necessary-condition test to a perturbation.

For Omega=-DeltaPsi and W=beta X+gradperpPsi-gradperpPsi(0), control of Psi through order5 on K and through order1 at0 provides the needed jet control. The center term cannot be omitted if0 is not in K: a compactly supported stream perturbation with nonzero center gradient changes the relative velocity by a constant outside its support. This is why the stated stream neighborhood controls the center as well as K. No canonical inverse for arbitrary perturbations is inferred here; every actual profile must still satisfy its inverse condition independently.

## Extension when both equations have residuals

For arbitrary smooth Theta, put t=W.gradTheta-kTheta and keep f=F-Theta_x. The same differentiation gives d[Theta_x]=J Theta_y-t_x and z[Theta_x]=k J Theta+J t-W2 t_x. Substitution into(1) yields the exact identity

    E=L_W f+M_W t,
    M_W t=J² t_y-J W2 t_xy
              +[W2 J_y+J(k-partial_y W2)]t_x.          (8)

To verify it, differentiate J t-W2 t_x in y in the definition of L, cancel J J_y t against itself, and keep the added k J t_x from d. This leaves exactly(8). Thus on a compact ball the square measurement is bounded by C(||f||_H²+||t||_H²). The identity(3) is the special case t=0. No inverse law or divergence hypothesis is needed for(8); these remain separate requirements for a B2 profile.

## Relation to the horizontal offset detector and a blind spot

Assume additionally Theta(0,y)=0 and |Theta_y(X)|<=C(1+|X|)^(-gamma) for some gamma>0 as in packet136, and let f be smooth and compactly supported. For the source F=Theta_x+f,

    lim_(L->infinity) int_0^L [F(x,y)-F(x,0)]dx
       = I_f(y)-I_f(0),
    I_f(y)=int_0^infinity f(x,y)dx.                     (7)

Indeed the Theta contribution tends to0 by its exact finite-interval difference; the compactly supported f integrals converge. I_f is smooth and compactly supported in y. Therefore the offset is identically0 iff I_f is constant, which by compact support is equivalent to I_f identically0.

Nonzero compact f can have I_f identically0: take any nonzero even-in-x compactly supported smooth phi with phi(0,y)=0 and f=partial_x phi, for example phi=x² eta(x²+y²) for a smooth radial bump eta supported on0<=s<=1 and positive on0<=s<1/2. Then f is odd in x and nonzero, while I_f(y)=phi(infinity,y)-phi(0,y)=0. This is a source-level example only; it is not claimed to arise from packet135 or to solve any stream system. Thus horizontal offsets alone do not detect every possible compact residual. The compatibility square(5) does detect each configuration of135 because of the proved analytic agreement.

## Dependencies and honesty boundaries

Dependencies: packet124's analytic obstruction for Psi_L, packet135's exact reference agreement and compact residual, and packet136 only for(7). The elementary identity(3), compact-support assertion and local bounds stand alone under their explicit hypotheses. Verification is by independent symbolic differentiation and manufactured compact tests after this proof. The control with W=(x,7y-x²/2), Theta=x² and Omega=x(1+y) is solely an algebraic test: this Omega is not -DeltaPsi for its displayed W. The second control Omega=x is the consistent local polynomial profile for Psi=3xy-x³/6. Neither polynomial control is a global admissible class A field. No numerical quadrature is a proof of a global PDE. No no-go theorem is obtained, and these measurements do not resolve the broad beta>2 branch or the beta=2 smooth-flat branch.

Written UTC: 2026-10-21T06:46:26.355728+00:00

General two-residual extension written UTC: 2026-10-21T06:47:02.005221+00:00

Fixed-reference corollary written UTC: 2026-10-21T06:49:01.632216+00:00

Review189 dependency clarification UTC: 2026-10-21T06:53:09.465769+00:00
