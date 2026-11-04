# Constant far fields under Dini derivative decay

Status: CONFIRMED with the explicit Dini hypothesis and, by A492, for bounded profiles with bounded gradient. The natural rates do not give nonexistence in the campaign interval.

## 1. Statement and dependencies

Fix0<c<1 and omega in R, J(x1,x2,x3)=(-x2,x1,0), A=cI-omega J and L0=(1-c)I+omega J. Let U in C2(R3;R3), P in C1(R3) satisfy

    div U=0, L0 U+DU(Ay+U)+grad P=0.

Suppose U and DU are bounded and m(r)=sup_(|y|>=r)||DU(y)|| satisfies integral_1^infinity m(r)dr/r<infinity. Put gamma=1/c. There is a unique vector uinf with

    |curl U(y)|<=C(1+|y|)^(-gamma),
    |U(y)-uinf|<=C r^(1-gamma)       if1<gamma<3,
    |U(y)-uinf|<=C r^-2 log r        if gamma=3,
    |U(y)-uinf|<=C r^-2              if gamma>3,       (1)

for r=|y|>=2, and grad P(y) tends to -L0 uinf. If1/3<c<1, then additionally ||DU(y)||<=C(1+|y|)^(-1/c). If0<c<2/5, U is constant. No rigidity is asserted at c=2/5 or in the campaign interval2/5<c<1/2. Constants depend on the fixed parameters and profile data.

A485 supplies only the actual pressure-gradient limit for a normalized decaying profile. A477 supplies only the sharper gradient estimate after normalization, with its A210 scattering dependency. The vorticity, velocity, normalization and energy arguments are proved here. A492 now supplies the explicit Dini premise for every bounded C2 profile with bounded DU. Thus all conclusions also hold in that class without assuming Dini decay separately. This does not infer bounded DU from bounded or decaying U.

## 2. Vorticity on complete exterior characteristics

Write B=Ay+U, W=curl U, M=sup|U|, L=sup||DU||. The carrier is globally Lipschitz and has linear growth, so its flow is complete. Choose R0>max(1,2M/c), and k=M/c. Along an exterior trajectory r=|y| satisfies cr-M<=r'<=cr+M, since the rotation is orthogonal to y. A backward trajectory from any r>R0 crosses r=R0 in finite time: otherwise r(-t)<=r(0)e^(-ct/2) while remaining at least R0, a contradiction. Starting at that crossing,

    k+(R0-k)e^(cs)<=r(s)<=(R0+k)e^(cs)-k.           (2)

In particular r'>=cr/2 and

    integral_0^t ||DU(Y(s))||ds
       <=(2/c)integral_(R0)^infinity m(r)dr/r.       (3)

The exact vorticity equation is W'=DU W-W-omega JW. Nonzero W remains nonzero on a finite trajectory by uniqueness for this linear equation. Its norm q satisfies q'<=(||DU||-1)q; rotation drops out. Equations(2)-(3) and the bounded initial sphere values yield

    q(Y(t))<=2L exp((2/c)integral_(R0)^infinity m(r)dr/r)e^-t
           <=C r(t)^(-1/c).                        (4)

Zero trajectories satisfy the same estimate. Compact boundedness completes the global estimate. Neither a small Dini integral nor a terminal flow limit is used.

## 3. Absolutely convergent reconstruction of the velocity

Let N(x)=1/(4pi|x|), so -Delta N=delta0, and define

    Z(x)=integral grad N(x-z) cross W(z) dz.         (5)

This has the same sign as curl(N*W). The degree-minus-two singularity is locally integrable against bounded W. For |z|>2|x|+2 the radial absolute tail is bounded by C integral r^(-gamma)dr, finite since gamma>1. Near/far splitting proves continuity and boundedness.

For R=|x|>=2, split into |z|<R/2, |x-z|<R/2, the remaining part of |z|<=2R, and |z|>2R. The respective absolute bounds are

    C R^-2 integral_0^(R/2) s^2(1+s)^(-gamma)ds,
    C R^(1-gamma), C R^(1-gamma),
    C R^(1-gamma)/(gamma-1).                       (6)

They give exactly the three velocity rates in(1), so Z tends uniformly to0.

In distributions Delta Z=-curl W. To verify it, test(5) against Delta phi for smooth compactly supported phi and apply Fubini. The same local and tail estimates give absolute integrability, and Delta grad N=-grad delta0 gives the stated sign. This does not require convergence of N*W itself. Since div U=0, Delta U=-curl W as well. Hence U-Z is a bounded harmonic distribution, represented by a smooth harmonic vector field. The interior gradient estimate on balls of radius R gives |D(U-Z)(x)|<=C R^-1 sup|U-Z|. Sending R to infinity proves U-Z=uinf constant. Continuity identifies the distributional and pointwise values. The uniform limit and its uniqueness follow.

## 4. The affine normalization preserves the equation

The matrix A is invertible because |Av|>=c|v|. Set

    y0=-A^-1 uinf, V(z)=U(z+y0)-uinf,
    Q(z)=P(z+y0)+(L0 uinf).z.                      (7)

Then A(z+y0)+U(z+y0)=Az+V(z). Substitution gives div V=0 and L0 V+DV(Az+V)+grad Q=0. The constant term L0 uinf is canceled by the displayed linear pressure correction. V tends to zero, is bounded with bounded derivative, and retains the C2/C1 regularity. For large r its exterior derivative supremum is at most m(r/2), so it retains the Dini condition. A485 gives grad Q->0, proving grad P->-L0 uinf. If1/3<c<1, the bounded normalized V has V(R .)->0 distributionally and satisfies all A477 hypotheses; that theorem gives DV=O(r^-1/c), and translation gives the asserted rate for DU.

## 5. The actual pressure at the finite-energy scope

Suppose0<c<2/5. Then gamma>5/2, and every applicable rate in(1) implies V in L2(R3). Boundedness also gives V in L4. Define the L2 pressure Q0 by the Fourier multipliers

    Q0hat(xi)=-sum_(i,j) (xi_i xi_j/|xi|^2) (V_i V_j)hat(xi), xi!=0.

Each multiplier is bounded by1. Plancherel gives Q0 in L2 and -Delta Q0=partial_i partial_j(V_i V_j). Taking divergence of the actual profile equation gives the same equation for Q. In coordinates the terms A_ji partial_j V_i and omega J_ij partial_i V_j cancel their skew parts, while their dilation part is c div V=0. Thus there is no extra rotation source.

By Section4 and A485, grad Q tends to zero and is bounded. Integrating along radial segments therefore gives Q(x)=o(|x|) uniformly after subtracting a fixed constant, and Q has at most linear growth. The harmonic distribution h=Q-Q0 is smooth. Its averaged absolute value on a radius-R ball centered at fixed x is at most C_x(1+R)+C R^-3/2||Q0||_2. The interior second-derivative harmonic estimate gives |D2h(x)|<=C R^-2 times that bound, tending to zero. Therefore h=b.x+b0. On a fixed annulus Q(Rz)/R tends uniformly to zero, and ||Q0(R .)/R||_2<=R^-5/2||Q0||_2. It follows that b.z=0 distributionally on that annulus, hence b=0. We have derived the actual normalization

    Q=Q0+b0, Q0 in L2.                            (8)

It was not assumed as a boundary condition.

## 6. Boundary terms in the energy identity

Let chi_R be smooth radial, equal to1 on the radius-R ball and zero outside radius2R, with |Dchi_R|<=C/R. Dot the normalized equation with V, multiply by chi_R and integrate. All integrations are over compact sets, and div V=0,div(Az)=3c,V.JV=0 give, with E=|V|^2/2,

    (1-5c/2)integral |V|^2 chi_R
       =integral E(Az).Dchi_R+integral(E+Q)V.Dchi_R. (9)

The rotation vanishes in the first term because chi_R is radial. Its dilation part is bounded by C integral_(R<|z|<2R)|V|^2, tending to zero. The cubic flux is at most C R^-1||V||_infinity times that same tail. The b0 pressure flux vanishes by div V=0. The Q0 flux is at most C R^-1||Q0||_2||V||_2, also tending to zero. Dominated convergence on the left yields (1-5c/2)||V||_2^2=0. Since0<c<2/5, V=0, so U=uinf. The original equation then gives grad P=-L0 uinf.

No finite energy follows from these rates at c=2/5 or above it. In the campaign interval the natural velocity tail is compatible with infinite energy. No conclusion about the main conjecture is implied.

## 7. Scope and review record

The full LIT121 source was read before this proof. Every sign, integrability threshold, translation, harmonic ambiguity and boundary term above was checked directly. There is no numerical computation. A492 has removed the Dini premise only for the explicitly bounded-gradient class. Existing configured-model file collaboration is requested for the absolute reconstruction and the pressure normalization; no new remote client is used.
