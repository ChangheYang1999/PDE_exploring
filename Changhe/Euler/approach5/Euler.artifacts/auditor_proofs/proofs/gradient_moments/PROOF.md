# Gradient moments and the restricted Euler model

## Statement

Let U in C2(R3;R3), P in C1(R3) be a divergence-free rotating Euler profile, with finite real c and omega. Write G=DU, S=(G+G^T)/2, K=(G-G^T)/2 and Omega=curl U. Let mu be a compactly supported B-invariant probability, where B=(cI-omega J)y+U. Then

    integral Omega dot S Omega = integral |Omega|^2,       (V1)
    integral S:D2P
       = -integral (|S|^2+tr S^3+|Omega|^2/4).            (V2)

In particular integral |S|^2 |Omega|^2 >= (3/2) integral |Omega|^2. No decay or restriction on rotation is used.

The damped restricted Euler matrix equation

    Ghat'=-Ghat-Ghat^2+(tr Ghat^2/3)I

has, for every w>0, the trace-free vortical equilibrium

    Gstar=diag(1,s2,s3)+(w/2)(e3 e2^T-e2 e3^T),
    s2=(-1+sqrt(9+w^2))/2,
    s3=(-1-sqrt(9+w^2))/2.

It satisfies tr Gstar^2=6, -det Gstar=2, and the algebraic forms of V1-V2 with the isotropic pressure Hessian -2I. This is a matrix-model statement, not a spatial Euler profile construction.

## Exact differentiation

For a general C2 divergence-free U define F=-[(1-c)U+GB+omega JU]. Differentiation gives

    B dot grad G+G+G^2+omega[J,G]+DF=0,
    B dot grad Omega=(G-I-omega J)Omega-curl F.

Consequently

    B dot grad(|Omega|^2/2)=Omega dot(S-I)Omega-Omega dot curl F,
    B dot grad(|S|^2/2)
       =-|S|^2-tr S^3-(Omega dot S Omega)/4-S:DF.          (4)

For (4), use K^2=(Omega Omega^T-|Omega|^2 I)/4, tr S=0 and S:[J,S]=0. The contraction with DF uses only its symmetric part.

If Q=-tr G^2/2, direct differentiation and cyclicity of trace give

    B dot grad Q=-2Q+tr G^3+tr(G DF),
    tr G^3=tr S^3+(3/4)Omega dot S Omega.                 (5)

For a profile, F=grad P and P is C2, so curl F=0 and DF=D2P. All functions being integrated are C1 and bounded on the compact invariant support. Integrating their orbit derivatives gives zero. The vorticity equation proves V1, and (4) followed by V1 proves V2.

For the weighted inequality, put W=integral |Omega|^2. If W=0 the assertion is immediate. Otherwise V1 and Omega dot S Omega<=lambda_max(S)|Omega|^2 give integral lambda_max(S)|Omega|^2>=W. Cauchy-Schwarz with weight |Omega|^2 gives integral lambda_max(S)^2 |Omega|^2>=W. The trace-free symmetric matrix inequality |S|^2>=(3/2)lambda_max(S)^2 then gives the claim.

## The coefficient in the Q relation

Let E1=integral(Omega dot S Omega-|Omega|^2), and let E2 be the displayed V2 moved to its left side:

    E2=integral[S:D2P+|S|^2+tr S^3+|Omega|^2/4].

Then integrating the right side of (5) gives E2+(3/4)E1, not E2+(1/2)E1. The coefficient 1/2 is correct if E2 is instead the unreduced strain moment from (4), with Omega dot S Omega/4 before V1 has been substituted. Either convention proves that Q adds no independent relation. The numerical coefficient must track which convention is used.

## Restricted Euler equilibrium

For an actual profile along an orbit, Q_t=exp(omega Jt) gives Ghat(t)=Q_t G(Phi_t x)Q_t^T and Hhat=Q_t D2P(Phi_t x)Q_t^T. The commutator cancels, so

    Ghat'=-Ghat-Ghat^2-Hhat,
    tr Hhat=-tr Ghat^2.

Replacing Hhat by its isotropic part produces the stated matrix model. In Gstar the lower 2 by 2 block has trace -1 and determinant

    s2 s3+w^2/4=(-2-w^2/4)+w^2/4=-2.

Cayley-Hamilton therefore gives Gstar^2+Gstar=2I. Hence it is an equilibrium, tr Gstar^2=6 and det Gstar=-2. Its curl vector is (w,0,0), and its strain eigenvalue in that direction is 1. Also

    |Sstar|^2=6+w^2/2,
    tr Sstar^3=-6-3w^2/4,
    Sstar:(-2I)=0.

These give V1 and V2 exactly. No numerical computation is needed.

## Scope

V1 also holds with an independent transported eigenfield W replacing Omega, because the same norm equation follows from [B,W]=-(1+c)W. V2 uses the actual momentum gradient and pressure Hessian. The isotropic closure omits the nonlocal deviatoric pressure Hessian, so its equilibrium neither proves nor disproves existence of a spatial decaying profile.

This confirms the substantive identities and model assertion in Theory Agent A C17, with the stated Q-coefficient clarification. Compact support of the invariant probability is part of the hypotheses; unrestricted invariant measures would need integrability and justification of the generator identities.
