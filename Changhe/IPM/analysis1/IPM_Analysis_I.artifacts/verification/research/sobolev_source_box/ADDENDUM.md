# Canonical law and the closed-ball regularity hypothesis

Read this with PROOF.md. The actual Opus5.5 proof review, completed
2026-10-21T04:52:13.962952+00:00, identified two hypothesis-matching
points. They are resolved here without shrinking the stated interval
0<delta'<=delta_h. The standalone proof's scalar claims have now passed
the two independent arithmetic methods and the exact output audit.

## 1. Canonical velocity for a noncompact Sobolev correction

The Fourier field U[h] in PROOF(1) belongs to Hs, is bounded and C2, and
has the stated parities. Its symbols give div U=0 and curl U=-h_x as
distributions and hence pointwise. Define

 psi_h(x,y)=-integral_0^y U1[h](x,t)dt.

The identity div U=0 and U2(x,0)=0 give partial_x psi_h=U2[h]; directly
partial_y psi_h=-U1[h]. Therefore -Delta psi_h=h_x and
psi_h is odd in x and odd in y. It is a C3 potential, and
psi_h,xy(0)=-partial_x U1[h](0)=sigma[h]. Since U is bounded it is
sublinear at infinity. This constructs the required whole-plane law.

For uniqueness let U* be any other whole-plane sublinear velocity with
the same divergence, curl and parities. The difference D=U*-U is
sublinear, with distributional Laplacian zero componentwise, by
Delta D1=partial_x div D-partial_y curl D and
Delta D2=partial_y div D+partial_x curl D. Mollify D with a smooth even
radial compact probability kernel. Each component f of the mollified
field is a smooth entire harmonic function and remains sublinear.
The mean-value identity for its derivative and the divergence theorem
on a radius-R disk centred at X0 give

 partial_i f(X0)=(pi R^2)^(-1) integral_(boundary B_R(X0)) f n_i,
 |partial_i f(X0)|<=2 sup_(B_R(X0))|f|/R ->0.

Thus each mollified component is constant. The parities of D and the
radial mollifier force these constants to be zero. Letting the mollifier
radius tend to zero gives D=0. This proves canonical uniqueness in the
sublinear class. The review's proposed shortcut using L2 membership of
U alone would not exclude adding a constant to a second field outside
L2. Parity is the decisive final condition here; it is not omitted.
The additive stream constant is fixed by oddness and has no velocity.

The normalized trial satisfies c_l=1/k=(1+sigma[rho0])/3 by its exact
normalization. Therefore div V0=2/k. The field
V=V0+U[h]+sigma[h]X/3 is the normalized stationary velocity for rho0+h
under that same law, whenever the center normalization is required.
The nonstationarity corollary is actually proved for the larger class of
all listed Sobolev corrections with this fixed law. It thus includes
any corrections in that class satisfying the additional center conditions.

## 2. An open regularity neighbourhood of the closed moved ball

At delta'=delta_h the closed moved ball may touch the boundary of
B_R0(P). Open-ball inclusion alone does not supply the neighbourhood
hypothesis of topic100. In this actual trial, a larger regularity
neighbourhood is available without a larger Hessian enclosure.

Every P_h under consideration lies on the axis with |p_h-p|<R=0.049.
Choose B'=B_(1/10)(P_h). The exact p bracket implies

 8 < p_lower-R-1/10 < |X| < p_upper+R+1/10 <9

for X in the closure of B'. Also 3delta'<=R0=0.0495<1/10, so B'
contains the closed source ball. Since e<3<8 and e^3>13>9, its radial
logarithms lie strictly between1 and3. The exact original knot vector
has simple interior knots and its interior range contains[1,3]. The
source-region argument of topic89 therefore gives rho0 in C6 and V0
in C6 on an open neighbourhood of this closed B'. It uses the actual
finite degree7 splines, their simple-knot C6 matching, and the moment
ODEs, not an assumed smoothness of X3.

The extra neighbourhood is needed only for regularity and extension.
The Taylor and Hessian budgets are used on the moved open B_(3delta'),
which remains inside B_R0(P), where the independently certified MV and
Mrho apply. No larger-disc derivative bound is inferred. The correction
U[h] is global Hs, and a compact cutoff of its affine strain is smooth,
so W belongs to the required Hs restriction space on B'. Choose all
cutoffs with the strict support nesting required by topic77. Their
supports are compact subsets of the moved balls. The localized velocity
has Hs norm and finite W1 because s>3; this supplies the coefficient
hypothesis of the graph-completion argument in topic100.

Thus equality delta'=delta_h is allowed, and all published ceilings are
unchanged. The scale itself satisfies delta_h<=33/2000, with equality
at h=0. No uniform comparison of moved norms or other constants follows.

## 3. Exact scope of the corollary and review corrections

Since3.2318e-7<7/50, all homogeneous location and source-box bounds
already hold at the smaller radius. In particular e0<mR and e1<m,
so P_h exists uniquely before stationarity is considered. The equation
in the corollary is precisely V[rho].grad rho=rho with the normalized
law above. The perturbation h has at least C1 regularity; the Fourier
argument in fact gives C2 when s>3, though only C1 is needed there.

The review's first angular-average arithmetic line, 2*2/(16*6)=1/8,
is false as written. The correct factorial expression is
2!*2!/(4^2*1!*1!*2!)=1/8. Its stated average and PROOF(9) are correct.
The exact recurrence diagnostic independently checks this and27 other
angular averages. The review's rounded hand values are not interval
endpoints and are not used for any acceptance check. In particular m0
is a strict lower bound, not an identity for A0-MV R0.

The threshold0.0099999/b1 is a sufficient radius obtained from a
conservative source box. It is not an optimal radius or the exact
symmetric mu margin. The actual bound here is H<=7/50.
The narrower nonstationarity statement is about the modal trial only.
An Hs radius and a residual supremum are different quantities, so their
numerical comparison cannot prove that a numerical uncertainty ball is
or is not excluded. No such inference is made, and no endpoint is reached.
