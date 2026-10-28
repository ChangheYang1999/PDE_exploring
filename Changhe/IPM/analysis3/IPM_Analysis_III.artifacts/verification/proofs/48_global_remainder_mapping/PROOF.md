# Global boundedness of the Taylor-subtracted remainder coupling

## Statement and hypotheses

Fix a=17/4, eta=5/4 and 0<k<1. Put p=x^2 y and

 R=L2_P(w dX),
 w=|x|^(-2a) W(r),  W(r)=max(1,r)^(2a-eta),
 d(R0)=R0^3 for R0<=1 and R0^k for R0>=1.

The notation R0 below is a positive scale, not the Hilbert space R. Assume rho=p b(log r,theta), with the prescribed parity, satisfies both of the following explicit regularity conditions.

(B1) The angular and first radial derivative bounds (1) of proof 47 hold. In particular the C2 angular norms of b-1 and b_t are O(r^2) near0, and the corresponding norms of b and b_t are O(r^(k-3)) at infinity. Three angular derivatives of b are included.

(B2) There is a finite constant M5 such that for every R0>0 the function X -> rho(R0 X)/d(R0) has C5 norm at most M5 on the fixed closed annulus 1/32<=|X|<=32. One-sided fifth derivatives, uniformly bounded and with the lower derivatives continuous, also suffice for the Taylor estimates used below.

These are qualitative coefficient hypotheses, not numerical bounds. The selected finite modal trial satisfies them: its inner correction is O(r^5) with the corresponding annular derivative bounds, its leading outer order is r^k, and its radial spline joins have the needed regularity. The failure of a fifth derivative at the single point0 does not violate (B2).

For smooth parity-preserving h supported away from0 and from the vertical axis, define T_h(y)=U2[h](0,y) and

 gamma_U[h](t)=(A+A') T_h(r)/r-2A T_h'(r),
 A(t)=rho2(r)/r, rho2(y)=lim_(x->0)rho(x,y)/x^2.

Define the radially lifted remainder

 D h=U[h].grad rho-p gamma_U[h](log r).                    (1)

Then D extends to a bounded operator R->R. More precisely it is the sum of a bounded operator D_near and a Hilbert-Schmidt operator D_far. If P_j restricts output to 2^j<=r<2^(j+1), then

 ||P_j D_near h||_R <= C d(2^j)/2^j
              ||1_{2^(j-3)<r<2^(j+3)}h||_R.             (2)

Here C is finite and depends only on the specified coefficient bounds, a, eta and k. No numerical value for C is asserted. Thus the origin and infinity tails of D_near tend to zero in operator norm.

Let chi0 be the cutoff from proof 46. The actual normalized remainder

 C_R h=[U[h]+chi0(c[h]/3)X].grad rho-E Gamma_h             (3)

also extends boundedly R->R, because C_R-D is bounded rank one. Together with topics46 and47, this proves the full mapping hypothesis (E0), and the boundedness part of (E-G), on the spaces of proof 44. This theorem alone does not prove the Garding inequality.

## Canonical velocity and density of the core

The weight is bounded below on each bounded set, so h in R belongs to L2 locally. Also

 integral_{|Z|>1}|Z|^(-4)w(Z)^(-1)dZ<infinity,

because eta<2. Thus the far part of the velocity kernel is absolutely integrable against h, by Cauchy-Schwarz. The local part is the ordinary L2 singular integral. This defines the canonical velocity as a local distribution without adding harmonic fields. Smooth parity-preserving functions supported away from the axis and0, with compact support, are dense in R. All estimates below are first proved for this core.

The two velocity components have unweighted L2 operator norms at most1 by their explicit Fourier multipliers. Off the diagonal their real kernels are

 K1(X)=-x y/(pi r^4),  K2(X)=(x^2-y^2)/(2 pi r^4).

The local point mass in K2 is included in the L2 operator. It never occurs in the separated-source calculations below.

## Comparable scales

Fix R0=2^j, output annulus A_j={R0<=r<2R0}, and input h_j=1_{B_j}h with B_j={R0/8<r<8R0}. On B_j and on A_j the factor W(r) is comparable to W(R0), with constants independent of j. The input is supported in |x|<8R0. The output is split into

 the axis wedge: |x|<=r/2,
 its complement: |x|>r/2.

Parity allows the proof to be given for x,y>0.

On the complement of the wedge, the output weight is bounded above by C W(R0) R0^(-2a), and

 ||h_j||_2<=C R0^a W(R0)^(-1/2)||h_j||_R.

The ordinary L2 velocity bound and |grad rho|<=C d(R0)/R0 therefore give

 ||1_{A_j,|x|>r/2} U[h_j].grad rho||_R
                    <=C d(R0)/R0 ||h_j||_R.              (4)

We must also subtract the radial jet there. Direct kernel Cauchy-Schwarz, after scaling (s,v)=R0(S,V), gives for y comparable to R0 and j0=0,1,2

 |T_hj^(j0)(y)| <= C R0^(a-1-j0) W(R0)^(-1/2)||h_j||_R.  (5)

Indeed the input is in a bounded scaled annulus and the only kernel singularity is at S=0,V=y/R0. Its squared integral against |S|^(2a) is finite exactly when a>j0+1; this holds for all three values. The coefficient estimates from (B2) give

 |gamma_U[h_j](log y)|+|partial_t gamma_U[h_j](log y)|
           <=C d(R0) R0^(a-5)W(R0)^(-1/2)||h_j||_R.      (6)

For clarity, gamma contains T/r and T', multiplied by A and A'; differentiation in t adds r T'' and derivatives through A''. These all have the same scale in (6). The C5 annular bound controls those coefficients. Multiplying (6) by p and integrating over the complement of the wedge yields the same bound as (4).

Inside the wedge, y is between sqrt(3)R0/2 and2R0. On the region |x|<8R0 with these y values, Taylor expansion in x gives

 rho_x=2x rho2(y)+x^3 r1(x,y),
 rho_y=x^2 rho2'(y)+x^4 r2(x,y),

 with |rho2|<=C d(R0)/R0^2,
      |rho2'|<=C d(R0)/R0^3,
      |r1|<=C d(R0)/R0^4,
      |r2|<=C d(R0)/R0^5.                                (7)

The segments used in this Taylor formula stay in the fixed scaled annulus of (B2), because y is comparable to R0. The uniform derivative count is at most5. Apply the verified strip estimate in proof 23 with strip radius8R0 to h_j. Its coefficients need only be bounded on the output y interval, since the output norm is restricted there. Equations (7) imply

 ||1_wedge [U[h_j].grad rho
             -x^2(-2rho2 T_hj'+rho2' T_hj)]||_R
                  <=C d(R0)/R0 ||h_j||_R.                (8)

This uses the same factor W(R0) on input and output, up to the fixed comparison constants.

The jet subtracted in (8) is x^2 y gamma_U[h_j](log y), whereas (1) uses log r. Their difference is bounded by (6) and

 |log r-log y|=-log(sin theta)<=C cos(theta)^2

on the wedge. The square of p cos(theta)^2 is integrable against the angular weight because

 integral_0^(2pi)|cos(theta)|^(8-2a)sin(theta)^2dtheta
                    =2 B(1/4,3/2)<infinity.              (9)

Scaling the radial integral over A_j then gives again C d(R0)/R0 ||h_j||_R. This proves (2). Each input point belongs to at most7 sets B_j; the A_j are disjoint. Also d(2^j)/2^j<=1. Summing squares proves boundedness of D_near. The same argument with j restricted to either end proves its stated vanishing radial tails.

## Separated scales: preparation

For each output annulus, the remaining inputs have |Z|<=R0/8 or |Z|>=8R0. Thus they are separated from both X and the lifted axis point (0,|X|). The operator is an ordinary integral kernel there. Reduce to input in the first quadrant by the given parity, summing the four reflected kernels with the corresponding signs. This only changes finite constants.

Write U1/x=P1 and U2/y=P2 for such a reflected kernel. These ratios extend smoothly across the axes, because U1 is odd in x and U2 is odd in y. The cofactor of U.grad rho is

 F=P1[2b+cos(theta)^2 b_t-cos(theta)sin(theta)b_theta]
   +P2[b+sin(theta)^2 b_t+cos(theta)sin(theta)b_theta].     (10)

The subtracted gamma_U is F at theta=pi/2. Hence the kernel of D is p times F-F_axis. Taylor's formula in theta gives an additional cos(theta)^2, as in (5) of proof 47. All bounds below therefore retain the factor

 q(theta)=|cos(theta)|^4 |sin(theta)|.

Its squared angular integral against |cos(theta)|^(-2a) is finite by (9).

We record two elementary kernel bounds, including their justification.

(i) Inner sources, |Z|<=r/4: the C2 angular norms of P1,P2 are at most C r^(-3). To divide by x, use direct division when |x| is comparable to r; when it is small, the segment from (0,y) to(x,y) stays a distance comparable to r from the input, so write U1/x as the integral of partial_x U1 along that segment. The same argument with x and y interchanged treats U2/y. Two angular derivatives require at most three kernel derivatives. Their bounds follow from |partial^m K_i|<=C_m distance^(-2-m).

(ii) Outer sources, |Z|>=4r: parity and div U=0 give the Taylor expansion

 U(X;Z)=c_Z(-x,y)+O(r^3 |Z|^(-5)),
 |c_Z|<=C |Z|^(-3).                                     (11)

The error, after division by x or y, has C2 angular norm at most C r^2 |Z|^(-5). To see the derivative count, the divided components are smooth even functions of x and y, their constant terms are -c_Z,c_Z, and their second spatial derivatives are bounded by third derivatives of K_i. Integrating the first and second derivatives from0 proves the stated order and its two angular derivatives. The linear coefficients have opposite signs because the reflected kernel is divergence free in the source-free disk. The quadratic velocity terms vanish by parity.

## The inner-source kernel is Hilbert-Schmidt

From (10), (B1), (i) and the angular subtraction,

 |D(X,Z)|<=C q(theta) d(r) r^(-3),  |Z|<=r/4.             (12)

The inverse-weight input volume satisfies

 integral_{|Z|<=r/4}w(Z)^(-1)dZ
       <=C r^(2a+2) for r<=1,
       <=C r^(eta+2) for r>=1.                           (13)

The second bound follows from w^(-1)<=|Z|^eta. The first follows from w^(-1)<=|Z|^(2a). For a kernel on R its squared Hilbert-Schmidt norm is the double integral of |D(X,Z)|^2 w(X)/w(Z). Equations (9), (12), (13) bound its radial integral by

 C integral_0^1 r^3 dr + C integral_1^infinity r^(2k-3)dr,

which is finite because k<1. Using the annulus-specific inner-source mask only reduces this bound.

## The outer-source kernel is Hilbert-Schmidt

For r<=1, insert (11) into (10). When b=1, the linear part gives the constant cofactor -c_Z, which cancels exactly under F-F_axis. With b-1 and b_t controlled by (B1), its remaining C2 angular norm is at most C r^2 |Z|^(-3). The nonlinear part of (11) contributes at most C r^2 |Z|^(-5). Thus

 |D(X,Z)|<=C q(theta) r^5 (|Z|^(-3)+|Z|^(-5)),
                              r<=1, |Z|>=4r.            (14)

Its squared input integral is bounded uniformly in 0<r<=1. Near input0 the worse term integrates as

 integral_0^1 s^(2a-9)ds<infinity

because a>4. At input infinity the worse term integrates as integral_1^infinity s^(eta-5)ds<infinity. Hence the output integral in (14) is bounded by

 C integral_0^1 r^(11-2a)dr<infinity,

with exponent11-2a=5/2. This is where both the exact leading cancellation and the stronger condition a>4 are used.

For r>=1, (B1) and (11) give instead

 |D(X,Z)|<=C q(theta) r^k |Z|^(-3), |Z|>=4r.              (15)

The r^2 |Z|^(-5) term is dominated by |Z|^(-3). Now

 integral_{|Z|>=4r}|Z|^(-6)w(Z)^(-1)dZ<=C r^(eta-4),

so the squared output integral is bounded by C integral_1^infinity r^(2k-3)dr. This is finite. Equations (14)-(15), including the annulus-specific mask, prove the Hilbert-Schmidt assertion for outer sources. Together with the preceding section they prove the assertion for D_far.

## Normalization and the full mapping conclusion

The difference between (3) and (1) is c[h] times the fixed function

 S0(X)=(chi0/3)X.grad rho
             -p chi0(r)(A+A'/3).

Its cofactor is chi0[(b-A)+(b_t-A')/3]. Angular Taylor subtraction gives an additional cos(theta)^2. Near0 its size is O(r^2 cos(theta)^2) by (B1), and it has compact radial support. Thus S0 belongs to R by the same r^(11-2a) integral. Proof 44 proves c is bounded on R. Therefore C_R=D+c[.]S0 is a bounded operator R->R.

Proof 46 proves Gamma:R->G is Hilbert-Schmidt. Proof 47 proves C E:B->Y is Hilbert-Schmidt. Combining them gives a bounded extension

 C:E B direct-sum R -> E G direct-sum R,

hence (E0) on Z=E B direct-sum D_R. Agreement with the canonical distributional formula follows by density, local L2 convergence of the velocity, and convergence of the trace pairings. No endpoint is supplied merely by a formal Taylor coefficient: each required remainder has been estimated in its actual target norm.

## Dependencies, verification and remaining issue

Dependencies: proof 23 (strip estimate), proof 44 (spaces and bounded strain), proof 46 (axis trace), proof 47 (jet inputs and angular subtraction). The proof is qualitative in the coefficient constants. The accompanying exact arithmetic audit checks every scaling exponent, the overlap bound used in the sum, and the two endpoint cancellations in a symbolic kernel model.

Verdict: CONFIRMED under (B1)-(B2). This establishes (E0), (E-J) and boundedness of C_R. The real-part inequality in (E-G), positive coefficient margins, injectivity, an inverse norm and nonlinear closure are still separate claims.
