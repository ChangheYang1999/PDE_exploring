# Scope and review availability

This accompanies the unchanged proof-first PROOF.md. The coefficient
condition has now passed two independent interval calculations and a
separate exact source/output audit. The exact b_d is
-6077384870622209/39614081257132168796771975168. Both computations give

184130.68809691860443309136512698
 < L_d <
184130.68809691860443309136512700.

This coefficient is in physical r coordinates; its large value is not a
lower bound for the full residual at a finite radius. The expansion has
other rows and a remainder, and all asymptotic conclusions are for each
fixed T as r tends to infinity. No cutoff radius is inferred from L_d.
The a2 row has not been evaluated. The two-case proof needs only that its
frequency-one coefficient either vanishes or does not vanish.

The finite class in PROOF(c) means a finite angular expansion and finitely
many exterior powers with the differentiated asymptotics used in the
canonical Green formula. Lower rows may have finite logarithmic powers;
any resonance at a smaller power contributes additional finite logarithms
at that smaller power. Such terms remain smaller than d. An arbitrary
function described only by a pointwise O bound, without derivative and
canonical inverse control, is not included. This restriction removes any
possible interpretation as a theorem about arbitrary unmodeled tails.

Both numerical methods ran serially and twice, with a third exact
four-frequency projection checking all261 sine coefficients from all260
original column6 entries. The source hashes are checked against the
previous complete input audit. The first hand-written public decimal for
b_d was incorrect; exact comparison rejected it. It was replaced by floor
and ceiling decimal rounding followed by exact rational inequalities.
The mistaken draft audit is archived as text and no verdict uses it.

Two actual Claude Opus 5.5 requests were made. Both returned
stop_reason=refusal, cyber category, and no final response text. The second
request transparently identified the apparent classification error and
submitted the same proof file unchanged. These responses give no
mathematical review and are not acceptance. The limitation is recorded in
evidence/review_availability.json, with the actual models, raw response
hashes and whole request hashes. No other model is silently substituted
and no policy guard is bypassed. The independent proof and computation
are available, but this topic's final collaborative review remains OPEN.
