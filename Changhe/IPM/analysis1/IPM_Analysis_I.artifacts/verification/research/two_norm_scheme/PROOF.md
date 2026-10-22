# A conditional quasilinear fixed-point theorem with graph domains

Date: 2026-10-20. Status: abstract conditional theorem. None of the IPM inverse hypotheses below has been proved globally. This statement isolates what a proposed iteration must actually establish; it is not a YES endpoint.

## Spaces and operators

Let X and E be Banach spaces of real corrections, with a continuous injective embedding X into E. The X norm is the high norm and the E norm is the norm used for contraction. For r>0 let B_r={h in X:||h||_X<=r}. Assume B_r is closed as a subset of E. This is a real hypothesis; boundedness in X alone is not a compactness or closure proof. The homogeneous parity and normalization constraints are included in the definition of X and E.

Let Y_H and Y_L be Banach spaces of forcing, continuously embedded in a common vector space Z of distributions, with Y_H embedded continuously into Y_L. Let epsilon belong to Y_H and ||epsilon||_{Y_H}<=eta. Let Gamma:X->V be the full linear velocity increment, with

||Gamma h||_V <= C_V ||h||_X.

For every h in B_r, define a linear operator A_h on a linear low domain D_h subset E, interpreted as taking values in Z. Require the following properties.

1. X is contained in D_h. For every u in X, A_h u belongs to Y_L.
2. The low a priori estimate holds for every u in D_h with A_h u in Y_L:

   ||u||_E <= K_L ||A_h u||_{Y_L}.

   In particular the kernel is trivial on that domain. Mere existence of one low right inverse would not imply this estimate for arbitrary differences.
3. For every f in Y_H there is a solution R_h f in X of A_h R_h f=f, and

   ||R_h f||_X <= K_H ||f||_{Y_H}.

   By property 2 this solution is unique within the low domain. No assertion that A_h maps all of X into Y_H is made. The natural high domain is {u in X:A_h u in Y_H}, endowed with a graph norm when needed.
4. There is a bilinear expression B:E x X->Y_L with

   (A_h-A_g)u=B(h-g,u),
   ||B(e,u)||_{Y_L} <= C_B ||e||_E ||u||_X,

   for h,g in B_r and u in X. The identities hold in Z, so they also give identities in Y_L whenever their terms belong there.

If the preceding operator hypotheses are known only for velocity increments bounded by r_V, require C_V r<=r_V. Otherwise r_V and this condition can be omitted. All constants must be uniform over the stated ball.

## Closing inequalities and conclusion

Suppose

K_H eta <= r,
q:=K_L C_B K_H eta <1,
C_V r<=r_V when the velocity restriction is used.

Then there is a unique h in B_r solving A_h h=-epsilon. It obeys

||h||_X <= K_H eta.

Starting from any h_0 in B_r, the iteration h_{n+1}=R_{h_n}(-epsilon) converges to h in E, with

||h-h_n||_E <= q^n ||h_1-h_0||_E/(1-q).

The stronger but simpler condition K_L C_B r<1 can replace q<1. The factor two sometimes put in the radius is optional slack, not a cure for a failed inverse or an omitted velocity term.

## Proof

Define T(h)=R_h(-epsilon). Property 3 gives ||T(h)||_X<=K_H eta<=r, so T maps B_r into itself. For h,g in B_r, both T(h) and T(g) belong to X and hence to D_h. Since D_h is linear, their difference also belongs to it. In distributions,

A_h(T(h)-T(g))
=-epsilon-A_h T(g)
=A_g T(g)-A_h T(g)
=-B(h-g,T(g)).

The right side belongs to Y_L by property 4. Applying property 2 and then property 3 gives

||T(h)-T(g)||_E
<=K_L C_B ||h-g||_E ||T(g)||_X
<=q ||h-g||_E.

Because E is complete and B_r is E-closed, B_r with the E metric is complete. The contraction argument now gives a unique fixed point h in B_r and the displayed geometric error bound. Applying the X estimate to T(h)=h proves the high bound. At the fixed point the defining right-inverse identity gives A_h h=-epsilon exactly. No weak-star passage through a nonlinear expression is required. Conversely any solution h in B_r must equal T(h), since its difference from T(h) lies in D_h and has zero A_h image; the low estimate implies equality. This proves uniqueness in the specified ball.

## Specialization to the canonical IPM equation

For an exactly normalized background rho_bar, let sigma[u]=psi[u]_{xy}(0), c[u]=sigma[u]/3 and

Gamma u=U[u]+c[u] X.

The background scalar is cbar_l=(1+sigma[rho_bar])/3. Let G=X dot grad(rho_bar), Vbar=cbar_l X+U[rho_bar], and

L u=Vbar dot grad(u)-u+U[u] dot grad(rho_bar)+c[u] G,
A_h u=L u+(Gamma h) dot grad(u),
B(e,u)=(U[e]+c[e] X) dot grad(u).

Linearity of the canonical inverse and of c gives the operator-difference identity exactly. The equation A_h h=-epsilon is exactly F(rho_bar+h)=0 with the scalar set by the canonical normalization, provided epsilon=F(rho_bar) and all expressions lie in the asserted distribution spaces. The term c[e]X dot grad(u) belongs in both the velocity norm bound and C_B; a bound for U[e] alone does not cover it. In particular, C_B needs a low-norm estimate ||U[e]+(sigma[e]/3)X||_{V_L}<=C_L||e||_E in a velocity space whose product with grad(u) lies in Y_L. The high bound C_V alone gives no such estimate. The scalar functional sigma must also be bounded in E. These bounds may instead be restricted to differences e=h-g in X, but their right side must still use the E norm.

High and low forcing norms must have a consistent far-field definition. In particular, the arbitrary logarithmic angular tails allowed by SPEC v1 do not map into its decaying forcing space plus one scalar direction, as proved in ../spec_audit/PROOF.md. The abstract theorem does not repair that mismatch. A derivative-preserving inverse on a suitable graph domain also differs from SPEC v1's impossible isotropic gain from C^{3,alpha} to C^{4,alpha}.

## Remaining obligations

To apply this theorem, exhibit the actual X,E,Y_H,Y_L and domains; prove closure of B_r in E; prove the uniform high solvability and low a priori estimate; prove the full velocity and bilinear bounds; certify epsilon in Y_H; and verify the closing inequalities. Parity, continuous center factorization, normalization, canonical growth and P_2 regularity must be consequences of these spaces. A small sampled residual, a finite matrix inverse, or local source transport alone proves none of the missing global inverse hypotheses.
