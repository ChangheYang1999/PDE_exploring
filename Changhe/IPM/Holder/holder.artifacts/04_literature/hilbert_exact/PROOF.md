# Exact real-line Hilbert-transform Hölder seminorm

Status: independent proof, motivated by a checked exact periodic theorem of V. F. Babenko. This auxiliary result belongs to the requested literature comparison. It is not transferred without proof to a two-dimensional operator.

## Statement and normalization

For $0<\alpha<1$, let $[f]_\alpha=\sup_{x\ne y}|f(x)-f(y)|/|x-y|^\alpha$ on the real line. Normalize the Hilbert transform by

$$Hf(x)=\frac1\pi\operatorname{pv}\int_{\mathbb R}\frac{f(z)}{x-z}\,dz.$$

For general homogeneous Hölder inputs it is defined modulo constants through the difference of the two kernels, with separate local principal values. This difference converges at infinity since it is $O(|z|^{-2})$, whereas an anchored input grows at most $|z|^\alpha$. The exact real-input norm is

$$\|H\|_{\dot C^\alpha(\mathbb R)\to\dot C^\alpha(\mathbb R)}
=N_\alpha=\frac{2^{1-\alpha}}\pi
B\left(\frac{1-\alpha}{2},\alpha\right).$$

The gamma duplication formula gives the equivalent symmetric expression

$$N_\alpha=\frac{\Gamma(\alpha/2)\Gamma((1-\alpha)/2)}{\pi^{3/2}}=N_{1-\alpha}.$$

The same sharp value is obtained by the supremum over $C_c^\infty(\mathbb R)$. In particular

$$\alpha N_\alpha\longrightarrow\frac2\pi\quad(\alpha\downarrow0),\qquad
(1-\alpha)N_\alpha\longrightarrow\frac2\pi\quad(\alpha\uparrow1).$$

## Reciprocal pairing proves the upper bound

Translation reduces any pair of evaluation points to $-a,a$, where $a>0$. The difference kernel is

$$\frac1\pi\left(\frac1{a-z}-\frac1{-a-z}\right)
=\frac{2a}{\pi(a^2-z^2)}.$$

It is positive on $(-a,a)$ and negative on its complement. Pair each $u\in(0,a)$ with $\rho(u)=a^2/u$, and pair $-u$ with $-\rho(u)$. The change of variables has the exact mass identity

$$\frac{2a}{\rho(u)^2-a^2}|\rho'(u)|
=\frac{2a}{a^2-u^2}.$$

Consequently the transform increment equals

$$Hf(a)-Hf(-a)=\frac{2a}\pi\int_0^a
\frac{f(u)-f(a^2/u)+f(-u)-f(-a^2/u)}{a^2-u^2}\,du.$$

The equality follows first with finite exterior cutoffs and excisions at $\pm a$, then by a limit. Reciprocal pairing changes a symmetric singularity cutoff by $O(\varepsilon^2)$; the unmatched interval contributes $O(\varepsilon)$ for the constant part and $O(\varepsilon^\alpha)$ for the Hölder remainder. Both vanish. The final paired integrand is integrable near $u=a$ as $(a-u)^{\alpha-1}$ and near zero as $u^{-\alpha}$.

Applying the Hölder inequality for increments and putting $u=av$ gives

$$\frac{|Hf(a)-Hf(-a)|}{(2a)^\alpha}
\le [f]_\alpha\frac{2^{2-\alpha}}\pi
\int_0^1 v^{-\alpha}(1-v^2)^{\alpha-1}\,dv
=N_\alpha[f]_\alpha.$$

This proves the upper bound for every pair of points.

## One function saturates every paired constraint

Fix $a>0$ and define for $s>0$

$$w(s)=\alpha\left|\frac{a^2}{s}-s\right|^{\alpha-1},\qquad
f(x)=-\int_a^{|x|}w(s)\,ds.$$

The integrable singularity at $s=a$ has order $|s-a|^{\alpha-1}$. At zero, $w(s)$ tends to zero like $s^{1-\alpha}$. Hence $f$ is a well-defined continuous even function. At infinity it grows at most a constant times $|x|^\alpha$.

We claim that every interval $[u,v]\subset[0,\infty)$ satisfies

$$\int_u^v w(s)\,ds\le(v-u)^\alpha.$$

For a fixed positive length $\ell$, the function $I(u)=\int_u^{u+\ell}w(s)\,ds$ is continuous on $u\ge0$, tends to zero as $u\to\infty$, and is not maximized at zero since $w(0)=0<w(\ell)$, with the derivative interpreted one-sided if $\ell=a$. The weight increases strictly up to $a$ and decreases strictly after $a$. Thus a maximizing interval straddles $a$. Away from endpoints equal to $a$, differentiation gives $I'(u)=w(u+\ell)-w(u)$, and the unique equality is

$$u(u+\ell)=a^2.$$

At the endpoint positions touching $a$, the one-sided derivative has the appropriate strict sign, so they are not maxima. Equivalently, direct monotonic comparison of the endpoint weights shows that $I$ increases until the reciprocal pair and decreases afterward. Thus the maximum occurs at $v=a^2/u$.

For such a pair, put $A(u)=a^2/u-u$. Both endpoints have weight $\alpha A(u)^{\alpha-1}$. Differentiating the paired integral gives

$$\frac d{du}\int_u^{a^2/u}w(s)\,ds
=-\alpha A(u)^{\alpha-1}(1+a^2/u^2)
=\frac d{du}A(u)^\alpha.$$

Both quantities vanish as $u\uparrow a$, so the paired integral equals $A(u)^\alpha$. This proves the interval claim and equality on every reciprocal pair.

For arbitrary real $x,y$, evenness and $||x|-|y||\le|x-y|$ now give $|f(x)-f(y)|\le|x-y|^\alpha$. Equality on reciprocal pairs proves $[f]_\alpha=1$. In the transform increment, both paired differences are positive and attain their Hölder bound. Hence the upper estimate is an equality, proving the norm formula.

The compact-support approximation uses the same metric-extension and positive-mollification argument as the two-dimensional upper-bound proof, now on the real line. The kernel difference is integrable against the uniform growth majorant. Thus fixed output increments converge and the sharp norm over smooth compact inputs is the same.

## Relation to the checked periodic source

V. F. Babenko, *Sharp Estimates for Norms of Functions from Conjugate Classes in Metrics C and L*, arXiv:1402.0829v1, Theorem 1(2), states an exact formula for the maximal conjugate-function increment over periodic functions with a prescribed concave Dini modulus. The paper is an English translation of a 1973 publication, as stated in its first-page footnote. Its conjugate kernel is normalized by $-1/(2\pi)\cot((t-x)/2)$.

For increment length $h\in(0,\pi)$ the theorem uses the pairing determined by

$$\int_0^u\frac{\sin(h/2)}{\cos v-\cos(h/2)}\,dv
=-\int_{\rho(u)}^\pi\frac{\sin(h/2)}{\cos v-\cos(h/2)}\,dv.$$

Direct integration solves it as

$$\tan\frac{\rho(u)}2\tan\frac u2=\tan^2\frac h4.$$

After rescaling and sending $h$ to zero this becomes the reciprocal pairing above. The real-line proof does not depend on taking this limit or on unverified details of the cited extremal lemma. The exact periodic theorem has been read in the source; the real-line norm has been proved here independently.
