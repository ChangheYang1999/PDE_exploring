# Pressure and helicity in the moving vortex frame

Status: A790-A792 and A794 CONFIRMED; source omission REFUTED A793; exhaustive obstruction OPEN A795. Independent audit of B46. The first-order identity is valid. Its stated second-order pressure inventory omits a term. The corrected identities give no pressure sign or exhaustive obstruction theorem.

## 1. Exact hypotheses and notation

Let 0<c<1/2 and omega be any finite real number, Jx=(-x2,x1,0), A=cI-omega J. Let U in C2(R3;R3), P in C1(R3) satisfy

    div U=0, ((1-c)I+omega J)U+DU(Ax+U)+grad P=0.

The local identities below also hold on any open set on which these equations hold. Set B=Ax+U, Omega=curl U, G=DU, S=(G+G^T)/2, K=(G-G^T)/2, Pi=D2P. Momentum gives grad P in C1, so Pi is continuous. No pressure normalization is needed for derivatives of P. On V={Omega!=0} put

    n=Omega/|Omega|, s=n.Sn, b=Sn-sn,
    eta=U.n, p_nn=n.Pi n, h=U.Omega,
    a=1-2c, kappa=1+c, g=U.B,
    H=P+|U|^2/2+(Ax).U, Q=P-|U|^2/2.

Here s is a scalar field, not a flow time. All n,s,b,eta are C1 on V. Since Kv=Omega cross v/2, one has Kn=0. Global velocity decay, when assumed, makes B complete by at most linear growth, but is not needed for the pointwise algebra. No global helicity condition is imposed unless explicitly stated.

For averaged statements let nu be a B-invariant probability with compact invariant support and nu(V)=1. The support may meet {Omega=0}; its zero set is required to have measure zero. All integrals below are with respect to nu. No integrability of log|Omega| is needed.

## 2. Gradient, direction and stretching equations

Differentiating momentum gives

    BG+G^2+G+omega[J,G]=-Pi.                            (1)

Indeed the derivative of GU's carrier term is (B.grad)G+G(A+G), and ((1-c)I+omega J)G+GA=G+omega[J,G]. The trace gives Delta P=|Omega|^2/2-|S|^2.

The vorticity equation and Kn=0 give

    B log|Omega|=s-1, Bn=b-omega Jn.                    (2)

Taking the symmetric part of(1) yields

    BS=-S-S^2-K^2-omega[J,S]-Pi.

Differentiate s=n.Sn. The two direction terms give2|b|^2-2omega(Jn).Sn. Since n.[J,S]n=-2(Jn).Sn and Kn=0, the rotation terms cancel and

    Bs=|b|^2-s^2-s-p_nn.                               (3)

Differentiate b=Sn-sn, using(2)-(3). The cancellations can be seen directly from S^2 n=s Sn+Sb and J(Sn)=s Jn+Jb. The result is

    Bb=-(1+2s)b-|b|^2 n-omega Jb-Pi n+p_nn n.           (4)

In particular the last term in(4) is required to project the pressure Hessian onto the plane perpendicular to n. Omitting it would even break the derivative of n.b=0.

## 3. The first-order helicity component

Using BU=-(1-c)U-omega JU-grad P and(2),

    B eta=(BU).n+U.(Bn)
         =-(1-c)eta+U.b-n.grad P.                      (5)

The two rotation terms cancel because (JU).n+U.(Jn)=0. Equivalently,

    n.grad P=U.Sn-(s+1-c)eta-B eta.                    (6)

These are the new B46 first-order identities. If global helicity is zero, eta is identically zero on V, so n.grad P=U.b=U.Sn. For general helicity, no sign is assigned to any term.

The scalar helicity equation is

    Bh+kappa h=Omega.grad g.                            (7)

For example, the Kelvin one-form identity L_B(U.dx)=-a U.dx-dQ evaluated on Omega gives Bh=-(a+kappa)h-Omega.grad Q. Since Q=H-g and Omega.grad H=-ah, this becomes(7). It is also obtained by dotting momentum with Omega and vorticity transport with U.

## 4. The corrected second derivative and its exact affine test

Differentiate(5) along B and use(4). Although eta need only be C1, its B derivative is C1 by(5), so this second directional derivative is legitimate at the stated regularity. The terms involving Pi are

    -U.Pi n+eta p_nn-n.Pi B
       =-n.Pi(B+U)+eta p_nn.                            (8)

The full identity is

    B^2 eta=-(1-c)B eta-(2-c+2s)U.b-|b|^2 eta
             -2b.grad P+omega(Jn).grad P
             -n.Pi(B+U)+eta p_nn.                       (9)

To check every term, (BU).b contributes -(1-c)U.b-omega(JU).b-b.grad P; U.Bb contributes -(1+2s)U.b-|b|^2 eta-omega U.Jb-U.Pi n+eta p_nn; and -B(n.grad P) contributes -b.grad P+omega(Jn).grad P-n.Pi B. The two remaining skew terms cancel.

Thus B46 Section2.4 omits eta p_nn from its inventory. It is zero in the helicity-free class, but must be retained in the sign-changing helicity class under discussion. This is a differentiated consequence of the first-order equations; it is not claimed to be algebraically independent of them.

An exact affine local test makes the omission visible. For any sigma>0 put

    U=(-x1/2-sigma x2, sigma x1-x2/2, x3),
    P=(1/2)(1/4+sigma^2)(x1^2+x2^2)-x3^2.

Its constant derivative G commutes with J, has trace zero and satisfies G^2+G=diag(-1/4-sigma^2,-1/4-sigma^2,2). Therefore the full rotating profile momentum equation holds for every c and omega. Here Omega=2sigma e3, n=e3, s=1, b=0, eta=x3, p_nn=-2, and B eta=(1+c)x3. Equation(9) gives B^2 eta=(1+c)^2 x3. Dropping eta p_nn instead gives this value plus2x3. The affine profile is smooth and exact but not decaying; it is a test of the local differentiation, not a counterexample to the campaign conjecture.

There is also a direct vortex-direction identity. Let psi=|U|^2/2+(Ax).U, so H=P+psi and n.grad H=-a eta. Differentiating along n gives

    p_nn=-a n.grad eta-n.D2psi n-(n.grad n).grad H.       (10)

All terms exist at C2/C1 regularity. This is another dependent local coupling between helicity and p_nn. The literal assertion that no local identity couples them is therefore incorrect. Neither(9) nor(10) supplies a favorable sign.

## 5. What invariant probabilities actually give

All of s,b,eta,P derivatives in these formulas are bounded on the compact support wherever n is defined. Their B derivatives in(2)-(5),(9) are bounded there as well. Invariance and the fundamental theorem along each orbit therefore give zero mean for the B derivative of every bounded observable used below, by dominated convergence. No derivative of the measure along vortex lines is assumed.

First, integral s=1. To avoid an unjustified logarithmic integral, apply the ergodic theorem to the bounded observable s-1. Its time average equals the limit of [log|Omega(Phi_T x)|-log|Omega(x)|]/T. The upper bound on |Omega| makes this limit at most zero. For almost every nonzero point, recurrence to some set {|Omega|>=1/m} supplies a sequence of arbitrarily large times on which that quotient tends to zero from below or above. The ergodic limit is therefore zero. Integrating the time-average identity gives integral(s-1)=0. Equivalently use the integer-time theorem and the unit-time integral of s-1.

Equation(3) now gives

    integral(|b|^2-p_nn)=2+integral(s-1)^2.               (11)

Equation(5) gives

    integral n.grad P=integral U.b-(1-c)integral eta
                     =integral U.Sn-integral(s+1-c)eta. (12)

The symmetric part of(1) gives the matrix moment

    integral(S+S^2+K^2+omega[J,S]+Pi)=0.                 (13)

This symmetric matrix has six independent entries; its trace is the already included Poisson identity, not an additional independent seventh fixed-frame constraint. One may also average(9), since B eta is bounded and C1 along the flow. Its resulting weighted pressure moment is

    integral eta p_nn
      =integral[(2-c+2s)U.b+|b|^2 eta+2b.grad P
                  -omega(Jn).grad P+n.Pi(B+U)].          (14)

The means of B eta and B^2 eta vanish. Equation(14) still has no sign and does not reduce to(11).

If integral|b|^2<2, (11) forces integral p_nn<0. If b=0 almost everywhere, it forces integral p_nn=-2-integral(s-1)^2<=-2. These are pressure-concavity conclusions, not contradictions by themselves. A separate nonnegative mean-p_nn bound together with integral|b|^2<2 would contradict(11). The parent THEORY_B Section14.6(v) correctly calls its conclusions sign conditions; the B46 wording that they alone suffice to close the obstruction is too strong.

## 6. Material domains and boundary terms

For a bounded C1 material domain D_t=Phi_t(D), Reynolds transport, div B=3c and(7) give

    d/dt integral_(D_t) h
       =-a integral_(D_t)h+integral_(boundary D_t) g Omega.normal.
                                                               (15)

The constants satisfy3c-kappa=-a. The divergence theorem is legitimate for the bounded smooth domain. If a domain is invariant, has finite helicity and has vanishing vortex flux at every boundary including infinity, (15) gives zero total helicity. On an unbounded domain, finite integral|h| alone does not justify deleting the separate g Omega cutoff term in this derivation.

For the natural-tail and canonical-pressure setting of Theory Agent A OB.1, the confirmed A524 proof supplies the needed integrated conclusion for every measurable vortex-invariant set without requiring a smooth boundary: use Omega.grad H=-ah and the cutoff estimate integral H Omega.grad chi_R=O(R^(2-2p))->0. That is the appropriate existing justification there. No extra bare-decay flux theorem is asserted from(15).

## 7. Verdict scope and verification

The B46 first-order identity and its compact invariant-probability averages are confirmed by the derivation above. The pressure inventory in Section2.4 requires the missing eta p_nn term; the claim of no local coupling is refuted by(9)-(10). The proposed exhaustive list of all possible differentiated or averaged identities remains open. Its own source disclaims a proof of exhaustion, and none is supplied here.

The full B46 source, the parent THEORY_B Section14.6 and the confirmed OB.1 argument were read. The explicit affine matrix and every term of(9) were checked analytically. No computation or formal build was needed. Existing configured model agents are asked to compare the correction, without a new client or agent; runtime is independently unattested.
