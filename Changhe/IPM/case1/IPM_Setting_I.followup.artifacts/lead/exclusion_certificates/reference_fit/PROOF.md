# An explicit compatible polynomial reference fitted to the trial trace

**Status: CONFIRMED for compatibility and negativity; numerical evidence only for approximation to the stored trace.** No bound for the distance in \(N\), and no obstruction or exclusion certificate for this fitted reference, is asserted.

## 1. Exact statement and definition

Take the exact decimals \(A_0=10.150725\), \(L_0=8.6000638\), and \(e_0=L_0^{-2}\). Let \(q(t)=\sum_{j=0}^{12}q_jt^j\), with the following coefficients interpreted as exact rational decimal numbers, in increasing order:

```text
-3.1086642790748664
 2.8463293854346565
-5.157019170237831
 9.6363849138295752
-10.568048035000519
-4.8988855905151825
 78.281466894874512
-247.83555958781369
 462.10389097961377
-550.96839996015603
 411.5296756206738
-175.45293252015944
 32.420024447785266
```

The exact coefficient strings are also stored in `data/fitted_reference.json`. Define
\[
w_0(u)=-A_0u\frac{1-u^2}{1+u^2}
u^3(1-u^2)^2q(u^2).
\]
Then \(w_0\) is odd, analytic on a neighborhood of \([0,1]\), satisfies
\[
w_0'(0)=-A_0,\quad w_0(1)=0,\quad w_0'(1)=A_0,
\]
and is negative on \(0<u<1\). Moreover
\[
\inf_{0<u<1}\frac{-w_0(u)}{u(1-u)}\ge A_0.
\]

## 2. Proof and exact negativity certificate

Oddness and analyticity follow directly from the formula. The perturbation vanishes to order three at 0 and to order two at 1, so it leaves the three displayed endpoint conditions unchanged.

Put \(H(t)=A_0-t(1-t^2)q(t)\). Factorization gives
\[
w_0(u)=-\frac{u(1-u^2)}{1+u^2}H(u^2).
\]
The exact rational computation in `verification/fit_reference.py` proves
\[
H(t)\ge A_0\qquad(0\le t\le1).                              \tag{40}
\]
Here is a complete description of its certificate, so that the claim does not rest on floating-point sampling. On each interval \([a,b]=[i/128,(i+1)/128]\), express
\[
H(a+(b-a)s)=\sum_{k=0}^{n}c_ks^k
          =\sum_{j=0}^{n}b_j {n\choose j}s^j(1-s)^{n-j},
\]
where \(n=\deg H\) and
\[
c_k=\sum_{m=k}^n H_m{m\choose k}a^{m-k}(b-a)^k,\qquad
b_j=\sum_{k=0}^j c_k\frac{{j\choose k}}{{n\choose k}}.
\]
All inputs and operations here are rational. Each computed \(b_j\) is at least \(A_0\); the minimum over all 128 intervals is exactly \(A_0\). The Bernstein basis functions are nonnegative and sum to one on \([0,1]\), proving (40). The script stores the exact minimum and checks it; its generation of the polynomial is numerical, but the resulting fixed polynomial's sign check is exact.

Since \(u(1-u^2)/(1+u^2)>0\) on \((0,1)\), (40) proves negativity. Finally
\[
\frac{-w_0(u)}{u(1-u)}
=\frac{1+u}{1+u^2}H(u^2)\ge H(u^2)\ge A_0,
\]
which proves the stated geometric bound. This is a certificate for this explicit compatible trace, not for the coupled IPM equation.

## 3. Exact reconstruction formula

For any polynomial \(q\) with \(H>0\), set
\[
T(t)=\frac12\int_0^t\frac{(1+s)^2q(s)}{H(s)}\,ds.
\]
The compatible reconstruction is exactly
\[
\boxed{g_0(u)=\frac{u^2H(u^2)}{A_0(1+u^2)}e^{T(u^2)}.}       \tag{41}
\]
To prove it, put \(z_0=-w_0/(A_0u)\). The origin-normalized solution of the first-order reconstruction equation is \(g_0=u^2z_0e^{E_0}\), where
\[
E_0(u)=\int_0^u\frac{z_0(s)^{-1}-1}{s}\,ds.
\]
Writing \(t=u^2\) and subtracting the rational-reference term shows
\[
\frac{d}{dt}\left(E_0(\sqrt t)+\log(1-t)\right)
 =\frac{(1+t)^2q(t)}{2H(t)}.
\]
Both sides integrate from zero with zero initial value, hence \(E_0=-\log(1-t)+T(t)\). Substitution cancels \(1-t\) and proves (41). This also verifies the origin normalization, positivity, and regular extension to the source without an endpoint singular quadrature.

In particular
\[
g_0(1)=\tfrac12 e^{T(1)},\qquad
w_0''(1)=A_0+8q(1).
\]
For the exact polynomial above,
\[
q(1)=-1.1717369007459792,\qquad
w_0''(1)=0.7768297940321664
\]
are exact decimal identities. Numerical quadrature of the integral gives
\[
g_0(1)\approx0.402227900155322443,\qquad
L_0^2g_0(1)\approx29.749216885933407.
\]
The latter is close to the supplied trial value \(29.7495\); neither comparison nor these quadrature digits are a certified error estimate.

## 4. How the fit was made, and what it does not measure

The read-only input was the NPZ file specified in the question. Its \(w/L_0\) and \(w'\) arrays were used to construct a piecewise cubic Hermite interpolant in \(u=x/L_0\). The least-squares fit used 701 equally spaced \(u\)-points on \([0.02,0.985]\) and the degree-12 Chebyshev basis in \(u^2\), multiplied by \(u^3(1-u^2)^2\). Thus the fitted residual was \(w-w_{\rm R12}\); dividing it by the vanishing prefactor before fitting was avoided. Conversion to the power basis and freezing the printed coefficient strings defines the exact polynomial above.

On the stored points in that band, the numerical maximum error in normalized \(w\) is about \(2.710\,10^{-7}\), with RMS error about \(2.103\,10^{-8}\). The rational reference alone has maximum error about \(0.217875\) on the same points. These comparisons are sample errors, not uniform bounds. The source-slope discrepancy of the interpolated data is approximately \(1.390\,10^{-7}\), whereas the polynomial has the required source slope exactly.

In particular these computations do not estimate the norm \(N\). That norm includes the actual origin jets, a strongly weighted second-derivative remainder all the way down to zero, and an endpoint modulus. Finite trial arrays cannot determine these quantities without additional interpolation/error hypotheses. The reported \(10^{-6}\) rational-reference exclusion radius therefore cannot be applied to this fitted reference or to the stored numerical trace on the strength of these residuals.

The data file records this limitation explicitly. The general certificate inventory in the preceding proof describes the remaining reference calculations.

`verification/reconstruct_reference.py` reproduces the numerical integral and endpoint values above from the frozen exact coefficient strings.
