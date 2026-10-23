# A continuous angular far-field limit

Status: independently derived; adversarially reviewed by the actual claude-opus-5-5 endpoint, then checked again by the verifier. The argument below proves a continuous leading angular limit. A smooth expansion with a second term is stated only conditionally.

## Statement

Let W be a smooth vector field on R^2 with

    div W=2c_l,  W(X)=c_l X+O(|X|^gamma),
    c_l>1,  0<gamma<1.

Let rho be smooth and satisfy W.grad rho=rho. Then there is a continuous 2pi-periodic function Theta0 such that, with p=1/c_l,

    sup_theta |r^-p rho(r,theta)-Theta0(theta)| -> 0 as r->infinity.

The assertion uses no bound on high derivatives of W at infinity. For a primary IPM profile, Theta0(pi/2)=K!=0 from ../scaling/PROOF.md. Consequently rho=O(r^p) globally. This is an exact conclusion for a hypothetical exact profile, not evidence that such a profile exists.

## Radial parametrization of trajectories

Write V=W.e_r and Q=W.e_theta. Choose R large enough that V(r,theta)>=c_l r/2 for r>=R. For each initial angle alpha, let theta(r,alpha) solve

    d theta/dr = Q(r,theta)/(r V(r,theta)),  theta(R,alpha)=alpha,

using a lift to the real line. Smoothness gives a smooth circle diffeomorphism for each finite r. The bound Q=O(r^gamma) implies |d theta/dr|<=C r^(gamma-2), uniformly in alpha. Thus theta(r,alpha) has a uniform limit theta_infinity(alpha), with an error O(r^(gamma-1)). The lift satisfies theta(r,alpha+2pi)=theta(r,alpha)+2pi.

Put

    tau(r,alpha)=integral_R^r 1/V(s,theta(s,alpha)) ds,
    H(r,alpha)=tau(r,alpha)-p log(r/R).

Since 1/V-p/r=O(r^(gamma-2)), H converges uniformly to a continuous function H_infinity.

## The angular Jacobian cannot collapse

Set J=partial_alpha theta. Differentiating the angular ODE gives

    d log J/dr = partial_theta [Q/(rV)].

The polar divergence identity is partial_r V+V/r+partial_theta Q/r=2c_l. Substitution and the chain rule along the trajectory yield

    partial_theta [Q/(rV)]
       =2c_l/V - 1/r - d log(V(r,theta(r,alpha)))/dr.

Since J(R,alpha)=1, integration gives the exact identity

    J(r,alpha)= R V(R,alpha) exp(2c_l tau(r,alpha))
                  / [r V(r,theta(r,alpha))]
       = [V(R,alpha)/(c_l R)] [c_l r/V(r,theta(r,alpha))]
           exp(2c_l H(r,alpha)).

The middle factor tends uniformly to 1. It follows that J has a uniform positive continuous limit

    J_infinity(alpha)=V(R,alpha) exp(2c_l H_infinity(alpha))/(c_l R).

Uniform convergence of theta and its first derivative proves that theta_infinity is C^1 with derivative J_infinity>0. Its lift has degree one. Therefore it is a C^1 circle diffeomorphism, with a uniformly continuous inverse. This step avoids assuming any integrable bound on DW.

## Transported amplitude

The profile equation along the radially parametrized trajectory gives

    rho(r,theta(r,alpha))=exp(tau(r,alpha))rho(R,alpha).

Consequently

    r^-p rho(r,theta(r,alpha))
       =R^-p exp(H(r,alpha))rho(R,alpha)
       -> A_infinity(alpha):=R^-p exp(H_infinity(alpha))rho(R,alpha)

uniformly in alpha. Define Theta0=A_infinity composed with theta_infinity^-1. Since the finite-r angular inverse converges uniformly to theta_infinity^-1, uniform continuity of A_infinity proves the asserted convergence at fixed physical angle. No rate at fixed angle follows from this last step without a modulus of continuity for A_infinity.

For a primary profile the positive y-axis is invariant, so theta(r,pi/2)=pi/2. The limit there is the nonzero K proved in the axis result. Boundedness of the continuous Theta0 and uniform convergence give rho=O(r^p) outside a disk; local smoothness supplies the global bound.

## What this proof does not establish

J_infinity is continuous; the argument does not bound its higher derivatives. It does not establish that Theta0 is smooth, that the rescaled velocity converges under a merely continuous density limit, or that a full asymptotic series exists. The Riesz inverse is not a bounded operator on arbitrary continuous functions in the uniform norm, so those steps cannot be inserted without estimates.

If stronger asymptotic regularity separately justifies

    rho=r^p Theta0(theta)+r^(2p-1)Theta1(theta)+o(r^(2p-1)),
    U=r^p U0(theta)+o(r^p),

with sufficient differentiated error control, then substitution into transport gives

    (1-c_l)Theta1 = -F0,

where F0(theta)=p U0_r(theta)Theta0(theta)+U0_theta(theta)Theta0'(theta) is the full coefficient of r^(2p-1) in the advective term. This is a conditional coefficient calculation. It does not supply the stronger regularity or its error control.

## Dependencies and scope

The proof uses the polar divergence formula, smooth finite-radius ODE dependence, uniform integration of r^(gamma-2), and the fundamental theorem of calculus for uniform convergence of a function and its derivative. It is valid for a general asymptotically radial field of constant positive divergence. IPM supplies that field through the canonical inverse theorem. It does not use an assumption about interior critical points, signs, or basin topology.
