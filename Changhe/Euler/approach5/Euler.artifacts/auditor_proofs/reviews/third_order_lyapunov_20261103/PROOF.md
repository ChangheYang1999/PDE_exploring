# Third-order universal local Lyapunov functions

Status: CONFIRMED as A434 after independent reconstruction and the focused configured-model review. This audits C31. It is a classification of universal local inequalities, not a nonexistence theorem for decaying profiles.

## 1. Exact statement and notation

Fix 0<c<1/2, any real omega, and a connected open set V in R3. Let J have J12=-1, J21=1 and all other entries zero. Set A=cI-omega J, kappa=1+c and a=1-2c. The source C31 uses a for our kappa; throughout this proof a means 1-2c. The velocity satisfies

    (1-c)U+B.grad U+omega JU+grad P=0,
    B=Ay+U,             div U=0.                    (1)

At a base point y, use x for the displacement and write the homogeneous Taylor terms as u,U1,U2,..., with Un a divergence-free vector polynomial of degree n. Denote their space by En; dim En=(n+1)(n+3). Put b=Ay+u. An admissible velocity k-jet satisfies the homogeneous parts through degree k-2 of

    Vort=[B,curl U]+kappa curl U=0.                 (2)

These are exactly the integrability conditions for the pressure Taylor terms of degrees 1 through k; the value p is arbitrary. Indeed the curl of momentum is (2), and a curl-free polynomial on a ball is a polynomial gradient. No global pressure normalization is imposed.

Let N3 be the set of admissible 3-jets with b!=0, including y and p among the coordinates. Let Psi(y,u,U1,U2,U3,p) be C1 on the whole indicated divergence-free jet space over V. Suppose its formal derivative along B is nonpositive at every admissible 4-jet with b!=0. Then, with

    psi(y,u,p)=Psi(y,u,0,0,0,p),

one has Psi=psi on the closure of N3. If omega!=0, psi is constant. If omega=0, psi=f(H), where f is C1, f'>=0, and

    H=p+|cy+u|^2/2+c(c-1)|y|^2/2.

In particular the equality holds on the jets of every local C3 velocity solving (1) with P in C1. The equation then gives P in C3 locally. Density of N3 in every algebraically admissible stagnating 3-jet is neither asserted nor needed.

All statements are intrinsic to admissible jets. A function can vanish with its differential on the admissibility locus and be nonconstant elsewhere. The hypothesis tests all local nonstagnating jets, not only jets that might extend to an entire decaying solution.

## 2. Polynomial freedom and realization

The following finite-dimensional facts supply all extensions used below.

For b!=0, d_b=b.grad maps En+1 onto En. After rotating and scaling b to e1, integrate a target N in x1. The resulting divergence is N1(0,x2,x3); subtract its x2-antiderivative from the second component. This correction has zero x1 derivative and restores zero divergence.

The curl map En+1 to En is onto. For a divergence-free homogeneous target W of degree n, the vector polynomial -x cross W/(n+2) has curl W. Add a polynomial gradient whose Laplacian cancels its divergence; the Laplacian from homogeneous degree n+2 to degree n is onto. For example its surjectivity follows by successively correcting |x|^2 times the target with higher powers of |x|^2 times its iterated Laplacians. The curl kernel in En is grad Hn+1, where Hm is the space of harmonic homogeneous scalar polynomials of degree m, of dimension 2m+1.

Also d_b:Hm to Hm-1 is onto. Its kernel consists of the two planar harmonics independent of the b direction, so the dimensions give surjectivity. Thus d_b curl:En+2 to En is onto and has a linear right inverse rho_n. Such inverses can be chosen smoothly in b near any nonzero b, by constant rank.

If b,w are independent, the map

    h -> (d_b h,d_w h)

is an isomorphism from Hm+1 to the pairs (g1,g2) in Hm x Hm with d_b g2=d_w g1. Its kernel would be a multiple of a single transverse coordinate to the power m+1, which is harmonic only when the multiple is zero. The compatibility map onto Hm-1 is surjective, so its kernel has dimension 2m+3, equal to dim Hm+1. We use m=3 below and m=2 in the second-order reduction.

In (2), the degree j part has the form d_b curl Uj+2 plus terms of lower order. It is divergence-free identically. Successive right inverses therefore extend every admissible nonstagnating jet to any higher finite order.

Such a jet is realized by a local analytic solution, as proved in A090. Here is the needed argument. Rotate coordinates so b1!=0. Solve div U=0 for partial_1 U1, the first component of (1) for partial_1 P, and the other two components for partial_1 U2 and partial_1 U3, dividing only by b1. This is an analytic first-order Cauchy-Kovalevskaya system. Polynomial tangential data on x1=0 realize the prescribed tangential jet. Induction on the number of normal derivatives in the differentiated normal-form equations recovers every prescribed normal derivative. This is a local construction only.

Consequently the formal velocity of a 3-jet induced by an admissible 4-jet is tangent to N3. Explicitly it has components

    y:b, u:Mb, U1:d_b U2, U2:d_b U3,
    U3:d_b U4, p:P1.b.                              (3)

Whenever two C1 representatives agree on an open part of N3, their derivatives along (3) agree. This justifies differentiating the intrinsic representatives used below without assuming ambient equality.

## 3. Reduced admissible data

Set

    M=DU, w=curl U, K=D curl U, z=curl curl U,
    L=Dz, M=S+[w]_cross/2, K=R+[z]_cross/2.

Here M,K,L are trace-free; S,R are symmetric trace-free; ax(N)=(N32-N23,N13-N31,N21-N12), so w=ax(M), z=ax(K). The first two homogeneous vorticity equations are

    Kb+w+omega Jw-Mw=0,                             (4)
    d_b Omega2-d_w U2+[K(A+M)-(A+M)K+kappa K]x=0,   (5)

where Omega2=curl U3. Taking the curl of (5) gives

    Lb=-kappa z-omega Jz+ax([S,R])+Rw=:v.            (6)

For the sign in (6), curl(d_w U2)=Kw, ax([A,K])=-omega Jz and ax([M,K])=ax([S,R])+w cross z/2. The terms z cross w/2 and w cross z/2 cancel.

Let R3 be the locus (4),(6) in coordinates (y,u,M,K,L,p), with b!=0 and all three matrices trace-free. The equations have six independent differentials: variation of K maps onto Kb in R3, then variation of L maps onto Lb independently. Thus R3 is smooth, with dimension 21 in (b,M,K,L). N3 has dimension 39 in (b,U1,U2,U3), since its eleven independent equations impose three conditions at degree zero and eight at degree one.

The projection pi:N3 to R3 is onto and has a smooth section defined even on the ambient b!=0 matrix space. To see this, fix right inverses r and r' of curl:E2 to E1 and curl:E3 to E2. The map

    T_b:E2 -> E1 x E1, Omega -> (d_b Omega,curl Omega)

has image exactly the 13-dimensional space

    I_b={(N'x,L'x): ax(N')=L'b}.

The inclusion follows from commuting curl with d_b. Its kernel is grad g for g in H3 with d_b g=0, of dimension two, so its rank is 15-2=13. For fixed inner products on both polynomial spaces, its Moore-Penrose inverse is smooth for b!=0 because the rank is constant. Set

    U1=Mx, U2=r(Kx),
    N1=d_w U2-[K(A+M)-(A+M)K+kappa K]x,
    U3=r'(T_b^+(N1,Lx)).                            (7)

The polynomial N1 is divergence-free. Equation (6) says precisely that (N1,Lx) belongs to I_b. Thus (7) supplies a smooth map sigma from the ambient set b!=0 into the ambient jet space. Its restriction maps R3 into N3, and pi sigma is the identity on R3. No admissibility of sigma off R3 is asserted or used.

On the open set G where b,w are independent, the pi-fibre is a connected affine space of dimension 18. Its directions are

    delta U2=grad d_b h,
    delta U3=r'(grad d_w h)+grad h',
    h,h' in H4,                                    (8)

with y,u,U1,p fixed. Indeed equality of K makes delta U2=grad g1 with g1 in H3. Equality of L makes delta Omega2=grad g2 with g2 in H3. Equation (5) gives d_b g2=d_w g1, and the harmonic-pair fact gives g1=d_b h,g2=d_w h. The residual curl-free freedom of U3 is grad h'. This proves both completeness of (8) and the fibre dimension.

## 4. Removing the 18 projection-fibre directions

Fix a 4-jet extending a point of N3. Vary U4 by tZ with d_b curl Z=0. Admissibility remains true for every real t, so monotonicity, which is affine in t, forces Psi_U3[d_b Z]=0. The possible d_b Z are precisely grad H4: d_b is onto E3 and commutes with curl. Integrating along the corresponding affine fibres shows

    Psi=Phi(y,u,U1,U2,Omega2,p)

on N3, for a C1 ambient representative obtained using r'. By (3), its derivative contains the terms Phi_U2[d_b U3]+Phi_Omega2[d_b curl U4], in addition to lower terms.

Now replace U3 by U3+t grad h, h in H4. Its curl is unchanged. The degree-two equation (2) changes only by -t grad d_w h, which is compensated by choosing delta U4 with d_b curl delta U4=grad d_w h. The point at which Phi is evaluated is unchanged. Monotonicity for all t therefore gives

    Phi_U2[grad d_b h]+Phi_Omega2[grad d_w h]=0.     (9)

Equation (9) holds at every point of N3 and integrates along the other directions in (8). Hence Psi is constant on the entire pi-fibre on N3 intersect G. With F=Psi composed with sigma,

    Psi=F composed with pi on N3 intersect G.       (10)

F is C1 on the ambient b!=0 matrix space. No extension theorem for a function on a singular algebraic variety has been used.

## 5. The affine fibre fields

For any divergence-free field, not necessarily a solution, direct differentiation of the vorticity residual gives

    B.grad z=-kappa z-omega Jz+ax([S,R])+Rw+curl Vort.

At an admissible 4-jet, Vort vanishes through degree two, so the derivative of curl Vort at the base point is zero. Consequently the formal B derivative of L has column j

    Q_j=partial_j(-kappa z-omega Jz+ax([S,R])+Rw)
        -L(A+M)e_j.                                (11)

This uses only the 3-jet. It is an identity for finite jets, so no unassumed fourth derivative of an actual C3 solution is needed.

Shift a 3-jet by the first h direction of (8) and extend it to order four. Its reduced value pi is unchanged. The reduced characteristic direction changes affinely by tX_h, where X_h fixes y,u,p and has matrix components

    delta M=H(b,b), delta K=H(b,w), delta L=ell_h(S,R),
    H(u,v)=D^2(d_u d_v h),
    ell_h(S,R)e_j=ax([H(b,e_j),R]+[S,H(w,e_j)])+H(w,e_j)w.  (12)

To verify (12), the shift changes partial_j S by the matrix H(b,e_j) and partial_j R by the matrix H(w,e_j), but fixes M,K,L,w,z and partial_j w. Substitution in (11) yields exactly the stated change. Thus (10) and monotonicity for every real t give

    dF[X_h]=0 on R3 intersect G.                   (13)

The fields X_h are tangent to R3, with the defining functions constant along them. Differentiating (4) gives H(b,w) b-H(b,b) w=0. Differentiating (6) gives

    ell_h b-ax([H(b,b),R]+[S,H(b,w)])-H(b,w) w=0,

by bilinearity of H(u,v). Their trace also vanishes. For the commutator terms in tr ell_h, write T=D4h; contraction of the symmetric T with the antisymmetric epsilon tensor vanishes. The remaining contraction is d_w^2 Delta h=0. Symmetry also makes ax(H(b,b))=ax(H(b,w))=0, so b,w,z stay fixed.

These fields have explicit global flows in the finite-dimensional reduced space. Write lambda_h(S,R)=ell_h(S,R)-ell_h(0,0), its linear part. Then

    S(t)=S+tH(b,b), R(t)=R+tH(b,w),
    L(t)=L+t ell_h(S,R)+(t^2/2)lambda_h(H(b,b),H(b,w)).   (14)

The flow preserves R3 intersect G for every real t. Equation (13) and the ordinary C1 chain rule make F constant along it. The completeness here is explicit completeness of polynomial affine jet-space flows, not completeness of a physical carrier orbit.

## 6. Five bracket directions fill the remaining L-fibre

Apply the four flows in order phi_h(t), phi_g(t), phi_h(-t), phi_g(-t). Formula (14) returns S,R to their initial values and changes L by t^2 beta(h,g), where

    beta(h,g)e_j=ax([G(b,e_j),H(b,w)]+[H(b,b),G(w,e_j)]
                    -[H(b,e_j),G(b,w)]-[G(b,b),H(w,e_j)]).  (15)

Here G(u,v)=D^2(d_u d_v g). All H(u,v) and G(u,v) in (12) and (15) are matrices; the final factor w in (12) is an ordinary matrix-vector product. This follows by expanding (14): the linear terms and individual quadratic terms cancel, leaving lambda_g(H(b,b),H(b,w))-lambda_h(G(b,b),G(b,w)). Interchanging g,h changes the sign. Thus F is invariant under every real multiple of beta(h,g), using only C1 regularity and explicit flow compositions.

Each beta has trace zero and beta b=0, by tensor symmetry and pairwise commutator cancellation. Let Lambda0(b) be all trace-free matrices annihilating b; it has dimension five. We now prove that the beta span is exactly Lambda0(b) whenever b,w are independent.

Formula (15) depends only on (h,g,b,w): c, omega, J and the reduced coordinates (y,u,p,S,R,z,L) do not occur. The harmonic space H4 is invariant under rotations, and for Q in SO(3) the exact covariance is

    beta(h composed with Q^T,g composed with Q^T;Qb,Qw)
        =Q beta(h,g;b,w) Q^T.

These rotations act only on this algebraic rank statement. The rotating Euler system and R3 are not SO(3)-invariant for omega!=0. Formula (15) is also homogeneous of degree two in b and degree one in w, and unchanged under w -> w+s b. For the last fact, the four added commutators cancel in opposite pairs. Rotate b onto e1, rotate the perpendicular component of w onto e2, remove its parallel component and rescale both nonzero lengths. These operations preserve the span dimension. It suffices to check b=e1,w=e2.

Use the following harmonic quartics, in variables x,y,z:

    h0=y^3 z-y z^3,        h2=3xy^2 z-xz^3,
    h4=3x^2 yz-yz^3,
    h5=3x^2 y^2-3x^2 z^2-3y^2 z^2+z^4,
    h6=x^3 z-xz^3,        h7=x^3 y-3xyz^2.

For the pairs (0,4),(0,5),(0,6),(0,7),(2,4), direct evaluation of (15), in coordinates (L12,L13,L22,L23,L32), has determinant -61917364224. All six Laplacians vanish; all five bracket matrices have first column zero and trace zero. The full exact matrices and minor are stored in the team records, generated directly from these polynomials by the independent script in the team records. They use no submitted-code imports. The nonzero minor, together with the preceding covariance argument, proves the rank statement for every independent b,w and every c,omega.

Composing translations by these five directions proves that F is constant on each full L-fibre. A smooth particular solution to (6) is, with n=b/|b|,

    L0=v n^T/|b|-(v.n)(I-n n^T)/(2|b|).

It has trace zero and L0 b=v. Setting F'(y,u,M,K,p)=F(y,u,M,K,L0,p) gives a C1 ambient representative on b!=0, and

    Psi=F'(y,u,M,K,p) on N3 intersect G.            (16)

## 7. Reduction from second order to order zero

Define Psi2(y,u,U1,U2,p)=F'(y,u,DU1,D curl U2,p). Given an admissible 3-jet in N3 intersect G, realize an admissible 4-jet analytically. Nearby along its carrier trajectory the 3-jets remain in N3 intersect G, where (16) holds. Differentiating the equality gives the nonpositive formal B derivative of Psi2 at every such 3-jet.

A100 is used as a proof template, not invoked as a theorem: Psi2 is defined only for b!=0 and its monotonicity is known only on G, whereas the original theorem has larger hypotheses. Every needed variation is repeated here. Write M=S+[w]_cross/2, K=R+[z]_cross/2. Admissibility is

    Rb-Sw=-[z]_cross b/2-w-omega Jw.                (17)

Replace U2 by U2+t grad g, g in H3. This fixes M,K,b,w and preserves (4). The degree-one vorticity residual changes by -t grad d_w g, so choose an admissible U3 for every real t using the surjectivity in Section2. All resulting jets stay in N3 intersect G. By (5), the characteristic K-direction changes by t H_w=t D^2(d_w g), independently of the chosen extension, while the M-direction changes by t H_b=t D^2(d_b g). The point at which F' is evaluated stays fixed. Monotonicity for every t therefore forces

    F'_M:H_b+F'_K:H_w=0.

For independent b,w these are exactly the seven-dimensional space of symmetric trace-free pairs (S0,R0) with R0 b=S0 w, by the harmonic-pair argument of Section2. Therefore F' is constant on the connected affine fibres of (17) and equals a C1 function F0(y,u,w,z,p).

A smooth representative exists on all b!=0, including parallel b,w: choose S=0 and solve Rb=q by the symmetric trace-free right inverse

    R=t n^T+n t^T-(n.t)(I+n n^T)/2,
    n=b/|b|, t=q/|b|.

The equality with this F0 holds on the open part N3 intersect G. The tangency argument in Section2 therefore justifies replacing the intrinsic derivative of F' by that of F0. The relevant characteristic identities are

    D_B w=-w-omega Jw+Sw,
    D_B z=-kappa z-omega Jz+ax([S,R])+Rw.

Let A0=F0_u-F0_p b, k=F0_w and l=F0_z. The strain-dependent part of the derivative is

    A0.Sb+k.Sw+l.(ax([S,R])+Rw).

In (17), vary S and R independently by sS0 and tR0 with S0 w=0,R0 b=0. Its mixed st coefficient must vanish. The vectors ax([S0,R0]) span R3 when b,w are independent. After rotating and scaling b in this algebraic span statement alone, one explicit check takes b=e1,w=q e1+d e2,d!=0, v=(-d,q,0),

    S1=vv^T-(q^2+d^2)e3e3^T, S2=ve3^T+e3v^T,
    R1=e2e2^T-e3e3^T, R2=e2e3^T+e3e2^T.

The axial commutators for (S1,R2),(S2,R1),(S2,R2) have determinant -8d^4. Hence l=0. The smooth representative extends this identity across the parallel locus by continuity, so F0 is independent of z.

Every trace-free symmetric S is available in (17) by solving for R. Its coefficient gives

    sym(b tensor A0)+sym(w tensor k)=mu I.

Each summand has at most one positive and one negative eigenvalue, so their sum cannot be a nonzero scalar multiple of the three-dimensional identity. Thus mu=0. Polynomial factorization for independent linear forms b.v,w.v gives k=beta0 b,A0=-beta0 w. Continuity extends k parallel to b across all w. Therefore F0=G0(y,u,p,sigma), sigma=b.w. Differentiating gives

    G0_u-G0_p b=-2 G0_sigma w.

Varying w within any plane b.w=sigma forces G0_sigma=0. This proves F'=F''(y,u,p) at every admissible point with b,w independent. All monotonicity variations in this paragraph preserve b,w, so restricting the hypothesis to G loses no needed test.

To identify the common value as psi, take w_n nonparallel to b tending to zero, U1=[w_n]_cross x/2, and successively choose U2=rho_0(-w_n-omega Jw_n), then U3 to cancel the residual of (5). These admissible jets tend to the zero derivative jet. Continuity identifies F''(y,u,p)=Psi(y,u,0,0,0,p).

Finally N3 intersect G is dense in N3. Perturb w by adding epsilon[v]_cross x/2 to U1, for v not parallel to b. Correct (4) using rho_0 and then (5) using rho_1. The residuals tend to zero with epsilon, so the corrected jets converge to the initial jet. Equality Psi=psi extends to N3 and then its closure.

## 8. Zeroth-order classification and actual solutions

Every first jet with b!=0 extends to a 4-jet and is analytically realized. Equality along its local trajectory transfers monotonicity to psi. At b=0 the zeroth-order formal derivative vanishes. We can therefore apply A044; the elementary argument is as follows.

Varying a trace-free M in the formal derivative forces psi_u=psi_p b. Integration yields psi=f(y,H_omega), with

    H_omega=p+|cy+u|^2/2+c(c-1)|y|^2/2
              -omega(Jy).(cy+u).

The exact rotating Bernoulli identity gives B.grad H_omega=-a(cy+u).B. Since u and p range freely, the remaining inequality, at any fixed y and H_omega, is a polynomial inequality in arbitrary b:

    -a f_H |b|^2+(f_y-a omega f_H Jy).b<=0.

It implies f_H>=0 and f_y=a omega f_H Jy. For omega=0, connectedness of V gives f=f(H). For omega!=0, the C1 function f is constant along both vector fields partial_y1+a omega y2 partial_H and partial_y2-a omega y1 partial_H. A small rectangular composition of their explicit flows translates H by a nonzero multiple of its signed area while returning y. Reversing the rectangle gives either sign, so f_H=0. Then f_y=0, and connectedness gives a constant. This argument needs no second derivative of f.

For a local C3 solution of (1), B!=0 on a dense set because div B=3c prevents B from vanishing on an open set. Its jets there lie in N3. Continuity puts every remaining jet in the closure. This proves the actual-solution assertion at the stated regularity.

## 9. Evidence, dependencies and limits

The submitted checker was fully read before execution. The independent run began 2026-11-03T02:46:13.863645+00:00 and ended 2026-11-03T02:46:59.611770+00:00. Every check and negative control passed. It checks the field identity, tangency, shifted formal derivatives, dimensions, bracket span and explicit flow loop. Those checks at its fixed rational c,omega are supporting evidence only; parameter-uniform statements follow from the proof.

The separate bracket witness ran from 2026-11-03T02:47:03.877438+00:00 to 2026-11-03T02:47:04.330627+00:00. Its exact minor is the finite algebraic certificate used in Section6. The plan preceded both computations. Only one busy worker ran at a time on CPU55, at low priority with one library thread.

Dependencies are A044/A081 (zeroth/first-order classification), A090 (local analytic jet realization), A100 (a template for the second-order calculation repeated at the needed scope, not a direct invocation), and elementary polynomial linear algebra. The independent proof checks all pressure and admissibility interfaces directly. There are no boundary integrals, decay assumptions, global characteristic-completeness assumptions or Fourier truncations.

The focused coordinator review in the team records found no mathematical gap. Its three requested exposition repairs are included: the parameter-free covariance argument, the harmonic-cubic variation in the present jet coordinates, and unambiguous matrix notation in (12) and (15). The review independently reproduced the five bracket matrices and the same determinant. This audit relies on its own read and executed scripts; the reviewer explicitly did not audit those scripts line by line. The collaboration uses the coordinator's configured with the primary model model; no provider attestation is claimed.

No conclusion is proved at order four or above. No density claim is proved for all stagnating algebraic 3-jets. In particular no unconditional nonexistence theorem for an entire decaying profile, or for all inequalities that use global information, follows from this local classification.
