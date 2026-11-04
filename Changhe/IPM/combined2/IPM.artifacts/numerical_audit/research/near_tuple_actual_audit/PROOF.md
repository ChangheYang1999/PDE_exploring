# Independent arithmetic for the near-bound tuple

Prepared on 2026-11-04 before the new tuple is published or checked.

## Exact statement and hypotheses

Fix c=4076476460239181/2251799813685248, q=21/10, sigma=1, r0=1/2, t=1/10, nu=1/40, and C_D=80127/40000. The exact Source013, near coefficient a_n and all full-plane norms have the meanings in ../source013_near_norms/PROOF.md. Let a_c(X)=c/(1+4|X|^2), a_r=a_n+a_c. Assume the previously admitted radial subtraction bounds D_j(a_r)^2 <= D_j(a_n)^2-K_j, for j=4,5,6, the NR25 Fourier bounds, the NR32 radial tail bound, and the HF1-NEAR localization inequality with its stated domains. This audit does not re-prove them.

Let d_j be the exact upper endpoint in the actually adopted whole-plane near result. Let K_j be certified lower subtraction constants with d_j^2>K_j. Put r_j=sqrt(d_j^2-K_j), x0=(q/2)log2, A=pi^2(1+q^2(sinh(x0)/x0)^2)+C_D/2 and M=sqrt((r4*r6+r5^2)/(2pi)). For v>2q+1, set

    U(v)=c*sqrt(pi)*v^(q+3/2)*exp(-v/2)/(2*(v-2q-1)),
    T(v)=r6*v^(q-5)/sqrt(4pi*(5-q)),
    B(f,mu)=(4/3)^q*f(3mu/4)+(8/mu)^q*f(mu/2).

For certified upper bounds Lambda, Sminus, Splus and L on Lambda_+(a_n), sup((a_n)_-W^2), sup((a_n)_+W^2) and ||(a_n)_+||1, respectively, and mu>=1 with 2nu<=mu and mu/2>2q+1, the five scalar loss terms are

    e1=(1+q^2)*max(Lambda,8*(2c-1))/(2mu^2),
    e2=A*(1024c+M)/mu^4,
    e3=B(U,mu), e4=B(T,mu), e5=L*nu^2/(8t*sqrt(2pi)).

Let E_i be their displayed rational upper bounds, E a rational upper for their exact displayed sum, P an upper for 2^sigma*(max(Sminus,Splus)*kappa0*kappa2q+2*Splus*kappaj^2/(1-t)), and D a lower for the stated allowance. Then the displayed cap margin is valid if it is at most c+1-q-b0-E. The displayed H4 rate margin is valid if it is at most beta_star-b0-eps_rest-E. The displayed remaining allowance and price ratio must be at most D-P and at least P/D, respectively, where D>0.

## Argument

The admitted radial subtraction bounds give D_j(a_r)<=r_j by positivity of the square root. NR25 and NR32 give M4(a_r)<=M and the two tail bounds T and U. The absolute Fourier moment is subadditive under a_n=a_r-a_c. Substitution in the admitted localization inequality gives the sum of the five displayed scalar expressions. Replacing each by a containing upper and then rounding their displayed sum upwards preserves the inequality. All later margins are differences of exact displayed rationals, so they must use that same E and P. The price expression has only rational arithmetic at these fixed parameters. An interval evaluation at higher precision bounds each transcendental expression independently.

For any reported D6 or Lambda grid threshold, checking the threshold and its next grid point proves the reported transition for this numerical interface provided its monotonicity and the specified search interval hold. It does not prove an optimal analytical threshold. The same distinction applies to a positive margin: eps_rest=0 is an OPEN placeholder, not a certified zero loss. UNAUDITED fallback kernel constants or allowances remain UNAUDITED even when their scalar arithmetic passes.

## Verification and scope

The independent checker will use exact rationals and 768-bit Arb, with no import or execution of the producer's code. Its actual input copy, source hashes, source and norm-adoption bindings, side conditions, displayed arithmetic and threshold comparisons will be recorded in verification/. It will distinguish the actual plan from the fallback, and preserve all noncertified input names.

Before verification records exist, this is a prepared checking method only. A passing future check confirms numerical arithmetic under the named analytic premises; it supplies no missing H4 remainder estimate, full inverse, invariant ball or existence theorem.
