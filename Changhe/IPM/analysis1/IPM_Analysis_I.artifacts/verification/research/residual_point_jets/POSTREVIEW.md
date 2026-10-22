# Correction to the completion review's Green calculation

The completion review accepted the result but gave two incorrect intermediate explanations. Neither is used by PROOF.md or the programs. With m=2n, w_{n-1}=m-1 and w_n=m+1, the identities are simply

    3-w_{n-1}=4-m,   3+w_n=4+m.

There is no extra exponential factor to absorb in these two identities. In particular, the review's sentence claiming (D+3)(exp(4t)f)=exp(4t)(D+4)f is false: the correct right side is exp(4t)(D+7)f. Its displayed chain involving 4-m+(m+4)-m does not derive 3-w_{n-1}. I reject those intermediate equalities.

For a direct correct calculation, put S=(H_{n-1}+H_n)/2. From the I and J equations,

    A'/exp(4t)=4S+S'+m^2 I-m H_{n-1},
    B'/exp(4t)=m^2 J-4S-S'-m H_n.

Define g/exp(4t)=S'+4S+(m/2)(H_n-H_{n-1}). Substituting A/exp(4t)=S-mI and B/exp(4t)=mJ-S immediately gives A'=-mA+g and B'=mB-g. This is exactly the formula implemented in compute_arb.py. Ordinary Leibniz differentiation of exp(4t)g_0 then gives the powers4^{a-b} used for higher derivatives. No (D+3) operator acts on that exponential factor in this step.

The review's three optional finalizer comments are handled explicitly. A separate finalize_v2.py preserves the already reviewed source unchanged, requires the listed substantive bundle members, accepts exactly one scoped VERDICT line in the final exchanges, and requires this correction and FINAL_ADJUDICATION.md in the final follow-up bundle. The original finalizer is retained as review history and will not publish the verdict. The final adjudication below retains the point-only, inherited-input scope.
