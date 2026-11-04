# Periods and infinitely many vortical components for a nowhere-zero scalar

Status: independently CONFIRMED at A665-A669 after complete source and proof postreads. This audits Theory Agent C C42 and strengthens its period conclusion. The unrestricted Euler conjecture and the infinite-component case remain open.

## 1. Exact statements and notation

Let D be R3 minus the origin, 1/3<c<1/2, a=1-2c, p=(1-c)/c in(1,2), lambda=a/c=p-1, A=cI-omega J, and Q_t=exp(omega t J), where Jx=(-x2,x1,0) and omega is any finite real number. Suppose V is C1 on D and

    div V=0, V.curl V=0,
    V(exp(tA)x)=exp(-(1-c)t) Q_t transpose V(x).             (1)

Write W=curl V, k=(Ax).V and E=grad k. Boundaries are relative to D. A period means the integral of V.dx/k around a piecewise C1 loop in {k!=0}.

The following statements hold under(1).

(a) The form V.dx/k is closed. No component C of {k!=0} admits a potential Gamma with grad Gamma=cV/k which tends to positive infinity at every boundary point of C. In particular k cannot be nowhere zero on D.

(b) If every boundary point of C has an open neighborhood on which W=0, C has a nonzero period. Its sphere section is not simply connected.

For the remaining statements assume 2/5<c<1/2, V not identically zero, b0=2(1-c), eta=a/b0, and S in C1(D) nowhere zero, with

    S(exp(tA)x)=exp(-b0 t)S(x),
    W.grad S=0 on D,
    E cross grad S=0 on {W!=0}.                            (2)

The sign of S is not prescribed. Since D is connected, that sign is constant.

(c) There are a bounded orbit-invariant theta in C1(D) and an orbit-invariant h in C1(D) such that

    c grad theta=|S|^-eta (Ax cross W),
    h=k |S|^-eta/c.                                       (3)

On each connected component O of {W!=0}, h has a nonzero constant value g_O. A period has the absolutely convergent representation

    integral V.dx/k
      =(1/a) sum_O (1/g_O) integral_{loop^-1(O)} d theta.   (4)

Every component C of {k!=0} contains at least two distinct values g_O. If it contains only finitely many O, or more generally inf_{O subset C}|g_O|>0, it has a nonzero period.

(d) Nevertheless EVERY period under(1)-(2) is zero. Consequently each component C of {k!=0} contains infinitely many vortical components with infinitely many distinct g_O and

    inf_{O subset C}|g_O|=0.                              (5)

A sequence from those components can be selected on the unit sphere which converges to a point of the boundary of C where V=W=k=E=0. In particular a finite-component or uniformly separated-constant example satisfying(1)-(2) is impossible. Claim(c)'s conditional nonzero-period conclusion and(d)'s zero-period conclusion are compatible because the former premises cannot occur.

No pressure equation is assumed anywhere. For the established natural tails of globally zero-helicity C2 Euler profiles, these results apply whenever the actual scalar S=P2-|V|^2/2 is nowhere zero. Such profiles still require their stated natural velocity and derivative bounds; bare velocity decay does not supply them.

## 2. Homogeneity and the sphere section

Differentiating(1) gives DV(Ax)=-(1-c)V-omega JV. Therefore

    E=A transpose V+DV transpose Ax,
    Ax cross W=E+aV,
    k(exp(tA)x)=exp(-at)k(x).                              (6)

The vector triple product and V.W=0 give E cross V=kW, hence curl(V/k)=0 where k!=0. The identity holds classically since V and k are C1 there.

Every scaling orbit stays within its component C of {k!=0}. If r=|x|, it meets the unit sphere at pi(x)=r^-1 Q_(log(r)/c)x. Thus x maps to(pi(x),log r), a homeomorphism C to U_C times R, where U_C=C intersect S2 is connected. Also |V(x)|<=M r^-p globally on D.

## 3. The divergent-potential obstruction

Suppose Gamma as in(a) exists. Along a scaling orbit its derivative is c, so

    Gamma(x)=Gamma(pi(x))+log r.

Its restriction to U_C attains a finite minimum m. Indeed any sequence in the compact sphere has a convergent subsequence; a boundary limit is excluded for a bounded-above minimizing sequence by the boundary divergence. If U_C is the whole sphere, compactness alone suffices. Thus Gamma>=m+log r.

Fix gamma>m and a smooth nondecreasing chi which is zero below1 and one above2. For epsilon>0 the set {Gamma<=gamma,r>=epsilon} is compact in C: r<=exp(gamma-m), and a boundary limit would force Gamma to diverge. Consequently zeta=(gamma-Gamma)_+ chi(r/epsilon), extended by zero, is an admissible compactly supported Lipschitz test for div V=0. It gives

    integral_{C,Gamma<gamma} chi(r/epsilon)c|V|^2/k
      =integral (gamma-Gamma)_+ V.grad chi(r/epsilon).       (7)

The right side is O(epsilon^(2-p)(1+|log epsilon|)): its shell has volume O(epsilon^3), the derivative of the cutoff is O(epsilon^-1), velocity is O(epsilon^-p), and the positive part is at most gamma-m+log(1/epsilon). It tends to zero because p<2.

The left side has one sign and its absolute value is bounded below by a positive constant for all small epsilon. Choose a compact ball in the nonempty open set {Gamma<gamma}. There k has one sign and V is nonzero, and chi is eventually one. This proves the contradiction without assuming a finite limiting integral. If k were nowhere zero on D, the closed form would have a potential on the simply connected D and the boundary condition would be vacuous. This proves(a).

## 4. Analytic boundary neighborhoods

If all periods on C vanish, path integration gives Gamma with grad Gamma=cV/k. Set

    Theta=lambda Gamma+log|k|,
    grad Theta=(Ax cross W)/k.                            (8)

Fix x0 in the boundary of C and an open ball B about it on which W=0. Equation(6) gives E=-aV, so k is C2 and harmonic on B. It is therefore real analytic. The semianalytic set {k!=0} intersect B has a locally finite family of connected components. A smaller neighborhood of x0 meets only finitely many of them. Each such component meeting C lies entirely in C, and Theta is constant on it because W=0. Thus Theta takes only finitely many values close to x0 within C. Since k tends to zero there, Gamma=(Theta-log|k|)/lambda tends to positive infinity, contradicting Section3.

The local-finiteness input is imported from Edward Bierstone and Pierre D. Milman, Semianalytic and subanalytic sets, Publications mathematiques de l'IHES67(1988),5-42, Corollary2.7(2), printed13. The actual primary PDF, its definition context and the complete corollary proof were read. That proof gives a neighborhood where a semianalytic set is a finite union of connected sign sets, using Theorem2.6. We do not claim to reprove all of semianalytic geometry. The retained PDF includes its copyright notice. The sphere-section conclusion follows from the product description in Section2 and the usual path-integral criterion for an exact closed form.

## 5. The zero-free localization input at the required regularity

We recall and recheck the zero-free case of A568. No Holder derivative assumption is needed here. Since Ax.grad S=-b0 S never vanishes, rank in(2) gives

    grad(k|S|^-eta)=0 on {W!=0}.                          (9)

If k vanishes at one point in a vortical component O, it vanishes throughout O by(9); hence E=0 and aV=Ax cross W there. At each boundary point of O, W=0 by continuity, and then V=0 by the preceding identity. Extend V and W by zero off O, denoting the extensions by Y and Z. The segment-to-boundary argument makes Y locally Lipschitz. Its distributional divergence is zero and curl Y=Z, with no boundary measure: derivatives vanish almost everywhere on the zero set of the Lipschitz extension. Both extensions keep their scaling covariance, and

    Ax cross Z=aY, Z.grad S=0.

Let f=|S|^-eta. It is C1 and positive. The triple product gives grad S cross Y=(S/eta)Z, hence curl(fY)=0 distributionally. The continuous closed field fY is the gradient of a global C1 potential psi on D. Since Ax.Y=0, psi is orbit invariant, and therefore attains a global maximum on the compact unit sphere. It solves div(f^-1 grad psi)=0. On each compact ball this is a scalar uniformly elliptic divergence equation with a positive C1 coefficient, so the local strong maximum principle gives psi constant on connected D. Equivalently, the zero-free case of the already checked Harnack theorem in A568 gives this step. Thus Y=0, contradicting nonemptiness of O.

We have proved W!=0 implies k!=0 and(9). If E=0 and V!=0 at a point, (6) gives W!=0, while Ax.E=-ak gives k=0, another contradiction. Therefore E=0 implies V=0. These are exactly the F3 inputs used in the C42 referee request, for either sign of S.

## 6. The global theta and the period decomposition

The homogeneity and transport of S give

    grad S cross(aV+E)=b0 S W.

For f=|S|^-eta, grad f=-eta f grad S/S. Thus

    curl[f(aV+E)]=f(a-eta b0)W=0

in distributions. The product with grad k is justified by C1 approximation of k on compact balls; no second classical derivative is assumed. A continuous distributionally closed field has a C1 local potential, obtained by mollification on balls, and the potentials glue globally on simply connected D. Normalize this potential by c grad theta=f(aV+E). It is orthogonal to Ax, hence orbit invariant and bounded by its values on S2. Its gradient is zero wherever W=0.

Equation(9) makes h=fk/c constant, and nonzero, on every vortical component O. Those components are at most countable. On O,

    (Ax cross W)/k=grad theta/g_O,
    V/k=(1/a)((Ax cross W)/k-grad log|k|).

Integrate around a loop. The logarithm has zero integral; the other integrand vanishes on W=0, giving(4). Absolute convergence follows by summing the integrals of the absolute value over the disjoint preimages of O. Their sum is at most the integral of the absolute value of the continuous field (Ax cross W)/k along the compact loop. This also covers infinitely many interval components of each preimage.

## 7. The conditional nonzero periods in C42

If k were identically zero, Section5 would force V=0; thus some C exists. If all g_O in a particular C had the same value g0, use g0=1 when no O is present. Then

    Gamma=(theta/g0-log|k|)/lambda

has gradient cV/k throughout C, including W=0. Bounded theta makes it diverge positively at every boundary point, contradicting Section3. Hence at least two distinct constants occur.

Suppose C contains finitely many O_j and every period vanishes. By(8), on each O_j the quantity Theta-theta/g_(O_j) is constant. Bounded theta bounds Theta on their union and its closure F relative to C. This set is nonempty. Each component Q of C minus F has W=0, so Theta is constant there. Its boundary relative to C is nonempty and contained in F: otherwise Q would be a proper nonempty clopen subset of connected C. Continuity transfers the bound to Q. Hence Theta is bounded on C, giving the same forbidden divergence of Gamma. This proves the finite-component part of(c).

The proof works more generally if |g_O|>=delta>0. Under zero periods, Theta is orbit invariant by its definition in(8). The set

    {u in U_C:|h(u)|>=delta}

is compact in U_C. A sphere limit still has |h|>=delta, hence k!=0 and belongs to the same component C. Every O meets the sphere inside this compact set; continuity and orbit invariance bound Theta on their whole union. The preceding F,Q argument finishes the proof. No bound on the separate additive constants Theta-theta/g_O is presumed.

## 8. A global regularization makes every period zero

This is the additional independent deduction. On {W!=0}, grad h=0 by(9). On its complement, grad theta=0 by(3). Therefore

    grad h cross grad theta=0 EVERYWHERE on D.              (10)

Fix any loop ell in {k!=0}. Its compact image has |h|>=delta for some delta>0. Choose a smooth real function phi which equals1/s for |s|>=delta, with any smooth interpolation near zero. Then G=phi(h)grad theta is continuous globally on D and

    curl G=phi'(h) grad h cross grad theta=0

in distributions. To justify the product formula with theta only C1, approximate theta in C1 on compact balls and pass in distributions; h and phi(h) are C1. Simple connectivity again makes G exact on D. Hence

    0=integral_ell G.dx
      =integral_ell (grad theta/h).dx
      =integral_ell ((Ax cross W)/k).dx.

Together with the zero logarithmic period, this proves every period of V.dx/k is zero. The choice of phi depends on the loop, which is harmless: each chosen G is globally exact. No division by h is made near its zeros. No scalar-pressure equation is used.

Section7 now excludes inf|g_O|>0 for every C, yielding(5) and infinitely many distinct constants. Select O_n with |g_(O_n)| tending to zero and x_n in O_n intersect S2. After a subsequence x_n tends to x0 on the sphere, with h(x0)=0. Since x_n lies in C, x0 belongs to its boundary. Equation(9) and continuity give grad h(x0)=0. From h=fk/c with f>0, we get k(x0)=E(x0)=0. Section5 yields V(x0)=0, and W(x0)=0 because nonzero W would imply nonzero k. This proves(d).

## 9. What the regularization does not prove

The global exact regularizations do not bound the unregularized potential Theta near h=0. For example, take t_n=2^-n, h_n=4^-n and L=log4. On the lower half of each interval[t_(n+1),t_n], smoothly raise h from h_(n+1) to h_n with theta fixed. On the upper half keep h=h_n and raise theta by L h_n. Choose fixed smooth transitions flat at their endpoints; set h(0)=theta(0)=0. The increments and derivatives are O(4^-n) and O(2^-n), respectively, so h,theta are C1 at zero with zero derivative. Everywhere h' theta'=0.

The primitive Theta'=theta'/h normalized by Theta(1)=0 has Theta(t_n)=-nL=log h(t_n). During each lower half Theta-log h falls from0 to-L, and during each upper half it returns to0. Thus -L<=Theta-log h<=0, although theta is bounded and every one-dimensional period vanishes. This checks the C42 referee's obstruction to inferring the logarithmic barrier from the potential identities alone. It is not a vector-field or Euler counterexample. The unrestricted infinite-component alternative remains open.

## 10. The azimuthal example and its precise exclusion

For omega!=0 and nonzero smooth phi on[-1,1], let F(x)=r^(-p-1)phi(x3/r), V=FJx. It is C1 on D, divergence free and helicity free. Its covariance is(1). Directly k=-omega F|Jx|^2. On a rotational circle through any point with k!=0,

    integral V.dx/k=-2pi/omega.

It is therefore a valid example for the kinematic assumptions(1), confirming C42's calculation. By Section8 it admits NO nowhere-zero scalar S satisfying(2), of either sign, for2/5<c<1/2. This settles the source's stated uncertainty at exactly that scope, without any pressure assumption. At omega=0 the example has k identically zero and Section5 yields the same exclusion of a nowhere-zero S. Scalars with zeros are outside this conclusion.

## 11. Verification and collaboration

The full C42 source and full independent referee proof were read, and all arguments above were reconstructed. The zero-free A568 dependency was reread and reduced in Section5 to its ordinary elliptic maximum principle. The primary Bierstone-Milman PDF was successfully retrieved and the relevant corollary and proof read here, despite the inner referee's failed retrieval. The inner referee's failed Bedrock credential attempt did not invoke model and is not counted as a model response. Existing configured-model Theory Agent C and coordinator agents are the continuing comparison channel; their configuration is the primary model, with provider runtime not independently attested. The new Section8 deduction was posted for their focused challenge.
