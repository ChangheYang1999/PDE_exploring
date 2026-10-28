# Compact coupling commutators and the cofactor principal symbol

## Statement

Use the actual modal background rho, canonical U, renormalized coupling C_ren, remainder coupling C_R, and space X_s of proof 123, with the actual order of proof 130. Thus sigma=25/4, s_0=41/20, delta=9/5 and gamma=-1/2. Let Xhat_s denote the same two-component norm with the zero vertical trace omitted, as in proof 138.

Let phi be a real or complex smooth bounded function on the cylinder, invariant under the two coordinate reflections, with all derivatives bounded. Multiplication M_phi is bounded on both spaces. Then

 [C_R,M_phi]:X_s -> X_s

is compact. In particular, if Lambda is the smooth bounded escape function of proof 128, then for every fixed real N,

 M_(exp(N Lambda)) C_R M_(exp(-N Lambda))-C_R

is compact on X_s. There is no bound uniform in N asserted here.

On every compact annular coordinate patch, the order-zero principal symbol of C_ren, in both the bulk variable h/b and the vertical cofactor variable h/(b p), is the physical symbol

 c_0(X,xi)=grad rho(X).u(xi),
 u(xi)=(xi_x xi_y/|xi|^2,-xi_x^2/|xi|^2), xi!=0.       (1)

For cylinder or other local coordinates, xi in (1) is the covector transported to Cartesian coordinates by the coordinate map. The equality of these two principal symbols does not say that their transport zeroth-order terms agree. It also does not assert that the cofactor principal term separately has zero axis trace.

All statements are qualitative. No H3 estimate or numerical commutator bound is claimed.

## Localization and the two different target spaces

Proof 138 proves that both output tails of C_ren are small as maps X_s to Xhat_s. Since M_phi is bounded on both spaces, the same is true of

 D=[C_ren,M_phi].                                      (2)

Indeed, for an escaping radial cutoff chi_R, multiplication commutes with phi, and

 chi_R D=chi_R C_ren M_phi-M_phi chi_R C_ren.

Thus ||chi_R D||_(X_s to Xhat_s) tends to zero. It suffices to prove compactness after a fixed compact radial output cutoff.

The normalization term c[h] chi_0 X.grad rho/3 can be treated as finite rank on a compact annulus. It must not be split off as a globally bounded map into Xhat_s: its leading origin term separately fails the remainder weight, and only its cancellation with the velocity term repairs this. The tail argument above uses the complete C_ren and respects this cancellation.

On a fixed output annulus, restrict the input first to finitely many neighboring annuli. The discarded radial inputs give operators whose norms tend to zero as the retained interval grows, by the six matrices of proof 123, with the output index in a fixed finite set. On these separated inputs the kernels are smooth, including at the output axis after parity and division, so every fixed output derivative has the same convergent geometric majorant. The same argument applies after either insertion of M_phi. Consequently it remains to consider bounded input and output annuli, covered by finitely many coordinate patches.

## The bulk variable

Away from the vertical axis, multiplication by the nonzero smooth factor b and changes of coordinates do not change an order-zero principal symbol. The localized operator has leading part

 rho_x U_1+rho_y U_2.

The difference caused by moving the smooth factor b through U, and the smooth cutoff errors, have order minus one. The normalization term on this annulus is finite rank. Thus (1) is the bulk principal symbol.

For the commutator, phi commutes with rho_x and rho_y, so its local leading pieces are rho_j[U_j,phi]. The commutators [U_j,phi] have order minus one. Their symbols and kernels follow directly by writing phi(Y)-phi(X) in the singular integral kernel and Taylor expanding once; the first factor X-Y removes one degree of its singularity. Higher Taylor terms give the usual lower orders. The low-frequency cutoffs contribute smooth kernels. Only finitely many local coefficient norms are needed below.

## The cofactor variable

Consider a Cartesian vertical-axis patch with y bounded above and below by positive constants. The negative y patch follows by parity. Write h=x^2 w and rho=x^2 f. Smooth nonvanishing factors convert w to the prescribed normalized cofactor, so it suffices to work with w. For the localized canonical multipliers the exact algebraic identity is

 U_1[x^2 w]/x
 =x U_1[w]+2[U_1,x]w+x^(-1)[[U_1,x],x]w,              (3)

and similarly

 U_2[x^2 w]
 =x^2 U_2[w]+2x[U_2,x]w+[[U_2,x],x]w.                 (4)

The localization cutoffs may be chosen reflection-even and equal to one on a larger patch. The missing terms then have smooth kernels and preserve the stated parities. A smooth even low-frequency regularization of the multipliers also only changes smooth-kernel terms.

Since

 (U[h].grad rho)/x^2=(2f+x f_x) U_1[h]/x+f_y U_2[h],   (5)

substituting (3)-(4) gives

 (U[h].grad rho)/x^2=rho_x U_1[w]+rho_y U_2[w]+R w,     (6)

where

 R=(2f+x f_x)(2[U_1,x]+x^(-1)[[U_1,x],x])
                         +f_y(2x[U_2,x]+[[U_2,x],x]). (7)

The single commutators have order minus one and the double commutators order minus two. The double U_1 commutator applied to an even w is odd in x. Division of this odd output by x costs at most one Sobolev derivative: the identity

 g(x,y)/x=integral_0^1 partial_x g(a x,y) da

and its differentiated versions, followed by interpolation, prove the local H^(q+1)-to-H^q bound. The integral in L2 has factor a^(-1/2), which is integrable. Thus every operator inside parentheses in (7) gains at least one derivative locally. This is a parity-restricted statement; an arbitrary division of a nonvanishing output by x would be invalid.

The actual coefficients f, f_x, f_y and the displayed products have local H^(51/8) regularity, as established in proof 123. In particular R maps local H^sigma inputs boundedly into H^(sigma+eta) for any fixed 0<eta<1/8, for example eta=1/16. Products are justified because H^(sigma+eta) is an algebra on a two-dimensional patch, the coefficient belongs to that space, and the gain-one operator puts the input in H^(sigma+1). All smooth coordinate factors preserve this statement. It follows that R is locally compact into H^sigma and that (1) is also the cofactor principal symbol.

To form the commutator with phi in (6), the leading part gives rho_j[U_j,phi], of order minus one. The two terms R M_phi and M_phi R are each locally compact into H^sigma by the same estimate. The locally finite-rank normalization terms remain compact. A sector input cutoff supported where s=sigma makes these estimates applicable to general X_s input. Input outside a slightly larger sector is separated from the axis output and gives a smooth kernel, already covered above.

## Local compactness in the variable-order component

For clarity, the gain just used in the bulk does not require the coefficients to be smooth of all orders. Let A be a smooth order-minus-one operator localized to a compact patch, and let q belong locally to H^(sigma+1/8). Then q A maps H^{s(.)} into H^{s(.)+eta}, for 0<eta<1/8. A maps into H^{s(.)+1}. The low-coefficient/high-input part of the product is bounded by the coefficient L-infinity norm. For the high-coefficient/low-input part use the L-infinity bound from the input order s_0+1>1, the upper target order sigma+eta<sigma+1/8, and the square sum of the coefficient in H^(sigma+1/8). The comparable-frequency part has the same bound with a convergent geometric factor. Spatial derivatives of 2^{j s(X)} produce powers of j, absorbed by the strict gap 1/8-eta. This is the product argument of proof 123 with the target order increased by eta.

On a compact patch, H^{s(.)+eta} embeds compactly in H^{s(.)}: remove frequencies above J, whose operator norm is bounded by C2^(-J eta/2), allowing the smooth order weights; the remaining frequency-localized compactly supported operator has a smooth square-integrable kernel and is compact. The analogous fixed-order statement applies to the cofactor. Since the Xhat_s norm is the sum of the two component norms, local compactness in both components gives compactness into their closed graph intersection. Indeed, from any bounded input sequence choose successive subsequences convergent in both components; their limits agree as distributions with the same physical function, since both components continuously embed in local distributions and obey the cofactor identity.

Consequently each bounded-annulus version of D in (2) is compact into Xhat_s. The radial input and output approximations above converge in operator norm, proving global compactness of D:X_s->Xhat_s.

## Axis subtraction and the final range

By proof 140, E Gamma_C:X_s->Xhat_s is compact. Both

 E Gamma_C M_phi and M_phi E Gamma_C

are therefore compact into Xhat_s. Subtracting their commutator from (2) proves compactness of [C_R,M_phi] into Xhat_s. But C_R and M_phi each preserve X_s, so the image has the exact zero cofactor trace. That trace condition is closed in Xhat_s. A sequence converging there with every member in X_s converges in X_s with the same norm. This proves the claimed compact map into X_s.

Finally,

 M_(exp(N Lambda)) C_R M_(exp(-N Lambda))-C_R
 =M_(exp(N Lambda))[C_R,M_(exp(-N Lambda))].             (8)

For fixed N the smooth bounded multipliers satisfy all preceding hypotheses. Equation (8) proves the escape-conjugation assertion. The result permits a compact remainder under this conjugation; it does not license discarding that remainder or bounding its norm independently of N.
