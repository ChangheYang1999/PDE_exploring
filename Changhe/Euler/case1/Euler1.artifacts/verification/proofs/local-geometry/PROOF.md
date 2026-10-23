# Conditional stagnation and vorticity-maximum tests

Status: proved informal conditional identities. No stagnation point or exact profile is constructed here. Dependencies: profile-identities/PROOF.md, the derivative test at a differentiable local maximum, and linear algebra. Let U be a C^2, divergence-free, Q-equivariant exact profile with c>0, C real, and V=cy+Ce_z+U.

## An axis stagnation point with nonzero vorticity

Suppose V(0,0,z_0)=0 and Omega(0,0,z_0) differs from zero. Differentiate U(Qy)=Q U(y) at this fixed point of Q. The Jacobian commutes with Q, so it is block diagonal:

    J=[[a,b,0],[b_2,d_0,0],[0,0,e]].

Its curl is Omega=(0,0,b_2-b), and div U=0 gives a+d_0+e=0. At the stagnation point, the vorticity equation reduces to Omega=J Omega. The nonzero third component implies e=1, hence a+d_0=-1. The transverse block of grad V consequently has trace 2c-1.

If c<1/2, the symmetric part of that transverse block has a negative eigenvalue because its trace is negative. Along the corresponding small transverse displacement h, h.V(y_*+h)=h.sym(grad V(y_*))h+o(|h|^2)<0 for sufficiently small h. Thus no nonnegative quadratic outgoing inequality can hold near this point. This conclusion concerns local directions of decreasing squared distance; eigenvalues of the nonsymmetric Jacobian alone are not used. The hypothesis Omega(y_*) differs from zero must not be imposed on every branch.

## A maximum of vorticity magnitude

Suppose |Omega|^2 has a differentiable interior local maximum at y_m. Then its gradient vanishes. Dotting the vorticity equation with Omega gives

    |Omega|^2+(1/2)V.grad |Omega|^2-Omega.J Omega=0.

At y_m the middle term vanishes, proving Omega.J Omega=|Omega|^2. For a nonzero decaying continuous vorticity field on the whole space, a positive global maximum is attained in a finite region; additional differentiability justifies this identity there. For a numerical approximation the maximum must be located and the residual assessed. A sampled maximum is not an exact maximizer, and neither this identity nor spatial rescaling permits an arbitrary normalization of the vorticity supremum.

## Source guardrails

R3 v3, Theorem 3.8, proves the stronger local implication c>=1/2+c_* when a C^2 exact profile has a stagnation point with nonzero vorticity and V(y).(y-y_*)>=c_*|y-y_*|^2 near it, with c_*>=0. Its proof uses the symmetric strain, whose eigenvalues include 1 and have trace zero. The outgoing inequality bounds its smallest eigenvalue below by c_*-c, so its largest eigenvalue is at most 2(c-c_*). Since 1 is an eigenvalue, the claimed bound follows.

Theorem 3.9 addresses nontrivial C^2 profiles with the paper's decay bounds (3.8), normalization (3.7), and Definition 3.7. That definition requires a finite nodal set and a uniform local outgoing inequality at every stagnation point. It is not a theorem without these assumptions. Theorem 4.5 additionally concerns axisymmetric profiles and explicitly assumes (3.5) and (3.8). A genuinely two-fold, non-axisymmetric field is outside that symmetry hypothesis. These distinctions were checked against the saved R3 v3 PDF; they do not assert that a proposed numerical candidate satisfies any theorem's global hypotheses.
