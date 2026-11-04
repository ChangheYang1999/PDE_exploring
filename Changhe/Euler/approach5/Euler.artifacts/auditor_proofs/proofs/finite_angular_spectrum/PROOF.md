# Finite angular spectra: exact consequences and limits

## Setting

Let U in C2(R3;R3), P in C1(R3) solve the rotating profile equation with div U=0, c>0, finite omega and U tending uniformly to zero at infinity. Write U_m and P_m for the Cartesian-covariant angular Fourier projections, so

    U_m(R_theta y)=exp(i m theta) R_theta U_m(y),
    P_m(R_theta y)=exp(i m theta) P_m(y).

Assume the velocity support S={m:U_m is not identically zero} is finite, nonempty, symmetric under m -> -m, and L=max S>=1. A073 gives S contained in S+S. All statements below retain the finite-spectrum hypothesis. The exclusion of an axisymmetric nonzero profile follows from A010 in 0<c<1/2; no such exclusion is imported here for every c>0.

## The finite support test

If 0 belongs to S, the inclusion S contained in S+S is automatic. If 0 does not belong to S, put S_+=S intersect positive integers. Then the inclusion is equivalent to

    every m in S_+ belongs to (S_++S_+) union (S_+-S_+).

In particular max S_+ must lie in S_++S_+. To see this, decompose any representation m=k+l according to the signs of k,l. Two negative summands cannot give positive m. Opposite signs give a difference of positive elements. The maximum cannot be such a difference, since it would require a strictly larger element in S_+. Conversely either a positive sum or a difference gives the required representation in S+S, and symmetry handles the negative elements.

With exactly one positive element no representation of the maximum is possible. With exactly two positive elements a<b, the only positive sum that can represent b without exceeding b is 2a, so b=2a. This condition also suffices, since a=b-a and b=a+a. The stated examples {plus/minus 1,plus/minus 2}, {plus/minus 1,plus/minus 2,plus/minus 3} and {plus/minus 2,plus/minus 3,plus/minus 5} all pass. This is only a combinatorial necessary test, not an existence result or a complete nonlinear classification.

## Pressure support and the highest-mode equation

Put N_m=sum_{k+l=m}(U_k dot grad)U_l. Angular projection of momentum gives

    (1-c)U_m+c(y dot grad)U_m-i m omega U_m+N_m+grad P_m=0.

The sign convention matches the covariance above. If m is outside S, then N_m=-grad P_m. If |m|>2L, the sum N_m is zero, so P_m is constant. Its nonzero angular character forces that constant to vanish. Thus the pressure has no modes outside [-2L,2L], up to its irrelevant additive mode-zero constant.

At m=2L the only nonlinear pair is (L,L). Therefore Z=U_L is a nonzero C2 complex divergence-free field on all of R3, tending to zero, and

    (Z dot grad)Z+grad P_(2L)=0.                          (1)

For m in S the nonlinear term N_m cannot be a gradient by the decaying linear-kernel argument in A073. This confirms the exact parts of Proposition 2.1. Merely counting equations and unknowns does not prove incompatibility of the resulting system.

## Conditional homogeneous-tail compatibility

Assume additionally, mode by mode, that

    U_k=Z_k^0+R_k,
    Z_k^0(t y)=t^{lambda_k}Z_k^0(y),
    lambda_k=-p+i k omega/c, p=(1-c)/c,
    |D^j R_k(y)|=o(|y|^{-p-j}), j=0,1,2,

uniformly in angle. The fields Z_k^0 must be C2 on the punctured space and correspond to globally regular spherical vector fields, rather than singular coordinate components at the poles. For every m outside S,

    curl sum_{k+l=m}(Z_k^0 dot grad)Z_l^0=0.             (2)

Indeed, curl N_m is zero by the preceding section. Replacing one or both factors by their remainders gives o(r^{-2p-2}); the derivative assumptions through order two are exactly what this estimate uses. The remaining finite sum is homogeneous of the common complex degree -2p-2+i m omega/c. A homogeneous function of this degree which is o(r^{-2p-2}) vanishes identically, by restriction to each ray. Divergence-free U_k similarly implies div Z_k^0=0. This proves the displayed compatibility lemma, including the highest-mode special case.

The sentence that no condition occurs at the same order in retained modes is not part of this rigorous conclusion. It requires an actual formal solvability calculation, with the scalar pressure homogeneity and possible resonances kept. In the target range 2/5<c<1/2, p lies in (1,3/2), so the real number 2p is not an integer, which removes the particular spherical-harmonic pressure resonance mentioned in the draft. That observation by itself is not an existence theorem for a full asymptotic expansion, especially in the broader stated range 0<c<1/2.

Even if (2) forced the leading highest-mode coefficient to vanish, the entire mode need not vanish. For example, a homogeneous harmonic scalar h on the exterior, of degree d and angular character L, gives a linear solution Z=grad h with

    P_lin=-[1-2c+cd-i L omega]h.

This follows from (y dot grad)grad h=(d-1)grad h and angular covariance. Negative harmonic degrees d=-ell-1, ell>=L, give faster decaying gradients. Their possible presence is why a leading-tail exclusion needs a further argument before it excludes finite spectra.

## Smooth decaying solutions of the isolated highest-mode equation

For every positive integer L, equation (1) by itself has a nonzero smooth decaying entire solution of exactly that angular character. This is an elementary complex Beltrami construction, not a rotating-profile construction.

Let r=|y|, set f(r)=sin r/r with its analytic value at zero, and define

    D_+=partial_x+i partial_y,
    psi=D_+^L f,
    T=curl(psi y)=grad psi cross y,
    Z=curl T+T.

The radial function f is analytic in r^2, solves (Delta+1)f=0 everywhere, and so does psi. It is smooth at zero, and

    psi=(x+i y)^L (r^(-1)partial_r)^L f.

This formula follows inductively because D_+(x+i y)=0. It gives angular character L. The operations curl and multiplication by the radial vector y preserve the corresponding vector covariance, so Z has exactly that character.

Since (Delta+1)(psi y)=2grad psi, taking curl gives (Delta+1)T=0. Also div T=0. Therefore

    curl Z=curl curl T+curl T=-Delta T+curl T=T+curl T=Z.

Consequently div Z=0 and the bilinear vector identity gives

    (Z dot grad)Z=grad(Z dot Z/2)-Z cross curl Z
                 =grad(Z dot Z/2).

Thus P_top=-Z dot Z/2 solves (1). Here the dot product is complex bilinear, as required in the complex steady equation.

The field is nonzero. The scalar psi is a nonzero radial factor times the harmonic homogeneous polynomial (x+i y)^L. Its angular Laplacian is -L(L+1)psi. Since T=grad_S psi cross n,

    n dot curl T=-Delta_S psi/r=L(L+1)psi/r,

which is not identically zero, whereas n dot T=0. Hence Z is nonzero. Finally (r^(-1)partial_r)^L f and its first derivative are O(r^{-L-1}) for large r. In T the radial derivative part of grad psi disappears in the cross product with y; the remaining angular polynomial has degree L. Thus T=O(r^-1), and differentiating once gives curl T=O(r^-1). The field Z tends uniformly to zero.

Its energy growth can also be checked explicitly. Write Y(n)=(n_x+i n_y)^L and psi=q(r)Y(n), where q(r)=r^L(r^(-1)partial_r)^L(sin r/r) is real. Set W=grad_S Y and V=W cross n. Then

    T=qV,
    curl T=(q'+q/r)W+L(L+1)qY n/r.

The real part of V dot conjugate(W) is zero. If N=integral_S2 |Y|^2>0, integration by parts on the sphere gives integral |W|^2=L(L+1)N. Hence

    integral_S2 |Z(rn)|^2
      =L(L+1)N[q^2+(q'+q/r)^2]
        +L^2(L+1)^2 N q^2/r^2.

Here q=r^-1 sin(r+L pi/2)+O(r^-2) and q'=r^-1 cos(r+L pi/2)+O(r^-2). It follows that

    integral_(|y|<R) |Z|^2=L(L+1)N R+O(log R).

For the target range, the profile exponent 5-2/c lies strictly between zero and one. Thus this construction's linear energy growth explicitly differs from the profile energy law; the failure is not merely an unexamined assertion about its tail.

This example establishes only that smoothness, decay, one angular character and the isolated complex steady highest-mode equation are compatible. It does not satisfy the remaining profile modes, the natural profile energy law, or the prescribed homogeneous tail with degree -p+i L omega/c. It cannot be used as a counterexample to the main conjecture or to the homogeneous top-tail problem.

## Dependencies and verification

The support and kernel implications use A073. All other calculations are exact vector calculus and finite Fourier projection. No Galerkin search, small optimization loss or numerical rank is used as proof.
