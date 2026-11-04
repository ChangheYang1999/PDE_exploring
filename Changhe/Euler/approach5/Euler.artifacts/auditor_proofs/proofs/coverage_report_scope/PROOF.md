# Exact scope of the smooth-coverage reduction in the draft report

## 1. The class and the verified equivalence

Fix c in (2/5,1/2) and an arbitrary finite omega. Let C_infinity denote all pairs (U,P) solving the exact divergence-free rotating Euler profile equation on R3, with U in C-infinity, P in C1 and U(y)->0 uniformly. For each such profile, A308 together with A207/A223 gives an at most countable family of compactly supported full-flow-ergodic vortical SRB probabilities and their invariant open essential basin domains D_i, whose union covers {curl U!=0} modulo a null set. Topological supports may meet the zeros of B or curl U.

The following statements are equivalent:

    (N) Every profile in C_infinity has U=0.
    (S) There is no profile in C_infinity with an essential basin D_i
        on which h=U.curl U takes both strict signs.

If(N) holds, there are no vortical essential basins and(S) follows. Conversely, suppose(S) holds and choose any profile. Each D_i then carries at most one sign of h, possibly a different sign for each i. A309 gives U=0. Equivalently, every nonzero profile in this exact class has AT LEAST ONE such basin with both signs. Continuity makes each strict-sign region a nonempty open positive-volume set. No implication about every basin is used.

This checks draft report item1c(i)-(ii), its opening Section7 reduction, and the explicit C-infinity interpretation of Note18 item2. The finite-r extension in the report must retain A312's quantitative condition. These statements supply neither regular-attractor coverage nor a classification of all topological supports.

## 2. The prompt's C2 baseline remains a separate open scope

The prompt does not authorize silently treating C-infinity as the whole target class. Its regularity paragraph explicitly says to start with U in C2(R3) and determine the weakest required regularity. Section8 again lists U in C2 among the actual target conditions for candidate examples. The report's own Section0 uses U in C2 and P in C1.

Therefore Note18 item1's assertion that C-infinity is the posed class and is not a restriction is incorrect as a reading of the task. A308 proves a strong result for the C-infinity subclass. It does not show that every C2 profile is automatically smooth, and no such bootstrap is supplied. The exact equivalence in Section1 is established for C-infinity profiles, or for the quantitatively restricted finite-r class, not for all C2 profiles requested at the start of the prompt.

A precise replacement is: For C-infinity profiles the remaining issue is a sign-changing essential basin; for the original C2 baseline both the coverage step and the unrestricted nonexistence problem remain open. The draft already mostly makes this distinction. Its sentence that neither part is available at C2 should be read as neither is asserted from C2 and decay alone. The given-basin conditional theorem A278 and the complete recurrent-vortex argument A283 do hold at C2.

## 3. Recurrence does not give nonmonotonicity on almost every basin line

A283 states that there is a full-volume recurrent set R such that each x in R with h(x)!=0 sees both helicity signs arbitrarily far in both vortex-time directions. It also proves that one sign on a forward-invariant open domain forces h=0 there. These statements do not imply that H is nonmonotone on almost every vortex line of an essential basin merely because h changes sign somewhere in that basin.

In particular, the available theorem does not rule out a positive-volume family of vortex lines on which h is identically zero. No ergodicity of the infinite-volume vortex flow on the whole essential basin has been proved. Ergodicity of the backward-carrier SRB probability is a different statement about a different flow and measure. Nor has nonzero helicity at almost every basin point or on the SRB support been shown.

The safe statement is: Almost every basin point is recurrent under the vortex time-one map; each recurrent point with nonzero helicity lies on a vortex line along which H is nonmonotone, and such points exist in each nonempty open strict-sign region. Thus nonmonotone lines occur on a positive-volume vortex-invariant subset. The stronger almost-every-line assertion in Note18 item2(c) and the end of the report Section10 remains OPEN and must not be attributed to A283.

The pending same-level recurrence proposal, if confirmed, strengthens the crossing values on one recurrent orbit. It does not fill this almost-every-line gap.

## 4. Dependencies and report status

This is a logical and hypothesis audit using the fully checked A308, A309, A207/A223 and A283. Full source snapshots and hashes are retained in the team records. The unrestricted Euler conjecture remains OPEN in every regularity class under discussion. No numerical, source-retrieval or model-substitution claim is involved.
