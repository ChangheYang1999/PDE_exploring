# Higher source traces under explicit regularity

Date: 2026-10-20. Status: proved under the hypotheses below. This is a local result, not an existence or nonexistence theorem for the IPM profile class.

## Statement and notation

Use coordinates (s,y) centered at P, put r=-s, and fix A>1. Let n>=2 be even, 0<alpha<1, and alpha>1-n/A. In a neighborhood of P assume

* f and W=(a,b) belong to C^{n,alpha}; f,b are odd in y and a is even in y;
* W.grad f=f, div W=A+1, W(P)=0, DW(P)=diag(A,1), and f_y(P)=g_*>0;
* f and W are smooth in a neighborhood of each point (s,0) with s<0 sufficiently small.

Then, as r decreases to zero,

    |partial_y^{n+1} f(-r,0)| <= C r^{alpha-1}.

In particular, if G_{n+1}=partial_y^{n+1}f/(n+1)! and H_{n+1} is a positive axis integrating factor comparable to r^{-n/A}, then G_{n+1}/H_{n+1} tends to zero.

The smoothness assumption on the punctured axis supplies the trace being estimated. Its deduction from center smoothness for IPM profiles is a separate transport regularity argument, audited in verification/c1_audit.md. It is not implicit in the C^{n,alpha} hypothesis at P.

## Finite punctured regularity version

In the statement, it suffices that f and W are C^{n+1} in a neighborhood of each punctured-axis point, instead of smooth there. The distributional identity below uses only C^{n,alpha} on the cone. Its characteristic estimate uses no higher derivatives. At the last step the sole additional requirement is that f_n(s,y) is differentiable in y at each fixed s<0, supplied by C^{n+1}. Thus exactly the same proof gives the same bound and source limit under this finite replacement. A later use of an axis ODE can require additional punctured regularity, which must be provided separately.

## Exact transport identity

Write f_k=partial_y^k f, a_k=partial_y^k a, b_k=partial_y^k b, D=a partial_s+b partial_y, and h=f_1/a, wherever a is nonzero. Define

    K_n = f_n - h a_{n-1}.

For smooth fields with E=Df-f and V=div W, direct differentiation gives

    (D+n b_1-1)K_n - F_n
      = E_n - (a_{n-1}/a) E_1 - f_1 V_{n-1},

where

    F_n = (a_1 a_{n-1}/a-a_n)(f_s+b h)
          - sum_{k=1}^{n-1} binom(n,k) a_k partial_s f_{n-k}
          - sum_{k=2}^{n-1} binom(n,k) b_k f_{n+1-k}
          + (a_s-(n-1)b_1) h a_{n-1}.

Here and below an empty sum is zero. To verify the identity, differentiate Df-f n times, keeping the k=n terms outside the sums. The first derivative of the original equation gives

    D h = (1-b_1-a_s)h - (a_1/a)(f_s+b h) + E_1/a.

Also D a_{n-1}=a(V_{n-1}-b_n)+b a_n. Subtract D(h a_{n-1}) from D f_n. The terms b_n f_1 cancel and the remaining terms are exactly the displayed identity. This establishes every highest derivative cancellation before an estimate is made.

For C^{n,alpha} fields the resulting equation (D+n b_1-1)K_n=F_n holds in distributions away from a=0. Indeed, mollify locally. The commutator error E_epsilon tends to zero in C^{n-1}, hence its n-th derivative tends to zero in distributions, and E_{epsilon,1} tends uniformly to zero. The constant divergence is preserved on smaller neighborhoods. The other terms in K_n and F_n converge uniformly. Multiplication of E_{epsilon,n} is unnecessary in this identity. In C^2 local flow coordinates, available since n>=2, the equation is a one-dimensional distributional ODE with continuous coefficients and right side. Integration shows it holds along each characteristic. Continuity extends the identity from almost every transverse parameter to every parameter.

## Cone estimates

Work in the left cone 0<r<r_0, |y|<=kappa r, with kappa and r_0 sufficiently small. Taylor expansion and parity imply

    a=As+O(r^2),        b=y(1+O(r)),
    a_s=A+O(r),         b_1=1+O(r),
    f_1=g_*+O(r),      f_s=O(|y|).

Let c_*=a_n(P) and lambda=g_* c_*/A. Since a_{n-1} is odd in y and a_n is alpha-Hoelder,

    a_{n-1}=c_* y+O(|y|r^alpha),
    h=g_*/(As)+O(1).

Consequently, with R=K_n+lambda y/s,

    |R(s,y)| <= C (|y|^alpha+|y|r^{alpha-1}).                 (1)

This uses f_n(s,0)=0 and the alpha-Hoelder continuity of f_n. It is valid also if c_*=0.

In the first binomial sum defining F_n, when k is odd, a_k is odd and is O(y), with its next derivative bounded; when k is even, partial_s f_{n-k} is odd and is O(y), again with one further derivative available. The endpoint k=n-1 has the same property. In the second sum, even k makes b_k odd, and odd k makes f_{n+1-k} odd. The available derivative orders do not exceed n. Thus both sums are O(|y|).

The product containing a_1 a_{n-1}/a is O(|y|^3/r^2)=O(|y|). In -a_n(f_s+b h), the leading term is -lambda y/s. The final term contributes (A-n+1)lambda y/s. All coefficient remainders are O(|y|r^{alpha-1}); O(|y|) fits this bound. Hence

    F_n=(A-n)lambda y/s+O(|y|r^{alpha-1}).

Moreover

    (D+n b_1-1)(y/s)=(n-A)y/s+O(|y|).

The singular terms cancel, leaving

    (D+n b_1-1)R=O(|y|r^{alpha-1}).                         (2)

## Backward characteristics and the exponent condition

Let a characteristic start at (-r,y), with eta=|y|/r in (0,kappa). For negative time t while it stays in the cone,

    r_t comparable to r exp(A t),    |y_t| comparable to |y| exp(t),

with comparison constants uniform in the starting point and backward travel time used here. In fact d log r_t/dt=A+O(r_t) and d log|y_t|/dt=1+O(r_t); the accumulated errors are bounded by C integral r_t dt <=Cr. Choose

    (1-alpha)/(n-1+alpha) < theta < 1/(A-1).

Such a theta exists exactly when alpha>1-n/A. Put T=theta log eta<0. Since eta exp((1-A)T)=eta^{1-theta(A-1)}, the backward segment [T,0] stays in a slightly larger left cone after reducing kappa if necessary.

The integrating factor for (2) is comparable to exp((n-1)t). The two terms of (1) at time T, multiplied by this factor, are bounded respectively by

    C |y|^alpha exp((n-1+alpha)T),
    C |y|r^{alpha-1} exp((n-A(1-alpha))T).

The first is at most C|y|r^{alpha-1} by the lower bound on theta; the second has that bound because n-A(1-alpha)>0. The forcing integral in (2) is at most

    C |y|r^{alpha-1} integral_T^0 exp((n-A(1-alpha))t) dt
      <= C' |y|r^{alpha-1}.

It follows that |R|<=C|y|r^{alpha-1}. The definition of R and the preceding expansion of h a_{n-1} now give

    |f_n(s,y)| <= C|y|r^{alpha-1}.

For each fixed s<0 the punctured-axis smoothness assumption permits division by y and passage to y=0. This proves the stated trace bound and the vanishing of G_{n+1}/H_{n+1}.

## Convergence of the source integral

For application to the axis hierarchy let j=n+1, q=n/A, w=a(s,0)<0, g=f_y(s,0)>0, and m=-w/g. Then m is comparable to r, m'=-A/g in the IPM axis system, and

    H_j=A^q g^j m^{-q}.

Suppose the hierarchy is written in the exact form

    F_j=L_j+(g^{j+1}/j) Q_j',       Q_j=W_{1,j-1}/g^j,

where W_{1,j-1} is the y^{j-1} Taylor coefficient of a. The lower-jet term L_j is bounded under the stated C^{j-1,alpha} hypotheses; Q_j is alpha-Hoelder at P. Then the L_j term in F_j/(wH_j) is O(r^{q-1}), which is integrable. The other term is

    -(j A^q)^{-1} m^{q-1} Q_j'.

For its integral, integrate by parts after subtracting Q_j(P). The boundary term m^{q-1}(Q_j-Q_j(P)) tends to zero, and the new integrand is O(r^{q+alpha-2}). Both statements use alpha+q>1, exactly the same condition as above. This proves convergence of the improper source integral; absolute integrability of the original derivative term is not asserted.

Thus the source constant ell_j exists and is zero under these hypotheses. At a nonresonant center, the separately derived relation C_{0j}=ell_j+B_j then makes center smoothness imply B_j=0. At a resonant center the logarithmic compatibility condition must be used instead; this proof does not force the finite-part number B_j to vanish.

## Dependencies and scope

The cone argument above is local and complete. Its IPM application uses the canonical inverse regularity and transport propagation audited in verification/c1_audit.md, the axis hierarchy, and the stated nonresonant center relation. For j=3 the condition is alpha>1-2/A; for j=5 it is alpha>1-4/A. The latter proof requires C^{4,alpha} at P. It does not upgrade the default C^{2,alpha} class to that regularity, even when A<4/3. No conclusion about existence of a global profile follows.


## Local chart, harmonic remainder and thin odd packets (D8 audit)

The following statements supplement the higher-source trace proof above. They are local statements at P and do not settle the fifth endpoint under only the original class regularity.

Let W(X)=LX+R(X), L=diag(A,1), 1<A<2, and assume W is C^(1,1), W(0)=0, DW(0)=L. Backward trajectories obey |Phi_t X|<=2|X|e^t on a sufficiently small ball for t<=0: apply scalar comparison to d_tau |Phi_(-tau)X|<=-|Phi_(-tau)X|+C|Phi_(-tau)X|^2. The variational equation gives |DPhi_t|<=C e^t because the integral of |Phi_t X| is bounded. Hence e^(-Lt)R(Phi_t X) and its X derivative have bounds C|X|^2 e^((2-A)t) and C|X|e^((2-A)t). Their integrals converge uniformly. Thus Xi=X-int_(-infinity)^0 e^(-Lt)R(Phi_t X)dt is C^1, tangent to the identity, and Xi(Phi_tau X)=e^(L tau)Xi(X) follows by translating the integral limit. It is a local chart by the inverse function theorem. Under only C^(1,gamma), the same proof uses exponent 1+gamma-A and needs A<1+gamma. This is a condition on this construction, not a necessary condition for every possible chart.

If W.grad f=f and f is differentiable with Df(0)=(0,g*), then f(X)=e^(-t)f(Phi_t X)=g* e^(-t)(Phi_t X)_2+e^(-t)o(|Phi_t X|). The error tends to zero since e^(-t)|Phi_t X| is bounded. Taking t to minus infinity proves f=g*Xi_2. No higher chart derivatives follow from this proof.

Constant divergence and curl b_s-a_y=-f_s give Delta a=f_sy and Delta b=-f_ss by differentiation and elimination. A difference of two local velocities with these data has zero divergence and curl. On a disk it is the gradient of a harmonic function. It is not an arbitrary smooth field. For localized C^(2,alpha) density, interior elliptic regularity and the smooth exterior harmonic remainder supply local C^(2,alpha) velocity, with no general derivative gain from the degree-zero multipliers.

Here is a direct bound for a thin odd density packet p(s,y)=M F((s-s0)/r,y/h), F Schwartz and odd in its second argument, epsilon=h/r<=1. Take the Fourier transform only in the first scaled variable and put k=epsilon|xi|. The transverse Green kernels of the multipliers give

    T1 F = (i epsilon xi/2) int sgn(Y-Z) exp(-k|Y-Z|) Ftilde(xi,Z) dZ,
    T2 F = -(epsilon |xi|/2) int exp(-k|Y-Z|) Ftilde(xi,Z) dZ.

The sign of the first imaginary prefactor depends on the Fourier convention and does not affect the bound. The first line is bounded by epsilon|xi|/2 times the Z L1 norm. Since oddness gives int Ftilde dZ=0, subtract exp(-k|Y|) in the second line and use its Lipschitz bound k|Z|. The resulting bound is epsilon^2 xi^2/2 times int |Z Ftilde|dZ. Integrating in xi proves sup|U1 p|<=C_F |M|epsilon and sup|U2 p|<=C_F |M|epsilon^2. These constants are finite for each Schwartz F. They are not uniform over shapes with arbitrarily large horizontal oscillation: a fixed-envelope family modulated with horizontal frequency 1/epsilon has both multiplier components of order one near its Fourier support. This is a statement about a varying family F_epsilon, not an exception for one fixed F.

For the transport construction with h=r^3, q=4/A, the actual density and vertical velocity amplitudes are r^(15-q), while the horizontal correction is r^(13-q). It already fails the curl law. A proposed extension of isolated-packet suppression to all interacting scales requires additional estimates and remains heuristic.

Finally H5 is comparable to r^(-q). The extra estimate |d_y^5 f(-r,0)|<=C r^(alpha-3) gives G5/H5=O(r^(alpha-3+q)); it implies the vanishing endpoint only for alpha>3-q. At equality it gives boundedness only. Subtracting the quadratic Taylor polynomial does not change a fifth derivative, and scaling shows the stated estimate is equivalent to a uniform fifth derivative bound on (f-T2 f)(rX)/r^(2+alpha) at (-1,0). In the transport examples the derivative is exactly -120r^(-q), so the bound fails precisely when alpha>3-q. All implications are conditional on the displayed extra estimate.
