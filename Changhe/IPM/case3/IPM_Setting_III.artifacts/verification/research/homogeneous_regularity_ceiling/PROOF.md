# The sharp regularity ceiling for noninteger frozen homogeneous modes

Date: 2026-10-20. Status: independent reconstruction of the lead's fived1 argument, with a different proof of the regularity obstruction using a test function with vanishing moments. This is a theorem about a frozen linear equation. It neither constructs a nonlinear IPM profile nor excludes all smooth profiles. The separate algebra and manufactured checks are in verification/.

## 1. Exact statement and inverse domain

Fix A>1, B=A-1 and a nonzero real a. On the whole plane, in the sense of distributions, consider

    (A x partial_x+y partial_y-1)h+a partial_x psi=0,
    -Delta psi=partial_x h.                                  (1)

The density h is homogeneous of a noninteger degree d>1, even in x and odd in y. The stream psi is homogeneous of degree d+1 and odd in both variables. Both are tempered distributions and smooth off the axes. The distributional requirement excludes unrecorded sources on either axis. Homogeneous functions or distributions of these degrees are not sublinear full-plane profile candidates.

Any two such streams for the same h differ by an entire harmonic tempered distribution. Its Fourier transform is supported at zero, so it is a polynomial. Since a nonzero polynomial cannot have noninteger degree d+1, the stream is unique. This is the homogeneous local inverse. It is not an adjustable harmonic strain or an invocation of the primary inverse on a superlinear input.

Set

    kappa_x=(A d-1)/B, p_y=(a-d+1)/B,
    u=(d-A)/B, v=(a+2-A(d+1))/B.                              (2)

For s=m+alpha, m a nonnegative integer and 0<alpha<1, regularity C^s means C^(m,alpha) on a neighborhood of the origin, including both axes. A nonzero solution cannot have that regularity if

    s>min(d,p_y).                                             (3)

If p_y<=0 there is no continuous representative on a neighborhood of the origin.

For a>B, the supremum of the positive noninteger regularities attained by some nonzero noninteger homogeneous solution is

    S=(a+1)/A.                                                (4)

No assertion of membership at s=S is made. More generally, for 0<a<=B that supremum is a/B. For a<0 no such solution is continuous. All existence assertions here concern (1), a linear equation, with the homogeneous inverse just specified.

## 2. Radial regularity obstruction

Suppose h is C^s near zero. Homogeneity extends this regularity to a neighborhood of every point of the plane. If h is nonzero as a distribution, it is now a nonzero function and some ray has h(t omega)=c t^d with c nonzero and t>0. Taylor expansion at zero with a C^s remainder cannot have this form when s>d and d is noninteger. Indeed, a first nonzero Taylor coefficient would have integer degree; comparing powers makes all coefficients through degree floor(d) zero, and the remaining O(t^s) estimate contradicts c t^d. The same argument applies if further derivatives are assumed. Thus s<=d is necessary. It remains to obtain the independent bound p_y at the vertical axis.

## 3. The one-dimensional odd homogeneous distribution

Use Fourier transform F[f](xi)=integral exp(-i x xi)f(x)dx and inverse factor 1/(2 pi). Define

    G_v(t)=sgn(t)|t|^v / Gamma((v+2)/2)                        (5)

by continuation as a tempered distribution. Here is the construction and the exceptional case. For Re v>-2, pairing its numerator with a test function is

    integral_0^infinity t^v[phi(t)-phi(-t)]dt.

At zero subtract finitely many odd Taylor terms of phi, using a cutoff equal to one there, and integrate each removed power explicitly. This continues the numerator meromorphically; its only poles are v=-2n-2, n=0,1,.... The reciprocal Gamma factor cancels every pole. The residues give

    G_(-2n-2)=(-1)^(n+1)n!/(2n+1)! delta^(2n+1).             (6)

The family is therefore nonzero at every real v. Away from these exceptional degrees it has a nonzero off-zero signed power. It is odd and satisfies t G_v'=v G_v, including at the exceptional values by continuation.

Every odd distribution satisfying tT'=vT is a scalar multiple of G_v. Away from zero, the scalar differential equation gives the signed power. A supported distribution is a finite sum of delta derivatives, and only delta^n has degree -n-1. For an odd supported distribution n must be odd. Thus uniqueness holds at nonexceptional v. At v=-m-1 with m positive and odd, test the Euler equation against t^m chi(t), where chi is even, compactly supported and one near zero. It requires

    <T,t^(m+1)chi'(t)>=0.

An off-zero signed-power coefficient c would instead give 2c integral_0^infinity chi'(t)dt=-2c. Every supported distribution pairs to zero with this test. Hence c=0 and only a multiple of delta^m remains, exactly as in (6).

On the open set y!=0, the inverse Fourier transform is

    F^(-1)G_v(y)= i 2^v/[sqrt(pi) Gamma((1-v)/2)]
                         sgn(y)|y|^(-v-1).                  (7)

To verify its constant, first take -1<v<0, insert exp(-epsilon t) in the sine integral, and pass to the limit. The coefficient is

    i Gamma(v+1)sin(pi(v+1)/2)/[pi Gamma((v+2)/2)],

which equals that in (7) by the Gamma duplication and reflection identities. Both sides, tested away from y=0, continue analytically in v: the construction above controls the origin and the Schwartz test controls infinity. This proves (7) at every real v. In particular the coefficient is nonzero for v<-1. Its only zeros are v=1,3,5,..., where G_v is a polynomial whose inverse transform is supported at zero. At v=-2n-2 it is a nonzero odd polynomial, consistent with (6).

## 4. Fourier classification, including axis-supported terms

Write F=hat h and use frequency coordinates (xi,eta). Fourier transformation of (1) away from the frequency origin gives

    [A xi partial_xi+eta partial_eta+A+2
                           +a xi^2/(xi^2+eta^2)]F=0.         (8)

Also F is homogeneous of degree -d-2. On xi>0 put q=eta/xi and F=xi^(-d-2)f(q). Defining g(q)=(1+q^2)^(a/(2B))f(q) reduces (8) to qg'=v g. The oddness in eta and Section 3 classify this equation even when it is supported on eta=0. Evenness in xi then gives

    F=C |xi|^(u-a/B)(1+eta^2/xi^2)^(-a/(2B))G_v(eta),
                                                        xi!=0. (9)

The exponent identities are

    u+v-a/B=-d-2,  p_y=d+v+1,  u-a/B=-1-p_y.                (10)

No missing nonzero solution is supported on xi=0. To see this, restrict first to eta!=0. Homogeneity allows us to check compact segments with |eta| bounded above and below, where a supported distribution has finite transverse order. Write its highest order as delta^(n)(xi)T(eta). Homogeneity forces T to have degree n-d-1. The coefficient of this highest order in (8) is

    -A(n+1)+(n-d-1)+(A+2)=1-d-B n,

which is nonzero for d>1 and n>=0. The xi^2/(xi^2+eta^2) term only lowers transverse order and cannot cancel it. Repeating the argument eliminates the supported distribution. The remaining possibility of support at the frequency origin would give a polynomial h, incompatible with its noninteger degree. Thus C is nonzero for a nonzero solution.

This step cannot be replaced by a quadrant-only formula: the values v=-2,-4,... give nonzero solutions supported on eta=0 in frequency space, and they affect the physical axis regularity.

## 5. Vertical-axis obstruction by vanishing-moment testing

Assume p=p_y<d. Then (10) gives v<-1, so (7) has a nonzero coefficient. Choose a smooth real phi, supported in (1,2), with nonzero pairing against F^(-1)G_v, and define the tempered distribution

    H(x)=integral h(x,y)phi(y)dy.

If h were C^s near the origin, homogeneity would give that regularity on a neighborhood of {0}x[1,2], hence H would be C^s near x=0. In this case H is a function of at most polynomial growth, since the continuous angular trace of h is bounded and |h(X)|<=C|X|^d.

Partial Fourier transformation of (9) gives, for |xi| tending to infinity,

    hat H(xi)=c_phi |xi|^(-1-p)+O_sym(|xi|^(-3-p)),
    c_phi!=0.                                             (11)

Here every fixed number of xi derivatives satisfies the corresponding differentiated bound. To prove it, pair (9) with hat phi(-eta)/(2pi). On |eta|<|xi|/2, Taylor expansion of (1+eta^2/xi^2)^(-a/(2B)) has leading term 1 and remainder xi^(-2) times a smooth multiplier bounded with all derivatives by a polynomial in eta. Pairing with the finite-order tempered distribution G_v and the Schwartz function hat phi gives the stated error. On the complementary region the Schwartz decay makes the pairing smaller than any prescribed power of |xi|, after any fixed number of derivatives. This proof also applies when G_v is a delta derivative. The leading coefficient is nonzero by our choice of phi and (7).

Choose a real even Schwartz function zeta whose Fourier transform is smooth, nonnegative, nonzero, and supported where 1<|xi|<2. Such a function is the inverse Fourier transform of any nonnegative even smooth bump on that annulus. All its moments vanish, because every derivative of its Fourier transform is zero at xi=0. Put

    I_epsilon=<H,epsilon^(-1)zeta(x/epsilon)>.

Using Fourier duality and (11), followed by xi=t/epsilon, gives

    I_epsilon=epsilon^p [c_phi J+O(epsilon^2)],
    J=(1/(2pi)) integral |t|^(-1-p)hat zeta(-t)dt >0.       (12)

If H is C^s near zero, subtract its degree-m Taylor polynomial in this pairing. All polynomial terms vanish by the moments of zeta. On |x|<delta, the remainder is O(|x|^s), so its contribution is O(epsilon^s). On |x|>=delta, polynomial growth of H and rapid decay of zeta give O(epsilon^N) for any chosen N; choose N>s. Thus I_epsilon=O(epsilon^s). Equation (12) contradicts this whenever s>p.

For mere continuity, subtract H(0) and use the zero integral of zeta. Dominated convergence on the rescaled integral, with the same rapidly decaying tail, yields I_epsilon=o(1). Equation (12) contradicts this when p<=0: it has a nonzero limit at p=0 and grows in magnitude when p<0. This proves both assertions in Section 1.

This argument handles even integer p and negative integer p without suppressing logarithmic or supported inverse transforms. It tests the leading high-frequency term directly and cannot confuse the exceptional positive odd v with a canceled singularity when p<d.

## 6. Attainability below the ceiling for the actual coupled equation

Let s>0 be noninteger. Choose a noninteger d>max(1,s) such that

    p_y>s, kappa_x>s,

and avoid integer p_y and kappa_x. We prove existence of a nonzero solution of (1) with h in C^s and psi in C^(s+1) locally on the whole plane. This extends the explicit C^(1,alpha), 1<d<2 construction in ../finite_regularity_and_concentration/PROOF.md; the homogeneous inverse here is defined by (1) and noninteger uniqueness, without using that proof's low-order subtraction formula for larger d.

On 0<theta<pi/2 set h=r^d Theta(theta), psi=r^(d+1)Phi(theta), c=cos theta, z=sin theta and q=A c^2+z^2. The coupled equations are

    (d q-1)Theta-B z c Theta'
                   +a[(d+1)c Phi-z Phi']=0,
    Phi''=z Theta'-d c Theta-(d+1)^2 Phi.                  (13)

They are an analytic three-dimensional first-order system in the open quadrant. At the horizontal axis t=theta, in Y=(Theta,Phi,Phi_t), the regular-singular residue is

    R_x=[[kappa_x,a(d+1)/B,0],[0,0,0],[0,0,0]].             (14)

At the vertical axis t=pi/2-theta, with the analogous Y, it is

    R_y=[[-(d-1)/B,0,-a/B],[0,0,0],[(d-1)/B,0,a/B]].       (15)

These rank-one matrices have eigenvalues 0,0,kappa_x and 0,0,p_y respectively and are diagonalizable. Their nonzero eigenvalues are positive nonintegers by the choices above.

For a regular-singular system tY'=(R+sum_(j>=1)R_j t^j)Y with these residues, every vector in ker R starts one analytic series. Its coefficients obey

    (jI-R)Y_j=sum_(l=1)^j R_l Y_(j-l), j>=1.

All these matrices are invertible. A nonzero eigenvector at exponent kappa likewise gives t^kappa times an analytic series, replacing j by j+kappa in the recurrence. For large j the inverse matrices have norm at most C/j, and the analytic coefficients R_j have a geometric bound. A larger geometric majorant bounds the recursively computed solution coefficients; finitely many small denominators only change its constant. Thus the series converge. This constructs three independent local solutions, rather than only listing formal exponents.

At the horizontal axis, analytic oddness of both Theta and Phi imposes Y_0=(0,0,z_0), a one-dimensional subspace of ker R_x. Uniqueness of the analytic series and reflection invariance of (13) give the required parity. The fractional branch has Theta=t^kappa_x times an analytic function with nonzero value at zero. The second equation of (13) gives Phi=O(t^(kappa_x+2)) and Phi_t=O(t^(kappa_x+1)). Oddly reflecting both functions gives density C^s and stream C^(s+1), since kappa_x>s. These two local branches give a two-dimensional admissible subspace at an interior angle.

At the vertical axis, analytic evenness of Theta and oddness of Phi require Phi(0)=0 and (d-1)Theta(0)+a Phi_t(0)=0, again a one-dimensional subspace. The fractional p_y eigenvector is (1,0,-1), so Theta is t^p_y times an analytic function, Phi_t is minus that leading term, and Phi=O(t^(p_y+1)). Evenly reflect the density and oddly reflect the stream. They have the required C^s and C^(s+1) regularities because p_y>s. This yields a second two-dimensional admissible subspace in the same three-dimensional interior solution space.

The two subspaces intersect nontrivially. Choose a nonzero intersection vector and reflect its solution across both axes. For s>0 the density is continuous and the stream is C^1; the distributional equations have no axis delta terms. Their higher stated Holder regularities follow from the strict endpoint-exponent inequalities. At the origin homogeneity and d>s give the same C^s density regularity and C^(s+1) stream regularity: derivatives through the relevant integer orders scale with the radial power; for a Holder difference, split point pairs into comparable-radius pairs and pairs separated by at least half the larger radius. The first uses the annular Holder estimate multiplied by a positive radial power; the second uses the derivative size bound. The point value and applicable Taylor derivatives vanish. No additional point-supported source can occur: the boundary terms on a circle of radius epsilon are bounded by positive powers of epsilon from d>1 and the homogeneous stream degree d+1>2.

If Theta were zero, (1) with a!=0 would force psi_x=0, and oddness in x would force psi=0. That contradicts our nonzero intersection vector. Thus h is nonzero, and uniqueness in Section 1 identifies the stream with the homogeneous inverse. This completes the construction for every d obeying the strict inequalities.

## 7. Optimization and exceptional cancellation

Since kappa_x-d=(d-1)/B>0, the upper constraint is min(d,p_y). If a>B, the increasing d and decreasing p_y cross at d=(a+1)/A>1, and

    sup_(d>1,d noninteger) min(d,p_y)=(a+1)/A.

For every positive noninteger s below this value the interval

    max(1,s)<d<a+1-Bs

is nonempty. Removing the discrete integer values of d,kappa_x,p_y still leaves choices, to which Section 6 applies. This proves sharpness as a supremum. For 0<a<=B the crossing is at or below1 and the same supremum is a/B, approached as d decreases to1. The same construction gives every positive noninteger s<a/B. If a<0 then p_y<0 for every d>1 and the continuity obstruction already applies.

For v=1,3,5,... the coefficient in (7) vanishes away from zero, but then p_y=d+v+1>d. These cancellations affect neither (3) nor the supremum: the radial degree is already the smaller bound. No smooth-angular spectral exclusion is needed for the upper bound.

As a direct check of the exceptional negative-even frequency case, let p>0 be noninteger and set a=A p, d=p+1. Then

    h(x,y)=y|x|^p,
    psi(x,y)=-y x|x|^p/(p+1)                              (16)

solves (1) distributionally on the whole plane, is smooth off the vertical axis, and has p_y=p, v=-2. Its first equation follows from psi_x=-h; its second follows by differentiating x|x|^p twice. These identities hold distributionally with no delta, since x|x|^p is C^1 for p>0 and its first derivative is continuous. It is homogeneous of degree d and its density has exactly the predicted vertical-axis obstruction. Discarding the eta=0 supported Fourier family would miss these explicit solutions.

## 8. Nonlinear scope and dependencies

The proof independently checks the full mathematics of the lead's fived1/PROOF.md. Section 5 replaces the explicit inverse-power and logarithm argument by the vanishing-moment test (12). Section 6 supplies the higher-regularity endpoint construction that cannot be inferred solely from our earlier degree-(1,2) result33. It uses elementary Fourier distribution identities, a convergent regular-singular series, and finite-dimensional linear algebra. The numerical checks do not prove these analytic steps.

A nonlinear consequence requires a genuine expansion with coefficient extraction in angular C^s norms across both axes and a justified termwise local inverse. Under those explicit additional assumptions, the first noninteger degree's highest logarithmic coefficient satisfies (1): the linear density and strain give its frozen equation, and interactions with higher-degree terms occur at higher degree. If a>B and s>(a+1)/A, that coefficient must vanish by the theorem. Iteration requires local finiteness of the expansion. This does not exclude integer-degree logarithms, establish such an expansion, prove nonlinear smoothness, or produce a full-plane profile. A raywise fit or a numerical slope is insufficient for coefficient extraction. No claim here changes the primary endpoint UNRESOLVED.
