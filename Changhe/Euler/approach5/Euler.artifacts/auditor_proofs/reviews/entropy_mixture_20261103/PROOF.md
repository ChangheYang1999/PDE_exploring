# Entropy integral affinity from finite parameter partitions

Status: LIT303 and its independent proof CONFIRMED A2491-A2495. This is a classical measure-entropy identity supplied with proof. The complete existing coordinator comparison has been read. This proof does not establish a new Euler theorem or certify an unread original reference.

## 1. Exact theorem and definitions

Let X,Z be standard Borel spaces, lambda a probability on Z, and T:X->X a Borel map. Suppose z->mu_z is a measurable probability kernel on X and T_*mu_z=mu_z for lambda-almost every z. Let

    mu(A)=integral_Z mu_z(A) d lambda(z).

Then, with natural logarithms and Kolmogorov-Sinai entropy defined by finite Borel partitions,

    h_mu(T,P)=integral_Z h_(mu_z)(T,P) d lambda(z)             (1)

for every fixed finite partition P, and

    h_mu(T)=integral_Z h_(mu_z)(T) d lambda(z),                (2)

including positive infinity. Both component entropy functions are measurable when defined to be zero on a measurable parameter null set where invariance fails. No ergodicity, invertibility, absolute continuity or finite entropy is assumed.

If Psi is a jointly measurable flow on a standard Borel space, p is a positive integer, mu_0 is invariant under g=Psi_p and s->(Psi_s)_*mu_0 is a measurable kernel, then

    nu=(1/p)integral_0^p (Psi_s)_*mu_0 ds

is invariant under every flow time and

    h_nu(Psi_1)=h_(mu_0)(g)/p.                               (3)

For the report's continuous flow on a compact metric support the required measurability holds. This is the precise Lemma24 entropy use. Lyapunov exponents, invariant manifolds and Euler hypotheses are separate inputs.

## 2. Finite entropy and invariant conditioning

For a finite partition P let P_n be the join of T^(-i)P for 0<=i<n. For an invariant probability eta, the entropy chain rule and monotonicity under conditioning imply subadditivity of H_eta(P_n), and therefore

    h_eta(T,P)=lim_n H_eta(P_n)/n=inf_n H_eta(P_n)/n.

For any finite partition Q, the same rules give

    H_eta(Q_n)<=H_eta(P_n)+n H_eta(Q|P).                       (4)

Indeed bound H(Q_n) by H(P_n)+H(Q_n|P_n), use conditional subadditivity for the n coordinates, discard all P conditions except the one at the corresponding time, and use invariance. Invariance need not be invertible for these equalities of distributions.

If R is a finite partition whose atoms are invariant modulo eta, then

    H_eta(P_n)-H_eta(R)<=H_eta(P_n|R)<=H_eta(P_n).

The conditioned sequence is subadditive too: in splitting the n+k block, invariance of eta and T^-1 R=R identify the shifted second-block conditional distribution. Consequently

    inf_n H_eta(P_n|R)/n=h_eta(T,P).                           (5)

This step would not hold for arbitrary noninvariant conditioning. In the next section the conditioning parameter is fixed by the transformation, so it does hold exactly.

## 3. The product-space argument for one finite partition

Construct the product-kernel probability M(dz,dx)=lambda(dz)mu_z(dx) on Z times X, and let T_hat(z,x)=(z,Tx). It preserves M. Choose increasing finite Borel partitions R_j of Z generating its Borel sigma algebra, which exist because Z is standard Borel. Their lifts to the product are invariant under T_hat.

Lift P_n from X. Its unconditioned M-distribution is the same as its mu-distribution. For a fixed n and an atom A of P_n, let q_A(z)=mu_z(A). Conditional probabilities on R_j are the finite conditional averages E_j q_A. These converge in L1(lambda) to q_A. To justify this without an ergodic theorem, the union of the finite partition algebras is dense for approximation in measure and hence its simple functions are dense in L1. If a is such a simple approximation, E_j a=a for all sufficiently large j, and

    ||E_j q_A-q_A||1<=2||q_A-a||1.

Since -t log t is bounded and uniformly continuous on [0,1], this L1 convergence yields convergence of entropy integrals. For example, outside a set of arbitrarily small measure the difference of the arguments is small by Markov's inequality, and on that exceptional set boundedness controls the error. Summing over finitely many atoms gives

    inf_j H_M(P_n|R_j)=integral_Z H_(mu_z)(P_n) d lambda(z).   (6)

The infimum is the limit because refinement decreases conditional entropy. Formula (5) applied on the product now gives

    inf_n (1/n)integral_Z H_(mu_z)(P_n) d lambda
      =inf_n inf_j (1/n)H_M(P_n|R_j)
      =inf_j inf_n (1/n)H_M(P_n|R_j)
      =h_mu(T,P).                                           (7)

Only two infima are commuted. For almost every z, the normalized component entropies converge by invariance and are bounded by log|P|. They are measurable because the kernel is measurable. Dominated convergence identifies the limit of the left side sequence with the right side of (1). The integrated unnormalized entropies are subadditive, so their normalized limit equals the infimum in (7). This proves (1).

## 4. Full entropy and the common generating sequence

Choose increasing finite Borel partitions P_k generating the Borel sigma algebra of X. The same sequence works for every probability on X; no selection depending on z occurs. For any probability eta and finite partition Q,

    H_eta(Q|P_k)->0.                                        (8)

One proof approximates the atoms of Q in eta-measure by sets in the algebra generated by P_k, disjointifies them with their original labels, and assigns the remaining points to a fixed label. The probability epsilon that the approximate and actual labels disagree tends to zero. For r=|Q|>=2, conditional entropy is at most

    -epsilon log epsilon-(1-epsilon)log(1-epsilon)
                        +epsilon log(r-1),

because after conditioning on the error indicator, the correct label is known on success and at most r-1 labels remain on error. This tends to zero. Subsequent refinements only reduce entropy, proving (8) along the whole sequence. A one-atom partition is immediate.

Divide (4) by n, take the limit, and use (8). For every invariant eta,

    h_eta(T)=lim_k h_eta(T,P_k).

The limit is increasing. For almost every component, h_(mu_z)(T,P_k) is the infimum of measurable normalized block entropies and is therefore measurable. Apply monotone convergence to (1) along P_k to prove (2), including infinite values. Completed-measurable finite partitions have Borel representatives modulo null sets, so allowing the completion changes no entropy; inverse images of null sets remain null under an invariant probability.

## 5. Flow averages, integer scaling and source comparison

The family mu_s=(Psi_s)_*mu_0 is p-periodic and each member is g-invariant. Periodicity makes its average nu invariant under every Psi_t by shifting the integration interval. The map Psi_s is an invertible measurable conjugacy between g with measures mu_0 and mu_s. Pulling partitions back under Psi_s preserves every name distribution and is a bijection of finite Borel partitions. Hence h_(mu_s)(g)=h_(mu_0)(g). Formula (2) gives

    h_nu(g)=h_(mu_0)(g).

For any probability-preserving T and positive integer p, the T^p n-name join of P is a subjoin of P_(pn), so h(T^p,P)<=p h(T,P). Conversely the partition Q=join_(i=0)^(p-1)T^(-i)P has exactly P_(pn) as its T^p n-name join, giving h(T^p,Q)=p h(T,P). Taking suprema proves h(T^p)=p h(T), also for infinite entropy. With T=Psi_1, this proves (3).

For a continuous flow on compact metric K, s->mu_s is weakly continuous, since continuous test functions composed with the flow depend continuously on s uniformly on K on compact time intervals. A monotone-class argument extends measurability of integrals from continuous functions to bounded Borel functions, and in particular to Borel indicator functions. Thus the kernel condition in the report holds.

The complete seven-section LIT303 proof was pinned and read. Every step matches this independent derivation: finite invariant parameter conditioning, L1 finite-averaging convergence, interchange of infima, bounded convergence for a fixed partition, a single generating sequence for all components, and positive-integer time scaling. The proof works for nonergodic component measures as stated. It is stronger than the earlier independent proof in the external-foundation review, which assumed an ergodic disintegration. Neither existence nor uniqueness of ergodic decomposition is required here.

Dependencies are the measure constructed from a measurable probability kernel, elementary finite entropy rules, density of simple functions from a generating algebra, the subadditive lemma, and dominated and monotone convergence. The conditional approximation arguments have been supplied. This result removes the separate unread integral-affinity theorem and general noninteger flow-entropy scaling as necessary inputs at report Lemma24. It does not alter the reading status of Jacobs, Walters or Abramov originals, replace other disintegration uses, or independently confirm the entire dynamical classification theorem.

The existing model coordinator compared all seven source sections and all five independent sections, with a seven-item written comparison of the product probability, lifted names, conditional subadditivity, finite averaging, two infima, common generator and periodic flow kernel. That complete addendum was read and is pinned in the team records. The actual provider execution remains independently unattested; no new model client or remote computation was used.
