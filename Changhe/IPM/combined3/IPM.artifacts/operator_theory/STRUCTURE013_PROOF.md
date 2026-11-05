# Exact Candidate 013 structure and the near analytic premises

This proof is paired with `verify_structure013.py` and `structure013_result.json`. The script was executed successfully against the actual unchanged Candidate 007 file recovered from combined1 and the actual raw Candidate 013 correction in combined2. It writes only into combined3. All algebraic decisions use exact rational arithmetic; Arb is used solely to display the already positive exact origin slope.

## Input identity

The script requires these SHA256 values before parsing:

| Input | SHA256 |
|---|---|
| Candidate 007 exact generator list | `ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21` |
| Candidate 013 raw exact correction | `a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a` |

There are 2,982 base generators and 12,273 correction atoms. After grouping as polynomials in \(z=s/(t+s)\), the correction has 3,057 nonzero groups. The script expands shifted Legendre polynomials exactly and verifies that the original atom representation and the stored elementary representation define precisely the same function. The fixed rational c in both files equals the campaign value.

## Smoothness, parity, and all-order decay

Put \(s=|X|^2\), \(H_m(X)=\operatorname{Re}(x+iy)^{2m}\), and
\[
\chi_{007}=\sum a_{m,j,T} H_m(X)(1+s)^{p_j-m}T(s/(1+s)),
\quad p_j=\tfrac12(3+1/c-j(1-1/c)).
\]
The exact generator list defines
\[
\rho_{007}=-\Delta\partial_y\chi_{007},\qquad
u_{007}=(-\partial_x\partial_y^2\chi_{007},\partial_x^2\partial_y\chi_{007}).
\tag{1}
\]
All factors are smooth. The harmonic polynomials H_m are even in each variable, so \(\rho_{007}\) is S1 and the velocity has the standard reflection parities.

If \(S^\nu\) denotes the class whose derivatives of every order obey \(|D^\alpha f(X)|\le C_\alpha\langle X\rangle^{\nu-|\alpha|}\), then each generator belongs to \(S^{2p_j}\). This follows from the product rule, the finite polynomial form of T, and differentiation of the positive radial powers; the rational function \(s/(1+s)\) lies in \(S^0\). Every j in the input is nonnegative. Thus \(2p_j\le3+1/c\), giving
\[
\rho_{007},u_{007}\in S^{1/c},\qquad
\nabla\rho_{007},Du_{007}\in S^{-\gamma},
\quad\gamma=1-1/c\in(0,1).
\tag{2}
\]

Every correction atom has the form
\[
a\,\operatorname{Im}(x+iy)^n s^h(1+s)^b(t+s)^{-d}
P_\ell(2s/(t+s)-1),
\tag{3}
\]
with n odd and positive, nonnegative integers h,d, and rational \(t>0\). These facts are checked for every actual row. The atom is smooth, S1, and belongs to \(S^\tau\), \(\tau=n+2h+2b-2d\). The maximum is verified exactly as
\[
\tau_{\max}=4/c-3<0.
\]
Consequently \(\phi\in S^{4/c-3}\), and
\[
h_*=-\Delta\phi\in S^{4/c-5},\qquad
U[h_*]=(-\phi_{xy},\phi_{xx})\in S^{4/c-5}.
\tag{4}
\]
The velocity identity follows in tempered distributions from the Fourier multiplier: \(\widehat h_*=|\xi|^2\widehat\phi\), and multiplication by the joint second-order Riesz multiplier yields exactly the Fourier transform of the displayed derivatives. Since \(\phi\) decays, no polynomial ambiguity at zero frequency is allowed. Equivalently both sides are decaying L2 fields with the same curl and divergence, so their harmonic difference is zero.

The correction's gradient and velocity derivative satisfy the all-order bounds with
\[
\gamma_h=6-4/c>\gamma.
\]
Thus the actual corrected background \(\rho_*=\rho_{007}+h_*\), \(u_*=u_{007}+U[h_*]\) satisfies precisely the all-order background assumption (5) of `OPERATOR_BRIDGE_v01.md` with \(\gamma=1-1/c\). This is a consequence of the actual finite formulas, not an extrapolation of sampled derivative values.

Since \(4/c-5<-1\), h_* is in L2. The dilation part of L007 h_* has the same exponent; the terms \(u_{007}\cdot\nabla h_*\) and \(U[h_*]\cdot\nabla\rho_{007}\) have exponent \(5/c-6<-1\). Hence h_* belongs to the actual maximal L2 graph domain of L007. The velocity correction is bounded and globally Lipschitz. The weight condition \(Wh_*\in H^s\), for every finite s at the campaign weight, follows from \(1+(4/c-5)<-1\); more generally it holds for \(\sigma<4-4/c\). These statements quantify admissible exponents but not norm constants.

## Exact origin normalization and slope

Only the homogeneous quartic part of \(\chi_{007}\) contributes to its velocity derivative and density slope at zero. Let t0 be the sum of its m=0 radial s² coefficients, t1 the m=1 radial s coefficients, and t2 the m=2 constant radial coefficients. Exact differentiation gives
\[
\partial_y(u_{007})_2(0)=8t_0-24t_2,
\quad\partial_y\rho_{007}(0)=-32t_0+24t_1.
\tag{5}
\]
The script computes these coefficients directly from the original generators, using generalized binomial coefficients and the exact expansion
\(P_n(2z-1)=\sum_{j=0}^n(-1)^{n-j}\binom nj\binom{n+j}jz^j\).
It verifies, as an equality of rational numbers,
\[
c+8t_0-24t_2=1.
\tag{6}
\]
It also verifies that the direct base density slope equals the base slope recorded in the Candidate 013 metadata.

Write the homogeneous cubic part of the actual correction as
\[
\phi_3=A\,y(x^2+y^2)+B\operatorname{Im}(x+iy)^3.
\]
Direct expansion of the original correction atoms, including their Legendre factors, reproduces the stored exact A and B and proves
\[
A+3B=0,\qquad\partial_yU_2[h_*](0)=2(A+3B)=0,
\quad\partial_y h_*(0)=-8A.
\tag{7}
\]
Combining (5)--(7) proves the actual corrected normalization \(c+\partial_y(u_*)_2(0)=1\). The computed exact slope has the displayed Arb enclosure
\[
\partial_y\rho_*(0)
=10.29736736525626727917786091807940725768\ldots,
\]
and is proved rationally to exceed one. Together with the independently certified \(\|\nabla k\|_\infty<(28/25)M\), \(M\le1/2\), it supplies the positive total slope needed for the fixed-point normalization identity in the bridge note.

This checks strain normalization. It does not prescribe the final density slope to equal its center value, and it does not vary c.

## Actual erflog coefficient and the radial-core identity

The corrected velocity is divergence free and has a smooth stream function \(\psi_*\). In polar coordinates,
\[
u_*\cdot X=-\partial_\theta\psi_*.
\]
Its angular mean is therefore zero at every r. With the exact erflog cut chi of Lemma 5 in the bridge note, set
\[
a_c=c/(1+4r^2),\quad
a_n=\chi(r)\frac{4u_*\cdot X-c}{1+4r^2},\quad a_r=a_n+a_c.
\]
Lemma 5 proves a_n is Schwartz. Thus its Hessian is bounded, its Fourier transform is integrable with every polynomial moment, all whole-plane Dm norms exist, and Plancherel applies. This settles the qualitative N1 and erflog-localization assumptions of combined2 `NEAR_CHECK_v02.md` section 3 for the actual coefficient.

Moreover the angular mean of a_n is exactly \(-\chi a_c\). Put \(s_n=a_n+\chi a_c\); it has zero angular mean. Every isotropic Fourier multiplier \(|D|^m\) commutes with rotations and hence preserves orthogonality between radial functions and zero-angular-mean functions. All functions below lie in Hm. Pythagoras therefore gives
\[
\begin{aligned}
\|D^ma_n\|_2^2&=\|D^ms_n\|_2^2+\|D^m(\chi a_c)\|_2^2,\\
\|D^ma_r\|_2^2&=\|D^ms_n\|_2^2+\|D^m((1-\chi)a_c)\|_2^2.
\end{aligned}
\]
Subtracting proves the exact radial identity used by the inherited near calculation:
\[
\boxed{\|D^ma_r\|_2^2
=\|D^ma_n\|_2^2-\|D^m(\chi a_c)\|_2^2
+\|D^m((1-\chi)a_c)\|_2^2.}
\tag{8}
\]
No compact-support approximation is needed. The radial integral **values** in the old certificate, and all numerical Dm upper bounds, remain inherited numerical inputs; this proof establishes their analytic identity and global applicability. The function a_r generally has the algebraic a_c tail and is not asserted to be Schwartz.

## Reproduction

From the repository root, using an environment with python-flint:

```bash
python -B Changhe/IPM/combined3/IPM.artifacts/operator_theory/verify_structure013.py \
  --output Changhe/IPM/combined3/IPM.artifacts/operator_theory/structure013_result.json
python3 -B Changhe/IPM/combined3/IPM.artifacts/operator_theory/verify_embedding_constants.py
```

The former script completes in approximately one second in the present environment. It is an exact structural check, not a residual or commutator-norm computation. No stationary existence claim follows from it alone.
