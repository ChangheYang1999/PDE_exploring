# A single seventh harmonic at delta=4/5

Status: PROVED in V504 after the complete certificate, independent exact and1024-bit replay V503, and the theory part specialization review at17:43Z.

All numerical response bounds and majorant boxes below use the unit leading profile, epsilon=1. For general nonzero epsilon, sigma_k scales by epsilon^Q and its absolute lower bound by |epsilon|^Q; the stated exterior radius already includes the resulting amplitude scaling.

## Statement to be certified

Set delta=4/5 and c=5, and let f_1(theta)=epsilon sin(7theta), with real epsilon!=0. If all compatibility responses satisfy |sigma_k|>=s>0, k>=1, there is a unique tuned pure density and stream sequence converging on a strict exterior with all appropriately weighted derivatives. A complete exact majorant box at w=z^5=r^-4=2^-q yields the sufficient exterior

    r>=R>2^(q/4)|epsilon|^(5/4).

The common potential is reconstructed with its exceptional order5 logarithmic term when required. This is a sign-changing exterior profile, without a claim of whole-plane extension, positivity or optimal radius.

## Argument before computation

The support theorem231 applies with h=2, Q=5 and M=Q+2h-2=7. At order5, every density frequency belongs to7S_5+E_4 and has modulus at least3. The first obstruction frequency is1, so first compatibility holds identically. No earlier stream inverse is resonant. The density bandwidth is8n-1.

The affine response theorem144 determines each later harmonic from the next compatibility condition whenever sigma_k!=0. The complete lower bound supplies the denominators required by145. The finite-prefix majorant172 uses the first five density norms, no previously free harmonics, B=8, the particular inverse bound L=3*5^2/[4(3*5-1)]=75/56, and

    kappa=8*(2-delta+max(delta,1-delta))*(1-delta)/delta*(6/5)=24/5.

Every initial value is an outward rational upper bound on n||f_n||_1. An exact nonnegative supersolution gives convergence in w. Each fixed derivative costs polynomial factors in n and is absorbed on a strict exterior. The common-potential theorem gives convergence of the reconstructed potential with the permitted logarithm. Homogeneity gives the amplitude factor |epsilon|^(5/4).

## Complete response and independent checks

At the kth stream resonance, the unit harmonic has frequency4k-2. The compact response formula149 agrees with the full response when4k-2>=BQ=40, hence for k>=11. Direct finite evaluation covers1<=k<=10. The remaining t_k=1/(4k-2) lie in[0,1/42]. A rational dyadic partition with the singleton and interval rules232 proves a common lower bound at every such integer. Taylor intervals use234.

The independent replay must reconstruct all rational endpoints and integer ranges, reevaluate every nonempty leaf at higher precision, and check the finite responses. A separate exact Cartesian recursion provides all first-five density and first-four stream coefficients and their norms. Rational evaluation of the majorant supersolution and scalar coefficient identities completes the check. A failed or unfinished check leaves the corresponding result open.

Dependencies:01,144,145,149,169,172,231,232,234. No finite sample is substituted for the complete integer cover.

## Completed certificate

The first compatibility is identically zero. Every later integer response has modulus greater than2^-20. The certificate has11 singleton leaves and2 Taylor leaves beyond k11, and10 direct finite responses. A separately written exact Cartesian prefix agrees at445 checked coefficient positions. The1024-bit replay verifies all responses, the rational integer partition and the exact majorant box with N5 and q80. Thus the sufficient exterior is

    r>=R>2^20 |epsilon|^(5/4).

The result includes all weighted derivatives and the common potential with its permitted finite logarithmic term. No optimality is asserted.
