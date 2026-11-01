# A majorant that retains the resonance period

Status: PROVED. Independent analytic review of171 and172 was completed by the theory part at2026-10-31T13:01Z. The exact supersolution certificates are confirmed in V325,V326,V330,V332.

## Statement and hypotheses

Assume the hypotheses of145: coprime integers h>=2 and Q>2h, delta=2h/Q, an even bandwidth B, a nonzero leading sine polynomial with frequencies below B, a vanishing first obstruction, and a uniform response lower bound s>0. Let positive rational d_j bound j||f_j||_1 for1<=j<=Q. Let L be a valid uniform bound for the particular Poisson inverse and let kappa be a valid common constant in inequalities(2)-(4) of145 at every subsequently estimated order. The original constants of145 always suffice; the sharper constants require their separate proofs168 and169.

The polynomial system below has2Q unknowns and a strictly triangular affine part at zero. Its unique nonnegative formal solution majorizes the tuned IPM coefficients. If its transformed map admits a nonnegative supersolution box at w=w0>0, then the density, stream, common potential and every appropriately weighted derivative converge absolutely and uniformly on each closed exterior

    r>=R>w0^(-1/(2h)).

For leading amplitude epsilon!=0, multiply this sufficient radius by |epsilon|^(Q/(2h)). The result is local to the exterior. No optimal radius or global stationary extension is asserted.

## 1. Keep harmonics only at resonant orders

Use x_n for scalar bounds on n||f_n||_1 and eta_n for scalar bounds on n|H_n|. Set x_j=d_j through Q. Set eta_n=0 unless n is a positive multiple ofQ. For each true resonance n=kQ, define u_(n,r) by equality in the nonnegative lookahead bounds of145, for1<=r<Q, and define eta_n by its response bound. At other base indices introduce neither u nor eta. After this step define x_(n+1) by the density inequality with equality. Explicitly,

    x_m = kappa sum_(i+j=m) (L x_i+eta_i)x_j,  m>Q,

    u_(n,r) = kappa [L sum_(i+j=n+r, i,j>=r) x_i x_j
                     +sum_(i+j=n+r, j>=Q+1) eta_i x_j
                     +2L sum_(j=1)^(r-1) d_j u_(n,r-j)],

    eta_n = (kappa/s)[L sum_(i+j=n+Q, i,j>=Q) x_i x_j
                      +sum_(i+j=n+Q, j>=Q+1) eta_i x_j
                      +2L sum_(j=1)^(Q-1) d_j u_(n,Q-j)].

All summation indices are positive integers. These equations are triangular in increasing n, then increasing r: restricted density indices are at most n, harmonic indices are at most n-1, and the remaining lookahead index is smaller. The actual free harmonic is zero at every nonresonant order, so retaining these zeros is valid. The domination proof of168 applies unchanged. In particular no artificial harmonic is inserted between successive resonances.

## 2. Group coefficients by their residue modulo Q

Put w=z^Q and define

    X_r(w)=sum_(k>=1) x_(kQ+r) w^(k-1),  1<=r<=Q,
    E(w)=sum_(k>=1) eta_(kQ) w^(k-1),
    V_r(w)=sum_(k>=1) u_(kQ,r) w^(k-1),  1<=r<Q.

Thus the full scalar density is P(z)+sum_(r=1)^Q z^(Q+r)X_r(z^Q), with P(z)=sum_(j=1)^Q d_j z^j, and the harmonic series is z^Q E(z^Q). The residue r=Q denotes multiples ofQ; its first density coefficient is x_(2Q), not x_Q.

All finite sums below have i,j in{1,...,Q}. For1<=r<=Q define

    D_r = sum_(i+j=r) X_i X_j,
    C_r = sum_(i+j=Q+r) X_i X_j,
    a_r = sum_(i+j=Q+r, i,j>=r) d_i d_j,
    b_r = sum_(i+j=Q+r) d_i d_j,

    A_r = a_r + 2w sum_(i+j=Q+r, i>=r) d_i X_j
                 + w D_r + w^2 C_r,
    B_r = b_r + 2 sum_(i+j=r) d_i X_j
                 + 2w sum_(i+j=Q+r) d_i X_j
                 + w D_r + w^2 C_r.

These are ordered sums. Cross products between a known coefficient and an unknown residue series therefore have the factor2. Projection of the scalar equations onto the indicated residues gives

    V_r = kappa [L A_r + w E X_r
                       +2L sum_(j=1)^(r-1) d_j V_(r-j)],  r<Q,
    E   = (kappa/s)[L A_Q + w E X_Q
                       +2L sum_(j=1)^(Q-1) d_j V_(Q-j)],
    X_r = kappa [L B_r + E d_r + w E X_r],  1<=r<=Q.       (1)

For completeness, a product of two unknown density terms has z degree2Q+i+j. After projection to residue r and division by z^(Q+r), it contributes w when i+j=r and w^2 when i+j=Q+r. A known/unknown cross product has degreeQ+i+j, giving the two cross sums in B_r. Restricting the known index to i>=r removes its constant-level cross sum, giving A_r. The harmonic times a density tail has degree2Q+r moduloQ, giving exactly w E X_r. Its product with the known density coefficient gives E d_r only in the ordinary density equation; the lookahead harmonic sum excludes density indices belowQ+1. These facts establish every shift in(1).

## 3. Triangularity and a finite convergence certificate

Order the unknown vector as

    Y=(V_1,...,V_(Q-1),E,X_1,...,X_Q).

At w=0, the V rows depend linearly only on earlier V rows. E depends only on V. The X_r row depends linearly on E and on X_j with j<r. There are no nonlinear unknown terms at zero. Hence Phi(0,Y)=c+JY, with J nonnegative and strictly lower triangular. Its inverse T=(I-J)^(-1)=I+J+...+J^(2Q-1) is nonnegative. Set Y0=T c and

    G(w,Y)=Y0+T[Phi(w,Y)-Phi(0,Y)].

All coefficients of Phi(w,Y)-Phi(0,Y) are nonnegative and have positive w degree. Suppose a vector b>=Y0 and w0>0 satisfy G(w0,b)<=b componentwise. Monotone iteration of G from zero stays below b at w0. For every fixed degree the coefficients stabilize to the unique formal solution, since every nonconstant term raises the w degree. Monotone convergence of the nonnegative evaluations bounds every residue series at w0. Consequently x_n and eta_n obey a common geometric bound with base A=w0^(-1/Q), up to fixed residue-dependent factors.

The true density and stream coefficients are dominated by these scalar bounds. Their angular support is at most Bn, and each fixed weighted spatial derivative costs only a polynomial factor in n. A strict exterior radius R>A^(1/delta)=w0^(-1/(2h)) absorbs these factors and permits a positive angular strip. The potential reconstruction of145 preserves the geometric base and its finite exceptional logarithm. This proves the stated convergence conclusion.

## 4. Independent checks and limitations

The implementation is to be checked against direct scalar sums indexed by the total order n, with eta forced to zero away from multiples ofQ. This is independent of the residue projection formulas. Check several complete block coefficients, the affine identity at zero, strict triangularity, exact rational box images, and failure of the adjacent dyadic box when reporting a smallest exponent within that box family.

Every input d_j and every response lower bound must have its own certificate. A small numerical prefix is not substituted for either the response hypothesis or the all-order argument. A failed supersolution box does not disprove convergence. This result addresses h>=2; an h=1 variant requires its different first-resonance initialization.

## Completed exact checks

The implementation checks three full coefficients in each residue component against a direct total-order scalar recurrence. Six generic exponent pairs give294 exact coefficient identities; seven certified4/9 profiles give378 more. All affine-map, strict-triangularity and dyadic-box checks pass. The generic, two-mode and Candidate-shaped batches took1.3164903898723423,1.635238619055599 and0.6667494093999267 seconds.

With the certified inputs of168 and169, the five ordered two-mode roots have smallest passing dyadic w-exponents156,152,167,156,171 in the box family2Y0. Their sufficient radius exponents would be39,38,167/4,39,171/4. Candidate-shaped roots2 and3 give w-exponents194 and200, normalized radius exponents97/2 and50, and conservative restored-amplitude exponents59 and60. These all-order improvements await independent review of the new block projection; the exact finite certificates are complete.

The additional Candidate-shaped root4 passes54 more coefficient checks. Its w-exponent198 gives normalized radius exponent99/2 and conservative restored-amplitude exponent60. Its exact calculation took0.28611187916249037 seconds. This certificate has the same pending analytic status as the other171 refinements.

## Independent review closure

The theory part independently rederived the scalar domination, every residue projection and the constant-level triangularity at2026-10-31T13:01Z. All exact boxes already passed. The earlier pending status above records the audit chronology; the theorem and these sufficient radii are now PROVED. The167 root interval is propagated through every Cartesian operation and every computed harmonic without a midpoint reset. Thus its prefix bounds contain the exact uniquely tuned coefficients at the exact algebraic root. The65-digit export bounds are treated as enclosing intervals before upward rational rounding.
