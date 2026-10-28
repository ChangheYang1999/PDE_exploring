# Independent audit clarifications

Recorded 2026-10-28T14:54:45.210262+00:00. All eight checks and eight findings of the independent audit were read and assessed.

Use chi_far for the cutoff in tail estimate (1), equal1 on B1 and0 outside B2. Use chi_org for the cutoff in the origin extension (2), equal1 on B_(1/2) and0 outside B1, as in proof 202. These are separate fixed radial cutoffs. The origin extension and support assertions always use chi_org.

The sharp velocity estimate U[zeta]=O(r^k(1+log r)), with fixed cylinder derivatives, follows by differentiating in q the explicit nonresonant homogeneous modal solution r^(q+1)P_q of proof 35. Its finitely many denominators remain nonzero near q=k. Compact transition differences contribute only decaying exterior multipoles. Differentiation therefore produces one log r and differentiates smooth modal coefficients, proving the bound used in the tail rate. The weaker O(r^(q_*)) estimate in proof 167 alone would not justify that exact displayed rate.

The sign n'_0>=3 follows from the positive certified angular strain moment in proof 31 and the nonnegative cutoff moment in proof 35; this proof only needs n'_0 nonzero. Near0, differentiate n'_0 m0=c[zeta]x^2E+R_zeta.grad rho0. The bounds E=O(r^3), DE=O(r^2), R_zeta=O(r^3), DR_zeta=O(r^2), grad rho0=O(r^2), D grad rho0=O(r) give partial_x m0=O(r^4). For the origin column norm use directly min(C delta^2 d,2C delta^3)<=C delta^(3-alpha)d^alpha on the divided cofactor. This handles close crossing pairs as well as distant ones. The rank-one commutator has rank at most two, an alternative reason that it cannot cure the previously proved noncompactness.
