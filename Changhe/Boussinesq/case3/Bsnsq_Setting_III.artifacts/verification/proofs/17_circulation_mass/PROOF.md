# Nonzero transported circulation and the necessary slow vorticity tail

Status: independent audit of lead notes/circulation_mass.md, with one signed-integral correction and a critical-integrability extension. No full B2 endpoint follows.

## Statement

Let beta>=2. On the whole plane let U, Omega and Theta be smooth, div U=0, -curl U=Omega. Set V=U-U(0), W=beta X+V and assume V=o(|X|). Require the exact equations

    W.grad Omega+Omega=Theta_x,  W.grad Theta=(beta-2)Theta,

and the B2 parity and center data: W(0)=0, the vertical axis is invariant, Theta(0,y)=0, Theta=a0 x^2+O(|X|^3), a0!=0. The local equations imply Omega_x(0)=4a0/beta.

There is a bounded piecewise smooth domain D in x>0, with boundary possibly on x=0, and a nonzero number A_D of the sign of a0, such that, for every 0<eta<1,

    integral_(phi_t D) Omega
       = e^((2 beta-1)t)[A_D+O(e^(-(1-eta)t))].                    (1)

Here phi_t is the complete flow of W. Under the stronger power bound |V(X)|<=C(1+|X|)^(1-delta), delta>0, the error in brackets is O(e^(-t)). It follows that for every eta in (0,1) and all sufficiently large R,

    integral_{B_R cap {x>0}} (sign(a0) Omega)_+
       >= c_eta R^((2 beta-1)/(beta+eta)).                        (2)

Under the power bound this improves to

    integral_{B_R cap {x>0}} (sign(a0) Omega)_+
       >= c R^(2-1/beta).                                       (3)

In particular M(R)=integral_{B_R}|Omega| satisfies these bounds. The signed integral over the entire half-ball is NOT asserted: opposite-sign vorticity outside phi_t D can cancel its circulation.

Even under only V=o(r), Omega cannot belong to any L^p(R^2) with 1<=p<=2 beta. The critical endpoint p=2 beta uses the div-curl inverse as explained below. Under the power bound, every radial weighted absolute integral with weight (1+r)^(-gamma), gamma<=2-1/beta, diverges. In particular a uniform tail Omega=o(r^(-1/beta)) is impossible; the stronger bound |Omega|<=C(1+r)^(-2/beta) is excluded.

## 1. Complete flow and radius bounds

Smoothness gives local existence and uniqueness. Sublinear V gives |W(X)|<=C(1+|X|), so no finite-time orbit can escape to infinity in either time direction. The autonomous flow is a smooth diffeomorphism, has determinant e^(2 beta t), and preserves x>0 by uniqueness and axis invariance.

For each eta>0, |V(X)|<=eta |X|+C_eta, hence every orbit from a fixed bounded set obeys |phi_t X|<=C_{K,eta}e^((beta+eta)t), t>=0. Under the power bound, first decrease delta to a number in (0,1) if necessary. The differential inequality for r=1+|phi_t X| is r'<=beta r+C r^(1-delta) almost everywhere; multiply by delta r^(delta-1) and integrate. This gives |phi_t X|<=C_K e^(beta t). These bounds are uniform on compact sets.

## 2. Exact circulation identity and convergence without derivative bounds

For any bounded piecewise smooth D, put J_D(t)=integral_(phi_t D) Omega. Reynolds transport and div W=2 beta give

    J_D'=(2 beta-1)J_D+B_D(t),
    B_D(t)=integral_(phi_t D) Theta_x=oint_(boundary phi_t D) Theta dy.

All operations are on bounded domains at each finite time. Pull back the positively oriented boundary and integrate by parts along its closed piecewise smooth parametrization:

    B_D(t)=e^((beta-2)t) oint_(boundary D) Theta d(phi_t X)_2
          =-e^((beta-2)t) oint_(boundary D) (phi_t X)_2 dTheta.

There is no boundary term at the corners because the values are continuous around the closed curve. The total variation of the fixed smooth Theta along boundary D is finite. Thus the radius estimate, with k=beta+eta or k=beta, yields |B_D(t)|<=C_D e^((beta-2+k)t). With k<beta+1 this is integrable after multiplication by e^(-(2 beta-1)t). Therefore

    A_D=J_D(0)+integral_0^infinity e^(-(2 beta-1)s)B_D(s) ds
       =integral_D Omega-oint_(boundary D) H dTheta,
    H(X)=integral_0^infinity e^(-(beta+1)s)(phi_s X)_2 ds.          (4)

The last integral converges uniformly on every compact set, so H is continuous. Fubini is justified by the radius bound times the fixed boundary variation. Differentiability of H is neither claimed nor needed. The tail estimate of this convergent integral gives exactly (1).

## 3. A domain with a nonzero coefficient

The equilibrium at zero and axis invariance imply (phi_s(0,b))_2>0 for each b>0 and every finite s>=0. Otherwise a one-dimensional orbit would hit the equilibrium zero, contrary to uniqueness. Consequently H(0,b)>0 and H(0,0)=0.

Smooth division gives Theta=x^2 a(x,y), a(0,0)=a0. In a sufficiently small rectangle a/a0>0 and Omega/x has the sign of a0 for x>0, since its value at zero is 4a0/beta. Define smooth local coordinates

    xi=x sqrt(a(x,y)/a0),  y=y.

They preserve orientation after restricting the neighborhood, and Theta=a0 xi^2 exactly. Choose a small fixed b>0 inside this chart. By continuity of H and H(0,b)>H(0,0), choose h>0 small enough that the image D of (0,h) times (0,b) lies in the chart and

    Htilde(xi,b)-Htilde(xi,0)>0,  0<=xi<=h.

On the vertical sides dTheta=0; on the bottom and top, dTheta=2a0 xi dxi. Positive orientation traverses the bottom to the right and the top to the left. Thus

    -oint_(boundary D) H dTheta
       =2a0 integral_0^h xi[Htilde(xi,b)-Htilde(xi,0)] dxi.

Both this expression and integral_D Omega have the sign of a0 and are nonzero. Hence sign(a0) A_D>0. This proves the asserted nonzero coefficient using continuity alone, including beta=2 and any permissible flat jets elsewhere.

## 4. Spatial mass, sign, and weighted consequences

For large t, sign(a0)J_D(t)>=|A_D|e^((2 beta-1)t)/2. It is bounded above by integral_(phi_t D)(sign(a0)Omega)_+. Since phi_t D lies in x>0 and the ball of radius C e^(k t), positivity allows extension of this positive-part integral to that half-ball. Every sufficiently large radius is C e^(k t) for a unique real t, so (2) and (3) hold for all large R, not just a sequence.

For gamma>0, if M(R)>=c R^alpha then Fubini gives

    integral_{1<|X|} |Omega(X)| |X|^(-gamma) dX
      >= gamma integral_1^infinity R^(-gamma-1)[M(R)-M(1)] dR.

The right side diverges for gamma<=alpha. For gamma<=0 divergence already follows from unbounded M(R) and the weight bounded below outside the unit ball. Uniform o(r^(-1/beta)) would instead imply M(R)=o(R^(2-1/beta)), by splitting off a fixed inner ball and integrating the uniform tail. The alleged critical r^(-2/beta) bound yields an even smaller mass order, so it too is impossible.

## 5. All finite L^p through the critical p=2 beta under only sublinear velocity

For p=1, (2) contradicts finite total mass. For 1<p<2 beta, choose eta>0 small enough that

    2-2/p < (2 beta-1)/(beta+eta).

Holder on B_R gives M(R)<=C ||Omega||_p R^(2-2/p), contradicting (2).

It remains to treat p=2 beta, which is at least 4. The once-subtracted whole-plane kernel K(Z)=(Z_2,-Z_1)/(2 pi |Z|^2) satisfies, for p>2 and p'=p/(p-1),

    ||K(X-.)-K(-.)||_(L^p') <= C_p |X|^(1-2/p).                 (5)

Near either kernel singularity p'<2 ensures integrability; at infinity the difference is O(|X|/|Y|^2), where p'>1 ensures integrability. Dilation gives the displayed exponent. Holder defines a continuous relative inverse V_* with |V_*(X)|<=C_p||Omega||_p |X|^(1-2/p), V_*(0)=0. Its distributional div and curl are the prescribed ones. The difference V-V_* is an entire harmonic vector field, sublinear, hence constant by the harmonic gradient estimate on arbitrarily large balls. It vanishes at zero. Thus V=V_* and the stronger power radius bound applies.

At p=2 beta, (3) requires M(R)>=c R^(2-1/beta). But split at any fixed R1 and apply Holder only on the tail:

    M(R)/R^(2-1/beta)
       <= M(R1)/R^(2-1/beta)+C ||Omega||_(L^p(|X|>R1)).

First R tends to infinity, then R1 tends to infinity; the right side tends to zero. This contradicts (3) and proves the critical case. If Omega is additionally bounded, membership in 0<p<1 implies L^1 and is also excluded; boundedness is not assumed in the main statement.

## 6. Scope and corrections to the lead draft

The circulation coefficient A_D is an integrated quantity. Formula (1) does not prove a pointwise limit of e^t Omega(phi_t X), nor a pointwise angular vorticity expansion without further hypotheses. Such interpretations must be conditional on a separate convergence theorem. Also, positive circulation on D_t does not give a lower bound on the signed circulation of a larger half-ball. The positive-part form (2)-(3) is the valid conclusion.

The mass rate is compatible with a generic r^(-1/beta) tail. The theorem rules out the previously considered r^(-2/beta) critical-tail subclass, making conditional sign statements within that subclass vacuous after this stronger result is accepted. It does not rule out the full smooth B2 class and does not choose an absolute-velocity observer convention.

Dependencies: local center identities, smooth division by x, the smooth ODE flow, Reynolds transport on finite domains, Green's theorem, integration by parts on a closed curve, continuity and Fubini, and the elementary whole-plane kernel estimate (5). No numerical evidence is used as proof.
