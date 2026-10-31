# Splitting the complete residual derivative by row block

Status: proved as a finite-dimensional identity under the hypotheses below. The implementation comparison is separate and initially pending.

The full reverse-over-reverse derivative constructs a graph for every momentum row even though only the closure target needs nested reverse differentiation. Evaluating those two row sets separately gives the same derivative and permits their temporary graphs to be released separately.

## Statement and notation

Let O be open in R^n, let q0 belong to O, and let E:O -> R^N be continuously differentiable. The map E includes the reduced-to-full coefficient map and the two optimizer-to-physical parameter maps. Let R:O -> R^m be a continuously differentiable residual and C a fixed set of closure row indices. Let S_C:R^m -> R^k select those rows, in their original order, and let I_C:R^k -> R^m insert a vector in C and put zero elsewhere. Thus S_C I_C is the identity on R^k.

Suppose W:O -> R^m is continuously differentiable, agrees with R in every row outside C throughout O, and uses frozen closure target and frozen pattern data in C. Suppose H:O -> R^k is the closure residual with its target and target norm recomputed but its pattern matrix frozen at the q0 value. Suppose V:O -> R^k has derivative at q0 equal to the missing explicit pattern contribution. More precisely, assume

    D(S_C R)(q0) = DH(q0) + DV(q0).

Then for every direction v in R^n,

    DR(q0)v = (I - I_C S_C) DW(q0)v
              + I_C [DH(q0)v + DV(q0)v].

There is no error constant in this identity. In particular the Euclidean norm of its right side equals ||DR(q0)v||_2, the quantity in the registered gradient-test floor.

For the campaign closure, write p(q)=(c_l(q),omega(q)), let a(q) be the coefficient vector after E, and write

    S_C R(q) = lambda/N(q) times w * [M(p(q)) b(a(q),p(q)) - G(q)],

where multiplication by the fixed row weights w is componentwise. Assume M,b,G,N are continuously differentiable near q0 and N(q)>0 there. In H replace only M(p(q)) by M(p(q0)). Then

    DV(q0)v = lambda/N(q0) times w *
              [DM(p(q0))[Dp(q0)v] b(a(q0),p(q0))].

The factors lambda and w may be any fixed real scalar and fixed vector of the required dimensions. No invertibility or rank assumption is needed.

## Proof

For a row outside C the functions R and W agree on the open set O, so their directional derivatives agree. The operator I-I_C S_C keeps precisely these rows and zeros the closure rows. On C the assumed derivative decomposition gives DH(q0)v+DV(q0)v. Inserting this vector fills precisely the removed entries and proves the displayed identity.

For the specified closure form, differentiate the product of lambda/N(q), the fixed weights, and the bracketed expression. Freezing M changes none of the derivatives of N, b or G. Their coefficients at q0 remain the same because M(p(q0)) has the same base value in both residuals. The sole missing term is the derivative of M composed with p, multiplied by the base b and lambda/N and the fixed weights. This is the displayed expression for DV. The formula includes any parameter dependence of a through E in DH; no fixed-full-coefficient substitution is made. The equality of Euclidean norms follows from equality of the vectors.

## Application, dependencies and scope

W is production residual_vector_wd composed with E, with pressure tables rebuilt and differentiated and nonlinear weights differentiated. H is production closure_rows composed with E after first_correction_graph supplies G and its norm, with the stored pattern matrix. The two physical pattern columns are multiplied by Dp(q0)v. Finite differences approximate those two pattern columns in the implemented audit, exactly as in its earlier full-graph route; this theorem does not bound that finite-difference error.

The fixed-active-set assumption is needed for continuous differentiability of the nonlinear max, median and clamp operations. A positive target norm is also required. Both are checked at sampled stencil points in the numerical audit, which cannot prove differentiability between those samples. The identity uses only the finite-dimensional chain and product rules. It does not establish pressure accuracy, global smoothness, or the validity of an Euler profile. No formal proof or Lean/Lake build is attempted.
