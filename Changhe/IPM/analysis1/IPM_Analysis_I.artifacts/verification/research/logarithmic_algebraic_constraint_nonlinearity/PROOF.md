# No finite algebraic linear constraints remove full-graph nonlinear discontinuity

This standalone informal proof is written before its new finite checks. Its status is OPEN until independent verification, actual Claude Opus5.5 review, resolution of objections and later own adjudication. It strengthens result210(B) by removing continuity and closedness assumptions on the finite constraints. It does not change210(A)'s inverse-constant statement.

## Setting and exact statement

Let rho be the exactly joined and canonically normalized modal_v2 density, ell=1/k, V=ell X+U[rho], and use the full-plane sublinear canonical velocity U[h]=(-psi_y,psi_x), -Delta psi=partial_x h. Define Sigma(h)=psi[h]_xy(0), and

 Lh=V.grad h-h+U[h].grad rho+(Sigma(h)/3)X.grad rho,
 Q(h)=U[h].grad h+(Sigma(h)/3)X.grad h.

For every fixed real b and finite s>=0 use

 ||h||Y=||exp((1/2-b)z)h(exp z,y)||H^s(R^2_(z,y)),
 ||h||G=||h||Y+||Lh||Y.

The unitary Fourier H^s norm has multiplier(1+|xi|^2)^(s/2). All spaces and maps are real linear. No closedness ofL, completeness of a test domain, or quantitative norm ceiling is assumed.

Take the fixed positive-quadrant smooth patches of209: nested disks B1 compactly insideB2 in a punctured inner disk, with four disjoint reflected copies ofB2. The fieldV is smooth there and admits a common smooth phase phi nearB1 with V.grad phi=0 and phi_y>1/2. LetK be the union of the four reflected openB2 disks, and

 D_cp={-Delta f: f is smooth compact, even inx, odd iny, supp(f) is compactly contained inK}.

Then h,Lh,Q(h) belong toY for everyh inD_cp. Let m>=0 be any integer and Lambda:D_cp->R^m be ANY real linear map, with no continuity assumption. PutM=kerLambda. There exist g inM and k_n inM, with constants c,C>0, such that

 ||g||G+sup_n||k_n||G<=C,
 ||U[g].grad k_n+U[k_n].grad g||Y>=cn-C.              (1)

Consequently for v_n^+=n^(-1/2)(g+k_n) and v_n^-=n^(-1/2)(g-k_n),

 max(||v_n^+||G,||v_n^-||G)->0,
 liminf max(||Q(v_n^+)||Y,||Q(v_n^-)||Y)>=c>0.        (2)

ThusQ is discontinuous at0 onM in the inherited full graph norm. For everyr>0 there is no finiteC_r with ||Q(h)||Y<=C_r||h||G^2 for allh inM with ||h||G<r. Equivalently this holds on every linear subspace ofD_cp of finite ALGEBRAIC codimension, whether or not closed. The constants and the constructed sequences may depend onLambda,m,b,s; no uniformity in those choices is claimed.

All constructed tests have compact canonical velocity and satisfy J=Sigma=all center jets=all exterior coefficients=0. HereJ is the center factor value in h=x^2y a_h; a_h is smooth compact. The normalized residual difference F(rho+h)-F(rho)=Lh+Q(h) has the same discontinuity. No statement is made for infinitely many constraints, nonlinear constraints, a weaker target, or arbitrary stronger domain norms. There is no PDE exclusion or inverse assertion.

## Canonical compact potentials and the local phase

The exact saddle derivative is DV(0)=diag(-A,D), A=2/k-1>0. Since V1(t,t)=-At+o(t), some sufficiently small positiveP=(t,t) has V1(P)!=0 inside the punctured smooth inner representation. Flowing the vertical transversal throughP gives a smooth coordinate map with initial determinantV1(P); the inverse second coordinatephi satisfies V.gradphi=0 andphi_y(P)=1. ShrinkingB1 givesphi_y>1/2. This qualitative construction and all-order fixed-patch Sobolev estimates are proved in209. The patches do not depend onLambda or m; any finite number of smaller disjoint disks fits insideB1.

For every compact potentialf of the specified parity, h=-Deltaf has streampsi=f_x and velocityU[h]=(-f_xy,f_xx), also compact. Indeed-Deltapsi=partial_xh. The difference from another sublinear canonical velocity is an entire harmonic vector field witho(r) growth; the derivative estimate2sup_boundary|H|/R makes it constant, and component parity kills that constant. Since the potentials are supported away from the axes, all center jets andSigma vanish, and dividingh byx^2y gives a smooth compact even-even factor. Since the velocities and densities vanish off their compact supports, so doLh andQ(h): the background coefficients on these supports are smooth. Hence all are inY for every fixedb,s, regardless of the behavior ofrho elsewhere.

## First finite elimination: many separate constrained plateaus

Choose (m+1)^2 pairwise disjoint open disks W_(i,j), with disjoint closures compactly inB1, indexed by0<=i,j<=m. For each choose a smaller open disk T_(i,j) compactly insideW_(i,j), a point(p_(i,j),q_(i,j)) in it and a smooth cutoffeta_(i,j) supported inW_(i,j), equal to1 near closureT_(i,j). Define on the positive patch

 F_(i,j)=eta_(i,j)(x-p_(i,j))^2/2,
 g_(i,j)=-Delta F_(i,j),

extending the potentials by even-x/odd-y reflection on the four disjoint copies before taking derivatives. Then onT_(i,j),

 g_(i,j)=-1, grad g_(i,j)=0, U[g_(i,j)]=(0,1).         (3)

Every other potential, density and velocity vanishes there. This last fact uses compact canonical velocities and disjoint supports, not a false locality assumption for a general density. The reflected plateau densities may change sign but their gradients still vanish.

For each fixedi, the m+1 vectors Lambda(g_(i,0)),...,Lambda(g_(i,m)) inR^m have a nontrivial linear relation. Choose one real vector(t_(i,0),...,t_(i,m))!=0 with

 G_i=sum_j t_(i,j) g_(i,j) inM.

These coefficients are chosen once, independently ofn. EachG_i is nonzero, because on aT_(i,j) witht_(i,j)!=0 its density equals-t_(i,j). The supports for distincti are disjoint. Choose one active indexj_i witht_i:=t_(i,j_i)!=0, and set

 g=sum_i G_i inM.

Thisg is nonzero and belongs toD_cp. On each selectedT_i:=T_(i,j_i), (3) gives

 grad g=0, U[g]=(0,t_i).                              (4)

The same gradient vanishing holds on the three reflected copies of eachT_i. No bound on the values ofLambda was used. The construction gives m+1 separate active patches of a SINGLE constrainedg.

## Wave families on the active patches

For eachi choose a real nonzero smooth amplitudea_i compactly supported inT_i. On that positive patch set

 f_(i,n)=n^(-s-2)a_i cos(nphi), h_(i,n)=-Delta f_(i,n),

and extend with the same potential parity. Everyh_(i,n) belongs toD_cp; supports for differenti remain disjoint. Define the linear cross map

 C_g h=U[g].grad h+U[h].grad g.

The fixed-patch mechanism of209 gives finite constantsH_i,alpha_i,beta_i>0 such that, for all integersn>=1,

 ||h_(i,n)||G<=H_i,
 ||(C_g h_(i,n))_positive_i||Y>=alpha_i n-beta_i.     (5)

Here the subscript denotes the function on the positiveT_i extended by zero. To see the leading term and the support claim directly, every velocityU[h_(i,n)] is compactly supported wheregradg=0. Therefore its dot product withgradg is zero EVERYWHERE. On positiveT_i the other term is t_i partial_yh_(i,n). The density has the expansion

 h_(i,n)=n^(-s)a_i|gradphi|^2 cos(nphi)
         +n^(-s-1)(2grada_i.gradphi+a_i Deltaphi)sin(nphi)
         -n^(-s-2)Deltaa_i cos(nphi).

The leading transverse derivative is

 -t_i n^(1-s)a_i|gradphi|^2 phi_y sin(nphi),            (6)

with nonzero amplitude; its remainder is uniformly bounded inY. Compact velocities have the same three modulation orders. V.gradphi=0 prevents growth in the full transport derivative, giving the uniform graph estimate in(5).

For clarity, the analytic estimate underlying(5) is Fourier translation in the smooth flow chart: n^(-s)||B exp(i n v)||Hs ->||B||2; for sine or cosine the limit is||B||2/sqrt2. Smooth changes of coordinates and nonzero smooth weights have bounded inverse maps on compactly supportedH^s functions for every finite s. Integer orders follow from the chain rule; fractional orders follow from the difference seminorm with kernel|X-Y|^(-2-2theta), the bi-Lipschitz chart comparison and bounded smooth multipliers. These arguments are proved in209. Its addendum supplies the positive-patch localization and explains why reflected physical supports are not presumed orthogonal at fractional orders. They remain valid for every one of the finitely manyT_i. Increasingbeta_i absorbs the finitely many smalln.

Choosechi_i smooth supported in positiveT_i, equal to1 near suppa_i, and zero on every other selected patch and its reflections. Since every derivative ofa_i is supported in suppa_i, the whole positive cross piece is selected exactly. Multiplication bychi_i has a finite operator boundM_i>0 onY. Thus for ANY real coefficientslambda_i,

 chi_i C_g(sum_j lambda_j h_(j,n))
   =lambda_i (C_g h_(i,n))_positive_i.                (7)

This is a support identity. No norm orthogonality or estimate onLambda enters it.

## Second finite elimination: constrained waves with bounded coefficients

For eachn, the m+1 vectorsLambda(h_(0,n)),...,Lambda(h_(m,n)) inR^m have a nontrivial real linear relation. Choose a coefficient vectorlambda_n in that kernel and normalize it by its maximum absolute coordinate:

 sum_i lambda_(i,n) Lambda(h_(i,n))=0,
 max_i |lambda_(i,n)|=1.

Such normalization is always possible because the selected vector is nonzero. No continuity, boundedness or measurability inn is needed; it is a countable sequence of finite-dimensional choices. The coefficients may depend onn but are spatial constants when derivatives are taken. Put

 k_n=sum_i lambda_(i,n) h_(i,n) inM.

The coefficients have absolute value at most1, so ||k_n||G<=sum_i H_i uniformly. Choosei_n with|lambda_(i_n,n)|=1. By(5),(7) and bounded multiplication,

 ||C_g k_n||Y >= (alpha_(i_n)n-beta_(i_n))/M_(i_n)
 >= c n-C,

wherec=min_i alpha_i/M_i>0 andC=max_i beta_i/M_i<infinity. All constants are fixed afterLambda has been chosen. This proves(1). Even wildly discontinuousLambda values merely change the finite kernel directionslambda_n; normalization keeps the coefficients bounded, and the selected patch prevents cancellation of the large cross norm.

This differs from210's proof: no correction of one wave through a graph-bounded right inverse is used, so no continuity assumption onLambda is needed. The finite parameter count is handled twice, once to make constrainedg active in m+1 patches and once to constrain the waves while retaining a nonzero component.

## Polarization, algebraic codimension and scope

OnD_cp, Sigma=0 andU is linear. Therefore

 Q(g+k)-Q(g-k)=2C_gk.

Quadratic homogeneity and(1) give

 ||Q(v_n^+)||Y+||Q(v_n^-)||Y
 >=(2/n)||C_g k_n||Y>=2c-2C/n.

Both input norms areO(n^(-1/2)), and their MAXIMUM output has lower limit at leastc. This proves(2). No separate positive lower bound for each sign is claimed. On every ball about0 these inputs eventually belong toM intersected with the ball. A quadratic bound or continuity there is therefore impossible. The same holds forLh+Q(h) because eachL v_n^+ andL v_n^- tends to0 inY. The canonical normalized residual difference equals that expression, withSigma(h)=0 preservingell.

IfM is any linear subspace of finite algebraic codimensionr inD_cp, its algebraic quotientD_cp/M is a vector space of dimensionr. Choose any linear isomorphism toR^r and compose it with the quotient map. This supplies a real linearLambda with kernelM, regardless of quotient topology or closedness. Applying the theorem proves the equivalent formulation. The caser=0 uses one plateau and one wave, with no nontrivial constraint.

This is an obstruction in a specified graph topology on specified smooth compact tests. It proves no global inverse, no closedness ofL, no bounded extension ofQ, no universal norm constant and no decisivePDEendpoint. Infinite-codimensional restrictions and nonlinear constraints remain outside this argument. A different domain norm inherits the counterexample only when it is bounded above by a fixed multiple of||.||G on the constructed tests; arbitrary stronger norms are not covered.

## Verification plan and dependencies

Result209 and its mandatory corrections supply the actual background, gauge and fixed-patch Sobolev mechanism. Result210 is a predecessor whose continuous-constraint restriction is strengthened, not an assumption of the new finite elimination. All inherited evidence pins will be freshly rehashed. Two exact methods will test the two rounds of kernel selection and maximum-coordinate normalization on manufactured matrices, including rankzero and rank deficiency, and separately reconstruct polarization and support-selection algebra. Finite examples do not prove the general linear-algebra and functional-analytic argument above. No new interval enclosure or modal norm ceiling is proposed. Full actual Opus5.5 proof and executed-evidence reviews, followed by later own adjudication resolving objections, are required beforeFINAL.
