# Certificate inventory and the exclusion theorem

**Status: CONFIRMED as a reference-dependent exclusion theorem, with the stated PDE obstruction as an input.** The rational references have numerical radii proved by rational inequalities. The fitted reference of [../../reference_fit/PROOF.md](../../reference_fit/PROOF.md) has certified compatibility and negativity, but its obstruction and exclusion constants have not been certified here.

Dependencies: `01-differential/PROOF.md`, `02-remainder/PROOF.md`, `03-norm-and-radius/PROOF.md`; the PDE endpoint implication in `FINAL_REPORT.md`, §6.3.1(h), including its stated inputs. This file distinguishes those inputs from the new estimates.

## 1. Complete inventory for a polynomial reference

Freeze \(A_0>2,e_0>0\) and every coefficient of \(q\) as exact numbers, or supply certified enclosing intervals throughout. Define
\[
H(t)=A_0-t(1-t^2)q(t),\qquad
w_0(u)=-\frac{u(1-u^2)}{1+u^2}H(u^2).
\]
The finite calculations to be supplied are the following.

1. **Geometry and scalar margins.** Prove
   \[
   H_{\min}=\inf_{0\le t\le1}H(t)>0.
   \]
   This proves the source conditions and negativity. In particular
   \[
   \mu_0=\inf_{0<u<1}\frac{-w_0(u)}{u(1-u)}
   =\inf_{0<u<1}\frac{1+u}{1+u^2}H(u^2)\ge H_{\min}.
   \]
   Choose \(h,h',r,\sigma,\theta,\tau\) and check \(e_0-h'>0\), \(A_0-h-\tau>2\), \(\sigma>2/(A_0-h-\tau)\), and \(\theta+2/(A_0+h+\tau)>1\). For the modulus variant use the two quantities in (29) instead of the last margin.

2. **Reconstruction and endpoint values.** Compute the explicit one-dimensional integral
   \[
   T(t)=\frac12\int_0^t\frac{(1+s)^2q(s)}{H(s)}\,ds,\qquad
   g_0(u)=\frac{u^2H(u^2)}{A_0(1+u^2)}\exp T(u^2).             \tag{37}
   \]
   Its derivation is in the next proof. Thus
   \[
   g_*=\tfrac12\exp T(1)>0,\quad
   w_{2*}=A_0+8q(1),\quad k_0(1)=w_{2*}/A_0,
   \]
   \[
   Q_0(1)=\frac{w_{2*}}{2A_0g_*^2}
          -\frac{e_0w_{2*}}{2g_*^3}.
   \]
   Derivatives of (37) are explicit in \(H,q,T\); no new differential equation has to be solved. Bounds for \(\inf g_0/u^2\) and \(\sup g_0/u^2\) can be obtained from this same formula. The constants below use more specific norms of \(g_0^{-2},g_0^{-3}\), so these two bounds alone do not replace the inventory.

3. **Origin data.** With the algebra norm (16), certify
   \[
   Z=\|z_0\|_{\mathcal A},\quad n=\|z_0^{-1}\|_{\mathcal A},
   \quad D=\|uz_0'\|_{\mathcal A},\quad
   J=\|-w_0''/(A_0u)\|_{\mathcal A},\quad E_o=\|E_0\|_{\mathcal A},
   \]
   where
   \[
   z_0=\frac{(1-u^2)H(u^2)}{A_0(1+u^2)},\qquad
   E_0=-\log(1-u^2)+T(u^2).
   \]
   Each norm is three Taylor coefficients and one weighted supremum on \((0,r]\). Taylor coefficients through order 9 of \(w_0\) suffice to identify the removable origin limits of the second-derivative remainders when \(\sigma\le2\). The supremum over the rest of the interval still needs a bound; a finite jet alone is insufficient. Check \(1-(2+b_+)E_o>0\), reducing \(r\) if necessary.

4. **Tail data.** Put \(a_0=-w_0/(1-u)\), \(k_0=(w_0'-A_0)/w_0\). With \(S,H\) defined in the second proof, certify
   \[
   \inf_{[r,1]}a_0,\quad H(a_0),\quad S(k_0),\quad H(k_0),
   \quad S(w_0''),\quad H(w_0''),
   \]
   \[
   S(g_0^{-p}),\ H(g_0^{-p})\quad(p=2,3),\qquad
   \max_{b\in\{b_-,b_+\}}\sup_{[r,1]}
   (a_0/A_0)^{b-2}g_0^{1-b}.
   \]
   These are finitely many one-dimensional suprema and an infimum. A third-derivative supremum is one convenient way of bounding an anchored seminorm; it is not a regularity requirement on neighboring traces.

5. **Small parameter derivatives.** Compute or majorize the finite-part integrals \(B_A,B_e\) in (9)–(10) at the reference, and the two suprema \(K_{AA},K_{Ae}\) in (25). The formulas following (25) specify them by one-dimensional integrals with zero, one, or two powers of \(\log[-w_0/(A_0g_0)]\). In each finite part use the three subtraction terms in (24), including their derivatives. There is only one real parameter in these suprema: dependence on \(e\) is affine, so its two endpoints suffice. An alternative is to bound each of those one-dimensional integrals uniformly over the parameter interval.

6. **Nonvanishing obstruction.** Compute (24) at \(A_0,e_0,\zeta=0\), or the equivalent \(m\)-integral in the question, with a certified error. Produce a number
   \[
   0<b_0\le|\mathcal B(A_0,e_0,w_0)|.
   \]
   It is enough to exclude zero by a comfortable margin; 30 correct digits are unnecessary for this purpose.

Equations (19)–(23), (26), and (32) now use just arithmetic in this inventory. No additional supremum over neighboring traces, unknown PDE solutions, or infinite-dimensional variational problem is hidden in the constants. If desired, the three first-variation jet coefficients are given by (8); computing them sharply is optional because \(D_N=M/d\) already bounds the whole differential.

For a theorem, all inequalities used to make \(d,\delta_0,M,M_e,D_A,D_e,K_{AA},K_{Ae},b_0\) valid need proved bounds. These can be analytic inequalities, exact rational polynomial certificates, or interval bounds with controlled quadrature error. They need not all be produced by an interval library. Two separately written codes agreeing to 30 digits provide valuable error detection, but do not by themselves certify even the sign of an improper or finite-part integral.

Only item 6 is used exclusively through the single scalar \(\mathcal B_0\). The reconstruction, origin data, and tail data also control derivatives and the remainder. Accurate computation of \(\mathcal B_0\) therefore does not replace their certification. Item 5 is likewise separate from the value of \(\mathcal B_0\). Sampled fitting errors and the stored trial's value of \(g_*\) enter none of the theorem's constants.

## 2. Precise theorem

**Theorem.** Let \(w_0,A_0,e_0\), the norm \(N\), and all constants satisfy the hypotheses and bounds of the preceding three proofs. Assume \(b_0>0\) and the parameter margin \(m\) in (32) is positive. Let \(\varepsilon\) be (32), or any smaller positive number.

There is no exact profile with all the following properties.

* It belongs to Setting I, \(P_\infty\): \(\rho\) is real, even in \(x\), odd in \(y\), is \(C^{2,\alpha_{\rm loc}}_{\rm loc}\) for some positive Hölder exponent as in the question, and is \(x^2y\,a(x,y)\) near zero with \(a\) smooth and \(a(0)=1\). It satisfies the canonical sublinear velocity law, the stated growth assumptions of the profile class, and
  \[
  W\cdot\nabla\rho=\rho,\quad W=c_lX+U,\quad
  U=(-\psi_y,\psi_x),\quad-\Delta\psi=\partial_x\rho.
  \]
* \(A=2c_l-1\) satisfies \(|A-A_0|\le h\). Its first positive source is \(P=(L,0)\), where
  \[
  e=L^{-2},\qquad |e-e_0|\le h'.
  \]
* At \(P\), either \(\rho\in C^{2,\alpha}\) on a neighborhood for some \(\alpha\in(0,1)\) with
  \(\alpha>1-2/A\), or the following precise cone condition holds: \(\rho,W\) are \(C^2\) near \(P\), and for some \(C,\kappa,r_0>0\) and such an \(\alpha\),
  \[
  |\rho_{yy}(x,y)|\le C|y|^\alpha,\qquad
  |(W_1)_{yy}(x,y)-(W_1)_{yy}(P)|
       \le C|(x-L,y)|^\alpha
  \]
  whenever \(L-r_0<x<L\) and \(|y|<\kappa(L-x)\).
* The normalized trace is
  \[
  \widetilde w(u)=W_1(Lu,0)/L,\qquad 0\le u\le1.
  \]
  It is compatible, with the origin expansion and endpoint regularity of the affine space in (12), and
  \[
  \left\|\widetilde w-\frac{A}{A_0}w_0\right\|_N
       \le\varepsilon.                                     \tag{38}
  \]

Here the PDE input is precisely the implication from §6.3.1(h), with its axis-propagation/third-axis-equation input:
\[
\text{the preceding profile and endpoint hypotheses}
\quad\Longrightarrow\quad B_3=0.                            \tag{39}
\]
If that implication is not being taken as a supplied theorem, add explicitly that the classical third axis equation holds on \((0,L)\), and that the endpoint argument of (h) applies there. Smoothness of \(\rho\) near every point of the open axis segment is a sufficient version of this additional input. The functional estimates proved here do not prove the microlocal propagation claim in §6.3.1(f). The later third-order argument described in §6.3.1(m) is another stated route to that input. Thus this proof does not silently upgrade a locally smooth density to a globally smooth density.

**Proof.** The normalization in (2) gives
\[
\mathcal B(A,e,\widetilde w)=L^{4+2/A}B_3.
\]
By (39) the right side is zero. To make the role of the origin explicit, the third axis equation gives \(C_0=\ell_3+B_3\); smoothness near zero sets \(C_0=0\), and (h) sets \(\ell_3=0\). The finite-part integrals in this equality converge under the weaker anchored endpoint hypotheses used here: the endpoint bound is \(O((1-u)^{\theta+\beta-2})\), and the origin remainder is \(O(u^{\sigma-\beta-1})\). These are exactly the convergence estimates already proved. No full Hölder seminorm over the tail is needed for the integrated identity.

On the other hand, (27) and (32) imply
\[
|\mathcal B(A,e,\widetilde w)-\mathcal B(A_0,e_0,w_0)|
  <\tfrac12|\mathcal B(A_0,e_0,w_0)|.
\]
The reference value is nonzero, so the left equality \(\mathcal B=0\) is impossible. This proves the theorem.

For the rational reference \(q=0,A_0=10.150725,e_0=0.0135206\), the choices in the third proof give the theorem with \(h=0.06,h'=0.0003,\varepsilon=10^{-6}\). For \(q=0,A_0=4,e_0=1/16\), they give \(\varepsilon=10^{-8}\) at those same parameter widths, or \(10^{-7}\) when both parameters are fixed.

## 3. Scope

The theorem excludes a specified neighborhood of a compatible axis trace in a strong, weighted norm. The reference need not be the trace of a coupled profile. It proves neither existence nor nonexistence of all \(P_\infty\) profiles; the endpoint hypothesis is additional when \(A>2\), and profiles outside the ball are not considered.

The stored numerical trace is not proved to be the trace of any exact profile. A small sampled error in \(w\), or even in \(w,w',w''\), gives no bound in \(N\) at the origin without rigorous subtraction and control down to zero. The finite dataset starts at positive \(x\), leaving an entire origin interval unobserved. Arbitrary smooth perturbations supported in that interval preserve all its entries while changing the weighted norm substantially. Noise in the subtraction of the origin jet further limits what can be inferred from trial data.

Consequently the fitted reference constructed next does not inherit either rational-reference radius. It has a concrete formula to which this inventory applies, and it is close to the stored trace in a sampled, unweighted sense only. Certifying its own \(\mathcal B_0\) and reference bounds, and establishing any relation to an exact profile, remain separate tasks.
