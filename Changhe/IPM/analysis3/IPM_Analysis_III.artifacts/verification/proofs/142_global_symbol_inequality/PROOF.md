# A positive symbol after escape and a characteristic penalty

## Statement

Use the actual background, compactified logarithmic cylinder, smooth escape function Lambda and order s of topics128 and130. Put sigma=25/4, s_0=41/20, delta=9/5, gamma=-1/2, ell=1/k, A=2ell-1, D=4ell-1 and Sigma=A+D. The exact k is1615536043799051/9007199254740992. Write W=(q,vartheta), beta=(log b)', and let p_0(X,nu)=grad rho(X).u(xi) be the local coupling principal symbol of proof 141, with the unit cylinder covector nu transported to the Cartesian covector xi. Only its direction matters.

Let Q be a closed vertical sector strictly separated from the horizontal axes, contained in the region s=sigma. On the compactified cylinder define

 m_v=1+ell-(1+beta)q-s nu^T(DW)nu-p_0,
 m_u=1+ell-(1+beta)q+2vartheta tan(theta)-vartheta cot(theta)
                                      -sigma nu^T(DW)nu-p_0.        (1)

The second symbol is defined on Q, with its continuous extension at the vertical axis. Then, for every real mu<m_x, where

 m_x=Sigma(3/2-s_0)+delta A>0.9726,

there exist finite N,L>=0 such that

 m_v+N W.grad Lambda+L(W.nu)^2>=mu,
 m_u+N W.grad Lambda+L(W.nu)^2>=mu                         (2)

on their respective compactified unit-covector bundles. The same N,L work in both inequalities. No values for N or L are certified. This is a pointwise symbol theorem, not yet a pseudodifferential inequality or a Fredholm estimate.

## The energy symbols

The cylinder Jacobian satisfies div W=2ell-2q. For the bulk variable v=h/b, transport is W.grad+beta q-1. Its negative real L2 energy is therefore multiplication by1+ell-(1+beta)q. The order-s commutator has the principal contribution -s nu^T(DW)nu to that negative energy. If the order varies, its additional term is (W.grad s)log|xi|, nonnegative at high frequency; this term is not needed for (2).

The cofactor variable is h/(b p), where p=cos(theta)^2 sin(theta). Away from the axes,

 partial_theta log|p|=-2tan(theta)+cot(theta).

Its extra transport multiplication is vartheta partial_theta log|p|, so its negative energy adds2vartheta tan(theta)-vartheta cot(theta). This proves the zeroth-order parts in (1). Proof 141 proves that the coupling principal symbol is p_0 in both variables, so subtracting its real symbol gives (1). The formulas refer to the uncut cofactor; cutoff overlap terms are not claimed to be part of this symbol inequality.

## Continuity on the compactification

The actual modal expansions give uniform convergence of W and its first cylinder derivatives to

 W_0=(-A cos(theta)^2+D sin(theta)^2, Sigma sin(theta)cos(theta))

at the inner circle, and to(ell,0) with DW tending to0 at the far circle. The coefficient beta tends to3+delta at the inner end and gamma at the far end. The order and the escape derivative have the continuous limits proved in topics128 and130.

Axis tangency and uniform convergence of the first angular derivative imply continuous extension of vartheta/cos(theta) at the vertical axis, including the end circles. For example, integrate partial_theta vartheta from the axis to theta and divide by cos(theta); the derivative convergence is uniform. This verifies the divided term in m_u. The cotangent term is bounded on Q. The physical grad rho is O(r^2) at the origin and O(r^(k-1)) at infinity, uniformly in angle, so p_0 tends to0 at both ends. These are principal-symbol rates, not the operator-norm rates of the full nonlocal coupling.

Thus both symbols in (1), E=W.grad Lambda and H=W.nu extend continuously to their stated compact domains. We have E>=0, and E>0 outside the critical set

 {P,-P,S_x^+,S_x^-,S_y^+,S_y^-} union the far circle F.

## Characteristic margins on the critical set

At P and -P, W=0 and s=s_0. The conformal cylinder change preserves the eigenvalues of the linearization there. The exact joint source symbol has minimum

 min(b_P-s_0 mu_P, b_P+g_P-s_0 A_P), b_P=1+ell.

Proof 132 independently encloses this minimum in(4.52536265678952,4.52536265685856). The source points are outside Q.

At S_x, W=(-A,0), so H=0 forces nu=(0,+/-1). There DW=diag(0,Sigma), p_0=0 and beta=3+delta. The bulk margin is

 1+ell+(4+delta)A-s_0 Sigma
 =Sigma(3/2-s_0)+delta A=m_x.                            (3)

At S_y, W=(D,0), so the characteristic covectors again are(0,+/-1), and DW=diag(0,-Sigma). Also vartheta tan(theta) tends toSigma and vartheta cot(theta) tends to0. Therefore the bulk and cofactor characteristic margins are respectively

 1+ell-(4+delta)D+sigma Sigma=79.60304794281565...,
 1+ell-(4+delta)D+(sigma+2)Sigma=142.50739927051420....    (4)

The cofactor expression also equals Sigma(sigma-1/2)-delta D. At F, DW=0, p_0=0 and the divided angular terms tend to0, so both margins are

 1+ell-(1+gamma)ell=1+ell/2=3.78768130532077....           (5)

The independent256-bit calculation in code/check.py derives (3)-(5) from the exact rational k. Every displayed critical characteristic margin is strictly larger than m_x except (3), where equality holds. In particular the minimum is m_x in both the union of the relevant critical sets and covector directions, if the absent horizontal points for Q are harmlessly included in the comparison.

## The compactness argument

Treat first either one of the two compact bundles and write m for its energy symbol. Fix mu' with mu<mu'<m_x. On the characteristic set H=0 define the closed bad set

 B={(X,nu):H=0 and m<=mu'}.

It is compact and does not meet the bundle over any critical point, by (3)-(5) and the source interval. If B is nonempty, E has a strictly positive minimum e_B on it. Choose N>=0 with N e_B>=mu'+max|m|. Then m+N E>=mu' on B, and off B within H=0 the inequality follows from m>mu' and E>=0. If B is empty, choose N=0. Thus in all cases G_0=m+N E is at least mu' on the whole characteristic set.

The closed set C={G_0<=mu} is now compact and disjoint from H=0. If nonempty, h_C=min_C |H| is positive. Choose L>=0 with L h_C^2>=mu+max|G_0|; if the right side is negative L=0 suffices. Then G_0+L H^2>=mu on C, and it is already greater than mu off C. If C is empty take L=0. This proves (2) for one component.

Apply the construction to each component and take the larger of the two N values first. Increasing N cannot spoil either inequality because E>=0. Repeat or enlarge the choices of L, which also cannot spoil positivity since H^2>=0. The two inequalities then hold with the same constants.

## Numerical illustration and scope

The theory author draft work/Hs.md contains a minor inaccurate decimal in the cofactor symbol at S_y. The exact constant term is

 1+ell-(4+delta)D+2Sigma=-54.06869862854376...,

not -54.06934. The bulk constant is -116.97304995624232... and D^2=453.75179095710307.... For the illustrative value mu=1/2, the least penalty at this single base point is L=0.2588927521552152... in the bulk and0.1202611201014578... in the cofactor. These values do not certify a global choice of L.

The compactness argument verifies Lemma Hs-sym after this decimal correction. It leaves the finite-regularity quantization, the variable-order conjugation, cutoff overlap estimates and maximal-domain limiting argument to separate proofs. None is a consequence of (2) alone.
