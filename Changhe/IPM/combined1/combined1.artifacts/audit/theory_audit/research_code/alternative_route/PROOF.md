# A posteriori closure from a computed linear correction

## Purpose and status

The baseline theorem estimates the correction by the inverse constant times the entire residual norm. A computed approximation to the linear correction can retain cancellation lost by that estimate. The result below gives a sufficient inequality in terms of that correction, its linear defect, and eight derivative bounds. It does not certify a numerical candidate: no such linear correction has yet been supplied by the numerical batch.

The theorem is conditional on the explicit background hypotheses of the baseline rough-transport inverse. All additional mapping and closure estimates are proved below. It preserves the fixed exponent, leading tail, and center-strain constraint.

## 1. Spaces, background and constants

All scalar functions are real and S1: even in x and odd in y. Let

\[
U[h]=(-R_1R_2h,R_1^2h),\quad
R_j=\partial_j(-\Delta)^{-1/2},\quad
H=\dot H^{-1}(\mathbb R^2).
\]

The velocity is the canonical Fourier velocity, with no harmonic field added. Set

\[
\omega=(1+4|X|^2)^{2/5},\qquad b_0=20/21,
\]
\[
E_2(h)^2=\|\omega D^2h\|_2^2+2^{14}\|Dh\|_2^2
 +2^{18}\|h\|_2^2+2^{18}b_0\|h\|_H^2,
\quad N_s(h)=E_2(J^sh),\quad J=(1-\Delta)^{1/2}.
\]

Both are completions of the smooth compact S1 core. Every tensor norm sums over all ordered derivatives. Let \(\bar\rho\) be a background with exponent c, normalized by \(c+c[\bar\rho]=1\), and with \(a_0=\bar\rho_y(0)\ne0\). Write

\[
F=F(\bar\rho;c)=(cX+U[\bar\rho])\cdot D\bar\rho-\bar\rho,\qquad
Lh=(cX+U[\bar\rho])\cdot Dh-h+U[h]\cdot D\bar\rho,
\quad A_k=L+U[k]\cdot D.
\]

Assume the baseline background hypotheses B0, B0n, B1-B5, B7 and B9c, as stated verbatim in `source/baseline_closure.md` under `../nonlinear_audit/`. Their consequences used here are:

- For \(0<s\le1/1024\), \(N_s(k)\le r\), and
  \[
  \mu=1/10-4800s,\quad A=5/\sqrt{s},\quad \beta_r=\mu-Ar>0,
  \]
  the maximal distributional operator A_k has a common high inverse with norm at most \(1/\beta_r\).
- For \(c[k]=0\), that inverse maps the forcing hyperplane \(f_y(0)=0\) into the solution hyperplane \(c[h]=0\).
- The consistent low inverse has norm at most
  \[
  K_L(r)=(19/5-d_r)^{-1},\qquad
  d_r=c_s r,\qquad c_s=[2\sqrt{\pi s(1+s)}]^{-1}.
  \]
- \(\|Dh\|_\infty,\|DU[h]\|_\infty\le c_sN_s(h)\), and the N_s ball intersected with c[h]=0 is complete in the H metric.
- For centrally odd f,
  \(\|\omega U[f]\|_2\le(9/5)\|\omega f\|_2\).

These are inputs from the existing proved baseline, not new numerical background certificates.

## 2. Explicit multiplication bound

Let g be a smooth S1 function in N_s. Define nonnegative finite quantities

\[
a_1=\|Dg\|_{F,\infty},\quad a_2=\|D^2g\|_{F,\infty},
\quad w_2=\|\omega D^2g\|_{F,\infty},\quad
w_3=\|\omega D^3g\|_{F,\infty}.
\]

Here the Frobenius norm is taken pointwise before the supremum. In addition let

\[
S_1=\sum_i\|\partial_i g\|_\infty,\qquad
S_j=\sum_{i_1,\ldots,i_j}\|\omega\partial_{i_1}\cdots\partial_{i_j}g\|_\infty
\quad (j=2,3,4).
\]

These component sums must not be inferred from a Frobenius supremum with an unjustified square-root factor. The number of components is always a valid conversion factor.

Form the nonnegative matrices

\[
M_g=\begin{pmatrix}
\frac95a_1&w_2/64&w_3/512&0\\
0&a_1&a_2/4&0\\
0&0&a_1&0\\
0&0&0&a_1
\end{pmatrix},
\]
\[
K_g=\begin{pmatrix}
17S_2&17S_3/64&17S_4/512&0\\
0&17S_2&17S_3/4&0\\
0&0&17S_2&0\\
0&0&17\sqrt{b_0}S_1&0
\end{pmatrix}.
\]

Then

\[
N_s(U[k]\cdot Dg)\le B_gN_s(k),\qquad
B_g=\|M_g+sK_g\|_{\ell^2\to\ell^2}.\tag{3}
\]

Any certified upper bound for B_g may be used. One simple certificate is
\(B_g\le\sqrt{\|M_g+sK_g\|_1\|M_g+sK_g\|_\infty}\). A sharper certificate can bound the largest eigenvalue of the symmetric matrix \((M_g+sK_g)^T(M_g+sK_g)\). No infinite-dimensional inverse is inferred from this small matrix; the matrix only summarizes an already proved multiplication estimate.

### Proof at E2 level

Put H_0=J^s k and
\[
e=(P,128a,512b,512\sqrt{b_0}h),
\quad(P,a,b,h)=(\|\omega D^2H_0\|_2,\|DH_0\|_2,\|H_0\|_2,\|H_0\|_H).
\]
Its Euclidean norm is N_s(k). Leibniz's rule, the unweighted vector multiplier norm \(\|U\|_{L^2\to L^2(\mathbb R^2;\mathbb R^2)}\le1\), and the weighted odd-function bound give

\[
\|\omega D^2(U[H_0]\cdot Dg)\|_2
\le\frac95a_1P+2w_2a+w_3b,
\]
\[
\|D(U[H_0]\cdot Dg)\|_2\le a_1a+a_2b,
\qquad \|U[H_0]\cdot Dg\|_2\le a_1b.
\]

For the low component, write \(\psi=\partial_x(-\Delta)^{-1}H_0\). Since \(U[H_0]=(-\psi_y,\psi_x)\),

\[
U[H_0]\cdot Dg=\operatorname{div}(\psi(g_y,-g_x)),\qquad
\|\psi\|_2\le\|H_0\|_H.
\]

Hence its H norm is at most a_1 h. Multiplying by the four norm weights proves the componentwise bound M_g e.

### Fractional commutator

For \(0<s\le1/2\),

\[
J^sf=f+\int\kappa_s(z)(f(X)-f(X-z))\,dz,
\quad
\kappa_s(z)=\frac{s}{2\Gamma(1-s/2)}
 \int_0^\infty e^{-t}(4\pi t)^{-1}e^{-|z|^2/(4t)}t^{-1-s/2}\,dt.
\]

The weight ratio satisfies \(\omega(X)/\omega(X-z)\le m(z)=(1+2|z|)^{4/5}\le1+2|z|\). Gaussian integration gives

\[
\int |z|\kappa_s(z)\,dz
 =\frac{s\sqrt\pi}{2}\frac{\Gamma((1-s)/2)}{\Gamma(1-s/2)},
\quad \int |z|^2\kappa_s(z)\,dz=2s.
\]

The gamma ratio is less than 5e on this range: the numerator is at most \(4+e^{-1}<5\), while the denominator is at least \(e^{-1}\). Consequently \(\int |z|m(z)\kappa_s(z)\,dz\le17s\), using \(\sqrt\pi<9/5\) and \(e<11/4\). The mean-value theorem along X-tz and Minkowski's inequality yield

\[
\|\omega[J^s,d]f\|_2\le17s\|\omega Dd\|_{\Sigma,\infty}\|f\|_2,\tag{4}
\]

and its unweighted counterpart. This holds for every scalar, vector or tensor contraction used here, with the indicated component sum.

Let \(C=[J^s,Dg]\cdot U[k]\). Differentiating twice gives the three terms
\([
J^s,Dg]\cdot U[D^2k]\),
\(2[J^s,D^2g]\cdot U[Dk]\), and
\([J^s,D^3g]\cdot U[k]\).
Since J^{-s} is an unweighted L2 contraction and \(\omega\ge1\), (4) bounds their weighted top component by
\(17s(S_2P+2S_3a+S_4b)\).
The derivative and L2 components are at most
\(17s(S_2a+S_3b)\) and \(17sS_2b\).
Finally incompressibility gives

\[
C=\operatorname{div}([J^s,g]U[k]),\qquad
\|C\|_H\le17sS_1b.
\]

With the four energy weights these are precisely sK_g e. Adding the bounds componentwise, then taking the Euclidean norm, proves (3) when k and g are in the smooth compact core. For general g as stated, replace it by a radial cutoff g_R=chi(X/R)g. The N_s embedding makes g and Dg bounded. All extra weighted derivative terms from the cutoff tend to zero in the eight coefficient bounds: the worst new term is O(R^(-1/5)) from omega Dchi_R Dg, and higher derivatives have greater negative powers. The main terms have coefficient bounds no larger than those for g. For fixed compact smooth k, the products therefore have a uniformly bounded N_s norm with the same limiting bound. Weak compactness and local distributional convergence place U[k].Dg in N_s and prove (3). Approximation in k now extends the map continuously to N_s; local Sobolev convergence identifies the extension with the displayed distributional product. This step gains no derivative: g is the fixed smooth factor, and k is the rough variable.

## 3. Defect theorem

Assume the background hypotheses above. Let g be a smooth element of the generator domain D(L) in N_s, with c[g]=0 and finite constants in Section 2. Suppose

\[
D=F+Lg\in N_s,\qquad N_s(g)\le m,\qquad N_s(D)\le\epsilon,
\qquad B_g\le B.
\]

The reference residual F is consequently in N_s as well, but its norm need not be used in the smallness inequality. If r>0 satisfies

\[
\beta_r=\mu-Ar>0,\qquad
m+\frac{\epsilon+Br}{\beta_r}\le r,\tag{5}
\]

then there is a unique h in
\(\{N_s(h)\le r,\ c[h]=0\}\) solving
\(F(\bar\rho+h;c)=0\). If the reference also satisfies the stated leading-tail hypothesis B11, the correction retains that leading tail. Its low-metric Picard contraction factor is at most

\[
q\le\frac{c_s r}{19/5-c_s r}<1.\tag{6}
\]

### Proof

For k in the stated ball define

\[
T(k)=g-A_k^{-1}(D+U[k]\cdot Dg).
\]

Equation (3) makes the inverse input an element of N_s. Since g belongs to D(L) and the perturbing product is in N_s, it belongs to D(A_k), using the maximal distributional domain. A direct substitution therefore gives
\(A_kT(k)=-F\).

The forcing has zero first y-jet. Indeed F_y(0)=0 by exact background normalization, \((Lg)_y(0)=a_0c[g]=0\), and
\((U[k]\cdot Dg)_y(0)=c[k]g_y(0)=0\). The normalized inverse gives c[T(k)]=0. Its high norm is bounded by the left side of (5), so T maps the ball to itself.

For two inputs k,l,

\[
A_k(T(k)-T(l))=-U[k-l]\cdot DT(l).
\]

The streamfunction divergence identity implies
\(\|U[z]\cdot Dv\|_H\le\|z\|_H\|Dv\|_\infty\). This forcing is also in L2, because z and v belong to N_s. The consistent low realization of A_k therefore applies to the difference and gives (6). The high ball with its strain constraint is H-complete, so Banach's fixed point theorem yields h. Any solution in that ball obeys the same high inverse equation, proving uniqueness there.

For completeness q<1 does not add a hidden smallness condition to (5). The condition \(\beta_r>0\) implies \(r/\sqrt{s}<1/50\), and \(c_s\sqrt{s}<3/10\); hence \(c_s r<3/500\). This gives \(q<3/1897<1\). Positivity of the corrected center slope follows from the baseline lower bound \(a_0>7/10\) and the same derivative estimate. Under B11, fixed leading-tail preservation is the N_s decay argument proved in the operator audit.

## 4. Scalar certificate and comparison

Inequality (5) is exactly

\[
(r-m)(\mu-Ar)-Br-\epsilon\ge0.\tag{7}
\]

For a preselected r it is enough to check this rationally after enclosing \(\sqrt{s}\). To search for a radius, the equivalent quadratic is

\[
-Ar^2+(\mu+Am-B)r-\mu m-\epsilon\ge0,
\]

with the separate requirements \(r\ge m\) and \(r<\mu/A\). A nonnegative discriminant alone is not the full certificate.

If g=0, then m=B=0 and D=F. Equation (7) reduces to the original high-norm criterion \(N_s(F)\le r(\mu-Ar)\). Thus this theorem contains the original residual estimate. With a useful g it can be stronger because D is a linear defect and the part Lg is retained exactly.

At s=2^(-18), two entirely rational sufficient boxes illustrate the test:

- m<=2^(-17), epsilon<=2^(-23), B<=1/100 and r=2^(-16) give beta_r=873/20480 and slack in (7) at least 717/13421772800.
- m<=2^(-16), epsilon<=2^(-25), B<=1/200 and r=3*2^(-17) give beta_r=473/20480 and slack at least 429/13421772800.

The script `verification/check_scalar_certificate.py` verifies these fractions and the quadratic identity using exact rational arithmetic. These are sufficient parameter boxes, not measured properties of an IPM profile.

This comparison proves no numerical improvement for the current candidate set. The numerical verification targets are now concrete: an admissible g, its N_s upper bound m, its defect norm epsilon, and the eight derivative bounds a1,a2,w2,w3,S1,S2,S3,S4 (with overlap allowed). A corrected reference with lower training loss does not provide those certificates.

## Dependencies and remaining work

The original high/low inverses and background conditions are retained. Section 2 is a new explicit fixed-factor multiplication bound; Section 3 uses it without a high-to-high estimate for the nonlinear map h -> U[h].Dh. There is no finite-dimensional inference of infinite-dimensional invertibility. No numerical g or validated defect has been produced by T4. This is an alternative sufficient test, not a claim of a closed IPM existence proof.
