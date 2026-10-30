# Radial distribution of a finite angular Laplacian projection

## Statement and exact target

Let c>1 be rational, delta=1-1/c, and let the smooth finite S1 residual be

    F(r,theta)=r sum_(ell,n) v^(ell delta/2) P_(ell,n)(t) sin(n theta),
    t=r^2/(1+r^2), v=1-t,

with rational polynomials P and positive odd angular frequencies n. Fix a finite subset S of those frequencies. Let F_S be the corresponding angular projection, with all radial branches for each n in S retained. The target on 0<=R0<R1<=infinity is

    E_S(R0,R1)=integral_(R0<|X|<R1) (1+|X|^2)^2 |Delta F_S|^2 dX.

The target is the a=0 weighted Laplacian energy N(0)^2. It is not the unweighted Hessian energy. The projection energy is at most the corresponding complete angular energy on the same annulus, because the weight and annular region are radial and the sine frequencies are orthogonal. A fraction relative to the complete whole-plane N(0)^2 is a lower bound on that annulus's fraction of the complete energy, not an equality unless S contains every residual mode.

For candidate C1-N1-007-d2w-j7-e2bal, use S={17,19,21,23,25,27,29,31}. Prior complete angular integration places about94.74percent of N(0)^2 in this band. The code rechecks each mode's whole-plane energy against that retained record. This earlier value motivates the subset; it does not replace any annular integral.

## Exact derivative and radial reduction

For d=ell delta/2, define T_d P=(1-2dt)P+2t(1-t)P'. The polar Laplacian of one term is

    Delta[r v^d P(t) sin(n theta)] = r v^(d+1) L(t) sin(n theta),
    t L=T_d(T_d P)-n^2 P.

Smooth origin vanishing makes L polynomial for these inputs. The code checks division by t with zero remainder. Compose L(1-v)=v^q Q(v), factoring the leading zero exactly over the rationals. Require ell delta+2q-2>0 for every nonzero term. This makes the diagonal power below integrable at v=0 and hence every cross power integrable as well.

Angular orthogonality and r dr=-dv/(2v^2) reduce each mode's energy to pi/2 times sums of integrals of the form

    integral v^b Z(v) dv,
    b=(ell+ell')delta/2+q+q'-3 > -1,
    Z(v)=(1-v)Q(v)Q'(v).

Here Q' denotes the polynomial from the second radial branch, not a derivative. Distinct branches have multiplicity two. Every pair is included before grouping equal rational b. Products and subsequent sums are outward Arb operations on coefficients converted only after exact differentiation and endpoint factorization. The derivation, tensor convention and source assembly are the ones proved in ../candidate007_laplacian_fast/PROOF.md and ../whole_plane_norms/PROOF.md.

## Incomplete power moments

For b>-1 and Z(v)=sum_j z_j v^j, define

    A_(b,Z)(x)=x^(b+1) sum_j z_j x^j/(b+j+1),  0<x<=1,
    A_(b,Z)(0)=0.

Termwise differentiation gives A'=x^b Z(x). The finite sum and b+j+1>0 show continuity at0 and absolute integrability there. Thus the integral over x0<=v<=x1 is exactly A(x1)-A(x0). For a rational radius R, x(R)=1/(1+R^2) is rational; x(0)=1 and x(infinity)=0. Therefore

    E_S(R0,R1)=(pi/2) sum_(n in S,b) [A_(b,Z_n)(x(R0))-A_(b,Z_n)(x(R1))].

The finite polynomial is evaluated by Horner's rule, its denominators are positive exact rationals, and the positive real rational power is evaluated outward in Arb. No quadrature, extrapolated asymptotic sector or omitted radial tail is used. All annuli partition the full radial domain, including the final unbounded annulus.

## Verification protocol and scope

The manifest binds the canonical candidate, complete residual cache, assembly evidence, program, this proof, helper code and prior complete mode records. Each evaluated annular mode energy must have a positive ball and at least100relative accuracy bits. Their sum must overlap the independently retained whole-plane mode energy. Complete radial sums and cross terms are required for every selected frequency.

Two rational fixtures check the antiderivative and annular orientation before loading the candidate: integral_0^(1/4) v^(1/2)(1-v)dv=17/240 and integral_0^1 v^(1/2)(1-v)dv=4/15. The complementary integral is47/240. These fixtures check constants and endpoints, while the displayed derivation proves the general formula.

The candidate's numerical annular values remain OPEN for independent peer reproduction. This is a distribution diagnostic for one finite reference. It does not give an inverse, a nonlinear theorem, a candidate with improved residual, or a statement of nonexistence.
