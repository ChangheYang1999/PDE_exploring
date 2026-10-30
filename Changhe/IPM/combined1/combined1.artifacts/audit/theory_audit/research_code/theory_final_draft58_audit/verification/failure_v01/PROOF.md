# Theory draft 58 and R1-052: independent acceptance

Written 2026-10-29T17:40Z before the checker. This result concerns THEORY_FINAL draft 58, sha256 f76c41fb4e5f3733e5f0ac2749120c80a9771349b97ab83f61bcfe86c059f91f, and R1-052 in review set 51, sha256 3198103bab14c90646fcaf4ba163dc739cc6abcccd2595694226e1ac2022127f. All 31 changed blocks against the accepted draft 55 were read. No peer program is executed. The preparation's expected draft 56 had already been superseded before copying; that failed expectation is preserved, and this proof concerns the frozen draft 58 only.

## Statement, hypotheses and dependencies

Accept R1-052's finite recomposition under the whole-field premises already established in T4-467, T4-472, T4-477, T4-480, T4-481, T4-486 and T4-488. The candidate is the exact saved C1-N1-016-legqs25-quot013, raw hash a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42. Its residual F is real, locally integrable, even in x and odd in y, with rF in L2(R2). Its full radial branch register has 1360 branches and 160 odd angular modes. The gradient dual and solenoidal estimates use the canonical homogeneous negative norm H=||F||_{dot H^{-1}}. The complete forcing norm is

    E2^2=P2^2+2^14 G1^2+2^18 G0^2+(20/21)2^18 H^2.

These definitions and the component weights are fixed across the comparison with 007. The sixteen radial mode integrals, the 2130 pairing groups and the exact mode energies are accepted input certificates, not new integration claims. T4-486 independently replayed the pairing intervals. T4-480 independently replayed the prefix integrals. T4-477 and T4-481 accepted both Opus reviews of the analytic upper bounds. T4-488 accepted the complete endpoint assembly. Each cited source is bound in the JSON manifest or in the two README archives. The earlier archive is reused from the own-lane draft-55 audit; the new archive stores only changed members.

The draft's numerical and analytic repairs are confirmed within the scopes proved below. One universal sentence about selected-threshold forcing factors is still literally false, because the same paragraph explicitly gives a sharpw forcing factor against eta*. Replace it, including its quotation in item 87 and the review acknowledgement, by: "Unless expressly compared with eta*, the sharpw forcing factors use the selected threshold 2.1035e-4." This wording change affects no bound or verdict.

## Complete argument for R1-052

For n=1,3,...,31 write q_n for the radial weighted residual square, L_n for its selected strict gradient-dual floor and J_n for its selected strict solenoidal improvement. Selection chooses one accepted floor of each kind at a given frequency. It never adds two trials at the same frequency. Distinct frequencies are orthogonal. Let qU_n bound q_n above, let RU bound ||rF||2^2 above, and put N=33. The complete prefix-tail inequality from T4-474 is

    V=RU/N^2+sum_n(1/n^2-1/N^2)qU_n >= sum_all_modes q_n/n^2.

All 144 omitted frequencies have n>=N. The coefficient 1/n^2-1/N^2 is positive at each included frequency. Thus upper endpoints enter with the correct sign and the omitted tail remains in the bound. Applying the accepted solenoidal improvement at the sixteen distinct frequencies gives

    L=sum_n L_n^2 < H^2 < U=V-J,   J=sum_n J_n.

The exact finite sums give J=60190270781084901078904854514861671131/(25*10^37), L>0.380360210930, V<0.622626936301 and U<0.381865853176. These are the producer's accepted outer prefix endpoints. They can differ from a tighter independent enclosure while proving the same directed displays, as T4-488 explicitly explains. J_1+J_3 equals the previously accepted two-mode improvement, and J-(J_1+J_3)>0.002101926.

Squaring the positive rational endpoints establishes

    308366750368225240013184170643/(5*10^29) < H(016)
      < 154488238463271634620877708271/(25*10^28),
    628580088526341/10^12 < E2(016)
      < 314439512374259/(5*10^11).

For E2, substitute the component lower bounds and L into the defining positive sum for the lower square, and the component upper bounds and U for the upper square. Every coefficient is positive. The squared endpoint comparisons are strict. In particular the directed displays 0.616733500736<H(016)<0.617952953854 and 628.580088526<E2(016)<628.879024749 are valid. Subtract the accepted E2(007) upper 606820219/10^6 to obtain E2(016)-E2(007)>21.759869526341. Subtract the H(016) upper from the lower endpoint of the accepted H(007) ball to obtain H(007)-H(016)>0.017571422147005. The older coarser displays are therefore valid too. Opposite orderings of these two norms do not order the unknown correction distances.

The width identity is algebraic. Define g_n=qU_n/n^2-J_n-L_n^2 and t=(RU-sum_n qU_n)/N^2. Expanding V gives

    U-L=sum_n g_n+t.

Every g_n and t is positive for these accepted endpoints. The finite sums satisfy sum_{n<=15}g_n<10^-9, sum_{17<=n<=31}g_n<0.000980734, t<0.000524909 and U-L<0.001505643. The strict H endpoint width is below0.001219454. The last eight selected modes and the tail contribute shares that round respectively to0.651 and0.349. These shares describe differences of certificate bounds. They are not per-mode norm enclosures or residual-energy proportions. The later the N3 numerics worker values involving unaccepted modes33to63 lie inside these intervals as numbers; that location supplies no certification of their source claims.

## Draft repairs and scope

All changed blocks are enumerated in data/changes.json. The checker verifies their exact positions against the two frozen drafts. The repair of the cumulative check count is correct:13 after the first part and20 after the second means20 checks total. The README's row-reference and verdict scripts now name the matrix v157 they actually read. All186 README entries have matching bytes, with177 reused from the old archive and9 stored in the delta archive. The83 candidate-row references and78 directed distance-factor floors remain correct; the108-row matrix preserves the OPEN rows for011,027and028.

The accepted T4-491 audit establishes the BS repairs: AJ2 is confirmed only with unchanged high-row margin and norm domination; WU3's factors use T2-R3 beta2 and T2-R1 beta11/4 respectively; its matrix-floor hypotheses remain9/10 and1/2; the closure requires beta(r)>0, a strict contraction and a positive slope margin; each ALT defect budget names its box. The displayed K_H uppers9.6432and6.4226 bound the exact reciprocals121000000/12551327 and405000000/63092119. Direct substitution into c_s=(4*pi*s*(1+s))^(-1/2), with sharp(s,r)=(1/7744,147/200000) and sharpw(s,r)=(1/5184,1351/10^6), gives slope margins above0.6817and0.6725.

AK2 is now identified specifically as the S1 squared Hessian velocity constant63/32 accepted in T4-301. Its proof uses only positive odd sine modes, the full ordered Cartesian Hessian and the canonical IPM multiplier. In the accepted Mellin decomposition, input energy is2(a+b), the velocity contributes the additional factor1/4, and Young parameters(1,4) give output energy at most(63/4)a+(61/4)b. Division gives63/32. The inhomogeneous squared weight follows by adding the unweighted, first-moment and second-moment squared estimates. It does not extend to arbitrary centrally odd inputs, nor supply an inverse or a normalization trace. This confirms the specific AK2 citation without certifying unspecified statements in the handoff.

T4-490 already independently proves that all five nonconstant degree-two and degree-four origin coefficients of saved007's F/y exceed2e-13 in magnitude. The draft correctly preserves the exact origin normalization and the separate tiny projection result. The first-mode007/013 descriptive correction is checked against the serialized FLOAT register only: the k<=128 extrema are about26.8456and9358.8589, and the later saved probes have improvements below2.1, including increases. Such decimal comparisons do not certify the underlying quadrature.

## Conclusion and limits

CONFIRMED: R1-052 under its stated, now accepted premises; the width identity and directed displays; all31 draft changes with the scoped repairs above,186 source bindings,83 matrix references and78 directed floors. REFUTED: the remaining universal selected-threshold sentence taken literally. OPEN:017's whole-field C1-C3, the later016 modes33to63 absent an independent replay, any ranking of actual correction distances, and existence near a registered candidate. The conditional a posteriori theorems retain all space, realization, normalization, positivity, inverse and nonlinear hypotheses. No numerical observation is promoted to an existence proof.
