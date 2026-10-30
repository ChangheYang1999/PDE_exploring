# A quantitative velocity remainder with unequal decay weights

Status: new analytic proposal, OPEN independent review. This argument is
written before its finite identity checks. It supplies a convergence
radius from explicit data; it does not supply a stationary weighted norm
budget or an existence certificate.

## 1. Two weights and the complete canonical operator

Let -5<a<-3 and a<q<0, put epsilon=q-a>0, and let g be a real centrally
odd C1 function on the plane. Assume finite constants A>0 and D>=0 satisfy

 |g(X)| <= A(1+|X|)^a,
 |grad g(X)| <= D(1+|X|)^(q-1).

Define M_g=integral Xg(X)dX, which converges absolutely since a<-3.
Use the complete canonical IPM operator

 U[g](X)=(0,-g(X)/2)+PV integral K(X-Y)g(Y)dY,
 K(Z)=(-z1 z2,(z1^2-z2^2)/2)/(pi |Z|^4).

Write log_+(x)=max(0,log x) for x>0, and log_+(0)=0. Set

 C_a=1/2+2^(3-a)+2^(a+2)/(-a)
           +2^(-a-2)/(-a-3)+2^(2-a)/(a+5),
 L_a=2^(1-a), k=D/(2^(epsilon+1) A).

Then for every r=|X|>=2,

 |U[g](X)+DK(X)M_g|
   <= A r^a [C_a+L_a(1+log_+(k r^epsilon))].                 (1)

In particular the right side divided by r^q tends to zero. The function

 J(r)=A r^(-epsilon)[C_a+L_a(1+log_+(k r^epsilon))]            (2)

is nonincreasing for r>=2. Consequently (1), divided by r^q, is at
most J(R) simultaneously for every r>=R>=2.

## 2. Proof of the two-weight estimate

The kernel has magnitude 1/(2pi|Z|^2), zero angular mean, and derivative
operator norm 1/(pi|Z|^3). Its third directional derivative is bounded
by 12|Y|^3/(pi|Z|^5). These identities follow by identifying a vector
(v1,v2) with v2+i v1 and writing K(z)=1/(2pi z^2).

Split the integral into B(X,r/2), B(0,r/2), the remainder in |Y|<=2r,
and |Y|>2r. The two open balls are disjoint. On B(X,r/2), subtract
g(X) using the zero angular mean. Put B=A(r/2)^a and
L=D(r/2)^(q-1). The segment from X to any point in this ball remains
in it, so the difference is bounded both by L|X-Y| and by 2B.
The entire principal-value contribution is therefore at most

 integral_0^(r/2) min(L,2B/s) ds
 <= 2B [1+log_+(Lr/(4B))].                                (3)

If Lr/2<=2B, the integral equals Lr/2<=2B. Otherwise split the
integral at s=2B/L to obtain equality with the last expression.
Since Lr/(4B)=k r^epsilon, (3) gives precisely the L_a term of (1).
This step requires only the weaker q-gradient weight; it does not
assume a gradient remainder with exponent a.

On the remainder in |Y|<=2r, both |Y| and |X-Y| are at least r/2.
Its area is at most 4pi r^2, giving 2^(3-a) A r^a. On |Y|>2r,
use |X-Y|>=|Y|/2 and integrate the amplitude bound to obtain
2^(a+2) A r^a/(-a). The contact term is at most A r^a/2.

On B(0,r/2), Taylor expand the kernel through order two. Central
oddness cancels the constant and quadratic integrals. The linear term
is -DK(X) times the moment inside the ball. Replacing it by M_g costs
at most 2^(-a-2) A r^a/(-a-3). The Taylor remainder is bounded by
64|Y|^3/(pi r^5), because every Taylor segment stays outside r/2.
Its integral is at most

 (128 A/r^5) integral_0^(r/2) s^4(1+s)^a ds
 <= 2^(2-a) A r^a/(a+5).

Here a>-5 is necessary for the final power integral. Summing proves
(1), including the contact term and the full moment replacement.

For k=0, monotonicity in (2) is immediate. Where k r^epsilon<=1,
J is a positive constant times r^(-epsilon). In the other region,
its derivative is

 -epsilon A r^(-epsilon-1)[C_a+L_a log(k r^epsilon)]<0.

The two expressions agree at the transition. This proves monotonicity
and the claimed limit. One coarse, completely explicit sufficient
radius for J(r)<=eta, with eta>0, is

 R>=max(2,[A(C_a+L_a(2+log_+ k))/eta]^(2/epsilon)).            (4)

Indeed log_+(k r^epsilon)<=log_+ k+epsilon log r for r>=1.
For x=epsilon log r>=0, x exp(-x/2)<=2/e<1. Multiplying this
inequality by exp(-x/2) proves (4). The sharper value J(R) can be
used directly instead; no inversion of this coarse formula is needed.

## 3. An explicit cutoff model and its harmonic error

Now suppose -5<q<-3 and b(theta)=sum b_n sin(n theta) is a finite
real odd-sine polynomial, with positive odd n only. Fix R0>=2,
L0=2R0, and set

 chi(r)=0, r<=R0;
 chi(r)=3t^2-2t^3, t=r/R0-1, R0<r<2R0;
 chi(r)=1, r>=2R0.

Then h_b=chi(r) r^q b(theta) is C1, S1, zero near the origin, and
has an absolute first moment. Let p=q+2 and define

 V_q[b]=(partial_xy,-partial_xx)
          [r^p sum b_n sin(n theta)/(p^2-n^2)] at r=1.

The denominators are nonzero because -3<p<-1 and n is odd. For r>=L0,

 r^(-q)|U[h_b](r e_theta)+DK(r e_theta)M_b-r^q V_q[b](theta)|
 <= B_b (L0/r)^(q+5),
 B_b=sum_(n>=3) |b_n|(n+1)/(2(n+q+2)).                       (5)

To prove this, the regular canonical Green formula for each density
mode f_n=chi(r)r^q b_n is

 A_n(r)=-[r^(-n) integral_0^r s^(n+1)f_n(s)ds
                  +r^n integral_r^infinity s^(1-n)f_n(s)ds]/(2n).

For n=1 its exterior value is exactly the homogeneous particular
solution plus the first-moment dipole; compensation cancels that dipole.
For every odd n>=3, n+q+2>0 and direct integration gives

 A_n(r)=b_n r^p/(p^2-n^2)+(b_n J_n/(2n))r^(-n),
 J_n=integral_0^L0 s^(n+q+1)(1-chi(s))ds,
 0<=J_n<=L0^(n+q+2)/(n+q+2).

The vector magnitude of the two indicated Hessian components of
r^(-n)sin(n theta) is exactly n(n+1)r^(-n-2). Thus its error, after
division by r^q, is at most

 |b_n|(n+1)/(2(n+q+2)) (L0/r)^(n+q+2).

All exponents n+q+2 are at least q+5>0. Their finite sum proves (5).
No density or velocity is approximated inside the cutoff transition.

## 4. Explicit hypotheses which bound the difference from the model

Let h be real C1 and S1, with finite

 H=max(sup(1+r)^(-q)|h|, sup(1+r)^(1-q)|grad h|).

Assume that, for every r>=R0 and angle,

 |h(r,theta)-r^q b(theta)| <= sum_i C_i r^(q-epsilon_i),      (6)

where the list is finite, C_i>=0, and epsilon_i>0. Choose
0<epsilon<=min_i epsilon_i and also epsilon<q+5. Put a=q-epsilon,
B0=sup|b|, G_b=sup sqrt(q^2 b^2+(b')^2), and define

 A_in=H(1+L0)^epsilon+B0(1+L0)^(-a) R0^q,
 A_out=2^(-a) sum_i C_i L0^(epsilon-epsilon_i),
 A=max(A_in,A_out),
 D=H+(1+1/R0)^(1-q)(G_b+3B0).                              (7)

Unless h and b are both zero, A>0. The difference g=h-h_b satisfies
exactly the two hypotheses of Section1 with these A,D. On r<=L0,
the h contribution to its weighted amplitude is at most the first
term of A_in. On the support of h_b in this region, r>=R0, so its
contribution is bounded by the second term. On r>=L0 use (6),
(1+1/r)^(-a)<=2^(-a), and epsilon<=epsilon_i to obtain A_out.
For its gradient, the radial cutoff obeys |r chi'|<=3 and
(1+1/r)^(1-q)<=(1+1/R0)^(1-q) on its support. Differentiating h_b
therefore gives (7). In particular no differentiated version of (6)
is assumed.

The moment-resolved stationary endpoint theorem T4-335 supplies a
specific five-term list (6) in its equation(7), provided all of that
theorem's reference, canonical velocity and stationarity hypotheses
hold. Its constants include H, H^2 and the first moment. They are
not numerically bounded by this statement.

By linearity, (1) and (5) now give, for every r>=R>=L0,

 r^(-q)|U[h](r e_theta)+DK(r e_theta)M_h-r^q V_q[b](theta)|
 <= J(R)+B_b(L0/R)^(q+5).                                 (8)

Both terms are explicit and nonincreasing in R. In the profile-specific
subspaces for which T4-402 proves |V_q[b]|<=Eprof H, this implies

 |U[h](r e_theta)+DK(r e_theta)M_h|
 <= [Eprof H+J(R)+B_b(L0/R)^(q+5)] r^q, r>=R.              (9)

Equation(9) is conditional on the stated quantitative inputs and on
that independent profile-specific theorem. It does not replace the
unknown weighted norm H by a ball norm. Nor does it improve the
reference transport term in a stationary closure inequality. Consequently
it supplies a finite-radius route for the proposed coefficient Eprof,
not an existence proof or a successful CI certificate.

## Dependencies and checks

Sections1-2 rederive the kernel estimate directly; they use no numerical
coefficient table. Section3 uses the elementary radial Green identity,
with all integrals and normalization specified above. Section4 is an
explicit consequence of its displayed input bounds. The endpoint
application depends on ../moment_resolved_tail/PROOF.md, already
independently accepted in T4-350. The additional coefficient0.583 depends
on ../profile_specific_velocity/PROOF.md, currently awaiting review.
Exact finite algebra and any campaign constants belong in data/ and
verification/. They verify arithmetic, not the missing hypotheses (6).
