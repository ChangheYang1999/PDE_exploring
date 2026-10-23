# Exact axis core constants from a polynomial compactification

Result217. This result concerns explicit finite hydrostatic trial densities, not exact solutions of SettingIII. Its purpose is to replace a long-radius fit of the axis constant by an independently derived convergent finite-part integral. All sources are frozen in verification/INPUTS.json. No producer evaluator is imported or copied.

## Hypotheses, notation and the inverse

Let1<P<=2 and L>0. Define w=(1-t)/2, sigma=1-w and

    y=C*sqrt(1-w)*w^(-P), C=L/2^P, 0<w<=1,
    p=1-1/P.

The saved trial density is g=y*w*sum_k sigma^k beta_k(t) cos(2k theta). Each beta_k is a polynomial, either directly or after an exactly specified affine change of the Chebyshev coordinate. Exact reconstruction from the saved binary coefficients is possible over the rationals.

Let H(w)=g(0,y(w))/y(w), and let k(w) denote d_y V2(0,y(w)), where V2 is the canonical hydrostatic inverse

    V2(0,y)=int_0^y t*g_xx(0,t)dt+y*int_y^infinity g_xx(0,t)dt.  (1)

These are polynomials inw, with H(0)=k(0)=0. The construction and proof of the exact k polynomial are in ../hydrostatic_axis_primitive/PROOF.md: if J_t=sum k_mode^2*(-1)^k_mode*[w+2P sigma]*sigma^(k_mode-1)*beta_k(t), J(-1)=0, then k=-H-J(1)+J(t). It follows directly by integrating the analytic polar identity g_xx=(H_logr+H_thetatheta)/y. In particular k_y=-g_xx, k(1)=d_yV2(0,0), and no tail cutoff or homogeneous velocity is added.

Write k(w)=sum_{j>=1} k_j*w^j and H(w)=sum_{j>=1} h_j*w^j. Here the index on k_j is a polynomial exponent, not an angular mode. The leading density and curvature coefficients are

    K=h1*C^(1/P), Q=k1*C^(1/P)/P.                    (2)

Indeed H~h1*w, k~k1*w and y^(p-1)~C^(-1/P)*w; k~Q*y^(p-1)/(1-p). The exact map exponentp is used in all limiting statements. When a stored transport parameterc does not equal1/p exactly, that mismatch is recorded separately rather than silently rounded away.

## A convergent formula for m0 when1<P<2

For1<P<2 define

    m0=lim_{y->infinity}[V2(0,y)-Q*y^p/(p*(1-p))].    (3)

This limit exists for the finite polynomial trial. To see it and compute it, integrate(1) by parts using k_y=-g_xx and change variable tow:

    V2(0,y(w))=y(w)*k(w)
       +C*int_w^1 v^(-P)*sqrt(1-v)*k'(v)dv.          (4)

The integral's only nonintegrable endpoint term at0 is k1*v^(-P). Define R(v)=(k'(v)-k1)/v, a polynomial. Then the finite part of that integral equals

    J=int_0^1 v^(1-P)*[sqrt(1-v)*R(v)
                         -k1/(sqrt(1-v)+1)]dv-k1/(P-1).  (5)

This is absolutely convergent, because1-P>-1. It uses sqrt(1-v)-1=-v/(sqrt(1-v)+1), so evaluation need not subtract close numbers near0. In(4) the divergent term has coefficient C*k1*P/(P-1)*w^(1-P). This agrees with the leading subtraction in(3) by(2). The difference between that power and y^p is O(w^(2-P)), which tends to0. Also all higher terms of y*k tend to0. Therefore

    m0=C*J.                                         (6)

An equivalent finite sum is

    m0=C*sum_{j>=1} j*k_j*B(j-P,3/2).               (7)

Forj>=2 the beta integral is convergent. Forj=1 define

    B(1-P,3/2)=B(2-P,1/2)/(2*(1-P)).

This equals the finite part of the j=1 integral: integrate the subtracted sqrt(1-v)-1 expression by parts, whose boundary terms vanish at0 and cancel the explicit1/(1-P) term at1. Thus(7) follows from convergent integrals and one integration by parts, without presuming a divergent integral is an ordinary beta integral. The usual gamma formula is an evaluation of this established finite part. AtP=3/2 the simple manufactures k=w and k=w^2 give m0=-pi*C and+pi*C, respectively.

For numerical verification, formula(5) can be regularized further by v=u^(1/(2-P)); then v^(1-P)dv=du/(2-P). This gives an ordinary finite interval integral. A distinct physical-axis cross-check uses direct density derivatives in(1). The absolutely convergent direct-curvature moment is proved separately in INTEGRAL_PROOF.md. Comparing(5) and(7), and increasing precision beyond the magnitude of the rational polynomial coefficients, tests cancellation in the finite sum. Rounded producer fits are compared only after these tests.

## The logarithmic coefficient atP=2

WhenP=2 the next term of sqrt(1-w)k'(w) is

    k1+(2*k2-k1/2)*w+O(w^2).

Thus(4) contains C*(2*k2-k1/2)*log(1/w), in addition to the leading power. Since log y=log C-2log w+O(w),

    V2(0,y)-Q*y^(1/2)/[(1/2)(1/2)]
       =B_log*log y+O(1),
    B_log=C*(k2-k1/4).                              (8)

This follows from convergent remainder integrals after subtracting the two displayed terms. No finite m0 exists if B_log!=0. The coefficient can be computed exactly from k1,k2 andL, since C=L/4. In terms of the old Chebyshev variablet,

    k1=-2*k_t(1), k2=2*k_tt(1),
    B_log=C*[2*k_tt(1)+k_t(1)/2].                    (9)

These identities are an independent endpoint check on the monomial conversion. Formula(8) is a statement about the saved trial, not an exact profile or a convergence sequence.

## Leading residual coefficient and the conditional m0/6 rule

The next density coefficient is obtained without fitting:

    G(y)=K*y^p+c2*y^(2p-1)+O(y^(3p-2)),
    c2=C^(2/P)*[h2-h1/(2P)].                        (10)

To verify(10), expand G=yH and subtract K*y^p at fixedw. The coefficient ofw^(2-P) is C*[h2-h1*(1-p)/2], and y^(2p-1)~C^(2p-1)*w^(2-P). This gives(10).

For a transport ratec, the axis residual R=(cy+V2)G'-G begins

    R=(c*p-1)K*y^p+r2*y^(2p-1)+...,
    r2=[c*(2p-1)-1]*c2+K*Q/(1-p).                  (11)

When c*p=1, r2=(1-c)*c2+KQ/(1-p). For1<P<2, the next nonlattice term is pK*m0*y^(p-1); the next pure polynomial-lattice power3p-2 is smaller becausep<1/2. If K>0, c*p=1 andr2=0, then Nf=2K*y^p*(1+o(1)), so

    lim y*R/Nf=p*m0/2.

Atc=3 this is m0/6, with its sign. Under the same K>0 and c*p=1 assumptions, if r2!=0, the leading value of y*R/Nf instead grows like [r2/(2K)]*y^p. ForK<0 replaceK in the denominator byabs(K), so the constant limit whenr2=0 is sign(K)*p*m0/2. No normalized limit here is asserted whenK=0. The frozen states haveK>0, which is checked explicitly in the summary. Ifc*p!=1, an even earlier exact leading term is present. Hence an unconditional m0/6 limit cannot be asserted for arbitrary stored trial states. This conclusion is derived from the defining axis transport, not inferred from an empirical fit.

## Scope of verification

The implementation will reconstruct rationalH,k polynomials from the frozen16 states, establish their endpoint cancellations, evaluate(7) at two or more adequate precisions when1<P<2, cross-check(5) on manufactures and selected states, and evaluate(8) exactly whenP=2. It will compute(2),(10),(11) directly, then compare the producer's fit values and selected physical-axis evaluations. The inverse is hydrostatic, not the full elliptic IPM inverse. None of these trial-state diagnostics can establish YES or NO for SettingIII.
