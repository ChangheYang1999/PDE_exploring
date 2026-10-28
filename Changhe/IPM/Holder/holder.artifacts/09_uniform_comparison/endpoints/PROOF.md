# Uniform relative bounds near the two endpoint exponents

## Statement and definitions

Use the operator constants and homogeneous Hölder space in `../../01_setup/PROOF.md`. Define $a_2,a_3$ as in `../../02_upper_bounds/PROOF.md`, and put

$$b(\alpha)=\frac{2^{\alpha+1}}{3\pi},\qquad
s(\alpha)=\frac{2a_3(\alpha)+(1-\alpha)b(\alpha)}{2a_2(\alpha)},$$

$$F_b(\alpha)=\frac{2a_2(\alpha)s(\alpha)^\alpha}{\alpha(1-\alpha)}.$$

The earlier upper-bound proof gives $C_\alpha\le F_b(\alpha)$. The use of this single valid shell bound avoids any need to compare interval-valued alternatives.

The compact cusp lower bound

$$L_1(\alpha)=(\sqrt2-1)^\alpha\left(\frac4{\pi\alpha(\alpha+2)}-\frac14\right)$$

and the degree-three homogeneous lower bound $H(\alpha)$ satisfy $L_1,H\le C_\alpha$. The Arb certificates in `../../data/endpoint_ratio_certificates.json` establish

$$\frac{F_b(\alpha)}{L_1(\alpha)}\le1.0172482934
\quad(0<\alpha\le0.005),$$

$$\frac{F_b(\alpha)}{H(\alpha)}\le1.0262309397
\quad(0.995\le\alpha<1).$$

Thus a certified upper bound lies within 3 percent of the sharp $C_\alpha$ on these two entire endpoint intervals. This statement is not yet a uniform result on the middle exponent interval. The exact optimized upper bound $F$ is no larger than $F_b$ and inherits the same comparison.

## Removal of the endpoint singularities

At zero, multiply both the numerator and denominator by $\alpha$. The ratio becomes

$$\frac{2a_2(\alpha)s(\alpha)^\alpha/(1-\alpha)}
{(\sqrt2-1)^\alpha[4/(\pi(\alpha+2))-\alpha/4]}.$$

All factors extend continuously to $\alpha=0$, with positive denominator. This expression is evaluated directly on the closed interval $[0,0.005]$.

At one, write $\delta=1-\alpha$. The degree-three integral is

$$J_\alpha=\int_0^{\pi/6}\sin((\alpha+2)t)\sin^\alpha t\,dt.$$

Since $0\le\sin t\le1$, one has $\sin^\alpha t\ge\sin t$. Concavity of sine on $[0,\pi/2]$ gives

$$\sin((\alpha+2)t)\ge\frac{\alpha+2}{3}\sin(3t).$$

Consequently $J_\alpha\ge(\alpha+2)\sqrt3/48$, using the exact integral $J_1=\sqrt3/16$. Also $\delta/\sin(\pi\delta/6)\ge6/\pi$. Substituting in the previously proved homogeneous lower bound gives

$$\delta H(\alpha)\ge
\frac{(\alpha+1)(\alpha+2)\sqrt3}{8\pi}
+\frac{2^{1-\alpha}(1-\alpha)}4.$$

Therefore $F_b/H$ is at most the nonsingular expression

$$\frac{2a_2(\alpha)s(\alpha)^\alpha/\alpha}
{(\alpha+1)(\alpha+2)\sqrt3/(8\pi)+2^{1-\alpha}(1-\alpha)/4}.$$

It is evaluated on $[0.995,1]$. This lower bound is used only to upper-bound the ratio; no equality with the homogeneous witness is asserted away from the limit.

## Interval verification

`../../code/certify_endpoint_ratios.py` uses 256-bit Arb arithmetic. The exact positive-series enclosure of $a_3$ is reused from the original upper certificate, with its proved tail estimate; its operations accept an interval exponent and therefore enclose every exponent in the interval. All other operations are elementary positive powers and rational operations with denominators separated from zero. The final displayed decimal is the ceiling of the upper interval endpoint at ten decimal places. The source and dependency hashes are recorded in the JSON output. These are interval-domain certificates, not tests at sampled exponents.
