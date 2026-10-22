# A fixed spline envelope fixes the admissible exponent

Status: CONFIRMED by independent proof and actual Opus89 review, with its two side-hypothesis clarifications adopted. The proof uses the previously established nonzero slow-tail theorem. This is a restriction of a numerical representation, not a full B2 exclusion. Actual creation time is in verification/README.md.

## Statement and hypotheses

Let the representation parameter be $b\in(2,4)$, and let $L>0$. Define

$$
z=\left(1+(r/L)^2\right)^{-1/(2b)},\qquad t=1-z,
\qquad \rho=\frac r{\sqrt{r^2+L^2}}.
$$

Suppose the represented vorticity is

$$
\Omega(r,\theta)=r\cos\theta\,z^{b+1}
 \sum_{k=0}^{K-1} P_k(t)\rho^{\epsilon_k}
 T_k(-\sin\theta),\qquad \epsilon_k\in\{0,1\}, \tag{1}
$$

where $T_k$ are Chebyshev polynomials and each $P_k$ is an ordinary polynomial on some final interval $t_*<t<1$. Formula (1) holds exactly for every sufficiently large radius in the same centered polar coordinates as (2); the spline has finitely many pieces, not knots accumulating at the endpoint. This includes the last span of the numerics lane's finite spline representation. The angular coefficient mask at the origin does not affect this assumption.

Assume this vorticity belongs to a smooth exact B2 profile in the prompt's class A. The already independently proved tail theorem states that its dynamical exponent $\beta$ satisfies $\beta\ge2$ and

$$
 r^{1/\beta}\Omega(r,\theta)\longrightarrow a(\theta)
 \quad\hbox{uniformly},\qquad a\not\equiv0. \tag{2}
$$

Then necessarily $\beta=b$. Therefore fixing $b$ in this range does not allow an exact profile with a different free dynamical exponent in this representation. This conclusion does not assert that a profile with $\beta=b$ exists. Packet84 independently excludes any exact finite angular support under its smoothness assumptions; the present argument isolates the additional restriction caused by the radial envelope, and extends to an enlarged angular representation only if a smallest endpoint order is attained, the resulting leading angular function is nonzero, and the remainder is uniformly smaller. These conditions are automatic for the finite sum in (1), and are extra hypotheses for an infinite sum.

## Proof

If every $P_k$ is the zero polynomial on its final interval, then $\Omega$ vanishes outside a ball, contradicting (2). Otherwise let $j\ge0$ be the smallest order of vanishing at $t=1$ among the nonzero $P_k$. For real coefficients $p_k$, not all zero,

$$
 P_k(1-z)=p_kz^j+O(z^{j+1}).
$$

Also $\rho=(1-z^{2b})^{1/2}=1+O(z^{2b})$ and
$r=Lz^{-b}(1-z^{2b})^{1/2}$. Hence (1) gives, uniformly in angle,

$$
 \Omega=Lz^{j+1}\cos\theta
 \left(\sum_kp_kT_k(-\sin\theta)+o(1)\right).
$$

The angular polynomial in parentheses cannot vanish identically: the $T_k$ are linearly independent on $[-1,1]$, and $-\sin\theta$ ranges over the interior of this interval where $\cos\theta\ne0$. Consequently

$$
 \Omega(r,\theta)=r^{-(j+1)/b}\bigl(A(\theta)+o(1)\bigr),
 \qquad A\not\equiv0. \tag{3}
$$

Two uniform power asymptotics with nonzero limiting angular functions must have the same exponent. Indeed, choose a direction where the coefficient in (3) is nonzero to exclude one strict inequality, and a direction where $a$ in (2) is nonzero to exclude the opposite inequality. Thus

$$
 \frac1\beta=\frac{j+1}{b},\qquad \beta=\frac b{j+1}.
$$

Since $\beta\ge2$ and $b<4$, any $j\ge1$ is impossible. Hence $j=0$ and $\beta=b$, as claimed.

This proof uses the exact slow-tail theorem, not merely a formal balance at one direction. In particular it covers possible temperature-tail cancellations without assuming their absence.

## Quantifying a mismatch in the leading transport terms

For fields with nonzero leading radial coefficients

$$
 \Omega=r^{-1/b}(A(\theta)+o(1)),\qquad
 \Theta=r^{1-2/b}(H(\theta)+o(1)),
$$

and differentiated asymptotics, any sublinear velocity whose derivatives have the usual decaying order gives

$$
 R_\Omega=(1-\beta/b)r^{-1/b}A+o(r^{-1/b}),
\qquad
 R_\Theta=2(1-\beta/b)r^{1-2/b}H+o(r^{1-2/b}). \tag{4}
$$

To verify (4), $\beta X\cdot\nabla$ acts on the radial powers by $-\beta/b$ and $\beta(1-2/b)$ respectively. The terms $V\cdot\nabla\Omega$ and $\Theta_x$ are lower order than $r^{-1/b}$, while $V\cdot\nabla\Theta$ is lower order than $r^{1-2/b}$. Subtracting the zeroth-order profile terms gives the displayed factors. The same conclusion holds for a fixed sublinear auxiliary velocity in a forcing homotopy. It is a far-field consistency diagnostic, not a global residual estimate.

## Reinterpreting source coefficients changes the source

Let $P_k$ be fixed coefficient polynomials for a nonzero source whose first endpoint jet has order $j=0$. Interpret the same coefficient arrays once with $b=b_S$ and once with $b=b_C\ne b_S$, holding $L$ fixed. Formula (3) then gives different nonzero leading exponents $1/b_S$ and $1/b_C$. Thus these two functions cannot be the same physical source, even though their coefficient arrays are identical.

In particular, if $b_C>b_S$, the reinterpreted source has the slower tail. At a direction with nonzero leading coefficient,

$$
 r^{1/b_S}|f_C-f_S|\longrightarrow\infty.
$$

A zero center-strain functional need not detect the change. For the lane's actual representation, $\epsilon_k=1$ for odd $k$ and zero for even $k$. This restriction matters for the following strain formula. In the angle $\varphi=\theta+\pi/2$, the coefficient of $\sin(2\varphi)$ in vorticity is $r z^{b+1}\rho(P_1-P_3)/2$, with $P_3=0$ if absent. The exact modal strain formula and the change of variables $\rho z^{b+1}dr=bLdt$ give

$$
 c=-\frac14\int_0^\infty z^{b+1}\rho(P_1-P_3)\,dr
   =-\frac{bL}{4}\int_0^1(P_1-P_3)\,dt.
$$

Thus the exact strain is $-bL/4$ times a fixed linear functional of the coefficient arrays. If that functional vanishes, it vanishes for every $b$, although the represented source has changed. This formula is specific to the actual odd-index $\rho$ factors, and is not claimed for arbitrary assignments of $\epsilon_k$ in (1). A small or zero strain mismatch is therefore insufficient to certify preservation of the physical source.

## Application to the inspected driver

The source snapshot in verification/fixed_basis_driver_20261020T2250 is read-only evidence. Its build function uses $b=\texttt{cur\_bb}$ when fixed_basis is enabled and adds the raw array $\lambda\,\texttt{cG\_fsrc}$ in this same basis. The blam12f restart has $\texttt{cur\_bb}=3.0035421536489726$ while its source metadata has $b_S=3$. Thus this source is fixed across those new stages but differs from the original seed source. The blam16f initial state has both parameters equal to three and avoids this particular mismatch.

For both runs, keeping the unknown-field envelope fixed near three adds the exponent restriction proved above to any proposed unforced endpoint. The class-A tail theorem is not being assumed for intermediate forced states. A representation that keeps the unknown-field envelope tied to the dynamical exponent while evaluating the fixed-source inverse separately avoids these two particular restrictions. No claim is made here about convergence or existence for that alternative.

## Dependencies and scope

Dependencies: packet40's admissible-class reduction; the nonzero slow-vorticity-tail theorem, already independently checked; elementary polynomial endpoint expansions; and the explicitly displayed serialized basis formula. The numerical source comparison is supplementary evidence. No solver code from the numerics lane is executed or imported. This result leaves the full B2 problem open.
