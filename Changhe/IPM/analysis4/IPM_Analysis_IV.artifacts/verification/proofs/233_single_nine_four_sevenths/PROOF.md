# A candidate sin(9 theta) branch at delta=4/7

Status: PROVED in V497. The complete response and majorant certificate and independent replay pass; the theory part accepted the specialization17:37.

All numerical response bounds and majorant boxes below use the unit leading profile, epsilon=1. For general nonzero epsilon, sigma_k scales by epsilon^Q and its absolute lower bound by |epsilon|^Q; the stated exterior radius already includes the resulting amplitude scaling.

## Statement to be certified

Set delta=4/7, c=7/3 and f_1(theta)=epsilon sin(9 theta), with nonzero real epsilon. Define sigma_k as the response of the coefficient of sin((4k+1)theta) in f_(7k+7) to the homogeneous stream coefficient H_(7k) of sin((4k-2)theta). If |sigma_k|>=s>0 for every k>=1, the uniquely tuned pure density and stream series converge on a sufficiently large exterior with all appropriately weighted derivatives. The common potential has the same strict exterior after its finite exceptional logarithmic correction is included.

For an exact prefix-majorant certificate with residue variable w=z^7=r^-4 and box parameter w=2^(-q), a sufficient exterior is

    r>=R>2^(q/4)|epsilon|^(7/4).

The leading density changes sign in the first quadrant. This statement does not assert positivity, a whole-plane extension, or that the sufficient radius is the true radius.

## Proof of the conditional statement

Topic231 gives first compatibility: at order7 every density frequency belongs to9S_7+E_6, so its modulus is at least3. The obstruction frequency is1 and its coefficient vanishes identically. Before this order the stream inverse has no resonance. The leading bandwidth is B=10.

The response hypothesis now gives every unique harmonic H_(7k) by the affine compatibility equation of144. The rational majorant145 applies. In the finite-prefix form172 its initial data are the first seven density norms and no previously free harmonics. The sharp particular Poisson bound169 is

    L=3*7^2/[4(3*7-1)]=147/80.

The nonlinear prefactor is

    kappa=10*(2-delta+max(delta,1-delta))*(1-delta)/delta*(8/7).

Exact rational upper bounds on n||f_n||_1 supply the fixed prefix. Any verified nonnegative supersolution of the transformed majorant at2^(-q) gives the stated strict exterior. Polynomial derivative factors are absorbed by its strictness. The common-potential reconstruction in145 gives the same radius, allowing the exceptional logarithm rather than assuming it vanishes. Homogeneity replaces z by epsilon z and gives |epsilon|^(7/4).

## Proposed response certificate

The full carrier and compact formulas coincide for4k-2>=BQ=70, hence for k>=18. The full response calculation checks1<=k<18. Topic232's finite rational partition of0<=t<=1/70 checks the remaining integers t_k=1/(4k-2), using interval, singleton and empty leaves. Every nonempty leaf must establish the same final positive s. A separately written audit reconstructs all endpoints and integer bounds and recomputes the nonempty enclosures at higher precision.

An exact signed-Laurent implementation reconstructs all first-seven density and first-six stream coefficients and compares them with the interval prefix. It uses exact Cartesian differentiation and rational Poisson division. Each Poisson result is checked against the differential equation. These are finite implementation checks; the all-order assertion depends on the complete certificate and the already proved majorant theorem.

## Evidence and scope

The finite probe is in231. The certificate and its independent replay will be retained here. A failed probe, incomplete partition, unsuccessful supersolution or failed replay leaves the corresponding all-order claim open. No termination or optimality claim is made for the search.

Dependencies:01,144,145,169,172,231,232. The proof above is conditional on the explicitly stated response bound until those checks finish.

The implemented interval leaves use the validated degree-two Taylor enclosure of234. Singleton leaves still use direct point evaluation. The independent replay checks the recorded enclosure method and recomputes it at1024 bits. The original unexecuted natural-interval versions are retained in sources.

## Completed certificate

V495 and V497 certify s=2^-25 and q=147. All40 tail leaves,17 finite responses,1045 exact low coefficients and the majorant supersolution passed the separate1024-bit replay. The preceding proposed-check descriptions record the method; their conditions are discharged.
