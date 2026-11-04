# Full polynomial Euler at a fast nonflat irrotational equilibrium

Status: CONFIRMED A447 after independent full polynomial calculation and comparison with the configured-model momentum and spectrum check. The solution is entire with a complete carrier, but grows quadratically. It does not satisfy uniform sublinearity or decay.

## 1. Statement and explicit fields

Let 0<c<1/2, omega in R, lambda in R and C!=0. Set

    kappa=1+c, a=1-2c,
    delta=sqrt(kappa^2/4+omega^2), m=lambda+kappa/2-c,
    N=diag(m+delta,m-delta), gamma=-2m=c-1-2lambda,
    ell=(omega,delta+kappa/2), f(X)=C(ell.X)^2,
    J2=[[0,-1],[1,0]].

For X=(x,y) and z in R define

    U(X,z)=(NX,gamma z+f(X)),
    Q=N+N^2+omega(J2 N-N J2),
    P(X,z)=-X.QX/2-gamma(1+gamma)z^2/2.

Then U,P solve the full rotating Euler equation everywhere, div U=0. Their carrier B=(cI-omega J)y+U is complete in both directions. At the origin B=W=0, DW has rank1 and square0, and

    spec DB(0)={lambda,lambda+kappa,-a-2lambda}.

Thus the stationary backward exponent is max(-lambda,a+2lambda), and can exceed any prescribed number by increasing lambda. This is an exact local-identity countertest on the nonflat zero-vorticity equilibrium stratum. Its quadratic growth prevents any conclusion about the entire decaying class.

## 2. Momentum and pressure checked directly

The divergence is tr N+gamma=0. The horizontal carrier matrix is

    D_h=cI2+N-omega J2
       =[[lambda+kappa/2+delta,omega],
          [-omega,lambda+kappa/2-delta]].

Direct multiplication gives D_h^T ell=lambda ell: the first component cancels the two terms involving delta+kappa/2, while the remaining second component is omega^2+kappa^2/4-delta^2=0. Hence

    (D_h X).grad f=2lambda f.

The horizontal nongradient momentum is

    (1-c)NX+N D_h X+omega J2 NX=QX.

The matrix Q is symmetric, because N is symmetric and (J2N-NJ2)^T=J2N-NJ2. It is canceled by the horizontal gradient of P. In the vertical component, B_z=(c+gamma)z+f, so the nongradient momentum is

    gamma(1+gamma)z+(1-c+gamma)f+(D_h X).grad f.

The coefficient of f is 1-c+gamma+2lambda=0. The pressure's z derivative cancels the remaining term. This checks all three momentum components with a genuine single-valued polynomial pressure. No pressure Poisson implication, missing harmonic normalization or boundary integration is used.

## 3. Vorticity, its derivative and resonance

Symmetry of N gives

    W=(f_y,-f_x,0)=-2C(ell.X)(J2 ell,0),
    DW=-2C (J2 ell,0) tensor (ell,0).

The vector ell is nonzero because delta+kappa/2>0. Thus DW has rank1, and DW squared is zero since ell.J2ell=0. In particular W(0)=0 and the first derivative is nonzero.

At zero Df=0, so DB is block diagonal with D_h and c+gamma. The eigenvalues of D_h are lambda and lambda+kappa because delta^2-omega^2=kappa^2/4. The third is -a-2lambda. They are all real. At the stationary orbit the backward derivative is exp(-t DB(0)); possible coincident rates do not alter its Lyapunov exponents. Their maximum is max(-lambda,a+2lambda), since -lambda-kappa<-lambda.

The same identities give D_h J2ell=(lambda+kappa)J2ell. Therefore

    DB(0)DW(0)-DW(0)DB(0)=kappa DW(0).

This verifies the exact first-jet resonance directly, with DW an actual curl derivative. Taking lambda positive gives two positive forward eigenvalues and one negative one, so the equilibrium is hyperbolic and has index-1. For sufficiently large lambda its backward top exponent exceeds any specified L>0, including2a. No finite algebraic upper bound follows from full local Euler, even on this nonflat stratum.

## 4. Complete carrier flow and failure of the global target conditions

For arbitrary initial (X0,z0), the exact carrier equations are triangular:

    X(t)=exp(t D_h)X0,
    z(t)=exp((c+gamma)t)
       [z0+integral_0^t exp(-(c+gamma)s) f(exp(sD_h)X0) ds].

Every integral over a finite positive or negative interval is finite. Thus every carrier orbit exists for all real time. This slightly strengthens the source's generic caveat about possible incompleteness; that caveat is unnecessary for this particular family. Completeness does not supply an absorbing ball. Indeed if lambda<0 a horizontal orbit in its lambda eigendirection escapes under backward time. If lambda>=0, the invariant vertical axis has forward rate -a-2lambda<0 and every nonzero point on it escapes under backward time. Thus no backward absorbing ball exists for any lambda.

Since C!=0 and ell!=0, U has a nonzero quadratic term along a horizontal ray. Hence neither uniform sublinearity nor decay holds. This alone disqualifies the example from the target class, even though it is entire, smooth, divergence-free, exact and carrier-complete. The equilibrium derivative cocycle requires no behavior at infinity and is fully defined independently of this discussion.

The helicity is

    U.W=-2C(ell.X)(NX).J2ell.

Using symmetry of N and the explicit matrices gives

    N J2ell=(lambda+1)J2ell-omega ell.

For omega!=0 the right side cannot vanish, since ell and J2ell are independent. Thus the helicity polynomial is not identically zero. When omega=0 it vanishes identically exactly at lambda=-1; this special field still grows quadratically. No global helicity-free sublinear example is obtained.

## 5. Verification and scope

The proof is an explicit polynomial calculation for all real parameters in the displayed ranges. It needs no existence or compactness theorem and no numerical computation. The submitted checker and its retained initial symbol issue are separate finite verification records; the proof does not infer its symbolic identities from their output.

The construction realizes the entire resonant spectral family in Section6 of the C32 reconstruction. It does not show that every nilpotent matrix permitted by that commutator is realizable, and it does not realize a large degenerate-core exponent in a decaying profile. In particular the componentwise bound Gamma_E<2a remains an additional hypothesis for the confirmed C2 coverage theorem.
