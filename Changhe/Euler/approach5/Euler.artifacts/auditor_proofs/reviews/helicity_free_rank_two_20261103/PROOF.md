# Rank-two vorticity derivatives at helicity-free carrier equilibria

Status: independent reconstruction of the additional LIT108 rank and threshold conclusions. The source is read in full. A468-A469 already confirm its underlying two spectral families. The refinements below await focused configured-model review and final verdict.

## 1. Statement and dependencies

Let0<c<1/2 and omega be real. Let U in C2(R3;R3), P in C1 solve the full rotating incompressible Euler profile equation, assume U=o(|y|) uniformly and U.curl U=0 everywhere. Set

    A=cI-omega J, B=Ay+U, W=curl U,
    a=1-2c, d=3c, kappa=1+c, D=1+4c.

Suppose p!=0, B(p)=W(p)=0 and K=DW(p)!=0. Put u=U(p)=-Ap and F=DB(p). Then u!=0 and p automatically belongs to closure{W!=0}. A469 gives a real rho with

    F^T u=rho u, K^T u=0, FK-KF=kappa K,
    tr F=d.                                         (1)

These identities use the global helicity-free rank theorem A413. They are not asserted for arbitrary local helicity-free germs. The commutator in(1) uses only C1 W, by first-order Taylor expansion at B=W=0. No third velocity derivative is taken.

The following additional necessary conditions hold:

1. K^3=0. If rank K=1, K^2=0.
2. If rank K=2, rho=-1 and spec F={-1,c,1+2c}. The largest backward exponent of the equilibrium atom is exactly1.
3. For spectral family I, spec F={rho,rho+kappa,-a-2rho}, the backward top exponent is max(-rho,a+2rho) and it is below2a exactly when -2a<rho<a/2.
4. For family II, spec F={rho,(-a-rho)/2,(D-rho)/2}, the backward top exponent is max(-rho,(a+rho)/2) and it is below2a exactly when -2a<rho<3a.

The two families may overlap. No globally admissible rank-two example or bound on rho is supplied. These are exact algebraic consequences for arbitrary omega.

## 2. Shift of generalized eigenspaces and nilpotence

Complexify R3 and decompose into generalized eigenspaces E_z of F. From(1),

    (F-(z+kappa)I)K=K(F-zI).

Iterating shows K(E_z) is contained in E_(z+kappa). Since kappa>0, each nonzero iteration passes to a distinct eigenvalue. Three applications would require four distinct eigenvalues in a three-dimensional space, so K^3=0. Thus K is nilpotent and its rank is at most two. If rank K=1, write K=v tensor ell. Its trace is ell(v)=0, so K^2=ell(v)K=0.

This argument permits complex spectra and Jordan blocks. It does not infer a spectral decomposition into eigenvectors before distinctness is established.

## 3. Rank two fixes the spectrum and the covector rate

If rank K=2, nilpotence in dimension3 implies K^2!=0. Choose z and a vector v in E_z for which K^2v!=0. Such a component exists by the direct sum decomposition. Then

    v in E_z, Kv in E_(z+kappa), K^2v in E_(z+2kappa)

are nonzero. The three eigenvalues are distinct and exhaust the dimension. Each generalized eigenspace is therefore one-dimensional, and F is diagonalizable over C. Trace F=d gives

    z+(z+kappa)+(z+2kappa)=d,
    z=d/3-kappa=-1.

All eigenvalues are consequently real and equal to -1,c,1+2c. The image of K is the span of the last two eigenspaces: Kv and K^2v are independent and rank K=2. By K^T u=0, image K is contained in the two-dimensional invariant plane u-perpendicular, hence equals that plane. The eigenvalue on the quotient by that plane is z=-1. The covector identity F^T u=rho u identifies this quotient eigenvalue with rho. Therefore rho=-1.

Negating the three eigenvalues gives backward exponents1,-c,-1-2c. Their maximum is1. In the target range2/5<c<1/2,2a=2-4c<2/5<1, so such an equilibrium would violate the strict C2 growth test. This is conditional on its existence in the stated global class; the algebra is not a construction.

## 4. Exact family thresholds

For family I, the backward exponents are -rho,-rho-kappa,a+2rho. The second is strictly below the first because kappa>0. Thus the maximum is max(-rho,a+2rho), which is below2a precisely when rho>-2a and rho<a/2.

For family II they are -rho,(a+rho)/2,(rho-D)/2. The last is strictly below the middle because a+D=2kappa>0. Thus the maximum is max(-rho,(a+rho)/2), which is below2a precisely when rho>-2a and rho<3a. Polynomial Jordan factors do not alter Lyapunov exponents, so repeated eigenvalues do not change these tests.

## 5. Scope and review evidence

A468 already confirms the vortical family and threshold; A469 already confirms the two nonflat irrotational families. The new rank-two refinement supplies one fixed possible spectrum, not exclusion of all carrier equilibria. Neither a surrounding nonstationary measure nor a recurrent basin is assumed, so stronger A461 support restrictions are not imported. Flat equilibria K=0 are outside this proof. Uniform sublinearity and global helicity enter through A413, with no imposed pressure normalization. No division by omega or symmetry restriction occurs.

The full LIT108 proof is pinned in the team records. The shorter generalized-eigenspace chain above independently verifies its block-matrix rank-two calculation. No computation is needed. Focused existing-agent configured-model collaboration remains pending; no new model client was used.
