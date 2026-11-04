# Residual identities, affine tests, and moment boundary terms

## Setting

Put X=cy+U, B=X-omega Jy, Omega=curl U, q=|U|^2/2, M=(Jy).U and a=1-2c. Let R=(1-c)U+DU B+omega JU+grad P be the momentum residual. The Bernoulli function H is the one in the prompt. The first-order identities below need U,P C1. Curl and helicity identities need U C2 and div U=0; the momentum equation then gives P C2. Statements for actual solutions set R=0.

## Absolute Bernoulli and helicity

The already checked identities B.grad H=-a X.B+B.R and B.grad M=-a M-(Jy).grad P+(Jy).R give

    B.grad(H+omega M)=-a|X|^2-omega (Jy).grad P+X.R.

This checks I3b with the full residual. The vorticity residual identity is

    B.grad Omega=DU Omega-Omega-omega J Omega+curl R.

Pair this with U and pair momentum with Omega. The skew terms cancel, yielding

    B.grad(U.Omega)=-(2-c)U.Omega-Omega.grad P
                    +U.(Omega.grad U)+Omega.R+U.curl R.

Thus I8, and for solutions div(Bh+(P-q)Omega)=(4c-2)h with h=U.Omega, are exact.

Dot grad H=-aX-Omega cross B with X and Jy to obtain, for solutions,

    X.(Omega cross B)=-omega Omega.(Jy cross X),
    X.grad H=-a|X|^2+omega Omega.(Jy cross X),
    (Jy).grad H=-aM+Omega.(Jy cross X).

These check the additional B01 identities from THEORY_B Section 5(c).

## Irrotational zeros and affine examples

At an irrotational zero p, DU(p)=S is real symmetric and trace-free, so DB=cI+S-omega J. For a complex eigenvector v, the real part of v*DBv/|v|^2 is c+v*Sv/|v|^2, because v*Jv is purely imaginary. Thus every eigenvalue lambda satisfies

    c+lambda_min(S)<=Re lambda<=c+lambda_max(S).

For S=diag(1,-1,0), the spectrum is c and c+-sqrt(1-omega^2). All real parts are positive if omega^2>1-c^2. The pair is real when 1-c^2<omega^2<=1 and genuinely complex when omega^2>1; a notation using i sqrt(omega^2-1) must allow the complex square root in the first range. The field U=(x,-y,0) is an exact affine profile with P=-x^2-2omega xy, so this is not merely an arbitrary matrix test. It is not decaying.

More generally let D=diag(d,-1-d,1), A=D+vJ, and U=Ay. Since tr A=0, the profile residual without pressure is (A+A^2+omega[J,A])y. Its skew part vanishes: the horizontal off-diagonal entries of A+A^2 cancel because the first two diagonal entries of D sum to -1. Explicitly the symmetric coefficient matrix has diagonal

    (d+d^2-v^2, d+d^2-v^2, 2)

and horizontal off-diagonal omega(2d+1). Taking P=-y.(A+A^2+omega[J,A])y/2 proves the full affine family in B01. The family is independent of c at the level of momentum and fails the decay hypothesis unless trivial.

## Periodic multiplier statements and vortex-line reparametrization

On a nonstationary periodic B-orbit of period T, DPhi_T fixes B. The Cauchy identity makes Omega an eigenvector of multiplier e^{(1+c)T}. If Omega is nonzero, it cannot be collinear with B. Since det DPhi_T=e^{3cT}, the remaining multiplier is e^{(2c-1)T}. This checks P1 and P2 and gives the two-dimensional stable and unstable manifolds, including the flow direction, for 0<c<1/2.

For a frozen-vorticity curve gamma, the correct formula is Phi_s(gamma(tau))=gamma_s(e^{(1+c)s}tau). Consequently a compact vortex segment contracts backward in Euclidean length, using the bound for Omega on the compact backward-trapping set of that entire initial segment. This does not require Omega bounded on all of R3. At a vortical zero p the same formula gives B(gamma_p(tau))=(1+c)tau Omega(gamma_p(tau)), so the two local branches are B-orbits with backward limit p.

## Remaining wording limits

The displayed bad-set radius 4|omega|sup|U|/c^2 in the source omits the condition ensuring |cy+U|>=c|y|/2. The proof supplies the sufficient radius max(2sup|U|/c,4|omega|sup|U|/c^2). Decay alone does not give a global bound for DU or Omega. These are proof-scope corrections; no nonzero decaying counterexample to the target conjecture is supplied.
