# The obstruction with compact canonical velocities

This strengthening is written before its new checker. Its real creation time and hash are in evidence/compact_proof_first.json. It supplements the original PROOF.md and uses the same actual background, exact source rectangle, logarithmic norm, and phase. Status OPEN pending the complete actual review of this additional argument.

## Stronger statement

For every fixed finite real a, at s=153/50, the sequence in (1) of PROOF.md can be chosen with both h_n and its canonical velocity U[h_n] supported in one fixed compact set away from both axes. In particular every Lh_n belongs to Y, and

 sup_n (||h_n||_Y+||Th_n||_Y)<infinity,   ||Lh_n||_Y -> infinity.   (9)

All center jets and all interior harmonic moments of the velocity vanish, as do J(h_n) and Sigma(h_n). Thus restricting only to smooth tests whose canonical velocity vanishes in a neighborhood of the entire axes does not repair the graph estimate. No closed linear operator on Y whose domain contains all of D(T) can agree with L on this sequence. The conclusion does not exclude a closed realization on a different, stronger domain.

## Construction from a compact potential

Use the same nonzero real b in C_c^infinity of the log rectangle Q and let beta=a-1/2. On Q, with z=log x and Phi=D z+A log y, set

 f_n(x,y)=n^(-s-2) x^beta b(log x,y) exp(i n Phi(log x,y)).

Extend evenly in x and oddly in y, and by zero elsewhere. This gives a smooth compact function, since the four supports are separated from the axes. Put h_n=-Delta f_n. The stream function psi_n=partial_x f_n solves -Delta psi_n=partial_x h_n and is odd in each coordinate. Its velocity

 U_n=(-partial_xy f_n,partial_xx f_n)

is smooth and compact. It is the canonical velocity: it solves the whole-plane elliptic equation and has the required parity and sublinear growth. To see uniqueness directly, the difference of two admissible velocities is an entire harmonic vector field with sublinear growth. The mean-value derivative estimate on radius R bounds its derivative at any fixed point by C/R times its supremum on that disc, tending to zero as R tends to infinity. Each component is therefore constant. Velocity parity rules out both constants. This also identifies the explicitly constructed compact velocity with the canonical angular Green solution.

Since f_n is zero near both axes, h_n has a global smooth x^2 y factor, all its center jets vanish, and Sigma(h_n)=partial_xxy f_n(0)=0 exactly. Moreover psi_n and U_n vanish near the axes, so every inner harmonic coefficient Gamma_(2j) is zero. No small approximate moment or correction bump is required.

## Density and frozen graph estimates

For w(z,y), direct Cartesian differentiation gives

 x^(-beta) Delta[x^beta w(log x,y)]
 =x^(-2)[w_zz+(2beta-1)w_z+beta(beta-1)w]+w_yy.                  (10)

Applying this to w=b exp(i n Phi), define the three fixed smooth compact amplitudes

 R_phi=D^2/x^2+A^2/y^2,
 B1=x^(-2)D[2b_z+(2beta-1)b]+2A b_y/y-A b/y^2,
 B0=x^(-2)[b_zz+(2beta-1)b_z+beta(beta-1)b]+b_yy.

The transformed density is exactly

 F_(h_n)=exp(i n Phi)[n^(-s)R_phi b-i n^(-s-1)B1-n^(-s-2)B0].   (11)

Here R_phi b is not zero, because R_phi>0. The H4/L2 interpolation estimate from PROOF.md bounds the H^s norms of the three terms by C, C/n and C/n^2. This applies on all reflected patches and proves ||h_n||_Y<=C.

The conjugate of T is P0=-A partial_z+D y partial_y+c. Its differential part annihilates Phi exactly. Applying it to (11) differentiates only the three fixed amplitudes, apart from multiplication by c. The resulting amplitudes are again smooth and compact. The identical estimate gives ||Th_n||_Y<=C. Thus each density belongs to the full maximal frozen graph domain, with bounded graph norm.

## Compact nonlocal output and variable transport growth

Every component of x^(-beta)U_n is an exponential exp(i n Phi) times a sum of three fixed compact smooth amplitudes with coefficients n^(-s), n^(-s-1), n^(-s-2). This follows directly from the two Cartesian derivatives in the formula for U_n. Its leading vector amplitude is

 (D A/(x y), -D^2/x^2)b.                                        (12)

In particular the H^s norm of U_n after multiplication by any fixed C4 coefficient on the support is bounded independently of n. More explicitly, multiplication by grad rho0 makes each compact amplitude C4; the H4/L2 interpolation argument remains valid. Multiplication by the weight x^(-beta) is harmless on the compact support and is already included in (12). The C6 density on the support supplies the required C4 derivatives of grad rho0. Therefore the entire global coupling U_n.grad rho0 has bounded Y norm and compact support. No off-support kernel estimate or general global weighted multiplier theorem is used.

Applying the variable transport to (11), the derivative of its phase in the leading term is

 i n^(1-s) R_phi b b_V exp(i n Phi).                             (13)

Its other terms have bounded Y norm. Indeed differentiating each fixed amplitude costs no n, and the phase derivative in the n^(-s-1) term has size n^(-s), while the one in the n^(-s-2) term has size n^(-s-1). The background coefficients are C4 on the fixed support. The conjugation also adds beta(V01/x) times the density, which is bounded by the same argument.

By the strict rectangle inequality b_V>10, the fixed compact amplitude R_phi b b_V is nonzero. Localizing to the positive patch and applying the partial-Fourier lower bound (4) of PROOF.md proves

 ||chi_+ Lh_n||_Y >= c n-C

for some c>0 and C independent of n. The -h_n term is bounded, the compact velocity coupling is bounded, and the rank-one term is identically zero. Every term of Lh_n is supported in the same four compact patches and is C4, hence belongs to Y. Since multiplication by chi_+ is bounded on Y, the preceding inequality implies (9).

Taking for each n the real or imaginary part with the larger localized output norm gives a real sequence, exactly as in the original proof. This preserves the potential construction, the compact velocities and every zero moment. A uniform scalar rescaling can make all input graph norms at most1 if desired.

## Consequence for closed realizations

The maximal frozen graph space D(T), with norm ||h||_Y+||Th||_Y, is Banach because T is closed. Suppose a closed linear operator A_full on Y has D(T) contained in its domain and agrees with the actual L on these tests. Its restriction D(T)->Y has closed graph: if h_j tends to h in the T graph norm and A_full h_j tends to g in Y, then h_j tends to h in Y, and closedness of A_full gives A_full h=g. The closed graph theorem therefore bounds ||A_full h||_Y by a constant times ||h||_Y+||Th||_Y for every h in D(T). This contradicts (9). In particular a domain equal to D(T) is impossible for a closed realization agreeing with these smooth test values.

This is a restriction on the choice of a global frozen domain, not a failure of all closed realizations or of all inverses. Taking the actual transport graph, intersecting graph domains, or choosing a stronger space changes the hypothesis. No PDE exclusion neighborhood and no decisive endpoint is established.

## Checks required before acceptance

The new checker must derive (10), the complete expression (11), the leading vector (12), and the fact that the frozen phase is annihilated. Independent Cartesian differentiation must check the Laplacian and the two velocity components without importing a symbolic formula from the first checker. Finite algebra checks establish identities only. Compact canonical uniqueness, functional-analytic estimates and the closed graph consequence require review of this full argument. Parent-source arithmetic and its interval rectangle remain those already computed for PROOF.md.
