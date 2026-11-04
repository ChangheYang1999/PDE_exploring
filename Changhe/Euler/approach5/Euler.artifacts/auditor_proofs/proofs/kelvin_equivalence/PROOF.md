# The full Kelvin circulation law is equivalent to the profile momentum equation

## Exact statement

Let O be a connected open subset of R3, U in C2(O;R3), c and omega finite real constants, A=cI-omega J, B=Ay+U and q=|U|^2/2. Let Phi be the local B flow. The following are equivalent:

1. There is a single-valued P in C1(O) satisfying

       (1-c)U+(B.grad)U+omega JU+grad P=0.

2. For every closed piecewise C1 curve gamma in O, and every sufficiently small flow time for which its image remains in O,

       integral_(Phi_t gamma) U.dy
          =exp((2c-1)t) integral_gamma U.dy.

The equivalence does not need div U=0. Adding that separate condition makes this the full divergence-free Euler profile system. No decay or completeness is required.

## Proof

Write beta=U.dy. The Lie derivative of this one-form is

    L_B beta=[(B.grad)U+(DB)^T U].dy
            =[(B.grad)U+cU+omega JU+grad q].dy,

because A^T=cI+omega J and (DU)^T U=grad q. Thus the momentum equation is equivalent to

    L_B beta-(2c-1)beta=d(q-P).                           (1)

If P exists, differentiating a material circulation and using the fact that the integral of an exact form around a closed curve is zero gives the scalar differential equation C'(t)=(2c-1)C(t). This proves statement2 on each interval of existence.

Conversely, differentiate statement2 at t=0. Every closed curve has zero integral of the C1 one-form

    eta=L_B beta-(2c-1)beta.

Fix a base point in O. The integral of eta along a piecewise C1 path to y is independent of the path, since the difference of two paths is a closed curve. It defines a single-valued primitive F with dF=eta. Put P=q-F. Equation(1) then gives statement1.

If one assumes the circulation law only for contractible curves, the conclusion is local exactness and a closed form eta; nontrivial periods may still prevent a single-valued pressure on a multiply connected O. The all-closed-curves formulation removes this obstruction.

## Consequence for the model audit

A divergence-free decaying U that fails the profile equation for every pressure cannot satisfy this full circulation law for its own carrier B. An independent field W obeying [B,W]=-(1+c)W supplies its own transported two-form. It does not make the actual one-form U.dy satisfy (1) when W differs from curl U.

The zero-circulation condition on individual periodic carrier orbits is a much weaker necessary test. Local exact examples with one such orbit show consistency only for those examples. They do not prove that all periodic orbits of a regular attracting model can simultaneously satisfy that condition. In this campaign, realizability of that weaker condition on an entire regular attractor remains open in Theory Agent C C27/F17.

Thus the report's final list of quantities supposedly satisfied by the regular kinematic model or by a smooth decaying non-profile cannot literally include the full Kelvin law. Nor should it dismiss the all-periodic-orbits test without the missing realization result. This is a correction to the claimed scope of the obstruction analysis, not a nonexistence proof.
