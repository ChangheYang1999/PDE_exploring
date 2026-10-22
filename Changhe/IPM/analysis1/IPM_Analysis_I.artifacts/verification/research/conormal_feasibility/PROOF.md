# Exact feasibility margins at the revised conormal parameters

2026-10-20. This is a scalar feasibility theorem, written before calculation. It supplies no global operator, geometry or embedding theorem.

Let k=1615536043799051/9007199254740992 be the exact normalized modal exponent. Put c_l=1/k, A=2/k-1, D=2A+1, b0=(A+3)/2 and beta3=(6A+1)/D. Choose

alpha=1/20, s=153/50, b=307/100, a=129/20,
gamma=129/1000, gamma_prime=1129/1000.

The exact inequalities to be checked are

0<alpha<1, 3+alpha<s<b<beta3+1/2,
11/2<a<13/2, delta=bD-aA-b0<0,
a-1/2>[D(s-1/2)-1]/A,
0<gamma<k, gamma_prime=1+gamma<2.

They are rational assertions and can be decided without floating-point rounding. For this k one also has10.1507252<A<10.1507253. For frozen mu=1 and any29.7494906<=g<=29.7494908, the source inequalities s<(g+b0)/A and s<b0 hold, by taking the smallest g. This does not identify the source parameters of an exact profile.

For any a,b with a<13/2, b>3+alpha and delta<0, elementary subtraction gives

0<|delta|=aA+b0-bD < (13/2)A+b0-(3+alpha)D
 =A-3/2-D alpha.

Hence the right side must be positive, equivalent to alpha<(A-3/2)/D. The identity

(A-3/2)/D=beta3+1/2-3

shows that this necessary bound agrees with the stated open feasibility window. The accepted local saddle theorem in ../conormal_saddle/PROOF.md gives base-space inverse norm1/|delta|, so in this scalar window

||T^(-1)|| > 1/(A-3/2-D alpha).

At the selected parameters, |delta|=(81A-157)/100. The graph norm ||h||+||Th|| instead gives inverse norm1+1/|delta|. The lower bound diverges as alpha approaches the endpoint from below; it is not a lower bound for the full variable IPM inverse without an additional localization theorem.

For the selected corner inequality, its lower threshold for a can equivalently be written

1/2+[D(s-1/2)-1]/A=2s-1/2+(s-3/2)/A.

Both forms will be compared exactly. The lower threshold from delta<0 is separately

(bD-b0)/A=2b-1/2+(b-3/2)/A.

The threshold difference is (b-s)(2+1/A)>0. Thus, under b>s, delta<0 implies the corner inequality; the latter is redundant in this window. We test both as an arithmetic consistency check. The C^(4,nu) trace correspondence in the saddle dependency uses a=9/2+nu and b=5/2+alpha; it does not apply at this selected point b=3.07, which differs from2.55. Trace regularity and the global embedding remain OPEN.

Scope of the lead's section3 conditions: T1 is checked only for the displayed frozen source family; T2 and the scalar margins in T6 are checked as rational inequalities. T4 is checked for the explicitly chosen gamma. T3 requires the actual characteristic geometry and integrable positive-rate traversals. T5 requires a specified variable order along the lifted flow. Neither follows from choosing four scalar parameters; both remain OPEN, as do all global trace/extension and inverse estimates.
