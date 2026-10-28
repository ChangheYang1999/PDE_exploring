# Quadratic recombination of the finer producer certificate

## Statement

For the real homogeneous seminorm [f]_(3/4)=sup_(z!=w)|f(z)-f(w)|/|z-w|^(3/4), let T_xx be the circular principal-value operator with kernel (z_1^2-z_2^2)/(2pi|z|^4), defined modulo constants by its convergent increments. Put D_(3/4)=||T_xx-I/2||. Use the exact polygon-plus-projection witness of the parent proof, with b=3/4, c=-3/10 and lambda=50/53. Its global profile certificate gives [f]_(3/4)<=1, f(0)=1/2 and f(e_1)=-1/2.

The exact positive increment lower endpoint constructed below, plus 1/2, is a lower bound for D_(3/4). The smooth compact approximation theorem gives the same lower bound when the defining supremum is restricted to real C_c^infinity functions. No pointwise integral at infinity or full Holder norm is used. The final exact endpoint and its downward decimal rounding are specified by independent_audit.json and admitted only by accepted.json.

## Finite integration contract

The parent proof explains the 3961 imported tasks and their exact decimal endpoints. Their 59232568 cells cover the near-pole annuli up to radius 1/2 and the remaining midpoint annuli up to R=10^16, with the exclusions defined by the frozen cell evaluator. Near-pole tasks evaluate one disk; reflection makes the other contribution equal. Every midpoint and radius text uncertainty is retained in the imported rational interval.

An exact coverage check and an audit of the cell formulas are mandatory. Seventy complete tasks, including both endpoints, changes in angular resolution and extreme error contributions, are independently recomputed. This corroborates the producer calculation but is not a complete independent replay of all fine-mesh cells. The complete coarser replay is the separate V233 certificate.

Choose a retained near-system starting radius epsilon from a task endpoint. Sum every retained near interval as [N_-,N_+] and every midpoint interval as [W_-,W_+], using exact rational arithmetic. Discarded near intervals are replaced by the analytic pole bound, never counted twice. Optimization over finitely many admissible endpoints merely selects the largest proved lower endpoint.

## Pole disks

Write alpha=3/4, k=2^(alpha-1), C_e=(1-2epsilon)^(alpha-1), and

    A=Gamma(1+alpha/2)/(2sqrt(pi)Gamma(3/2+alpha/2)),
    M=lambda A epsilon^alpha/alpha+epsilon^2/4,
    E_c=alpha C_e^3 epsilon^(3-2alpha)/(6pi lambda^2(3-2alpha)),
    E_s=epsilon^(alpha+2)/((alpha+2)(1-epsilon)^2).

Require epsilon in (0,1/2), (lambda+k)epsilon^alpha<=c+1/2, and lambda epsilon^alpha<=1/2. The independently accepted quadratic pole theorem then bounds each omitted disk from below by M-E_c-E_s. Its proof keeps the nonnegative kernel part of the clamp and integrates the negative part using P(u)>=alpha |u|^alpha(-u_1/|u|)^2. The projection profile contributes lambda A epsilon^alpha/alpha; the smooth opposite-pole constant contributes epsilon^2/4 by harmonicity. This is exactly the circular principal value because the subtracted own-pole constant has zero angular mean.

For the upper endpoint set U_c=0 if alpha C_e epsilon^(1-alpha)<=lambda/2, as the sign-controlled pole theorem then applies. Otherwise take U_c=alpha C_e epsilon/pi. The upper pole contribution is M+E_s+U_c. Every inequality is checked by directed ball endpoints.

## Exterior and midpoint sliver

Put H=sqrt((b+1/2)^2+b^2), B=max(H^alpha+|c|,1/2+2^(-alpha)), q=1/(4R^2). Require lambda(1+2^(-alpha))>=1. The accepted homogeneous exterior theorem and its angular refinement give the exterior main term and error

    T=2a_3(alpha)R^(alpha-1)/(1-alpha),
    E_T=4B/(pi R)+B/(3R^3(1-q)^2)
                       +R^(alpha-3)/(2(3-alpha)(1-q)^2).

Here a_3 is the explicitly integrated six-lobe angular coefficient in the cited exterior proof. The independent auditor evaluates it through the accepted formula. The midpoint hole has radius eta=1/100 and absolute contribution at most

    E_0=2^(alpha+3)eta^(alpha+3)/(pi(alpha+3)sqrt(1-eta^2)).

These estimates include convergence at infinity: alpha<1 makes the dipole radial integral convergent. All constants are represented by outward rational endpoints.

## Final recombination and scope

Using lower or upper directed endpoints as indicated, the complete trace-free increment lies in [L,U], where

    L=2N_-+W_-+T_-+2M_--2(E_c)_+-2(E_s)_+-(E_T)_+-(E_0)_+,
    U=2N_++W_++T_++2M_++2(E_s)_++2(U_c)_++(E_T)_++(E_0)_+.

The identity term contributes exactly +1/2. Hence D_(3/4)>=1/2+max(0,L,-U). Taking the maximum over finitely many valid epsilon values preserves the inequality. Round the resulting rational lower endpoint downward at ten decimal places. The acceptance record binds every imported task, source, profile proof, omitted-region proof, selected replay, and arithmetic record. It explicitly retains the distinction between an audited producer certificate and a complete independent fine-mesh replay.
