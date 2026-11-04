# The sharp pressure lower bound at a C2 double zero

Status: CONFIRMED A2668-A2670 after full independent and existing coordinator comparison. Unrestricted consequences remain OPEN A2671. This is a local kinematic Poisson theorem, with an exact whole-ball conclusion.

## 1. Statement, normalization and scope

Let R>0 and B_R be the open ball in R3 centered at zero. Suppose V is C2(B_R;R3), P is C1(B_R;R), and

    div V=0, -Delta P=tr((DV)^2) in distributions,
    V(0)=0, DV(0)=0, P(0)=0,
    P(x)>=|V(x)|^2/4 for every x in B_R.                   (1)

Here tr((DV)^2)=sum_ij partial_i V_j partial_j V_i. Then V=P=0 throughout B_R. There is no upper bound on P and no assumption |V|^2/2-P>=0. At a translated center x0 the pressure comparison must be P(x)-P(x0)>=|V(x)|^2/4, with the velocity and its first derivative zero at x0.

The coefficient 1/4 cannot be lowered in this C2 class, and C1,1 velocity does not suffice at equality. Those countertests below solve local stationary Euler and grow at infinity. They are not smooth decaying self-similar Euler profiles. The full-ball pressure comparison is an additional hypothesis, not a consequence of bare decay.

## 2. Stress identity without a pressure upper bound

Set E=|V|^2, T=V tensor V+P I, and let brackets denote normalized integration over the unit sphere. Define

    e(r)=<E(rn)>, v(r)=<(V(rn).n)^2>, pbar(r)=<P(rn)>,
    A(r)=v(r)+pbar(r), B(r)=e(r)-v(r)+2pbar(r).

Incompressibility gives div div(V tensor V)=tr((DV)^2), so div div T=0 distributionally. Since T is C1, div T is continuous. Mollify div T inside a ball larger than any fixed sphere and smaller than B_R. Its mollifications are divergence free and have zero flux. Uniform convergence on that sphere implies zero flux for div T as well. Thus no center point source is hidden.

The sphere average of the radial divergence decomposition gives

    0=A'(r)+(2A(r)-B(r))/r,
    r A'(r)=e(r)-3v(r).                                  (2)

The tangential divergence integrates to zero. The Taylor bound V(x)=O(|x|^2) implies e,v=O(r^4). Continuity and P(0)=0 give A(0)=0, so integration of (2) yields

    A(r)=integral_0^r [e(s)-3v(s)]ds/s=O(r^4).             (3)

This is the needed pressure control. It does not follow by assuming a pointwise upper bound on P.

## 3. The exact nonnegative endpoint defect

Let k=4pbar-e>=0 by (1), and G=A/r^4. Then A=v+pbar>=e/4>=0 and

    G'=-(7v+k)/r^5.                                      (4)

Equation (3) bounds G near zero. Since G is nonincreasing with r, the limit L=lim_(r downarrow0)G(r) is finite and nonnegative, and for every r1<R,

    integral_0^r1 (7v+k)dr/r^5=L-G(r1)<infinity.           (5)

If L=0 then G=0 everywhere, so A=e=0 and V vanishes on every sphere. Inequality (1) gives P>=0, while pbar=0. Continuity forces P=0 on every sphere and at zero.

Suppose instead L>0. Let Q(x)=(1/2)D2V(0)[x,x]. If Q=0, Taylor expansion gives e,v=o(r^4), and (3) then gives A=o(r^4), contradicting L>0. Thus Q is a nonzero homogeneous quadratic. Since v/r^4 converges to <(Q(n).n)^2>, its weighted integrability in (5) forces that limit to be zero. Hence x.Q(x)=0 everywhere. Incompressibility passes to Q, so div Q=0.

## 4. Direct L1 pressure blow-up

For epsilon>0 set V_epsilon(x)=epsilon^-2 V(epsilon x), P_epsilon(x)=epsilon^-4 P(epsilon x). On every fixed compact ball these are defined for small epsilon. C2 Taylor expansion gives V_epsilon to Q in C2 locally, and E_epsilon to |Q|^2 uniformly. The nonnegative defect 4P-E has sphere mean k. Thus for fixed b,

    integral_(B_b)|4P_epsilon-E_epsilon|dx
       =4pi epsilon^-7 integral_0^(epsilon b) k(s)s^2ds
       <=4pi b^7 integral_0^(epsilon b) k(s)ds/s^5 ->0.     (6)

The last convergence follows from (5). Therefore P_epsilon to |Q|^2/4 in L1 locally. No fourth derivative or fourth-order Taylor expansion of P is used.

The exact scaled Poisson equation is -Delta P_epsilon=tr((DV_epsilon)^2): both sides acquire the factor epsilon^-2 from the original equation. Its left side passes to the distributional limit by (6), and its right side converges uniformly locally. Hence

    Delta|Q|^2/4+tr((DQ)^2)=0.                            (7)

## 5. Tangential quadratics cannot satisfy the limit equation

Differentiate x.Q=0 to obtain (DQ)^T x=-Q. Homogeneity gives DQ x=2Q, so

    x cross curl Q=(DQ)^T x-DQ x=-3Q.

Because curl Q is linear, Q=x cross Mx for a real matrix M. Its divergence is -x.curl(Mx). As that curl is constant, div Q=0 forces curl(Mx)=0 and therefore M symmetric. Choose an oriented orthonormal eigenbasis. Then

    Q=(A yz,B xz,C xy), A+B+C=0.

The coefficients of x^2,y^2,z^2 in (7) respectively give

    B^2+C^2+4BC=0,
    A^2+C^2+4AC=0,
    A^2+B^2+4AB=0.

Using A+B+C=0, these become A^2=-2BC, B^2=-2AC, C^2=-2AB. Multiplication gives (ABC)^2=-8(ABC)^2, so ABC=0; the three equations then force A=B=C=0. This contradicts the nonzero Q from Section 3. Thus L>0 is impossible and Section 3 proves the whole-ball conclusion.

## 6. Exact sharpness and missing-hypothesis tests

For rho=sqrt(x^2+y^2) and beta>1 define

    V_beta=rho^(beta-1)(-y,x,0),
    E_beta=rho^(2beta), P_beta=rho^(2beta)/(2beta).

Off the axis,

    div V_beta=0,
    (V_beta.grad)V_beta=-rho^(2beta-1)e_rho=-grad P_beta,
    tr((DV_beta)^2)=-2beta rho^(2beta-2),
    Delta P_beta=2beta rho^(2beta-2).                     (8)

For j<=2, derivatives of V_beta off the axis are O(rho^(beta-j)). If beta>2 these derivatives extend continuously, with V=DV=0 on the axis, so V_beta is C2 and P_beta is C1. Given any real gamma<1/4, choose beta>2 close enough to two that 1/(2beta)>=gamma. Equations (8) give a nonzero normalized counterexample to replacing 1/4 in (1) by gamma. No C-infinity sharpness for arbitrary beta is claimed.

At beta=2, V_beta is C1,1. Its first derivatives are homogeneous of degree one with bounded derivatives off the axis, and integrate to Lipschitz functions across it. It is not C2: its second component on y=0 is x|x|. Nevertheless P_beta=E_beta/4=rho^4/4 is smooth, and (8) extends distributionally with no axis measure. This tests the endpoint regularity.

Without DV(0)=0, linear rotation V=(-y,x,0), P=rho^2/2 is an analytic nonzero example with P=E/2. Without P(0)=0, use the analytic beta=3 field and pressure P_3+C on B_R, with C>=R^6/12. Since P_3=E_3/6 and E_3<=R^6, the pressure is at least E_3/4, while the velocity has a double zero and is nonzero elsewhere. Thus the center normalization is essential to the statement.

## 7. Dependencies and audit boundary

The proof uses only C1 stress flux, C2 Taylor expansion, nonnegative weighted defect integrability, a direct L1 limit and the complete three-dimensional quadratic classification. It does not use a pending theorem as a black box. It strengthens the quarter-ratio formulation by obtaining the needed sphere-mean bound from center pressure normalization and the exact ODE.

All sharpness statements concern the local kinematic Poisson class (indeed the examples also solve stationary Euler), with no similarity transport equation imposed. The arbitrary-helicity decay-only campaign remains open. No computation, remote client, formal build or external literature claim is needed. Existing configured model file comparison is completed in Section 8; actual provider runtime independently unattested.


## 8. Complete existing comparison and wording check

All ten substantive items, both wording points and the supplied exact-check log of the existing coordinator comparison have been read against all seven source and independent sections. The center normalization is used in equation (3), before any pressure upper estimate. The pressure sign is used both for the L1 defect in equation (6) and to conclude P=0 after V=0. No pressure regularity beyond C1 enters the endpoint proof. The quadratic classification is written out in full in Section 5 rather than inferred from a numerical minimum or a finite sample.

The proposed stronger endpoint wording is correct provided the surrounding statement retains V=DV=0 at the center, C2 velocity, C1 pressure, the full-ball Poisson equation and pointwise bound. At equality the C1,1 countertest has velocity rho^2 e_theta, and the nearby C2 examples have velocity rho^beta e_theta with beta>2. No smooth-class sharpness for nonintegral beta is asserted. The completion theorems already derive H>0 and H/E tending to zero, so this strengthening does not enlarge those particular applications by itself.

The existing comparison is from the agent configured as model; actual provider runtime is independently unattested. The supplied log is corroboration only. No new computation, model client or formal build was needed.
