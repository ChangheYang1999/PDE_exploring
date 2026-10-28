# Reference hypotheses for the compatible weighted theorem

This is the complete sufficient reference contract for V081. It also implies the hypotheses of V078. It does not assert that these constants are necessary. The numerical status below concerns only the exact accepted state 131. A new reference needs its own certificates.

## 1. Notation and fixed spaces

All functions are on the full plane. Write <r>=(1+r^2)^(1/2), V=cX+u, u=U[rho], and

    A=[[rho_y,-rho_x/2],[-rho_x/2,0]],
    M=(2c+1)I+sym Du+A,
    omega0=<r>^(-6/5), omega1=<r>^(-1/5),
    omega2=(1+4r^2)^(2/5), R=2^35,
    w=(1+r^2/R^2)^(-11/10).

The velocity is U=(-R1 R2,R1^2) with the canonical full-plane realization fixed by the compact parity completion and sublinear growth. There is no additional harmonic velocity. All tensor bounds below use the Euclidean norm of the ordered Cartesian tensor, pointwise before the supremum. Componentwise suprema are summed only when explicitly indicated.

Let L(h)=||wh||_(Hdot^-1), Pj(h)=||omegaj D^j h||_2, and

    E1(h)^2=P1(h)^2+2^31 L(h)^2,
    E(h)^2=P2(h)^2+2^22 P1(h)^2+2^53 L(h)^2,
    N_s^w(h)=E(J^s h), J=(1-Delta)^(1/2).

Each is the completion of compact smooth even-x, odd-y scalar functions. Derivatives and velocities have their induced parity. The operator is its maximal distributional realization in the specified space. This is a domain condition, not the assertion that the transport maps the entire space boundedly to itself.

## 2. Complete sufficient hypotheses

(W0) Structure. The real density rho is smooth, even in x and odd in y, has sublinear growth, and has canonical sublinear velocity u. Its derivatives appearing in W3 are bounded with the stated weights. The exponent satisfies 9/5<c<37/20. The origin coefficient a0=rho_y(0) is at least 1. The velocity vanishes at the origin by parity.

(Wn) Exact normalization. c+c[rho]=1, where c[rho]=partial_xy psi[rho](0). The definition includes the local derivative term in the full-plane distributional strain formula. No approximate normalization is substituted.

(W1) Low matrix and decay coefficients. At every point, M>=19I/5. Also, with delta=2/5,

    sup r^delta (|D rho|+r|D2 rho|) <=152,
    sup r^(-1+delta)|u| <=18,
    sup r^delta|Du| <=18,
    sup r^(1+delta)|D2u| <=45.

The values at r=0 are interpreted by continuity when applicable. The first expression is a sum at the same point; bounding its two terms separately and adding is permissible. These four bounds, W0 and the low matrix are sufficient for the low semigroup decay 1/5 at R=2^35. In fact the proved lower bound exceeds 0.22888161. The exact rational check uses 1/sqrt(2)<5/7 and the commutator constant 14. The generator realization and its inverse are part of the conclusion of the low proof, not an extra assumed surjectivity statement.

(W2) Weighted principal matrices. For k=1,2, put

    Mk=(1+c+V.D log omegak)I-k sym DV+A.

Require M1>=I/2 and M2>=I/2 everywhere. The first weight is omega1=<r>^(-1/5); it is not the unweighted first-derivative matrix. For k=2 the displayed 2 by 2 matrix represents the principal quadratic form after summing over the remaining derivative index. Both inequalities are sufficient pointwise conditions on the symmetric derivative tensor.

(W3) Background derivative bounds. Require

    |Du|<=14/5, |D rho|<=16,
    <r>|D2u|<=3, <r>|D3u|<=16,
    |D2rho|<=3, <r>|D2rho|<=8,
    <r>^2|D3rho|<=32, <r>^2|D4rho|<=512.

Every bound is global. W0 already implies |c|<2. Safe sums of component suprema, used in the fractional commutator proof, are respectively 12, 24, 256 for Du,D2u,<r>D3u, and 32,12,256,8192 for D rho,D2rho,<r>^2D3rho,<r>^2D4rho. These follow by multiplying a Frobenius bound by the number of ordered components. There is no invalid interchange of a supremum with a square sum.

(Wm) Actual forcing membership. F(rho;c)=V.Drho-rho belongs to N_s^w. This is a condition on the actual unnormalized density residual. A normalized or sampled residual cannot replace it.

(Ws) Actual forcing smallness. At s=2^-30 require N_s^w(F(rho;c))<=2^-46. This is the only condition in this list that fails for exact state 131.

(Wt) Leading profile, needed for the tail and scaling conclusions. For gamma=1/c, there is a nonzero continuous angular function Theta0 such that r^(-gamma)rho(r,theta) converges uniformly to Theta0(theta). By W0, 1/5<gamma<1. Corrections in N_s^w obey |h(X)|<=2^13 max(1,r)^(1/5)N_s^w(h), so their normalized leading coefficient tends uniformly to zero. Thus both the full leading angular function and exponent remain fixed. Scaling changes the leading function to t^(1-gamma)Theta0, which equals Theta0 only for t=1. Its derivative is (1-gamma)Theta0, which is nonzero. The infinitesimal scaling vector is outside the correction space. This fixes scaling by the asymptotic class; it does not introduce a nonexistent nonzero phase functional on that correction space.

## 3. Conclusions and proof of reference independence

W0-W3 imply the low and E semigroup bounds in SHARP_WEIGHTED_H2_PROOF.md, by the radial low argument, both weighted principal matrices, the full differentiated energy identities, and the common flow construction. The Riesz constants 8/3,3/2,9/5 and weighted-negative-order velocity constant 13/2 are universal for these spaces and parity. They are not new numerical hypotheses on rho.

PROOF.md supplies the reference-independent fractional embeddings and multipliers. SHARP_LOW_COMMUTATOR_PROOF.md uses W3 only through its explicit component sums. SHARP_ROUGH_INVERSE_PROOF.md then gives, for 0<s<=2^-12,

    ||exp(t A_k)||_(N_s^w -> N_s^w)
      <= exp[-t(1/20-2^23 s-2^19 N_s^w(k)/sqrt(s))],
    A_k=(cX+u+U[k]).D-1+U[.].D rho.

The common maximal realization, low consistency, high-ball completeness in the low metric, and derivative-loss-free difference estimate are proved in sections 6-8 of ROUGH_INVERSE_PROOF.md, with the sharper commutator and low inclusion replacing its earlier constants. No finite-potential formula occurs in those arguments.

With Wn,Wm,Ws and s=2^-30, the normalized radius 2^-41 ball has a unique fixed point solving F(rho+h;c)=0. The high inverse is at most 32, low inverse at most 6, and contraction factor 3/1024. On c[k]=0 the trace identity is

    (A_k h)_y(0)=c[k]h_y(0)+a0 c[h]=a0 c[h].

Thus the forcing hyperplane f_y(0)=0 corresponds precisely to c[h]=0. Wn and parity give F(rho;c)_y(0)=0. The slope changes by at most 2^-15, so the nonlinear stationary normalization also holds with positive slope. The combined low, adapted Holder, jet-subtracted moment and strain inverse constant is 2^68 at this s. Wt adds the fixed-tail and scaling statements; it is not used in the energy estimate or contraction.

## 4. Relation to the lead's B0-B11 list

| Existing label | Role in this weighted theorem |
| --- | --- |
| B0 | Supplies structure and boundedness. W0 strengthens a0>0 to a0>=1 for the stated radius and keeps the same c interval. |
| B0n | Exactly Wn. |
| B1 | Exactly the matrix part of W1. The four decay constants in W1 are additional quantitative hypotheses. |
| B2, B3 | Not used in this weighted proof. They enter the unweighted-bottom energy route. |
| B4 | Not sufficient for W2: its first-derivative matrix uses weight 1. The weighted M1 certificate must be used. |
| B5 | Exactly the M2 part of W2 when omega=(1+4r^2)^(2/5). |
| B6 | Not used. This proof does not require the auxiliary third-derivative energy or X_w interpolation. |
| B7 | Its |D2rho|<=3 is used. Its omega-weighted bounds alone do not give the stronger <r> and <r>^2 bounds in W3. The original certificates, not merely B7's statement, prove those extra bounds. Its 28 and 40 constants are not needed here. |
| B8 | Its qualitative boundedness helps B0, but its loose numerical constants are not the W3 constants. W3 must be verified. |
| B9, B9c | Neither numerical aggregate is assumed or used. W3 supplies the different explicit component sums needed here. |
| B10m | Replaced by Wm in the distinct N_s^w space. Original state 131 fails B10m but satisfies Wm. |
| B10s | Replaced by Ws, at s=2^-30 and eta=2^-46. |
| B11 | Wt adds gamma=1/c and its explicit range; true for state 131. Used only to identify the fixed asymptotic/scaling class. |

Consequently one cannot cite B0-B9 alone as the entire reference contract for V081. W1's decay coefficients, W2's weighted first matrix, and W3's sharper derivative bounds must be retained.

## 5. Exact state 131 evidence

The machine-readable registry verification/reference_audit.json binds this document and every listed input by SHA256. The exact source is research/source_audit/state131_exact.json, whose canonical coefficient serialization hash is 4d80cf85ea1746d41c3fcfbdc622c74465cff5b9358e68614e521531ea78fb01. Its rational exponent is c=4076476460239181/2251799813685248. Approximate decimal values in this paragraph are orientation only: c=1.8103192102, a0=10.3002948918, gamma=0.552388769.

| Condition | Evidence | Status |
| --- | --- | --- |
| W0,Wn,Wt | source_audit/state131_exact.json; 01_operator/PROOF.md; 05_tails/PROOF.md; exact potential and center coefficient reconstruction | CONFIRMED |
| W1 matrix | 02_energy/COMPACT_CERTIFICATE_PROOF.md and verification/compact_certificate_audit.json | CONFIRMED |
| W1 decay constants and low rate | 07_weighted/RADIAL_COMMUTATOR_PROOF.md; verification/state131_weighted_bounds.json and radial_commutator_constants.json | CONFIRMED |
| W2 both matrices | 07_weighted/HIGH_SYMBOL_CERTIFICATE_PROOF.md; verification/high_symbol_certificate_audit.json; 131 and 201 complete leaves, each independently recomputed at 384 bits | CONFIRMED |
| W3 first derivatives | 02_energy/AUXILIARY_CERTIFICATE_PROOF.md; auxiliary_certificate_audit.json and state131_coefficient_bounds.json | CONFIRMED |
| W3 D2rho, weighted D2rho,D3rho,D2u | 07_weighted/SHARP_COEFFICIENT_PROOF.md; verification/sharp_coefficient_audit.json; 663 complete leaves, 384 bits | CONFIRMED |
| W3 weighted D4rho,D3u | 07_weighted/R2_DERIVATIVE_PROOF.md; verification/r2_extra_audit.json; 315 complete leaves, 384 bits | CONFIRMED |
| Wm | exact residual symbol degree 2/c-1 in (0,1/5), smooth center, and derivative symbol bounds; 16_weighted_fractional/RESIDUAL_GAP_PROOF.md | CONFIRMED |
| Ws | three independent 768-bit evaluations give F(0,1000)>1/8; growth embedding gives N_s^w(F)>2^-18 | REFUTED, by a strict factor greater than 2^28 |

A CONFIRMED membership statement does not estimate the actual residual norm from above. A REFUTED smallness hypothesis disproves applicability of this sufficient theorem to this reference, not existence in the weighted class. Independent review by the lead of the analytical proofs was requested.
