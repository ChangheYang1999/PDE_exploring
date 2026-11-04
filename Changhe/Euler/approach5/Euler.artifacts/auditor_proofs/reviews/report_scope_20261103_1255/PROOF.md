# Interim report scope corrections

Status: the precise corrections below are independently confirmed; this is not a complete audit of the draft.

## 1. Escaping W2 traces

At global C2/C1 Euler, zero helicity and both natural velocity and derivative bounds, an escaping W2 connection trace has a scattering direction w with V(w)=W(w)=0 and w in supp W. The established trace formulas do not determine DV(w). If DV(w)=0, this point is in Tflat. If DV(w)!=0, it is a nonflat irrotational velocity zero. Thus the draft's unconditional description of the W2 trace as flat in Section10 is not licensed by A830. No actual Euler counterexample to flatness has been constructed, and the mathematical flatness question stays OPEN.

For the nonflat case one must still distinguish the interior of {k=0} from the complement of the closure of that interior. A973 excludes a nonflat boundary point. The local nodal mass estimate A832 applies to the latter region, where its nodal premise holds. It does not apply inside an open zero region. See the complete independent proof in the team records, A981-A983.

## 2. Backward-time vorticity sign

The exact carrier vorticity equation is (B.grad)Omega=DU Omega-Omega-omega J Omega. Wherever sym DU=0 along an orbit, taking its scalar product with Omega gives d|Omega|^2/dt=-2|Omega|^2. Hence |Omega(Phi_t y)|=exp(-t)|Omega(y)|. The norm grows as t tends to minus infinity. A nonzero value therefore contradicts compact backward trapping and continuity. The draft's phrase that it decays along the backward carrier flow must be replaced by this directionally correct formula. The cited contradiction is sound after this repair.

## 3. Superseded conditional criterion

For 2/5<c<1/2 and every finite real omega, assume global C2/C1 Euler, zero helicity and both natural bounds with p=(1-c)/c. A1018-A1021 prove that absence of a supported flat velocity zero alone implies U=0. No additional assumption that k is not identically zero is needed. The draft's older two-alternative criterion is weaker but not false. The standalone proof is in the team records. This does not exclude supported flat zeros or remove the helicity and derivative assumptions.

A1022 and A1041-A1045 additionally fix the original rate at an actual vortical velocity zero to rho=-2(1-c). This applies to escaping W1 half-lines under the full tail hypotheses. It does not replace the bound rho<=-2(1-c) for an escaping W2 trace, whose full tail vorticity vanishes.

## 4. Evidence and scope

The excerpt in the team records preserves the exact inspected wording. Its source hash and real inspection time are in the team records. Earlier complete independent proofs supply the mathematical dependencies. No formal build, numerical computation, outside-agent edit or whole-report certification was performed. LIT201 is a separate newly submitted strengthening and is not presumed in these corrections.
