# Flat continuation for an exact homogeneous harmonic planar weight

Status: proved at the exact local scope below. This independently reconstructs all eight sections of LIT218. Read after the weighted nodal-interface review. No variable-weight or Euler-tail conclusion is implicit.

## 1. The theorem

Let R>0, let H be a nonzero real homogeneous harmonic polynomial of integer degree l>=1 on R2, and let 0<eta<1. Let psi be real and C-infinity on the open disk B_R, and suppose the pointwise equation

    H Delta psi-eta grad H.grad psi=0

holds everywhere in B_R, including the nodal set of H. If all derivatives of psi vanish at0, then psi=0 on B_R. Consequently, if all derivatives of grad psi vanish at0, then psi is constant on B_R.

There is no integrability assumption on |H|^(-eta) at the center. In particular l eta>=2 is allowed. The only weak integrations used in the proof take place on annuli of positive inner radius.

## 2. Nodal sectors and their actual conormal condition

Write H(r,theta)=r^l h(theta). Harmonicity gives h''+l^2h=0, so after an angular translation h=C sin(l theta), C!=0. Thus there are exactly2l equally spaced zero rays. On one sector let t=l(theta-theta_j) range over (0,pi), and set

    f(r,t)=psi(r,theta_j+t/l),
    w(t)=sin(t)^(-eta).

Dividing the equation by H inside the sector and using polar differentiation gives

    f_rr+(1-l eta)f_r/r+(l^2/r^2)w^(-1)(w f_t)_t=0.       (2.1)

At a boundary ray with r>0, grad H is nonzero and normal to the ray. The undivided pointwise equation therefore gives f_t=0 on that ray. On every compact positive-radius annulus, smoothness implies f_t=O(t) at0 and O(pi-t) atpi. Hence w f_t tends to zero separately on both rays, because eta<1. This condition follows from the pointwise equation and smoothness; it is not inferred from cancellation of opposite interface fluxes. The angular measure w dt is finite.

## 3. Complete angular polynomials

Under x=cos t, the measure becomes rho(x)dx with

    rho(x)=(1-x^2)^(-(1+eta)/2), -1<x<1.

This is a finite positive measure. Orthogonalize 1,x,x^2,... and normalize to obtain real polynomials P_n of exact degree n. Positivity of the measure on every open interval makes the construction nondegenerate. These polynomials are complete in L2(rho dx): continuous functions are dense for this finite measure, and polynomial uniform approximation on [-1,1] approximates them in L2. For completeness of the first density statement, approximate interval indicators by continuous piecewise-linear functions, using finiteness and absolute continuity of the measure, and then use simple-function approximation.

On polynomials define

    T P=-(1-x^2)P''+(1-eta)xP'
       =-rho^(-1)[(1-x^2)rho P']'.

Since (1-x^2)rho=(1-x^2)^((1-eta)/2) tends to zero at each endpoint, integration by parts has no boundary term for polynomials. T is symmetric, preserves polynomials of degree at most n, and multiplies the leading coefficient of a degree-n polynomial by n(n-eta). For j<n, symmetry gives <TP_n,P_j>=<P_n,TP_j>=0. Therefore TP_n-n(n-eta)P_n has degree at most n-1 and is orthogonal to every such polynomial. Its norm is zero and

    T P_n=n(n-eta)P_n.

Thus e_n(t)=P_n(cos t) is a complete orthonormal basis of L2(w dt), with

    -w^(-1)(w e_n')'=n(n-eta)e_n.

Also e_n'=O(t) at0 and O(pi-t) atpi, so its weighted conormal derivative vanishes separately at both endpoints. No self-adjoint extension choice or external spectral classification is needed: the complete polynomial family suffices for the following projections.

## 4. Projection with every boundary term

For 0<r<R set a_n(r)=integral_0^pi f(r,t)e_n(t)w(t)dt. Smoothness on compact annuli and integrability of w permit all r derivatives under the integral. Integrate the angular part of (2.1) first on (epsilon,pi-epsilon). The boundary terms after two integrations by parts are w f_t e_n and w e_n' f. Both are O(epsilon^(1-eta)) on a compact annulus, and tend to zero. The remaining integral converges, since f is bounded and (w e_n')'=-n(n-eta)w e_n is integrable. It follows that

    r^2 a_n''+(1-l eta)r a_n'-l^2n(n-eta)a_n=0.           (4.1)

These are exact ODEs on the entire connected interval (0,R). No integration across r=0 occurred, so a hidden central conormal condition is not being used.

## 5. Flatness kills every finite radial power

Put r=exp(s) in (4.1). For n>=1 its characteristic roots are l n and l(eta-n), which are distinct, with the latter negative. Hence

    a_n(r)=A_n r^(l n)+B_n r^(l(eta-n)).

For n=0 the two roots are0 and l eta, again distinct, and

    a_0(r)=A_0+B_0 r^(l eta).

Taylor's theorem and flatness of psi imply |psi(x)|<=C_N |x|^N near0 for every integer N. Since e_n w is integrable, |a_n(r)|<=C_(n,N) r^N. For n>=1 the negative term must first vanish, and choosing N>l n eliminates the positive term. For n=0 first the constant and then the positive power vanish by choosing N>l eta. Thus all coefficients vanish identically for all0<r<R.

At each fixed positive radius, completeness of the e_n makes f zero in L2(w dt); continuity makes it zero everywhere on the sector. Repeat for all2l sectors and use continuity on the rays and at0 to obtain psi=0 on the entire disk. For the gradient formulation apply this result to psi-psi(0).

## 6. Exact relation to a planar conservation model

Suppose a smooth planar vector field F and scalar S satisfy

    div F=d rho, F.grad S=b rho S,

with constants b,d>0, and suppose exactly F=grad psi and eta=d/b. Elimination of rho gives

    S Delta psi-eta grad S.grad psi=0.

If S is exactly a nonzero homogeneous harmonic polynomial and0<eta<1, an infinitely flat F must therefore vanish locally, and in fact on every disk where all these exact assumptions hold. A nonzero constant multiple of S and a rigid planar coordinate change cause no change in the argument. This is the sole claimed model application.

The campaign exponent lies in this interval, but actual angular fields can have a non-Euclidean matrix and drift, and the full scalar need not equal its first harmonic Taylor term. Those are different equations. Finite-order agreement of coefficients does not determine an unknown that is flat to all orders, so a Taylor substitution cannot prove the desired transfer.

## 7. What a possible extension would have to prove

If S has first term H_l harmonic, smoothness gives grad S=grad H_l+O(r^l). In the plane, |grad H_l|=l|C|r^(l-1), so |grad S| is comparable to r^(l-1) for small positive r. The formal vector field

    Z=x+[(lS-x.grad S)/|grad S|^2]grad S

then satisfies Z.grad S=lS and Z-x=O(r^2) off the center. This elementary size statement alone proves neither smooth extension of Z nor a weighted frequency estimate, admissible transformed matrix, or interface condition. Those require a separate argument. LIT219 proposes such an extension and is audited separately.

## 8. Dependencies and verification evidence

The proof uses Taylor's theorem, elementary integration, polynomial approximation and a constant-coefficient ODE. The exact source is pinned with its hash. All eight source sections and all sections of this reconstruction were read. No numerical evidence, paper theorem, formal proof assistant, server, model client or outside-agent modification is a dependency. The unrestricted Euler conjecture remains open.
