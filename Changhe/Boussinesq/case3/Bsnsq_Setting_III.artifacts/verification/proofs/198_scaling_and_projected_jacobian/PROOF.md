# Spatial scaling in divided fields and a projected fixed-point Jacobian

## Statement and scope

Let beta>0, let Omega=xG, Theta=x^2F and Psi=xH be smooth fields with x-reflection symmetry, and let U=(-Psi_y,Psi_x), -Delta Psi=Omega. Use the canonical relative whole-plane velocity V[Omega]=U-U(0), assumed linear and compatible with dilation. These hypotheses hold for the convergent once-subtracted inverse in the specified power-decaying classes. No candidate solution is assumed for the algebra below.

For ell>0 the B2 spatial scaling is Omega_ell(X)=Omega(X/ell), Theta_ell(X)=ell Theta(X/ell), Psi_ell(X)=ell^2 Psi(X/ell). Its divided fields and tangent at ell=1 are

 G_ell(X)=ell^-1 G(X/ell), F_ell(X)=ell^-1 F(X/ell), H_ell(X)=ell H(X/ell),

 dot G=-G-X.grad G, dot F=-F-X.grad F, dot H=H-X.grad H.

The tangent -X.grad G obtained by differentiating G(X/ell) alone is not the exact B2 scaling tangent. When G is nonzero it differs by G, and at the center it has value zero instead of -G(0). The genuine scaling keeps the strain c=Psi_xy(0) fixed and sends a0=F(0) and b0=G(0) to a0/ell and b0/ell. The incomplete transformation G(X/ell) instead sends the strain to ell c, whenever its Poisson inverse has the stated scaling property.

The normalized forced iteration with fixed a0 and fixed external velocity has no scaling symmetry from these formulas. It is therefore not justified to demand that either the incomplete tangent or the correct projected tangent be a null vector of the matrix J_T-I for that iteration. Singular values of a coefficient Jacobian also depend on the coefficient norm and on conditioning of the representation; they are not basis-invariant evidence of a physical near-kernel.

## Derivation of the divided scaling and strain check

Write Omega(X/ell)=(x/ell)G(X/ell)=xG_ell(X). Similarly ell Theta(X/ell)=ell(x/ell)^2F(X/ell)=x^2F_ell(X), and ell^2 Psi(X/ell)=ell xH(X/ell). Differentiation in ell at1 gives the formulas above. The derivative computation uses ordinary smoothness and has no elliptic approximation. At the center a0 and b0 have the stated scaling. Twice differentiating Psi_ell in x,y cancels its prefactor ell^2, so c is invariant. A convergent relative inverse obeys V[Omega_ell](X)=ell V[Omega](X/ell), by the kernel change of variables Y=ell Z. For the incomplete divided scaling, xG(X/ell)=ell Omega_ell(X); linearity of the inverse therefore multiplies Psi_ell and its strain by ell.

In the recorded radial representation a dilation is exactly realized by replacing the geometric scale L by ell L, dividing every active G and F coefficient by ell, retaining beta_basis, degree and dimensionless knots, and multiplying the H coefficients by ell if H is separately represented. The odd-angular-mode factor r/sqrt(r^2+L^2) transforms under the same change of L. This is an exact identity of the ideal reconstructed fields, including their axis values. It does not mean that this family lies in a solver with L and a0 held fixed. Its derivative at fixed representation can be projected into that representation, but projection error must then be checked.

## Fixed-source residual identity

Let eps and lambda be fixed real parameters. Write the forced transport field as W(X)=beta X+eps V[Omega](X)+lambda V_f(X), where V_f(0)=0 is a given smooth relative source velocity. Define R_Omega=W.grad Omega+Omega-Theta_x and R_Theta=W.grad Theta-(beta-2)Theta. For the scaled unknowns but the same V_f, put D_ell(X)=V_f(X)-ell V_f(X/ell). Exact substitution gives

 R_Omega[Omega_ell,Theta_ell;V_f](X)=R_Omega[Omega,Theta;V_f](X/ell)+lambda D_ell(X).grad Omega(X/ell)/ell,

 R_Theta[Omega_ell,Theta_ell;V_f](X)=ell R_Theta[Omega,Theta;V_f](X/ell)+lambda D_ell(X).grad Theta(X/ell).

Indeed W_ell(X)=ell W(X/ell)+lambda D_ell(X), grad Omega_ell=ell^-1 grad Omega(X/ell), and grad Theta_ell=grad Theta(X/ell). At ell=1, dot D=X.grad V_f-V_f. Thus even at an exact forced solution the linearized residual in the genuine scaling direction has source terms lambda(X.grad V_f-V_f).grad Omega and lambda(X.grad V_f-V_f).grad Theta. They need not vanish. A source scaled simultaneously as V_f,ell=ell V_f(X/ell) restores the covariance of the forced equations. No such source scaling is performed in the documented fixed-source vertex iteration.

## What the strain projection does to the Jacobian

Let coefficient vectors lie in R^n. Let c be a nonzero linear functional and q a vector with c(q) nonzero. The affine projection to strain c_*=constant is

 P(z)=z+q(c_*-c(z))/c(q), so DP=I-q c/c(q) and DP q=0.

Suppose a differentiable iteration has the form T=Q composed with P, with all other parameters held fixed. Then J_T q=DQ DP q=0. For A=J_T-I one has A q=-q. The projection direction is an exact zero eigenvector of J_T and an eigenvector of A with eigenvalue-1; it is not a null vector of A. This assertion is exact for the defined map, independent of whether z is a fixed point. Forward differences in direction q also give zero in exact arithmetic, since P(z+hq)=P(z). Coordinatewise finite differences and floating projection need not preserve this exactly.

Changing coordinates from z to z'=Sz, for invertible S, gives J'=SJS^-1 and A'=SAS^-1. Eigenvalues are unchanged, but Euclidean singular values can change. For example A=[[1,M],[0,1]] has both eigenvalues1 and determinant1. Its smallest singular value is at most1/sqrt(1+M^2), by testing the unit vector proportional to(-M,1), and tends to0 as M grows. It is similar to [[1,1],[0,1]] using S=diag(M,1), for M>0. Thus a small coefficient singular value without a fixed norm and representation conditioning does not establish a physical near-kernel.

## Finite differences and existence claims

A finite-difference matrix of a numerical fixed-point map is a sampled derivative approximation. Comparing selected columns at two or three steps measures their disagreement. It does not by itself bound derivative error in all columns, prove invertibility of the true derivative, bound nonlinear remainder terms, or prove a nearby fixed point. For example a scalar map f(t)=t+C t(t-h)(t-10h) has values f(0)=0, f(h)=h and f(10h)=10h, but derivative f'(0)=1+10C h^2, arbitrary as C varies. A third tested positive step can be included as another vanishing factor with the same conclusion. For any prescribed finite set of nonzero steps, a polynomial vanishing at those steps and at0 has a nonzero derivative at0 unless its coefficient is zero. Finite differences are useful diagnostics; a rigorous derivative error requires additional smoothness bounds or another proved error estimate.

## Dependencies and verdict

The proof uses the prompt's exact scaling, linearity and covariance of the relative inverse, the chain rule, and finite-dimensional linear algebra. It does not import the numerics lane's code or claim any unseen matrix calculation. The phrase "exact-scaling direction" for the derivative of G(X/(1+e)) is REFUTED as written. Whether the actual implementation computes the correct tangent remains OPEN until its saved diagnostic data specify the tested vector. The future matrix's numerical conditioning, its projected-map derivative accuracy, and any nonlinear fold remain OPEN.

## Verification evidence

UTC 2026-10-21T19:21:14.667330+00:00.

CONFIRMED the exact divided scaling G_ell=ell^-1 G(X/ell), F_ell=ell^-1 F(X/ell), H_ell=ell H(X/ell), with strain invariant and a0,b0 divided byell. REFUTED NUM7m(ii)'s formula calling the derivative of G(X/(1+e)) alone the exact-scaling direction: it misses -G. Whether the implementation tests that literal vector remains OPEN until saved diagnostics specify it.

CONFIRMED the forced fixed-a0, fixed-source iteration lacks the claimed scaling family in general. The exact source defect is lambda[V_f(X)-ell V_f(X/ell)]. For T=Q composed with the affine strain projection, J_T q=0 and (J_T-I)q=-q. A small Euclidean coefficient singular value depends on coordinates and is not by itself a physical near-kernel. Agreement of finitely many difference steps supplies no universal derivative bound: the explicit polynomial counterexample retains all tested values and changes the derivative arbitrarily.

Independent controls: 53 exact algebra checks, six native reconstructed states, 77 Cartesian points per field, seven-point differences in the scaling parameter at three steps versus analytic radial differentiation; maximum scaled difference 1.84587622964e-11. Six independent Cartesian Duffy full-plane inverse tests on a shifted Gaussian at three scales and two orders give maximum absolute error 1.11022302463e-16. Elapsed 1.679221699s. These floating controls are consistency evidence, not enclosures or proof of a continuum Jacobian. No NUM code was reused.

The complete proof was written19:11:18 before controls. Its original text is retained from the actual review369 request; the final text only repairs an awkward algebraic display and adds this verification record. Review370 completed with actual claude-opus-5-5; review369 supplied no audit text and is not counted as an endorsement. No matrix or root had been supplied at the time of this audit. B2 YES and full NO endpoints remain OPEN.
