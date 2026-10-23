# Bounded features and the first unwanted tail power

Date: 2026-10-23. Status: proved expansion under the stated smoothness and representation assumptions. This is a representation audit, not an existence or nonexistence theorem for Euler profiles.

## Statement and hypotheses

Let 0.4<c<0.5 and d=1-1/c, so -3/2<d<-1. Set the axial drift C=0. Let l_in,l_env>0. Suppose the learned potential has a leading term

    A_lead(y) = (1+R²/l_env²)^((d+1)/2) F(xi,tau),
    xi = y/sqrt(l_in²+R²),  tau = R²/(l_in²+R²),  R=|y|,

where F is a smooth vector function on a neighborhood of {(n,1):n∈S²}. A finite tanh network satisfies this assumption. F may already include the linear Q-symmetry projection. Add the prescribed seed potential and a second smooth bounded-feature term with potential degree 2d. Let the pressure be the prescribed seed pressure plus analogous bounded-feature terms of degrees 2d and 3d-1. Assume their envelope shifts are zero, as in the audited v2 configuration.

Then there are smooth angular vector coefficients B_0,B_2,B_N such that the velocity U=curl A has a differentiable uniform angular expansion

    U(Rn) = R^d B_0(n) + R^(d-2) B_2(n)
            + R^(2d-1) B_N(n) + o(R^(2d-1)).

The coefficient B_2 is not removed merely by adding the degree-2d potential term. If U,P are an exact Euler profile in this representation, B_2 must vanish identically. More generally the momentum residual satisfies

    R^(-(d-2)) R_m(Rn) -> -2c B_2(n)

uniformly on S². If B_2 is nonzero, the full-term-normalized residual can decrease like R^-2 while the residual divided by the natural nonlinear power R^(2d-1) grows like R^(1/c-2).

Dependencies: Taylor expansion on a compact set, differentiation of homogeneous fields, and the profile equation in ../profile-identities/PROOF.md. Seed definitions and expansion are in ../seed-family/PROOF.md. No formal verification or exterior numerical enclosure is claimed.

## Expansion of the leading learned potential

Write a=d+1. Uniformly in n∈S² as R tends to infinity,

    xi = n - (l_in²/(2R²))n + O(R^-4),
    tau = 1 - l_in²/R² + O(R^-4),
    (1+R²/l_env²)^(a/2)
        = l_env^(-a) R^a [1 + a l_env²/(2R²) + O(R^-4)].

Taylor expansion of F at (n,1) gives

    A_lead(Rn) = R^(d+1) A_0(n) + R^(d-1) A_2(n) + O(R^(d-3)),

where

    A_0(n) = l_env^(-a) F(n,1),
    A_2(n) = l_env^(-a) [a l_env² F(n,1)/2
                 - l_in² (n·grad_xi)F(n,1)/2
                 - l_in² partial_tau F(n,1)].

All remainders needed here can be differentiated in physical coordinates because F is smooth on a fixed neighborhood of the compact boundary. One derivative lowers the radial degree by one. Thus curl A_lead has degrees d, d-2, and a remainder O(R^(d-4)).

The prescribed seed has

    A_seed(Rn) = -R^(d+1) [1 - 1/(2cR²) + O(R^-4)] (n×Mn)/3.

It contributes to the same two leading potential degrees and hence the same velocity degrees d and d-2. The total B_2 is the curl coefficient of the sum of the seed and learned degree-(d-1) potentials. Only that curl coefficient must cancel. Requiring the potential coefficient itself to vanish would unnecessarily fix a gauge.

The second envelope has potential degree 2d. The same Taylor argument gives velocity degree 2d-1 and next correction degree 2d-3. Since -3/2<d<-1,

    d > d-2 > 2d-1 > d-4,
    2d-3 < 2d-1.

These inequalities prove the stated ordered expansion of U. The pressure has leading degree 2d and its gradient has degree 2d-1. The seed pressure has that same leading degree. All its even inverse-radius corrections are lower order.

## Necessary cancellation in the Euler equation

The linear dilation operator L_c W=(1-c)W+c(y·grad)W multiplies a homogeneous field of degree k by 1-c+ck. In particular,

    L_c(R^d B_0)=0,
    L_c(R^(d-2) B_2)=-2c R^(d-2) B_2,
    L_c(R^(2d-1) B_N)=-R^(2d-1) B_N.

The nonlinear term (U·grad)U starts at degree 2d-1 and grad P also starts there. Because d-2>2d-1, neither can cancel the degree-(d-2) linear residual. Dividing the exact equation by R^(d-2) and taking R to infinity proves B_2=0. The same calculation for an arbitrary represented approximation proves the residual limit in the statement.

If B_0 and B_2 are nonzero, a full-term sum typically has order R^d, giving relative residual order R^-2. Relative to the natural nonlinear power, the exponent difference is

    (d-2)-(2d-1) = -d-1 = 1/c-2 > 0.

When a particular nonlinear denominator vanishes or has extra cancellations, its ratio can be even larger or undefined. The power statement does not assume a positive lower bound for that denominator.

## Scope for the campaign

Bounded features allow a smooth nonconstant angular leading coefficient and avoid the generic saturation defect of dir_log. The explicit second envelope supplies the fractional nonlinear correction that a smooth function of bounded xi,tau alone cannot generally supply. Both improvements are real. They still leave a necessary cancellation of the seed-plus-network velocity coefficient B_2. A finite training radius or a small linear-relative tail residual does not certify that cancellation.

For C!=0, the drift term C partial_z U introduces another earlier power. The present statement assumes C=0 and makes no claim about that case. Nonzero envelope shifts require a new ordering of powers. No universal approximation theorem for this architecture is asserted.
