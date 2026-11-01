# A convergent seventeenth-harmonic branch at delta6/13

Status: PROVED inV528. The complete all-index cover, exact majorant box and independent1024-bit replay passed at18:32Z, after the independent specialization review18:06Z.

All numerical response bounds and majorant boxes below use the unit leading profile, epsilon=1. For general nonzero epsilon, sigma_k scales by epsilon^Q and its absolute lower bound by |epsilon|^Q; the stated exterior radius already includes the resulting amplitude scaling.

## Statement

Set delta=6/13, c=13/7, and f_1(theta)=epsilon sin(17theta), for real epsilon!=0. Let sigma_k be the response of the next compatibility coefficient to the unit homogeneous stream mode at order13k. If |sigma_k|>=s>0 for every integer k>=1, the uniquely tuned density, stream and common-potential series converge with all appropriately weighted derivatives on a sufficiently large strict exterior. For a verified majorant box at w=z^13=r^-6=2^-q, a sufficient exterior is

    r>=R>2^(q/6)|epsilon|^(13/6).

No logarithm is needed in the common potential at this exponent. The leading density changes sign. No positivity or whole-plane extension is claimed.

## Proof before computation

Here h=3, Q=13, M=Q+2h-2=17 and B=M+1=18. The support theorem231 gives f_13 frequencies in17S_13+E_12, whose modulus is at least5. The first compatibility frequency is2h-3=3, so it vanishes identically. Earlier inverse operators are nonresonant. The affine-response theorem144 fixes each later free harmonic once the response hypothesis is established.

The finite-prefix majorant172 applies to the first13 density norms with no earlier free harmonics. It uses the particular inverse bound L=3*13^2/[4(3*13-1)]=507/152 and

    kappa=18*(2-delta+max(delta,1-delta))*(1-delta)/delta*(14/13)=7938/169.

An exact nonnegative supersolution bounds all later coefficients geometrically. Each fixed derivative adds polynomial factors, which are absorbed by the strict exterior inequality. Since h>=3, neither exceptional common-potential exponent occurs at an integer series order, so the reconstructed potential is a pure power series. The standard reconstruction and absolute product convergence give the stationary equation. Homogeneity in epsilon gives its stated exponent13/6.

## Complete certificate

The unit carrier has frequency6k-2. The compact response identity149 is valid once6k-2>=BQ=234, hence for k>=40. The finite part is1<=k<=39. The tail samples t_k=1/(6k-2) lie in[0,1/238]. A complete rational dyadic partition, with interval bounds234 and discrete leaves232, must separate all these samples from zero by the same final s. A finite sample or nonzero limiting response alone is insufficient.

The replay must reconstruct the integer coverage, reevaluate every accepted leaf and finite response at higher precision, compare the low interval prefix with a separately written exact Cartesian recursion, and verify the majorant box using rational arithmetic. The claim stays conditional if any of these tasks fails.

Dependencies:01,144,145,149,169,172,231,232,234. This exponent lies strictly between2/5 and1/2 but is not Candidate007's stored exponent.

The initial degree-two cover was stopped because cancellation forced excessive subdivision. Its partial partition and actual runtime are retained. The replacement uses degree-five Taylor enclosures, justified by the same general jet theorem234, and a smaller initial positive response threshold; singleton samples may lower that threshold further. The completed partition and every degree-five enclosure subsequently passed the fresh higher-precision replay described below.

The theory part reviewed and accepted this specialization as a conditional theorem at18:06Z. The later arithmetic admission below discharges its response and majorant hypotheses.

## Completed verification and quantitative conclusion

The unit responses satisfy |sigma_k|>2^-45 for every integer k>=1. The complete partition has22 singleton leaves and16 degree-five Taylor leaves, with no empty leaves. Its768-bit construction was independently replayed using manual Taylor jets at1024bits. The replay checked6,209 exact Cartesian prefix coefficients, all39 finite responses and all38 leaves. Every interval endpoint and integer range was reconstructed, and the leaves form the entire interval[0,1/238].

The exact rational supersolution at w=2^-334 passes all component inequalities. Its independent reconstruction also passes78 direct scalar coefficient identities. Therefore a sufficient exterior is

    r>=R>2^(167/3)|epsilon|^(13/6).

The branch has pure density, stream and common-potential power series, with every appropriately weighted derivative convergent there. The necessary lower-radius constant from245 is now attached to this proved branch: any exterior of absolute convergence must have R at least0.49543724057280308957... times |epsilon|^(13/6), with the exact constant defined in245. This is a lower bound, not a determination of the convergence boundary.

The stability theorem243 applies to this center on every fixed finite odd17 lattice, giving a neighborhood of compatible leading profiles with uniformly positive responses and a common sufficient exterior. The theorem gives a qualitative neighborhood, not a numerical perturbation radius.

The native construction took329.06seconds; the independent replay took1296.97seconds. Exact inputs, hashes and the admission gate are in verification/admission.json. The earlier incomplete attempts are retained as computation history and are not proof inputs.
