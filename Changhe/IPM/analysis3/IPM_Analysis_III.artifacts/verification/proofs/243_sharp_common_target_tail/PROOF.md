# Sharp decay of the full moving-tail coupling on the common Holder targets

## Exact statement

Fix the actual exactly joined and normalized case1 modal trial rho0 and its canonical full-plane velocity. Let k=1615536043799051/9007199254740992 and p=2k-1. Fix0<alpha<1. The space E2 consists of bounded continuous functions h, even in x and odd in y, with h(0,y)=0 and norm

 ||h||E2=||h||infinity+[h]_x+[h]_(y,2),
 [h]_x=sup |h(x,y)-h(x',y)|/|x-x'|^alpha,
 [h]_(y,2)=sup |h(x,y)-h(x,y')|/(|x|^2 |y-y'|^alpha).

For every gamma>4k put

 Y_gamma=E2 intersect L2((1+r^2)^(-gamma/2)dX),
 ||h||Y_gamma=||h||E2+||h||L2((1+r^2)^(-gamma/2)dX).

Let C0h=U[h].grad rho0+c[h]M0 be the complete moving-tail coupling of topics217 and226. Here M0=H0+m0 is the exact chart column, with the canonical tail derivative and the same scalar normalization as those topics. Let chi_* be any fixed smooth radial cutoff equal1 on B1 and0 outside B2, and beta_R(X)=1-chi_*(X/R).

There exist constants0<c_alpha<=C_alpha<infinity and R_alpha>=e, depending only on the displayed alpha, the fixed trial, norm and cutoff, such that for R>=R_alpha,

 c_alpha R^p log R <= ||beta_R C0||_(E2->E2)
                            <= C_alpha R^p log R.            (1)

For every fixed gamma>4k there likewise exist0<c_(alpha,gamma)<=C_(alpha,gamma)<infinity and R_(alpha,gamma)>=e such that

 c_(alpha,gamma) R^s_gamma log R
       <= ||beta_R C0||_(Y_gamma->Y_gamma)
       <= C_(alpha,gamma) R^s_gamma log R,
 s_gamma=max(2k-1,2k-gamma/2).                              (2)

These constants are qualitative, not numerically certified. In particular the rate R^(k-1)(1+log R) is impossible for the full C0 in either target. Every exponent in(1)-(2) is negative. The full output tails still tend to zero. These statements concern C0 on the whole indicated input space, not its restriction to ker c. They do not assert a global inverse or a parametrix estimate.

## Exact nonzero logarithmic coefficient

Proof 222 equations(10)-(13), independently audited with its binding clarifications, give the uniform angular expansion

 M0(r,theta)=r^p log(r) S_M(theta)+O(r^p),
 S_M=-2k^2 Q_k/n'_0, n'_0>=3.                              (3)

The finite trigonometric polynomial S_M is not zero. More precisely its sin(1043theta) coefficient equals

 k^2(521-k)a_521^2/[2n'_0(521+k+2)]>0,
 a_521=exp((3-k)t_plus) Aout[259,0]/8,
 Aout[259,0]=-8059128652303703/10384593717069655257060992658440192.

The coefficient is an exact original-data identity, not a rounded observation. The low-mode normalization repair cannot change it. The O(r^p) bound in(3) is uniform in theta. It follows from the finite homogeneous interaction and the faster remainder O(r^(3k-2)(1+log r)); the latter is O(r^p) since k<1. Thus there is a closed angular interval I of positive length and b>0 such that |S_M(theta)|>=2b on I. Choose I away from the axes if necessary; a nonzero trigonometric polynomial cannot be supported only on finitely many angles.

## One fixed admissible input detects the column

Choose a nonnegative smooth bump supported in a sufficiently small disk about the point of polar radius1 and angle pi/6, add its even-x and odd-y physical reflections, and call the result q0. The disks can be chosen disjoint and away from both axes and the origin. The strain kernel is

 K(X)=sin(3theta)/(pi r^3)=y(3x^2-y^2)/(pi r^6).

It has the same parity as q0 and positive product Kq0 on all four disks. Hence its absolutely convergent integral c[q0] is strictly positive. Put q=q0/c[q0]. Then q is smooth and compactly supported, has physical parity, c[q]=1 and J(q)=0.

The function q belongs to E2 and every Y_gamma above. Its support has positive distance from x=0; therefore the x^(-2) vertical seminorm is bounded wherever q is nonzero, and the crossing differences are bounded by the ordinary smooth extension. Its transport image Tq=(ell0 X+U[rho0]).grad q-q has the same compact support and is at least C1, so it belongs to these spaces as well. Thus q is even in their exact maximal transport and full domains, the latter by the bounded coupling theorem of proof 226. Domain membership is not required merely for the bounded operator norm, but it rules out use of an inadmissible test perturbation.

Parity gives integral q=0. The order-zero canonical velocity kernel and its separated derivatives have homogeneity-2,-3,..., so its expansion outside the fixed support gives U[q]=O(r^-3). The constant term vanishes by the zero mass. Since grad rho0=O(r^(k-1)),

 C0q=M0+O(r^(k-4)).                                      (4)

Because k-4<p, (3)-(4) imply that for sufficiently large r and all theta in I,

 |C0q(r,theta)|>=b r^p log r.                             (5)

All constants here are for the same fixed input q. Its normalization does not depend on R.

## Lower bounds in both norms

For r>=2R, beta_R=1. Taking r=3R at any theta in I in(5) and using the supremum term of E2 gives

 ||beta_R C0q||E2 >= b 3^p R^p log R.

After division by ||q||E2 this proves the lower bound in(1).

For the weighted part, integrate(5)^2 over 2R<=r<=3R and theta in I. For R>=1, the weight is at least10^(-gamma/2)R^(-gamma), and r^(2p)>=3^(2p)R^(2p) because p<0. The polar area is(5/2)|I|R^2. Hence

 ||beta_R C0q||L2(w_gamma)
   >= b 3^p 10^(-gamma/4) sqrt(5|I|/2)
                         R^(p+1-gamma/2) log R.           (6)

The E2 lower bound and(6), divided by the fixed finite ||q||Y_gamma, give a positive multiple of R^max(p,p+1-gamma/2) log R. This is the lower bound in(2), including gamma=2. No equivalence between E2 and Y_2 is assumed.

## Matching upper bounds and scope

The complete target-tail estimate of proof 226 is

 ||beta_R C0||_(Y_gamma->Y_gamma)
 <=C[R^(k-1)+R^(k-gamma/2)+R^p+R^(2k-gamma/2)](1+log R),

and the E2 estimate omits the two weighted terms. Since k>0, k-1<p and k-gamma/2<2k-gamma/2. For R>=e, 1+log R<=2log R, so these estimates reduce to the upper bounds in(1)-(2). Their exponents are strictly negative because k<1/2 and gamma>4k.

Finally p-(k-1)=k>0 and s_gamma>=p. The lower bounds divided by R^(k-1)(1+log R) therefore grow at least as a positive multiple of R^k. No uniform constant can give that faster rate for C0. The earlier rate for Cren=U[.].grad rho0+c[.]H0 in the corresponding earlier scope is unaffected: H0 is compact, and the nonzero M0 logarithmic column is absent there.

This is a precise tail statement on already obstructed common Holder targets. It supplies no inverse, no complement certificate, no profile existence or nonexistence, and no new certified number. The argument is entirely analytic. Dependencies are proof 213 for the spaces and exact kernel, proof 217 for the exact column, proof 222 with its binding clarifications for the nonzero far coefficient, and proof 226 with its binding audit clarifications for the full upper bounds. An actual independent review is requested before adopting the new two-sided rates as a theorem.
