# Adaptive full-plane modal inverse with the material-center gauge

Status: the mathematical representation and uniqueness below are proved. The implementation has independent manufactured and Cartesian checks. Floating-point quadrature error estimates are not rigorous enclosures.

## Statement and hypotheses

Let 0 < nu < 1. In coordinates X=(r sin(phi),-r cos(phi)), suppose

\[
\Omega(X)=\sum_{n=1}^{N}h_n(r)\sin(n\phi)
\]

is smooth on the entire plane and |h_n(r)| <= C r^{-nu} for r >= 1. In particular the coefficients have the origin compatibility h_n(r)=r^n f_n(r^2), with f_n smooth near zero. Define J(a,b)=(-b,a). The sign convention throughout is

\[
-\Delta\Psi=\Omega,\qquad V=J\nabla\Psi,\qquad \Omega=-\operatorname{curl}V.
\]

For n >= 2 define

\[
p_n(r)=\frac1{2n}\left[r^{-n}\int_0^r s^{n+1}h_n(s)\,ds
+r^n\int_r^\infty s^{1-n}h_n(s)\,ds\right].
\]

For n=1 define

\[
p_1(r)=\frac12\left[r^{-1}\int_0^r s^2h_1(s)\,ds
-r\int_0^r h_1(s)\,ds\right].
\]

Then Psi=sum p_n sin(n phi), with its value at the origin defined by continuity, gives the unique velocity satisfying the defining elliptic equation, V(0)=0 and V=o(r) uniformly in angle. It is the canonical full-plane relative inverse

\[
V(X)=\int_{\mathbb R^2}[K(X-Y)-K(-Y)]\Omega(Y)\,dY,
\quad K(Z)=\frac{(Z_2,-Z_1)}{2\pi |Z|^2}.
\]

The center strain in the Cartesian convention c=Psi_xy(0) is

\[
c=-\frac12\int_0^\infty h_2(s)\,\frac{ds}{s},
\]

with the integral zero if mode 2 is absent. Its generally nonzero value is forced by the whole-plane source. It is not an added harmonic strain.

## Radial equation and regularity

Write A_n(r)=int_0^r s^{n+1}h_n(s)ds and B_n(r)=int_r^infinity s^{1-n}h_n(s)ds. The latter is finite for n >= 2 because n+nu>2. Differentiation, including the two cancelling endpoint terms, gives

\[
p_n'=\tfrac12[-r^{-n-1}A_n+r^{n-1}B_n],\quad
p_n''=\tfrac12[(n+1)r^{-n-2}A_n+(n-1)r^{n-2}B_n]-h_n.
\]

Consequently p_n''+p_n'/r-n^2p_n/r^2=-h_n. At zero, B_n(0) is finite because its local integrand is O(s), and

\[
p_n(r)=\frac{B_n(0)}{2n}r^n+O(r^{n+2}).
\]

The full compatibility of h_n gives smoothness, by these integral formulas or local elliptic regularity after distributional extension across zero. There is no point mass at zero because p_n and its radial flux have the stated vanishing orders.

For n=1 put C(r)=int_0^r h_1(s)ds. Directly,

\[
p_1'=\tfrac12[-r^{-2}A_1-C],\qquad p_1''=r^{-3}A_1-h_1.
\]

These also give the radial equation. If h_1(r)=d r+O(r^3), then p_1=-d r^3/8+O(r^5). Thus this mode contributes no constant velocity. Modes n>=2 also have zero velocity at the origin, so V(0)=0.

For the second mode, r^2 sin(2 phi)=-2xy. Hence its leading stream is -B_2(0)xy/2 and c=-B_2(0)/2, proving the strain formula. The leading speed of this local strain is |B_2(0)|r/2.

## Growth, gauge and uniqueness

The tail assumptions imply A_n=O(r^{n+2-nu}) and B_n=O(r^{2-n-nu}). Also C=O(r^{1-nu}), using nu<1. Hence p_n/r and p_n' are O(r^{1-nu}) for every mode. Finitely many modes give V=O(r^{1-nu})=o(r) uniformly.

The relative kernel integral converges absolutely. Near each kernel singularity this follows from local boundedness of Omega and integrability of 1/|Z| in two dimensions. At infinity, the difference of kernels is O_X(|Y|^{-2}), so the radial majorant is C_X r^{-1-nu}. It gives the same div-curl equations, origin gauge and sublinear growth. These facts can also be checked by differentiating the convergent relative stream integral

\[
\Psi(X)=-\frac1{2\pi}\int
\left[\log|X-Y|-\log|Y|+\frac{X\cdot Y}{|Y|^2}\right]\Omega(Y)\,dY.
\]

For completeness, when r=|X|>s=|Y|, the first angular harmonic of the bracket is +(r/s-s/r)cos(phi-phi_Y). The stream prefactor is negative. Thus angular integration yields the stated negative-inner-complement term in p_1. For s>r that harmonic cancels exactly. There is no such subtraction of mode 2.

If two admissible velocities have the same source, their difference is a harmonic vector field H with H=o(r). An interior derivative estimate on balls centered at any fixed point bounds |DH| by C R^{-1} sup_{B_R}|H|, which tends to zero as R tends to infinity. Therefore H is constant; H(0)=0 makes it zero. This establishes equality of the two inverse representations and uniqueness.

Adding a constant multiple of r sin(phi) changes the constant velocity and violates V(0)=0. Adding a constant multiple of r^2 sin(2 phi) changes a harmonic linear strain and violates V=o(r). In particular replacing B_2(r) by -int_0^r h_2(s)ds/s changes the stream coefficient by -r^2 B_2(0)/4 and is forbidden. A nonzero local linear term forced by B_2(0), which is cancelled at large radius by the rest of the source contribution, is allowed.

## Scaled adaptive integrals and differentiation

At each fixed r>0 set

\[
I_n=\int_0^1 z^{n+1}h_n(rz)\,dz,\quad
C_1=\int_0^1 h_1(rz)\,dz,\quad
O_n=\int_0^1 q^{n-3}h_n(r/q)\,dq\quad(n\ge2).
\]

Substitution s=rz or s=r/q gives exactly

\[
\frac{p_1}{r}=\frac r2(I_1-C_1),\quad p_1'=-\frac r2(I_1+C_1),
\]
\[
\frac{p_n}{r}=\frac r{2n}(I_n+O_n),\quad p_n'=\frac r2(-I_n+O_n).
\]

The oriented frame is e_r=(sin(phi),-cos(phi)), e_phi=(cos(phi),sin(phi)). Therefore

\[
V_r=-\sum_n n(p_n/r)\cos(n\phi),\qquad
V_\phi=\sum_n p_n'\sin(n\phi).
\]

On the two parts of the axis, where phi=0 or pi,

\[
\partial_xV_1(0,y)=\frac1r\sum_n n[p_n'-p_n/r]\cos(n\phi).
\]

This follows by differentiating V_1=V_r sin(phi)+V_phi cos(phi) and x=r sin(phi) at those angles. It supplies the divided transport velocity on the axis without computing 0/0.

The implementation uses independent adaptive Gauss-Kronrod quadrature in physical radius after z=t^2 and q=t^{1/nu}. The latter removes the worst q^{nu-1} endpoint singularity. The tail bound alone does not promise a smooth transformed integrand. More importantly, as r tends to zero, O_2 contains a concentrating contribution from q comparable to r; a quadrature tolerance on absolute velocity alone does not control the strain after dividing by r. The center moment must be evaluated separately, and small-radius refinement must be checked. These are numerical limitations, not qualifications of the representation theorem.

## Verification and dependencies

Source: `code_independent/adaptive_modal_inverse.py`. Independent tests: `code_independent/test_adaptive_modal_inverse.py`, with raw outputs in `verification/adaptive_modal_inverse/`.

The manufactured stream combines modes 1 through 4 with rational fractional-power radial factors. Its known velocity is checked at radii from 1e-5 to 1e6 and two quadrature tolerances. The largest observed error divided by 1+r is 2.23e-16; the largest absolute error is 5.46e-12 at the largest scales. Angular extraction agrees with direct spline values to 3.56e-15. On a nontrivial saved field, this inverse and the independently implemented Cartesian Duffy/exterior inverse agree to 4.24e-10 at the tested points. These observations do not certify continuum error bounds.

Actual model collaboration: `opus_reviews/62_adaptive_inverse/` returned model `claude-opus-5-5` and a written audit. Own checking identified a raw-log-kernel sign slip and missing strain factors in its prose. Follow-up `opus_reviews/63_adaptive_inverse_followup/` acknowledged the corrections. Its second paragraph switched radial-source conventions; that alternate convention is not adopted here. Every displayed formula above was independently derived with -Delta Psi=Omega. The tests use this same sign throughout.

No formal proof assistant was run. Dependencies are elementary Fourier orthogonality, one-dimensional differentiation under convergent integrals, local elliptic regularity and the harmonic derivative estimate. This packet supplies a verification method and no B2 existence or nonexistence result.

## Observed tiny-radius limitation

The independent scan in `verification/near_center_inverse/` confirms the limitation just stated. For the exact smooth manufactured stream p2=0.3r^2(1+r^2)^(-1/6), absolute velocity tolerances1e-8 and2e-11 permit O(1) strain errors below radii1e-10 and1e-11 respectively, while the quadrature reports success. A separate physical-radius origin moment recovers c=-0.6 to within2.3e-14. This is not used to extend the tested domain of the broad-grid audit, whose smallest radius is1e-5.
