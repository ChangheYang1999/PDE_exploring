# Certified obstruction on the fitted reference

**Question (1): CONFIRMED.** The exact reference in the question satisfies

$$
0.2830400682<\mathcal B(A_0,e_0,w_0)<0.2851567624.
\tag{1}
$$

Thus \(b_0=7/25=0.28\) is a certified positive lower bound. The numerical value \(0.284073229231419611\ldots\) is consistent with (1); its extra digits are not certified here. No pointwise certificate of \((H_-)\) is claimed or needed.

## Exact statement, notation, and dependencies

The exact decimals are \(A_0=10.150725\), \(L_0=8.6000638\), and \(e_0=L_0^{-2}\). The exact coefficient strings are frozen in [data/fitted_reference.json](data/fitted_reference.json), copied byte for byte from fred22. [../INPUTS.json](../INPUTS.json) records the input paths and SHA-256 digests. Throughout,

$$
w_0(u)=-A_0u\frac{1-u^2}{1+u^2}
+u^3(1-u^2)^2q(u^2).
\tag{2}
$$

The plus sign is necessary. It is missing typographically in the displayed definition in fred22/05-reference-fit/PROOF.md; its factorization, code, JSON, and the question all use (2).

For a compatible trace \(w\) at \(A>2\), put

$$
\beta=2/A,\quad g'/g=(w'-A)/w,\quad g/u^2\longrightarrow1,\quad
Q=(g'-ew'')/(2g^3),\quad m=-w/g.
$$

We use the supplied functional identity from FINAL_REPORT §6.3.1(i):

$$
\mathcal B(A,e,w)=\frac{(\beta-1)A^{1-\beta}}3
\operatorname{FP}\int_0^1(Q-Q(1))m^{\beta-2}g^{-1}\,du.
\tag{3}
$$

The finite part removes the three divergent powers at zero. There is no logarithmic resonance when \(0<\beta<1\). The certificate below proves a bound on this explicitly defined scalar functional; it uses no PDE endpoint theorem or existence assumption.

For a physical source \(L\), the substitutions
\(\widetilde w(u)=w_{\rm phys}(Lu)/L\),
\(\widetilde g(u)=g_{\rm phys}(Lu)/L^2\), \(e=L^{-2}\) give
\(Q_{\rm phys}(Lu)=L^{-5}Q(u)\), \(m_{\rm phys}(Lu)=L^{-1}m(u)\). Substituting \(dx=L\,du\) in (3) proves

$$
\mathcal B=L^{4+\beta}B_3.
\tag{4}
$$

Thus (1) is in the requested normalized natural units.

## Geometry and reconstruction

Set \(H(t)=A_0-t(1-t^2)q(t)\). Exact rational Bernstein arithmetic proves

$$
A_0\le H(t)<11,\qquad q(t)<0\quad(0\le t\le1).
\tag{5}
$$

Here is the full polynomial enclosure argument. On each of the 128 intervals \([a,b]=[i/128,(i+1)/128]\), write \(p(a+(b-a)s)=\sum c_ks^k\). If \(n=\deg p\), its Bernstein coefficients are

$$
c_k=\sum_{m=k}^np_m{m\choose k}a^{m-k}(b-a)^k,\qquad
b_j=\sum_{k=0}^jc_k\frac{{j\choose k}}{{n\choose k}}.
$$

The polynomial lies between the smallest and largest \(b_j\), since the Bernstein basis is nonnegative and sums to one. All inputs and operations are `Fraction` arithmetic. The exact extrema of these coefficient bounds are saved in the JSON. In particular no samples establish (5).

Factorization gives \(w_0=-u(1-u^2)H(u^2)/(1+u^2)\). It is therefore negative on \((0,1)\), odd and analytic near the whole real interval, with \(w_0'(0)=-A_0\), \(w_0(1)=0\), \(w_0'(1)=A_0\), and \(-w_0/[u(1-u)]\ge A_0\).

Define

$$
T(t)=\frac12\int_0^t\frac{(1+s)^2q(s)}{H(s)}\,ds.
$$

The exact reconstruction is

$$
g_0(u)=\frac{u^2H(u^2)}{A_0(1+u^2)}e^{T(u^2)}.
\tag{6}
$$

To verify it, put \(z=-w_0/(A_0u)\) and
\(E(u)=\int_0^u(z(s)^{-1}-1)\,ds/s\). Then \(g=u^2ze^E\) has the required logarithmic derivative and normalization. Differentiation in \(t=u^2\) gives \(E(\sqrt t)=-\log(1-t)+T(t)\), with both sides zero at zero. Substitution cancels \(1-t\) and proves (6).

In particular

$$
g_*=\tfrac12e^{T(1)},\quad
w_{2*}=w_0''(1)=A_0+8q(1)=0.7768297940321664.
\tag{7}
$$

The last decimal is an exact identity. Interval arithmetic proves

$$
0.40222790015<g_*<0.40222790016.
\tag{8}
$$

## Parameter separation

For the slice \(w=(A/A_0)w_0\), put \(f=w_0/A_0\) and \(n=-f/g_0\). The reconstruction is independent of \(A\). Define

$$
Q_g=g_0'/(2g_0^3),\quad Q_w=-w_0''/(2A_0g_0^3),\quad
J_i(\beta)=\operatorname{FP}\int_0^1(Q_i-Q_i(1))n^{\beta-2}g_0^{-1}\,du.
$$

Substitution in (3) proves

$$
B_0(A,e)=c(A)\{J_g(\beta)+eA J_w(\beta)\},\qquad
c(A)=(\beta-1)/(3A).
\tag{9}
$$

The code encloses \(J_i,J_i',J_i''\) at \(\beta_0\) and uniformly on
\([2/(A_0+0.06),\,2/(A_0-0.06)]\).

## Rigorous endpoint and middle integration

Split the integral at \(u_c=1/4\) and \(1-d_e=15/16\).

At zero write \(t=u^2\), \(D=2tz_t\), \(J=-w_0''/(A_0u)\), and \(E=-\log(1-t)+T(t)\). The integrands in \(J_i\) become

$$
u^{-5-\beta}F_i(u^2)-Q_i(1)u^{-\beta}V(u^2),
$$

$$
F_g=\tfrac12z^{-4}e^{-(\beta+1)E}(1+z+D),\quad
F_w=\tfrac12z^{-4}e^{-(\beta+2)E}J,\quad
V=z^{-1}e^{(1-\beta)E}.
\tag{10}
$$

Indeed \(n=u^{-1}e^{-E}\) and \(ug'/g=(1+z+D)/z\), which directly give (10). For each factor use Taylor coefficients through degree 11 at \(t=0\) and bound its twelfth normalized derivative on **all** of \([0,1/16]\). Taylor's theorem places the remainder in \(t^{12}\) times this derivative interval. Integrate each polynomial term exactly:

$$
\operatorname{FP}\int_0^{u_c}u^{2k-5-\beta}\,du
=\frac{u_c^{2k-4-\beta}}{2k-4-\beta}.
\tag{11}
$$

The remainder uses \(k=12\), where the integral is ordinary. For \(V\), replace \(2k-4-\beta\) by \(2k+1-\beta\).

For parameter derivatives, \(F_i^{(j)}=(-E)^jF_i\) and \(V^{(j)}=E^jV\). Leibniz's rule combines these with derivatives of (11). If \(I=r^{p-\beta}/(p-\beta)\), then

$$
I'=I(-\log r+(p-\beta)^{-1}),\quad
I''=I[(-\log r+(p-\beta)^{-1})^2+(p-\beta)^{-2}].
\tag{12}
$$

In the remainder integrals the powers of \(-\log u\) have constant sign, so their exact moments can multiply the interval derivative bounds. This handles the logarithmic finite parts as well as the value.

At the source put \(s=1-u\), \(a=-w_0/(1-u)\), and \(L=\log(a/(A_0g_0))\). The smooth factor multiplying \(s^{\beta-1}\) is

$$
F_i(s)=\frac{Q_i(1-s)-Q_i(1)}s(a/A_0)^{\beta-2}g_0^{1-\beta}.
\tag{13}
$$

Its beta derivatives are \(F_iL^j\). Use degree 9 and a bound on the tenth normalized derivative throughout \(0\le s\le1/16\). To avoid interval division by \(s\), write the quotient as \(-\int_0^1Q_i'(1-ts)\,dt\). Its \(k\)-th normalized derivative is a weighted average of
\((-1)^{k+1}Q_i^{(k+1)}/(k+1)!\), with weight \((k+1)t^k\) of mass one. Its range is therefore enclosed by the interval for this derivative of \(Q_i\) on the whole source interval. At zero this is the exact endpoint coefficient. Taylor multiplication now bounds (13), including its remainder.

The source moments are \(d_e^{k+\beta}/(k+\beta)\). Their first derivative multiplies by \(\log d_e-1/(k+\beta)\), and the second by the square of that quantity plus \(1/(k+\beta)^2\). Each power of \(\log s\) has constant sign, so the same remainder argument applies.

On the middle interval use 88 equal panels. On \([c-d,c+d]\), integrate the degree-7 Taylor polynomial at \(c\). Taylor's theorem encloses the error in

$$
\frac{2d^9}{9}\operatorname{range}_{[c-d,c+d]}\frac{F^{(8)}}{8!}.
\tag{14}
$$

This is applied separately to the integrand and its first two beta derivatives, obtained by insertion of \((\log n)^j\).

Finally \(T\) itself is enclosed by the degree-9 version of (14) on 64 panels, applied to its rational derivative. Prefix integrals and one partial-panel integral give \(T\) at every required rational argument. Equation (5) proves \(T'<0\), so endpoint enclosures bound its value on entire intervals.

## Arithmetic verification and derivative bounds

[verification/certify.py](verification/certify.py) implements the preceding operations in `mpmath.iv` at 40 decimal places. Jet coefficients are normalized derivatives. Their recurrences follow from the product rule, \(XX^{-1}=1\), \((\log X)'=X'/X\), and \((e^X)'=X'e^X\). Evaluating these recurrences with interval constants encloses every derivative at every point in the input interval. Every reciprocal checks that zero is avoided. Polynomial translations are exact rational changes of basis.

[data/obstruction_certificate.json](data/obstruction_certificate.json) stores exact rational interval endpoints for \(T(1)\), \(g_*\), the three integral pieces, their totals, and the parameter derivatives. Printed floating-point displays are not the certificates.

Writing \(J=J_g+eA J_w\), differentiation of (9) gives

$$
B_A=c'J+c(eJ_w+\beta'J_\beta),\qquad B_e=cA J_w,
$$

$$
B_{AA}=c''J+2c'(eJ_w+\beta'J_\beta)
+c(2e\beta'J_w'+\beta''J_\beta+(\beta')^2J_{\beta\beta}),
$$

$$
B_{Ae}=c'A J_w+c(J_w+A\beta'J_w'),
$$

where \(c'=(A-4)/(3A^3)\), \(c''=(12-2A)/(3A^4)\),
\(\beta'=-2/A^2\), \(\beta''=4/A^3\). The stored enclosures prove

$$
|B_A(A_0,e_0)|<0.007,\quad |B_e(A_0,e_0)|<7.1,\quad
\sup|B_{AA}|<0.007,\quad \sup|B_{Ae}|<1.85.
\tag{15}
$$

The suprema cover the full requested parameter rectangle. Equations (1), (8), and (15) are checked by comparing the exact stored endpoints to the displayed rational bounds. This is an interval arithmetic proof, not a proof-assistant formalization or a claim that \(w_0\) solves IPM.
