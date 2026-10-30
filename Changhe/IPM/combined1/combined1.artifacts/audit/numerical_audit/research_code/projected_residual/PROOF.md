# Exact first angular residual mode without the other modes

## Setting and statement

Use the finite exact rational campaign potential chi and the independently derived fields

rho=-chi_xxy-chi_yyy, U1=-chi_xyy, U2=chi_xxy,
F=(cX+U).grad rho-rho.

Let gamma=1/c, delta=1-gamma, t=r²/(1+r²), u=1-t, and p_j=(3+gamma-j delta)/2. A field obtained by d Cartesian derivatives is represented as

r^-d sum_(j,n) u^-p_j P_(j,n)(t) T_n(theta),

where T_n is the sine or cosine appropriate to its parity, and every P is an exact rational polynomial. These derivative formulas and the canonical input conversion are dependencies proved and independently checked in the radial_fourier and refit_audit topics.

There are exact rational polynomials Q_ell such that the first sine coefficient of F is

F_1(r) = r sum_ell u^(ell delta/2) Q_ell(t).

It can be assembled without computing any other residual mode. The construction below is algebraically identical to projecting the full residual onto sin(theta); it does not discard contributions from high angular frequencies whose difference is one.

## Linear contribution

For a density term r^-3 u^-p_j P(t) sin(n theta), radial differentiation gives

(cr d_r-1)[r^-3 u^-p_j P(t)]
 = r^-3 u^-p_j L_j(P),

L_j(P)=c[2tP'-3P+2t(p_j P-tP')]-P.

Only n=1 survives the projection. For the smooth campaign bases used here L_j(P) is divisible by t². Since r^-4 u^-p_j=t^-2 u^(2-p_j) and 2-p_j=(j+1)delta/2, this contributes Q_(j+1)=L_j(P)/t². The implementation checks exact divisibility, rather than substituting a limiting numerical value.

## Nonlinear contribution

Both products U1 rho_x and rho_y U2 have one cosine factor C_n and one sine factor S_m. The coefficient of sin(theta) in their angular product is

w(n,m) = [1_(m+n=1)+1_(m-n=1)-1_(m-n=-1)]/2.            (1)

This follows from cos(n theta)sin(m theta)=[sin((m+n)theta)+sin((m-n)theta)]/2 and oddness of sine. Formula (1) includes the cosine zero mode correctly: w(0,1)=1. All other frequency pairs have zero projection.

The radial product of a branch-i velocity and a branch-j density derivative is r^-7 u^(-p_i-p_j) P Q. Divide by the exterior r in F_1. Since

r^-8 u^(-p_i-p_j)=t^-4 u^(4-p_i-p_j),
4-p_i-p_j=(i+j+2)delta/2,

the contribution is Q_(i+j+2) += w(n,m) P Q/t^4. Exact divisibility of the accumulated polynomial by t^4 is checked. No small coefficient is dropped, and all arithmetic before interval evaluation is rational.

The linear and nonlinear contributions exhaust F. Finite linearity and sine orthogonality prove the construction. Frequencies larger than one enter whenever their difference is one, so this reduction is a projection, not a low-frequency approximation of the background.

## Verification and uses

For d2 and Mpen2 the builder compares every output coefficient exactly against the first sine mode of the already independently constructed full residual cache. It also records the precise input and output hashes and the number of nonzero contributing frequency pairs. A future candidate can use the same proved construction without materializing all other modes.

The rational and compact annular weak tests in the neighboring topics pair only against this first mode. All background terms in their denominators still use the complete velocity and density gradient, with every angular mode. Replacing their residual input by this exact projection changes no mathematical bound.

For a noncompact probe, all hypotheses of localized_weak_probe/PROOF.md remain necessary, including the stated background growth and residual membership. For compact annular probes the local hypotheses of annular_weak_probe/PROOF.md suffice. Projection alone does not establish either set of hypotheses and does not certify a new candidate norm or an existence result.

The output is a small exact JSON certificate input. It is not a proof by itself: the algebra, divisibility tests, source identities, and interval integration are separate dependencies.
