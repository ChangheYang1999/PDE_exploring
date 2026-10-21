# Fifth-order obstruction on the compatible R12 axis data

Checked independently by the verifier on 2026-10-20. This is a statement about prescribed axis data. It does not establish existence of a coupled profile or nonexistence for the whole admissible class.

## Statement and notation

Let A > 1, L > 0, u = x/L, and on 0 < x < L prescribe

    w = -A x (1-u^2)/(1+u^2),     g = x^2/(1+u^2),
    h = A+1-w',                  S_A = 6A(4A-3)/(8A-1).

Assume L^2 = S_A. Use the axis transport hierarchy and elliptic coefficient identities

    a_2 = (g'-w'')/2,             b_3 = -a_2'/3,
    a_4 = (b_3'+G_3')/4,          b_5 = -a_4'/5,
    w G_3' + (3h-1)G_3 = F_3,     F_3 = -a_2 g' - b_3 g,
    w G_5' + (5h-1)G_5 = F_5,     F_5 = -a_2 G_3' - 3b_3 G_3 - a_4 g' - b_5 g.

Here G_j is the coefficient of y^j in the odd Taylor expansion of the density along the x-axis. Select G_3 by G_3/H_3 -> 0 at x = L. Define H_j as the positive homogeneous solution normalized by H_j/x^{p_j} -> 1 at 0, where p_j = 2j+(j-1)/A. For A in (1,4), A != 2, define

    B_5 = - FP integral_0^L F_5/(w H_5) dx,

where FP removes exactly the divergent powers at 0, with no finite constant added. Then

    G_3 = 10A u^2 / ((8A-1)(1+u^2)^3),
    B_5 = P(A) Beta(-4-2/A,4/A) /
          [15A(2A-1)(3A-2)(4A-3)(8A-1)L^{10+4/A}],
    P(A) = 1248A^4 - 548A^3 + 297A^2 - 178A + 84,

and B_5 < 0 throughout both (1,2) and (2,4). Beta denotes its meromorphic continuation. At A=2, L=2, the logarithmic coefficient of the integral is zero and the directly evaluated resonant finite part is +11/1474560. The nonresonant limit along L^2=S_A is -11/1474560. Their difference is -11/737280.

The selection of G_3 is a hypothesis of this statement. Its validity for an actual profile requires a separate source regularity result. The result itself supplies no such theorem.

## Proof

The axis equation for g is w g' = (w'-A)g, verified by substitution. Its normalization is g/x^2 -> 1. Put q_j=(j-1)/A. Direct logarithmic differentiation gives

    H_j = A^{q_j} g^{j+q_j}|w|^{-q_j}
        = x^{p_j}(1+u^2)^{-j}(1-u^2)^{-q_j}.

Indeed H_j'/H_j = (1-jh)/w and its normalization at 0 is as specified. It diverges at L with exponent -q_j.

Substitute the displayed rational G_3 into the third equation, using L^2=S_A. Clearing denominators makes the residual the zero polynomial. It is bounded at L, so G_3/H_3 tends to zero. Any two solutions differ by a multiple of H_3, so this establishes uniqueness under that endpoint selection. The independent symbolic reconstruction in code/check_axis.py performs the substitution from the stated w and g, including all differentiations.

The fifth source obtained from this G_3 is

    F_5 = u^2 [c_0+c_2 u^2+c_4 u^4] /
          [15(4A-3)(8A-1)(1+u^2)^6],
    c_0 = 2076A^2+741A-36,
    c_2 = -3060A^2+305A-70,
    c_4 = 1400A^2-950A+50.

Because -dx/(w H_5) = (A L^{p_5})^{-1}
 u^{-p_5-1}(1+u^2)^6(1-u^2)^{4/A-1} du, cancellation gives

    B_5 = 1/[15A(4A-3)(8A-1)L^{p_5}]
          FP integral_0^1 u^{1-p_5}(c_0+c_2u^2+c_4u^4)
                          (1-u^2)^{4/A-1} du.

Set t=u^2 and a=-4-2/A, q=4/A. Each monomial integral is (1/2)Beta(a+j,q), j=0,1,2. To justify this equality for negative a, first define the integral for Re(a)>0. Subtract finitely many Taylor terms of (1-t)^{q-1} at t=0 and integrate these terms explicitly. The remaining integral is convergent in a successively larger left half-plane, and the explicit terms are meromorphic there. At non-pole a this continuation is exactly the finite part specified above. Substitution t=u^2 preserves the constant term because it merely replaces each lower-end power by its corresponding t-power. Thus the calculation uses precisely the stated finite-part convention.

The beta recurrence gives Beta(a+j,q)=Beta(a,q)(a)_j/(a+q)_j. Reducing the quadratic expression yields P(A) divided by the stated denominator. All recurrence denominators are nonzero on (1,4). At A=2 the limiting recurrence can still be used for the limit, but it does not replace direct evaluation at resonance.

For z=A-1,

    P(1+z)=1248z^4+4444z^3+6141z^2+3764z+903 > 0.

On 1<A<2, a is in (-6,-5), a+q is in (-3,-2), so Gamma(a)>0 and Gamma(a+q)<0. On 2<A<4, a is in (-5,-9/2), a+q is in (-7/2,-3), so Gamma(a)<0 and Gamma(a+q)>0. Gamma(q)>0 in both cases. This proves the asserted negative sign without sampling.

At A=2 the reduced integrand is a Laurent polynomial proportional to
 u^{-11}(c_0+c_2u^2+c_4u^4)(1-u^2). It contains no u^{-1} term. Integrating every monomial and retaining its constant term gives +11/1474560, as also checked using exact rationals in verification/axis.json. On the curve approaching A=2,

    a=-5+(A-2)/2+O((A-2)^2),
    a+q=-3-(A-2)/2+O((A-2)^2),

and the gamma residues give Beta(a,q) -> -1/20. Substitution into the prefactor gives -11/1474560. The jump is therefore -11/737280. It is not a numerical quadrature artifact.

Finally F_5 is smooth up to x=L and F_5/(w H_5)=O((L-x)^{4/A-1}), which is integrable for A>0. For every solution G_5 on (0,L) its normalized limit ell_5 therefore exists. Integrating the first-order equation shows that its center homogeneous coefficient is C_{0,5}=ell_5+B_5. In the nonresonant range, a smooth even center requires C_{0,5}=0. Thus, when the third selection hypothesis holds, a smooth-center solution would require ell_5=-B_5>0. If a separate regularity theorem forces ell_5=0, it rules out these axis data. Without that theorem, the cancellation remains possible as far as this argument goes.

## Dependencies, evidence and scope

Only the displayed axis hierarchy, elementary differentiation, and the Euler beta integral and recurrence are used. The hierarchy can be derived by expanding W.grad rho=rho, div W=2c_l, and curl W=-rho_x in powers of y, with A=2c_l-1. The derivation above has been reconstructed independently, rather than importing the lead's formula or numerical evaluator. Exact symbolic checks and 55-digit numerical evaluations are in verification/axis.json. No formal proof-assistant run is claimed.

The additional claim that class regularity gives the third source selection on 1<A<2, or that C^(4,alpha) regularity forces both source selections on 1<A<=4, is not proved here. The lead's source theorems must be audited separately before those conditional consequences can be applied to profiles. This result does not establish NO_inf for all profiles and does not establish a coupled profile with these axis data.

## Endpoint A tending to one

Write A=1+delta. Then a=-6+2delta+O(delta^2), a+q=-2-2delta+O(delta^2), and q tends to 4. The residues Gamma(-m+epsilon)~(-1)^m/(m! epsilon) give Beta(a,q) tending to -1/60. The rational prefactor without L^{-p_5} tends to 43/5, L^2 tends to 6/7, and p_5 tends to 14. Hence B_5 tends to -(43/300)(7/6)^7. Multiplication by L^{p_5-4} gives the natural-unit limit -2107/10800. This is a limit from the nonresonant curve, not a finite-part definition at A=1.

## Parameter paths through the fifth resonance

This calculation concerns the R12 finite-part functional with the third coefficient selected by zero normalized source limit. It does not assert that these axis data are realized by a profile. Put $S=L^2$ and keep $S$ independent of $A$. Near $(A,S)=(2,4)$, write the regular even part of $G_3$ as $\sum_{m\geq0}c_{2m}x^{2m}$. Its coefficients are uniquely determined by
\[
 wG_3'+(3h-1)G_3=F_3,\qquad
 (6A+2-2mA)c_{2m}=\text{the lower-order forcing coefficient}.
\]
None of these denominators vanishes near $A=2$ for the finite orders used below. The possible additional third homogeneous term has exponent $p_3=6+2/A$, near seven. In the fifth finite-part integrand it contributes powers with integral denominators $p_3-p_5+2m$, near odd integers, so it creates no pole at this fifth resonance.

Define $E_{12}(A,S)$ to be the coefficient of $x^{12}$ in
\[
 \frac{F_5(x)}{A}(1+x^2/S)^6(1-x^2/S)^{4/A-1},
\]
using the regular even part of $G_3$. The full integrand for $B_5$ is this expression times $x^{-11-4/A}$. Consequently the corresponding integrated monomial has coefficient $E_{12}/(2-4/A)$. Exact power-series recursion gives
\[
 E_{12}(2,4)=0,\quad
 \partial_A E_{12}(2,4)=\frac{1049}{3686400},\quad
 \partial_S E_{12}(2,4)=-\frac1{10240}.
\]
The recursion, including both first parameter derivatives, is implemented with rational dual numbers in `code/resonance_path.py`. Each step is rational arithmetic; the complete coefficients are in `verification/resonance_path.json`.

After subtracting finitely many center powers on a fixed small interval, all other terms of the finite part depend continuously on $(A,S)$ near $(2,4)$. The source-selected third solution also depends smoothly on these parameters: its integrating-factor integral converges uniformly at the source, and its center homogeneous coefficient is a nonresonant third finite part. The fifth source integral has the same uniform convergence since $4/A>0$. The regularized center remainder can be differentiated and bounded uniformly after enough terms are removed. These observations justify isolating the single monomial above. Thus for $S=4+\lambda(A-2)+o(A-2)$,
\[
 \lim B_5(A,S)=\frac{11}{1474560}
  +\frac{1049}{3686400}-\frac{\lambda}{10240}.
\]
For the zero-$B_3$ curve, $S_A'(2)=46/15$, so its jump is $-11/737280$ and its limit is $-11/1474560$. For fixed $S=4$, the limit instead is $2153/7372800$. This proves that there is no path-independent limit, independently of the earlier numerical observation.

There is also a correction to an inherited statement. The exact Laurent-polynomial calculation at fixed $A=2$ gives
\[
 E_{12}(2,S)=\frac{4(S-10)(S-4)}{15S^7}.
\]
Hence the fifth logarithmic coefficient vanishes at both $S=4$ and $S=10$. The inherited D56 addendum's assertion that it vanishes on R12 only at $L=2$ is false without an extra restriction to zero-$B_3$ data. Code: `code/resonance_log_polynomial.py`; evidence: `verification/resonance_log_polynomial.json`. Its elementary polynomial arithmetic supplies the coefficient exactly. At $S=10$, the third functional is nonzero, so this additional fifth log zero does not give smooth-center compatibility. The report's separate statement of path dependence is unaffected.
