# Cartesian derivative norms evaluated in the polar frame

## Statement, inputs and conventions

Let c>1 be rational and delta=1-1/c. Let F be the complete residual of a finite smooth rational candidate, represented exactly by

    F(r,theta)=r sum_(ell,n) v^(ell delta/2) P_(ell,n)(t) sin(n theta),
    t=r^2/(1+r^2), v=1-t,

where P are rational polynomials, the sum is finite and each n is a positive odd integer. The canonical source, complete residual cache and assembly evidence are retained and hashed. No residual frequency or cross term is omitted.

The targets are

    rF = ||rF||_2,
    G1 = ||grad F||_2,
    P2 = ||omega D^2 F||_2,  omega=(1+4r^2)^(2/5),

where |D^2F|^2=F_xx^2+2F_xy^2+F_yy^2. The rF target is a radial moment norm, not the homogeneous negative norm. This proof gives an alternate finite integration formula for the exact norms in ../whole_plane_norms/PROOF.md.

## Exact polar differentiation

For d=ell delta/2 define T_d P=(1-2dt)P+2t(1-t)P'. For one radial amplitude f=r v^d P(t), direct differentiation gives

    f'=v^d T_d P,
    f/r=v^d P.

Thus the two gradient components of f sin(n theta) in the orthonormal frame (e_r,e_theta) are v^d T_d P sin(n theta) and n v^d P cos(n theta). The frame is orthonormal pointwise, so its Euclidean norm equals the Cartesian gradient norm even though its basis depends on theta.

For the Hessian, the frame coefficients are f'' sin(n theta), n(f'/r-f/r^2) cos(n theta), and (f'/r-n^2 f/r^2) sin(n theta). They can be written r v^(d+1) times the rational polynomials

    A=-2d T_d P + 2(1-t)(T_d P)',
    B=n[-2d P+2(1-t)P'],
    C=(T_d P-n^2 P)/t.

The quotient defining C is required to be polynomial by exact division with zero remainder. For the smooth finite candidate components this also follows from their exact origin vanishing. A failed check stops the computation.

The tensor transformation between orthonormal polar and Cartesian frames is orthogonal on both indices. Therefore its squared Frobenius norm is A^2+2B^2+C^2, including sums over radial branches before squaring. This proves equality with the ordered Cartesian tensor convention. As a separate identity, A+C=(T_d(T_d P)-n^2P)/t, the Laplacian polynomial of ../candidate007_laplacian_fast/PROOF.md. The code checks this identity exactly for every component.

## Angular orthogonality and radial moments

For each relevant polynomial E(t), compose E(1-v)=v^q Q(v) and factor its first nonzero power exactly. Convert Q to containing Arb coefficients only after this step. The contribution for a pair (ell,q,Q),(ell',q',Q') has exponent

    b_rF = (ell+ell')delta/2+q+q'-4,
    b_G1 = (ell+ell')delta/2+q+q'-2,
    b_P2 = (ell+ell')delta/2+q+q'-9/5.

Its polynomial is respectively (1-v)^2 QQ', QQ', or (1-v)QQ'. The P2 exponent has already extracted the v^(-4/5) weight factor. These formulas follow by squaring the displayed amplitudes and using |r dr|=dv/(2v^2). Angular integration gives pi for either sin(n theta)^2 or cos(n theta)^2. Different positive frequencies are orthogonal. Distinct radial branches of the same frequency have multiplicity two; the mixed Hessian coefficient B also has tensor multiplicity two. The square is formed separately for each polar component before summing its integral.

For every nonzero component the code requires diagonal b>-1. Every cross exponent is then above-1 by arithmetic averaging and is checked directly. This suffices for convergence of the complete norm. No infinity claim is made when the check fails. All products of the remaining polynomials are outward Arb products. Integration is the finite formula

    integral_0^1 v^b sum_j z_j v^j dv = sum_j z_j/(b+j+1).

All denominators are positive exact rationals, converted outward. Every evaluated nonzero mode has a positive energy enclosure with at least150relative accuracy bits. Failure stops that mode.

## Analytic weight and complete enclosures

The remaining P2 weight is (4-3v)^(4/5). At degree112 the already reviewed binomial construction gives rational W and epsilon>0 with

    W(v)-epsilon <= (1-3v/4)^(4/5) <= W(v),  0<=v<=1.

Indeed every nonconstant coefficient of this binomial series is negative; the absolute ratio of successive terms is less than3/4. The omitted tail is bounded by four times the first omitted coefficient. If S is a mode's unweighted base integral after extracting v^(-4/5), and T is its W-weighted integral, then its P2 energy lies between

    (pi/2)4^(4/5)(T-epsilon S) and (pi/2)4^(4/5)T.

Although grouped polynomial coefficients can have either sign, S is the integral of the original nonnegative squared tensor amplitude. The pointwise weight inequalities therefore apply. Ball arithmetic encloses both expressions; a positive lower endpoint is required. The code keeps both enclosing endpoints. Distinct implementations can have different weight approximants, so comparisons concern the complete resulting intervals, not corresponding endpoints.

Every final total requires one immutable result for each frequency in its exact input manifest. Sum lower energies and upper energies separately and then take outward square roots. Hashes bind the source, cache, assembly, code, proof and helper implementations. This is complete integration to infinity, with no radial mesh or omitted tail.

## Independent validation and scope

The first calibration is the finite P2 norm of state131, whose exact complete Cartesian Hessian norm was already independently reproduced. Its G1 and rF norms diverge, so they are not finite calibration targets. The new script checks trace identities in every mode and compares the final P2 enclosure with that retained route. Subsequent candidate007 results are compared with N3's independent Cartesian derivative and beta-integral computation on the same canonical source. Equality of representation follows from the derivation above, rather than interval overlap alone. A new value remains OPEN until a peer checks it. No inverse bound or nonlinear existence statement follows.
