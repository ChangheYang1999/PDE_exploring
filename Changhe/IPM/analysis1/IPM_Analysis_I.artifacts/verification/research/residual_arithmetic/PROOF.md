# Auditing the residual Taylor models

Date: 2026-10-20. Verdict: REFUTED for the source snapshot identified in evidence/taylor_audit.json. This is a certificate implementation audit, not a theorem excluding any IPM solution.

## Definitions and inputs

The numerics source cert_resid.py represents a scalar function on 0<=tau<=h by a polynomial of degree Q with interval coefficients and a uniform remainder. The tested value Q=12 is the default. A coefficient interval must contain the actual coefficient; summing rounded products does not give that guarantee without a rounding error bound. The source snapshot and exact reproducer are in evidence/ and code/. All counterexamples use finite dyadic inputs, and exact rational arithmetic supplies the reference values except for one final exponential, enclosed by independent Arb arithmetic.

## Product accumulation fails under cancellation

Use the exact polynomial A(tau)=10^16+tau+...+tau^6-10^16 tau^7 and B(tau)=1+tau+...+tau^7. All higher coefficients through degree twelve are zero. The exact degree-seven coefficient of A B is 6. In the source's ascending accumulation it becomes

RN(...RN(RN(10^16+1)+1)...+1-10^16)=0,

because binary64 spacing at 10^16 is 2. The two large product balls contribute a radius about 2.22044605; the six small terms and outward successor calls add only rounding-scale corrections. The final error allowance is proportional to the absolute value of the final sum, which is zero. The reproduced interval therefore excludes 6. The test computes its exact dyadic endpoints and compares them to the integer 6; this does not depend on a rounded reference.

A correct sum bound must use the sum of absolute summands or outward interval additions at each step. The same final-sum form occurs in the degree collection of conv_scatter. In this particular degree-seven product test, discarded degrees thirteen and fourteen create a uniform remainder large enough to mask the missing coefficient at h=.01. The test proves a false coefficient invariant, not a false final function supremum; the proof does not claim otherwise. The product example alone disproves the asserted general enclosure guarantee; it does not establish that a particular profile cell attains this cancellation pattern.

## Exterior Green ODE sign: repaired in the audited snapshot

Write m=2n. For

B_n(t)=exp(m t) integral_{exp(t)}^infinity s^(1-m) f_n(s) ds,

Leibniz differentiation gives B_n'=m B_n-exp(2t)f_n(exp(t)). Put g=exp(2t)f_n(exp(t)). The general ode_tm routine uses a sign parameter, and the frozen source with hash 3c6785... already calls it with gsign=-1 for B. The original test accidentally exercised the default +g equation, then attributed that result to cell(). That assertion is withdrawn. The corrected test uses the actual B call and encloses the solution B(tau)=(1+exp(2tau))/2 for n=1,B(0)=1,g=1.

An earlier live-source read lacked this sign parameter, but it changed before the recorded snapshot. The archived initial JSON preserves the erroneous finding; the current result and verdict explicitly correct it. The model follow-up identified this provenance mistake. No residual certificate is inferred from the corrected toy test.

## Wrong difference-frequency sign for tangential transport

The two trigonometric products obey

2 cos(m theta) sin(j theta)=sin((j+m)theta)+sin((j-m)theta),
2 sin(m theta) cos(j theta)=sin((j+m)theta)-sin((j-m)theta).

Thus the sign of the difference frequency must be reversed between radial and tangential transport. The source uses the same conv_scatter sign array S2 for both products. For m=2, j=1 and unit amplitudes the tangential term must be sin(3theta)+sin(theta), but the returned coefficients represent sin(3theta)-sin(theta). The reproduced constant coefficient ball for sin(theta) excludes +1. The common prefactors in the residual do not change this relative-sign requirement.

## Bernstein conversion uses an inexact matrix as exact data

For Q=12, the Bernstein matrix entry B[4,1]=binom(4,1)/binom(12,1)=1/3. It is stored as its nearest binary64 value with radius zero. That dyadic is not 1/3. This refutes the constructor's exactness claim. A later operation might accidentally have enough slack to cover some such errors, but no proof of that compensation is present. The transform must use enclosing matrix coefficients or supply an explicit transformation error. This item is a proven provenance error; by itself it is not a constructed false final supremum.

## Scope and dependencies

The reproduction imports only the local source snapshots and uses single-threaded NumPy and Arb. No profile residual values are upgraded from samples. The analytical identities above are independently derived, and the exact dyadic counterexamples are independent of the numerics lane's least-squares fit. These defects concern the proposed numerical certificate only. The inverse theorem and a closing inequality remain separate open obligations.

## Refreshed signs and outer exponent transfer

The newer source snapshot in evidence/refreshed_1448 repairs tangential transport by calling conv_scatter(...,flip2=True). The exact n=1,j=0 trigonometric test now contains the required positive sin(theta) coefficient. Its B ODE call also retains the already repaired negative forcing. These two sign defects are not asserted against this snapshot. The product-coefficient cancellation counterexample remains reproducible.

The new outer exporter exp_terms writes alpha_mid=float(alpha.mid()) and alpha_rad=float(alpha.rad()), without the midpoint-conversion allowance used for its polynomial coefficients. For the actual exact k in modal_v2.json, alpha_0=k-3 is an exact dyadic that is not representable by its rounded binary64 midpoint. At 256 bits its Arb representation is exact with radius zero, so the exported pair has radius zero and excludes alpha_0. The code/audit_current_export.py test extracts and executes the actual nested exporter by Python AST, then compares its output to the exact Fraction k-3. The later cert_resid_regions.py reader never reads alphas_rad and passes the rounded exponent as an exact float. Thus even fixing the exporter alone would not propagate uncertainty through that reader.

This is a concrete false enclosure of a specified mathematical input. It does not quantify the error in a completed final residual bound, since other margins might happen to cover a particular numerical discrepancy. Valid certification requires an explicit uniform error argument, or interval exponents propagated through exponential coefficients, derivative factors, and remainders. The infinite exterior asymptotic statement must retain the exact leading exponent k-3 so that c_l k=1 holds exactly.
