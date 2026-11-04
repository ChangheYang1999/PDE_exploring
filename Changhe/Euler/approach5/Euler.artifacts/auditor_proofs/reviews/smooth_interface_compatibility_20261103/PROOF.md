# Smooth irrotational interfaces and the scalar sign

## 1. Exact local statement

Fix 0<c<1/2 and finite real omega. Let Jx=e3 cross x, X=(cI-omega J)x, a=1-2c, b=2-2c, eta=a/b and q=b/a. On a connected open set G contained in R3 minus {0}, let V,P be smooth and satisfy

    div V=0, W=curl V, k=X.V, S=P-|V|²/2,
    X.grad V=-[(1-c)I+omega J]V, X.grad P=-bP,
    -Delta P=tr((DV)^2), W.grad S=0,
    k grad S=qS grad k on {W!=0}.

Put O=int_G{W=0}. At every z in the relative boundary of O for which S(z)!=0, necessarily k(z)!=0, V(z)!=0 and S(z)<0. Writing E=|V(z)|², M=DV(z), L=(1-c)I+omega J, one has

    M=M^T, tr M=0, MX=-LV, grad k=-aV,
    grad S=-bS V/k,
    S=-2|M|² k²/(bE), R=E/|S|=bE²/(2|M|²k²).

Every W derivative vanishes at z. Every derivative of Delta(|S|^eta) also vanishes there. The last assertion is about jets at one point, not harmonicity on an open set. All norms of matrices below are Frobenius norms.

## 2. The two closures and the zero-constant issue

A boundary point of O is in its closure and in the closure of {W!=0}: otherwise a whole neighborhood would have W=0 and lie in O. Smoothness therefore makes every W jet zero there. Incompressibility gives Delta V=-curl W, and differentiation of k gives

    grad k=X cross W-aV,
    Delta k=X.Delta V-2omega W3.

Thus all Delta V and Delta k jets vanish at z. Curl and divergence give the matrix symmetry and trace, and homogeneity gives MX=-LV.

Choose a small ball about z on which S is nonzero, let h=|S|^eta and f=k/h. The rank identity says grad f=0 on its vortical open part. Every positive-order derivative of f is consequently zero at z, even if infinitely many different components approach it. Hence every multi-index alpha obeys

    partial^alpha k(z)=f(z) partial^alpha h(z).

If k(z)=0, this makes every k jet zero. The gradient formula and the zero W jets then make V infinitely flat. The point belongs to supp W. The fully reread theorem A1328-A1331, retained in verification, excludes a supported infinitely flat velocity zero with S(z)!=0 under exactly the smooth identities in Section1. Its proof uses harmonic zero extension across arbitrary irrotational patches and ordinary elliptic continuation on a transverse disk; it requires neither density nor a regular interface. Its range is all 0<c<1/2 and finite omega. Since X(z)!=0, local homogeneity integrates on the required flowbox. Its hypotheses hold here, so k(z)!=0. In particular V(z)!=0 and f(z)!=0. The identity for all jets and the zero Delta k jets now give all Delta h jets zero.

## 3. Pressure sign without a false positive source

Differentiate the rank equation on vortical points before taking limits to z. Since k and S are nonzero nearby,

    Delta S=q(q-1)S|grad k|²/k²+q(S/k)Delta k.

At z, grad k=-aV, Delta k=0 and q(q-1)a²=b, because b-a=1. Thus Delta S=bSE/k². Independently, differentiating the kinetic term in S and using Poisson gives

    Delta S=-tr(M²)-|M|²-V.Delta V=-2|M|².

The last equality is valid because M is symmetric and Delta V=0 at this interface point. It is not asserted inside a vortical region. Also M cannot be zero: MX=-LV, L is invertible and V!=0. Comparison proves the sign and all exact scalar identities in Section1. No pressure normalization is used.

## 4. Quantitative angle bounds and the regional conclusion

If e is unit, M symmetric and trace free, and Me=w, choose e as the first coordinate. The remaining block has entries u,v,v,-w1-u. Its squared norm is minimized at u=-w1/2,v=0. Therefore

    |M|²>=2|w|²-(w.e)²/2>=3|w|²/2.

Take e=X/|X| and w=-LV/|X|. Since |LV|²=(1-c)²E+omega²|JV|², and t=k²/(|X|²E) lies in (0,1], substitution into the exact R formula gives

    R<=2/[3(1-c)t].

If omega=0 the stronger first matrix bound gives

    |M|²>=(1-c)²E(4-t)/(2|X|²),
    R<=2/[(1-c)t(4-t)].

These bounds do not assert realizability of equality by a full interface solution.

If S>0 throughout connected G and W is nonzero somewhere, a nonempty O would be a proper nonempty open subset and would have a relative boundary. Section1 contradicts S>0 there. Thus O is empty, {W!=0} is dense, and continuity of grad(k/S^eta) makes it zero on G. Connectedness makes k/S^eta one constant.

## 5. The earlier finite-regularity interface

The entire A617 proof was reread to check the comparison. At its normalized equatorial point r=1,z=0 the frame matrix is diag(-p,p-1,1), p=(1-c)/c, and E=1,k=c,S=-1. If the smooth compatibility of this theorem applied, the rank and zero-Delta-k formula would give Delta S=-2p(p+1). The irrotational-side value is -4(p²-p+1). Their difference is 2(p-1)(p-2), nonzero for 1<p<3/2.

A617 has only C1,1 velocity and scalar across that interface. In particular Delta k has different one-sided behavior. The first number is the hypothetical smooth-interface requirement, not an independently computed actual vortical one-sided value after discarding a nonzero Delta k term. The contradiction diagnoses failure of the stronger regularity; it does not refute A617 or exclude every negative-scalar interface.

## 6. Scope and verification

All six submitted sections, all nine sections of A1328's dependency and all seven sections of A617's current proof were read. The sign, jet relations, matrix bounds and regional density consequence are confirmed. Smoothness, Poisson and rank are essential stated premises; W.grad S is needed in the A1328 application. Neither negative-scalar interfaces nor common-flat scalar-zero contacts have been excluded. The bare-decay campaign remains open. No computation, formal build or new model client was used. Continued comparison is requested through existing configured model agents; provider runtime remains unattested.
