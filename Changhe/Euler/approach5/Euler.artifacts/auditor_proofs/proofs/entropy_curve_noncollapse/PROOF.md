# Interleaved geometric families prevent collapse of selected curves

## Statement

Use D, lambda, eta_n, L_n, P^ell and the weighted selected curve measures of the preceding entropy lemma. Suppose there are finite family partitions Q^ell with

    P^(ell-1) coarser than Q^ell coarser than P^ell, ell>=1.

Every family contains at most A0 individual atoms, for a fixed integer A0. Certain families are geometric. For each geometric family F assume:

1. The sum of lengths of its images g^ell(P), P subset F, is at least v0>0.
2. The positive arclength Jacobian of g^ell on F has ratio of maximum to minimum at most D1.
3. Every selected atom at time ell belongs to a geometric family.

Assume the selected image parametrizations lie in a fixed compact C1 class and their lengths equal their image lengths. Then every weak limiting curve marginal q satisfies

    q{length<h}<=D1 A0 h/v0, h>0,
    q{length=0}=0.

There need be no lower bound for the length of an individual family member. This confirms the abstract assertion of LIT53.

## Proof

For a finite partition R define H(R)=sum_C eta_n(C)log(eta_n(C)/lambda(C)). It lies in [0,L_n]. Put K_ell=H(P^ell)-H(Q^ell)>=0. Interleaving and the entropy chain rule give

    sum_(ell=1)^(n-1) K_ell
      <=sum_(ell=1)^(n-1)[H(P^ell)-H(P^(ell-1))]<=L_n.       (1)

For a family F with eta_n(F)>0, let p_i and q_i be its conditional member probabilities under eta_n and lambda. For any subset I of the members, the binary log-sum inequality gives

    sum_I p_i <= sum_I q_i + sqrt(KL(p||q)/2).                (2)

Indeed the binary relative entropy as a function of p=sum_I p_i, with q=sum_I q_i fixed, has second derivative 1/(p(1-p))>=4 and is zero with zero derivative at p=q. Thus it is at least 2(p-q)^2. Endpoints follow by limits.

Let I be the short image members of a geometric family, with length less than h. Their total image length is at most A0 h. Comparing the arclength Jacobian above and below over F gives

    sum_I q_i <=D1 A0 h/v0.                                 (3)

Multiply (2) by eta_n(F), sum over geometric families, and apply Cauchy-Schwarz. The entropy chain rule over the family partition gives

    eta_n{short atoms in geometric families at time ell}
      <=D1 A0 h/v0+sqrt(K_ell/2).                            (4)

Selected short atoms are a subset. Average (4) over 1<=ell<n and use (1) and Cauchy-Schwarz again. The omitted time zero has mass at most 1/n. Therefore

    q_n{length<h}<=D1 A0 h/v0+sqrt(L_n/(2n))+1/n.             (5)

Because L_n=o(n), the error vanishes. Length is C1-continuous, so its strict sublevel sets are open. Portmanteau gives the same bound for q. Let h decrease to zero to obtain noncollapse.

## Source correspondence and its limits

The actual Ben Ovadia-Burguet manuscript's tree description on printed page 24 puts a whole child family inside one individual parent chart. Definition 3.8 provides the individual partition. Pulling both back to the initial curve gives exactly the interleaving above. A blue node has fewer than A_(r,d) members; its admissible union has length bounded below by Definition 3.6 and the following remark. The family lies inside the enclosing bounded chart theta-prime. Comparing the speed of sigma_ell there and the initial speed of sigma gives whole-family distortion at most two, provided the stated bounded-couple speed estimates hold. Definition 5.19 selects only blue nodes at unexpanded BG times.

These displayed properties were checked against the actual text. Their existence theorem and positive-density selection have not been reconstructed in full. In particular, genuine C1 compactness remains an explicit premise: the literal derivative-modulus seminorm on page 21 does not imply it.

The later phase-domination claim in LIT53 Section 5 is separate from this theorem. Expanded BG times in Definition 6.3 use an existential witness in a parent atom; they are not automatically future BG times of the same point. A separate audit addresses that issue and gives a fixed-M alternative. No full-source certification or Euler theorem follows from this lemma alone.
