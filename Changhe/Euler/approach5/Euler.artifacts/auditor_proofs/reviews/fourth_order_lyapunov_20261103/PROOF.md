# Fourth-order universal local Lyapunov functions

Status: CONFIRMED as A489, 2026-11-03T05:35:15.318937+00:00, for Theory Agent C C33 in the team records, distinct from Theory Agent A C33. The exact algebraic certificate passed independent verification, the entire focused coordinator review was checked, and the complete proof was postread. This classifies universal local inequalities; it does not prove decay-only nonexistence.

## 1. Exact statement and notation

Fix 0<c<1/2, omega in R and a connected open set V in R3. Write J12=-1,J21=1, other entries zero, A=cI-omega J, kappa=1+c,a=1-2c. The incompressible profile equation is

    (1-c)U+B.grad U+omega JU+grad P=0,
    B=Ay+U, div U=0.                                  (1)

At a base point y let x be displacement, u=U(y), b=Ay+u, and Un the homogeneous Taylor polynomial of velocity of degree n. Let En be the divergence-free homogeneous vector polynomials of degree n, of dimension(n+1)(n+3), and Hm the scalar harmonic homogeneous polynomials of degree m, of dimension2m+1. Write d_v=v.grad, and ax(N)=(N32-N23,N13-N31,N21-N12).

An admissible k-jet has Un in En and the homogeneous parts through degree k-2 of

    [B,W]+kappa W=0, W=curl U, [X,Y]=DY X-DX Y.         (2)

Pressure value p is free. These are exactly the pressure-integrability conditions for the momentum coefficients through the available order. Let N4 be the admissible 4-jets with b!=0, including y,p as coordinates.

Let Psi(y,u,U1,U2,U3,U4,p) be C1 on the full indicated jet space over V. Assume its formal derivative along B is nonpositive at every admissible 5-jet with b!=0. Put psi(y,u,p)=Psi(y,u,0,0,0,0,p). The theorem is

    Psi=psi on the closure of N4;
    omega!=0: psi is constant;
    omega=0: psi=f(H), f in C1, f'>=0,
    H=p+|cy+u|^2/2+c(c-1)|y|^2/2.                     (3)

In particular the equality holds on every local C4 velocity solution of(1) with P in C1. It does not claim that N4 is dense in all algebraically admissible stagnating jets. It makes no assumption about global decay, a complete flow or a pressure normalization.

## 2. Polynomial extension and reduced coordinates

The elementary polynomial and realization facts are proved in A434 Section2 and A090. For b!=0, d_b:En+1 to En and curl:En+1 to En are onto, curl's kernel on En is grad Hn+1, and, for m>=1, d_b:Hm to Hm-1 is onto with a two-dimensional kernel. For m>=1 and independent b,w, h maps to(d_b h,d_w h) is an isomorphism from Hm+1 to compatible pairs(g1,g2) in Hm squared satisfying d_b g2=d_w g1. Dimensions and integration in the b direction prove these statements. Successive right inverses of d_b curl extend every admissible nonstagnating jet to any higher order. The analytic normal-form system of A090 realizes it by a local solution. Thus formal characteristic vectors are tangent to the smooth admissibility manifold. This justifies differentiating equal C1 representatives there.

Set M=DU1=S+[w]_cross/2,w=curl U1, K=D curl U2=R+[z]_cross/2, with S,R symmetric trace-free. Put

    Omega=curl U3 in E2, Z=curl curl U4 in E2.

The degree-two and degree-three parts of(2) are

    V2=d_b curl U4+[Ax+U1,Omega]+kappa Omega
                       +[U2,curl U2]-d_w U3,
    V3=d_b curl U5+[Ax+U1,curl U4]+kappa curl U4
                       +[U2,Omega]+[U3,curl U2]-d_w U4. (4)

Every vorticity residual is divergence-free. Project the jet to r=(y,u,U1,U2,Omega,Z,p). The reduced locus R4 is given by b!=0,V0=V1=0 and

    d_b Z+curl[Ax+U1,Omega]+kappa curl Omega
                       +curl[U2,curl U2]-d_w Omega=0. (5)

The three groups of equations have independent differentials, successively in curl U2,Omega,Z. Their codimensions are3,8,8. Thus the velocity part has dimension56-19=37, compared with85-(3+8+15)=59 for N4.

There is a smooth section sigma:R4 to N4, with an ambient smooth formula on b!=0. Choose fixed curl right inverses rho3,rho4. Set U3=rho3(Omega), and let N2 be minus the terms after d_b curl U4 in V2. The map

    T_b:E3 to E2 times E2, Q maps to(d_b Q,curl Q)

has image {(N,Z):curl N=d_b Z}. Its kernel is grad g, g in H4,d_b g=0, of dimension2. The image therefore has dimension24-2=22, equal to30-8. Its Moore-Penrose inverse is smooth at constant rank. Set curl U4=T_b^+(N2,Z), then U4=rho4(curl U4). Equation(5) supplies compatibility, proving the section assertion.

Over independent b,w, each fibre of the projection is the connected affine space of shifts

    delta U3=grad d_b h,
    delta U4=rho4(grad d_w h)+grad h', h,h' in H5.      (6)

Indeed equality of Omega makes delta U3=grad g1, equality of Z makes delta curl U4=grad g2, with g1,g2 in H4. The V2 difference says d_b g2=d_w g1; homogeneity removes the possible constant. The harmonic-pair isomorphism gives(6). Its dimension22 agrees with the preceding difference.

## 3. Elimination of the projection fibres

At fixed admissible 4-jet, change U5 by arbitrary t Q with d_b curl Q=0. The change of the formal derivative is t Psi_U4[d_b Q]. The set of d_b Q is exactly grad H5: it is curl-free and divergence-free, and every such gradient is attained using Q=grad h6 and surjectivity on harmonics. Monotonicity for all t implies invariance along U4+grad H5.

Next shift U4 by t grad h,h in H5. The reduced top-curl representative is unchanged. The change in V3 is -t grad d_w h, which can be compensated in U5. The characteristic U3 and curl U4 directions change by grad d_b h and grad d_w h. Their coefficient in the inequality must vanish. Integration along the affine fibres(6) gives

    Psi=F composed with pi on N4 intersect G,
    G={b,w independent}, F=Psi composed with sigma.     (7)

Here F has a C1 ambient representative for b!=0. Analytic realization lets us differentiate(7) along the formal characteristic vector. No ambient equality away from admissibility is asserted.

The reduced characteristic has components

    y:b, u:Mb, U1:d_b U2, U2:d_b U3,
    Omega:d_b curl U4, Z:d_b curl curl U5, p:grad P.b.  (8)

The Z component is minus the curl of the terms after d_b curl U5 in V3, so (8) depends only on the 4-jet. Under(6) with h'=0 it changes linearly by X_h, where

    X_h=(U2:grad d_b^2 h, Omega:grad d_b d_w h, Z:l_h),
    l_h=ax([S,H_w])+ax([H_b,R])+H_w w,
    H_v=Hess(d_v h).                                  (9)

All unlisted components vanish. To verify signs, use

    curl[Nx,grad f]=-ax([N,Hess f]),
    curl[grad f,grad g]=-ax([Hess f,Hess g]).           (10)

These follow by differentiating components; third derivative terms vanish against the alternating tensor. The commutator of a skew matrix and symmetric Hessian is symmetric, so its ax is zero. Formula(4) then gives(9), including its last term H_w w.

Monotonicity for all fibre shifts gives dF[X_h]=0. The field depends only on b,w,S,R, none of which it moves, since its U2 component is a gradient. Consequently its flow is the translation tau_s(r)=r+s X_h(r), and DX_h squared is zero. Formula(5) verifies tangency: its change is

    d_b l_h-ax([S,H_bw])+ax([R,H_bb])-H_bw w=0.

Thus tau_s preserves R4 intersect G for every real s and F composed with tau_s=F.

## 4. The quadratic translation coefficient

Fix r=pi(zeta) in R4 intersect G and h in H5. Put f=d_b^2h,g=d_b d_wh. Lift tau_s r to

    U2(s)=U2+s grad f, U3(s)=U3+s A3, U4(s)=U4+s A4,

where curl A3=grad g and A4 is chosen by T_b^+ to satisfy the linear V2 change and curl curl A4=l_h. The compatibility identity is exactly the preceding tangency identity. Since V2 has no product of two changed factors, these jets are admissible for every real s.

In V3 the only quadratic changed product is [U2(s),Omega(s)], giving

    Yhat(zeta(s))=Y0+sY1+s^2Y2,
    Y2=(Z:ax([H_bb,H_bw])).                           (11)

In the variables on which X_h depends, Y1 changes S by H_bbb and R by H_bbw, and does not change b,w. Therefore

    DX_h Y1=(Z:ax([H_bbb,H_w])+ax([H_b,H_bbw])),
    DX_h Y2=0.

Differentiate F composed with tau_s=F along the tangent space and use (I+s DX_h)^(-1)=I-s DX_h. Applying monotonicity at the lifted jet yields for every real s a quadratic polynomial with coefficient

    dF[(Z:Q_h)]<=0,
    Q_h=ax([H_bb,H_bw])-ax([H_bbb,H_w])
                            -ax([H_b,H_bbw]).         (12)

The vector Q_h lies in K_b=ker(d_b:E2 to E1), dimension7. Indeed (I-s DX_h)Yhat(zeta(s)) is tangent to R4 at r for every s, and its quadratic coefficient has only the Z component. Equation(5) forces d_b Q_h=0. It is also divergence-free, either by that tangent-space argument or directly from(10).

## 5. The exact finite algebraic lemma

The required statement is: for independent b,w, if a linear functional ell on K_b makes h maps to ell(Q_h) semidefinite on H5, then ell=0.

The expression(12) is equivariant under simultaneous rotations of h,b,w and the output vector polynomial. It is homogeneous of degree3 in b and degree1 in w. Adding t b to w leaves it unchanged, since at w=b the first commutator is zero and the other two cancel. Rotate b to e1, remove the parallel part of w, rotate its perpendicular component to e2 and rescale. These operations are used only for this algebraic lemma; the rotating Euler equation is not asserted SO(3)-invariant. It suffices to prove the lemma for b=e1,w=e2.

Choose an explicit rational basis h_i,i=1,...,11 of H5. Express Q_h in a basis of K_e1. The seven coordinate forms have symmetric rational matrices M_k of size11. It suffices to exhibit exact rank7 of these matrices and a positive definite rational matrix P with

    tr(P M_k)=0 for k=1,...,7.                         (13)

Then any semidefinite M=sum ell_k M_k gives a semidefinite P^(1/2)MP^(1/2) of trace zero, hence M=0. Rank7 implies every ell_k=0.

The exact certificate is in the team records. Its harmonic basis is obtained as the rational nullspace of the Laplacian matrix on the degree-five monomials x^i y^j z^(5-i-j), ordered by increasing i and then j. The output coordinates of K_e1 are

    (q1_y2,q1_yz,q1_z2,q2_y2,q2_yz,q2_z2,q3_y2).

The two omitted coefficients are q3_yz=-2q2_y2 and q3_z2=-q2_yz/2, exactly the divergence constraint; all x coefficients vanish. Every diagonal and polarized off-diagonal value of(12) was computed directly from these harmonic polynomials. The independent script imports no submitted code. It verifies the output constraints for all pairs.

With the exact Frobenius Gram matrix G_ij=tr(M_i M_j), set alpha=G^(-1)(tr M_i)_i and P=I-sum alpha_i M_i. The stored rank minor of the seven flattened matrices has determinant -41085390865563648. Direct exact multiplication gives tr(P M_i)=0. The rational LDL decomposition stored in the same JSON has eleven strictly positive pivots, and multiplication verifies P=L D L^T exactly. These finite identities prove positive definiteness and rank seven, hence the algebraic lemma. Large rational tables remain in the exact JSON rather than being manually transcribed here. The small verification script regenerates them from(12), so imported data alone is not being treated as proof.

## 6. Elimination of Z and reduction to A434

Assuming the lemma, dF annihilates all Z directions in K_b. At fixed lower coordinates the Z fibre is the entire affine space Z0+K_b, by(5). A smooth particular solution is minus the Moore-Penrose inverse of d_b applied to the remaining right side. Thus(7) becomes

    Psi=F'(y,u,U1,U2,curl U3,p) on N4 intersect G.      (14)

Define the C1 third-order function Psi3 by the right side. Realize any admissible 4-jet in G by an admissible analytic 5-jet. Nearby along its carrier trajectory(14) holds, so Psi3 has nonpositive formal derivative at that 4-jet. It depends on U3 only through curl U3.

Apply the proof, not the unrestricted statement, of A434 Sections4-7 starting after its top harmonic-gradient elimination. Its required variations fix b,w and use only b!=0 and G. Its bracket translations eliminate the remaining curl-curl third-order derivative. Its repeated second-order argument then eliminates the trace-free symmetric fibres by harmonic cubics, the curl-curl value by two independent strain variations and the axial-commutator rank3 test, and the vorticity by varying it on planes b.w=constant. The explicit formulas and span certificates are supplied in A434; no assumption outside the present open set is used in those steps. Hence Psi3=F''(y,u,p) on N3 intersect G, and Psi=F'' on N4 intersect G.

To identify F'' with psi, send a nonparallel w to zero, choose U1=[w]_cross x/2 and successively use fixed local right inverses of d_b curl to cancel V0,V1,V2. These jets tend to the zero-derivative jet. For density in N4, perturb the skew part of U1 slightly so w is nonparallel to b, and correct U2,U3,U4 successively by the same right inverses. Corrections tend to zero. Continuity gives equality on N4 and then its closure.

Every admissible first jet with b!=0 extends to a local analytic solution, so equality along its trajectory gives the zeroth-order formal inequality. At b=0 that derivative is zero. A044, or A434 Section8's repeated elementary proof, gives(3). For any actual C4 solution, div B=3c prevents B from vanishing on an open set; continuity of its 4-jet puts every point in the closure of N4. The equation also upgrades P to C4 locally. This completes the mathematical argument, with the exact certificate in Section5.

## 7. Verification plan and remaining scope

The theoretical question stated before the one computation was exactly(13): does the seven-dimensional space of quadratic forms contain a nonzero semidefinite element? Pass required exact polarized coefficients from(12), the correct seven-dimensional output space, rank7, exact trace orthogonality and eleven positive rational LDL pivots. All passed. Adding the identity to the form span gives the zero projected certificate, and the parallel case w=b gives the zero quadratic family; both negative controls passed. No floating eigenvalue is used. All large matrices and rational coefficients are in exact JSON, generated by a small indexed checker; no numeral-filled formal source is generated.

The originally submitted proof is preserved in the team records; the fully reviewed current source is in the team records. This reconstruction preceded the verification computation, which ran from 2026-11-03T04:06:00.713577+00:00 to 2026-11-03T04:06:03.887473+00:00 on CPU55 at low priority with one library thread. Its script, exact JSON and complete log are in verification. The focused configured-model coordinator review has been fully read and independently checked through existing working files. The source's random-jet diagnostics are not used as a proof for all parameters. The new formula is independent of c,omega. Orders k>=5, density in all stagnating algebraic 4-jets, global inequalities and the original nonexistence conjecture remain outside the claim.

## 8. Final focused review and the certificate basis

The complete coordinator review found the analytic argument correct and independently reproduced the exact stored certificate, including all eleven positive rational LDL pivots. The reviewer also checked the quadratic translation coefficient using an independent construction and a different parameter pair; these spot checks supplement, but do not replace, the written parameter-independent calculation. Earlier failed helper tests and unsuccessful candidate metrics are recorded in the review rather than presented as proof evidence.

One source sentence needs a basis qualification. The Frobenius projection of I onto the orthogonal complement of the quadratic-form span need not be positive definite in an arbitrary basis of H5. Section5 here explicitly names the basis and stores the successful rational matrix, so that defect is absent from this reconstruction. The basis-free statement is existence of some positive definite rational P with tr(P M_k)=0. If h=C h_new, the form matrices become C^T M_k C and the certificate becomes C^(-1)P C^(-T); positivity and trace orthogonality are preserved. Thus the theorem is basis-independent although that particular projection formula is not. The exact basis or stored certificate must be cited in the source proof.

The review also verifies that the arguments of the cited nonstagnating manifold and local-solution closure propositions apply at k=4, despite their source heading k>=5. P is C4 by the momentum equation when U is C4. The remaining claims about all stagnating algebraic jets and order>=5 are not inferred. The coordinator is configured for the primary model; this identifies configuration, not independent provider attestation.
