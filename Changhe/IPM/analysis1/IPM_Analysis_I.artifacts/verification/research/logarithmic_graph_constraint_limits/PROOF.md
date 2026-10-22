# Linear normalization and finite continuous constraints in the full IPM graph norm

This standalone proof is written before its finite checks. Its status is OPEN until independent checks, actual Claude Opus 5.5 review, resolution of objections and later own adjudication. It proves consequences of the accepted full graph results 208 and 209. No inverse estimate or PDE exclusion is asserted.

## Exact background, spaces and claims

Let rho be the exactly joined and canonically normalized modal_v2 density. Put ell=1/k, V=ell X+U[rho], and use the full-plane canonical sublinear velocity U[h]=(-psi_y,psi_x), -Delta psi=partial_x h. Write Sigma(h)=psi[h]_xy(0), J(h)=a_h(0,0) for h=x^2 y a_h, and

 Lh=V.grad h-h+U[h].grad rho+(Sigma(h)/3) X.grad rho,
 Q(h)=U[h].grad h+(Sigma(h)/3) X.grad h.

For a fixed real b and finite s>=0 let

 ||h||Y=||exp((1/2-b)z)h(exp z,y)||H^s(R^2_(z,y)),
 ||h||G=||h||Y+||Lh||Y.

H^s uses the unitary Fourier transform with multiplier (1+|xi|^2)^(s/2). The background, gauge, graph and parameter conventions are identical to 208 and 209. All spaces below are real linear spaces; no completeness or closedness of L is assumed.

There are two separate conclusions.

(A) For every real b<5/2 and 0<=s<4, let D_test be the space of smooth compact even-x/odd-y densities h=x^2 y a_h with smooth compact a_h, Sigma(h)=0, and h,Lh inY. Set D_0=D_test intersected with ker J. The set of finite nonnegative constants C for which

 ||h||Y <= C ||Lh||Y                                     (1)

holds on D_0 is exactly the set for which it holds on D_test. In particular their best constants in [0,infinity] agree, where the best constant is the infimum of the valid finite constants and inf(empty)=infinity. Thus imposing J=0 does not improve this particular inverse inequality in these spaces. This includes b in (1+k,2), s=153/50. The result does not say that either best constant is finite. More generally the same conclusion holds when D_test and D_0 are replaced by their closures in any normed graph space into which they embed isometrically, since both component norms are continuous.

(B) For every real b and every finite s>=0, take the fixed compact-potential test space D_cp from 209, defined more explicitly below. Let Lambda:D_cp -> R^m be any linear map continuous for ||.||G, where m is any nonnegative integer, and let M=ker Lambda. Then there are v_n^+,v_n^- inM such that

 max(||v_n^+||G,||v_n^-||G)->0,
 liminf max(||Q(v_n^+)||Y,||Q(v_n^-)||Y)>0.               (2)

Consequently Q restricted toM is discontinuous at0. For every radius r>0 no finite C_r bounds ||Q(h)||Y by C_r ||h||G^2 for all h inM with ||h||G<r. The same holds for every closed finite-codimensional linear subspace of D_cp equipped with this graph norm. This does not cover arbitrary discontinuous constraints, nonlinear constraints, a different target, or stronger domain norms.

Every constructed density in (B) is smooth compact, has compact canonical velocity, and satisfies J=Sigma=all center jets=all exterior coefficients=0. These identities preserve the normalization and far field exactly. The same discontinuity holds for the normalized residual difference F(rho+h)-F(rho)=Lh+Q(h). It is a difference inY even where F(rho) individually is not inY. No constant in (2) is computed.

## Proof of (A): graph density preserves the inequality

The accepted result 208 supplies h_delta inD_test with J(h_delta)=1 and ||h_delta||G->0. For each fixed h inD_test set

 h_delta^0=h-J(h)h_delta.

Linearity and Sigma(h_delta)=0 show h_delta^0 inD_0. Also

 ||h_delta^0-h||G=|J(h)| ||h_delta||G->0.                 (3)

This assertion only needs the numerical value J(h) of the one fixed smooth h, not continuity of J. If (1) holds on D_0 with a finite C, apply it to h_delta^0. Graph convergence gives both ||h_delta^0||Y->||h||Y and ||Lh_delta^0||Y->||Lh||Y by the reverse triangle inequality. Passing to the limit proves (1) on D_test with the SAME C. Restricting any inequality on D_test to D_0 proves the reverse implication. Equality of the sets of valid constants proves equality of their infima, including zero and infinity. It also handles nonzero kernel elements without defining a quotient 0/0. In a graph completion the same continuous limiting argument extends the valid inequality, proving the closure statement. There is no assumption that the closures form the domain of a closed differential operator.

## Local building blocks for (B)

For completeness the relevant verified mechanism of 209 is recorded here. The actual field V is smooth in a punctured inner disk and DV(0)=diag(-A,D), where A=2/k-1>0. Hence at some sufficiently small P=(t,t) in the positive quadrant, V1(P)=-At+o(t) is nonzero. A flow chart from the vertical transversal has a smooth inverse phase phi satisfying V.grad phi=0 and phi_y(P)=1. There is a fixed positive-quadrant disk B2, away from the axes and with four disjoint reflected copies, and a smaller disk B1 compactly inside it, such that this phase is smooth near B1 and phi_y>1/2 there. All these disks are inside the smooth inner region of the background. Let K be the union of the four open reflected B2 disks and define

 D_cp={-Delta f: f is smooth compact, even inx, odd iny, supp(f) is compactly contained inK}.

For such f the canonical stream is f_x and U[-Delta f]=(-f_xy,f_xx) is compact. The difference from any other allowed sublinear canonical velocity is an entire harmonic vector field with o(r) growth. The harmonic derivative bound 2 sup_boundary |H|/R tends to zero, so the difference is constant; component parity kills it. Thus no nonlocal tail is omitted. All tests vanish near both axes, and their compact potentials force Sigma=0. Every h,Lh,Q(h) lies inY: all products are smooth and supported inside the fixed smooth patches.

Inside B1 choose m+1 pairwise disjoint open disks W_j with disjoint closures, and nested smaller disks T_j compactly inside W_j, for j=0,...,m. All remain in the common phase chart. Choose smooth eta_j supported inW_j, equal to1 near closure(T_j), and a center (p_j,q_j) inT_j. On the positive patch let

 F_j=eta_j(x-p_j)^2/2,

then extend with the required four-patch parity, and set g_j=-Delta F_j. Supports, including all reflections, are mutually disjoint. OnT_j,

 g_j=-1, grad(g_j)=0, U[g_j]=(0,1),

while all other g_i and their velocities vanish there. These identities follow by two derivatives of the displayed polynomial; the reflected patches retain grad(g_j)=0. Each g_j is nonzero and the family is linearly independent by restriction toT_j.

There are m equations Lambda(sum t_j g_j)=0 in m+1 unknown real numbers. Thus a nonzero vector t exists. Put g=sum t_j g_j inM and choose j_* with t_(j_*)!=0. Disjoint supports ensure g is nonzero. OnT_(j_*), grad(g)=0 and U[g]=(0,t_(j_*)). The same gradient vanishing holds on its reflected copies.

Choose a nonzero real smooth amplitude a compactly supported inT_(j_*). Set on that patch

 f_n=n^(-s-2)a cos(n phi), h_n=-Delta f_n,

with the same parity extension. The wave computation and Sobolev estimates of 209 give

 sup_n ||h_n||G<infinity,
 ||C_g h_n||Y>=c n-C, c>0,
 C_g h=U[g].grad h+U[h].grad g.                         (4)

Here is why the same proof applies in the smaller patch and with this g. Each derivative of f_n gives fixed smooth compact amplitudes at orders n^(-s), n^(-s-1), n^(-s-2) for h_n and U[h_n]. V.grad phi=0 removes the possible extra n in V.grad h_n. On fixed compact charts, smooth coordinate maps and positive smooth weights give equivalent H^s norms for every finite s. Fourier translation gives n^(-s)||B exp(i n v)||Hs->||B||2, and the sine or cosine limit is ||B||2/sqrt(2). These facts yield the bounded full graph norm, with the compact velocity multiplied only by smooth background coefficients.

The term U[h_n].grad g vanishes identically because compact U[h_n] is supported where grad(g)=0. On the selected positive patch C_g h_n=t_(j_*) partial_y h_n. Its leading term is

 -t_(j_*) n^(1-s) a |grad phi|^2 phi_y sin(n phi).

The amplitude is nonzero. All other terms have uniformly bounded Y norm there. The Fourier modulation lower bound and a fixed smooth cutoff selecting this positive patch give (4), with new qualitative c,C depending on g and the patch. Upper estimates use the finite sum of the reflected pieces. No fractional-order orthogonality of disjoint physical supports is assumed. The negative-x reflected supports enforce parity and are not counted a second time in the x>0 definition ofY. These analytic estimates, including smooth fractional chart estimates, are proved in 209, read with its mandatory addendum.

## A bounded finite correction puts the waves inM

Let E=Lambda(D_cp), a finite-dimensional subspace of R^m, of dimension r<=m. If r=0, set S=0 and skip all sums below. Otherwise choose q_1,...,q_r inD_cp whose images e_l=Lambda(q_l) form a basis ofE. For v=sum c_l e_l define S(v)=sum c_l q_l. Then Lambda S=Id_E. Every coordinate c_l is continuous in the Euclidean norm onE: in a fixed finite-dimensional basis the inverse coordinate matrix is bounded. Also ||S(v)||G<=sum |c_l| ||q_l||G, so S is bounded fromE to the graph space, without any completeness assumption.

Since Lambda is graph-continuous and (h_n) is graph-bounded, the coefficients c_(n,l) of Lambda(h_n) in that basis are uniformly bounded. Define

 k_n=h_n-S Lambda(h_n).

Then Lambda(k_n)=0 and sup_n||k_n||G<infinity. For each fixed q_l, C_g q_l is smooth compact and inY. The map h -> C_g h is linear on D_cp, so

 C_g k_n=C_g h_n-sum c_(n,l) C_g q_l.

The correction has uniformly bounded Y norm. The triangle inequality and (4) give ||C_g k_n||Y>=c n-C' with the same positive leading c. No assumption that the correction supports avoid the selected patch is needed. All correction functions are fixed, so they cannot cancel an unbounded leading Y norm with bounded coefficients and bounded Y images.

Both g and k_n belong toM. Since Sigma is zero on all D_cp, exact polarization and homogeneity give

 Q(g+k_n)-Q(g-k_n)=2 C_g k_n,
 Q(n^(-1/2)(g+k_n))-Q(n^(-1/2)(g-k_n))=(2/n) C_g k_n.

Take v_n^+ and v_n^- to be these two inputs. Their graph norms are O(n^(-1/2)). The sum of their output norms is at least 2c-2C'/n, so the MAXIMUM has lower limit at least c>0. This proves (2); no lower bound for each sign separately follows. Selecting a sign that attains the larger norm supplies a single discontinuity sequence if desired. A quadratic bound on any ball would force both outputs to zero and is impossible. Since ||L v_n^+||Y and ||L v_n^-||Y tend to zero, the same maximum lower limit holds for the residual differences L v_n^+ +Q(v_n^+) and L v_n^- +Q(v_n^-).

## Closed finite-codimensional subspaces and precise limits

If M is closed and finite-codimensional in the normed space D_cp, its quotient D_cp/M with the quotient norm is a finite-dimensional normed space. The quotient seminorm is a norm: if distance(h,M)=0, closedness gives h inM. Choose any linear isomorphism from that quotient to R^r; finite-dimensional norm equivalence makes it continuous. Composing with the continuous quotient map gives a continuous Lambda with kernelM, so (B) applies. The zero-codimension case is included. Incompleteness of D_cp causes no problem for this quotient argument.

These statements concern exactly the graph topology and test domains specified above. They neither construct nor exclude an inverse in some stronger norm, make L closed, prove the full nonlinearity well-defined on the completion, nor exclude an exact X3 profile. Discontinuous finite constraints and nonlinear conditions are not treated. For a different domain norm the same nonlinear counterexample transfers only if that norm is bounded above by a fixed multiple of ||.||G on the constructed tests. There is no assertion for arbitrary stronger norms.

## Dependencies and evidentiary standards

Result 208, including its review corrections, supplies (3) only for b<5/2 and s<4. Result 209, including its mandatory addendum and correction of the two-sign wording, supplies the smooth phase and all-order Sobolev wave mechanism for (B). The current argument gives the general finite-dimensional elimination, projection and limiting proofs, not just finite examples. Parent hashes will be rechecked independently. Two finite algebra routes will check generic polarization/correction identities and manufactured projection systems, including rank zero and rank-deficient systems. Those finite systems are regression checks only; no inference from finitely many matrices to all continuous constraints is made. No new interval enclosure or norm ceiling is claimed. Actual Opus5.5 must review this full proof and the executed evidence, and a later own adjudication must resolve any objections before a FINAL verdict.
