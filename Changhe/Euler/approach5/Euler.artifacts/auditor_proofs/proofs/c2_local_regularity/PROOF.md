# Exact C2 profiles without local regularity improvement

## Statement and scope

Fix \(0<c<1/2\) and \(\omega\in\mathbb R\). Write
\(J(x,y,z)=(-y,x,0)\), \(a=1-2c\), \(\kappa=1+c\), and
\(d_0=c(1-c)+\omega^2\). For every \(f\in C^2(\mathbb R)\) and primitive
\(F'=f\), the fields
\[
 U=(-cx-\omega y,\ \omega x+(c-1)y+f(x),\ z),
\]
\[
 P={d_0\over2}(x^2+y^2)-\omega axy+2\omega F(x)-z^2
\]
solve, on all of \(\mathbb R^3\),
\[
 \operatorname{div}U=0,\qquad
 (1-c)U+(B\cdot\nabla)U+\omega JU+\nabla P=0,
 \quad B=(cI-\omega J)(x,y,z)+U.
\]

There are choices of \(f\) for which \(U\) is C2 and not C3 in a
neighborhood where \(B\times\operatorname{curl}U\ne0\). For each prescribed
\(\theta>0\) there is such a choice whose second derivatives are not
locally \(\theta\)-Hölder. Thus the local profile equation, even on its
regular transverse region, gives no universal C3 or positive Hölder
improvement of C2 regularity.

These examples do not decay, are not uniformly sublinear, and do not
have a trapping backward carrier flow. They do not decide any regularity
bootstrap or nonexistence question in the decaying class.

## Complete proof

The divergence is \(-c+(c-1)+1=0\), and direct cancellation gives
\[
 B=(0,-ay+f(x),\kappa z).
\]
In particular, the transport operator has no \(x\) derivative. Since
\(\partial_yU=(-\omega,c-1,0)\) and \(\partial_zU=(0,0,1)\),
\[
 (B\cdot\nabla)U=(-\omega(-ay+f),(c-1)(-ay+f),\kappa z).
\]
Adding \((1-c)U+\omega JU\) yields
\[
 Q=(-d_0x+\omega ay-2\omega f,\ \omega ax-d_0y,\ 2z).
\]
For the second component the coefficient of \(f\) cancels. Differentiating
the displayed pressure gives \(\nabla P=-Q\), proving the equation.

The vorticity and its bracket are
\[
 \Omega=(0,0,2\omega+f'(x)),\qquad
 (B\cdot\nabla)\Omega=0,\qquad
 (\Omega\cdot\nabla)B=\kappa\Omega.
\]
Hence \([B,\Omega]=-\kappa\Omega\) and \(\operatorname{div}\Omega=0\)
hold exactly, including at points where \(\Omega\) vanishes.

Choose \(f(x)=(1-2\omega)x+x_+^p\), where \(2<p<3\). The nonlinear
term and its first two derivatives match continuously across \(x=0\).
For \(x>0\) its third derivative is
\(p(p-1)(p-2)x^{p-3}\), which is unbounded near zero. Its second derivative
divided by \(x^\theta\) is unbounded whenever \(p-2<\theta\).
Thus the assertions about regularity follow by choosing
\(0<p-2<\min\{\theta,1\}\) when necessary.

At \((0,1,0)\), \(B=(0,-a,0)\) and \(\Omega=(0,0,1)\). Their cross
product is nonzero, so continuity gives an open regular neighborhood.
Every neighborhood of this point contains the failure of C3 regularity.

Finally \(U_3=z\), so neither decay nor uniform sublinearity holds.
For the backward carrier \(\Psi\), \(x\) is constant and
\(\dot y=ay-f(x)\). Taking \(y(0)\ne f(x)/a\) produces an exponentially
escaping orbit. This proves the stated failure of trapping.

## The invariant-section contraction test

For any C2 profile with complete backward flow satisfying the exact
vorticity transport identity, put \(f_T=\Psi_T\). Then
\[
 (\mathcal T s)(x)
   =e^{-\kappa T}(Df_T(x))^{-1}s(f_Tx)
\]
fixes \(\Omega\), zero, and every scalar multiple of \(\Omega\).
On any normed section space that contains a nonzero \(\Omega\) and on which
this operator acts, a strict Lipschitz contraction is impossible:
\(\|\mathcal T\Omega-\mathcal T0\|=\|\Omega\|\).
This is a test of this unnormalized operator only. It does not exclude
a normalized construction with separately verified domination and bunching.

Likewise, \(-\Delta U=\operatorname{curl}\Omega\) does not itself improve
the a priori regularity of \(\Omega=\operatorname{curl}U\). The exact
family above prevents treating transport followed by this identity as
a local smoothing argument. A bootstrap in the decaying class requires
additional global information.

## Dependencies and verification

The proof uses only differentiation and elementary ODEs. The submitted
componentwise calculation and the coordinator's independent check were
read; no symbolic output was needed or executed in this agent.
The exact supplied construction is in the verification snapshots.
Verdict A377: CONFIRMED at this local and nondecaying scope.
