# Finite isolated velocity terms, nodal geometry and local flux

Status: independent proof and source audit of LIT209 and LIT210. All conclusions retain the hypotheses below. A separate stronger actual-tail argument is recorded in the team records; it makes the supported local nodal configuration impossible under the same smooth isolated-leading hypothesis. The local calculations here remain valid implications, not an existence construction.

## 1. Profile class and local data

Fix 2/5<c<1/2 and arbitrary finite omega. Put Jx=(-x2,x1,0), A=cI-omega J, X(x)=Ax, a=1-2c, b=2(1-c), p=(1-c)/c and q=b/a>6. Assume U in C^2(R^3;R^3), P in C^1(R^3), finite C, and

    div U=0, (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(y)|<=C(1+|y|)^(-p), |DU(y)|<=C(1+|y|)^(-p-1).

Use the actual tails V,W=curl V,P2 on D=R^3 minus {0}, and k=X.V, S=P2-|V|^2/2, Z=int_D{k=0}, V0=1_Z V, E0=supp(V0|S^2). A533/A539 give V in C^(1,alpha), P2 in C^(2,alpha) locally for every alpha<1. Previously proved identities used here are

    div V=0, V.W=0, grad k=X cross W-aV,
    DV X=-[(1-c)I+omega J]V, X.grad k=-ak,
    X.grad S=-bS, grad k cross grad S=0 on {W!=0},
    -Delta P2=tr((DV)^2).

On a connected open vortical set with k!=0, the scalar identity implies S=D_*|k|^q for a single finite constant D_*. On a full ball about V=W=0, the bound |S|<=C_*|V|^q implies V vanishes nearby, by the complete local pressure lemma A1006. Both the full ball and q>2 matter.

For Sections3-10 fix x0!=0, V(x0)=DV(x0)=0, and assume V is smooth nearby with a first nonzero Taylor term V_m of degree m>=2. Let E=X(x0)-perp, and assume V_m(y)!=0 for all nonzero y in E. Also assume the local nodal premise

    k=0 implies W=0 on a neighborhood of x0.    (Nloc)

No prescribed S value or pressure jet is added. Smooth V actually makes P2 smooth by its local Poisson equation, but the LIT210 proof below needs only the already established pressure regularity and A1006.

## 2. The support boundary selector and isolation

Here is an elementary result independent of Euler. Let v,v0 be continuous vector-valued functions on an open planar disk, with v0(x) in {0,v(x)}. Every point of boundary(supp v0) is a nonisolated zero of v. If v is nonzero on a connected disk, the continuous function lambda=(v0.v)/|v|^2 takes values in {0,1}, so is constant. Neither constant allows a support boundary. If v has an isolated zero at the center, use the same argument on the connected punctured disk. The zero choice makes v0 vanish on the full disk by continuity; the one choice puts the entire disk in its support. Both contradict a boundary point.

A984-A985 give continuous V0, and A1053 gives boundary E0 contained in

    T0={V=DV=S=P2=0 on S^2} intersect supp W.

Thus every boundary point is a nonisolated zero of the FULL V restricted to the sphere. No assumption on a differentiable boundary is involved.

If the isolated-leading hypothesis of Section1 holds at such a point, compactness of the transverse unit circle and Taylor's theorem give |V(x0+y)|>=d|y|^m on a small punctured transverse disk. Following the explicit X flow e^(tA) maps this disk diffeomorphically to an angular disk, because X(w).w=c>0 on S^2. Homogeneity multiplies V by an invertible scalar and rotation. Hence the angular V zero is isolated, a contradiction. If every T0 point satisfies this hypothesis, E0 has empty boundary and so is empty or all of S^2. Mere isolation of the angular V zero suffices for this particular argument.

## 3. Exact planar transport and the general leading velocity

Choose oriented orthonormal coordinates (t,s,z3) centered at x0 with e3=X(x0)/ell, ell=|X(x0)|. The degree m-1 homogeneity equation gives partial_3 V_m=0. Divergence then gives homogeneous planar polynomials psi of degree N=m+1 and chi of degree m such that

    V_m=(-psi_s,psi_t,chi),
    W_(m-1)=(chi_s,-chi_t,Delta psi).

The leading helicity equation reads grad psi.grad chi=chi Delta psi. There is no prior assumption that chi=0.

The exact triple product identity is

    grad k cross V=kW.

Indeed (X cross W) cross V=W(X.V)-X(W.V)=kW. Restrict to z3=0, put f=k|E and C=(V2,-V1). Its third component gives

    C.grad f=f div C, div C=W3.                (3.1)

At any f zero, Nloc gives W=0 and grad_E f=-a(V1,V2). All statements are exact on the plane.

## 4. Exclusion of a normal leading component and of a radial stream

Write psi=r^N g(theta), chi=r^m h(theta). Helicity becomes

    g'h'=h(Ng+g'').                             (4.1)

If h!=0 at an angle, the radial derivative m h makes grad chi nonzero there. At a zero of the nonzero trigonometric polynomial h, let j>=1 be its finite order. The lowest power in (4.1) first forces g'=0. Comparing the next coefficient gives (j-1)g''=Ng. Isolation of V_m makes g nonzero at this angle. Thus j=1 is impossible, and for j>=2

    Delta psi=N^2g+g''=[N^2+N/(j-1)]g!=0

on the unit circle. Consequently if chi is nonzero, W_(m-1) is nonzero in every transverse direction. Its positive norm minimum and smooth Taylor estimates make W nonzero on a small punctured transverse disk.

The local product chart (tau,y)->e^(tau A)(x0+y) extends this to a connected open punctured tube, using twisted homogeneity of W. Its complement is only the central X orbit. Nloc gives k!=0 on this connected tube, so it has a single constant S=D_*|k|^q. Continuity extends |S|<=C|V|^q across the central orbit and onto a full smaller ball. At x0, V=0 gives k=0 and Nloc gives W=0. A1006 forces V=0 nearby, contrary to its nonzero Taylor term. This proves chi=0 and V_m=R grad psi, R(t,s)=(-s,t), with grad psi nonzero off0.

If g is a nonzero constant, Delta psi=N^2g r^(N-2) is again nonzero on the punctured disk, and the same contradiction applies. Thus g is nonconstant. This argument never bounds constants on infinitely many vortical components: it has produced exactly one connected punctured tube before using the constant law.

## 5. The first possible scalar term

Because chi=0, k=X.V has no degree m term. Let H_N=r^N h_N(theta) be its degree N term on E, allowing H_N=0. Smoothness gives, with the corresponding angular derivative estimates,

    f=H_N+O(r^(N+1)), C=grad psi+O(r^N),
    div C=Delta psi+O(r^(N-1)).

The degree 2N-2 part of (3.1) yields g'h_N'=g''h_N. On any interval where g'!=0, h_N/g' is constant. Trigonometric polynomials are real analytic, so equality on that interval implies the same identity on the whole circle. Thus for one real D, possibly zero,

    H_N=D r^N g'.                              (5.1)

The nonzero scalar order will be proved, not assumed.

## 6. The radial invariant curve

Choose theta0 where |g| has a positive maximum, and put g0=g(theta0)!=0. Then g'=0 and g''/g0<=0 at theta0. Divide the polar equations of C by r^(N-2). They become

    dot r=r[Ng(theta)+O(r)], dot theta=g'(theta)+O(r).

Near theta0 the first coefficient is nonzero. With z=theta-theta0, division gives

    r z'=sigma z+z^2 G(z)+r H(r,z),
    sigma=g''(theta0)/(Ng0)<=0,

where G,H are smooth and bounded. In the Banach space of continuous z with z(0)=0 and norm sup|z(r)|/r, use

    Tz(r)=r^sigma integral_0^r
       [s^(-sigma-1) z(s)^2 G(z(s))+s^(-sigma)H(s,z(s))] ds.

For |z|<=Lr the constant H part is bounded by ||H||r/(1-sigma), while the quadratic part is O(L^2 r^2). A sufficiently large fixed L and small r0 make this a self map. Differences of the quadratic term and of H give norm at most C r0 times the input norm. This is a contraction after another shrink. Its fixed point solves the equation for r>0 and has z=O(r). Negative g0 only reverses time orientation. No complete C flow is assumed.

Along this curve, (5.1) gives f=O(r^(N+1)). Equation(3.1) divided by the radial component gives

    r df/dr=[nu+O(r)]f,
    nu=N+g''(theta0)/(Ng0)<=N.

A nonzero solution has f=C r^nu exp(O(r)), with C!=0; the integrable O(r)/r error justifies its finite nonzero coefficient. Such a solution cannot be O(r^(N+1)). Thus f vanishes identically on the curve. Nloc makes W vanish there, and its leading third component yields

    g''(theta0)=-N^2 g0.                        (6.1)

## 7. The equality case forces a harmonic stream

The restriction of psi to the circle is a trigonometric polynomial of degree at most N. For any such real T, finite Fourier orthogonality gives

    T''(0)=sum_(j=0)^(2N-1) w_j T(pi j/N),
    w_0=-(2N^2+1)/6,
    w_j=-(-1)^j/[2 sin^2(pi j/(2N))], j>0,
    sum |w_j|=N^2.                             (7.1)

For completeness, the interpolation kernel is K(theta)=1+2sum_(k=1)^(N-1)cos(k theta)+cos(Ntheta)=sin(Ntheta)cot(theta/2), with removable values filled continuously. The weights are K''(-pi j/N)/(2N). Discrete orthogonality selects the second derivative of every frequency |k|<N; the two highest cosine coefficients add, while the highest sine has zero samples and second derivative at0. Applying the formula to cos(Ntheta) gives the absolute-weight sum. This proves |T''|<=N^2||T||_infinity exactly.

Translate theta0 to zero and change sign if necessary so g0=M>0. Equation(6.1) is equality with negative sign in (7.1). All weights are nonzero, so every sample must equal M(-1)^j. The only sample-null mode is sin(Ntheta), hence g=M cos(Ntheta)+B sin(Ntheta). Its supremum norm is sqrt(M^2+B^2); the known maximum M forces B=0. Undoing the shift and sign proves

    psi=r^N M cos(N(theta-theta0)), M!=0,
    Delta psi=0.                               (7.2)

No trigonometric inequality is left as an unverified citation or numerical observation.

## 8. Scalar normalization and exact nodal curves

On the constructed curve f=0, the exact gradient identity gives partial_theta f=-a r V_T.e_theta. Since R grad psi has angular component N g r^(N-1),

    partial_theta f=-a N g0 r^N+O(r^(N+1)).

On the other hand (5.1) and (6.1) give partial_theta f=-D N^2g0 r^N+O(r^(N+1)). Thus D=a/N and

    k_N=(a/N)r^N g'.                            (8.1)

This is nonzero and has exactly2N simple angular zeros. The uniform estimates f/r^N=h(theta)+O(r), partial_theta f/r^N=h'(theta)+O(r), h=(a/N)g', show that for each small r there is exactly one zero on each of2N disjoint arcs and no others. Monotonicity on those arcs gives uniqueness; the implicit function theorem makes them smooth graphs theta_j(r) for r>0. These are connected nodal curves, not only a count on each circle.

## 9. Vorticity estimate and flux integral

Harmonicity cancels the whole degree m-1 term of W, so smooth Taylor estimates give |W|+|partial_theta W|<=C r^m on E. Since Nloc gives W(r,theta_j(r))=0, on each nodal arc

    |W|<=C r^m |theta-theta_j(r)|,
    |f|>=d r^N |theta-theta_j(r)|, d>0.

Split a small disk at r_*=C_* tau^(1/N). The inner contribution is bounded by C r_*^(m+2)=C tau^(1+1/N). For outer radii, the f sublevel is confined to the chosen arcs, with angular width at most C tau/r^N. Its contribution is at most

    C tau^2 integral_(r_*)^r0 r^(m+1-2N) dr
      =C tau^2 integral_(r_*)^r0 r^(-N) dr
      <=C tau^(1+1/N),                          (9.1)

since N=m+1>=3. Therefore the local integral of |W| on {|f|<tau} is O(tau^(1+1/N)).

The explicit X flow maps this disk to a sphere patch with bounded Jacobian and inverse Jacobian. It multiplies k and |W| by positive bounded factors. The sphere sublevel therefore pulls back into a disk sublevel at threshold C tau, proving the same order on the sphere. Adding an S sublevel can only decrease the integral. All constants are local, finite and independent of small tau.

## 10. Conditional global nodal conclusion

Assume the global premise N: k=0 implies W=0 on D, and the smooth finite isolated-leading hypothesis at every T0 point. If U!=0, the confirmed actual partial-flow theorem A1055-A1057 gives positive constants c0,c1,c2 with

    J(tau)=integral_{S^2, |k|<c1 tau, |S|<c2 tau^q}|W|dA>=c0 tau.

This theorem uses a complete original vorticity flow only up to each partial scattering-flow arrival, never a continuation of the tail flow through0. Its full derivation and the localization were reread in the team records Sections7-8.

Section9 makes every T0 patch contribute o(tau). Off vorticity support the contribution is zero. A nonzero scalar excludes the sublevel locally. At a joint zero, N gives W=0. If V!=0, grad k=-aV gives regular angular coordinates and the Holder nodal bound O(tau^(1+alpha)). If V=0,DV!=0, the confirmed C1 saddle coordinates A832 give O(tau^(1+alpha/2)). Every remaining supported joint zero belongs to T0. Compactness supplies a finite cover, so J=o(tau), a contradiction. This proves U=0 with N and the extra tail hypothesis.

## 11. Source comparison and exact limitations

All four LIT209 and all twelve LIT210 sections were read. The selector, normal-component argument, radial contraction, exact Fourier equality, normalization and integration have been independently reconstructed above. No computation or formal build was needed. No original-profile analyticity, second derivative of Xi, local vorticity density or a priori finite component count was introduced.

The separate completed coordinator the external referee (a second model) derivation gives a stronger result under these smooth finite isolated-leading assumptions: a supported T0 point has a full k-zero neighborhood. It is separately audited, and is not a model review; its requested model invocation failed credentials. A focused comparison by an existing configured model agent remains pending. The local flux calculation here does not assert that its center exists in the actual N class.

The unrestricted campaign is open. Neither finite order, the isolated leading polynomial, smoothness of the tail, global helicity nor the natural derivative estimate follows here from bare velocity decay. Degenerate leading directions and infinite flatness are not covered.
