# A uniform compact-error estimate for small high-space transport perturbations

## Exact statement

Let rho_bar be the exact normalized C6-joined case1 modal trial of topics15 and68, with k=1615536043799051/9007199254740992 and c_l=1/k. Put V=c_l X+U[rho_bar], with U=(-R_1 R_2,R_1^2) in the canonical full-plane convention. In cylinder coordinates t=log r, theta, write W=(V.e_r/r,V.e_theta/r). Fix

 delta=9/5, gamma=-1/2, sigma=25/4, s_min=41/20,
 b(t)=exp(3t)a(t), p(theta)=cos(theta)^2 sin(theta), beta=b'/b,

where a is the fixed smooth positive weight of proof 123. Thus b=exp((3+delta)t) sufficiently far left and b=exp(gamma t) sufficiently far right. Choose specifically the smooth repeller-block order s of proof 130, rather than an arbitrary order merely satisfying W.grad s>=0. It is reflection invariant, s_min<=s<=sigma, and equals sigma on an open neighborhood of the fixed vertical sector. Proof 152 proves

 W.grad s>=kappa_s |grad s|, kappa_s>0.                  (1)

Use the fixed cutoffs of proof 123; enlarging a vertical cutoff inside the region s=sigma changes only equivalent norms. Define X_s to be the even-x, odd-y functions h for which

 v=h/b belongs to H^{s(.)}(R times S1),
 u=chi h/(b p) belongs to H^sigma(R times S1),
 u(t,pi/2)=u(t,3pi/2)=0.

The norm is the square sum of these two Sobolev norms. Let G_s be the coefficient input space of proof 155: g=J x^2 y chi_0(t)+b v_g with v_g in H^{s(.)} and chi_1 v_g/p in H^sigma, of the same parity, with no zero-trace condition. Its norm is |J|+||v_g||H^s+||chi_1 v_g/p||H^sigma. The inner cutoff chi_0 is one sufficiently far left and zero sufficiently far right. The larger angular cutoff chi_1 is one near supp chi, within the constant-order region.

For g in G_s set

 B_g=(U[g].e_r/r,U[g].e_theta/r)+(c[g]/3,0),
 T_g h=(V+U[g]+c[g] X/3).grad h-h,
 S_g=T_g+C_R,
 D_g={h in X_s:T_g h belongs to X_s in distributions}.    (2)

Here c[g]=partial_y U_2[g](0), and C_R is the fixed normalized remainder coupling of proof 123, computed from rho_bar. In particular this is a transport perturbation with fixed coupling; it is not a claim about replacing grad rho_bar by grad(rho_bar+g). Give D_g its maximal graph norm. At g=0 these are the actual T,S,D_s of proof 149.

Let epsilon=1/5120. For every finite L>=0 there are numbers r_*>0, C<infinity, a Hilbert space W_*, and a compact linear map K:X_s->W_*, all independent of g and lambda, such that

 ||h||X_s<=C||(S_g-lambda)h||X_s+||Kh||W_*,
 h in D_g, ||g||G_s<=r_*, 0<=lambda<=L.                 (3)

There is also a uniform intermediate estimate

 ||h||X_s<=C_1[||(S_g-lambda)h||X_s
             +||h||X_(s-epsilon)+||J_*h||X_s],          (4)

with a fixed compact J_*. The lower space reduces both the variable bulk order and the cofactor order by epsilon and retains the same closed trace condition. Constants and the radius are qualitative. No numerical inverse bound or injectivity is asserted here.

## Coefficient bounds and the logarithmic sign

Proof 155 gives a decomposition B_g=c[g] E+Z_g, with E fixed, smooth and bounded with all bounded derivatives, and

 |c[g]|+||Z_g||H^s+||B_g||C_b^(1,alpha)
 +||chi_2 Z_g||H^sigma+||chi_2 Z_(g,theta)/cos(theta)||H^sigma
 <=C_alpha||g||G_s,                                    (5)

where Z_(g,theta) is the angular component of Z_g. Here alpha may be any number below1/20 and chi_2 is any of the nested output cutoffs needed below. The input cutoff can be enlarged without changing the space, since s=sigma between the cutoffs and p is bounded away from zero there.

Take alpha=1/40. By (1) and the supremum bound in (5), decreasing r_* if necessary gives

 (W+B_g).grad s>=0                                     (6)

for every allowed g. Its C^(1,alpha) norm is uniformly bounded. Proof 153 therefore gives a uniform lower bound for its logarithmic quadratic form with an H^(-1/2560) remainder. Proof 157 compares the square sum of these negative norms to X_(s-epsilon); our epsilon=1/5120 is smaller than that available gain.

We also need elementary product estimates. For positive smooth bounded order s, the same Bony decomposition and moderate weights as proof 156 give

 ||f v||H^s<=C(||f||infinity||v||H^s+||f||H^s||v||infinity).

For the high-high terms use the summable factor 2^(-(k-j)s_min); for the low-high terms use the uniform L-infinity norms of the low cutoffs. The identical proof applies to s-1, whose minimum is21/20>0. Since H^s embeds into W^(1,infinity), these estimates and (5) imply

 ||B_g.grad v||H^(s-1)<=C||g||G_s ||v||H^s,             (7)
 ||beta B_(g,r) v||H^s<=C||g||G_s ||v||H^s.             (8)

The fixed smooth component is treated as a multiplier. In the vertical sector the same statements hold at order sigma and with the scalar coefficient

 d_g=beta B_(g,r)+(p'/p) B_(g,theta).

This follows from p'/p=-2tan(theta)+cot(theta) and the divided angular bound in (5). Extend these vertical coefficients with a larger smooth cutoff before applying a constant-order estimate. They agree with the original coefficients near supp u, so the equation is unchanged. No global H^sigma bound for the bulk velocity is assumed.

## Perturbed dyadic energy

Use the reductions A_j from proof 157 and write w_j=A_j v. The perturbation identity is exact:

 A_j(B_g.grad v)
 =B_g.grad w_j-N(B_g.grad Lambda)w_j
  -(B_g.grad s) A_j log<D>v
  +sum_l[A_j,B_(g,l)]partial_l v.                      (9)

Proof 156 bounds the square sum of the last terms by C||g||G_s||v||H^s, using H^s into W^(1,infinity). The difference between A_j log<D>v and log<D>w_j is a relative-order-minus-one smooth commutator, bounded in the square sum by the lower norm as in proof 157. Integration by parts in B_g.grad contributes div B_g/2, and the escape term contributes N B_g.grad Lambda. Both have supremum norm at most C||g||G_s. The zeroth-order term is bounded by (8).

Add (9) to the fixed-background dyadic energy of proof 157. Its logarithmic coefficient is now exactly (W+B_g).grad s; (6) and the preceding positive-form bound permit its disposal with a uniform lower-norm remainder. The unchanged background matrix is still the matrix of proof 142. All other new bulk energy terms have absolute value at most

 C||g||G_s ||v||H^s^2+C'||h||X_(s-epsilon)||h||X_s.      (10)

The second constant can be chosen uniformly for ||g||G_s<=r_*; it need not be small. The cofactor order is constant, so its logarithmic term vanishes. Its velocity is localized to a larger vertical sector as described above, and the constant-order instance of proof 156 and (5) give the same bound there.

The cofactor cutoff forcing is ((W+B_g).grad chi)v/p. It is supported where p is bounded away from zero and s=sigma. Its norm is at most C_chi||v||H^s, with one constant for the whole small ball. Thus the coupling from bulk to cofactor remains triangular. There is no cofactor-to-bulk term of this type.

## The penalty and absorption

Fix mu=1/2, and then N,L_0 and the background matrix margin from proof 142, before choosing the radius. The dyadic penalty estimate (8) of proof 157 and the equation give, for every a>0,

 (sum_j ||W.Rw_j||_2^2+||W.Rz_j||_2^2)^(1/2)
 <=C F+(a+C_2||g||G_s)H+C_a Y,                        (11)

where F=||(S_g-lambda)h||X_s, H=||h||X_s, Y=||h||X_(s-epsilon), and z_j is the cofactor reduction. In deriving (11), the fixed C_R is bounded on the lower space by proof 146. The new first-order term uses (7). The zeroth-order terms and the bounded interval of lambda contribute only to C_aY or a small multiple of H. The cutoff term in the penalty is measured at order sigma-1, so it is also controlled by Y. Consequently C and C_2 can be fixed independently of a and g.

The two energy inequalities now have exactly the form of (3)-(4) in proof 149, with the added high error C_3||g||G_s H^2 and the replacement a by a+C_2||g||G_s in the squared penalty. The compact error map comes only from the fixed background coupling. Choose the fixed approximation errors and a small enough for the triangular absorption in proof 149. Then choose r_* small enough both for (6) and for all new high errors to fit within the remaining absorption margin. The overlap constant was already bounded uniformly on this ball. This proves (4), with a fixed compact J_* and constants independent of g and lambda.

## Exact maximal domain

For h in D_g the bulk and cofactor distributional equations hold by their definitions. Each fixed A_j v and constant-order A_j u belongs to every finite ordinary Sobolev space, as proved in proof 157. Thus integration by parts against W+B_g, which is bounded and Lipschitz on the cylinder, is legitimate. Formula(9) holds by distributional approximation, with its coefficient commutator in the square-summed L2 space by proof 156. The cofactor forcing is in H^sigma, and the extended divided scalar coefficient has the bounds already checked.

Sum through a finite frequency index. All nongraded terms are controlled by the square-sum estimates. Bound each logarithmic form from below, discard its positive part, and pass to the full sum; its negative remainders are summable by (2) of proof 157. This proves (4) on D_g itself. Smooth density in X_s is not being used as a substitute for graph density. D_g is closed because convergence in X_s implies local distributional convergence and T_g has fixed bounded Lipschitz coefficients for each g.

The parity and trace requirements are compatible with this domain. The angular component B_(g,theta) vanishes on both axes, and near the vertical axes B_(g,theta)/cos(theta) is continuous. For a zero-trace even cofactor u, its tangential trace derivative is zero and its normal first derivative is zero. Consequently the transport does not create a new cofactor trace. This also follows by its tangent flow. The fixed C_R has zero cofactor trace by proof 123.

## Uniform removal of the lower norm

Put N_0(h)=||h/(b cos^4(theta))||L2. Proof 139 proves, on these fixed spaces,

 Y<=eta H+C_eta N_0(h),                                (12)

and compactness of every radially localized map into the lower space and into N_0. Its double-Hardy proof uses the even zero-trace cofactor and remains unchanged.

The actual background N_0 transport energy has a strictly positive coefficient on sufficiently distant radial ends. For the perturbed field the change in that coefficient is exactly

 (div B_g)/2-beta B_(g,r)+4 B_(g,theta) tan(theta).       (13)

It has supremum norm at most C||g||G_s, by (5); away from the vertical sector there is no singular denominator. Shrinking r_* retains, for example, half of the fixed end margin. This bound is global in angle and requires no decay of the central strain.

The full output tail of the fixed C_R into N_0 tends to zero by proof 138. The end energy argument of proof 139 therefore works with the same large radial cutoffs and constants for every allowed g. It is valid on D_g without using an unproved high-space flow theorem. The differentiated double-Hardy formula in proof 139 places z=h/(b cos^4) in H1: it uses three cofactor derivatives and one bulk derivative, both available here. Its transformed equation has a bounded Lipschitz transport field and the bounded scalar coefficient (13). Ordinary L2 integration by parts, with radial cutoffs and then their limit, therefore gives the required energy identity. There is no axis boundary term because the double quotient is in H1 and the angular field is tangent to the axis. The radial cutoff commutator has coefficient q+B_(g,r), uniformly bounded. Its N_0 norm is bounded by a fixed constant times the N_0 norm of h on a fixed compact radial set. Thus its compact map can be chosen independently of g.

Insert (12), first absorb eta H, and then absorb the fixed small coupling tail exactly as in proof 139. The remaining terms are F, the fixed compact J_*h, and radially localized lower and N_0 norms. Take their finite direct sum, with the fixed scalar factors, as K. This proves (3).

## Scope

The result is a uniform a priori estimate on the exact, possibly varying maximal domains D_g. It avoids the false bounded perturbation from D_0 with its first-order graph norm. It applies to the frozen-coupling transport operator in (2), which is the one used in the proposed quasilinear iteration. It does not prove a numerical radius, a complement inverse, an inverse norm, or injectivity. Generation and a Fredholm consequence for these rough perturbed domains require the additional argument in the next topic.
