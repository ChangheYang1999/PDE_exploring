# Four discrete row functionals on the same saved image

2026-10-21. Written before the independent arithmetic. This result concerns exact finite arrays. It is not an enclosure of the full IPM linearized operator.

## Exact statement and hypotheses

Let n>=2, M>=1, t_0<...<t_(n-1), w_i>0 and g>0 be exact real numbers. Let f_iN be a real array for0<=i<n,0<=N<M and put nu_N=2N+1. Write Delta_i=t_(i+1)-t_i and wbar_i=(w_i+w_(i+1))/2. Define nodal trapezoid weights omega_0=Delta_0/2, omega_(n-1)=Delta_(n-2)/2 and omega_i=(Delta_(i-1)+Delta_i)/2 otherwise. Define

E_L2=sum_i,N w_i^2 f_iN^2,
E_L2q=sum_i,N omega_i w_i^2 f_iN^2,
E_H1=sum_i,N (1+nu_N^2)w_i^2 f_iN^2 + sum_i=0..n-2,N wbar_i^2 (f_(i+1)N-f_iN)^2/Delta_i^2,
E_H1q=sum_i,N omega_i(1+nu_N^2)w_i^2 f_iN^2 + sum_i=0..n-2,N wbar_i^2 (f_(i+1)N-f_iN)^2/Delta_i.

The corresponding scalar quotients are Q_R=sqrt(E_R/g). All are well-defined and nonnegative. For fixed arrays, E_H1>=2E_L2 and E_H1q>=2E_L2q. If omega_- and omega_+ denote the smallest and largest nodal weights, then omega_- E_L2<=E_L2q<=omega_+ E_L2. If mu_- and mu_+ are the extrema of all nodal omega_i and edge Delta_i together, then mu_- E_H1<=E_H1q<=mu_+ E_H1. These bounds require the same image and denominator in both quantities.

## Proof and independent edge formula

Every summand is nonnegative because all weights, widths and g are positive. The inequalities with factor2 use nu_N>=1; the others follow by multiplying each nonnegative value or edge summand by a scalar between the appropriate extrema.

For any finite sequence v_i,
sum_i omega_i v_i = sum_i=0..n-2 Delta_i(v_i+v_(i+1))/2.
Indeed the endpoint values occur once with coefficient Delta/2, and each interior v_i occurs on two adjacent edges with total coefficient (Delta_(i-1)+Delta_i)/2. Apply this to v_i=w_i^2 f_iN^2 and to (1+nu_N^2)v_i. This gives edge formulas for E_L2q and E_H1q independent of the nodal-weight construction. In the derivative term wbar_i^2/Delta_i^2 equals (w_i+w_(i+1))^2/(4Delta_i^2), and the quadrature version has only one Delta_i in the denominator. These are exact finite identities. Positive division by g and the increasing square root give the quotient statements.

No quadrature convergence theorem is used. In particular calling a functional L2q or H1q is only a label for its displayed exact finite definition. The unweighted sums and t-weighted sums have different measures. The weight array is the literal saved w_i, not a rigorous evaluation of an underlying continuous weight. The positive saved scalar g is treated as data; its equality to an actual graph-space norm is not proved here.

## Source selection and computation plan

Preselect six Fminus saved directions before calculation: vector indices0,2,4 from M16/s8/o40 L2q, index0 from M16/s8/o40 H1q, and index0 from each M24/s16/o40 L2q and H1q. All use ppc4 and NJ1. The first two additional M16 L2q directions are the third and fifth, for which the team reports large derivative-sensitive quotients. This deterministic selection is a diagnostic audit, not random evidence for a global minimum.

Freeze the four source NPZ files and their four saved image-evaluation JSON files. Copy the source image evaluator for review only; do not execute it or write in the numerics lane. Export selected binary64 arrays to exact JSON. A new Arb evaluator uses the nodal formulas above. A separate mpmath.iv evaluator imports the frozen original binary data with manual IEEE754 decoding, checks it against the export, uses the edge formulas for the quadrature functionals, and reverses summation order. Compare every selected scalar enclosure, saved displayed quotient and the direct same-image inequalities. Arithmetic enclosures concern only these literal finite arrays.

## Dependencies and scope

The proof uses only finite algebra, positivity and the increasing square root. The exact saved images can have discretization, assembly and rounding errors relative to a true operator image. The saved g can be only a broken-energy diagnostic. The saved vectors need not satisfy exact external constraints, as separate audits already demonstrate. The four row functionals therefore do not certify a continuous H1 norm, an infimum over any complete function space, singular values, inverse bounds or an IPM endpoint. Stability of a finite minimum under two parameter choices is likewise not a convergence proof. Changing stride and cutoff simultaneously cannot by itself isolate either change.
