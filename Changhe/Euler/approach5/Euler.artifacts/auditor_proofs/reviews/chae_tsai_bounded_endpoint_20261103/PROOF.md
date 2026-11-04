# Constant fields at the bounded endpoint of the DSS theorem

## 1. Exact statement under audit

The primary source is Dongho Chae and Tai-Peng Tsai, On discretely self-similar solutions of the Euler equations, Mathematical Research Letters21(2014),437-447, DOI10.4310/MRL.2014.v21.n3.a2. The retained journal PDF is pinned in the team records. Printed page446 was read both as extracted text and as a rendered page. Equation(1.6) on page438 and the associated-pressure formula(3.2) on page442 were read in context. The mathematical text on pages437-446 was read; this audit does not independently reconstruct every theorem in that text.

Theorem3.2 assumes a C1loc pair(V,P) on R3 times R satisfying the ordinary periodic profile equation, a period S0>0, V in Lp(R3 times[0,S0]) for3<=p<=infinity, and the pressure formula(3.2). It asserts V=0 if -1<alpha<=3/p or alpha>3/2. Its literal bounded endpoint includes p=infinity,alpha=0.

That endpoint conclusion is false. The counterexample below satisfies the pressure formula with centered principal-value truncation. It also gives a constant BMO pressure representative if that interpretation is used. The same endpoint qualification already found in the archived Chae-Shvydkoy theorem must be retained when citing this DSS extension.

## 2. Complete counterexample, including pressure

Choose any nonzero vector v0 in R3 and any S0>0. Set

    alpha=0, V(y,s)=v0, P(y,s)=-|v0|^2/3.

The kernel printed in(3.2) is

    K_ij(z)=(3z_i z_j-delta_ij|z|^2)/(4pi|z|^5).

Since integral over S2 of theta_i theta_j is(4pi/3)delta_ij, its angular mean is zero. Consequently, for every0<epsilon<R,

    integral_(epsilon<|y-z|<R) K_ij(y-z)(v0)_i(v0)_j dz=0.

Thus the two-sided centered truncation of the displayed associated-pressure integral exists and gives exactly P=-|v0|^2/3. Taking the inner principal value first gives the same result. A change of additive constant has no effect on the equation. If an unqualified integral were instead required to converge absolutely at infinity, the printed assertion for arbitrary bounded velocities would itself need a different definition; absolute convergence is not a hidden condition supplied in Theorem3.2.

The actual equation(1.6) is

    V_s+alpha V/(alpha+1)+(y.grad)V/(alpha+1)+(V.grad)V=-grad P,
    div V=0.

Every derivative in this display is zero and alpha=0. Hence the complete equation holds. Both functions are smooth, periodic for every positive period, and V belongs to the stated spacetime Linfinity class. It is nonzero. Constant physical velocity and pressure also satisfy the physical Euler equation and local energy equality, so imposing that equality would not remove the example. The definition of DSS on page438 explicitly includes stationary self-similar solutions as a special case; minimal temporal period is not required.

## 3. The boundary term and the limited repair

Theorem3.2's proof refers to the Chae-Shvydkoy argument with one additional period integral. For any nonzero nonnegative compact smooth sigma and L>0,

    L^-3 integral_0^S0 integral_R3 |V|^2 sigma(y/L)dy ds
       =S0 |v0|^2 integral_R3 sigma(z)dz>0.

The outer normalized energy term therefore does not vanish at alpha=0,p=infinity. Integrating in time does not repair that endpoint. This reproduces the independently checked obstruction A1481-A1485 in the cited stationary argument.

The extra hypothesis that the period-averaged L^-3 energy on B_L tends to zero removes this particular obstruction. Uniform spatial decay in similarity time implies it by splitting at a fixed radius M: the normalized inner integral tends to zero as L tends to infinity, and the outer integral is bounded by S0 times the unit-ball volume times the squared exterior supremum. Then let M tend to infinity. This proves only the needed outer limit, not a new complete endpoint theorem.

## 4. Consequences and verdicts

The literal assertion V=0 at the stated bounded alpha=0 endpoint is REFUTED by the exact example. The example and pressure calculation are CONFIRMED. A quotation of this journal theorem should flag that endpoint, rather than repeat its entire interval without qualification.

The campaign convention is c=1/(1+alpha). The disputed endpoint is c=1, outside2/5<c<1/2, and the example fails velocity decay. It does not challenge the campaign's subcritical energy conclusion, the finite-p ranges, the vorticity criteria, or the main conjecture. No new theorem for the target class follows. Its unrestricted arbitrary-rotation, arbitrary-helicity form remains OPEN.

## 5. Verification and collaboration

No numerical calculation is used. The pressure integral, profile residual and normalized energy were checked directly. The primary statement was visually verified. All five independent sections were postread. Existing configured model agents receive this focused finding through in the team records for comparison; actual provider runtime remains unattested. No new model client or delegated agent was used.
