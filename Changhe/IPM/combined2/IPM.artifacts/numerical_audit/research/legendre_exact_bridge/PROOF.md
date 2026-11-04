# Exact conversion of a Legendre-modulated potential

Prepared 2026-11-03T01:20:20Z before this topic's implementation. This bridge extends the elementary atom interface without changing a frozen potential.

## Statement and hypotheses

Let s=x^2+y^2, H_n=Im((x+iy)^n), and fix c=4076476460239181/2251799813685248 and mu=4/c-3. Every input atom is

a H_n s^h (1+s)^b (t+s)^(-d) P_k(2s/(t+s)-1),

where a,b,t are exact rationals, t>0, n is a positive odd integer, h,d,k are nonnegative integers and tau=n+2h+2b-2d<=mu. P_k is the usual Legendre polynomial with P_k(1)=1. A hash-bound file specifies all these integers and rational strings, the exact base center, and any claimed elementary expansion and origin metadata.

For each atom replace it by the k+1 elementary atoms with coefficient

a (-1)^(k+j) binom(k,j) binom(k+j,j),

and indices (n,h+j,b,t,d+j), for 0<=j<=k. Combine identical elementary signatures using exact rational addition and remove exact zeros. The resulting finite function is identically the original potential, with identical derivatives of every order. Its inherited tau is unchanged. Thus every established elementary evaluator applies to it after this identity and all relevant metadata are checked. The conversion supplies no numerical norm or background bound by itself.

## Polynomial identity and independent construction

Set z=s/(t+s), so 0<=z<1. The shifted polynomial L_k(z)=P_k(2z-1) has coefficients (-1)^(k+j) binom(k,j) binom(k+j,j). One proof uses Rodrigues' formula L_k(z)=(1/k!) d^k/dz^k [z^k(z-1)^k]: expand the bracket, differentiate each monomial and cancel factorials. Multiplying by z^j adds j to both h and d. Since the sum is finite and t+s>0, this is a global identity between smooth real functions, so all Cartesian derivatives agree.

A separate exact construction uses L_0=1, L_1=2z-1 and (k+1)L_(k+1)=(2k+1)(2z-1)L_k-kL_(k-1). Comparing every coefficient of this recurrence with the binomial formula for every degree present independently checks the finite coefficient generation. It is a check of the finite data used, in addition to the analytic identity above.

## Origin and leading coefficient

At z=0, L_k(0)=(-1)^k and L_k'(0)=(-1)^(k+1) k(k+1). Because z'(s)=1/t at s=0, an atom with n=1,h=0 contributes

a t^(-d) (-1)^k [b-(d+k(k+1))/t]

to the coefficient A of s y in the cubic Taylor polynomial. If n=1,h=1 it contributes a t^(-d)(-1)^k instead. An atom n=3,h=0 contributes a t^(-d)(-1)^k to B, the coefficient of H_3. All other atoms contribute zero to A and B. The canonical elementary sum independently yields A and B by the formulas of ../fitted_center_constraints/PROOF.md. Check exact equality of both constructions and of every producer identity used. Normalization is A+3B=0 and a_star=a_base-8A. A nonzero numerical value obtained by ignoring k has no bearing on the actual potential.

At infinity z tends to1 and L_k(1)=1. The leading degree remains tau with coefficient a. The coefficient at e=mu-2 of the complete source is consequently the formula in ../fitted_center_constraints/PROOF.md with the original atom coefficients a and tau=mu. The sums of expanded coefficients must reproduce this because sum_j L_k,j=1. Lower exterior terms and their finite-radius sizes require the complete elementary evaluator.

## Data and verification contract

Freeze the original producer JSON byte for byte. Parse strict integer fields and rational strings. Reconstruct the entire elementary coefficient map, compare the union of its support with the exported atoms_elementary map, and reject duplicate or zero entries in that exported map. Independently compute the origin identities from the original Legendre atoms and elementary atoms. Check the leading coefficient additions on their full frequency support. The derived JSON uses only the verified elementary map, records the original SHA256 and conversion record path, and has newly computed atom counts. Its new hash is an equivalent-representation hash, not a new optimized candidate. No producer code is executed.

The existing elementary structural checker and a separate Cartesian Python-Fraction reducer then operate on the derived JSON. Their results may be transported to the original exact function only together with the conversion proof and successful identity record. The original file and failed attempts remain unchanged. Class membership, residual norms, conditioning and background are distinct claims. The final large-coefficient elementary representation must not be evaluated in ordinary binary64 merely because the Legendre representation is stable.

## Dependencies and scope

Dependencies are the original exact coefficient JSON, this polynomial identity, ../fitted_center_constraints/PROOF.md and the previously certified base-center structure and origin records. The fixed parameter and authoritative Candidate007 remain unchanged. This method does not infer a least-squares optimum or a whole-plane residual estimate from a training grid.
