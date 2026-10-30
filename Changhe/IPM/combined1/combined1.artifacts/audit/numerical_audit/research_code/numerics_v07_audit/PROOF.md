# What a damped finite optimization diagnostic establishes

## Exact statements and scope

Consider a real finite-dimensional least-squares problem

    m = inf_x ||b-Ax||2,
    x_lambda = argmin_x [||b-Ax||2^2+lambda ||x||2^2],
    lambda>0.

Every computed trial vector supplies m<=||b-Ax||2, an upper bound on
the optimal residual. A positive residual at a damped trial vector does
not supply a positive lower bound on m. Two positive damping values do
not in general bracket the undamped minimizer's norm or residual. This
applies even to exact arithmetic in a full-rank one-dimensional problem;
redundancy and floating-point conditioning are not needed.

A finite list of candidate-specific necessary correction distances does
not by itself imply a uniform distance over every coefficient vector
in a family. A bound proved for every solution correction around one
specified exact reference is a statement about that reference. An
additional uniform certificate or global coefficient argument is needed
to quantify over references as well.

For a probe phi explicitly included in a candidate's optimization
objective, a subsequent exact whole-plane weak test using phi is a
valid necessary test of the frozen candidate. It is not a probe held
out of that optimization. Its proof uses the equation and exact
reference, independent of whether phi influenced candidate selection.

## Complete counterexample for the damped inference

Take A=[1], b=[1]. The undamped objective is(1-x)^2, with minimizer
x_0=1 and m=0. Differentiating(1-x)^2+lambda x^2 gives
2[(1+lambda)x-1], so x_lambda=1/(1+lambda). The positive second
derivative2(1+lambda) proves uniqueness. The damped residual is
lambda/(1+lambda)>0. Thus any two positive damping values give positive
residuals although the undamped minimum is zero. Both computed solution
norms1/(1+lambda) are strictly below||x_0||=1, so they do not bracket
that norm either. Exact rational fixtures at lambda=1/10^6 and1/10^4
record this counterexample. No numerical tolerance or limiting argument
is involved.

The trial-vector inequality follows immediately from the definition of
an infimum. More trial vectors can improve an upper bound but cannot
reverse its direction. For the family statement, inf_{a in family}d(a)
requires a lower bound for every a. Finite sampled values d(a_i) do not
control the unsampled values. This is a missing quantified argument,
not a proof that the actual IPM family's infimum is zero.

## Application to the frozen publication

The frozen numerics_v07 has SHA256
8fb65706ecd07ff52be92b0604483c0b02a19ac8de483bc755c3b967d8661c33.
Its Newton tables are explicitly FLOAT mesh diagnostics. The inference
that these damped steps establish the span's residual floor0.34 or
that the two damping values bracket the answer is unsupported by those
tables. The separate already audited lower bound for every exact L2
Newton correction from007 has its own theorem and is not retracted.
The publication's section4 explicitly says a conditioning stall cannot
be decided from the normal-matrix spectrum. That caution must also
qualify the stronger span-floor wording in sections0,2 and6.

Candidate014 raw SHA256
8dfc33c3dc5f8265e802831a500d757e2da09bc26890c457c0d3603afc3cb746
has meta.pair_k containing[21,522],[23,523],[25,524] among102 rows.
The code checks these exact metadata entries and their uniform weight
1e12. Its n21 weak certificate is a certified design probe. The v07
body correctly says these angular rows were in the objective; its
final request calling them held out for014 should use the same scope.
Candidate013 had a first-mode objective, so its angular probe has a
different provenance.

## The stated bare radial profile is monotone

The frozen N1 note at05:30 explains high-m conditioning by saying the
bare profile r^(2m)(1+r2)^(p-m) is concentrated near r=1. For branch1,
p=(3+gamma-delta)/2=1+gamma>0. For every m>=1 and r>0,

    d/dr log[r^(2m)(1+r2)^(p-m)]
                         =2(m+p r2)/[r(1+r2)]>0.

The identity follows by differentiating2m log r+(p-m)log(1+r2)
and taking a common denominator. Thus the stated bare profile is
strictly increasing, has no interior radial maximum, and grows like
r^(2p) at infinity. Even after dividing out r^(2p), its remaining
factor t^m is strictly increasing. At r=1 that factor is2^-m; at
r=sqrt(m) it is(m/(m+1))^m. This refutes that literal localization
explanation. It does not refute measured conditioning of Legendre
combinations, differentiated fields, mesh weights or cancellations.
Those require the actual physical Gram/design matrices and remain
separate numerical claims.

## Dependencies and evidence

Inputs are the frozen publication and the exact copied014 snapshot.
The code uses rational arithmetic for the scalar counterexample and
checks exact JSON metadata. It does not execute foreign optimization
code or reproduce its large matrix. The actual least-squares optimum,
conditioning in the physical Gram metric, and any uniform IPM family
floor remain OPEN. This proof is checked before the short audit code.
