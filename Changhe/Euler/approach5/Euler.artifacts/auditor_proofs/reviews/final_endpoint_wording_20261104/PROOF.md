# Distinguish the two derivative amplitudes in the final summary

## Exact statement and complete argument

Let U be a C1 divergence-free field on R3 with E(R)/(L R^beta) tending to one, where L>0 and 0<beta<1. Put t=(beta-3)/2, k=(beta+1)/2 and H=t^2(k^2+4)/(k^2+2). Write D for the full spatial limsup of |y|^((5-beta)/2)|DU(y)|, with the Frobenius norm, and put

    D_H^2 = beta L H/(4pi),
    D_*^2 = 9 beta L t^2/(4pi(k^2+2)).

Let G(R)=integral_(1<|y|<R)|y|^(2-beta)|DU(y)|^2. The ratio D_*^2/D_H^2=9/(k^2+4)>1. The Hardy-endpoint theorem A3149 assumes the additional limsup G(R)/(beta L log R)<=H and proves D>=D_*. Without that endpoint premise, A3150 proves D>D_H, allowing D infinite, and A3179 supplies a quantitative gap above D_H. In contrast, the explicit smooth control of A3157 has

    D_H^2 < D^2 = beta L M_d/(4pi) < D_*^2,
    M_d > H.

Thus it refutes extending the D_* lower bound to the energy-ratio class without the endpoint premise. It does not refute the D_H lower bound or its independently proved quantitative improvement. These conclusions follow directly from the displayed strict inequalities; no numerical approximation or limiting interchange is used. The control fails the full Euler profile equation for every c and omega, so it is not a counterexample to rotating-profile nonexistence.

## Report comparison, dependencies and scope

Theorem 8(o), frozen report cdeab661 lines1128-1173, explicitly defines both constants and gives the correct distinction. Section6 lines5421-5423 says only that under the energy law alone the endpoint amplitude is not a lower bound. Since the preceding sentences discuss D_H and its small quantitative improvement, that shortened phrase can be misread. Replace it by the larger endpoint value D_* of Theorem8(o), and state that the general lower bound D_H and its quantitative improvement remain valid. This is a clarification of an already correct detailed theorem, not a new result or a refutation.

The exact source passages are retained in the team records. The complete independent controls proof is in the team records, particularly Section4, and the endpoint argument is in the team records, particularly Section1. Those statements and the complete amplitude calculation were reread for this comparison. No claim to have freshly checked every supplementary source or computation is made. The report still awaits the separate A3230-A3231 hypothesis repairs.
