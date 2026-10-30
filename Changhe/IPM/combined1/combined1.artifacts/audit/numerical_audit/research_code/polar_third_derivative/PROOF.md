# Complete weighted third-derivative norm in an orthonormal polar frame

## Exact statement and hypotheses

Let c>1 be rational, delta=1-1/c, t=r^2/(1+r^2) and v=1-t. Let the smooth real S1 residual F have the complete finite representation

    F(r,theta)=r sum_(ell,n) v^(ell delta/2) P_(ell,n)(t) sin(n theta),

with rational polynomials P and positive odd integers n. The canonical candidate, complete residual cache and its verified assembly are exact inputs. For every nonzero component assume the quotients and endpoint conditions below pass exact checks. The target is

    Q3(F)=||(1+4r^2)^(2/5) D^3 F||_L2(R2),
    |D^3 F|^2=F_xxx^2+3F_xxy^2+3F_xyy^2+F_yyy^2.

This note derives a complete finite integration formula, independent of the Cartesian derivative construction used by N3. It proves no inverse estimate or existence result. New numerical outputs remain OPEN until independently reviewed. State131 is a calibration target because its Q3 is finite and has a separately verified complete Cartesian value. Candidate007 is evaluated only after that calibration succeeds.

## Derivation of all third derivatives

For d=ell delta/2 define the polynomial operator

    T_d P=(1-2dt)P+2t(1-t)P'.

Since dt/dr=2r v^2, the derivative of r v^d P(t) is v^d T_d P. The verified polar Hessian calculation in ../polar_derivative_norms/PROOF.md gives the orthonormal Hessian components as r v^(d+1) times

    A sin(n theta), B cos(n theta), C sin(n theta),
    A=-2d T_d P+2v(T_d P)',
    B=n(-2d P+2vP'),
    C=(T_d P-n^2 P)/t.

The three components correspond to rr,rtheta,thetatheta. Division by t must have zero remainder. Smoothness of the separated harmonics supplies the cancellation for the intended candidates; the computation checks it exactly.

The orthonormal frame satisfies

    nabla_(e_r)e_r=nabla_(e_r)e_theta=0,
    nabla_(e_theta)e_r=e_theta/r,
    nabla_(e_theta)e_theta=-e_r/r.

For a covariant Hessian tensor H, its covariant derivative is

    (nabla_a H)(b,c)=a[H(b,c)]-H(nabla_a b,c)-H(b,nabla_a c).

Thus the four independent third-tensor components, in the order rrr,rrtheta,rthetatheta,thetathetatheta, are v^(d+1) times

    A3 sin(n theta), B3 cos(n theta), C3 sin(n theta), D3 cos(n theta),
    A3=T_(d+1) A,
    B3=T_(d+1) B=nA-2B,
    C3=T_(d+1) C=A-C-nB,
    D3=nC+2B.

For example, differentiating H_rr along e_theta gives v^(d+1)(nA-2B)cos(n theta), and differentiating H_rtheta along e_theta gives v^(d+1)(A-C-nB)sin(n theta). The two connection terms in the derivative of H_thetatheta give +2B. Equality with radial differentiation is exactly the symmetry of third derivatives of a scalar. The checker verifies both displayed polynomial identities for every input component, independently of numerical point tests.

At every point away from the origin, an orthogonal change of frame on each tensor index preserves its squared norm. The third tensor is symmetric, so the ordered Cartesian norm equals

    A3^2 sin(n theta)^2+3B3^2 cos(n theta)^2
      +3C3^2 sin(n theta)^2+D3^2 cos(n theta)^2,

after summing all radial branches within each tensor component. The multiplicities count the three positions of the unequal index. The origin has measure zero, and the assumed smoothness extends the fields there. No frequency mixing arises from the frame coefficients used for their norm.

## Complete radial integral and weight enclosure

For each nonzero third-component polynomial E(t), write E(1-v)=v^q Q(v), extracting its first nonzero power exactly. For branches (ell,q,Q) and (ell',q',Q'), their product has radial exponent

    b=(ell+ell')delta/2+q+q'-4/5.

Indeed the third derivative amplitudes contribute v^((ell+ell')delta/2+2); the measure is |r dr|=dv/(2v^2); and the squared weight is

    (1+4r^2)^(4/5)=v^(-4/5)(4-3v)^(4/5).

There is no remaining factor1-v in this third-derivative integral. Angular integration gives pi for each positive sine or cosine frequency. Different positive frequencies are orthogonal. Cross terms of distinct radial branches have multiplicity2. The four tensor components have multiplicities1,3,3,1. Keeping all those products gives a finite grouped polynomial integrand whose unweighted base integral S is nonnegative because it is a sum of squared real tensor amplitudes.

Require the diagonal exponent ell delta+2q-4/5>-1 for every nonzero component, and check every cross exponent too. Averaging proves the cross condition from the diagonals. These conditions imply absolute integrability. Failure stops the computation; this sufficient test alone is not used to assert divergence. Every finite power integral is

    integral_0^1 v^b sum_j z_j v^j dv=sum_j z_j/(b+j+1),

with positive exact rational denominators. Convert rational coefficients to outward balls only after endpoint extraction and use outward polynomial multiplication and division throughout.

The already reviewed degree112 binomial bound supplies rational W and epsilon>0 such that

    W(v)-epsilon <= (1-3v/4)^(4/5) <= W(v), 0<=v<=1.

Every nonconstant coefficient of this binomial series is negative, and the ratio of consecutive term magnitudes is less than3/4 on the unit interval. Four times the first omitted coefficient therefore bounds the complete omitted tail uniformly. If T is the same grouped integral after multiplication by W, the full weighted mode energy lies between

    (pi/2)4^(4/5)(T-epsilon S) and (pi/2)4^(4/5)T.

This comparison applies to the original nonnegative squared integrand even though its polynomial coefficients have mixed signs. Retain positive accurate outward endpoint balls. Sum lower mode energies and upper mode energies separately and take outward square roots only after every mode in the manifest is present. This integrates the entire plane, including both endpoints, without a radial mesh or a tail approximation.

## Independent fixtures and verification evidence

Before any candidate norm, test n=1,3,7 and integer d=4,5 using

    P(t)=t^((n-1)/2)(1-2t+3t^2),
    F=Im(x+iy)^n [1+2(x^2+y^2)^2]/(1+x^2+y^2)^(d+(n-1)/2+2).

Differentiate this Cartesian rational expression three times symbolically. At rational points compute all four tensor projections onto(e_r,e_theta). After multiplying by r^n, the remaining factor r^(n-3) is an integer power of r^2, so every comparison is an exact rational identity. Check the ordered Cartesian squared norm against the polar squared norm as a second identity. This verifies the connection terms and the multiplicities without using the candidate derivative implementation. Check elementary power moments separately.

Then compute complete state131 Q3 and compare its containing interval with the retained Cartesian result. Only after that succeeds compute candidate007 Q3 and compare with N3 on the identical canonical source. Different valid weight approximants need not give equal endpoints; comparison is of the complete enclosing intervals. Source hashes bind the candidate, complete D0 cache, its assembly, own proof/code and all helpers. Every immutable mode record binds the same manifest and lists its endpoint and tensor identities. A peer can reproduce the formula without importing either Cartesian derivative implementation.

Dependencies are the exact radial-Fourier residual assembly, elementary polar tensor differentiation, finite polynomial power integration and the previously verified binomial bound. The informal proof above precedes execution. There is no proof-assistant build, remote computation or optimizer execution in this audit.
