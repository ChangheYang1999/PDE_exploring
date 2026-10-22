# Conditional forcing bound with explicit Hessian substitutes

Written2026-10-21 before this topic's computation. This is a conditional
postprocessing theorem. Its numerical derivative hypotheses are OPEN.

## Statement and exact inputs

Use delta=33/2000, a fixed center P from topic76, and
S(v)=1-126v^5+420v^6-540v^7+315v^8-70v^9 on[0,1], extended by1 to the
left and0 to the right. Let tau(X)=S((|X-P|-7delta/4)/(delta/2)).
Let g be a real W4,infinity function on a neighborhood of the closed disk
B_{9delta/4}(P), odd in y. Set f=tau*g and use the unitary Fourier norm
N_{lambda,s}(f)^2=int(lambda^2+|xi|^2)^s |fhat(xi)|^2 dxi.

Let Omega_j be the43949 upper-half-plane cells of topic115, restricted to the
closed cutoff disk, and reflect them across y=0. Topic115's two geometry
proofs establish coverage up to null boundaries. Let a_j be the stored
upper bound for the sum of the areas of Omega_j and its reflection.
All decimal JSON numbers are interpreted as their parsed binary64 values,
then as exact rational numbers. The precise data file is authenticated in
this topic's evidence. Assume the saved G0,G1,GL,GL1,GL2 on every Omega_j bound
|g|, |grad g|, |Delta g|, |grad Delta g|, |Delta^2 g| respectively.
Vector bounds here and below use the Euclidean norm.

Additionally assume the three saved B94 global entries S20,S11,S02 bound
|g_xx|, |g_xy|, |g_yy| throughout the cutoff disk. Set the exact rational
M=9363/1000000, and require
                         S20^2+2S11^2+S02^2 < M^2.               (1)
This inequality is a finite rational check, not proof of its derivative
hypotheses. No per-cell G2F is assumed to have been saved or verified.

For each cell, use saved T0,T1,TL,TL1,TL2. Topic115 independently proves
these bounds on |tau|, |grad tau|, |Delta tau|, |grad Delta tau| and
|Delta^2 tau|. Its stronger proof of TL establishes a bound on
                         |t''(r)|+|t'(r)|/r,                    (2)
where r=|X-P|, tau=t(r), and derivative terms vanish on the inner disk.
This stronger meaning of TL, not a bound on |Delta tau| alone, is essential.

Define exact nonnegative per-cell quantities
 A=T0 G0,
 B=T0 G1+T1 G0,
 C=T0 GL+2T1 G1+G0 TL,
 D=T1 GL+T0 GL1+3TL G1+2M T1+G0 TL1,
 E=T0 GL2+G0 TL2+2TL GL+4T1 GL1+4G1 TL1+4M TL.            (3)
For every lambda>0, put
 J3(lambda)=sum_j a_j[lambda^2(lambda^2 A_j+C_j)^2
                                    +(lambda^2 B_j+D_j)^2],
 J4(lambda)=sum_j a_j[lambda^4 A_j+2lambda^2 C_j+E_j]^2.    (4)
Then N_{lambda,3}(f)<=sqrt(J3), N_{lambda,4}(f)<=sqrt(J4), and
               N_{lambda,31/10}(f)<=J3^(9/20) J4^(1/20).    (5)
The same assertion holds for overlapping cell covers. In code the scalar C is named L and each cell is identified by its indices.

## Proof of the Hessian substitutions and product estimate

The symmetric Hessian of g has squared Frobenius norm
|g_xx|^2+2|g_xy|^2+|g_yy|^2. The hypotheses and(1) therefore give
||D2g||F<M pointwise. For r>0, the radial Hessian of tau has eigenvalues
t'' and t'/r, obtained by differentiating grad tau=t'(r)(X-P)/r.
Its Frobenius norm is sqrt((t'')^2+(t'/r)^2), bounded by(2), hence by TL.
Near r=0 all these derivatives vanish. This uses neither an absent saved
T2F nor any cancellation in the Laplacian.

Successive product rules give
 Delta(tau g)=tau Delta g+2grad tau dot grad g+g Delta tau,
 grad Delta(tau g)=grad tau Delta g+tau grad Delta g
    +2D2tau grad g+2D2g grad tau+grad g Delta tau+g grad Delta tau,
 Delta^2(tau g)=tau Delta^2g+g Delta^2tau+2Delta tau Delta g
    +4grad tau dot grad Delta g+4grad g dot grad Delta tau
    +4D2tau:D2g.
The elementary inequalities |Hv|<=||H||F |v| and
|H:K|<=||H||F ||K||F follow by Cauchy-Schwarz in the matrix entries.
Together with the two Hessian substitutes, the displayed product rules
bound |f|, |grad f|, |Delta f|, |grad Delta f|, |Delta^2 f| by A,B,C,D,E.
The factor3 in D combines2TL G1 from D2tau grad g and TL G1 from
grad g Delta tau. All terms are nonnegative and no other term is removed.
The formulas hold almost everywhere under the stated Sobolev regularity.

S'=-630v^4(1-v)^4; S and its first four derivatives match the constant
extensions at the joins. Thus f is compactly supported W4,infinity and
belongs to H4. Plancherel yields
 N_{lambda,3}^2=lambda^2||(lambda^2-Delta)f||2^2
                           +||grad(lambda^2-Delta)f||2^2,
 N_{lambda,4}^2=||(lambda^2-Delta)^2 f||2^2.
Triangle inequalities and integration over the covered disk give(4).
Reflection across y=0 preserves the relevant absolute values and norms.
Overlaps only add nonnegative integrals. In Fourier space, write the
order31/10 integrand as the product of the order3 integrand to power9/10
and the order4 integrand to power1/10. Holder with exponents10/9 and10,
followed by a square root, proves(5).

## Independent computations and dependencies

The primary computation will evaluate(3)-(4) directly in Arb256, using
only the saved area,G,T and three global derivative endpoints. A second
computation will form(3) in exact rational arithmetic and expand(4) into
nine moments, followed by iv120 evaluation of the twentieth root of
J3^9 J4. The original F0,F1,FL,FL1,FL2 outputs and original final integrals
are excluded as inputs. Both programs must validate the exact data hash,
all row identities, positivity and(1). A final audit will check all old
pins, both totals and strict rational public ceilings.

Topic115 supplies the geometric, cutoff and local-regularity arguments.
Its finite code explicitly bounds the sum in(2) in both independent
methods. The inherited physical residual derivative hypotheses remain
OPEN. This result eliminates only the need for omitted per-row Hessian
inputs in a new conditional bound. It does not prove the old FL1/FL2
values, a physical forcing norm, a global inverse, a closing inequality,
an exclusion neighborhood, or a decisive endpoint.
