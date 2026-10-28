# Conditional nonlinear existence for the exact moving-tail family

## Precise implication

Fix either low setting (O) or (N) of proof 173, and write X, Y for its low correction and target spaces. In (N) fix one angular exponent a_w in[18/5,4]. Use the high spaces H=H_full and Y_H=Y_full of that topic, with the fixed variable order s, cutoffs and norms. Let rho_0 be the exact normalized modal trial, k=1615536043799051/9007199254740992 and ell_0=1/k. Its leading far angular factor is Theta. Set

 U=(-R_1 R_2,R_1^2), c[f]=psi_xy[f](0),
 F_ell(rho)=(ell X+U[rho]).grad rho-rho,
 rho_ell=rho_0+chi_infinity(r)(r^{1/ell}-r^k)Theta,
 n(ell)=3ell-1-c[rho_ell].                              (1)

All velocities are canonical full-plane velocities with the required parity and no added harmonic velocity. The cutoff chi_infinity is zero near0 and one outside a fixed disk. Choose a compact interval I with ell_0 in its interior and

 0<max(k,sup_{ell in I}1/ell)<q_*<1/4.                 (2)

Then n(ell_0)=0 and n'(ell)>=3. Define

 H_0=chi_0 X.grad rho_0/3,
 B(ell)=F_ell(rho_ell)-n(ell)H_0,
 m(ell)=(B(ell)-B(ell_0))/n(ell), M(ell)=H_0+m(ell),
 f_0=B(ell_0), eta_H=||f_0||Y_H,                        (3)

using the removable value of m at ell_0. For h in a sufficiently small H ball define ell(h) by n(ell(h))=c[h], and

 A_h f=(ell(h)X+U[rho_ell(h)]+U[h]).grad f-f
                         +U[f].grad rho_ell(h)+c[f]M(ell(h)). (4)

Assume base low injectivity:

 A_0:E B_w direct-sum D_w(0)->Y is injective.           (I)

Topics167 or171, respectively, then provide r_*>0 and finite constants K_H,K_L such that, for every h with ||h||H<=r_*, the parameter lies in I, the high and low realizations of A_h are isomorphisms, their inverses agree on Y_H, and

 ||A_h^{-1}f||H<=K_H||f||Y_H,
 ||g||X<=K_L||A_h g||Y for all g in H.                 (5)

The latter quantifier is justified by proof 173. Also there is a finite C for this ball such that

 ||(A_h-A_v)g||Y<=C||h-v||X||g||H.                    (6)

Suppose there is r with

 0<r<=r_*, K_H eta_H<=r, q_0=K_L C K_H eta_H<1.        (S)

Then the sequence

 h_0=0, h_{j+1}=-A_{h_j}^{-1}f_0                     (7)

converges in X to h in H, with ||h||H<=K_H eta_H. Its parameter ell=ell(h) belongs to I, and

 F_ell(rho_ell+h)=0.                                  (8)

The density is C^{1,alpha} on every compact subset of the punctured plane for every0<alpha<1/20. It has the required parity and

 (rho_ell+h)/(x^2 y)->1+J(h) at0,
 rho_ell+h=r^{1/ell}Theta+O(r^{-1/2}) at infinity.     (9)

The quotient at the axes is understood through its continuous extension. Equation(8) holds pointwise off0. If K_L C r<1, h is the unique solution of f_0+A_h h=0 in the closed H ball of radius r in this fixed moving-tail chart.

If additionally |J(h)|<1, then lambda=sqrt(1+J(h)) is positive and

 rho_norm(X)=lambda(rho_ell+h)(X/lambda)               (10)

is a solution with unit cubic coefficient, the same ell and c, and leading tail lambda^{1-1/ell}r^{1/ell}Theta. A sufficient numerical condition for this last step is

 ||J||_{H*} K_H eta_H<1.                              (11)

The uniqueness assertion concerns h before the rescaling. It does not assert uniqueness in an unqualified class of unit-normalized profiles or in a ball preserved by (10).

## Verification of the hypotheses supplied by earlier theorems

Proof 167 proves that B and m are smooth Y_H-valued families. At0 the subtraction n H_0 removes the entire cubic term. At infinity ell(1/ell)=1 removes the leading linear tail; the remaining nonlinear exponent after division by b is at most2q_*-1/2<0. The exact joined modal density is C6 at its nonzero knots, so its residual is locally H^sigma for sigma=25/4<13/2. Thus eta_H is finite. It has not been numerically bounded in this run.

Proof 173 proves Y_H into Y, H into every low maximal transport domain and H into the high product space of proof 71. For (O), the low/high product theorem and the exact difference identity from proof 59 give (6). For (N), proof 172 gives the corresponding estimate in the new low norm. Explicitly, with d=h-v and z=rho_ell(h)-rho_ell(v),

 (A_h-A_v)g=W[d].grad g+W[z].grad g+U[g].grad z
                                 +c[g](m(ell(h))-m(ell(v))), (12)

where W[f]=U[f]+c[f]X/3. This uses the exact identity

 3(ell(h)-ell(v))=c[d]+c[z].                           (13)

The singular cubic terms cancel in (12). The first term uses the low/high product bound. The next two use the smooth tail velocity and coupling families, and the last uses the Y-valued smooth m. Since

 |ell(h)-ell(v)|<=||c||_{X*}||h-v||X/3,

all terms have the bound(6). No derivative of the low input d is taken.

The uniform inverse theorem supplies (5) under(I), with its varying maximal domains. Its high graph inverse in particular maps Y_H to H with the stated bound. The low inverse estimate applies to all g in H because of the separate embedding theorem; no unjustified common high graph domain is required. The uniform constants in(5)-(6) can be fixed once on the ball r_* and then used on any smaller ball.

Finally direct expansion, with n(ell(h))=c[h], gives the exact identity in Y

 F_ell(h)(rho_ell(h)+h)=f_0+A_h h.                     (14)

This identity includes the moving exponent, not a finite logarithmic truncation.

## Convergence and uniqueness

From(5) and(S), every iterate(7) lies in the H ball of radius K_H eta_H. For j>=1 subtract the two equations for adjacent iterates, now using A_{h_j} on both of them:

 A_{h_j}(h_{j+1}-h_j)=(A_{h_{j-1}}-A_{h_j})h_j.

Both arguments belong to the low domain of A_{h_j} by proof 173. Equations(5)-(6) imply

 ||h_{j+1}-h_j||X<=q_0||h_j-h_{j-1}||X.

Thus h_j has a strong X limit h. The H ball is weakly sequentially compact because H is Hilbert. Every weakly convergent subsequence has the same X limit by the continuous embedding, so h belongs to H with ||h||H<=K_H eta_H. The same is true of a weakly convergent subsequence of h_{j+1}.

Equation(6) implies ||A_{h_j}-A_h||_{H->Y}->0. Hence A_h h_{j+1}->-f_0 strongly in Y. For fixed h, A_h:H->Y is bounded by proof 173 and the coupling bounds. Along the weakly convergent subsequence it therefore has weak limit A_h h. This identifies A_h h=-f_0 and proves(8) by(14).

For two solutions h,g in the r ball,

 A_h(h-g)=(A_g-A_h)g.

Applying(5)-(6) gives ||h-g||X<=K_L C r||h-g||X. Under the strict uniqueness inequality the two corrections agree. This proves exactly the stated uniqueness in the chosen chart.

## Pointwise properties and normalization

The decomposition of proof 173 writes h as a factored H^sigma component and a bulk H^{41/20} component supported away from the vertical axis. On the cylinder H^{41/20} embeds into C^{1,alpha} for alpha<1/20, while H^sigma supplies at least five continuous derivatives to the factored component. Their physical counterparts have this C^{1,alpha} regularity on compact annuli. The canonical U[h] is locally continuous there: local singular integrals act on the positive Holder regularity, and the separated far part converges after the prescribed parity cancellation. The same holds for rho_ell. The distributional equation in Y therefore holds pointwise off0.

At0 the scalar part is J(h)x^2 y+O(r^{3+delta}). The factored remainder is O(r^{3+delta}) after dividing out its bounded angular cofactor. For the bulk part, oddness in y and C1 angular regularity divide out sin(theta) continuously; its support stays away from cos(theta)=0. Thus its quotient by x^2 y is O(r^delta), uniformly with the continuous axis extensions. Since rho_ell=rho_0=x^2 y+O(r^5) near0, the first limit in(9) follows.

At infinity, every high correction is O(r^gamma)=O(r^{-1/2}) pointwise. This includes the scalar part, since r^3 a_H=b and the one-dimensional z is bounded. The original far remainder is O(r^{2k-1}); because k<1/4, 2k-1<-1/2. The cutoff tail in(1) is exact outside a fixed disk. This proves the sharper O(r^{-1/2}) remainder in(9).

Homogeneity of the canonical velocity gives U[lambda rho(./lambda)](X)=lambda U[rho](X/lambda). Therefore

 F_ell(lambda rho(./lambda))(X)=lambda F_ell(rho)(X/lambda).

The cubic coefficient is multiplied by lambda^{-2}, the central strain is unchanged, and the leading r^q tail is multiplied by lambda^{1-q}. This proves(10)-(11).

## Audit verdict and remaining work

The theory author's Lemma Emb and Theorem E in work/Exist_cond.md are confirmed as the conditional implication above, with the uniqueness scope and the optional unit-normalization condition made explicit. The file's final phrase saying this is not an existence theorem should be read as saying it is not an unconditional existence proof for the actual trial. It is a conditional existence theorem.

The actual base injectivity(I) is OPEN. No numerical bounds for r_*, K_H, K_L, C or eta_H have been certified, so(S) is OPEN. The certified low residual bounds6049.11<||f_0||Y_O<8601.42 and ||f_0||Y_N<485.632 cannot replace eta_H. The statement that the present approach needs about ten thousand low modes is a planning estimate, not a proved lower bound on the dimension required by every possible computer-assisted method.

Dependencies: topics59,71,167,171,172 and173, together with the original modal construction used by those theorems. The audited theory author snapshot is stored with proof 173; its hash and all proof hashes are bound in the evidence.
