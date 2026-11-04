# Sparse support without power integrability

## Statement

There is a smooth nonzero divergence-free U on R3 tending uniformly to zero at infinity whose velocity and vorticity are supported in a fixed-width tube around a half-line. The nonzero-vorticity set occupies volume O_C(R) in each shell R<|y|<CR, C>1 fixed. Nevertheless neither U nor curl U belongs to any Lp with finite p>0, and DU is unbounded. The field fails the rotating Euler profile equation for every c>0 and every omega, whatever pressure is chosen.

This is a counterexample between hypotheses for general vector fields, not a counterexample to a profile theorem.

## Construction and proof

Choose a smooth cutoff chi supported in the unit ball and identically one in the ball of radius 1/2. Set, for integers n>=2,

    a_n=3n e3, epsilon_n=1/log(n+1), k_n=exp(n^2),
    f_n(y)=(epsilon_n/k_n) chi(y-a_n) cos(k_n y1),
    U_n=curl(f_n e3), U=sum_n U_n.

The supports are disjoint and locally finite, so U is smooth and divergence-free. The estimate sup|U_n|<=epsilon_n(1+||Dchi||_infinity/k_n) proves uniform decay. Support lies in the union of the unit balls centered at a_n, hence in a fixed tube. Only O_C(R) such balls meet a large shell, giving its claimed support volume.

On Q_n=a_n+[-1/4,1/4]^3 the cutoff is one and

    U=(0,epsilon_n sin(k_n y1),0),
    curl U=(0,0,epsilon_n k_n cos(k_n y1)).

For each p>0, integration over complete periods gives positive constants d_p independent of n such that the integrals of |sin(k_n s)|^p and |cos(k_n s)|^p on [-1/4,1/4] exceed d_p. The smallest k_n is exp(4), so discarding at most two incomplete periods leaves a uniformly positive fraction. Therefore

    integral_Q_n |U|^p >= C_p epsilon_n^p,
    integral_Q_n |curl U|^p >= C_p (epsilon_n k_n)^p.

The first series diverges because (log(n+1))^{-p} eventually exceeds n^{-1/2}; the second has terms tending to infinity. At a_n, partial_1 U_2=epsilon_n k_n, proving unbounded DU.

Finally, at a_n one has U=0, Omega=epsilon_n k_n e3, DOmega=0, partial_3 U=0 and J Omega=0. The curl of the profile momentum residual is

    Omega+B.grad Omega-(Omega.grad)U+omega J Omega=epsilon_n k_n e3,

which is nonzero independently of c and omega. A pressure gradient cannot cancel this curl. This completes every stated property.

## Scope and evidence

This confirms LIT22. It explains why a support-density hypothesis alone is different from integrability or derivative bounds for arbitrary fields. Within the exact profile class, CO7 uses the additional B invariance of the vortical set, which this example lacks. No finite numerical sampling or computation is part of the proof.

Audit date: 2026-11-02T19:37:03Z. Source: in the team records.
