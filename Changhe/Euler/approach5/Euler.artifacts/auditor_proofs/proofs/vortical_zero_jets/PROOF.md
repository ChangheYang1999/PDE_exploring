# Exact first jets at a vortical stagnation point

## Statement

Fix c>0, omega real and p in R3. Put A=cI-omega J. A velocity first jet U(p)=u0=-Ap, DU(p)=G, tr G=0, with w=curl G nonzero, is compatible with the differentiated profile equation at B(p)=0 if and only if

    (S-omega J)w=w,  S=(G+G^T)/2.

Every such jet is realized by an exact affine profile. The remaining two eigenvalues of DB(p) may be any real pair or complex conjugate pair with sum 2c-1. These realizations are not decaying or uniformly sublinear.

## Proof

Use ax(M)_i=epsilon_ijk M_kj, so w=ax(G) and G=S+[w]_cross/2. The differentiated momentum equation at B=0 is

    D2P=-(G+G^2+omega[J,G]).

The axial vector of its right side, apart from the sign, is w-Sw+omega Jw. This follows directly from ax(G^2)=-Sw for trace-free G and ax([J,G])=Jw. Thus symmetry is equivalent to the asserted constraint, which is also (A+G)w=(1+c)w.

Conversely let C=G+G^2+omega[J,G] be symmetric and put z=y-p. Then

    U(y)=u0+Gz,
    P(y)=P0-((1-c)u0+omega Ju0) dot z-z^T C z/2

solves the profile equation exactly: B(y)=(A+G)z, its constant momentum term is canceled by the linear pressure, and its linear term is Cz, canceled by the quadratic pressure. Divergence is tr G=0.

For the spectral freedom, take

    S=diag(d,-1-d,1), w=2(v+omega)e3, v!=-omega.

Then the constraint holds and DB has the eigenvalue 1+c and a planar block

    [[c+d,-v],[v,c-1-d]].

Its other eigenvalues are c-1/2 plus and minus sqrt((d+1/2)^2-v^2). By varying real d and v while avoiding v=-omega, the quantity under the square root ranges over all real numbers. This realizes exactly all possible real or conjugate pairs with the required trace. The freedom of a pair subject to fixed trace should not be read as independence of its two eigenvalues.

## Scope of the numerical statement

The finite random rank checks in THEORY_B Proposition 8.2 do not prove generic full rank, nor full rank at every order. A nonzero exact minor would prove an algebraic generic statement at a specified order. No such exact certification has been audited here. The numerical trials remain numerical evidence. The weaker conclusion that an admissible first jet has no obstruction to some local solution at any finite order already follows rigorously from the affine realization, with all higher velocity derivatives zero. It does not show that arbitrary lower higher-order jets extend.

Dependencies: elementary matrix identities only. B10(a) is CONFIRMED; the proposed numerical-to-generic inference is not certified.
