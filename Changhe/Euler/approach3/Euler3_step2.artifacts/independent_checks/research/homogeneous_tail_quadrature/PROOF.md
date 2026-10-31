# Separated radial evaluation and exact integration of a rotating leading tail

Status: proved identities for the finite potential representation. The formulas do not assert any floating-point accuracy or Euler solution.

## Hypotheses and notation

Let I be an open subset of (2/5,1/2) times (0,infinity). Put alpha=(1-c)/c and kappa=w/c. Let U(x;c,w)=curl(Tx)+curl curl(Sx), where T,S have the finite smooth channel representation stated in ../represented_tail_decay/PROOF.md. Fix all radial scales and harmonic index sets. The real coefficients are C1 on I; if they are obtained by the reduced tail solve, assume its elimination matrices are nonsingular on I. Each real solid harmonic H of degree l is harmonic and homogeneous of degree l. Its restriction and first two Cartesian derivatives at a unit vector n are denoted H(n), h(n), K(n). Write rho=r^2 and primes for derivatives in rho.

For one harmonic, let f(rho) H(x) and g(rho) H(x) be its toroidal and poloidal scalar potentials after resolving the twist into real harmonic partners. Thus all angular dependence is in H and f,g may depend on c,w. Define

A=(l+1)g+2rho g', A'=(l+3)g'+2rho g'',
B=-2l g', B'=-2l g''.

For n in S2 define the vector C=h(n) cross n and the matrix D by

D_ij=(K(n)[:,j] cross n)_i+(h(n) cross e_j)_i.

The notation a tensor b means the matrix with entries a_i b_j. The Cartesian Jacobian has entries (DU)_ij=partial_j U_i. All formulas below hold for r>0. The origin is evaluated by the original smooth Cartesian formulas, never by a negative power of r.

## Separated field identities

The velocity contributed by this harmonic is

U(rn)=f r^l C+A r^(l-1)h+B r^(l+1)n H.

Its Jacobian is

DU(rn)=2f' r^(l+1)(C tensor n)+f r^(l-1)D
       +A r^(l-2)K+2A' r^l(h tensor n)
       +B r^l(I H+n tensor h)+2B' r^(l+2)H(n tensor n).

These formulas extend by finite summation and by first parameter differentiation. When reduced coefficients depend on parameters, their derivatives must be included in f_p,g_p; the displayed formulas are linear in f,g and their rho derivatives, so applying them to f_p,g_p gives U_p,DU_p.

Proof. The potential reconstruction identity from ../field_reconstruction/PROOF.md is

U(x)=f(grad H cross x)+A grad H+B x H.

It also follows directly from curl(Tx)=grad T cross x and curl curl(Sx)=2grad S+(D^2 S)x-x Delta S. Euler homogeneity gives x dot grad H=lH, while Delta H=0. Applying the product rule and partial_j rho=2x_j gives

DU=2f'(grad H cross x) tensor x+f[(D^2 H[:,j] cross x)+(grad H cross e_j)]_ij
   +A D^2 H+2A'(grad H tensor x)+B(IH+x tensor grad H)+2B'H(x tensor x).

Homogeneity gives H(rn)=r^l H(n), grad H(rn)=r^(l-1)h(n), and D^2 H(rn)=r^(l-2)K(n). Substitution proves each displayed power. Parameter differentiation commutes with finite sums and the spatial derivatives under the hypotheses. This proves the separated evaluation identities without assuming an angular quadrature.

## Exact rotating leading source

Define U_infinity by retaining only A,C channels, replacing s by r, and replacing every radial polynomial by its value at the outer endpoint xi=1. Its coefficients may still depend on c,w. Let f_infinity=tr((DU_infinity)^2). Use orthonormal complex spherical harmonics with azimuthal convention Y_lm(theta,phi)=y_lm(theta) exp(i m phi). Put

A_lm(c,w)=integral_S2 f_infinity(n;c,w) conjugate(Y_lm(n)) dS.

Then the exact spherical source coefficient at radius r>0 is

(f_infinity)_lm(r)=r^(-2alpha-2+i m kappa) A_lm.

For p equal to c or w its parameter derivative at fixed r is

(partial_p f_infinity)_lm(r)=r^(-2alpha-2+i m kappa) [A_p,lm+B_p,lm log r],

B_c,lm=A_lm(2/c^2-i m w/c^2),
B_w,lm=A_lm i m/c.

Here A_p is the parameter derivative of the full unit-radius source, including the reduced coefficient derivative and any fixed R0 factors. It is not only the derivative of the explicit exponent.

Proof. Let R_t denote rotation by t about the third axis. The scalar leading potentials have radial powers -alpha and 1-alpha, with their angular argument rotated by kappa log(r/R0). The fixed phase at r=1 and every R0 power are already included in their unit-radius values. For a fixed lambda>0 let Q=R_(-kappa log lambda) and M=lambda Q, a constant linear similarity. The potentials satisfy T_infinity(Mx)=lambda^(-alpha)T_infinity(x) and S_infinity(Mx)=lambda^(1-alpha)S_infinity(x). For a scalar f, the chain rule and the curl identities give

curl((f composed with M)x)=Q^T [curl(f x)] composed with M,
curl curl((f composed with M)x)=lambda Q^T [curl curl(f x)] composed with M.

Applying these identities to T_infinity and S_infinity proves

U_infinity(Mx)=lambda^(-alpha)Q U_infinity(x),
DU_infinity(Mx)=lambda^(-alpha-1)Q DU_infinity(x)Q^T.

The second identity follows by differentiating the first with respect to x with M fixed. In particular, choose lambda=r and x=R_(kappa log r)n to obtain

U_infinity(rn)=r^(-alpha) R_(-kappa log r) U_infinity(R_(kappa log r)n).

Thus the Jacobian at rn is r^(-alpha-1) times the orthogonal conjugate of the unit-radius Jacobian at the rotated argument. Its squared trace is invariant under this conjugation. Consequently

f_infinity(rn)=r^(-2alpha-2) f_infinity(R_(kappa log r)n).

Changing azimuthal variables in the spherical coefficient multiplies it by exp(i m kappa log r), which proves the first coefficient identity. Differentiating it uses alpha_c=-1/c^2, alpha_w=0, kappa_c=-w/c^2, kappa_w=1/c and proves the next two identities. Differentiation under the sphere integral is valid because the integrand is C1 on a compact sphere and all harmonic sums are finite.

The convention for the phase is essential. Reversing the rotation sign in the representation reverses all occurrences of i m kappa. The code must check this identity on an independent radius before using it.

## Exact exterior integrals

Let a>0 be the start of a final radial interval. For a real integration power b and a mode m, put

E=b-2alpha-1+i m kappa.

Assume Re E<0. For complex numbers A,B, the absolutely convergent integral is

integral_a^infinity s^b s^(-2alpha-2+i m kappa)(A+B log s) ds
  = I0 [A+B(log a-1/E)],
I0=-a^E/E.

Proof. For real s>0 use s^E=exp(E log s). The derivative of s^E/E is s^(E-1). The condition Re E<0 implies s^E tends to zero at infinity, so the integral of s^(E-1) is -a^E/E. The antiderivative of s^(E-1)log s is s^E(log s/E-1/E^2); its value at infinity is also zero because s^(Re E)log s tends to zero. Evaluating the two antiderivatives at a proves the formula, including absolute convergence.

For the unweighted leading source use A=A_lm,B=0. For a parameter source use A=A_p,lm,B=B_p,lm. The monopole and dipole moments use b=l+2 with l=0,1. Their exponents have real parts 1-2alpha and2-2alpha, strictly negative since alpha>1. Exterior Newton integrals use b=1-l, whose exponent has real part -l-2alpha<0 for every l>=0. The origin pressure and gradient use b=1 and b=0. These therefore all converge under the stated parameter range.

## Subtraction identity and numerical scope

Let a true projected source F_lm(s) have the convergent moment integral under consideration. Subtract the exact leading source L_lm(s)=s^(-2alpha-2+i m kappa)(A+B log s) only for s>a. Then

integral_0^infinity s^b F_lm(s) ds
 =integral_0^a s^b F_lm(s) ds
  +integral_a^infinity s^b [F_lm(s)-L_lm(s)] ds
  +I0[A+B(log a-1/E)].

This is algebraic equality of absolutely convergent integrals. It changes neither a source moment nor a pressure boundary condition, and it imposes no zero moment. In numerical use the first two integrals still have angular and radial quadrature error. Projecting A and A_p by angular quadrature adds its own error. All raw moments must therefore remain diagnostics. The theorem gives no floating-point error bound or convergence rate for a particular quadrature; those require separate checks.

Dependencies: finite potential representation and its smoothness/decay; Cartesian field reconstruction; elementary homogeneity, rotation equivariance of curl, and integration of complex powers on the positive real axis. No formal proof assistant or numerical result is a premise.
