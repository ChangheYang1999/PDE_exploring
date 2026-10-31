# Interior pressure moments from boundary fluxes

Status: proved conditional identities for smooth divergence-free fields. Numerical adoption is open. These identities do not set finite-radius moments to zero.

Let R>0, let U be a real C^2 vector field on an open neighborhood of the closed ball B_R in R^3, and suppose div U=0. Write a=(U dot grad)U and f=tr((DU)^2), with (DU)_ij=partial_j U_i. Let Y_lm be any orthonormal complex spherical harmonic, with regular solid harmonic H_lm(y)=|y|^l Y_lm(y/|y|), extended as a homogeneous harmonic polynomial at zero. Define

F_lm(s)=integral_{S^2} f(s n) conjugate(Y_lm(n)) dOmega(n),
I_lm(r)=integral_0^r s^(l+2) F_lm(s) ds,  0<r<=R.

Then, with H=conjugate(H_lm),

I_lm(r)=r^2 integral_{S^2} [H(rn) a(rn) dot n - (grad H(rn) dot U(rn))(U(rn) dot n)] dOmega(n)
         + integral_{B_r} sum_{i,j=1}^3 (partial_i partial_j H) U_i U_j dy.

In particular, since the Hessians of degree-zero and degree-one polynomials vanish,

I_00(r)=r^2 conjugate(Y_00) integral_{S^2} a(rn) dot n dOmega(n),

I_1m(r)=r^3 integral_{S^2} conjugate(Y_1m(n)) a(rn) dot n dOmega(n)
         -r^2 integral_{S^2} [conjugate(d_m) dot U(rn)] [U(rn) dot n] dOmega(n),

where H_1m(y)=d_m dot y for a constant complex vector d_m. These formulas give the exact finite-radius source moments, including all main and correction channels present in U.

## Proof

With repeated indices summed, div U=0 gives

partial_i a_i = partial_i(U_j partial_j U_i)
              = (partial_i U_j)(partial_j U_i) + U_j partial_j(div U) = f.

Also a_i=partial_j(U_i U_j). Polar integration gives I_lm(r)=integral_{B_r} H f. Integration by parts once gives

integral_{B_r} H partial_i a_i = integral_{partial B_r} H a_i n_i - integral_{B_r} (partial_i H) a_i.

Substitute a_i=partial_j(U_i U_j) into the last integral and integrate by parts again:

-integral_{B_r} (partial_i H) partial_j(U_i U_j)
 = -integral_{partial B_r} (partial_i H) U_i U_j n_j
   +integral_{B_r} (partial_j partial_i H) U_i U_j.

The surface element is r^2 dOmega. This proves the general formula. H_00 is constant, and H_1m is linear with gradient conjugate(d_m); their Hessians vanish. Substitution gives the two displayed special cases. All integrations are classical because U is C^2 and H is polynomial.

## Relation to full-space pressure

Suppose further that U is C^2 on R^3, div U=0, and |U(y)|<=C(1+|y|)^(-alpha), |DU(y)|<=C(1+|y|)^(-alpha-1) for constants C<infinity and alpha>1. Then f has a convergent decaying Newton potential and, for each r>0,

P_lm(r)=[r^(-l-1) I_lm(r) + r^l J_lm(r)]/(2l+1),
P'_lm(r)=[-(l+1)r^(-l-2) I_lm(r) + l*r^(l-1) J_lm(r)]/(2l+1),
J_lm(r)=integral_r^infinity s^(1-l) F_lm(s) ds.

The interior boundary formulas may replace I_00 and I_1m in these equations. J_lm is retained as the actual exterior source integral. There is no change of boundary condition and no imposed zero finite-radius or discrete total moment. This replacement is an identity for the continuous field; equivalence of finite numerical discretizations needs its own tests.

The bounds above imply |a(rn)|<=C^2(1+r)^(-2alpha-1). Thus I_00(r)=O(r^(1-2alpha)) and I_1m(r)=O(r^(2-2alpha)) as r tends to infinity. Both tend to zero under alpha>1. Their finite-radius values are generally nonzero. Computing those small values through the boundary identities avoids subtracting contributions accumulated across the entire interior ball, but does not itself bound floating-point or angular quadrature errors.

## Parameter derivatives

If U(y,p) is C^1 in a real parameter p with the required spatial derivatives jointly continuous on the closed ball, and div U(.,p)=0 on a neighborhood of the parameter value, then differentiation under these compact-domain integrals is valid. For V=partial_p U,

partial_p a=(V dot grad)U+(U dot grad)V,
partial_p f=2 tr(DU DV).

The derivative of the boundary formula follows by replacing a by partial_p a in its first term and replacing the product U_i U_j by V_i U_j+U_i V_j in the remaining terms. Full-space differentiation additionally needs the uniform decay assumptions stated in ../pressure_consistency/PROOF.md. No claim is made for discrete fields whose divergence-free identity fails or whose radial/parameter derivatives are inconsistent.

## Dependencies and scope

The proof uses two applications of the divergence theorem, the solid-harmonic definition and the full-space Green representation in ../pressure_consistency/PROOF.md. It is not a new velocity ansatz, a proof of an Euler solution, or a validated production change. Numerical evaluation must use the same full field and normalization, keep the exterior term, and independently check agreement, parameter derivatives and residual blocks before adoption.
