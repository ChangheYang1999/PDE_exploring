# The transverse-scale term in the strip-to-disc energy design

Topic63. The result is an exact calculation of a specified Hamilton expression and two obstructions to its uniform negativity. It does not prove failure of an inverse, Fredholm property, or IPM existence. The strip-to-disc design considered here has been set aside by the lead; these calculations audit its stated reasons.

## 1. Setup and statement

Use X=(x,y), frequencies zeta=(xi,eta), and a real C2 vector field V. Set p=V1 xi+V2 eta and define

    H_p = V1 partial_x + V2 partial_y
          -(V1_x xi+V2_x eta) partial_xi
          -(V1_y xi+V2_y eta) partial_eta.

The stationary residual is F(rho)=(c_l X+U[rho]) dot grad rho-rho. Its fixed-scaling linear part is L0 h=V dot grad h-h+U[h] dot grad rho. Differentiating the density-dependent scaling adds the separate rank-one strain term. Thus the signs of both -h and +U[h] dot grad rho are fixed by this stated residual, not by a time-evolution convention.

For a C1 density rho define the canonical order-zero velocity-coupling symbol

    q(X,zeta)=(rho_x xi eta-rho_y xi²)/(xi²+eta²), zeta !=0.

The sign follows directly from -Delta psi=h_x and U=(-psi_y,psi_x): U1 has multiplier xi eta/|zeta|² and U2 has multiplier -xi²/|zeta|². The rank-one strain term is not represented by q and is not estimated here.

Let lambda(x)>0 in an open transition interval, phi be C1, and b be a CONSTANT real exponent. Write

    a(x,y)=sqrt(y²+lambda(x)²), W=exp(phi(x)) a^-b,
    Q=xi²+a² eta², m=W Q^(sigma/2), sigma>0,
    c0(X)=1+div V(X)/2,
    beta_m=-c0-H_p log m+q.                                (1)

For an IPM transport field div V=2c_l, c0=1+c_l. Formula(1) is the candidate principal real energy coefficient: the transport contribution to the real unweighted L2 pairing is -1-div V/2, by integration by parts. This proof treats beta_m as the exact Hamilton expression in(1). Identifying it with a particular global fractional-operator realization, and controlling lower-order remainders through degeneracy, require a calculus not proved here. Nothing below asserts that such a global realization or inverse has been constructed.

Set v_a=V dot grad log a. Direct differentiation gives

    beta_m = -c0-V1 phi'+b v_a+q
       +sigma [V1_x xi²+(V2_x+a²V1_y)xi eta
                          +a²(V2_y-v_a)eta²]/Q.            (2)

Thus the changing transverse scale contributes to both the weight derivative and the frequency stretching. If b were a function of x, an additional term V1 b' log a would appear. Treating b as a variable function while omitting that term is invalid.

## 2. Proof of the Hamilton calculation and coupling bound

Since H_p acts on scalar functions of X as V dot grad,

    H_p log W=V1 phi'-b v_a.

Also H_p xi=-(V1_x xi+V2_x eta), H_p eta=-(V1_y xi+V2_y eta), and H_p(a²)=2a²v_a. The product rule therefore gives

    H_p Q = -2V1_x xi²-2(V2_x+a²V1_y)xi eta
                               +2a²(v_a-V2_y)eta².

Substitution into H_p log m=H_p log W+sigma H_p Q/(2Q) proves(2), including every sign. No limiting pseudodifferential argument is needed for this algebraic identity.

With t=(xi,a eta), the stretching quotient is t^T S_a t/|t|², where

    S_a = [[V1_x, (V2_x/a+a V1_y)/2],
           [(V2_x/a+a V1_y)/2, V2_y-v_a]].                 (3)

The coupling matrix in ordinary frequency variables is [[-rho_y,rho_x/2],[rho_x/2,0]]. Its eigenvalues are (-rho_y +/- sqrt(rho_x²+rho_y²))/2. Hence

    q <= (|grad rho|-rho_y)/2,
    beta_m <= -c0-V1 phi'+b v_a
                      +sigma lambda_max(S_a)
                      +( |grad rho|-rho_y )/2.             (4)

This sufficient upper bound loses the correlation between the two frequency quotients. For rho_y>0, rationalizing gives

    (|grad rho|-rho_y)/2
       =rho_x²/[2(|grad rho|+rho_y)] <=rho_x²/(4rho_y).      (5)

None of these bounds controls the omitted nonlocal strain or lower-order commutators.

## 3. Scale collapse at a finite endpoint

Take the axis-linear field V1=w(x), V2=mu(x)y. Then

    v_a=(w lambda lambda'+mu y²)/(lambda²+y²).              (6)

At y=0 and xi=0, eta !=0, the coupling q is exactly0, without any assumption on rho_y. Equations(2) and(6) give

    beta_perp=-c0-w phi'+sigma mu
                          +(b-sigma)w lambda'/lambda.      (7)

Here c0=1+(w'+mu)/2 for this model. In the IPM case w'+mu=2c_l and c0 is constant. At y=0 this direction also satisfies p=0. The positivity problem cannot be dismissed solely as a direction away from the characteristic set.

Suppose lambda is C1 and positive on(x0,x1], tends to0 as x decreases to the finite endpoint x0, w<=-w0<0 there, b<sigma, and the function -c0-w phi'+sigma mu is bounded below. Then beta_perp is unbounded above along a sequence x_n decreasing to x0.

Proof: lambda'/lambda cannot be bounded above on any interval(x0,x0+epsilon). Otherwise choose a nonnegative upper bound M and integrate it from x to x0+epsilon to obtain

    log lambda(x) >= log lambda(x0+epsilon)-M epsilon,

contrary to lambda(x)->0. Choose x_n->x0 with lambda'(x_n)/lambda(x_n)->+infinity. Because (b-sigma)w >= (sigma-b)w0>0, equation(7) diverges to+infinity along this sequence. This argument does not require monotonicity of lambda; monotonicity is a sufficient feature of the proposed cutoff. Bounded w,mu,w',phi' near x0 imply the stated lower bound on the other terms.

This REFUTES uniform negativity of this particular beta_m under these hypotheses. For each fixed positive lambda, beta_m is continuous in y, so the same failure is approached from y>0. It does not refute a different norm, an estimate using other terms, or an inverse of the full operator. If b>=sigma, this specific adverse sign disappears; that inequality does not establish the required mappings or coercivity.

A simple exact illustration is w=-1, mu=1, phi=0, lambda=x^nu on x>0, nu>0. Here c0=3/2 and beta_perp=sigma-3/2+(sigma-b)nu/x. Smooth flat cutoffs such as exp(-1/x) produce the same phenomenon, with lambda'/lambda=1/x².

## 4. The pure strip and the characteristic set

On the pure strip lambda=0 and y>0, a=y. Put tau=y eta. For the same axis-linear field, v_a=mu and the matrix(3) is exactly

    S_strip=[[w',mu'/2],[mu'/2,0]].                         (8)

The stretching part is therefore

    (w' xi²+mu' xi tau)/(xi²+tau²).

Suppose grad rho is bounded near the axis. For fixed (xi,tau) with tau !=0 and eta=tau/y, the ordinary coupling q tends to0 as y decreases to0. Indeed its numerator is rho_x xi tau/y-rho_y xi² and denominator is xi²+tau²/y²; multiplication by y² makes the numerator tend to0 while the denominator tends to tau². No assertion at tau=0 follows from this limit.

Assume w!=0 and mu!=0. On the conormal characteristic set p=w xi+mu tau=0, choose xi !=0 and tau=-w xi/mu. Taking the preceding y-limit at this fixed x gives

    beta_char=-c0+b mu-w phi'
             +sigma (w'-w mu'/mu)/(1+(w/mu)²).              (9)

This proves the claimed characteristic expression, including its division hypotheses. If x tends to L from below with w->0, w'->A_P>0, mu->1, and mu',phi' bounded, the limit is

    -[1+(A_P+1)/2]+b+sigma A_P
       =(sigma-1/2)A_P+b-3/2.                             (10)

If the field obeys w'+mu=2c_l, this is -c0+b+sigma A_P. It is an ITERATED limit: first y->0 at each x<L with w!=0, then x->L. At x=L, the characteristic direction has tau=0, so the vanishing-coupling argument does not apply by direct substitution. A diagonal sequence with y/|tau|->0 realizes the iterated limit. This explains why the ordinary source-disc coupling can have a different effect from the pure-strip limit without a contradiction.

A robust illustrative parameter check uses sigma=13/4, b=307/100, A_P in[10,51/5] and mu_P in[99/100,101/100], with c0_P=1+(A_P+mu_P)/2. The corresponding limit is

    (sigma-1/2)A_P+(b-1/2)mu_P-1 >=290443/10000>0.         (11)

This is an exact rational example of the failure of negative characteristic rate in this pure-strip model. The nearby actual source data are not required for(11), and no parameter enclosure for a hypothetical exact profile is inferred from it.

## 5. Moving cutoff and scope

For chi(x,y)=theta(y/lambda(x)), lambda>0, the ordinary transport commutator is multiplication by

    [V dot grad,chi]=theta'(y/lambda)
                      [V2/lambda-y V1 lambda'/lambda²].   (12)

This follows by differentiating the quotient y/lambda. It supplies another term that must be bounded in a localization proof. Neither the matrix calculation nor a sampled symbol supplies that bound automatically.

Dependencies: the explicitly defined Hamilton derivation, elementary symmetric-matrix eigenvalues, the fundamental theorem of calculus for log lambda, continuity and algebraic limits. No global pseudodifferential calculus, compactness assertion, candidate enclosures or inverse theorem is invoked. CONFIRMED subject to checks: formulas(2),(7),(9),(12) and the stated failures of uniform negativity. OPEN: an actual global operator estimate in any revised norm, all jet/remainder/domain matching, the full inverse and every PDE endpoint.
