# A second-order frequency error for the real principal coupling

## Statement and scope

Let the rectangular torus have radial period L and angular period 2pi, with normalized Lebesgue measure and frequency lattice Gamma={(2pi j/L,n):j,n integers}. Let S_i, i=1,2, be the bounded self-adjoint Fourier multipliers

 s_i(p)=p_i/|p| for p!=0, s_i(0)=0.

Let B(X) be a real symmetric 2 by 2 matrix field, with absolutely convergent Fourier coefficients and second Fourier moment

 S2mat(B)=sum_(q in Gamma) |q|^2 ||Bhat(q)||_op < infinity.

For scalar b write S2(b)=sum_q |q|^2 |bhat(q)|. Suppose b is real, its second Fourier moment is finite, and B(X)<=b(X)I pointwise. Define

 Cpr=sum_(i,j) M_(B_ij) S_i S_j,
 Q_Lambda=1_(|p|>=Lambda), Lambda>0.

Then every u=Q_Lambda u satisfies

 Re<Cpr u,u> <= integral b |u|^2
       + [S2mat(B)+S2(b)] ||u||^2/(2 Lambda^2).            (1)

In particular the IPM matrix on a regular cylinder is

 B=R_theta^T [[-g2,g1/2],[g1/2,0]] R_theta,
 bplus=(|g|-g2)/2,
 b_eta=(sqrt(|g|^2+eta^2)-g2)/2, eta>0.

If the displayed Fourier moments are finite, then

 Re<Cpr u,u> <= integral bplus |u|^2
       + [eta/2+(S2mat(B)+S2(b_eta))/(2 Lambda^2)]||u||^2. (2)

One may replace S2mat(B) by sum_(i,j) S2(B_ij). This gives an explicit quadratic improvement in the cutoff dependence over the first-commutator estimate of proof 78. It is a regular-cylinder principal-operator theorem. It does not yet bound the full variable Mellin remainder, singular angular conjugation, cutoffs, radial tails, jet subtraction, or the complement inverse of the actual operator.

## Exact double-commutator identities

For an operator A let [S,A]=SA-AS. Put

 T_B=sum_(i,j) S_i M_(B_ij) S_j,
 D_B=sum_(i,j)[S_i,[S_j,M_(B_ij)]].

All are bounded under the stated Fourier assumptions. Expanding each commutator, using S_i S_j=S_j S_i and B_ij=B_ji, proves

 (Cpr+Cpr*)/2=T_B+D_B/2.                                 (3)

There is no first-commutator remainder in (3). The symmetry of the coefficient matrix is essential. The pointwise matrix inequality gives <T_Bu,u><=sum_i <b S_i u,S_i u>.

Let P0 denote the constant Fourier projection. Since sum_i S_i^2=I-P0, another exact expansion gives

 sum_i S_i M_b S_i
  =M_b-(P0 M_b+M_b P0)/2
          -(1/2)sum_i[S_i,[S_i,M_b]].                    (4)

For the high-frequency u in (1), P0u=0, so the two P0 terms vanish in its quadratic form. Combining (3) and (4) reduces (1) to the norm of two compressed double commutators.

## Sharp high-high direction bound

For nonzero p,k, elementary expansion gives the identity

 |k/|k|-p/|p||^2
   = [|k-p|^2-(|k|-|p|)^2]/(|k||p|).

Thus, when |p|,|k|>=Lambda,

 |s(k)-s(p)|^2 <= |k-p|^2/Lambda^2.                       (5)

The Fourier entry of D_B from p to k=p+q is

 (s(k)-s(p))^T Bhat(q)(s(k)-s(p)).                        (6)

Even though Bhat(q) can be complex, the difference vector is real, so its absolute value is at most ||Bhat(q)||_op |s(k)-s(p)|^2. By (5), the entry is at most |q|^2 ||Bhat(q)||_op/Lambda^2 on the compressed high-high block. Young's convolution inequality, or the equal row and column Schur bounds, therefore gives

 ||Q_Lambda D_B Q_Lambda|| <= S2mat(B)/Lambda^2.           (7)

For the summed scalar double commutator the entry is bhat(q)|s(k)-s(p)|^2. The same argument gives S2(b)/Lambda^2. Insert these two bounds into (3)-(4) to prove (1). The eigenvalues of the displayed IPM matrix give B<=bplus I<=b_eta I, and 0<=b_eta-bplus<=eta/2. This proves (2). The proof only uses high frequency on the quadratic-form input and output; it does not claim the same constant for an uncompressed high-to-all operator.

## Derivative certificate for the Fourier moment

Define, using normalized L2 norms on the torus,

 D4(a)^2=
   sum_(j=0)^2 binom(2,j)||partial_t^j partial_theta^(2-j)a||_2^2
 +2 sum_(j=0)^3 binom(3,j)||partial_t^j partial_theta^(3-j)a||_2^2
 +  sum_(j=0)^4 binom(4,j)||partial_t^j partial_theta^(4-j)a||_2^2.

Then

 S2(a) <= C_L D4(a),   C_L^2 <= 1+pi/2+3L/4.             (8)

Indeed Cauchy-Schwarz splits |p|^2 |ahat(p)| into factors (1+|p|^2)^(-1) and |p|^2(1+|p|^2)|ahat(p)|. The squared sum of the second factor is D4(a)^2 by Parseval and the binomial expansions. For the first factor, let h=2pi/L. For each integer n, comparison of the positive decreasing function of |j| with its integral gives

 sum_j (1+n^2+h^2j^2)^(-2)
 <=(1+n^2)^(-2)+pi(1+n^2)^(-3/2)/(2h).

The corresponding sums in n are at most 1+pi/2 and 3. Their substitution proves (8). Finite derivative suprema can replace the normalized L2 derivative norms. Four derivatives suffice. The actual background has the required derivatives on regular compact patches after choosing smooth cutoffs and a smooth periodic extension. The nonsmooth bplus is replaced by b_eta, whose derivative bounds must actually be computed; they are not uniform as eta tends to zero.

## Local projection and practical meaning

If a physical-space localization uses finitely many real cutoffs chi_j, impose P_(<Lambda_j)(chi_j u)=0 for every j. This is a finite collection of linear conditions: u is perpendicular to each cutoff times a low Fourier mode. Its codimension is at most the sum of the local low-mode counts, with the actual Gram matrix used if these functions overlap. On this subspace (2) applies to each chi_j u. The remaining localization terms are independent errors. The second-order estimate does not make those errors vanish.

For a desired principal frequency budget E>eta/2, (2) permits the sufficient cutoff

 Lambda^2 >= [S2mat(B)+S2(b_eta)]/[2(E-eta/2)].             (9)

This can be much smaller than a cutoff inferred from the earlier first-moment bound, but no actual rank improvement is certified until the second moments, localization and conjugation errors have been enclosed. A large fourth derivative or small eta can erase the improvement. Qualitative compactness still carries no quantitative rank information.

## Verification and dependencies

The accompanying exact-rational matrix script verifies (3), (4), the zero-mode terms and (5) on an independent nontrivial finite example of commuting multipliers. It is a sign and factor check, not a replacement for the full argument above. The proof is self-contained apart from elementary Hilbert-space Fourier expansion, Parseval and Young's inequality. Proof 78 specifies the same principal IPM convention and the separate Mellin remainder.
