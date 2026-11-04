# The stable vortex sheet and its degenerate curve

## Corrected statement

Let a C2 Euler profile have a vortical zero p of B. Suppose DB(p) has distinct real eigenvalues lambda3<0<lambda2<b=1+c. For the backward flow Psi_t=Phi_-t, let Ws(p) be its two-dimensional global stable manifold and Wss(p) its one-dimensional strong stable manifold. Then Omega is nonzero and tangent to Ws everywhere, in its strong contracting direction. The maximal Omega curve through p is Wss(p). On Ws,

    X^flat=-dH/(1-2c),
    U^flat=d(-H/(1-2c)-c|y|^2/2),

provided c!=1/2. On Ws outside Wss(p), the plane field span(B,Omega) equals the tangent plane and its connected leaves fill that complement.

The original assertion that Ws minus only p is a union of regular B08 leaves is false. The whole punctured strong stable curve is still in {B cross Omega=0}, where those two-dimensional regular leaves are undefined.

## Proof

The stable manifold theorem applies because all three eigenvalues of the backward vector field are nonzero. For x in Ws(p), transport gives

    D Psi_t(x) Omega(x)=exp(-bt) Omega(Psi_t x).

The right side is O(exp(-bt)) and Omega(Psi_t x)->Omega(p)!=0. Consequently Omega(x)!=0. Along an orbit tending to a hyperbolic zero, the tangent stable bundle consists of the decaying variational directions; the uniquely faster stable line, with rate -b rather than -lambda2, contains this vector. This can also be obtained from the exponential dichotomy of the variational equation, whose coefficient converges to -DB(p). It follows that Omega is tangent to Ws and to its strong stable foliation.

Let gamma(tau) be the Omega curve through p, parametrized by Omega time. The exact conjugacy is

    Phi_s gamma(tau)=gamma(exp(bs)tau).

Therefore gamma belongs to Ws, has decay rate b under Psi, and by uniqueness of the strong stable curve its maximal image is Wss(p). Differentiating the same identity at s=0 gives

    B(gamma(tau))=b tau Omega(gamma(tau)).

Thus the entire curve, not just p, is degenerate for the regular two-plane distribution.

Conversely, suppose x in Ws minus {p} has Omega(x)=q B(x). The scalar q is nonzero. Along its backward orbit the transport law gives

    B(Psi_t x)=q^-1 exp(-bt) Omega(Psi_t x).

Integrating the orbit velocity from t to infinity shows |Psi_t x-p|=O(exp(-bt)). The strong stable characterization then puts x in Wss(p). Hence the degenerate locus in Ws is exactly Wss(p).

Away from it, B and Omega are independent tangent vectors and span the tangent plane. Their flows preserve Ws: B does so by definition, and the conjugacy shows that a sufficiently short Omega displacement of a point whose backward orbit tends to p still has that limit. Iterating such displacements proves preservation for every defined Omega segment. Thus the regular distribution leaves through these points remain in Ws and fill its complement of Wss.

Finally the exact identity

    (1-2c) X + Omega cross B + grad H=0

pulls back to Ws with its cross-product term zero. This is immediate where B and Omega span the tangent plane and extends to Wss by continuity. It proves the first potential formula. Subtracting the exact form c y dot dy proves the second. Every closed curve in the immersed stable manifold therefore has zero X and U circulation.

## Explicit failure of the puncture-only claim

Take any 0<d<1+c and omega!=0 in the affine family

    U=(d x-omega y, omega x-(1+d)y,z).

Then B=((c+d)x,(c-1-d)y,(1+c)z), Omega=2omega e3. Choose d also so c+d<1+c, for example d=1/2. The backward stable plane is {y=0}; its strong stable line is the z-axis. Every nonzero point of that axis is in Ws minus {0} but has B parallel to Omega, so it is outside the regular foliation domain. This is an exact H0 counterexample to the wording, independent of global decay.

Dependencies: A002, A003, the hyperbolic stable-manifold theorem, and the exact affine construction A095. The corrected geometry and potentials are CONFIRMED; the puncture-only regular foliation assertion is REFUTED.

## B13: formula on the vortex curve, and terminology

The identity B(gamma_p(tau))=(1+c)tau Omega(gamma_p(tau)) used above holds on the whole maximal Omega-time domain through every vortical zero p of B. It follows by differentiating Phi_s(gamma_p(tau))=gamma_p(exp((1+c)s)tau) at s=0; only a neighborhood of s=0 is required for each fixed tau. Under H1-prime the Omega flow is complete by A048, so the maximal domain is all real tau. Under H0 alone no such global domain is asserted.

This establishes B13's exact formula. Calling the curve "Beltrami for B" should be avoided: curl B=Omega-2omega e3, so B parallel to Omega need not mean B parallel to curl B. For example take Omega=e1 and

    DU = [[1,omega,0],[omega,-1,-1/2],[0,1/2,0]],  U(y)=DU y.

This trace-free matrix satisfies (S-omega J)Omega=Omega, hence defines an exact affine Euler profile with quadratic pressure by A095. On the x-axis B=(1+c)x e1, but B cross curl B=2omega(1+c)x e2, which is nonzero when omega x is nonzero. The strong-stable interpretation still requires the strict spectral ordering from this proof; A057 rules out that interpretation for unrestricted vortical zeros.

Audit date: 2026-11-02T19:35:29Z.
