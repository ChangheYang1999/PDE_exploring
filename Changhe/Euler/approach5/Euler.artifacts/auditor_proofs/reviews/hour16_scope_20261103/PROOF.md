# Exact scope of the hour-16 strain target and completed jet work

Status: scope audit, not a new profile theorem. A513 records the verified dependency correction.

## 1. Setting and the confirmed strain criterion

Let U in C2(R3;R3),P in C1(R3) solve the full incompressible rotating Euler profile equation, with 0<c<1 and any finite omega. Write S=sym DU and lambda(y)=lambda_max(S(y)). A506 proves:

1. If U is bounded and limsup_(|y|->infinity) lambda(y)<1+c/2, then DU tends uniformly to zero.
2. If U tends uniformly to zero and, outside a ball,

       lambda(y)<=1+c/2+epsilon(|y|),
       epsilon>=0 bounded and integral_R^infinity epsilon(r)dr/r<infinity,

   then DU tends uniformly to zero.

The second conclusion depends on the displayed integral. It is not a criterion with an unspecified positive epsilon or with epsilon(r)->0 alone. The actual proof integrates the scalar vorticity inequality along the outward carrier flow and then uses A498. The complete independent proof is in the team records.

## 2. What the current packet leaves unspecified

The proposed derivative-decay target in the team records says to prove lambda_max(sym DU)<=1+c/2+eps or DU=O(r^(1/2)) from U->0. The second alternative matches A498(B) exactly. The first needs its error specified before it is a sufficient target under the current proofs. Acceptable forms already covered are the strict limsup inequality of Section1, or its critical Dini envelope.

This is a dependency limitation, not a counterexample to a new Euler implication. For example, a fixed epsilon0>0 in the pointwise strain bound yields only

    |W(y)|+|DU(y)| <= C(1+|y|)^(1/2+epsilon0/c)

from the confirmed transport estimate. It does not give the O(sqrt r) input to A498(B). An error epsilon(r)=1/log r for r>=e tends to zero but has divergent integral epsilon(r)dr/r; the direct transport estimate allows a logarithmic correction to sqrt r. Thus merely making the error small or convergent to zero does not validate the cited chain. Additional quantitative velocity decay could support other theorems, but is not assumed in the bare-decay target.

## 3. The jet-classification scope

A489 and A493 already confirm the universal local Lyapunov classification through orders four and five. The packet's earlier statement that orders four and higher are open, and its continuing order-four assignment, are stale. The remaining stated classification problem is order six and higher. This concerns universal functions on full free-jet space; it does not rule out a profile-specific local quantity, a nonlocal quantity, or an Euler proof using more than this universal sign identity.

## 4. Current geometric targets

Write a=1-2c. At the global C2 uniformly sublinear helicity-free scope, A496 leaves rho<=-a at vortical carrier equilibria. A510 shows that rho<-a forces the connected Bernoulli-level component through the equilibrium to be unbounded; the forward regular-level alternatives are escape or a compact critical limit set with unbounded W-saturation. A511 excludes the bounded alternative when omega=0. Under the additional U->0,DU=O(sqrt r),1/3<c<1/2 hypotheses, A509 forces H(p)=Hinf and a zero of the leading Bernoulli-gradient tail. A512 refines singleton components of that zero set. These are necessary conditions, not removal of the lower vortical witness.

The nonzero irrotational equilibrium and flat periodic witnesses remain separate. The smooth arbitrary-helicity target remains separate from this helicity-free C2 route. The C-infinity coverage and one-sign Liouville chain remains conditional on the helicity-sign premise for nonexistence. Unrestricted nonexistence is still OPEN.

## 5. Verification and use

Read the complete current hour-16 packet, the current Section1c statements, and the exact A506/A498 criteria; compare to the completed A493, A509-A512 verdicts. This audit supports refreshing the decision packet, not replacing its primary research objective. Existing configured-model packet and strain-source exchange supplies collaboration. No computation or external client is used. Only the scope corrections here are confirmed; the packet is not a proof of any missing implication.
