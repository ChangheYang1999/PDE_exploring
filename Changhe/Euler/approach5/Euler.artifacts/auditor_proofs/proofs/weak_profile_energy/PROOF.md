# Energy identities and Liouville criteria for bounded weak profiles

Audited 2026-11-02T21:01:38Z. This independently checks Theory Agent A C20. The final method-optimality wording is excluded from the verdict.

## Exact setting and conclusions

Let 0<c<1, omega be real, A=cI-omega J, and let U be an essentially bounded measurable vector field on R3. Suppose div U=0 and

    (1-4c)U+omega JU+div(U tensor Ay+U tensor U)+grad P=0       (W)

in distributions, where div(V tensor W)_i=partial_j(V_i W_j). Assume U(R .) tends to zero in distributions as R tends to infinity. Initially P may be a distribution. Define q=|U|^2/2, B=Ay+U, sigma=5c/2-1, alpha=5-2/c, and

    D=sigma |U|^2-div(qB+PU).                              (D)

The pressure has a locally L2 representative, and D is well-defined and independent of an added pressure constant.

1. If D=0, the energy conclusions A040/A052 and their shell, weighted, velocity-integrability and Lorentz consequences hold with essential values and almost-everywhere equality. The vorticity Lorentz criterion also holds whenever curl U is represented by a function in the stated Lorentz space. In particular, U=0 for c<2/5, while for 2/5<c<1,

    E(R)=L R^alpha+O(R^(alpha-1)),   L>=0,
    L=0 if and only if U=0 almost everywhere.

2. A sufficient condition for D=0 is the local increment condition: for every compact K,

    sup_(|z|<=h) integral_K |U(y+z)-U(y)|^3 dy=o(h).         (B3)

Local Holder exponent strictly greater than 1/3 suffices, as does the local little-Besov condition B^(1/3)_(3,c0). This is a sufficient threshold, not a necessary regularity characterization.

3. Suppose D is a nonnegative distribution and hence a Radon measure. If c<2/5, U=0. If c=2/5, U is in L2, D=0, and in fact the exterior energy is O(R^-5). If 2/5<c<1, the limit L=lim R^-alpha E(R) exists and is nonnegative. The finite quantity

    delta(R)=(2/c) integral_R^infinity r^(-1-alpha)D(B_r) dr

satisfies

    R^-alpha E(R)-L=delta(R)+O(R^-1).                     (2)

Moreover U is in L2 if and only if L=0 and D(R3)<infinity. In that event

    D(R3)=sigma ||U||_2^2.                                (3)

No nonzero dissipative profile is constructed. No assertion is made that zero defect is logically necessary for every Liouville method in the target range.

## 1. Pressure and the weak scaling identity

Taking divergence in (W) gives -Delta P=partial_i partial_j(U_i U_j). The linear rotation terms cancel: the commutator from differentiating Ay.grad U is the negative of div(omega JU), while div U=0 removes the scalar linear terms. A local cutoff of U_i U_j belongs to L2. Its Newton double-derivative potential belongs to L2, and subtracting it from P leaves a harmonic distribution on the smaller ball. Thus P is locally L2 without an initial pressure regularity assumption.

The canonical-pressure proof A031 uses only this Poisson equation, the distributional momentum equation, boundedness and the vanishing dilates. Every integration involving a velocity derivative is integration by parts against a smooth test, and the nonlinear term is div(U tensor U). Therefore it applies to (W) without differentiability of U. It removes the harmonic pressure gradient and yields exactly the same inner, comparable-radius and exterior pressure decomposition and estimates as in the smooth proof. In particular the dyadic shell flux estimate used below is valid for measurable U. A constant pressure change has zero divergence when multiplied by U.

For completeness, let tau=-t in (0,1), s=-log tau, Q_s=exp(omega sJ), y=tau^-c Q_s^T x, and put u=tau^(c-1)Q_s U(y), p=tau^(2c-2)P(y). The change of variables is smooth on every compact time subinterval. The linear transformation identities, valid first for smooth fields and then for distributions, are

    partial_t[tau^(c-1)Q_s V(y)]
      +div_x[tau^(2c-2)Q_s F(y)Q_s^T]+grad_x[tau^(2c-2)S(y)]
    =tau^(c-2)Q_s[(1-c)V+Ay.grad V+omega JV+div F+grad S](y),

and

    partial_t[tau^(2c-2)f(y)]+div_x[tau^(3c-3)Q_s g(y)]
    =tau^(2c-3)[(2-5c)f+div_y(f Ay+g)](y).

Take (V,F,S)=(U,U tensor U,P) and (f,g)=(q,(q+P)U). The first proves weak Euler, and the second gives its energy defect by

    <D(u),phi>=integral_(-1)^0 tau^(5c-3)
                     <D,phi(tau^c Q_s .,t)> dt.            (4)

The extra factor tau^(3c) is the spatial Jacobian. Nonnegativity and vanishing of the two defects are equivalent, using test functions phi(x,t)=chi(t)psi(tau^-c Q_s^T x), with nonnegative nonzero chi supported away from the time endpoints.

## 2. A direct commutator proof of (B3)

This proof avoids importing the defect formula from a source. Let rho_epsilon be a smooth compactly supported spatial mollifier and use subscript epsilon for convolution. Define

    R_epsilon=(U tensor U)_epsilon-U_epsilon tensor U_epsilon,
    C_epsilon=Ay.grad U_epsilon-(Ay.grad U)_epsilon.

Then

    C_epsilon(y)=integral [Az.grad rho_epsilon(z)+3c rho_epsilon(z)]
                              [U(y-z)-U(y)] dz.           (5)

The kernel in brackets has integral zero and uniformly bounded L1 norm. On a fixed compact set let a_epsilon be the supremum of the L3 norm of increments with |z|<=epsilon, on a slightly enlarged compact set. Translation continuity gives a_epsilon tending to zero, and the usual convolution identities give

    ||C_epsilon||_3 <= C a_epsilon,
    ||grad U_epsilon||_3 <= C epsilon^-1 a_epsilon,
    ||R_epsilon||_(3/2) <= C a_epsilon^2.                 (6)

The last identity follows by writing R as the average of increment tensor squares minus the square of the averaged increment. All norms are local, with the fixed compact enlargement understood.

The filtered momentum equation is

    (1-c)U_epsilon+Ay.grad U_epsilon+omega JU_epsilon
       +div(U_epsilon tensor U_epsilon)+grad P_epsilon
       =C_epsilon-div R_epsilon.

Dotting with U_epsilon and using div U_epsilon=0 yields

    sigma|U_epsilon|^2-div(q_epsilon(Ay+U_epsilon)+P_epsilon U_epsilon)
       =-U_epsilon.C_epsilon+div(R_epsilon U_epsilon)
                       -R_epsilon:grad U_epsilon.        (7)

The first two terms tend to zero in distributions by (6) and boundedness. Condition (B3) says a_epsilon^3=o(epsilon), so the last term tends to zero in L1 by (6). The left side tends to D: U_epsilon converges in every finite local Lp, remains uniformly bounded, and P_epsilon tends to P in local L2. Thus D=0.

For local Holder regularity theta>1/3, a_epsilon^3=O(epsilon^(3theta))=o(epsilon). The little-Besov condition is exactly the corresponding vanishing increment modulus. No time regularity, global derivative bound or vorticity equation is used.

## 3. Radial balance with a measure defect

Assume D is a signed Radon measure. The function E(R)=integral_(B_R)|U|^2 is absolutely continuous. For almost every R,

    (cR/2)E'(R)-sigma E(R)=-F(R)-D(B_R),
    F(R)=integral_(|y|=R)(q+P-p)U.n dS.                  (8)

To prove this without a trace assumption, take any smooth chi compactly supported in (0,infinity), set Psi(r)=integral_r^infinity chi, and test (D) with Psi(|y|). Coarea evaluates the flux, and Fubini gives the cumulative measure D(B_R). Open and closed balls differ for at most countably many radii on compact intervals. The pressure constant p drops out because div U=0 gives zero radial flux for almost every radius. This proves (8) distributionally in R and hence almost everywhere.

Writing g(R)=R^-alpha E(R), integration gives

    g(R2)-g(R1)=Fl(R1,R2)
               -(2/c)integral_(R1)^(R2) r^(-1-alpha)D(B_r)dr,   (9)

where Fl is -(2/c) times the weighted spatial integral of (q+P-p)U.n with weight |y|^(-1-alpha). This identity holds for every positive pair R1<R2 after taking the absolutely continuous representative of g.

## 4. The bootstrap uses only the sign of the defect

The pressure shell estimate established in A031/A040 says: if E(r)<=K r^mu for r>=1, with 0<=mu<=3, then

    |Fl(R1,R2)|<=C R^(mu-1-alpha),   R<=R1<R2<=2R.      (10)

Its proof uses the pressure decomposition, bounded U and Holder's inequality, so it remains valid here. The initial exponent is mu=3. If D>=0, (9) bounds each upward increment of g by (10).

Put beta=mu-1-alpha. Summing dyadically from a fixed radius gives the following upper bounds:

- beta>0: E(R)<=C R^(mu-1);
- beta=0: E(R)<=C R^alpha log(2R);
- beta<0: E(R)<=C R^alpha.

In the middle case replace log(2R) by R^epsilon for any fixed epsilon in (0,1), then apply one further step. These are finite iterations. If alpha<0 they give a negative-power or negative-power-log upper bound on the nondecreasing E, so E=0. If alpha=0 they give bounded E. If alpha>0 they give E<=C R^alpha. This checks the one-sided bootstrap rather than silently reusing an absolute increment estimate.

In the latter two cases, use (10) with mu=alpha, where alpha=0 is permitted. The total flux Fl(2,R) converges absolutely in dyadic shells, with tail O(R^-1). The cumulative defect integral in (9) is nondecreasing. It is bounded above because g>=0 and the total flux is bounded. Hence it converges as well, proving existence of L and the exact relation (2). In particular delta(R) is finite and tends to zero.

If D=0 and alpha>0, L=0 gives E(R)<=C R^(mu-1) from any current exponent mu<=alpha, now by summing (10) from R to infinity. Repeating finitely many times gives E=0. Thus the positive coefficient theorem extends with no hidden differentiability. The shell, weighted and velocity criteria use only this energy theorem. The vorticity Lorentz proof uses -Delta U=curl(curl U) and harmonic mean values in distributions and therefore also applies whenever its vorticity function hypothesis holds.

## 5. Critical and finite-total-defect conclusions

At alpha=0, bounded E gives U in L2. Since U is bounded, U tensor U is in L2 and the normalized pressure P2 is in L2. Choose a smooth radial cutoff phi_R increasing to one, equal to one on B_R and supported in B_(2R). Test (D). The terms containing its gradient are bounded in absolute value by

    C integral_(R<|y|<2R)|U|^2
      +C R^-1 ||U||_infinity ||U||_2^2
      +C R^-1 ||P2||_2 ||U||_2,

which tend to zero. The rotational part of Ay is tangent to each sphere. Since sigma=0 and D>=0, every fixed compact ball has zero D-mass. Thus D=0. The critical zero-defect shell estimate A054 uses exactly (8), the pressure split and monotone tail energy; it does not use pointwise differentiability. Its inequality

    T(R)<=C R^-1 T(R/2)+C R^-5/2 sqrt(T(R))

therefore remains valid. Young absorption and five finite iterations give T(R)=O(R^-5).

Now alpha>0. If U is in L2, then L=0. The same cutoff computation and monotone convergence give (3), so D has finite total mass. Conversely assume L=0 and D_tot<infinity. Then

    delta(R)<=(2D_tot/(c alpha))R^-alpha.

If E(r)<=K r^mu with 0<=mu<=alpha, the flux tail in (10) and (9) imply

    E(R)<=C R^(mu-1)+2D_tot/(c alpha).

Starting at mu=alpha, finitely many iterations give bounded E, hence U in L2. Equation (3) follows from the same cutoff argument. This proves the stated equivalence, including both directions.

## Scope

The zero-defect theorem is a verified extension of the energy method. The nonnegative-defect theorem identifies what the same one-sided estimates still imply. It does not prove that every weaker-regularity profile has nonzero defect, that such profiles exist, or that some other global argument cannot exclude them. In particular the phrase “the method needs exactly zero defect” must not be promoted to a universal impossibility theorem. The dynamical claims elsewhere in the campaign retain their C2 hypotheses.
