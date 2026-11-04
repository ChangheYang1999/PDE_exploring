# One-signed angular contraction and the exact nodal flux

Status: independently proved at the hypotheses below. Ledger A677-A681. The unrestricted rotating-profile conjecture remains OPEN.

## 1. Statement and notation

Let D = R^3 minus {0}, 2/5 < c < 1/2, omega any real number, J(x1,x2,x3)=(-x2,x1,0), A=cI-omega J, p=(1-c)/c, lambda=p-1, mu=2-p, a=c lambda, t=omega/c, eta=lambda/(2p), q=1/eta. Suppose V is C1 on D, divergence free and helicity free, and

    V(exp(sA)x)=exp(-(1-c)s) exp(-omega s J)V(x).

Let P2 be C1, homogeneous under exp(sA) with exponent -2(1-c), and put W=curl V, k=(Ax).V, S=P2-|V|^2/2. Assume

    {k=0} is contained in {W=0},
    grad k cross grad S=0 on {W!=0}.

The first premise is explicit; in the project's A2 tail class it is A597. The pressure equation is not required until Section 7. For the derivative-vanishing conclusion assume additionally V in C^(1,alpha)_loc for at least one alpha>0. Actual tails under the previously confirmed natural estimates have this regularity for every alpha<1.

Use rho=log r, z=cos theta, w=1-z^2, chi=phi+t rho. On the unit sphere write

    V=r^(-p)(R e_r + H/sqrt(w) e_theta + F/sqrt(w) e_phi),
    P2=r^(-2p)u, S=r^(-2p)h, K=R-tF,
    V.dx=r^(-lambda)(K d rho+gamma),
    gamma=-(H/w)dz+F dchi, Z=partial_chi.

The expressions are smooth tensor expressions across the axis, interpreted in Cartesian charts there. Let M be the positive map from one-forms to vectors given by the spherical inverse metric plus t^2 Z tensor Z. Define Bq=M gamma+tKZ. The notation Bq distinguishes this compact angular field from the original three-dimensional carrier field.

Then:

1. If K has one sign, V=0 at its zero cone. With the stated Holder assumption, DV=0 there as well.
2. If K has one sign, h=0 on the boundary of {K=0} on S^2. Consequently S=P2=0 on those twisted rays. No uniform control of the constants on accumulating vortical components is assumed.
3. If S is nowhere zero and K has one sign, V=0. Hence every nonzero tail with nowhere-zero S has both signs of K.
4. On N={K=0,dK!=0}, the measure

       d nu = M(dK,dK)/(lambda |dK|) dH1

   has finite mass. It has no additional part at critical zeros. For every real C1 function psi on S^2,

       int_{K>0}(mu psi R-dpsi(Bq))=-int psi dnu,
       int_{K<0}(mu psi R-dpsi(Bq))=+int psi dnu.

   In particular

       int |K|+(2/mu)nu(S^2)=-t int sgn(K)F.

   A regular zero gives a strict unweighted flux inequality. One-signed K gives nu=0 and equality for every C1 weight.
5. For r0>1, the pressure weight |h|^r0 gives the same identity, and its defect measure is concentrated on regular zeros lying in open irrotational regions where rank fails. Here concentrated means zero measure on the complement, not that the topological support avoids all boundary accumulation points.

The reduction in Section 8 and the zero-free identity in Section 6 also hold. None is an unconditional exclusion of tails whose S has zeros.

## 2. Exact differential identities

Twisted homogeneity and helicity give

    grad k=-aV+(Ax) cross W,
    grad k cross V=kW, W.grad k=0.

For example the second follows by crossing the first with V and using V.W=0 and (Ax).V=k. On {k!=0} this proves curl(V/k)=0. The exterior derivative of V.dx is

    r^(-lambda)[d gamma-d rho wedge(lambda gamma+dK)].

Its wedge with V.dx proves K d gamma=dK wedge gamma. Thus gamma/K is closed wherever K!=0. The same expression says W=0 exactly when both d gamma=0 and dK+lambda gamma=0.

Direct divergence in the twisted coordinates gives

    div Bq=-mu R, R=K+tF, int R=0.

Contracting grad k cross grad S=0 with the radial carrier direction, whose derivatives are (Ax).grad k=-ak and (Ax).grad S=-2(1-c)S, gives

    S grad k=eta k grad S, h dK=eta K dh

on the vortical set and its closure. On an open irrotational set V=-grad k/a and Delta k=0. Its angular equation is

    L K=div(M dK)+t(1-2lambda)ZK-lambda mu K=0.

This is a smooth uniformly elliptic scalar equation on the compact sphere, with a strictly negative zeroth-order term. In particular K is smooth on every open irrotational set. At every zero of K, the explicit nodal premise gives

    gamma=-dK/lambda, Bq=-M dK/lambda.                 (2.1)

These identities use no pressure normalization or boundary limit at spatial infinity.

## 3. Barrier argument and the value on boundary rays

We first prove a local maximum principle with a restricted equation. Let u>=0 be C1 in a connected domain. Suppose L is uniformly elliptic with locally bounded lower-order coefficients and nonpositive zeroth-order coefficient. Assume, locally with a finite constant C, that u is C2 and Lu=0 near each point where |Du|>Cu. Then u is everywhere positive or identically zero.

If not, a sufficiently small ball lying in {u>0} is tangent to an interior zero. Use Euclidean coordinates containing its closed outer annulus. On R/2<|x-y|<R take

    v=epsilon(exp(-kappa |x-y|^2)-exp(-kappa R^2)).

Uniform ellipticity makes Lv>0 for sufficiently large kappa; increasing kappa also gives |Dv|>Cv on the annulus. Choose epsilon>0 small enough that v<=u on the inner sphere; this holds on the outer sphere since v=0. A negative interior minimum of u-v has Du=Dv and |Du|>Cv>Cu. Thus Lu=0 at that point, while L(u-v)=-Lv<0. At a negative minimum its Hessian is nonnegative, its first derivative is zero, and its zeroth-order contribution is nonnegative. This is a contradiction. Hence u>=v. At the tangent zero the inward derivative of v is strictly positive, contradicting Du=0 at a minimum of the nonnegative C1 function. This proves the lemma. Connectedness propagates the local conclusion.

Suppose K<=0. At each zero, dK=0 and homogeneity gives grad k=0. The nodal premise and grad k=-aV+(Ax) cross W give V=0. Near a point where h!=0, the rank contraction bounds |dK|<=C|K| on the closure of the vortical set. Wherever this bound fails there is an open irrotational neighborhood and L K=0. Apply the lemma to -K. Thus K is strictly negative nearby or identically zero nearby. Neither permits a boundary point of {K=0} there. It follows that h=0 at every such boundary point. Since V=0 there, P2=S=0 along the entire corresponding twisted ray.

Every such boundary point is a limit of vortical points. Otherwise a neighborhood is irrotational, and the ordinary strong maximum principle for L again makes K identically zero there. Conversely the interior of {K=0} has V=W=0 and cannot contain a vortical accumulation point. Replacing K by -K proves the other sign case.

If h is nowhere zero, the lemma on the connected sphere forces a one-signed K to be strictly signed or identically zero. The latter gives V=0. In the former case beta=gamma/K is a global closed C1 form on S^2 and hence beta=dphi. With m=|K|, divergence becomes

    div(m e^(-mu phi)(M dphi+tZ))
       =-mu m e^(-mu phi)[(1+tZphi)^2+|dphi|^2].      (3.1)

The bracket is positive; indeed it is at least 1/(1+t^2). Integration over the sphere contradicts (3.1). This proves assertions 2 and 3, for arbitrary t.

## 4. The first derivative at a one-signed zero

At a zero x0, V=W=0. Let D0=DV(x0). It is symmetric and trace free. Differentiating homogeneity in its parameter gives D0(Ax0)=0. If D0!=0, its eigenvalues are d,-d,0 with d!=0 and kernel spanned by Ax0. Since (Ax0).x0=c|x0|^2>0, the tangent plane to the sphere is transverse to that kernel. The restriction of D0 to that plane is a nondegenerate indefinite symmetric form: its projection to the quotient by the kernel is an isomorphism, so the two forms are congruent.

At V=0 this restriction is the derivative of gamma in angular coordinates. Define the C1 vector field X by i_X dA=gamma in an oriented chart. Its derivative has trace zero and negative determinant, so x0 is a hyperbolic saddle and div X(x0)=0. The helicity identity becomes

    XK=K div X.                                      (4.1)

There is a nonconstant trajectory y(s) converging exponentially to x0 as s tends to infinity. The C1 stable manifold theorem gives this trajectory. To make the exponential assertion explicit, write the local field as Lx+g(x), with L hyperbolic and Dg(0)=0. The stable integral equation

    x(s)=exp(sL)xs+int_0^s exp((s-t)L)Ps g(x(t))dt
                         -int_s^infinity exp((s-t)L)Pu g(x(t))dt

is a contraction in the norm sup exp(beta s)|x(s)| for any sufficiently small beta>0 below the linear spectral gap, after shrinking the neighborhood. The two convolution bounds are finite and the local Lipschitz norm of g can be arbitrarily small. A nonzero small stable datum gives the required nonconstant exponentially decaying solution. The primary source in verification proves the C1 version by the same integral equation; no higher differentiability of the vector field is used.

The additional Holder hypothesis gives |div X(y(s))|<=C|y(s)-x0|^alpha, which is integrable. Solving (4.1), K(y(s)) is K(y(0)) times an exponential with a finite positive limit. But K(y(s)) tends to zero, so K(y(0))=0. At every one-signed zero gamma=0 and X=0. This contradicts the nonconstant trajectory. Therefore D0=0.

Taylor's formula now gives V(x0+y)=O(|y|^(1+alpha)) and DV(x0+y)=O(|y|^alpha). The Holder assumption is material for this proof. We do not assert this conclusion for arbitrary C1 tails without a Dini modulus.

## 5. Finite flux measure, including critical zeros

Let E={Bq=0}. At nodal points (2.1) identifies critical zeros with the zeros of Bq. Away from E every nodal point is regular. For epsilon>0 choose a nondecreasing smooth cutoff chi_epsilon=chi(|Bq|/epsilon), zero for |Bq|<=epsilon and one for |Bq|>=2epsilon. The norm need only be differentiated where it is nonzero, so this is a C1 cutoff. On its support the compact regular nodal set admits finitely many C1 boundary charts. The ordinary divergence theorem there yields

    int_{K>0} div(psi chi_epsilon Bq)
       =int_N psi chi_epsilon M(dK,dK)/(lambda|dK|) dH1.  (5.1)

The sign is positive: the outward normal to {K>0} is -dK/|dK| and Bq=-M dK/lambda there. This localization avoids assuming the entire nodal boundary is a smooth curve.

The cutoff error is bounded by

    C |psi| |DBq| 1_{0<|Bq|<2epsilon}.

Its integral tends to zero by dominated convergence. A C1 map has derivative zero almost everywhere on a level set where it is constant. One proof uses Lebesgue density points and differentiability: a nonzero derivative would give a cone of positive relative measure missing the level set. Hence DBq=0 almost everywhere on E. This also gives div(psi Bq)=0 almost everywhere on E. The main term in (5.1) therefore tends to int_{K>0}div(psi Bq).

For psi=1 the right side increases to nu(N), and (5.1) shows this limit is finite. For general psi, dominated convergence with this finite measure proves the formula. There is no extra mass at a critical zero. Repeating for {K<0} changes the outward normal and the sign. Substitution of div Bq=-mu R gives precisely the two identities in Section 1.

The nodal set contributes zero to the area integral of R: its regular part has area zero; on its critical part K=0 and gamma=0, so R=0. Subtracting the two formulas with psi=1 and using R=K+tF proves

    int |K|+(2/mu)nu(S^2)=-t int sgn(K)F.

Any regular zero has a regular arc on which the density is strictly positive, so nu(S^2)>0. For one-signed K every zero is critical, so nu=0. This proves the strictness and equality statements without a Sard theorem or a finite-component premise.

For psi=|h|^r0, r0>1, its derivative is r0|h|^(r0-2)h dh. At a regular zero in the vortical closure, h dK=eta K dh gives h=0. The same implication holds wherever full rank holds at a regular zero. Hence the weighted measure assigns zero mass outside the regular zeros in open irrotational regions where rank fails. Its closed topological support can still contain their boundary limit points. No sign for dh(Bq) follows from W.grad S=0.

## 6. Explicit zero-free scalar identity

If h never vanishes, put f=|h|^eta and g=K/f. The continuous form

    delta=gamma/f+(g/lambda)d log f

is distributionally closed. Indeed its exterior derivative is the continuous two-form

    (d gamma)/f+(gamma wedge df)/f^2+(dK wedge df)/(lambda f^2).

On the vortical set dg=0 and K d gamma=dK wedge gamma cancel it. On the irrotational set d gamma=0 and dK=-lambda gamma cancel it. Products and the exterior derivative are justified by C1 approximation of f; no second derivative of f is required. Thus delta=dpsi for a global C1 function on S^2. Moreover dg=0 on the vortical set and dg=-lambda dpsi on the irrotational set, so dg wedge dpsi=0 everywhere.

Approximate sgn by bounded smooth functions. Their product with dpsi is closed since dg wedge dpsi=0. At critical zeros of g, dpsi=0; regular zeros have area zero. Passing in distributions gives sgn(g)dpsi=dPsi for a global Lipschitz function Psi. Since

    F=fZpsi-(g/lambda)Zf,

integration by parts in the rotational Killing field Z gives

    2lambda nu(S^2)+lambda mu int |K|
       =t mu int (|g|+lambda Psi)Zf.                 (6.1)

The separated nonnegative defect of A618 is exactly 2lambda nu(S^2). This can be read directly from the regular nodal coarea limit: the derivative of a smooth sign approximation has mass 2, and at g=0, dg=dK/f. Section 5 excludes any critical defect. Equivalently the already confirmed A618 identity and (6.1), with these identical potential definitions, identify the two defects.

With G=|g|+lambda Psi, Cauchy-Schwarz yields

    lambda int |K|+(2lambda/mu)nu(S^2)
       <= |t| ||G-average(G)||_2 ||Zf||_2.

This proves nonexistence for t=0 or Zh=0 within this class, but does not give a uniform sign for arbitrary twist. When h has zeros, no use of (6.1) is justified by this proof.

## 7. Additional pointwise consequences and pressure scope

At any nodal point in the vortical closure, S grad k=0 and grad k=-aV. Hence V=0 or S=0. If V!=0 the zero is regular. Without one-signed K the alternative S!=0 does not force DV=0.

If also -Delta P2=partial_i partial_j(V_i V_j)=tr((DV)^2), with V C^(1,alpha), local elliptic regularity gives P2 C^(2,alpha). At a one-signed zero the previous theorem gives DV=0, so Delta P2=0 there and

    S(x0+y)=P2(x0)+grad P2(x0).y
                +(1/2)y^T D2P2(x0)y+O(|y|^(2+alpha)).

At a boundary zero only the constant term has been proved to vanish. Neither the gradient nor the entire Hessian has been proved zero. For the canonical twisted pressure at a stagnation point the integral kernel has both signs. There is no extension here of the pure-swirl negative axis-pressure argument to an arbitrary zero ray.

## 8. Exact remaining one-signed problem and its end flux

For K=-m<=0, on Omega={m>0} write beta=gamma/K, b_beta=beta(Z), A_beta=M beta+tZ, G_beta=(1+t b_beta)^2+|beta|^2. Then

    gamma=-m beta, R=-m(1+t b_beta), F=-m b_beta,
    2e=m^2 G_beta,
    d beta=0, div(m A_beta)=-mu m(1+t b_beta).

Conversely these are exactly the helicity and divergence equations on Omega. There W=0 if and only if d log m+lambda beta=0: that equation gives both dK+lambda gamma=0 and d gamma=0; the reverse implication follows from the first of the two curl equations. On the vortical subset full rank is exactly d(h/m^q)=0. The transport W.grad S=0 follows there from rank and W.grad k=0, and is automatic where W=0.

Thus the unresolved A2 problem is to find or exclude a nonzero m>=0 and closed beta with these equations, the required Cartesian extension of V, V=DV=0 at the zero cone, h=0 at boundary rays, the canonical pressure equation, the rank equation on the vortical subset, and |h|^eta locally A2. These are exact requirements, not a constructed solution.

If beta=dphi on one component, then for every compactly supported C1 cutoff chi,

    mu int chi m e^(-mu phi) G_beta
       =int m e^(-mu phi) A_beta.dchi.               (8.1)

Since G_beta>=1/(1+t^2), an exhaustion with 0<=chi<=1, chi tending pointwise to 1 and right side tending to zero is impossible, by Fatou's lemma and positivity on a compact ball. A surviving candidate therefore has a nonzero period or, if beta is exact, a nonvanishing end flux in this precise exhaustion sense. Exactness alone does not control an unbounded phi near the deleted zero set. The original statement that only periods could defeat the flux proof was too strong.

## 9. Verification and dependencies

All source files, including the original question and complete answer, were read. The independent argument above checks the finite critical-set defect directly and retains the Holder assumption for the derivative result. The source's internal request for an additional model consultation failed before a model answer; it is not counted. The existing coordinator's configured model check of the answer is the comparison available here. Its actual provider runtime is not independently attested. A focused comparison of the critical-set argument and regularity qualifications is recorded in the team records.

Dependencies: A597 supplies the nodal premise for the A2 application; A618 fixes the earlier zero-free potential convention. Section 3 independently reproves the needed kinematic zero theorem. The C1 stable-manifold integral equation is independently checked in Section 4 against S. Schecter, Proof of the Stable Manifold Theorem, January 23, 2013, Theorem 1 and its four-page proof, archived in verification. No numerical, symbolic or formal computation is used in this result. Only public read-only reference retrieval was performed.
