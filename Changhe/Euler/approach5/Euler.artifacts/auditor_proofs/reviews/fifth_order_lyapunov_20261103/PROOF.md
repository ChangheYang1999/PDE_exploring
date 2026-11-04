# Universal fifth-order Lyapunov functions

Status: CONFIRMED as A493 at the exact scope below; independent informal proof and exact finite certificate checked. This concerns universal jet inequalities, not nonexistence of Euler profiles.

## 1. Statement and exact scope

Let 0<c<1/2, omega be any real number, A=cI-omega J, and V be a connected open subset of R3. Put B=Ay+U and W=curl U. Let Psi be C1 on V times the full divergence-free velocity 5-jet space times the pressure value p. Assume its formal derivative along B is nonpositive at every admissible 6-jet with b=Ay+U(y) nonzero. Admissibility means the homogeneous coefficients of [B,W]+(1+c)W vanish through degree4 at order6, or through degree3 at order5; div U=0 is imposed at every degree. The pressure gradient is specified by the Euler momentum equation.

Let N5 be the set of admissible 5-jets with b nonzero, with y,p attached. Then on closure(N5), Psi equals psi(y,u,p)=Psi(y,u,0,0,0,0,0,p). If omega is nonzero, psi is constant. If omega=0, psi=f(H) with f C1 and f' nonnegative, where

    H=p+|cy+u|^2/2+c(c-1)|y|^2/2.

In particular the equality holds on the jets of every local C5 velocity and C1 pressure solving Euler. It does not classify all admissible stagnating jets outside closure(N5), inequalities assumed only for globally decaying profiles, or orders at least6. The hypotheses do not require decay.

Dependencies are the already audited local analytic jet realization and nonstagnating manifold constructions, A434's lower-order elimination, A489's fourth-order proof, and the elementary onto maps of divergence-free and harmonic homogeneous polynomials described below. No numerical observation is used for a universal parameter claim.

## 2. Polynomial notation and the reduced manifold

Write U_n for the homogeneous degree-n Taylor polynomial, E_n for divergence-free vector homogeneous polynomials of degree n, and H_n for scalar harmonic homogeneous polynomials of degree n. Put d_v=v.grad, kappa=1+c, Omega_j=curl U_(j+1), M=DU_1, S=sym M, w=Omega_0, K=D Omega_1, R=sym K, D=A+M. Matrix commutators are [L,N]=LN-NL and ax(N)=(N32-N23,N13-N31,N21-N12). For vector fields [P,Q]=DQ P-DP Q. Work first on G={b,w independent}.

Retain r=(b,U1,U2,U3,Omega,Z), Omega=curl U4 in E3, Z=curl curl U5 in E3. The reduced equations are V0=V1=V2=0 and curl V3=0, where V=[B,W]+kappa W. The two top equations before taking the curl are

    V3=d_b Omega4+[Dx,Omega]+kappa Omega+[U2,Omega2]+[U3,Kx]-d_w U4,
    V4=d_b Omega5+[Dx,Omega4]+kappa Omega4+[U2,Omega]+[U3,Omega2]+[U4,Kx]-d_w U5.  (1)

Projection from N5 onto this reduced set R5 is onto and has a smooth section for b nonzero. Choose right inverses rho_n of curl:E_n to E_(n-1), put U4=rho4 Omega and write N for minus the rest of V3. The map T_b:E4 to E3 times E3, L to (d_b L,curl L), has image {(N,Z):curl N=d_b Z}. Its kernel consists of grad q, q in H5, d_b q=0, and has dimension2. Since dim E4=35, its rank33 equals the dimension of that image (48-15). A smooth Moore-Penrose inverse gives L=T_b^+(N,Z), U5=rho5 L. This also defines a smooth ambient section; only its restriction to R5 is admissible. Triangular surjectivity of d_b curl gives smoothness of R5. These are constant-rank statements, not inferences from a rank at one numerical point.

On G the omitted affine fibres have directions

    delta U4=grad d_b h,
    delta U5=rho5(grad d_w h)+grad h',       h,h' in H6.  (2)

Indeed compatibility of the two harmonic potentials is d_b q2=d_w q1. The map h to (d_b h,d_w h) is an isomorphism onto these compatible pairs: its kernel is a harmonic homogeneous polynomial killed by two independent directions, hence zero in degree6, and the dimensions agree. Pressure freedom at order6 eliminates the independent harmonic-gradient part in U5. The paired freedom is eliminated by the next formal monotonicity variation, exactly the top two eliminations in A489 with all degrees increased by one. Thus Psi=F composed with pi on N5 intersect G, with F C1 via the preceding smooth section.

## 3. Characteristic derivatives and annihilating translations

The reduced characteristic vector at a 6-jet over zeta is

    Y_b=Db, Y_U1=d_b U2, Y_U2=d_b U3, Y_U3=d_b U4,
    Y_Omega=d_b Omega4,
    Y_Z=-curl([Dx,Omega4]+kappa Omega4+[U2,Omega]+[U3,Omega2]+[U4,Kx]-d_w U5).  (3)

The last expression eliminates U6 by V4=0. Attach also y'=b and p'=grad P.b; neither varies in the shifts below. Every admissible 5-jet with b nonzero extends to an admissible 6-jet and is locally realized, so these vectors are tangent.

For h in H6 write H_I=Hess(d_I h) for any word I in b,w. The omitted-fibre variation of (3) gives

    X_h=(U3:grad d_b^2 h, Omega:grad d_b d_w h, Z:l_h),
    l_h=ax([S,H_w]+[H_b,R])+H_w w.                   (4)

The identities curl[Nx,grad f]=-ax([N,Hess f]) and curl[grad f,grad g]=-ax([Hess f,Hess g]) follow componentwise by cancellation of third derivatives against the alternating tensor. They prove (4) and div l_h=0; the last term is grad d_w^2 h. The top reduced equation is preserved since

    d_b l_h=ax([S,H_bw]+[H_bb,R])+H_bw w.

Monotonicity for both signs of the fibre parameter gives dF X_h=0. The coefficients depend only on b,M,K, which X_h fixes, and DX_h squared is zero. Therefore the translations tau_s(r)=r+sX_h(r) preserve R5 intersect G for all real s and F composed with tau_s=F.

Put f=d_b^2h, g=d_b d_wh, C=rho4(grad g),

    N=-[Dx,grad g]-kappa grad g-[grad f,Kx]+d_w C,
    L=T_b^+(N,l_h), E=rho5 L.

Here curl N=d_b l_h by the same identities. The admissible lift of tau_s is

    U3(s)=U3+s grad f, U4(s)=U4+s C, U5(s)=U5+s E.   (5)

In V2 its change is grad(d_b g-d_w f)=0; in V3 it is d_b L-N=0. Lower equations do not change. The first product of two changed terms has degree5, so V4 contains no such product. Thus Y(zeta(s))=Y0+sY1, where

    Y1_U2=grad d_b^3h, Y1_U3=d_b C, Y1_Omega=N,
    Y1_Z=-curl([Dx,L]+kappa L+[U2,grad g]+[grad f,Omega2]+[C,Kx])+d_w L.  (6)

All other components are zero. Since Y1 fixes b,M,K, DX_h Y1=0. Pull back (3) by tau_s to get

    0>=dF_r[Y0+s B_h],   B_h=Y1-DX_h Y0,            (7)

for all real s. Hence dF B_h=0, and B_h is tangent. For verification, with v=Db, eta=Kb, Sdot=sym D(d_b U2), Rdot=sym D(d_b Omega2), the nonzero correction components are

    (DX_h Y0)_U3=2grad d_b d_vh,
    (DX_h Y0)_Omega=grad(d_v d_wh+d_b d_eta h),
    (DX_h Y0)_Z=ax([Sdot,H_w]+[S,H_eta]+[H_v,R]+[H_b,Rdot])+H_eta w+H_w eta.  (8)

These formulas specify smooth fields for b nonzero. Their coefficients in b involve smooth right inverses and need not be polynomial in b. With b,M,K fixed, however, B_h is constant in every component except Z, which is affine in U2 and Omega2. This is the polynomial structure actually used below.

## 4. The bracket and a C1 flow argument

For g,h in H6, use G_I=Hess(d_I g) and define

    T(g,h)=ax([G_bbb,H_bw]+[H_bb,G_bbw]-[G_bbbb,H_w]-[H_b,G_bbbw]),
    beta(g,h)=T(g,h)-T(h,g).                         (9)

B_g fixes b,M,K. It changes U2 by grad d_b^3g, Omega2=curl U3 by grad d_b^2 d_wg, Sdot by G_bbbb and Rdot by G_bbbw. Differentiating (6)-(8) therefore gives DB_h B_g=(Z:T(g,h)). The first two commutators in (9) come from the U2,Omega2 terms of (6); the last two come from (8), with their minus signs. All lower components are unchanged. Also X_g fixes U2,Omega2,b,M,K and B_h fixes the coefficients of X_g. Thus

    [B_g,B_h]=(Z:beta(g,h)), [X_g,B_h]=0.             (10)

No second derivative of F is needed. The exact B_h flow is

    phi_t^h(r)=r+tB_h(r)+(t^2/2)(Z:T(h,h)).           (11)

It fixes b,w, has no finite-time blowup, and stays in the relatively closed algebraic constraint set R5 by tangency and continuation within b nonzero. Its coefficients with b fixed are polynomial in t. Since dF B_h=0, F is invariant under (11). Direct substitution gives, with the rightmost map first,

    phi_-s^h phi_-t^g phi_s^h phi_t^g(r)=r+st(Z:beta(g,h)).  (12)

All intermediate points are admissible reduced points with the same b,w. This proves invariance under every bracket translation using only C1 F.

## 5. Exact universal spanning lemma

Each beta(g,h) is divergence-free, by the curl identities already used. Moreover

    d_b T(g,h)=ax([G_bbb,H_bbw]+[H_bbb,G_bbw]),

which is symmetric in g,h. Thus beta belongs to K_b=ker(d_b:E3 to E2), of dimension24-15=9. Formula(9) is equivariant under simultaneous proper rotations, homogeneous of degree4 in b and degree1 in w. At w=b its first two commutators cancel and its last two cancel, so adding any multiple of b to w leaves beta unchanged. Every independent pair reduces by rotations, that shear and nonzero scalings to b=e1,w=e2. These are symmetries of (9), not a claim of full rotational invariance of the Euler equation with fixed J.

An exact certificate at this pair suffices. Let Delta12=partial1^2+partial2^2 and define

    E(P,Q)=sum_(m=0)^3 (-1)^m z^(2m) Delta12^m P/(2m)!
          +sum_(m=0)^2 (-1)^m z^(2m+1) Delta12^m Q/(2m+1)!.

For j=0,...,5 set h_(2j)=E(0,x^j y^(5-j)), h_(2j+1)=E(x^j y^(6-j),0), and h12=E(x^6,0). These thirteen polynomials are harmonic, and their Cauchy data at z=0 prove they are a basis of H6. Evaluate beta on the pairs

    (0,8),(0,9),(0,10),(0,11),(2,6),(2,7),(2,8),(2,9),(4,6),

and divide their columns respectively by 1920,3840,4800,4800,384,2304,192,384,96. Extract the coefficients of (Z1:z^3,yz^2,y^2z,y^3; Z2:z^3,yz^2,y^2z,y^3; Z3:y^3). These are coordinates on K_e1: independence of x and the divergence condition determine the other three Z3 coefficients. The source predicts the resulting determinant -20736. The independently written checker in verification reconstructs the basis and (9), rather than importing submitted code or its matrix. Pass requires exact harmonicity, output divergence and d_b constraints, that nonzero determinant, rank9, a rank-zero parallel-pair control and failure of the d_b constraint when the correction terms in (9) are omitted. All coefficients and the finite matrix remain in exact JSON.

The independent exact check passed all criteria, including determinant -20736 and the two negative controls. Therefore the nine vectors span K_e1, and the preceding symmetry argument proves that all beta(g,h) span K_b at every independent pair b,w.

## 6. Elimination and conclusion

At fixed b,U1,U2,U3,Omega the only remaining equation for Z is

    d_b Z+curl([Dx,Omega]+kappa Omega+[U2,Omega2]+[U3,Kx])-d_w Omega=0.  (13)

Its entire fibre is Z0+K_b, with Z0 chosen smoothly by the right inverse of d_b. By (12) and the spanning lemma, F is constant on this fibre. Consequently Psi=F'(y,u,U1,U2,U3,curl U4,p) on N5 intersect G, with F' C1 on the ambient lower variables where b is nonzero.

For an admissible 5-jet in G, choose an admissible analytic 6-jet extension and its realizing solution. Nearby along its carrier trajectory the displayed equality holds. Differentiating gives the corresponding nonpositive formal derivative of F' as a four-jet function. It already has the conclusion of the top harmonic-gradient elimination of A489. Apply the remaining proof of A489 on G: its variations fix b,w, so its proof needs no hypotheses outside G or across b=0. It reduces F' to a function f(y,u,p).

For fixed b nonzero send w to zero through nonparallel vectors, choose U1=[w]_cross x/2 and successively solve V0,...,V3 by fixed right inverses of d_b curl. The resulting U2,...,U5 tend to zero. Hence f=psi. To prove density of N5 intersect G in N5, perturb the skew part of U1 and correct U2,...,U5 successively by the same triangular onto maps; the corrections tend to zero. Continuity now gives Psi=psi on closure(N5).

Every admissible first jet with b nonzero extends analytically, so the zeroth-order inequality follows there; at b=0 its formal derivative is zero. The already audited zeroth-order classification gives the stated constant or nondecreasing f(H) conclusion. For an actual local C5 solution, div B=3c prevents B vanishing on an open set, so every velocity5-jet belongs to closure(N5). The momentum equation gives P in C5 locally from U in C5 and P in C1. This proves the stated solution corollary.

The proof does not extend by the same bracket to k>=6: these fields then fix U2 and Omega2, so both brackets in (10) vanish. This is only a limitation of this argument, not a counterexample or an impossibility theorem for higher orders.

## 7. Verification and collaboration record

The written argument precedes the new exact computation. Its theoretical question and pass/fail criteria are specified in Section5. Only one small CPU computation is authorized for that question; no floating-point rank, sampled-parameter inference, GPU or proof-assistant build is needed. Source in the team records and its full precursor proof are pinned in verification. The existing Theory Agent C configured-model author has independently rederived the analytic formulas and rerun the precursor checks, as recorded in the team records. Configuration is the primary model, not provider attestation. The precursor's own attempted separate model request failed before invocation and is not counted as collaboration. The present review uses only existing working files. The existing configured-model author reconstruction, complete precursor and independent regeneration agree. The separate follow-up wording request remains pending and does not affect the proof, which already states the needed smooth and polynomial properties correctly.

The finite check ran from2026-11-03T05:38:26.674203+00:00 to2026-11-03T05:38:27.748855+00:00, elapsed1.074648seconds, on CPU55 at low priority with one library thread. It passed harmonicity, all nine output constraints, rank9, exact determinant-20736, all parallel controls and correction-deletion failures at three pairs. The complete informal proof was postread after computation.
