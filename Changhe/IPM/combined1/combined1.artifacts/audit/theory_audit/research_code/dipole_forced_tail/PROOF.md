# Forced correction tails below exponent minus three

This independently checks R2 and R3 of Opus the review of T4-294. The velocity
estimate and conditional theorem below are analytic. The final application
uses the exact sector coefficients already audited in the adjoining topics.

## 1. Spaces and velocity estimate

Let h be a real centrally odd C1 function on R2. For real q define

    H_q(h)=max(sup_X (1+|X|)^(-q)|h(X)|,
               sup_X (1+|X|)^(1-q)|grad h(X)|).

For q<-3 and H=H_q(h)<infinity, h belongs to L2 and its canonical IPM
velocity has Fourier multiplier (xi_1 xi_2,-xi_1^2)/|xi|^2. Equivalently,

    U[h](X)=(0,-h(X)/2)+PV int K(X-Y)h(Y)dY,
    K(Z)=(-z_1 z_2,(z_1^2-z_2^2)/2)/(pi |Z|^4).

For r=|X|>=2,

    |U[h](X)| <= D_q H r^-3,                                      (1)
    D_q = 2^(q+3) (1/2+2^(-q)+2^(3-q)+2^(q+2)/(-q))
                    +32/[(-q-1)(-q-2)(-q-3)].

Proof. The contact term is bounded by Hr^q/2. Use the disjoint regions
|Y-X|<r/2, |Y|<r/2, the remainder with r/2<=|Y|<=2r, and |Y|>2r.
The kernel satisfies |K(Z)|=1/(2pi|Z|^2), zero angular mean, and
||DK(Z)||_op=1/(pi|Z|^3). On the first region subtract h(X) and use
|grad h|<=H(r/2)^(q-1). The bound is 2^(-q)Hr^q. On the third and
fourth regions the respective bounds are 2^(3-q)Hr^q and
2^(q+2)Hr^q/(-q), by the area and radial integrals given in
../forced_integrable_tail/PROOF.md. Those estimates need only q<0.

On |Y|<r/2 central oddness gives int h=0. Subtract K(X). Along the
segment X-tY the radius is at least r/2, so this contribution is at most

    (8/(pi r^3)) int |Y| |h(Y)| dY
    <= 16H r^-3 int_0^infinity rho^2(1+rho)^q d rho
    = 32H r^-3/[(-q-1)(-q-2)(-q-3)].

The last integral is B(3,-q-3), obtained by t=rho/(1+rho), and converges
for q<-3. Finally r^q<=2^(q+3)r^-3 for r>=2, which proves(1).
The principal value is justified by the local C1 difference; the far
integral converges absolutely. The explicit contact term has not been
removed. This proof uses neither a derivative of U[h] nor an L2-to-Linfinity
estimate. A compact S1 h with nonzero int y h has a nonzero r^-3 dipole,
so no general bound of order r^q can replace(1) when q<-3.

## 2. Conditional asymptotic theorem

Fix c>1, gamma=1/c, delta=1-gamma and gamma-4<q<-3. Let R be a real
C1 S1 reference with its specified canonical velocity U[R]. Suppose,
for r>=R0>=2, continuous A on the circle, epsilon>0 and V,G,E>=0,

    |U[R]|<=V r^gamma,     |grad R|<=G r^(gamma-1),
    |F(R)(r,theta)-r^q A(theta)|<=E r^(q-epsilon),
    F(R)=c X.grad R-R+U[R].grad R.

Let h be real centrally odd C1 with H=H_q(h)<infinity. Suppose R+h is
stationary at this same c and its velocity is U[R]+U[h]. The equation
may be pointwise, or distributional with continuous terms. Then

    h(r,theta)=r^q A(theta)/(1-cq)+e(r,theta),                     (2)
    |e| <= E r^(q-epsilon)/[1-c(q-epsilon)]
         + V H r^(q-delta)/[1-c(q-delta)]
         + D_q G H r^(gamma-4)/(4c)
         + D_q H^2 r^(q-4)/[1-c(q-4)].                            (3)

All bounds are uniform in theta; all denominators are positive. In
particular e=O(r^(q-epsilon_*)), where

    epsilon_* = min(epsilon,delta,q-gamma+4,4)>0.

Proof. Subtract the reference equation:

    c r partial_r h-h = -F(R)-U[R].grad h-U[h].grad R-U[h].grad h.

By(1), the three additional absolute bounds are respectively
VH r^(q-delta), D_q GH r^(gamma-4), and D_q H^2 r^(q-4).
Every exponent is less than gamma. Since r^-gamma h tends uniformly
to zero, integrate partial_r(r^-gamma h) from r to infinity. For any
p<gamma,

    (r^gamma/c) int_r^infinity t^(p-gamma-1) dt = r^p/(1-cp).

This identity gives(2)-(3), including the positive sign of A/(1-cq).
For the third term 1-c(gamma-4)=4c. The condition q>gamma-4 is exactly
what makes that term lower order than r^q. This proves the theorem.
No coefficient conclusion is asserted at q=gamma-4; at that endpoint
a nonzero dipole can contribute at the same order as the residual.

## 3. Faster decay is impossible under these hypotheses

In the theorem, assume A is not identically zero. There is no such
stationary correction with H_q'(h)<infinity for any q'<q. Indeed,
H_q(h)<=H_q'(h), and (1+r)^(-q)h tends uniformly to zero if q'<q.
Equation(2) instead forces r^-q h to tend to the nonzero continuous
function A/(1-cq). This is a contradiction.

The same argument applies to the earlier theorem with -3<q<0 in
../forced_integrable_tail/PROOF.md. It does not assume that every L2
correction has weighted C1 decay. It is a necessary asymptotic obstruction
in the explicitly stated class, not general nonexistence.

## 4. Exact campaign application

Set c=4076476460239181/2251799813685248. For each of the exact
references007,013,014, let eta be the global smooth repair in
../forced_integrable_tail/PROOF.md, accepted in T4-315. Its residual
has first nonzero sector(9,0), unchanged from the original reference:

    q2=1-9delta,  A=F_(9,0),  epsilon=2-4delta.

The next nonzero sector(5,1) is lower by epsilon. The convergent radial
expansion gives the uniform remainder and finite V,G,E required above;
their numerical values are not needed for the asymptotic conclusion.
The exact data independently establish gamma-4<q2<-3 and epsilon>0.
Hence, if R+h is exact and H_q2(h-eta)<infinity,

    h=eta+r^q2 F_(9,0)/(1-cq2)+o(r^q2).

The three F_(9,0) coefficient maps agree exactly. The checker encloses
D_q2 and the L2 circle norm of F_(9,0)/(1-cq2), using all exact sine
coefficients and orthogonality. It compares the former with the Opus
interval; the latter is an independent numerical refinement of the
Opus decimal. In particular no correction to R+eta can decay faster
than r^q2 in the above weighted C1 sense. Before the repair, the analogous
statement holds with q1=-1-4delta and A=F_(4,1). Both A maps are nonzero.

## 5. Scope and evidence

This theorem verifies the two new claims of the independent Opus
review. The proof above precedes the specialization checker. It does
not assume a new branch exists in the optimizer, does not construct a
solution, does not certify an inverse, and makes no statement about
an arbitrary L2 correction. The canonical c remains fixed. Exact
coefficient data, source review and directed-arithmetic output are
stored alongside this proof.
