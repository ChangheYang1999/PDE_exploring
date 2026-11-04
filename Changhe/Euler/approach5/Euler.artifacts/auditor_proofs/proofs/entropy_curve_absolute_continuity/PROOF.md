# Entropy controls the limiting conditional measures on nonconstant curves

## Statement

Let D be a compact embedded C1 curve with normalized arclength lambda in a compact smooth Riemannian manifold M. Let g be a C1 diffeomorphism. Let P^ell be nested finite interval partitions of D, modulo lambda-null boundaries. For measurable E_n with m_n=lambda(E_n)>0, put eta_n=lambda|E_n/m_n and L_n=log(1/m_n)=o(n). Choose integers N_n tending to infinity with N_n/n ->0 and N_n L_n/n ->0.

For each n and 0<=ell<n select whole atoms P of P^ell. Give the embedded image g^ell(P) a C1 parametrization gamma_(ell,P) on [0,1]. Assume all these parametrizations lie in a fixed compact C1 class C, and that for one constant D0,

    (g^ell)_*(lambda|P/lambda(P)) <= D0 lambda_gamma,

where lambda_gamma is normalized image arclength with multiplicity. Assume also that every descendant Q in P^(ell+N) of a selected parent has diameter(g^ell(Q))<=epsilon_N, where epsilon_N ->0.

Let rho_(n,ell,P) be the pullback to [0,1] of (g^ell)_*(eta_n|P/eta_n(P)). Form the finite measure

    p_n=(1/n) sum_(ell,P selected) eta_n(P) delta_(gamma,rho).

Its mass is at most one. Along any convergent subsequence let p be the limit on C times the parameter probability space, q its curve marginal, and theta the image of p under (gamma,rho) -> delta_gamma times gamma_*rho. On C_+={gamma:length(gamma)>0},

    theta << q(dgamma) lambda_gamma(dx).

No conclusion on constant limiting curves is included. All hypotheses are finite-time geometric or measure assumptions; no Euler equation enters.

## 1. Relative entropy bound

Fix n and abbreviate eta=eta_n, N=N_n. Put

    H_ell=sum_(P in P^ell) eta(P) log(eta(P)/lambda(P)).

By Jensen and eta<=lambda/m_n, 0<=H_ell<=L_n. For one parent P, write p_Q=eta(Q)/eta(P) and q_Q=lambda(Q)/lambda(P) on its level-(ell+N) descendants. Call Q bad if p_Q>K q_Q, for fixed K>1. Write b_P=sum_bad p_Q and d_P=sum_bad q_Q<=b_P/K.

The log-sum inequality applied to bad and good groups gives

    KL(p||q)>=b_P log(b_P/d_P)
             +(1-b_P)log((1-b_P)/(1-d_P))
            >=b_P log K-log 2.

Zero terms are interpreted by continuity. The chain rule is

    H_(ell+N)-H_ell=sum_P eta(P) KL(p_P||q_P).

Summing for 0<=ell<n-N telescopes along the N residue classes, giving at most N L_n. Therefore

    (1/n) sum_(ell<n-N) sum_P eta(P)b_P
          <= [N L_n/n+log 2]/log K.                 (1)

The same upper bound holds after restricting to selected parents.

## 2. Retain all parent weights

For each selected parent at ell<n-N restrict rho to its good children, obtaining a subprobability rho^K. Keep the original parent weight eta(P)/n, even when rho^K has mass zero. Delete the last N time indices. Let pcheck_n^K be the resulting measure on C times parameter subprobabilities, and thetacheck_n^K its joint image measure. Then

    0<=thetacheck_n^K<=theta_n,
    mass(theta_n-thetacheck_n^K)
       <=N/n+[N L_n/n+log 2]/log K.                 (2)

The curve marginal of pcheck_n^K loses only the deleted time indices, of mass at most N/n. This distinction is essential: lost conditional mass does not change the parent weights.

For a nonnegative Lipschitz h on M, choose one point in the image of each descendant. Its oscillation on that image is at most epsilon_N Lip(h). Since p_Q<=Kq_Q on good children, summing and using the distortion assumption gives

    integral h d(gamma_*rho^K)
       <=K D0 integral h d lambda_gamma
          +(K+1)epsilon_N Lip(h).                 (3)

This proof needs neither a density lower bound nor control of normalized conditionals with changing marginals.

## 3. Passage to the limit

Extract a common subsequence for K=exp(j), j=1,2,... . Compactness of C and of the probability and subprobability spaces on [0,1] gives limits. Evaluation of any continuous joint test at (gamma,gamma(t)) is continuous in the C1/weak topology. Thus the joint image measures converge and

    0<=thetacheck^K<=theta,
    mass(theta-thetacheck^K)<=log 2/log K.          (4)

The curve marginal of pcheck^K is exactly q.

The length functional is C1-continuous. On C_+, gamma ->lambda_gamma is weakly continuous, because its numerator is integration against |gamma'|dt and its denominator stays positive locally. Apply (3) to a countable dense family of nonnegative Lipschitz tests. A strict violation of its limiting inequality has an open neighborhood with length bounded below and a fixed violation margin, so is eventually excluded by (3). Portmanteau makes that neighborhood null for pcheck^K. It follows that

    gamma_*rho^K<=K D0 lambda_gamma

for pcheck^K-almost every pair over C_+. After integrating using its curve marginal q,

    thetacheck^K|C_+ <=K D0 q(dgamma)lambda_gamma(dx).

If A is null for the right-hand reference measure, (4) gives theta(A)<=log 2/log K for every K=exp(j). Let j tend to infinity. This proves the asserted absolute continuity and, by standard disintegration, its conditional formulation.

If a bounded increasing family of joint measures has this property, put all its curve classes in their countable disjoint union. The limiting curve marginal dominates each finite marginal; therefore each joint measure is absolutely continuous on the nonconstant locus with respect to the limiting reference measure. Their increasing limit retains this property.

## 4. Noncollapse is a separate condition

Take g to be the identity, E_n=D, and P^ell the dyadic interval partitions. Select all atoms and parametrize them affinely. All assumptions hold with distortion one and epsilon_N proportional to 2^(-N). The averaged limiting curves are constant, although the ambient limiting measure remains lambda. This example has no positive derivative growth. It refutes only the inference that these geometric assumptions alone prevent constant limiting curves.

## Dependencies and scope

The argument uses finite relative entropy, its chain rule and log-sum inequality, compactness, and weak convergence. It confirms the abstract LIT52 lemma. Applying it to the external dynamical manuscript requires genuine C1 compactness, the stated distortion and descendant-diameter estimates. The source's printed modulus-only derivative seminorm does not by itself give that compactness; see the separate counterexample audit.
