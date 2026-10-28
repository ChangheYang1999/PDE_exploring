# Audit of the lead's finite-part direction maximum

## Statement and scope

Use the real homogeneous Hölder space and normalized kernels in `../../01_setup/PROOF.md`. Put $a=1/2$, $G(w)=w/[\pi(w^2-a^2)^2]$, $\nu_b=\operatorname{Re}(e^{2ib}G)$, and

$$N(b)=\lim_{\rho\downarrow0}\left\{\frac12\int_{\mathbb C\setminus(B_\rho(a)\cup B_\rho(-a))}|\nu_b(w)|\,dA(w)+\frac2\pi\log\rho\right\}.$$

Then $N$ is even, $\pi/2$ periodic, and strictly increasing on $[0,\pi/4]$. Its maximum is $N(\pi/4)=1/2$. Consequently, using the general-direction asymptotic theorem in `../../06_small_alpha_second_term/general_direction/PROOF.md`,

$$C_\alpha=\frac2{\pi\alpha}+\frac12+\frac{\log2-1}{\pi}+o(1).$$

This document audits the lead's Green-formula proof. The independent annular-residue/Jacobi proof is in `../../06_small_alpha_second_term/direction_maximum/PROOF.md`. The diagonal value is proved in `../../06_small_alpha_second_term/diagonal/PROOF.md`. The optional closed formula for $N(0)$ in the lead's draft is not needed here and is not certified by this audit.

## Uniform finite-part moments

Let $\Theta=2\arg G$ and

$$M_n(\rho)=\int_{\mathbb C\setminus(B_\rho(a)\cup B_\rho(-a))}|G|e^{in\Theta}\,dA,\qquad n\ge1.$$

Conjugation makes these moments real. Near $a$, write $w=a+re^{it}$ and $G=(2\pi r^2)^{-1}e^{-2it}u(w)$, where $u=2w/(w+a)^2$ is holomorphic and $u(a)=1$. The phase map $\Theta=-4t+2\arg u$ has derivative $-4+O(r)$. Changing variables on its four covering branches gives an angular density $1/4+O(r)$, uniformly in $n$. The constant term integrates to zero against $e^{in\Theta}$. Thus every annulus between radii $\rho$ and $\rho'$ contributes at most $C|\rho-\rho'|$, uniformly in $n$. The same argument holds at $-a$, and the remaining absolute integral is finite. Therefore $M_n=\lim M_n(\rho)$ exists and is uniformly bounded in $n$.

The difference $|\cos(\Theta/2+2b)|-|\cos(\Theta/2)|$ has zero mean and absolutely summable Fourier coefficients. Uniform boundedness of the moments therefore justifies termwise passage to the finite part. The cosine Fourier series gives

$$N(b)-N(0)=\frac2\pi\sum_{n\ge1}\frac{(-1)^{n+1}(\cos4nb-1)M_n}{4n^2-1}.$$

## Green-formula evaluation

Under $z=4w^2$, accounting for both sheets and the area Jacobian gives

$$M_n=\frac1\pi\operatorname{pv}\int_{\mathbb C}z^{p-1}\overline z^{q-1}(1-z)^{-2n-1}(1-\overline z)^{2n-1}\,dA(z),$$

where $p=3/4+n/2$, $q=3/4-n/2$. Powers are paired so that their exponent difference is an integer. The images of the two removed circles coincide and differ from the circle $|z-1|=4\rho$ by an annulus of thickness $O(\rho^2)$. Since the integrand is $O(\rho^{-2})$, this changes the integral by $O(\rho)$.

Set

$$Q(\zeta)=\sum_{k=0}^{2n-1}\frac{(-1)^k\binom{2n-1}{k}}{q+k}\zeta^{q+k},\qquad
U(z)=z^{p-1}(1-z)^{-2n-1}Q(\overline z).$$

The denominators are nonzero quarter-integers. Every paired term is single-valued, and $\partial_{\overline z}U$ is the integrand. Also $U=O(|z|^{1/2})$ at zero and $U=O(|z|^{-3/2})$ at infinity, so their boundary integrals vanish. On the clockwise circle around one, expansion in $h=z-1$ gives

$$U=-h^{-2n-1}(1+h)^{p-1}Q(1+\overline h).$$

Only terms with holomorphic exponent $2n+k$ and antiholomorphic exponent $k$ survive angular integration. Every $k>0$ term vanishes as $\rho^{2k}$, leaving

$$M_n=\binom{p-1}{2n}Q(1).$$

The rational identity

$$Q(1)=\frac{(2n-1)!}{q(q+1)\cdots(q+2n-1)}$$

follows first by integrating the beta polynomial when $q>0$, then by equality of rational functions. Cancelling the common factors yields

$$M_n=\frac{(-1)^n}{2n}P_n,\qquad
P_n=\prod_{k=0}^{n-1}\frac{2n+1+4k}{2n+3+4k}.$$

In particular $M_1=-3/10$. Substitution into the Fourier formula gives

$$N(b)-N(0)=\frac1\pi\sum_{n\ge1}\frac{P_n(1-\cos4nb)}{n(4n^2-1)}.$$

## Strict maximum

Extend the product by

$$P(t)=\frac{\Gamma(t/2+3/4)\Gamma(3t/2+1/4)}{\Gamma(t/2+1/4)\Gamma(3t/2+3/4)},\qquad t>0.$$

The digamma integral gives

$$\frac{d}{dt}\log P(t)=\int_0^\infty e^{-tu}\left(\frac1{2\cosh(u/2)}-\frac1{2\cosh(u/6)}\right)du<0.$$

Differentiation makes the integrand positive, so $(\log P)''>0$ and $P''>0$. Hence $c(t)=P(t)/(4t^2-1)$ is positive, decreasing and strictly convex for $t\ge1$. This uses the product rule: both factors and their second derivatives are positive, and both first derivatives are negative.

For $d_m=c(m)-2c(m+1)+c(m+2)>0$, two summations by parts give, at $0<\theta<\pi$,

$$\sum_{n\ge1}c(n)\sin(n\theta)=\sum_{m\ge1}d_m\frac{(m+1)\sin\theta-\sin((m+1)\theta)}{4\sin^2(\theta/2)}>0.$$

The boundary terms vanish since $c(n)=O(n^{-2})$. Each displayed numerator is positive: $|\sin(k\theta)|<k\sin\theta$ for integer $k\ge2$ and $0<\theta<\pi$. Termwise differentiation of the absolutely convergent direction series is valid, and gives $N'(b)=(4/\pi)\sum c(n)\sin(4nb)>0$ for $0<b<\pi/4$. Symmetries give the claimed global maximum. The separately proved diagonal value finishes the argument.

## Audit conclusions

The lead's principal-value cutoff conversion, two-sheet factor, Green-formula orientation, gamma-product cancellation, uniform Fourier passage, and strict sine-series argument are correct. The independent proof arrives at the same moments using different local coordinates. No unverified numerical value or optional axis formula enters the theorem.
