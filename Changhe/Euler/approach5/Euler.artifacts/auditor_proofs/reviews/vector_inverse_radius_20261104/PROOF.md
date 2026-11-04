# Independent audit of the strict vector inverse-radius threshold

Status: independent reconstruction complete; existing configured model comparison and designated verdict pending. Source: in the team records, submitted SHA256 d2aaab4ab1d683ab2d91a7829a1122c80f9b04f60dbbfa5c617a2e96a6828a69. The captured source and all37 manual checks were read in full. All assertions concern finite-dimensional complex vectors with Euclidean norm.

## 1. Exact claims and dependencies

Let O be a connected open subset of C containing0, write dbar=(partial_x+i partial_y)/2, and let N be a positive integer. If u belongs to H1_loc(O;C^N), |dbar u|<=C|u|/|z| almost everywhere, and0<=C<1/4, then infinite L2 integral order at0 implies u=0 almost everywhere on O. Infinite order means r^(-L) integral_B(0,r)|u|^2 ->0 for every L>0.

Conversely, for each C>1/4 there is R>0 and a smooth map u:B(0,R)->C^2 that is nonzero off0, flat to every derivative order at0, and satisfies that inequality off0. The coefficient b=C/|z| has weak-L2 quasi-norm K2(b)=C sqrt(pi) and high-tail limit lim_s s^2 area{b>s}=pi C^2. Assigning b(0)=0 makes the inequality valid at0 as well.

The proof below uses the fundamental theorem of calculus, Fourier Parseval on the circle, H1 approximation on compact annuli, elementary cutoff estimates and Fatou's lemma. It imports no endpoint continuation theorem. It does not decide equality C=1/4; that separate submission is audited elsewhere. The infimum of inverse-radius constants allowing a smooth vector counterexample is1/4, irrespective of that equality question.

## 2. Construction and seam compatibility

Put epsilon=C-1/4. Choose smooth nondecreasing chi on[0,1], identically0 near0 and1 near1, and M=sup chi'. Then M>=1 and is finite. Choose L>=pi M/(4epsilon). For each integer n>=1 and t in[nL,(n+1)L], define theta=(pi/2)chi((t-nL)/L), so0<=theta'<=2epsilon. Define F(L)=0 and F'=n+sin^2 theta there.

Both definitions of F' at the seam (n+1)L are identically n+1 on a full neighborhood. Consequently integration defines a smooth F with a single common value at the seam, and all its derivatives match. On t>=L,

    t/L-1 <= F'(t) <= t/L+1,
    F(t) >= t^2/(2L)-t+L/2.

All derivatives F^(j) with j>=2 are uniformly bounded: within each interval they differentiate a fixed translated function, and that function is constant near the seams.

Let j_n=1 for even n and2 for odd n. For z=r exp(i phi), t=-log r>=L, put

    u(z)=exp(-F(t))[cos(theta)exp(in phi)e_(j_n)
                       +sin(theta)exp(i(n+1)phi)e_(j_(n+1))].

Integer frequencies make the formula single-valued. Orthogonality of the two components gives |u|=exp(-F)>0. Near the seam only mode n+1 survives, in the same component on either side. Since F=(n+1)t+d_n on that neighborhood, the formula is exactly exp(-d_n)z^(n+1)e_(j_(n+1)). Thus the infinitely many seams are holomorphic neighborhoods, not merely matched boundary values.

## 3. Exact residual and the coefficient

In these coordinates,

    dbar=exp(i phi)(-partial_t+i partial_phi)/(2r).

After removing the unit phases of the two components, write w=(cos theta,sin theta), D=diag(n,n+1). The amplitude residual is (F'I-D)w-w'. Since F'=n+sin^2 theta,

    (F'I-D)w=-sin(theta)cos(theta)(-sin theta,cos theta),
    w'=theta'(-sin theta,cos theta).

The norm is therefore theta'+sin(theta)cos(theta), exactly, not just bounded above. Restoring the envelope and phases gives

    |dbar u|/|u|=(theta'+sin(theta)cos(theta))/(2r)<=C/r.

The envelope derivative is essential to this calculation. The orthogonal components are also essential; replacing their vector norm by either scalar component would be invalid. At seams both sides agree with the holomorphic formula.

## 4. Smoothness at the accumulating center

A Cartesian derivative is r^(-1) times a bounded angular combination of partial_t and partial_phi. Iterating k derivatives produces r^(-k) times a finite sum of cylinder derivatives of order at most k with bounded angular coefficients. Angular derivatives cost powers of n+1<=2+t/L; derivatives of theta are uniformly bounded; derivatives of exp(-F) are that envelope times polynomials in F',...,F^(k). Hence, for each k, constants A_k and m_k independent of n give

    |D^k u(z)|<=A_k(1+t)^(m_k)exp(-F(t)+kt).

Multiplication by r^(-p)=exp(pt), for any fixed p>0, still leaves a quantity tending to0 by the quadratic lower bound on F. Thus every punctured derivative is o(r^p), uniformly in angle and annulus. Extend each derivative by zero at0. Induction proves that these are the actual derivatives of the extension: continuity follows from the bound, and each difference quotient at0 tends to0, using p>1. This proves smoothness and all-order flatness without any unjustified inference from the function's size alone.

For any target L0, choose p with2p+2>L0. On a sufficiently small disc, |u|<=r^p, so r^(-L0) integral_B(0,r)|u|^2 <=pi r^(2p+2-L0)->0. Nonvanishing on the punctured disc remains true.

The superlevel area of C/r on B(0,R) is pi min(R^2,C^2/s^2). This proves the claimed weak norm and tail limit. The rank-one matrix A=(dbar u)u*/|u|^2 off0, A(0)=0, satisfies Au=dbar u. Its operator and Frobenius norms equal |dbar u|/|u|, so its entries are weak-L2. No continuity of A at0 is claimed.

## 5. Compact-annular Carleman estimate

Let v be H1 with compact support in an annulus excluding0. For every half-integer lambda,

    ||r^(-lambda-1)v||_2 <=4||r^(-lambda)dbar v||_2.            (C)

For smooth v, expand the full Fourier series v(t,phi)=sum_k v_k(t)exp(ik phi). Its compact annular support is compact support in t. Parseval and dA=r^2 dt dphi give respectively

    2pi sum_k integral exp(2lambda t)|v_k|^2,
    (pi/2)sum_k integral exp(2lambda t)|v_k'+kv_k|^2

for the squares of the two norms before the factor4. Put w_k=exp(lambda t)v_k. Integration of the real cross term gives

    integral |w_k'+(k-lambda)w_k|^2
       =integral |w_k'|^2+(k-lambda)^2 integral |w_k|^2
       >=(1/4)integral |w_k|^2.

This applies componentwise and sums over every integer k. The squared norm ratio is at most16, proving(C). Smooth approximation in a fixed slightly larger annulus proves the H1 case, because both weights are bounded there. No noncompact approximation with growing weights is used.

## 6. Cutoff limits in the positive result

Fix B(0,R) compactly contained in O. Let chi0 be a smooth cutoff equal to1 on B(0,R/2), supported in B(0,R). Let eta_delta vanish on B(0,delta), equal1 outside B(0,2delta), and satisfy |dbar eta_delta|<=K/delta. Apply(C) to v_delta=chi0 eta_delta u and absorb the term 4C||r^(-lambda-1)v_delta||_2. For positive half-integers lambda,

    (1-4C)||r^(-lambda-1)v_delta||_2
       <=4(R/2)^(-lambda)A
          +4K delta^(-lambda-1)||u||_(L2(B(0,2delta))),

where A=||u dbar chi0||_2 is finite and independent of lambda. For fixed lambda, integral flatness makes the last term tend to0, using an integral exponent exceeding2lambda+2. Fatou therefore gives the same inequality for chi0 u without that term. For0<rho<R/2,

    ||u||_(L2(B(0,rho)))
       <=[4A rho/(1-4C)](2rho/R)^lambda.

Only now let lambda tend to infinity through positive half-integers. This proves u=0 almost everywhere in B(0,R/2). The order of the limits and positivity of1-4C are explicit.

## 7. Connected propagation

Let Z consist of points with an almost-everywhere zero neighborhood. It is open and contains0. If p is a relative boundary point, then p!=0. Choose B(p,2r) compactly contained in O excluding0 and a bound K on C/|z| there, with Kr<1/4. Choose a in Z with |a-p|<r/8. On B(a,r), the coefficient is at most Kr/|z-a|, and u is flat at a because a has a zero neighborhood. Section6 centered at a proves zero in B(a,r/2), which contains a neighborhood of p. Thus Z is also relatively closed. Connectedness gives Z=O. No completeness of a characteristic flow is relevant to this planar argument.

## 8. Actual-source and campaign scope

The actual Pan-Zhang arXiv2404.01947v1 PDF has SHA2560b0954e59be965e9a3456fb7c3ba019fe45c2116ecc36ffe5bd6dd08b5741249 and is retained in the adjacent Example4 audit. Printed pages19-23 were read through the complete Theorem6.1 proof, and page19 was rendered and visually inspected. Its Theorem6.1 states the strict vector H1 result used here as precedent. Its proof uses a compact outer cutoff. The noncompact negative-weight proposition has a separate scope audit; it is not needed for the valid compact-annular argument above. No other theorem on page23 is certified by this reading.

The original Pan-Wolff1998 manuscript remains unavailable in the retained literature evidence; publisher metadata or HTML is not a manuscript reading. Neither the construction nor the positive proof above imports that original. No novelty claim is made.

This counterexample refutes unrestricted weak-L2 continuation for a smooth map into two complex components. It does not refute the smooth scalar theorem or the finite-regularity scalar thresholds, because |dbar u_j|<=b|u_j| is not implied. C67 uses one complex scalar formed from two real transverse components, not two complex components. There is no real carrier, divergence condition, Euler transport, pressure or decay assertion here. The optimal universal weak-norm threshold and arbitrary-norm rough scalar continuation are separate questions. No mathematical computation was needed.

## 9. Existing model comparison and independent response

Items7-9 of the complete Theory Agent C note of 2026-11-04T04:34:34Z were read and retained. The existing configured model comparison agrees with the exact signed polar derivative, the residual (theta'+sin(theta)cos(theta))/(2r), and the holomorphic matching at both ends of every annulus. Actual provider execution is independently unattested. The finite-difference tests in that note are not independently certified or used as proof. In particular, the fixed-width estimates in Sections2-4 control every Cartesian derivative and prove a smooth extension with all jets zero, rather than only continuity.

The full angular expansion in Section5 proves the compact-annular inequality with constant4. The inner cutoff is removed at each fixed positive half-integer; only then does that half-integer increase. The strict positive statement therefore has C<1/4. This audit and this comparison alone do not decide C=1/4; the separate submitted critical audit treats it. The counterexample has two complex components and cannot be inserted into the single-complex-component carrier reduction. The unrestricted vector weak-L2 analogue is false, while an Euler quotient estimate remains absent.

## 10. Confirmed-source revision check

The exact source revisionf16d2a51213ab55f3fba9da3f5957dc210c3ca691ad61e3b3874e707e8f56c05 was compared with the submission in full. Only the opening status and an appended confirmation note change. A2922-A2923 cover the strict positive theorem and every larger-constant smooth two-complex-component example. The note correctly leaves equality to the separate349 audit and keeps the scalar, carrier and Euler conclusions distinct. No mathematical assertion changes.


## 11. Correction of the previous section's exact-hash attribution

The preceding section and A2928 quoted the earlier announced hash f16d2a51213ab55f3fba9da3f5957dc210c3ca691ad61e3b3874e707e8f56c05. The actual source retained at04:45:35Z and compared with the submission already had hash e989fc5d31edc0b5dcbba6896b1117d119f4d5b7971de73f7c56d75394307f5e, as its unchanged capture JSON proves. Thus the attribution of that exact earlier hash to that earlier file inspection was inaccurate. It does not affect the mathematics.

The earlier version has now been retrieved from the literature agent's archived04:45:25Z handoff, copied into verification, and hashed independently. The complete difference between it and the retained version is one heading: 9 C becomes 9. There is no other change. Both versions therefore preserve the same statements and proofs, and the earlier announced version is now directly checked as well. The earlier reading must not be backdated. The current live file is byte-identical to the version actually retained at04:45:35Z. The full original-to-retained difference and this one-heading difference have both been read.
