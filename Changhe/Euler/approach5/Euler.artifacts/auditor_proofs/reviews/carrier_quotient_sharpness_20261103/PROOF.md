# Smooth flat carrier fields with all subcritical planar integrability exponents

Status: independently CONFIRMED A2481-A2484 after full proof checking and the existing coordinator comparison of the exact construction; full-system extensions OPEN A2485. The construction satisfies the carrier system only. It is not a common-flat Euler construction or a decaying global Euler profile.

## 1. Exact statements and scope

Let D be a planar disc centred at zero, and let b:D->R2 be smooth. There is a smaller disc D_R and a smooth field w:D_R->R2 such that

    div w=b.w,
    every derivative of w at zero vanishes,
    w(y) != 0 for 0<|y|<R,
    |Dw(y)|/|w(y)| <= C (1+(log log(1/|y|)+2)/|y|).             (1)

Here R<exp(-e), C is a finite constant depending on b and R, and |Dw| may be either the operator or Frobenius norm after increasing C. In particular the ratio is in Lp(D_R) for every 0<p<2, where the value at zero is assigned arbitrarily. For p<1, Lp means finiteness of the pth-power integral, without asserting it is a normed space.

For the carrier application fix any 0<c<1/2 and omega in R, put

    Jx=e3 cross x, A=cI-omega J, X(x)=Ax,
    L=(1-c)I+omega J, kappa=3c-1.

Let sigma:D->R3 avoid zero, be smooth and satisfy

    det(sigma_1,sigma_2,X(sigma)) != 0.

Then a smaller flowbox about x1=sigma(0) carries a smooth vector field V satisfying

    div V=0, X.V=0, DV X=-LV.                                 (C)

It is flat at x1 and nonzero at sigma(y) for every nonzero y in that smaller section disc. Writing W=curl V, it satisfies

    |(W.X)(sigma(y))|/|V(sigma(y))|
       <= C (1+(log log(1/|y|)+2)/|y|).                        (2)

Thus this ratio lies in every Lp with 0<p<2. The construction is valid for every omega. The confirmed L2 continuation theorem C68(a), A2471, shows that this ratio is not in L2 on any section disc about zero. This is sharpness only within (C). No S, pressure, Poisson equation, Euler energy identity, decay condition or global extension is provided.

The submitted C69 theorem is the special case omega=0 or c=1/3. Section 6 checks its original integrating-factor proof separately. Sections 2-5 supply a different construction for arbitrary smooth b and hence arbitrary omega.

Dependencies are elementary differentiation, the inverse function theorem, the coordinate divergence formula and the previously derived carrier-quotient correspondence A2437. The needed direction of that correspondence is proved again in Section 5. No numerical computation or formal build is used.

## 2. The flat radial factor

For 0<r<R<exp(-e), put t=log(1/r) and

    g(r)=exp(-t log t).

Then g is positive and increasing, and

    g'(r)=(log t+1)g(r)/r.                                    (3)

For each integer k>=0, differentiation gives

    g^(k)(r)=r^(-k) Q_k(t) g(r),
    Q_0=1, Q_(k+1)=(log t+1-k)Q_k-Q_k'.

The functions Q_k are finite polynomials in log t and 1/t. Induction on k bounds their absolute values by C_k(1+log t)^k for t>e. Consequently, for every k and N there is a finite C_(k,N) such that

    |g^(k)(r)| <= C_(k,N) r^N, 0<r<R.

Indeed log t eventually exceeds any prescribed power exponent, and powers of log t are negligible compared with exp(epsilon t) for fixed epsilon>0. All claims about flat extension below use these derivative bounds, not just flatness of g itself.

## 3. Solving the quotient equation by a radial correction

For y=r(cos theta,sin theta), write e_r=(cos theta,sin theta), e_theta=(-sin theta,cos theta), and

    b_r(r,theta)=b(re_r).e_r,
    b_theta(r,theta)=b(re_r).e_theta.

After shrinking R, all mixed derivatives of these two functions in r and theta, of each fixed finite order, are uniformly bounded on (0,R] times the circle. This follows by differentiating the smooth Cartesian b on the closed disc; angular differentiation introduces bounded trigonometric factors and nonnegative powers of r.

Define

    E(r,s,theta)=exp(integral_s^r b_r(u,theta) du),
    q(r,theta)=r^(-1) integral_0^r s b_theta(s,theta)g(s)
                                      E(r,s,theta) ds,
    w(re_r)=g(r)e_theta+q(r,theta)e_r.                         (4)

The integrals converge absolutely. They are periodic in theta and smooth for r>0. Differentiating r q at positive r gives

    partial_r(rq)=r b_theta(r,theta)g(r)+b_r(r,theta) r q,
    q_r=b_r q+b_theta g-q/r.                                  (5)

The polar divergence identity and the absence of theta dependence in g give

    div w=(1/r)partial_r(rq)+(1/r)partial_theta g
         =b_r q+b_theta g=b.w.                                (6)

No exactness condition on the one-form b.dy has been used. Equation (6) is an exact identity for every smooth b.

## 4. Smooth flat extension and the quantitative ratio

Let M bound |b_r| and |b_theta| on the closed disc in polar coordinates. For 0<s<=r<=R, E lies between exp(-MR) and exp(MR). Since g(s)<=g(r), formula (4) gives

    |q(r,theta)| <= (M exp(MR)/2) r g(r).                     (7)

The same estimate, with a new constant C_l, holds for every fixed angular derivative:

    |partial_theta^l q(r,theta)| <= C_l r g(r).                (8)

To see this, differentiate under the integral. Every angular derivative of E is E times a finite sum of products of integrals integral_s^r partial_theta^j b_r du. Each such integral is uniformly bounded by a constant times r-s. Derivatives of b_theta are uniformly bounded as well. The absolute value of the differentiated integrand is therefore at most C_l s g(s), and (8) follows by integration. The constants may depend on l; no uniform analytic estimate is claimed.

For completeness, all mixed radial and angular derivatives are flat too. An induction using (5), first differentiated in theta, gives the following sufficient bound for each k,l:

    |partial_r^k partial_theta^l q(r,theta)|
       <= C_(k,l) r^(1-k)(1+log t)^k g(r).                    (9)

For k=0 this is (8). At the induction step differentiate the right side of the identity (5) k times and l times in theta. Leibniz' rule gives bounded mixed derivatives of b_r,b_theta multiplying already bounded derivatives of q or g, and derivatives of 1/r multiplying derivatives of q. A term with j radial derivatives on q and k-j on 1/r is bounded by a constant times r^(-k+j-1) r^(1-j)(1+log t)^j g=r^(-k)(1+log t)^j g, exactly of the required form for order k+1. The terms containing g have the same or a better power by Section 2. Terms with bounded coefficient derivatives are absorbed using r<=R and enlarging the constant. This proves (9).

Cartesian derivatives of w on the punctured disc are finite sums of polar mixed derivatives of g and q, multiplied by trigonometric functions and fixed powers of 1/r. This follows inductively from

    partial_y1=cos theta partial_r-(sin theta/r)partial_theta,
    partial_y2=sin theta partial_r+(cos theta/r)partial_theta.

Sections 2 and (9) imply that every Cartesian derivative is O(r^N) for every N. Define w(0)=0 and each derivative there to be zero. These are the actual derivatives: induction on the order uses the difference quotient along coordinate segments, whose numerator is o(|h|), and continuity of the already extended derivative. Hence w is smooth on D_R and flat at zero. Since b.w and div w extend continuously, equation (6) holds at zero too.

Orthogonality of e_r and e_theta gives

    |w|^2=g^2+q^2 >= g^2>0,

so w has no punctured-disc zeros. Equation (5), (7), and (8) with l=1 give

    |q_r|<=C g, |q_theta|<=C r g.

Also

    partial_r w=g' e_theta+q_r e_r,
    partial_theta w=(q_theta-g)e_r+q e_theta.

Therefore

    |Dw|<=C (|g'|+g/r+g),
    |Dw|/|w|<=C (1+(log t+2)/r),                              (10)

as claimed in (1). Finally, polar integration reduces Lp integrability to

    integral_0^R r^(1-p)(log log(1/r)+2)^p dr < infinity

for every 0<p<2. With t=log(1/r), this is an integral of exp(-(2-p)t)(log t+2)^p on a half-line. Its exponential factor proves convergence. No estimate at p=2 follows from this upper bound alone.

## 5. Lifting to the full carrier system for arbitrary omega

On a relatively compact section disc set

    j=|det(sigma_1,sigma_2,X(sigma))|>0,
    beta_i=X(sigma).sigma_i/|X(sigma)|^2,
    b=kappa beta.

All coefficients are smooth, with bounded derivatives of each fixed order and positive lower bounds for j and |X(sigma)| after restricting the disc. Use the w just constructed for this b, and define

    v=w/j, h=-beta.v,
    Phi(y,t)=exp(tA)sigma(y),
    V(Phi(y,t))=exp(-t) D Phi(y,t)(v(y),h(y)).                 (11)

The inverse function theorem gives a smaller product D_R times (-t1,t1) on which Phi is a diffeomorphism onto an open set U. The set U avoids zero because exp(tA) is invertible and sigma avoids zero.

The coordinate vector field X is partial_t, so (11) implies [X,V]=-V and

    DV X=AV-V=-LV.

The linear map exp(tA)=exp(ct)exp(-omega tJ) is a scalar times an orthogonal map. Thus X(Phi).V(Phi) equals exp((2c-1)t) times X(sigma).(sigma_i v_i+hX(sigma)), which is zero by the definition of h. The volume density is exp(3ct)j. Hence

    div V=exp(-t)j^(-1)[div_y(jv)+kappa j h]
         =exp(-t)j^(-1)[div w-kappa beta.w]=0.                 (12)

This checks all three equations of (C).

The factors in (11) and the inverse coordinate map are smooth. Every derivative of v and h at zero vanishes. Differentiating (11) in y and t therefore shows that V is flat along the whole central orbit segment, in particular at x1. If y!=0, w(y)!=0, hence v(y)!=0. The invertibility of D Phi makes V(Phi(y,t))!=0. The zero set in this flowbox is exactly the central orbit segment.

On the compactly contained section, the linear map (v,h)->sigma_i v_i+hX(sigma) and its inverse are uniformly bounded. Since j is bounded above and below and h=-beta.v,

    C^(-1)|w|<=|V(sigma)|<=C|w|.

Differentiating (11) once, including the inverse coordinate map, gives

    |W(sigma)|+|V(sigma)|<=C (|Dw|+|w|).

All constants are uniform on the smaller section; t derivatives in this estimate are smooth matrix multiples of v and h, so they introduce no uncontrolled derivative. With |X(sigma)| bounded, (10) now gives (2). This also gives |W|/|V| in Lp for every 0<p<2 in this local construction. Neither claim uses a global flow or behaviour at infinity.

## 6. Independent check of the submitted C69 construction

The pinned C69 source is read in full. For omega=0, beta=d(log|sigma|)/c, while c=1/3 gives kappa=0. In either case kappa beta=d tau with smooth tau. Choose the radial stream function psi(y)=integral_0^|y| g(s) ds. The submitted field

    jv=exp(tau)(-partial_2 psi,partial_1 psi), h=-beta.v

satisfies div(jv)=kappa beta.(jv) by the product rule and equality of mixed derivatives. The lift (11) then satisfies (C) by the exact calculations in Section 5. Smooth flatness follows from the Section 2 derivative bounds and radial differentiation. On the punctured disc |grad psi|=g, and

    |D2 psi|<=|g'|+g/r=(log t+2)g/r.

Bounded section matrices give the stated lower bound on |V| and upper bound on |W.X|, either from the C67 circulation equation or the direct coordinate derivative estimate above. Thus every step of the main C69 theorem is valid at its exact stated parameters. Its inverse-flowbox argument and all finite-time uses are local and complete.

The statement in C69 Remark 1 that kappa beta is not exact on an open transverse section when omega!=0 and c!=1/3 has the previously checked scope: there is no single integrating factor that converts the equation to divergence freedom for every local solution. It does not prevent solving the quotient equation by a correction of a selected vector field. Construction (4) does precisely that. Therefore C69's unresolved all-omega sharpness question is a new question answered by Sections 2-5, not a consequence that was already established by C69.

No numerical residual, symbolic test, or referee assertion is used as a proof. The C69 submission is the existing model C contribution. The coordinator independently checked the exact Volterra formula, all-order polar derivative argument, ratio estimate and carrier lift in the team records, a comparison of the submitted sketch. That complete comparison was read; it is not described as a full reading of this later six-section proof. The complete independent proof has been read and checked separately. Actual model-provider execution is not independently attested.
