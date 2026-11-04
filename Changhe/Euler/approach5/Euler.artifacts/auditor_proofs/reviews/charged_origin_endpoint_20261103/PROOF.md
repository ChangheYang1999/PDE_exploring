# The charged radial endpoint at c=1/3

Status: CONFIRMED at the exact conditional or countertest scopes in A600. Full independent proof postread completed. The unrestricted campaign conjecture is not proved.

## 1. Exact statement

Let Q be a nonzero real number, omega any finite real number, Jx=(-x2,x1,0), c=1/3, A=cI-omega J, L=(1-c)I+omega J, p=2 and beta=1/4. On D=R3 minus{0}, with r=|x| and n=x/r, define

    V=Q x/r^3, P2=-Q^2/(2r^4), S=P2-|V|^2/2=-Q^2/r^4,
    k=(Ax).V=cQ/r, b=|S|^beta=|Q|^(1/2)/r.

This smooth nonzero punctured profile satisfies div V=0, curl V=0 and LV+DV(Ax+V)+grad P2=0 on D. Consequently it satisfies local Poisson, helicity freedom, W.grad S=0 and global rank grad k cross grad S=0. Its twisted degrees are the velocity and scalar degrees required in the tail theorem. The weight b is globally A2 on R3, but the core rigidity conclusion fails at p=2.

## 2. Every equation and the A2 condition

Direct differentiation gives DV=Q r^-3(I-3n tensor n), DV x=-2V and DV Jx=JV. Thus the linear part of momentum is (1-3c)V=0, with exact cancellation of the rotation. Also DV V=-2Q^2 r^-5 n and grad P2=2Q^2 r^-5 n. The derivative matrix is symmetric and trace free, so divergence and actual curl vanish. Its squared trace is6Q^2/r^6; the radial formula Delta r^-4=12r^-6 verifies -Delta P2=tr(DV^2)=partial_i partial_j(V_iV_j) on D.

The scalar gradients are grad S=4Q^2 x/r^6 and grad k=-cQ x/r^3, which are parallel. The regularized core identity reduces to grad S cross V=0. Radial covariance under T_t=exp(tA) is V(T_t x)=exp(-2ct)exp(-omega tJ)V(x), and2c=1-c. The pressure scales by exp(-4ct)=exp(-2(1-c)t).

The centered ball averages of b and b^-1 are3|Q|^(1/2)/(2R) and3R/(4|Q|^(1/2)); their product is9/8. On a ball B(x,R) with |x|>2R the radial weights are comparable to constants. For |x|<=2R, enclose it in B(0,3R) and use the centered estimates and the fixed volume ratio. This proves a uniform global A2 bound, with arbitrary assignment at0. No theorem about power weights is needed.

## 3. Distributional charge and energy failure

Set q0=Q/|Q|^(1/2). Then G=V/b=q0 x/r^2=grad psi for psi=q0 log r. Both psi and G are locally integrable at0; an inner cutoff gives no gradient defect. In contrast, integration by parts on r>epsilon gives, for a compactly supported smooth test phi,

    -integral_(r>epsilon) V.grad phi
        =Q integral_S2 phi(epsilon n)d sigma(n).

The inward spherical boundary for the punctured region has outward normal -n. Taking the limit proves

    div(b grad psi)=div V=4pi Q delta0.

There is a divergence charge, even though the factor field G has no curl charge. The weighted energy is exactly

    integral_(epsilon<r<R) b|grad psi|^2
        =4pi |Q|^(3/2)log(R/epsilon).

It diverges as epsilon tends to0. The weighted function integral stays finite, since it is proportional to integral_0^R r(log r)^2 dr. The additive scaling law psi(T_t x)=psi(x)+(q0/3)t has nonzero logarithmic drift. Both the source-free weak equation and the completed gradient energy required for weighted continuity at0 fail. These are exactly the two strict p<2 steps in the independently checked A2 proof.

## 4. Scope

The velocity is unbounded at0, has flux4pi Q through every sphere and its stress is not locally integrable at0. This is not a whole-space C2 profile or a canonical-stress example from the1<p<3/2 class. It does disprove replacing p<2 by p<=2 under the OTHER punctured-space hypotheses of the standalone weighted theorem.

A globally smooth divergence-free U cannot have V as a uniform order-r^-2 tail. If U(rn)-V(rn)=o(r^-2) uniformly, its spherical flux differs from4pi Q by o(1), while the divergence theorem makes its flux0 for every radius. Zero flux is an additional necessary condition on an actual tail; no claim is made that it repairs every p=2 obstruction. Every calculation is exact and elementary, with no numerical or external existence input.
