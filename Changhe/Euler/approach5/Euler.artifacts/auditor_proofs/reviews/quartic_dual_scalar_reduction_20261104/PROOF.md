# A scalar formula for the exact quartic dual minimum

Status: CONFIRMED at A2794. Unrestricted pressure optimization and Euler applicability remain OPEN at A2795.

## 1. Statement and dependencies

Let

    D={b in R3: b_i>0, sum b_i=1, sum 1/b_i<=49},
    m(c)=min_(b in D) sum_i c_i b_i,  c in R3.

If c=(lambda,lambda,lambda), m(c)=lambda and every b in D minimizes. If c is not constant, there is exactly one real mu>-min_i c_i such that

    Z_+(mu)Z_-(mu)=49,
    Z_+=sum_i sqrt(c_i+mu),  Z_-=sum_i (c_i+mu)^(-1/2).   (1)

The unique minimizing vector and the minimum are

    b_i=1/[Z_- sqrt(c_i+mu)],
    m(c)=Z_+/Z_--mu=49/Z_-^2-mu.                       (2)

Repeated entries are allowed; only the all-equal case is excluded from (1). If d=max c_i-min c_i>0 and e_i=(c_i-min c_i)/d, the root theta for e satisfies

    1/2401<theta<1,
    mu=d theta-min c_i,  m(c)=min c_i+d m(e).            (3)

This theorem uses elementary real calculus, compactness and Cauchy-Schwarz. Its interpretation as a test for Laplacians of nonnegative ternary quartics additionally uses A2790. No numerical root computation is a proof dependency.

## 2. Compactness and the scalar root

The inverse-sum condition gives b_i>=1/49. On the box [1/49,1]^3 all constraints are closed, so D is compact. It is nonempty because b=(1/3,1/3,1/3) has inverse sum9. A continuous linear functional therefore attains its minimum.

For nonconstant c, put p=Z_+Z_- on the stated open interval. At its left endpoint at least one inverse square root diverges, while a strictly larger c_i supplies a positive lower bound on Z_+. Thus p tends to infinity, including when the smallest entry has multiplicity two. Dividing the terms by sqrt(mu) at positive infinity shows that p tends to9. Direct differentiation gives

    2p'=Z_-^2-Z_+ sum_i(c_i+mu)^(-3/2).                 (4)

Apply Cauchy-Schwarz to the vectors with entries (c_i+mu)^(-3/4) and (c_i+mu)^(1/4). Their inner product is Z_-, and their squared norms are the two factors of the second term in (4). Equality requires all positive numbers c_i+mu to be equal, which is excluded. Hence p'<0. Continuity, strict decrease and 9<49 prove existence and uniqueness in (1).

## 3. Minimum and uniqueness

At the root define b by (2). Its sum is1 and its inverse sum is Z_-Z_+=49, so it is feasible. For any beta in D write d_i=c_i+mu>0. Cauchy-Schwarz gives

    (sum_i d_i beta_i)(sum_i 1/beta_i)>=Z_+^2.

Since the inverse sum is at most49,

    sum_i c_i beta_i >= Z_+^2/49-mu
                     = Z_+/Z_--mu.                    (5)

The stated b attains both inequalities, proving the value in (2). If equality holds, Cauchy-Schwarz forces sqrt(d_i beta_i) to be proportional to1/sqrt(beta_i). Thus beta_i is a common positive multiple of d_i^(-1/2). The sum-one condition gives exactly (2), proving uniqueness. This includes repeated largest or smallest entries. In the constant case the functional is identically lambda, so uniqueness is neither true nor claimed.

## 4. Exact bracket and rescaling

For normalized e, one entry is0 and one is1. At theta=1/2401, the positive sum defining p contains the term

    sqrt(1+theta)/sqrt(theta)=sqrt(2402)>49

and further positive terms. Thus p(1/2401)>49. At theta=1, every square root is at most sqrt2 and every inverse square root is at most1. Therefore p(1)<=9sqrt2<49; the latter inequality follows from162<2401. Strict decrease proves the bracket (3).

If mu=d theta-min c_i, each c_i+mu equals d(e_i+theta); the factors sqrt(d) and1/sqrt(d) cancel in p. This proves the root transformation. Since every b has sum1, the linear objectives obey sum c_i b_i=min c_i+d sum e_i b_i. Positive d preserves minimizers and proves the transformation of m.

## 5. Matrix and pressure interpretation

For real symmetric C, the minimum of tr(BC) over positive definite B with tr B=1 and tr B^-1<=49 equals m(eigenvalues(C)). For fixed eigenvalues of B, an orthogonal-orbit minimizer exists. Variation by exp(tS), for skew S, gives tr(S[B,C])=0; setting S=[B,C] forces the commutator to vanish. The minimum is therefore an eigenvalue pairing, and D already contains every permutation. This argument does not require distinct eigenvalues or differentiable eigenvectors.

By A2790, C is the Laplacian matrix of a nonnegative homogeneous ternary quartic exactly when this minimum is nonnegative. For a solenoidal homogeneous quadratic Q, the tested C_gamma is defined by x^T C_gamma x=-tr((DQ)^2)-gamma Delta|Q|^2; A2791 gives the pressure equivalence. The scalar theorem itself uses neither Hilbert's theorem nor cone separation. The interpretation retains the dependencies of A2790.

All five submitted sections were read. No exploratory search, negative search outcome or rounded root is a proof of a universal pressure threshold. Neither the value of Gamma_2 nor an automatic pressure inequality for a decaying rotating Euler profile follows.

## 6. Existing comparison and verdict scope

All four items and W1-W3 of the existing coordinator comparison were read, together with all nine check-log entries. The root derivative and endpoint algebra are exact checks; the 64 high-precision cases and 20000 sampled dual points per case are supplementary observations, not a minimization proof. The complete proof is Sections2-4. No disagreement was found.

W2 supplies useful sufficient certification methods: a feasible dual vector with a strictly negative exact pairing proves nonmembership, while the exact root formula or an explicit nonnegative preimage can prove membership. This is not an assertion that those are the only possible proof methods. The boundary case m=0 requires exact treatment and cannot be decided by an unbounded floating-point error.

A2794 confirms the theorem and its combination with A2790-A2791 at their exact scopes. A2795 leaves the unrestricted value of Gamma_2 and an automatic pressure bound for a decaying Euler profile open. The comparison used the existing coordinator configured as model through working files; actual provider execution is independently unattested. No new client, agent or remote compute was used.


## 7. Source status revision

The complete delta from the archived submission to current source SHA256 88fd8c85c51868aa078d954db85efccdf2917a2b9e5c5b25766406e6b1debc6c was read. The revision changes status and adds Section6. The exact root theorem and separate scalar case are unchanged. The matrix interpretation now cites confirmed A2790-A2791. The reference to two bounded searches asserts no universal result, and this audit does not newly certify those numerical runs.

All added reading-scope statements distinguish this audit from the submitting agent's own reading. The retained delta and hashes are in the team records and in the team records. This revision needs no new mathematical computation.
