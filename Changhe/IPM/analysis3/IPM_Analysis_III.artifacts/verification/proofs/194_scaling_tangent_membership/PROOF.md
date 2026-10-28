# The formal scaling tangent need not belong to the high domain

## Exact statement

Let rho_0 be the exact normalized joined modal trial of topics04 and67, with its canonical velocity and parameter ell_0=1/k. In the spline region write

 rho_0(r,theta)=r^3 p(theta) sum_(m=0)^259 s_m(t) cos(2m theta),
 t=log r, p(theta)=cos(theta)^2 sin(theta).

Its vertical-axis cofactor is A(t)=sum_m (-1)^m s_m(t). At the original knot with index700, put

 t_*=4958764014967233/2251799813685248,
 j_A=A^(7)(t_*+)-A^(7)(t_*-).

The exact rational check accompanying this proof must establish j_A!=0 before the following conclusion is recorded for the actual trial. Let

 K=rho_0-X.grad rho_0.

Choose any smooth radial cutoff chi(t), supported in the interior spline interval and equal to one near t_*. Then chi K fails to belong to the high correction space H_full=B_H plus X_s of proof 171. The obstruction is local at this knot and persists after adding a function whose axis cofactor is locally H^(29/4) there. It is independent of the far-field growth of K.

Nevertheless the formal scaling identities are valid for the uncut K:

 J(K)=-2, c[K]=0,
 L_full K=F_0-X.grad F_0,
 F_0=(ell_0 X+U[rho_0]).grad rho_0-rho_0,
 L_full h=(ell_0 X+U[rho_0]).grad h-h
                  +(U[h]+c[h]X/3).grad rho_0.

These identities alone do not permit inserting K into the high inverse or the scalar-radius test of proof 181. This is a domain conclusion, not a counterexample to either inverse theorem.

## The scalar high coordinate and the exact jump

The high decomposition in proof 171 is h=E beta+u, where E beta=r^3 p beta, beta belongs to

 B_H=R chi_0+a_H H^(29/4)(R),

and u belongs to X_s with zero vertical-axis cofactor trace. On a fixed compact radial interval, a_H is smooth and strictly positive. Every beta in B_H is therefore locally H^(29/4). The axis cofactor trace is unique: the zero-trace condition on u makes it equal to beta, with its continuous representative. This trace is meaningful because the sector cofactor of u has order25/4, which exceeds1/2.

Since X.grad=partial_t in physical logarithmic polar coordinates,

 K/(r^3 p)=-2 sum_m s_m cos(2m theta)
                         -sum_m s'_m cos(2m theta).

Its axis cofactor is beta_K=-2A-A'. The splines are exactly C6 across t_*. Hence beta_K is C5 there and its sixth derivative has the nonzero jump

 [beta_K^(6)]=-j_A.

The cutoff chi is identically one near t_*, so it changes neither this equality nor its regularity consequence. A one-dimensional piecewise smooth function with a nonzero jump does not belong locally to H^(1/2). Indeed its fractional seminorm contains a positive constant times

 integral_0^epsilon integral_0^epsilon (u+v)^(-2) du dv=infinity.

Apply this to the sixth derivative of beta_K. It follows that beta_K is not locally H^(13/2), hence not locally H^(29/4). It cannot be the scalar coordinate of an element of H_full. Adding an H^(29/4) axis cofactor cannot change this failure, since H^(29/4) is a vector space contained in H^(13/2).

No continuity error is inferred from rounded data. All stored binary64 numbers are interpreted as their exact dyadic rationals. The axis spline coefficients are projected with the exact integer weights(-1)^m. Seven exact derivative recurrences give the one-sided seventh derivatives. Independent exact de Boor polynomial evaluation on the two adjacent spans checks these derivatives and all six joining derivatives. The normalization repair affects only the outer continuation, so it does not alter j_A.

## Formal scaling identities and their scope

For positive lambda, set rho_lambda(X)=lambda rho_0(X/lambda). The canonical degree-zero velocity satisfies U[rho_lambda](X)=lambda U[rho_0](X/lambda). This follows by change of variables in its homogeneous degree-minus-two kernel, including its local multiplier term, or by its Fourier multiplier. The canonical strain is unchanged: its absolutely convergent degree-minus-three kernel has the factors lambda from density, lambda^2 from area and lambda^(-3) from the kernel. The convergence needed for differentiation holds uniformly for lambda in a compact neighborhood of1, using the cubic origin behavior and outer exponent k<1. Thus c[K]=0 and ell(rho_lambda)=ell_0.

The exact residual therefore transforms as F(rho_lambda)(X)=lambda F_0(X/lambda). Differentiating at lambda=1 gives L_full K=F_0-X.grad F_0, as an identity of distributions and of the available classical derivatives away from interfaces. There is no omitted variation of ell because c[K]=0. Finally rho_lambda has leading coefficient lambda^(-2), so differentiation gives J(K)=-2.

The raw K also changes the leading far amplitude, another reason it is outside the fixed high correction space. The cutoff construction above removes that independent tail issue and proves that even a compact radial version has a local high-domain obstruction. Correcting its cubic coefficient or attaching smooth tail coordinates cannot repair the exhibited knot singularity. A smoothed substitute would require its own exact membership and image error estimates before use as a test direction.

## Dependencies and acceptance

Topics01 and04 give the canonical scaling conventions and exact trial. Proof 67 gives the spline recurrence and knot interpretation. Topics150 and171 give the unique scalar coordinate and high space. The companion exact check binds the original NPZ, proof and script identities. Its nonzero-jump result is required for the actual-data conclusion; no numerical size of j_A is used as an estimate.
