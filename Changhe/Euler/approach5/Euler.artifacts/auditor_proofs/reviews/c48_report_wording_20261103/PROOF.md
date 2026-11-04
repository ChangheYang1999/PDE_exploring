# Scope of the C48 report statements

Status: targeted wording audit. A902-A909 retain their existing verdicts.

## 1. Exact sufficient premise

Use the setting and notation of A904, fully stated in the team records Sections 3-4: U is a decaying C2 profile, 0<c<1, omega arbitrary, W=curl U has a C^alpha seminorm bounded by C(1+|y|)^N on B(y,3), and D_rho is the measurable admissible misalignment integral. With a fixed exterior base sphere, write F(z) for the D_rho average on the backward carrier segment from the far vortical point z to that sphere. If there are epsilon>0 and Rstar such that

    F(z)<=1+c/2-epsilon for every |z|>=Rstar with W(z)!=0,

then DU tends uniformly to zero. Natural rates are additionally confirmed for c>1/3. Both polynomial Holder growth and the uniform positive margin are extra hypotheses. Neither is derived from bare velocity decay in A904.

## 2. The two different converse statements

A905 says that prescribed far points z_n with |W(z_n)|>=delta|z_n|^(1/2), delta>0, have F(z_n)>=1+c/2-o(1). It does not require the polynomial Holder premise, and it concerns those specified vortex-growth points.

A separate converse follows by contraposition of A904. Retain polynomial Holder growth and all the other setting assumptions. If DU does not tend to zero, then for every epsilon>0 and every Rstar the uniform displayed bound fails. Taking epsilon=1/n and Rstar=n yields far vortical points z_n with

    F(z_n)>1+c/2-1/n.

In particular failure of DU=O(sqrt(|y|)) implies this conclusion under the same Holder premise. This is an existential sequence from A904's contraposition, not A905 applied to prescribed large-gradient points. No statement equating large strain and large local vorticity was used. Thus the draft implication can be retained with the Holder premise explicit and its citation changed to A904; the square-root-vorticity formulation is the exact A905 alternative.

## 3. The local direction at a vorticity zero

A902 already states in its standalone proof Sections 1-2: choose any unit xi with W(z) cross xi=0. This includes W(z)=0. Its ledger confirms all bounds in those sections. No new extension is needed. For clarity, the proof uses only W(z) cross xi=0: since W is C1, |W(z+x) cross xi|=O(|x|), giving absolute convergence of the local integral. Contraction of the signed cutoff kernel bounds it by D_rho, and the annular remainders total 5 log 2 times m_ann/rho. No division by |W(z)| occurs in that local proof. The later along-orbit application separately restricts to W!=0 to define its moving direction.

## 4. Concrete report corrections

The draft in the team records sentence citing A905 for failure of the gradient bound should use either A905's exact square-root-vorticity formulation or the Holder-qualified existential contraposition in Section 2. It is not necessary to call the implication false when its preceding Holder premise is retained.

The stand-alone summaries in the team records and the final C48 paragraph must retain polynomial Holder growth as an additional premise. A precise replacement is: Under polynomial Holder growth of curl U, a uniform positive-margin bound on the backward-segment misalignment average suffices for the derivative premise. Neither extra condition is proved from decay.

The in the team records table and this report table must specify at most 1+c/2-epsilon, for one epsilon>0 uniformly on every sufficiently far vortical segment. The valid derivative-decay range is 0<c<1; natural rates are confirmed for 1/3<c<1. The existing local statement using any aligned unit xi is already within A902 and needs no narrowing.

Only these identified excerpts were audited here. No complete current report or restructured report is certified by this targeted review. The relevant current excerpts, source hashes and actual check time are retained in verification.
