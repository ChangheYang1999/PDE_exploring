# Exterior tail witnesses for the homogeneous negative norm

## Why this check is needed

The parity Hardy inequality is an upper bound, \(\|F\|_{\dot H^{-1}}\le\||X|F\|_2\). It cannot by itself give a necessary onset radius for a fixed residual sector. The exact exterior dual witness below supplies a lower bound and identifies the angular factor omitted by a radial size model. A sector coefficient without an onset or remainder bound gives no positive uniform forcing-norm floor.

This is a new T4 argument, pending independent review. The formulas concern forcing functions and their norms. They do not assert that arbitrary such functions are realizable as residuals of the specified finite IPM potential family.

## 1. Statement

Let \(\sigma>0\), \(T>0\), and let I be a finite nonempty set of positive odd integers. Let \(a_n\in\mathbb R\), not all zero. Suppose a real S1 distribution F belongs to \(H=\dot H^{-1}(\mathbb R^2)\) and, on the open exterior \(r>T\),

\[
F(r,\theta)=r^{-2-\sigma}\sum_{n\in I}a_n\sin(n\theta).
\tag{1}
\]

Here S1 means even in x and odd in y, and H is the completion of the compact smooth S1 core with Fourier norm \(\|(-\Delta)^{-1/2}F\|_2\). Then

\[
\boxed{\quad
\|F\|_H^2\ge \frac{\pi T^{-2\sigma}}{2\sigma}
\sum_{n\in I}\frac{a_n^2}{(n+\sigma)^2}.
\quad}
\tag{2}
\]

This lower bound is independent of the forcing on r<T. If \(A^2=\pi\sum a_n^2\) and \(N=\max I\), it implies

\[
\|F\|_H\ge\frac{A T^{-\sigma}}{\sqrt{2\sigma}(N+\sigma)}.
\tag{3}
\]

Consequently a necessary condition for \(\|F\|_H\le\tau\) is

\[
T\ge\left[\frac{A}{\tau\sqrt{2\sigma}(N+\sigma)}\right]^{1/\sigma}.
\tag{4}
\]

If F is the exactly truncated sector, zero on r<T, its full norm is instead

\[
\boxed{\quad
\|1_{r>T}r^{-2-\sigma}\sum a_n\sin(n\theta)\|_H^2
=\frac{\pi T^{-2\sigma}}{2\sigma}
\sum_{n\in I}\frac{a_n^2}{n(n+\sigma)}.
\quad}
\tag{5}
\]

The Hardy proxy for this function is \(A^2T^{-2\sigma}/(2\sigma)\). Neither the proxy nor A alone determines the exact H norm.

## 2. Exterior Dirichlet witness

For n not equal to sigma define

\[
v_n(r)=\frac{a_n}{n^2-\sigma^2}
\left(r^{-\sigma}-T^{n-\sigma}r^{-n}\right),\qquad r>T.
\tag{6}
\]

For n=sigma, use the continuous limit

\[
v_n(r)=\frac{a_n}{2n}r^{-n}\log(r/T).
\tag{7}
\]

Each v_n is zero at T, decays at infinity, and solves

\[
-v_n''-r^{-1}v_n'+n^2r^{-2}v_n=a_n r^{-2-\sigma}.
\tag{8}
\]

Extend \(\varphi=\sum v_n(r)\sin(n\theta)\) by zero on r<=T. The zero trace makes this extension belong to \(\dot H^1\). Its derivatives are square integrable both near T and at infinity, including the logarithmic case. Radial cutoffs and smooth approximation show that it is a \(\dot H^1\) limit of compact smooth S1 tests supported in r>T.

Integration by parts in the exterior has no inner boundary contribution because v_n(T)=0; the outer contribution tends to zero by the displayed decay. Orthogonality over the full circle gives

\[
\|D\varphi\|_2^2
=\pi\sum_n a_n\int_T^\infty r^{-1-\sigma}v_n(r)\,dr.
\tag{9}
\]

For n not equal to sigma, the radial integral times a_n is

\[
\frac{a_n^2 T^{-2\sigma}}{n^2-\sigma^2}
\left(\frac1{2\sigma}-\frac1{n+\sigma}\right)
=\frac{a_n^2 T^{-2\sigma}}{2\sigma(n+\sigma)^2}.
\]

For n=sigma, direct logarithmic integration gives the same value. Thus the right side of (9) equals the right side of (2), say K>0. Pairing F with the exterior approximating tests and passing to the limit yields \(\langle F,\varphi\rangle=K\), regardless of its interior values. Duality gives \(\|F\|_H\ge K/\sqrt K\), proving (2). Equations (3)-(4) follow immediately.

This argument does not assume the canonical potential of F vanishes on the interior. The Dirichlet solution is a freely chosen test, not an assertion about that potential.

## 3. Exact norm of the truncated model

The truncated forcing belongs to H by the centrally odd Hardy estimate, since \(\int_T^\infty r^{-1-2\sigma}dr<\infty\). For a radial mode f_n, its canonical Poisson solution is

\[
u_n(r)=\frac1{2n}\left[
r^{-n}\int_0^r f_n(t)t^{n+1}\,dt+
r^n\int_r^\infty f_n(t)t^{1-n}\,dt\right].
\]

The two contributions to \(\pi\int f_nu_n r\,dr\) agree by reversing the two radial integrations. Hence the modal squared norm is

\[
\frac{\pi}{n}\int_T^\infty a_nr^{-n-1-\sigma}
 \left(\int_T^r a_nt^{n-1-\sigma}\,dt\right)dr.
\]

For n not equal to sigma the inner integral is \(a_n(r^{n-\sigma}-T^{n-\sigma})/(n-\sigma)\). The resulting difference of two elementary integrals is

\[
\frac{\pi a_n^2T^{-2\sigma}}{n(n-\sigma)}
\left(\frac1{2\sigma}-\frac1{n+\sigma}\right)
=\frac{\pi a_n^2T^{-2\sigma}}{2\sigma n(n+\sigma)}.
\]

At n=sigma the logarithmic integral or its continuous limit agrees. Summing orthogonal modes proves (5).

For a single mode, the Hardy proxy exceeds the true H norm by exactly \(\sqrt{n(n+\sigma)}\). The norm's power of T is nevertheless exactly T^-sigma. This is the correct distinction between a useful scaling model and a certified necessary bound.

## 4. Quantified remainder

Suppose instead that the selected Fourier coefficients of the exterior forcing satisfy

\[
F_n(r)=a_nr^{-2-\sigma}+R_n(r),\qquad
|R_n(r)|\le\varepsilon |a_n|r^{-2-\sigma},\quad 0\le\varepsilon<1.
\tag{10}
\]

Other angular modes are unrestricted. The radial factor v_n has the same sign as a_n on r>T, by (6)-(7), or positivity of the exterior Dirichlet Green function. Therefore \(\langle F,\varphi\rangle\ge(1-\varepsilon)K\). The lower bounds (2)-(3) hold with the norm lower bound multiplied by 1-epsilon. This gives an actual sufficient data contract for certifying a necessary tail cost: a coefficient vector, an onset T, and a verified relative remainder bound for those modes.

A merely asymptotic statement ensures that some onset exists. Without an upper bound on that onset it supplies no quantitative exclusion at a prescribed threshold.

## 5. A fixed sector alone has no positive norm floor

Fix a smooth radial cutoff chi, zero on r<=1 and one on r>=2. For T>=1 set

\[
F_T(X)=\chi(|X|/T)|X|^{-2-\sigma}\sum a_n\sin(n\theta).
\]

Every F_T has exactly the same far-field coefficient vector. Nevertheless \(F_T(X)=T^{-2-\sigma}F_1(X/T)\), and homogeneous scaling gives

\[
\|F_T\|_H=T^{-\sigma}\|F_1\|_H\longrightarrow0.
\]

The same holds in each fixed baseline Ns norm. Indeed the ordinary L2 and gradient norms scale as T^-1-sigma and T^-2-sigma. The weighted Hessian and third derivative norms are bounded by constants times T^-11/5-sigma and T^-16/5-sigma because \(\omega(TX)\le T^{4/5}\omega(X)\). Thus E2(F_T)=O(T^-sigma), while the weighted third derivative is smaller. The explicit E2/Q3-to-Ns estimate of Analysis II P8.1(25) gives Ns(F_T)=O_s(T^-sigma).

This disproves a positive forcing-norm lower bound derived only from a fixed nonzero integrable sector. It does not bypass a theorem that also bounds the radial degree, coefficients or onset, and it does not construct an IPM profile with residual F_T. In particular the existing degree-limited six-branch obstruction remains unaffected.

## Audit implication

The T1 model correctly identifies the slow power T^-sigma for sigma approximately0.133. Its numerical onset estimates based on the Hardy proxy are diagnostic, not necessary lower bounds as written. Broad statements excluding every finite family or every unweighted framework need additional hypotheses. Equations (2) and (10) specify one way to add them. The numerical lower bounds already proved for particular degree-bounded families have their own independent basis-extremal arguments and must retain that scope.
