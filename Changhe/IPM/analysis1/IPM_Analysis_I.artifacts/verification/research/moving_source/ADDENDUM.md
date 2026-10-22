# Scope and response to the first actual Opus 5.5 review

The completed review at 2026-10-21T02:30:16Z accepted S0-S4 and their
constants, but described a substantive S5 cutoff-scale gap. That objection
misreads the stated hypothesis: our proof already restricts the moved
estimate to 0<delta'<=delta_h=(R0-d_h)/3. The displayed numbers evaluated
at delta0=33/2000 are conservative upper bounds because delta'<=delta_h
<=delta0. No claim permits delta'=delta0 when d_h>0. The positivity
threshold computed at delta0 is sufficient at every smaller admissible
scale, and is not claimed sharp there. The same interpretation applies
to the lead's S5. This clarification is mandatory.

The moved local estimate uses new cutoffs centred at P_h and scaled by
delta', with the tail and annulus norms in that translated estimate.
Its existence follows by translating and rescaling the explicit radial
cutoffs in77. The raw strain functional is still evaluated at the fixed
origin. The proof77 applies with p replaced by p_h>8.55. Only the local
forcing coefficient K1 and its source hypotheses are bounded uniformly
here. No comparison with the old centred norms and no uniform values of
K2,K3,K4 are claimed. S4 is a separate estimate using the old cutoffs to
bound the perturbation and its source displacement.

The hypotheses of the Sobolev-and-tail section explicitly include
h(0)=grad h(0)=0, zeta h in H^r, finiteness of N, and existence of the
stated canonical operator. The agreement of the compact-part canonical
operator and the Fourier multiplier follows from the same full-plane
canonical inverse as77: both solve -Delta psi=partial_x(zeta h), and
its canonical normalization rules out their harmonic difference. For a compact source v, partial_x v has total integral zero. The
canonical stream is O(1/r) and its velocity is O(1/r^2) outside a large
bounded set. The distributional Fourier computation gives the stated
velocity multiplier. A polynomial velocity ambiguity is excluded by
this decay; the remaining additive stream constant has zero velocity. These facts are not
additional numerical estimates. The sentence 'the last equality uses
zeta=1' means the final inequality for e3.

The review's shortened decimals 0.9175805,1.6056305 and0.2295305 round
inward when used as E upper bounds. The exact values retained in checks
and the lead's lemma are .91758051,1.60563051,.22953051. Our local K1
ceilings .40709660,.56549268,.3181 are verified by both directed engines.
The review's informal decimal K1 values are not used. Its final 'trial
only' phrase must be read as an obstruction centred on this trial: the
proved statement excludes every exact perturbed profile satisfying all
listed inequalities, not merely h=0. The excluded neighbourhood is still
too narrow for a decisive endpoint.

The first fresh output audit mistakenly put 800/(pi delta) in k1,
twice its correct value 400/(pi delta). Its failed log and code are
retained. Version2 corrects only that audit expression; the primary
checker, proof, and proposed constant were already correct.
