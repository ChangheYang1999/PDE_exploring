# Derivatives of transported and fitted characteristic outputs

## Scope and exact assumptions

This packet distinguishes two finite-cutoff maps before comparing their numerical derivatives. Fix beta>2, lambda, a0 and the fixed source. Let z be a finite vector of active coefficients of G=Omega/x and let q be its center-strain functional. The velocity uses the affine projection

 Pz=z+q(1+beta/2-lambda*c_f-q^T z)/(q^T q),
 D=I-q q^T/(q^T q).

The whole-plane relative inverse is linear, so a coefficient perturbation v changes the velocity by the canonical relative field Z_v=V[Omega_(Dv)]. No harmonic strain or independent drift is added. Let W_z be C^2 along all trajectories used below. Assume every backward trajectory from each point under consideration hits the circle of radius delta at a finite time T_z and the outward flux at that hit is nonzero. The initial point is outside the circle and |Y(s)|>delta for 0<=s<T_z, excluding an earlier tangential contact; this and nonzero hit flux make the local first-hit branch differentiable. Boundary data are C^2 in their spatial variables and differentiable in z with the mixed derivatives needed below. The fixed source enters W additively and independently of z. These assumptions concern the finite-cutoff problem, not the cutoff limit or a global B2 solution.

For the raw (unfitted) characteristic temperature t_z(X), let B_z(X) be the transported vorticity boundary contribution and define the linear forcing operator

 K_z f(X)=integral_0^{T_z(X)} exp(-s) partial_x f(phi^z_(-s)(X)) ds.

The raw coupled vorticity is M_z=B_z+K_z t_z. Let Q_F be a fixed linear fit-and-evaluate operator for temperature, and Q_G a fixed linear fit-and-evaluate operator for vorticity. The corresponding fitted map is N_z=Q_G[B_z+K_z Q_F t_z]. A fit for F=Theta/x^2 defines Q_F on Theta by dividing at the fit points, fitting the divided coefficients with the stated weights and then multiplying by x^2. A fit for G analogously defines Q_G. Their definitions include the sample locations, active basis and pseudoinverse convention. We assume these fixed operators are bounded on the finite collections and function spaces used. The weights, sample locations, basis, active set and pseudoinverse rank are independent of z. Fit locations have x nonzero. We assume t_z has two spatial derivatives along the paths and the mixed parameter/spatial derivatives needed for partial_x dot(t). No identity between N and M is presumed.

## Exact difference of the derivatives

At a point where these maps are differentiable, write a dot for differentiation in direction v. Then

 dot(M)=dot(B)+dot(K)t+K dot(t),
 dot(N)=Q_G[dot(B)+dot(K)Q_F t+K Q_F dot(t)],
 dot(N)-Q_G dot(M)=Q_G[dot(K)(Q_F-I)t+K(Q_F-I)dot(t)].

To prove this, differentiate the defining expressions. Q_F and Q_G are fixed linear maps at fixed beta and basis, so they commute with the parameter derivative. Apply the product rule to K_z t_z. Subtract the two resulting equations and collect the terms. Consequently the exact pointwise identity is

 dot(N)-dot(M)=(Q_G-I)dot(M)+Q_G[dot(K)(Q_F-I)t+K(Q_F-I)dot(t)].
 If the boundary prescription or trajectory discretization differs, its derivative difference supplies further terms. The calculation is an identity, not an error estimate: a bound requires control of each fit error and of K and its derivative.

For completeness, at fixed terminal X the backward path Y(s)=phi^z_(-s)(X) and its derivative p satisfy Y'=-W_z(Y), p'=-DW_z(Y)p-Z_v(Y), p(0)=0. If n is the outward unit normal at S=Y(T), differentiation of |Y(T)|=delta gives dot(T)=n.p(T)/(n.W_z(S)); dot(S)=p(T)-W_z(S)dot(T). Applying the product and chain rules to K gives

 dot(K)f=exp(-T) partial_x f(S) dot(T)
          +integral_0^T exp(-s) grad(partial_x f)(Y(s)).p(s) ds

when f itself is held fixed. For boundary traces theta_b(z,S) and omega_b(z,S), the temperature and vorticity boundary terms are

 t_z=exp((beta-2)T)theta_b(z,S), B_z=exp(-T)omega_b(z,S).

Thus, with the parameter held fixed in each spatial gradient,

 dot(t)=exp((beta-2)T)[(beta-2)theta_b dot(T)+partial_z theta_b[v]+grad(theta_b).dot(S)],
 dot(B)=exp(-T)[-omega_b dot(T)+partial_z omega_b[v]+grad(omega_b).dot(S)].

Here dot(S) is tangent to the circle since n.dot(S)=0, so any smooth extension of the boundary traces gives the same tangential term. These formulas justify the preceding product rule under the stated smoothness and non-grazing transversal-hit assumptions. They concern the leading-jet map when applied to P212/P213; derivatives of NUM higher boundary jets are additional terms.

## Linearity and finite differences

The variational path equation and its initial condition are linear in Z_v. Since v maps linearly to Z_v, p, dot(T), dot(S) and every differentiated transport variable are linear in v. Uniqueness for linear ordinary differential equations proves dot(M)[v1+v2]=dot(M)[v1]+dot(M)[v2]. The same is true for the fitted derivative under fixed Q_F and Q_G. A floating-point check of this identity is a consistency test, not a derivative-error bound.

For a scalar f in C^5 on [-2h,2h], its four-point centered derivative is [f(-2h)-8f(-h)+8f(h)-f(2h)]/(12h). Let P be the degree-at-most4 interpolant at -2h,-h,0,h,2h. Its derivative at0 is this stencil. Put C=(f'(0)-P'(0))/(4h^4). Then f-P-C x(x+2h)(x+h)(x-h)(x-2h) vanishes at the five nodes and has derivative zero at0. Repeated Rolle's theorem, counting the double zero at0, gives a point xi with f^(5)(xi)=120C. Therefore f'(0)-P'(0)=h^4 f^(5)(xi)/30, proving the absolute bound h^4 sup|f^(5)|/30. If each sampled value has error at most e, the derivative error from those values is at most 3e/(2h), by the sum of the absolute stencil weights. These conditional estimates explain why reducing h can increase numerical noise. We do not assume a C^5 parameter bound for a piecewise C^2 velocity interpolant or know e for the numerical solves. Comparing several h and solver tolerances therefore yields numerical observations only.

## Application to the stored comparison

P210 and P212 use their own whole-plane inverse and raw transported temperature gradient. Source inspection on 2026-10-21 shows that NUM's saved map first fits the transported temperature, differentiates that fitted temperature in its vorticity integral, and then fits the resulting G. It uses higher local boundary jets and fixed time steps, while P210/P212 use an event at exactly delta, leading boundary jets and compatible transported gradients. Projection, fixed amplitude and active output coefficients agree in meaning, but the maps differ by the explicitly described fitting and discretization operations. The measured gaps must therefore be described as gaps between these numerical procedures. They do not directly establish an error in the saved Jacobian of NUM's own discrete map.

The next controls compare zeroth-order outputs, the projected-direction array identity, analytic linearity and parameter differences at larger steps and tighter tolerances. The base-point coefficient hash and input parameters are checked separately. No fit-error bound, exact derivative enclosure, isolated nonlinear fixed point, fold, unforced profile or full B2 endpoint follows from these controls.

Dependencies: P198 (scaling and projection), P205 (physical Gram), P208 (saved array), P210 (finite-cutoff reconstruction), P212 (moment inverse and analytic moving-hit derivative). Source inspection is recorded with hashes and frozen excerpts, not by importing or running NUM modules.
