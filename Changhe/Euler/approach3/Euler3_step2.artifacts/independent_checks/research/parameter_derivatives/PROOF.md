# Parameter derivatives at fixed coefficient coordinates

Status: proved identities under the hypotheses below. These identities do not establish that any saved state solves Euler, or that any implementation differentiates them correctly.

## Statement and notation

Let A be an open subset of R^N, let Θ be an open subset of (2/5,1/2) × (0,∞), and write θ = (c,ω). Fix R0 > 0. Suppose the scalar potentials T(a,θ,y) and S(a,θ,y) have continuous parameter derivatives and all spatial derivatives needed below, with commuting mixed derivatives. Set

U = curl(T y) + curl curl(S y),

J = [[0,-1,0],[1,0,0],[0,0,0]],

W = c y - ω J y + U,

R = (1-c)U + DU W + ω J U + ∇P.

Here (DU)ij = ∂j Ui, so DU W = (W·∇)U. Parameter derivatives hold a and y fixed. Assume P is C1 in θ and that its parameter derivative commutes with ∇. A sufficient full-space pressure hypothesis and its proof are given in `../pressure_consistency/PROOF.md`.

Then

∂c R = -U + (1-c)Uc + DU(y+Uc) + DUc W + ω J Uc + ∇Pc,

∂ω R = (1-c)Uω + DU(-Jy+Uω) + DUω W + J U + ω J Uω + ∇Pω.

The envelope exponent α=(1-c)/c and smooth twist ψ=ω log(1+|y|²/R0²)/(2c) satisfy

αc=-1/c², ψc=-ω log(1+|y|²/R0²)/(2c²), ψω=log(1+|y|²/R0²)/(2c).

All parameter derivatives Uc,Uω are divergence free. Their values are obtained by applying the same two curl operators to Tc,Sc or Tω,Sω.

## Proof

The coordinate y and the matrix J are independent of θ. Differentiating the definition of W therefore gives Wc=y+Uc and Wω=-Jy+Uω. Componentwise, (DU W)i=Σj (∂j Ui)Wj. Its parameter derivative is Σj(∂j Upi)Wj + Σj(∂j Ui)Wpj, which is DUp W + DU Wp. Differentiating each remaining term in R gives precisely the two displayed identities. In particular, ∂ω(ωJU)=JU+ωJUω. The term JU is present even if the represented field happens to be parameter independent.

Since α=1/c-1, its derivative is -1/c². The logarithm in ψ is constant under either parameter derivative, giving the two stated twist derivatives. Spatial and parameter derivatives commute by hypothesis, so parameter differentiation commutes with each curl. The divergence of each curl vanishes by equality of mixed spatial partial derivatives. This proves the assertions about Up.

## Explicit envelope and angular derivatives

Write s=(1+|y|²/R0²)^(1/2). Let an envelope be E=s^(-mα-b), where m,b are parameter independent and m may be 0. Then

Ec=(m/c²) log(s) E, Eω=0.

For a real cosine/sine pair at azimuthal order k, let

Hc(ψ)=hc cos(kψ)-hs sin(kψ),
Hs(ψ)=hs cos(kψ)+hc sin(kψ).

For either parameter p, ∂p Hc=-k ψp Hs and ∂p Hs=k ψp Hc. These signs refer to the actual field evaluated at φ+ψ; rotating coefficient pairs uses the inverse rotation and hence the opposite sign convention. A test must compare like conventions.

The leading toroidal and poloidal envelopes have m=1; the existing nonlinear B and D correction envelopes have m=2. Their derivative contribution is twice the leading exponent contribution at the same s. An untwisted E correction whose exponent and coefficients are independent of c,ω has zero parameter derivative at fixed coefficient coordinates. Its contributions to U, DU, and the cross terms in tr((DU)²) still participate in the pressure derivative. Chebyshev maps, R0, R1 and the core damping power are held fixed in this campaign.

## Derivative of the complete least-squares loss

Let a differentiable real residual vector be b(X), let A(X) be a differentiable matrix of weights or normalization, and let g(X) contain differentiable gauge or penalty rows. Define v(X)=(A(X)b(X),g(X)) and L(X)=||v(X)||²/2. Then

vp=(Ap b + A bp, gp),
Lp=(A b)·(Ap b+A bp)+g·gp=v·vp.

This follows by the matrix product rule and ∂p(v·v)=2v·vp. It applies to rectangular A and to weights depending on coefficients as well as on c,ω. A scalar normalization b/d, for d>0, has derivative bp/d-b dp/d². Omitting dp differentiates a lagged surrogate, not the stated loss.

For the momentum weight s^α, its logarithmic derivative is -log(s)/c² in the c direction and zero in the ω direction. The weight s^(1/c) on vorticity has the same logarithmic derivative. This is separate from the parameter derivatives of the underlying field and pressure.

For the leading-tail gauge, let l,k label a real spherical harmonic and let t=R0^(α+l)Σj Aj and q=R0^(α+l-1)Σj Cj. Define λ=l(l+1), κ=ω/c and B=λ²+λ[(2-α)²+k²κ²]. The mode energy is λ t²+Bq². At fixed coefficients,

tc=αc log(R0)t, qc=αc log(R0)q,
B_c=λ[-2(2-α)αc+2k²κ(-ω/c²)], B_ω=2λk²κ/c.

Thus the c derivative of the energy is 2λttc+B_cq²+2Bqqc, and its ω derivative is B_ωq². Summing modes gives the derivative of the squared tail norm. This calculation includes R0≠1.

If a solver rescales coefficients, phase-aligns a field, or maps unconstrained coordinates into physical parameters before evaluating the loss, the derivative of that operation must also be included. For c=0.4+0.1 sigmoid(z), dc/dz=0.1 sigmoid(z)[1-sigmoid(z)], and for ω=exp(w), dω/dw=ω. Small transformed gradients can therefore coexist with non-small physical gradients near a boundary. At switches of max/min, clipping, pivot selection, or rank selection, a classical derivative need not exist; either test within a fixed smooth branch with a stated margin, or report directional derivatives and the switch explicitly.

## Dependencies and scope

Only the product rule, commuting mixed derivatives, and the divergence-of-curl identity are used for the momentum statements. Pressure differentiation additionally uses the dominated-convergence and decay argument in the companion proof. All statements are continuous identities. No assertion here validates angular tables, source interpolation, adaptive quadrature, a fixed-parameter kernel, or an optimizer stopping criterion.
