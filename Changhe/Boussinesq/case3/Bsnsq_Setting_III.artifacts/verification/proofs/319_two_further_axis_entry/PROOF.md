# Complete report entry for the next two axis relations

Prepared 2026-10-22T08:42:31.255324+00:00 before entry controls. This is a full-statement, proof and integration audit of lead proposed item4.55, not a new global theorem.

## Statement, hypotheses and normalization
Fix beta=2, u=y_*-y, Ck!=0, B=u+ku^2-(Ck/260)u^13 and H=-k^7/231. Let t=u^10(1+O(u)), Y=u^6(1+O(u)) solve the normalized analytic homogeneous equations, T=Ct, Z=tY, and G'=t/(BY), G(0)=0. Then eta=Y(H-CG). P303/P306 give analytic solutions D,gamma of the first five axis relations; D can vary by ell T^2 and gamma by a multiple of Z once D is fixed. The lead notation a1=T/2,a2=D/24,q0=eta,q1=gamma/6,v2=-(B''+eta)/2,v4=-(q1+v2''/3)/4 agrees with the factorial-free P308 recurrence, with all odd y derivatives changing sign under u=y_*-y.

The next scalar homogeneous factors are t^3 of order30 and t^2Y of order26. For Bf'-A(u)f=R with normalized homogeneous factor z=u^m times an analytic unit, division gives (f/z)'=R/(Bz). Analytic R gives a meromorphic integrand of pole order at mostm+1. Its residue vanishes exactly when an analytic f exists. A nonzero residue produces r z log|u|, whose mth derivative is unbounded on either side. If the residue vanishes, any smooth two-sided solution differs from an analytic particular solution by a multiple of z: the two one-sided constants must agree because the mth derivatives agree. Thus all smooth solutions are analytic. This proves the asserted C30/C26 failure alternatives once the compatibility matrix is checked.

Choose zero-constant Laurent primitives for one pair D_*,gamma_* and normalize D=D_*+24E t^2, q1=gamma_*/6-4E ZG+F1 Z. These are precisely the two-parameter family, by variation of constants. E=C^2 ell/24 plus the constant arising from the earlier reference particular solution; no absolute ell origin is assumed. A free a3 homogeneous addition changes the next integrand by a multiple of t/(BY)=O(u^3), so it has no residue. If the thermal residue is nonzero, omit the logarithmic primitive to define the next finite coefficient: the omitted term starts at u^30, above the coefficients through u^26 used by that next residue. This definition agrees with the actual residue after compatibility.

P308 proves the arbitrary-parameter residue variation matrix in E,F1:

    [ 416a+(52/25)Ck,                  0 ]
    [ -(6/385)k^8-(63/25)Hk, 390a+(21/20)Ck ].

The tuned matrix has entries12Ck/25,0,-9k^8/1925,-9Ck/20 and determinant-27C^2k^2/125. Consequently exactly one E and then one F1 removes the two obstructions. This fixes one pair D,gamma as germs. The new a3 and q2 retain their own homogeneous constants. The proof of these coefficient identities is the complete finite Laurent calculation in P308; P320 independently adjudicates A171's same formulas and the single missing plus in its intermediate display. Those dependencies are frozen here, not assumed from a summary.

## Scope of residue estimates and integration
The pole bound12 pertains to the variation integrands used for the matrix, not the entire fixed thermal integrand, which may have a pole of order31. All relative unit corrections from a u^13 start at degree12, with G-G0=O(u^16), and cannot affect these variation residues except through the explicit B'' and B''' terms. The fixed residues themselves can depend on further Laurent coefficients. The exact primitive and normalization statements must retain that distinction.

This finite result imposes no new condition on B,T,eta after their stated tuning, but is a statement only about this family and through the specified two relations. The sign condition Ak<0 is inherited only when the profile sign conditions H/A>0,C/A>0 are additionally imposed. A,C,H as used in the general local statement do not automatically have H/A>0. The outcome does not construct a profile, a full-plane inverse, a moving-center extension, or a solution of the two PDEs on an open set. New P321 studies all formal orders separately and is not a premise of this entry; language about what is undecided must be explicitly scoped to this finite result.

The complete preview must add only the eight item paragraphs, four declared cross-reference replacements, one result-table row and one dated timeline entry. All previous table rows and timeline entries must remain unchanged. Derivative/sign relations, indicial exponents, matrix conversions and all literal protected formulas will be checked independently. No teammate code is executed or imported. No JavaScript/TypeScript, servers/listeners, RLScience cluster or Lean/Lake builds; write only in the verifier lane. General B2 remains OPEN.
