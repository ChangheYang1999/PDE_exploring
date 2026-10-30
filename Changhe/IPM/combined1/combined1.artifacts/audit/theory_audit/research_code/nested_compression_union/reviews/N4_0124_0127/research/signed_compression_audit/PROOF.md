# Signed compression budget: independent proof review

## Exact statement

Let H be an infinite-dimensional real Hilbert space, A:H->H a self-adjoint
Hilbert-Schmidt operator, and S:R^d->H an injective linear map. Set
G=S* S, B=S* A S and T=tr(G^-1 B G^-1 B). Suppose C is a real number with
||A||HS^2<=C, and q>=0 is a real number such that qG-B is positive
semidefinite. Then

    C-T+q^2 >= 0,
    <Ah,h> <= sqrt(C-T+q^2) ||h||^2       for every h in H.       (1)

For the IPM commutator, A is its restriction to the even-in-x, odd-in-y
space S1. The three other parity spaces reduce the full commutator K.
If their selected finite compressions have total squared norm T_other,
then C=kappa^2-T_other is admissible, where kappa^2=||K||HS^2.
The resulting bound is an upper quadratic-form bound. It need not bound
||A||op. It does not by itself establish a PDE generator, inverse,
background bound, high-space estimate or nonlinear solution.

## Proof

The map U=S G^-1/2 is an isometry from R^d to H. Its compression matrix
D=U* A U=G^-1/2 B G^-1/2 is real symmetric. Therefore

    ||D||HS^2=tr(D^2)=T.

The matrix hypothesis says D<=qI. Write the positive eigenvalues of D in
decreasing order mu_1>=...>=mu_r>0, and the absolute values of its negative
eigenvalues in decreasing order nu_1>=...>=nu_s>0. Put alpha=mu_1 if r>0
and alpha=0 otherwise. Then alpha<=q.

The compact self-adjoint spectral theorem decomposes A into positive,
negative and zero eigenspaces. Write its positive eigenvalues as lambda_i
in decreasing order, and the absolute values of its negative eigenvalues
as eta_i in decreasing order. The finite-dimensional min-max principle,
applied to subspaces of ran U, shows lambda_i>=mu_i for 1<=i<=r. Applied
to -A it shows eta_i>=nu_i for 1<=i<=s. These comparisons also show that
A has at least r positive and s negative eigenvalues.

Set L=max(0,sup spectrum(A)). If A has a positive eigenvalue, L=lambda_1.
If D has positive eigenvalues, omit only mu_1 from the comparison above;
all remaining positive and all negative compression eigenvalues compare
with distinct full eigenvalues other than lambda_1. If D has no positive
eigenvalue, none of its eigenvalues use lambda_1. Thus in both cases

    L^2 + T-alpha^2 <= ||A||HS^2.

If A has no positive eigenvalue, D has none either, L=alpha=0, and the
same inequality is just compression contraction for the Hilbert-Schmidt
norm. Since H is infinite dimensional and A is compact, zero belongs to
its spectrum, so L=sup spectrum(A) even in this last case. Hence

    0<=L^2<=||A||HS^2-T+alpha^2<=C-T+q^2.

The spectral theorem gives <Ah,h><=L||h||^2, proving (1). For an orthogonal
reducing decomposition into four parity spaces, their squared
Hilbert-Schmidt norms add. Each selected compression uses at most its
own block's squared norm. Therefore ||A||HS^2<=kappa^2-T_other, which
proves the stated application.

## Scope checks and exact examples

The role of q cannot be dropped. On l2, let A=diag(3,2,0,...) and choose
the first coordinate as the compression. Then C=13 and T=9. The invalid
formula sqrt(C-T)=2 is smaller than the true positive bound3. The valid
choice q=3 gives sqrt(13), and no improvement over the full norm is
claimed for a one-dimensional positive compression.

Signed improvement can be strict without improving the absolute norm.
Let A=diag(-10,1,0,...) and compress to the first coordinate. Then C=101,
T=100 and q=0 satisfy all hypotheses. Formula (1) gives the sharp upper
quadratic-form bound1, while ||A||op=10. This excludes an absolute-norm
interpretation of the signed certificate.

The total T may be evaluated exactly from rational G,B. A rational LDL
factorization with positive pivots of qG-B certifies the required
positive semidefinite inequality by the stronger positive-definite
property. Strict LDL positivity is sufficient, not necessary. Rounded
floating eigenvalues, approximate Gram matrices and truncated background
integrals do not supply this certificate. If interval values are used,
C must be an upper bound, T a lower bound, and q a nonnegative upper
bound satisfying the exact matrix inequality.

## Review finding and dependencies

This independently reproduces the mathematical claim in the frozen
source/T4_PROOF.md (T4-133). Its proof correctly removes the largest
positive compression eigenvalue exactly once; no omitted off-diagonal
matrix block is assumed zero. No mathematical repair was needed.
Dependencies are the compact self-adjoint spectral theorem, finite
min-max principle, and the separately audited full IPM commutator and
parity identities. No new numerical candidate claim is made here. Any
low-generator rate c+1-theta-sqrt(C-T+q^2) remains conditional on that
generator's domain, transport and signed principal hypotheses.
