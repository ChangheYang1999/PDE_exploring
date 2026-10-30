# Trading the signed L2 rate in the sharpened three-component closure

## Exact conditional statement

All functions are real on R^2, even in x and odd in y. Put U[h]=(-R1 R2 h,R1^2 h), with R_j symbol i xi_j/|xi|, J=(1-Delta)^(1/2), and omega=(1+4|X|^2)^(2/5). For positive w1,w0 define the completion of compact smooth S1 functions in

    E_w(h)^2=||omega D^2h||_2^2+w1||Dh||_2^2+w0||h||_2^2,
    X_(s,w)(h)=E_w(J^s h), 0<s<=1/1024.

Every derivative tensor is an ordered Cartesian Frobenius tensor. Let rho be a smooth S1 reference with canonical smooth sublinear velocity u, V=cX+u, L=V.D-1+U[.].D rho, and a0=rho_y(0)>0. Assume all of the following.

1. 9/5<c<37/20 and c+partial_y u2(0)=1. The coefficient fields Drho, <r>D^2rho, <r>^2D^3rho, <r>^2D^4rho, Du, <r>D^2u and <r>D^3u are bounded. For some gamma<1, |D^j rho|=O(r^(gamma-j)) for j=0,1,2.
2. With theta=ess sup (|Drho|-rho_y)/2 and

       kappa^2=[(log2-1/2)||D rho_x||_2^2+(3log2-2)||D rho_y||_2^2]/(16pi),

   the signed low rate satisfies c+1-theta-kappa>=beta_L>0.
3. Define A=[[rho_y,-rho_x/2],[-rho_x/2,0]], v=omega^2,

       M1=I-sym Du+A,
       M2=(1+c+V.Dlogomega)I-2sym DV+A,
       S=(v_xy rho_x-v_xx rho_y-v_x rho_xy+v_y rho_xx)/2.

   Require M1>=(9/10)I, M2>=(1/2)I and

       (||D^2rho||inf,||omega D^2rho||inf,||omega D^3rho||inf,
        ||omega D^2u||inf,||D(v Drho)/omega||inf,||S||inf)
          <=(3,8,10,3,28,40).

4. The sums of the separate component suprema of

       (|c|,Du,omega D^2u,omega D^3u,Drho,omega D^2rho,
        omega D^3rho,omega D^4rho)

   are bounded by (2,6,24,160,22,32,80,2048), respectively.

Use either (w1,w0,C')=(16384,262144,401) or (32768,1048576,397). If mu>0 and

    G(mu)=[[1/2-mu,-347/10,-5],
           [-347/10,w1(9/10-mu)-40,-3w1],
           [-5,-3w1,w0(beta_L-mu)]]

is positive semidefinite, then A_k=L+U[k].D has the consistent maximal-domain L2 inverse bound 1/beta_L and high inverse bound 1/beta, whenever

    beta=mu-C's-(8/5)X_(s,w)(k)/sqrt(s)>0.

Let r>0 and eta>=0 satisfy

    beta_r=mu-C's-(8/5)r/sqrt(s)>0,
    eta<=r beta_r,
    c_s r<beta_L,
    c_s r<7/10,
    c_s=1/[2sqrt(pi s(1+s))].

If the exact stationary residual F=V.Drho-rho belongs to X_(s,w) and X_(s,w)(F)<=eta, there is exactly one correction in the ball X_(s,w)(h)<=r, partial_y U2[h](0)=0, solving the stationary equation at this c. Its origin slope is positive and its fixed growing leading profile is unchanged.

These are sufficient conditional statements. A smaller signed rate can be used, but the remaining background, membership and smallness hypotheses must all be certified for the actual candidate.

## Energy and realization proof

The signed L2 decomposition and maximal transport argument of ../l2_closure/PROOF.md use the numerical value 2 only as a lower rate. With beta_L replacing 2, the same exact decomposition gives

    Re<A_k h,h>_L2 <= -beta_L ||h||_2^2.

The divergence-free transport U[k].D contributes zero. The complete Lipschitz flow and bounded coupling generate the maximal L2 semigroup with decay exp(-beta_L t); its integral gives the inverse bound.

The audited first and second derivative identities give

    -Re<D Lh,Dh> >=(9/10)a^2-6ab,
    -Re<D^2 Lh,omega^2D^2h> >=P^2/2-(347/5)Pa-10Pb-40a^2,

where P=||omega D^2h||_2, a=||Dh||_2, b=||h||_2. Add these inequalities with weights 1,w1,w0 and the signed L2 inequality. Subtract mu(P^2+w1a^2+w0b^2). The remaining lower bound is exactly the quadratic form of G(mu), so its nonnegativity proves the base high rate.

The independently audited smooth and rough commutator losses in ../sharp_l2_audit/PROOF.md are C's and (8/5)X_(s,w)(k)/sqrt(s). Their proofs use the coefficient bounds and weights, not the value beta_L. Thus the stated high energy rate follows. Smooth approximation of k converges in W^(1,infinity) after applying U. Uniform high bounds and the L2 Duhamel difference give the high semigroup as a strongly continuous restriction of the low one. The low maximal distributional domain and its Duhamel identity identify the high maximal domain. Integrating a positive high decay rate gives the high inverse, and low uniqueness proves consistency. There is no additional high-to-high nonlinear boundedness assertion.

## Normalization and nonlinear proof

The Fourier embedding gives ||Dh||inf<=c_s X_(s,w)(h). The exact contact formula, including its local term, is

    c[h]=-h_y(0)/4+(1/pi)PV integral sin(3theta)h(X)|X|^-3 dX.

At a normalized k the first-order origin expansion gives (A_k h)_y(0)=a0 c[h], while F_y(0)=0. Therefore T(k)=-A_k^(-1)F remains normalized and its norm is at most eta/beta_r<=r. The high ball is complete in the L2 metric by weak high compactness and continuity of the trace.

Subtracting the two equations gives A_k(T(k)-T(l))=U[l-k].D T(l). The low inverse, the L2 contraction of U and the gradient bound imply contraction factor c_s r/beta_L<1. Banach's theorem proves existence and uniqueness in the ball. Every other stationary correction in the ball belongs to the maximal domain because its equation is A_hh=-F, so it is a fixed point. At the origin M1>=(9/10)I and normalization give a0>=c-11/10>7/10. Thus c_s r<7/10 preserves its positive slope. The correction vanishes at infinity by Fourier integrability, preserving a fixed growing leading profile.

## Exact critical signed rates of this Gram certificate

At mu=0, the leading block B=[[1/2,d],[d,b]], d=-347/10, b=(9/10)w1-40, is positive definite for both listed weights. Its Schur complement gives the exact equivalence

    G(0)>0 if and only if beta_L>beta_crit,
    beta_crit=[25b+1041w1+(9/2)w1^2]/[w0(b/2-(347/10)^2)].

Hence a positive Gram rate exists exactly above this critical value. Continuity supplies a positive mu when G(0)>0; conversely G(mu)>=0 with mu>0 implies G(0)>0 because G(0)-G(mu)=mu diag(1,w1,w0)>0. This is a statement about this fixed sufficient Gram certificate, not the optimal decay rate of the operator.

The four-decimal phrases "down to 0.3432" and "down to 0.7602" must not be interpreted as admissible endpoints: those rounded values lie below the exact critical rates. The checker supplies outward enclosures and safe five-decimal sufficient values.

## Optional continuous optimization and scope

For fixed positive mu and C', the largest r beta_r at fixed s is achieved at r=(mu-C's)sqrt(s)/(16/5). Its value is (mu-C's)^2 sqrt(s)/(32/5), maximized at s=mu/(5C') while mu-C's>0. These are algebraic properties of the displayed sufficient inequalities. The resulting floats in the peer table are observations, not directed parameter certificates. The two rational parameter rows are checked separately with exact minors and pi>=333/106.

No global matrix lower bound or signed rate for a new candidate is proved by this parameter trade. In particular relaxing beta_L does not turn a failed original rate-two condition into a complete existence certificate. The source script and its output are frozen under source/; independent exact arithmetic is under verification/.
