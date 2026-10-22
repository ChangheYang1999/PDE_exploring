# Independent adjudication of A171 on the next two resonances

Status: criterion and informal algebra written before the new controls. P308 is the independent mathematical proof being audited; A171 is an additional referee argument, not a premise taken on trust.

## Statement, notation and dependencies
Use the exact P308 hypotheses: beta=2, u=y_*-y, Ck nonzero, B=u+ku^2+a u^13 with a=-Ck/260 and H=-k^7/231. Its normalized analytic factors are t=u^10(1+O(u)), Y=u^6(1+O(u)), Z=tY and J'=t/(BY), J(0)=0. The varying existing coefficients are delta_E theta2=t^2, delta_E omega1=-4ZJ and delta_F omega1=Z. The new compatibility residues act on theta3 and omega2. P308 independently proved every entry of their affine matrix, with 256 exact Fraction and 23 separate symbolic controls. This packet reads A171's complete argument, checks its new algebra and notation against those definitions, and distinguishes an audit from an unavailable model invocation.

## Complete argument
Expanding the original polynomial products gives the recurrences in P308. For analytic B=u times a unit and homogeneous exponent m a nonnegative integer, an analytic right side divided by BZ has a convergent Laurent expansion with worst pole m+1. Integrating all powers except u^-1 and multiplying by Z removes every pole. Thus analyticity is equivalent to zero residue, and a nonzero residue produces Z log|u|. For theta3 the logarithm starts at order30; the omega2 residue only uses degrees through26, so the two affine compatibility functions are simultaneously well-defined. This also prevents the new theta3 homogeneous constant from changing omega2's residue. The product formulas contain at most one previously varying coefficient in every product at these two orders, which proves affine dependence.

With P=1+ku, the base units are t0=u^10/P^6 and Y0=u^6/P^4. Corrections to their units are O(u^12); J-J0=O(u^16). The residue formulas have poles of order at most12, so these unit corrections do not alter their residues. The explicit B'' and B''' corrections must remain. Their contributions are (-2*1716/3+156*10)a=416a and (-1716/2+156*16/2)a=390a. The four entries before tuning are 416a+52Ck/25, 0, -6k^8/385-63Hk/25, and 390a+21Ck/20. Substitution gives 12Ck/25, 0, -9k^8/1925, -9Ck/20 and determinant -27C^2k^2/125. The determinant is nonzero under Ck nonzero, which gives a unique pair of existing homogeneous constants. This confirms the matrix independently of the referee's code.

The finite convolution producing -6/385 is -2016/11+3472/5-1008+690-1520/7+24. The earlier obstruction rV1 needs four ADDITIVE terms at B0, modulo zero-residue terms:

    Ck u^-12 P^4(14+6ku)J0
    - Ck u^-8 P^2
    + (CH/3)u^-6(6+4ku)J0
    - (CH/3)u^-2 P^-2.

The first residue is -3Ck^8/770, the second is zero, and the last two sum to -CHk/5. The explicit curvature correction is182aH. Therefore rV1=182aH-CHk/5-3Ck^8/770 and its tuned value is -9Ck(H+k^7/231)/10. The published A171 proof omitted the plus sign before the third term. As rendered, the adjacent factors multiply and the displayed equality is false; inserting '+' restores the actual derivation and its subsequent result. This is a local transcription correction, not a change to P308 or the matrix verdict.

If the D increment is ell T^2 and the gamma homogeneous increment is F_gamma Z, then D=24theta2, gamma=6omega1 and T=Ct give E=C^2 ell/24 and F=F_gamma/6. Multiply the two matrix columns by C^2/24 and1/6. The resulting matrix is (C^3k/50,0; -3C^2k^8/15400,-3Ck/40), determinant -3C^4k^2/2000. This column conversion is the only change of normalization being checked.

A finite analytic polynomial stream with v3 fixed by curl has exact Poisson relation. Thermal coefficients through x^6 and vorticity coefficients through x^5 vanish; parity gives residuals O(x^8) and O(x^7) on a smaller local neighborhood. Nothing in this argument provides convergence of the full transverse series, a whole-plane inverse, attachment to the material center, or a B2 profile.

## Scope and verification
Freeze A171's proof, answer and model failure status and the P308 proof/evidence. Check the displayed rational identities, conversions, exact correction anchor and finite coefficient convolution with own code only. The referee's source is read, never executed/imported. Its Opus status is a credential failure before invocation, so it cannot be counted as an actual Opus review. Our own model consultation must report the actual service model label and availability. No JavaScript/TypeScript, servers/listeners, RLScience cluster, Lean/Lake builds or writes outside this lane are permitted. General B2 remains OPEN.
