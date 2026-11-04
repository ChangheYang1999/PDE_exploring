# The printed modulus seminorm does not control tangent variation

## Exact claim being tested

On printed page 21 of Ben Ovadia-Burguet, arXiv:2506.18238v2, the displayed definition is

    ||d^j F|| := max_(|alpha|=j-1) Lip(|partial^alpha F|),
    ||F||_r := max_(1<=j<=r) ||d^j F||.

The absolute-value bars are inside the Lipschitz operator in the actual PDF, not merely in the text extraction. Under its literal interpretation as the Lipschitz constant of the scalar magnitude, this seminorm does not bound variation of the vector or its tangent direction. Definition 3.1 and Lemma 3.2, with that literal interpretation, do not imply the stated tangent oscillation estimate. Nor does the printed strong bound imply a common genuine C1 compact class.

This is not a disproof of the intended theorem. Replacing the displayed scalar-modulus Lipschitz constants by the Lipschitz constants of the vector derivatives is a plausible intended correction. The complete construction under that correction still requires its own audit.

## 1. An exact bounded-couple counterexample

Work in a Euclidean coordinate ball, or an isometric small ball in a flat three-torus. Fix positive a,b sufficiently small that all curves below stay in this ball, and let N be a positive integer. Put w_N=2*pi*N and

    sigma_N(t)=(a cos(w_N t), a sin(w_N t), b t), 0<=t<=1,
    theta(t)=t.

The positive third-coordinate derivative b makes sigma_N a smooth embedding. Its speed is the constant sqrt(a^2 w_N^2+b^2). Every derivative of order j>=2 has constant magnitude a w_N^j. Consequently for the vector map F(t)=sigma_N'(t), the scalar magnitude of every derivative is constant, so every displayed seminorm ||d^s F|| is zero.

Thus (sigma_N,Id) is a bounded couple in the literal Definition 3.1 for every finite regularity index r. At t=0 and t'=1/(2N), however,

    |sigma_N'(t)-sigma_N'(t')|=2a w_N,
    |sigma_N'(t)|=sqrt(a^2 w_N^2+b^2).

For a=b and N>=1, the first quantity is strictly greater than one tenth of the second. This contradicts the conclusion printed in Lemma 3.2.

The tangent-space angle conclusion of Lemma 3.3 also fails. Compare t=0 and t'=1/(4N), for which the derivative vectors are (0,a w_N,b) and (-a w_N,0,b). The cosine of the angle between their unoriented lines is b^2/(a^2 w_N^2+b^2), less than cos(pi/6) for a=b and N>=1.

The error is specifically the step bounding the difference of two vector values by a Lipschitz constant of their scalar magnitudes. Such a bound is false even when the scalar magnitudes are identical.

## 2. The strong bound does not control length

For sigma_N itself,

    |sigma_N(t)|=sqrt(a^2+b^2 t^2),
    Lip(|sigma_N|)<=b.

All higher terms in the displayed seminorm are zero, since the corresponding derivative magnitudes are constant. Thus ||sigma_N||_r<=b under the printed definition. Take a=b=epsilon/10. Then the couple is strongly epsilon-bounded in Definition 3.5 for k=1, for every N, while its length is

    sqrt(a^2 w_N^2+b^2),

which tends to infinity. Therefore the length upper bound in the remark after Definition 3.6 cannot follow from the literal strong-bound definition for any fixed dimensional constant.

## 3. Even bounded speed does not restore C1 compactness

Instead take a_N=epsilon/(10 w_N) and b=epsilon/10. The images converge uniformly to sigma_infinity(t)=(0,0,bt). Their genuine speeds are uniformly bounded, and their printed seminorms are still at most b for every r. But

    sigma_N'(t)-sigma_infinity'(t)
       =(-epsilon sin(w_N t)/10, epsilon cos(w_N t)/10,0)

has constant magnitude epsilon/10. No subsequence converges in C1, since any C1 subsequential limit would have to be the derivative of the uniform limit sigma_infinity. Thus merely replacing the source's endpoint topology by C1 does not yield compactness from its literal printed bounds.

## Scope

These counterexamples are elementary and use no numerical computation. They refute the specified printed implications under the scalar-modulus interpretation. They do not refute LIT52 or LIT53, which assume genuine C1 compactness explicitly, and do not refute the external main theorem with a corrected derivative convention. The campaign must retain the genuine derivative bounds as an external premise until the intended convention and its construction are checked.
