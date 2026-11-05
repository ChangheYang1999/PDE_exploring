# Full near-strain TIS and the p sandwich, with explicit damping use

This is a new rigorous analytic estimate with executed scalar certificates. It uses the actual near strain \(S_n=\chi\operatorname{Sym}Du_*\), the inherited global strain bound 137/125, and the exact erflog moments proved in `LOWBAND_LOCALIZED_PRICING_v01.md`. All remaining scalar calculations use Arb with rational inputs. It does not certify the far TIS or the other commutators.

Notation: \(q=21/10\), \(G=J^q(Wg)\), \(N=\|G\|_2\), \(R_0=\|g\|_2\), \(P=\|J^{-1}G\|_2\), \(p=J^{-1}\), \(n=1-|D|J^{-1}\). Set \(\nu=1/40\), \(\psi_\lambda(r)=e^{-(r/\lambda)^4}\), and \(s=137/125\). The vector Riesz transform is denoted by \(\mathcal R\) in this note, to distinguish it from a radius. Define \(\eta=11/10^6\).

## 1. Exact mid-band kernel price

For any \(\mu\ge1\), write \(Q=\psi_\mu-\psi_\nu\). It vanishes to fourth order at zero. Consider the vector multipliers
\[
\mathcal R QJ^q,\quad p\mathcal R QJ^q,\quad n\mathcal R QJ^q.
\]
Their radial amplitudes are \(b(r)=t(r)Q(r)\), where respectively
\[
t_R=J^q,\quad t_p=J^{q-1},\quad
t_n=\frac{J^{q-1}}{J+r}.
\]
For the three cases use the pairs
\[
(\beta,d)=(q,q),\quad(q-1,q-1),\quad(q-2,q).
\]
They satisfy \(0\le t(r)\le J(r)^\beta\) and \(|t'(r)|\le dJ(r)^{\beta-1}\). For t_n, differentiate \(\log t_n=(q-1)\log J-\log(J+r)\); its derivative is \((q-1)r/J^2-1/J\), proving the bound.

Let K be the vector convolution kernel of \(i\omega b\). Polar Plancherel gives the exact identities
\[
\|K\|_2^2=\frac1{2\pi}\int_0^\infty rb(r)^2\,dr,\qquad
\||x|K\|_2^2=\frac1{2\pi}\int_0^\infty\left(rb'(r)^2+\frac{b(r)^2}{r}\right)dr.
\tag{1}
\]
All integrals are finite, including at zero because Q vanishes to fourth order. The kernel is odd, so the weighted Hilbert--Schmidt argument of the low-band note gives
\[
\|S_n t(|D|)\mathcal R Q(Wg)\|_2\le\mathcal P(\beta,d;\mu)R_0,
\tag{2}
\]
where it suffices to take
\[
\mathcal P^2\le\frac{A_1^2}{2\pi}I_0+
\frac{2A_0^2}{\pi}(I_D+I_A).
\tag{3}
\]
The notation in (2) means the vector multiplier with radial amplitude tQ applied to Wg, as in (1). In particular its t for the R case already includes Jq.

Here are explicit closed upper bounds for the three integrals; no numerical quadrature is required. Define
\[
E_m(\lambda)=\int_0^\infty r^m e^{-2(r/\lambda)^4}\,dr
=\frac{\lambda^{m+1}}4\,2^{-(m+1)/4}\Gamma((m+1)/4),\quad m>-1,
\]
\[
F_{\gamma,m}(\lambda)=
\begin{cases}
E_m(\lambda),&\gamma\le0,\\
2^{\max(\gamma-1,0)}[E_m(\lambda)+E_{m+2\gamma}(\lambda)],&\gamma>0.
\end{cases}
\]
The elementary concavity/convexity inequality \((1+r^2)^\gamma\le2^{\max(\gamma-1,0)}(1+r^{2\gamma})\), for gamma>0, proves that F bounds its defining weighted integral. Then
\[
\begin{aligned}
I_0&=F_{\beta,1}(\mu),\\
I_D&=2d^2F_{\beta-1,1}(\mu)
+64[\mu^{-8}F_{\beta,7}(\mu)+\nu^{-8}F_{\beta,7}(\nu)],\\
I_A&=\frac{(1+\nu^2)^\beta}{8}
+2^\beta\left[\log(1/\nu)+E_{2\beta-1}(\mu)\right].
\end{aligned}
\tag{4}
\]
For ID use \(|(tQ)'|^2\le2t'^2Q^2+2t^2Q'^2\), \(Q^2\le\psi_\mu^2\), and \(Q'^2\le2(\psi_\mu'^2+\psi_\nu'^2)\). For IA split at nu and 1. Below nu, \(Q\le(r/\nu)^4\); on [nu,1], bound J2beta by 2beta and integrate dr/r; beyond 1, use J2beta<=2beta*r2beta and Q²<=psi_mu². These prove (4).

Combine the mid-band price (3) with the proved low-band prices to obtain
\[
\begin{aligned}
\|S_n\mathcal R\psi_\mu G\|_2&\le A_RR_0+\eta N,\\
\|S_np\mathcal R\psi_\mu G\|_2&\le A_pR_0+\eta N,\\
\|S_nn\mathcal R\psi_\mu G\|_2&\le A_nR_0+\eta N,
\end{aligned}
\tag{5}
\]
where \(A_R=99+\mathcal P(q,q;\mu)\), \(A_p=99+\mathcal P(q-1,q-1;\mu)\), \(A_n=100+\mathcal P(q-2,q;\mu)\). The A0,A1 in (3) are bounded by the exact actual coefficient moments (9) of the low-band note. The code verifies the following simple outward rational thresholds:

| mu | A_n upper | A_p upper | A_R upper |
|---:|---:|---:|---:|
| 10 | 202 | 512 | 4827 |
| 12 | 223 | 696 | 8276 |
| 16 | 264 | 1173 | 19696 |
| 20 | 306 | 1803 | 38909 |

## 2. The full near TIS form

For \(G_h=(1-\psi_\mu)G\), the elementary multiplier bounds
\[
\|nG_h\|_2\le\frac{N}{2\mu^2},\qquad
\|pG_h\|_2\le\frac{N}{\mu}
\]
follow from \(n(r)\le1/(2r^2)\), \(p(r)\le1/r\), and \(1-e^{-(r/\mu)^4}\le\min(1,(r/\mu)^4)\). Therefore
\[
|T_{IS}(S_n;G_h)|
\le e_hN^2,\qquad e_h=qs\left(\frac2{\mu^2}+\frac1{4\mu^4}\right).
\tag{6}
\]
No moment of S or its derivatives is used in (6).

The exact polarized low/high decomposition from the low-band note remains valid with mu in place of nu. Keep the smoothing norm P in every factor that permits it, rather than replacing it by N. From (5) and \(n\le p\) one obtains
\[
|T_{IS}(S_n;G)-T_{IS}(S_n;G_h)|
\le2q[(A_n+A_p+A_R)R_0P+A_nR_0N+3\eta NP+\eta N^2].
\tag{7}
\]
Consequently, for every \(D>0\) and \(\varepsilon_Y>0\),
\[
\boxed{|T_{IS}(S_n;G)|
\le(e_h+8q\eta+\varepsilon_Y)N^2+DP^2
+\left[\frac{q^2(A_n+A_p+A_R)^2}{D}
+\frac{q^2A_n^2}{\varepsilon_Y}\right]R_0^2.}
\tag{8}
\]
This is an actual bound for the **entire** near TIS contribution, with every cross term included. Its damping term D P² must be paid from the exact negative multiplier retained in the new energy; it is not free slack.

For \(D=1\), \(\varepsilon_Y=1/200\), the executed certificate gives approximately (all final machine values are exact rational majorants at the integer A thresholds):

| mu | high-norm rate upper | weak price upper | p-damping used |
|---:|---:|---:|---:|
| 10 | 0.05127434 | 1.72e8 | 1 |
| 12 | 0.037179216 | 4.17e8 | 1 |
| 16 | 0.023174830 | 2.04e9 | 1 |
| 20 | 0.016696397 | 7.51e9 | 1 |

The certificate JSON gives the exact rational rate and price for each row; the displayed decimal prices are conservative upward bounds.

## 3. The near p sandwich

The remaining compact strain term in the new decomposition is \(-q\langle S_np\mathcal RG,p\mathcal RG\rangle\). Its sign need not be favorable. The same exact polarized split and (5) give, for any \(D_s>0\),
\[
\boxed{q|\langle S_np\mathcal RG,p\mathcal RG\rangle|
\le\left(\frac{qs}{\mu^2}+2q\eta\right)N^2+D_sP^2
+\frac{q^2A_p^2}{D_s}R_0^2.}
\tag{9}
\]
The high-high part costs qs/mu². In the low difference, both localized low p factors are bounded by A_pR0+eta N and their partners by P. Young's inequality proves (9).

Combining (8)--(9), with \(D_s=1/10\), gives the full near-strain cost
\[
e_{nearS}=qs\left(\frac3{\mu^2}+\frac1{4\mu^4}\right)
+10q\eta+\frac1{200},\qquad D_{nearS}=\frac{11}{10},
\]
\[
C_{nearS}=q^2(A_n+A_p+A_R)^2+200q^2A_n^2+10q^2A_p^2.
\tag{10}
\]
For mu=12 its rate is below 0.05321 and price below 4.39e8. For mu=16 they are below 0.03222 and 2.10e9. These numbers are compatible with a useful fraction of the original total weak-price budget, but they require a new complete energy join and a corresponding reoptimization of the strong ball.

## 4. Exact join with other far and near forms

Suppose the scalar weight forms TII+Caw have already been rigorously bounded by
\[
e_aN^2+C_aR_0^2+A_{far}P^2,
\]
and suppose a new actual far-strain supremum \(\|(1-\chi)S\|_{\infty,\mathrm{op}}\le s_f\) is certified. Its p sandwich costs at most \(qs_fP^2\). Keep the far TIS form separate. Adding the exact background energy decomposition then gives
\[
\mathfrak Q_*(G)
\le-\int(\mathcal RG)^T\mathcal M_*(\mathcal RG)
+(e_a+e_{nearS})N^2+(C_a+C_{nearS})R_0^2
\]
\[
-\left[qc-A_{far}-\frac{11}{10}-qs_f\right]P^2
+T_{IS}((1-\chi)S;G)+C_{tr}(G)+\sum_{j=1}^3C_{vsj}(G).
\tag{11}
\]
The bracket may be used only after its actual inputs are supplied. For example an actual certified sf<=1/2 would leave a positive bracket at the inherited A_far. The far TIS and other forms in the final line of (11) are **still present**. They are not bounded by this calculation.

The favorable sign retained in (11) explains why the new D terms may be useful. They cannot be inserted into the old join while also charging its entire p damping a second time.

## Reproduction

```bash
python -B Changhe/IPM/combined3/IPM.artifacts/operator_theory/verify_near_strain_full_pricing.py \
  --output Changhe/IPM/combined3/IPM.artifacts/operator_theory/near_strain_full_pricing_result.json
```

The calculation uses only closed Gamma integrals and interval arithmetic, not a periodic field, sampled continuum supremum, or an uncontrolled quadrature tail. It inherits exactly the same actual strain input as the previously reviewed low-band certificate.
