# Independent check of refined weighted weak probes

## Exact statement and inputs

For each exact reference, exponent a and integer k in data/claims.json, every fixed-c distributional stationary correction h in the canonical S1 weighted space H_a has

    ||(1+r^2)^(-a/2)h||_2 > strict_lower.

The references are exact canonical potential data under data/. Their conversion from published generators was already independently checked. The source claims come from the frozen T2 review in source/. They concern four references and the exponents 1 and6/5. All displayed bounds are necessary correction distances, with no assertion of optimality or existence.

## Complete argument

Use the audited theorem T4-081, whose statement and cutoff proof are in ../weighted_weak_probe/PROOF.md and whose independent theory review is frozen alongside it. For w=(1+r^2)^(-a/2), phi_k=y[r^2/(1+r^2)]^k/(1+r^2)^2, write

    I=|integral F phi_k|,
    D=||(2c+1)phi_k+cX.Dphi_k||_(L2(w^-2))
        +|||u||Dphi_k|||_(L2(w^-2))
        +C_U||phi_k Drho||_(L2(w^-2)),
    H=||Dphi_k/w^2||_infinity.

Testing the stationary equation against phi_k gives I<=Dm+C_U Hm^2, where m=||wh||_2. The compact cutoff argument is valid for0<a<2 and the smooth sublinear reference fields. Thus

    m >= 2I/[D+sqrt(D^2+4C_U H I)].

For a=1 take C_U=2 from the audited odd-mode velocity bound. For a=6/5 take C_U=808233/500000 from the independently checked rational S1 Schur certificate. Replace the background and gradient norms by the explicit conservative upper bounds(6),(7) of T4-081. This can only decrease the resulting necessary distance.

Independently form rho and the stream function from the canonical potential. Integrate the weak equation directly by polar orthogonality, including every nonlinear pair of adjacent angular frequencies. Assemble all background quadratic forms exactly. Every radial integral is a finite beta sum with positive beta parameters; evaluate it by outward log-gamma arithmetic. This differs from T2's expansion in t and its finite rational beta recurrence. Positivity of all squared norms and the pairing is checked. Finally the lower endpoint of the resulting root must strictly exceed the exact decimal rational in data/claims.json.

All inputs, code and result hashes are retained. No conclusion uses a float comparison or claims that k is the maximizing integer. The already confirmed unrefined numbers for005 are included as checks of the new execution, not as a new theorem.
