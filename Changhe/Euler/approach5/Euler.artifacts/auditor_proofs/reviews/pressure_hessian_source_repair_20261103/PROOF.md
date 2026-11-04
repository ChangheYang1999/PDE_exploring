# The repaired moving-frame pressure identity

## 1. Setting and corrected identity

Let 0<c<1/2, omega be real, Jx=e3 cross x, and let U in C2(R3;R3), P in C1(R3) solve div U=0 and (1-c)U+DU((cI-omega J)x+U)+omega JU+grad P=0. Work on {Omega=curl U!=0}. The equation improves P to C2. Put B=(cI-omega J)x+U, S=sym DU, n=Omega/|Omega|, s=n.Sn, b=Sn-sn, eta=U.n and p_nn=n.D2P n. No decay is needed for the local algebra.

A790-A793 independently established

    B.eta=-(1-c)eta+U.b-n.grad P,
    B.b=-(1+2s)b-|b|^2 n-omega Jb-D2P n+p_nn n.

Differentiating the first identity along B therefore gives exactly the pressure-Hessian contribution

    -n.D2P(B+U)+eta p_nn

to B2 eta. The repaired Theory Agent B source now contains this missing term. The dependent identity obtained from n.H=-a eta, a=1-2c, is

    p_nn=-a n.eta-n.D2(|U|^2/2+(Ax).U)n-(n.grad n).grad H.

These statements are proved in the complete seven-section derivation in the team records. The repaired source matches them. Neither has an established sign.

## 2. Vanishing of the product is not equivalent to zero helicity

The source adds that eta p_nn vanishes exactly in the helicity-free case. The implication from zero helicity is valid; the converse is not a local algebraic fact. The following exact affine solution tests it.

Set omega=sqrt(2)=s0 and, for any c,

    U=(x+s0 y, s0 x-z, y-z),
    P=-3s0 xy-(5/2)y^2+z^2/2.

Its derivative G and pressure Hessian Pi satisfy

    G = [1,s0,0; s0,0,-1; 0,1,-1],
    G+G^2+omega[J,G] = [0,3s0,0; 3s0,5,0; 0,0,-1] = -Pi.

Also tr G=0. For an affine U=Gx, this matrix identity is exactly the full profile momentum equation. Hence the example is a genuine smooth local and global polynomial solution of the equations. Its curl is Omega=2e1, so n=e1, eta=x+s0 y and p_nn=0 identically. Therefore eta p_nn=0 while helicity=2(x+s0 y) is not identically zero.

This field is nondecaying and is not a counterexample in the campaign class. It refutes the asserted local equivalence. The safe source wording is that the term vanishes in the helicity-free case.

## 3. The mean does not yet contradict anything

For any invariant probability covered by A119,

    integral(|b|^2-p_nn)=2+integral(s-1)^2.

Thus integral|b|^2<2 implies integral p_nn<0. It does not alone contradict this identity. A further independently justified pressure sign or comparison is needed. The source's parent Section 14.6(v) has the correct negative-mean interpretation; the compressed new Section 3(c) must retain that qualification. Exhaustion of all local differentiated identities remains open, as already recorded in A795.

The updated source, the exact affine matrix and the prior full proof were checked analytically. No numerical computation or formalization was used.
