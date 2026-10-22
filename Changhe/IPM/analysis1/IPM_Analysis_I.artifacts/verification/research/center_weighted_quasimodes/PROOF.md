# No same-norm inverse estimate in the diagnostic weighted H1 space

This is a new analytic argument awaiting independent review. It is not a statement about existence or nonexistence of an IPM profile. All numerical applications and the final verdict are OPEN until the stated checks and reviews are complete.

## Precise statement

Let 0<k<1/2, L>0, ell=1/k and c=3ell-1. Let rho be a fixed even-x, odd-y background with its canonical velocity U. Assume the following facts for this actual background:

1. Near0, rho=x^2 y+O(r^5), |grad rho|<=C r^2 and |D2 rho|<=C r. It is sufficiently smooth locally for the displayed derivatives and products below; C^{4,alpha}_loc for some alpha>0 suffices.
2. U is C2 near0, U(0)=0, and DU(0)=diag(-c,c). Thus V=ell X+U=A X+O(r^2), DV=A+O(r), where A=diag(alpha,beta), alpha=1-2ell and beta=4ell-1. The letter alpha in A is an eigenvalue, not the Holder exponent.
3. At infinity, |rho|+r|grad rho|+r^2|D2 rho|<=C r^k. The canonical operator on smooth compact perturbations has -Delta psi[h]=partial_x h and U[h]=(-partial_y psi[h],partial_x psi[h]), with the unique sublinear velocity of the required parity.

Set D=X dot grad, Sigma(h)=partial_xy psi[h](0)=-partial_x U[h]_1(0), and

    L_rho h=V dot grad h-h+U[h] dot grad rho+(Sigma(h)/3) D rho.

The diagnostic weighted weak H1 norm is

    ||f||_X^2=integral_R2 (f^2+r^2|grad f|^2) w(r) dX,
    w(r)=L^6 r^-6 (1+r^2/L^2)^(3/2-k).

Then there is a sequence h_j of smooth compactly supported real densities, even in x and odd in y, vanishing on a neighborhood of0, satisfying

    Sigma(h_j)=0, J(h_j)=0, ||h_j||_X=1,
    ||L_rho h_j||_X ->0.                                  (1)

Here J is the center factor value in h=x^2 y b. Each h_j has a smooth even-even factor b globally, so this trace is literal. These perturbations also have zero leading far coefficient because they are compactly supported. Consequently no finite C can satisfy ||h||_X<=C||L_rho h||_X on any linear perturbation domain containing this sequence. In particular this rules out that estimate on the broad graph domain of modal_graph_scaling and on its J=Sigma=0 subdomain. It also rules it out on a zero-leading-tail subdomain if that subdomain contains these compact perturbations. It does not rule out an estimate with different domain or forcing norms, or a domain that excludes this sequence.

For the distinguished exactly normalized modal trial, all three background hypotheses are supplied by modal_graph_scaling and its supplements, the canonical modal definition and its regularity proofs. The application must recheck those inherited pins and the exact scalar relation before acceptance. No retained numerical matrix is used.

## A critical homogeneous solution of the center transport

Let

    q=(4ell-1)/(6ell-2), p=(8ell-3)/(6ell-2).

Since ell>2, one has p+q=2, alpha p+beta q=1, 1<p<3/2 and1/2<q<1. Away from the axes the degree-two function

    H(x,y)=|x|^p sign(y)|y|^q

therefore solves (A X dot grad-1)H=0. Its angular factor is

    F(theta)=|cos theta|^p sign(sin theta)|sin theta|^q.

Put a(theta)=alpha cos^2 theta+beta sin^2 theta and b(theta)=(beta-alpha)sin theta cos theta. The angular transport operator on degree-two functions is

    T F=b F'+(2a-1)F.

Direct differentiation on each quadrant proves T F=0. The two endpoint powers p,q exceed1/2, so F belongs to H1 of the circle. This H1 fact is essential; no H2 membership is claimed.

Choose a smooth real cutoff chi on[0,infinity), zero on[0,1] and one on[4,infinity). For epsilon>0 put

    chi_e(theta)=chi(sin^2 theta/epsilon^2) chi(cos^2 theta/epsilon^2),
    F_e=chi_e F.

For sufficiently small epsilon, F_e is smooth on the circle, has the required reflections, and vanishes in neighborhoods of all axes. It converges to F in H1. Moreover

    G_e=T F_e=b chi_e' F ->0 in H1.                       (2)

To check both assertions, take the angular distance s from any axis. The local exponent nu is p or q, and |F^{(j)}|<=C s^{nu-j} for j=0,1 on each side. On a transition epsilon<=s<=C epsilon, the cutoff derivatives have sizes O(epsilon^-1) and O(epsilon^-2), while b=O(s) and b'=O(1). Thus G_e=O(epsilon^nu) and G_e'=O(epsilon^{nu-1}). Their squared integrals are O(epsilon^{2nu+1}) and O(epsilon^{2nu-1}), respectively, and tend to0. The same estimates for (1-chi_e)F and its derivative prove H1 convergence. Finite sums cover every axis. The limiting F is not zero.

## Long logarithmic annuli and the local transport bound

Fix 0<delta<1/4 so the center bounds hold on r<=delta, and set t0=log delta. Choose zeta smooth, zero on(-infinity,0] and one on[1,infinity), with0<=zeta<=1. For N>2-t0 define

    eta_N(t)=zeta(t+N) zeta(t0-t),
    f_(e,N)(r,theta)=r^2 eta_N(log r) F_e(theta).

This is a smooth compact density. It vanishes for r<=exp(-N) and r>=delta, and near each axis. It has a smooth global factor x^2 y b and J=0. All derivatives of eta_N of any fixed order are uniformly bounded in N; derivatives are supported on two intervals of bounded length. On the plateau -N+1<=t<=t0-1, eta_N=1.

For a degree-two angular function Z and a radial logarithmic factor eta, polar coordinates give exactly

    ||r^2 eta(t) Z(theta)||_X^2
      =L^6 integral (1+exp(2t)/L^2)^(3/2-k)
           [eta^2 Z^2+(2eta+eta')^2 Z^2+eta^2 (Z')^2] dt dtheta.       (3)

The radial factor in(3) lies between1 and a fixed positive constant on t<=t0. Put A(Z)^2=integral(5Z^2+(Z')^2) dtheta. The plateau gives

    ||f_(e,N)||_X >= L^3 sqrt(N+t0-2) A(F_e).              (4)

For the frozen local operator L0=A X dot grad-1,

    L0 f_(e,N)=r^2 eta_N G_e+r^2 eta_N' a F_e.

Using(3), uniform bounds on eta_N and its first two derivatives, and the bounded lengths of the transition intervals, one obtains constants C independent of e,N and C_e independent of N such that

    ||L0 f_(e,N)||_X <= C sqrt(N) A(G_e)+C_e.              (5)

Here C may depend on the fixed background, k,L,delta and zeta. Taking N large and then epsilon small in(4)-(5) will give an approximate kernel once the remaining terms are bounded independently of N.

## Uniform control of the actual background error

For fixed epsilon, differentiation of the displayed f_(e,N), including the cutoff intervals, gives uniformly in N

    |f_(e,N)|<=C_e r^2, |grad f_(e,N)|<=C_e r,
    |D2 f_(e,N)|<=C_e

on its support. Since V-A X=O(r^2) and D(V-A X)=O(r), the local error satisfies

    |(V-A X) dot grad f_(e,N)|<=C_e r^3,
    |grad[(V-A X) dot grad f_(e,N)]|<=C_e r^2.

Its squared X norm is therefore bounded by a constant times integral_0^delta r dr, independent of N. This uses the exact weight bound on the fixed disc and no passage of derivatives through an unqualified asymptotic expression.

## Uniform control of the canonical nonlocal term

For fixed epsilon the densities f_(e,N) have uniformly bounded H^{5/2}(R2) norms, despite the increasing logarithmic support length. Here is a direct proof. Use a smooth dyadic partition of unity on0<r<=delta. On a piece of radius R<=1, write the localized density as R^2 g(X/R). The function g is supported in a fixed annulus and has uniformly bounded derivatives through order3, independently of N and R; the bound may depend on epsilon. Thus ||g||_(H^{5/2})<=||g||_(H^3)<=C_e. Fourier scaling gives

    ||R^2 g(X/R)||_(H^{5/2})^2
       =R^6 integral (1+|xi|^2/R^2)^(5/2) |hat g(xi)|^2 dxi
       <= R ||g||_(H^{5/2})^2.

The triangle inequality and the convergent geometric sum of R^(1/2) prove the uniform bound. Only finitely many pieces are nonzero for any fixed N; their number does not enter this geometric estimate.

For smooth compact h, the Fourier multipliers of the canonical velocity are

    hat U[h]_1=(xi_x xi_y/|xi|^2) hat h,
    hat U[h]_2=-(xi_x^2/|xi|^2) hat h.

Their vector multiplier has norm at most1, so U is bounded on H^{5/2}. By Fourier Cauchy-Schwarz, the finiteness of

    integral_R2 (1+|xi|)^2(1+|xi|^2)^(-5/2) dxi

implies ||U[h]||_infinity+||DU[h]||_infinity<=C||h||_(H^{5/2}). It also gives continuous first derivatives. The velocity has the required reflection parities, hence U[h](0)=0, and so |U[h](X)|<=C_e r for r<=1. These Fourier velocities decay at infinity and satisfy the distributional Darcy identities; canonical uniqueness identifies them with the prescribed U[h].

The compact supports lie in a fixed disc and the L1 norms are uniformly bounded. Outside twice that disc, the differentiated logarithmic Green kernel gives |U[h](X)|<=C_e r^-2 and |DU[h](X)|<=C_e r^-3. A possible local distribution term in the order-zero multiplier vanishes outside the support. These far estimates also follow by differentiating the nonsingular kernel there; no singular integral estimate is being applied across its support.

Near0, the background derivative bounds now give

    |U[h] dot grad rho|<=C_e r^3,
    |grad(U[h] dot grad rho)|<=C_e r^2.

At infinity the corresponding orders are r^(k-3) and r^(k-4). On the intervening compact region, all factors and the weight are bounded. The near-center radial integral is integral r dr, and the far squared integral is bounded by a constant times integral r^-8 dr. Both are finite, uniformly in N. Consequently

    ||U[f_(e,N)] dot grad rho||_X<=C_e,
    |Sigma(f_(e,N))|<=C_e.                               (6)

Also D rho belongs to X by the stated center and far estimates. Thus the rank-one term has uniformly bounded X norm. Combining this with(5) and the local background error yields

    ||L_rho f_(e,N)||_X<=C sqrt(N) A(G_e)+C_e.             (7)

## Exact strain and center normalization

Choose a nonnegative nonzero smooth radial function chi0 supported in1<r<2 and let b0=x^2 y chi0(r). It is smooth, compact, has the required parities, vanishes near0 and has a smooth even-even factor. Its canonical strain is

    Sigma(b0)=(1/4) integral_0^infinity r chi0(r) dr>0.    (8)

For completeness, if h=F1(r)sin theta+F3(r)sin3theta, the sin2theta source coefficient in partial_x h is g2=(F1'-F1/r+F3'+3F3/r)/2. The canonical radial Green formula gives Sigma(h)=(1/2)integral g2/r dr. Compact support away from0 permits integration by parts: the F1 contribution vanishes and the F3 contribution is integral F3/r^2 dr. For b0, F1=F3=r^3 chi0/4, proving(8).

Set b=b0/Sigma(b0). The function b has J=0 and Sigma=1. Both b and L_rho b belong to X: local transport terms are compactly supported away from0, the velocity product has the same integrable bounds just proved, and D rho belongs to X. Define

    v_(e,N)=f_(e,N)-Sigma(f_(e,N)) b.

It has J=Sigma=0, the required parities, a smooth global factor, and compact support. By(4), (6) and(7),

    ||v_(e,N)||_X >= L^3 sqrt(N+t0-2) A(F_e)-C_e,
    ||L_rho v_(e,N)||_X <= C sqrt(N) A(G_e)+C_e.           (9)

All constants C_e are finite for fixed epsilon. Since A(F_e) tends to A(F)>0 and A(G_e) tends to0, choose a sequence epsilon_j ->0 and then integers N_j large enough that the ratio in(9) tends to0 and the denominator is positive. Dividing v_(epsilon_j,N_j) by its exact X norm proves(1).

## Consequence, dependencies and verification

If a finite same-norm inverse estimate held on a domain containing this sequence, substitution in(1) would give1<=C||L_rho h_j||_X ->0, a contradiction. This is failure of bounded below, not a claim of an exact kernel, a Fredholm index or a nonexistent nonlinear profile. It concerns the diagnostic weighted weak H1 norm; Hölder norms, higher Sobolev norms, derivative-loss estimates and finite-dimensional classes are not covered by this proof.

Before accepting the modal application, independently check the exact scalar identities, endpoint exponent inequalities, the angular transport identity, the weight/Jacobian powers, Fourier symbol signs and normalization functional. Recheck the accepted canonical trial, graph-domain and regularity source pins. Request actual Claude Opus5.5 adversarial review, resolve objections, and write a later independent adjudication. This argument and the scalar checks are analytic; neither a floating sample nor an unproved compactness assertion is used.
