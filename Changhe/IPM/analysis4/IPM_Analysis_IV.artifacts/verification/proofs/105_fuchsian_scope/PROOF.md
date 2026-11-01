# Scope of the proposed Fuchsian argument and an analytic-input obstruction

Status: PROVED algebraic scope statements and arbitrary-input counterexample, independently reviewed in V312. Bibliography metadata and the cited original hypotheses were checked directly in V206. No conclusion about nonlinear-series convergence follows.

## Statements and hypotheses

Let delta=a/b be a reduced rational number in (0,1), c=(1-delta)^(-1), g=gcd(a,2), h=a/g, and q_0=2b/g. Use the canonical polynomial-log Poisson inverse with the whole resonant stream constant removed, as in topics10 and104. Put P_n=2-n delta and D=partial_t, with t=log r.

The following statements concern the specified representation of the equations and arbitrary input sequences. They do not prove convergence or divergence of the generated nonlinear stationary sequence.

1. The Poisson symbol C(n,q)=(2-delta n)^2-q^2, for positive even q, has infinitely many exact resonances. At delta=2/3 it fails every eventual lower bound |C(n,q)|>=c_0(n+q+1)^2 with c_0>0, even after exact resonances are excluded.
2. The direct local-angle Poisson equation has a nonzero linear coefficient of the second angular derivative at the singular variable z=r^(-delta)=0. It therefore fails condition C2(iii) of Tahara and Yamane's 2008 Theorem4.1 in that direct formulation.
3. There exists an arbitrary density sequence satisfying the sharper canonical log-degree and frequency bounds, with M_n<=1 and an analytic lift in independent variables z and z^(q_0)t, whose canonically inverted stream coefficient norms have no geometric bound. This shows that an analytic logarithmic lift and those support bounds alone cannot supply the needed uniform inverse estimate.

These are failures of particular sufficient hypotheses. They do not exclude a different reduction, an adapted norm exploiting the nonlinear recurrence, or a different theorem.

## The transformed equations and the joint symbol

Set rho=r U(z,theta), psi=r^2 V(z,theta), z=r^(-delta), and Z=z partial_z. Here Z differentiates the logarithmic dependence too. Since r partial_r z=-delta z, the stationary equation c x dot grad rho-rho+u dot grad rho=0 gives

    (c-1)(Z-1)U = ((2-delta Z)V) partial_theta U
                  -(partial_theta V)((1-delta Z)U).

The relation -Delta psi=partial_x rho gives

    -[(2-delta Z)^2+partial_theta^2]V
       =cos(theta)(1-delta Z)U-sin(theta)partial_theta U.

The identities follow by substituting r partial_r=(degree)-delta Z and the polar velocity u_r=-psi_theta/r, u_theta=psi_r. They agree with the independently derived coefficient recurrence in topic01.

On z^n sin(q theta), the second-order block has symbol C(n,q), up to overall sign. For every integer j with hj>=2,

    n=q_0 j,    q=2hj-2

is an exact positive-even-frequency resonance: delta n=2hj, so 2-delta n=-q. These pairs are unbounded.

At delta=2/3 choose n=3k+2 and q=2k for k>=1. Then

    P_n+q=2/3,
    C(n,q)=4/9-8k/3,
    |C(n,q)|/(n+q+1)^2=(8k/3-4/9)/(5k+3)^2 -> 0.

The divisor is nonzero at every such pair. This proves statement1 without invoking a literature theorem. More generally, writing x=exp(i theta) changes the principal part, after division by its radial coefficient, to

    lambda^2-delta^(-2) nu^2.

Its roots in lambda at nu=1 include the positive number 1/delta. Thus the unchanged block fails the Poincare condition of the directly checked 2003 theorem. The local-angle representation also fails A3: its second angular derivative coefficient is a nonzero constant. Changing to x=exp(i theta) makes that coefficient proportional to x^2, but gives the positive principal root just computed, and does not eliminate the separate Laurent-versus-holomorphic issue.

## The directly checked Fuchsian hypotheses

The 2003 paper, Theorem2 on page1098, assumes A1-A3 and condition(P). A3 requires the linear coefficient of a tangential derivative of order alpha to vanish to order alpha in x; (P) excludes nonnegative real principal roots. Proposition1 on page1097 gives finiteness of the resonance set and a linear lower bound on each nonresonant root factor. Theorem2 then gives a holomorphic representation in finitely many variables t(log t)^j. These are directly checked source statements, distinct from our algebraic application above.


Tahara and Yamane, "Logarithmic singularities of solutions to nonlinear partial differential equations," Journal of the Mathematical Society of Japan60(2) (2008),603-630, DOI10.2969/jmsj/06020603, state Theorem4.1 under conditions C1 and C2. In C2(iii), the derivative of the right-hand side with respect to every unknown involving a positive tangential derivative order must be O(|z|^s) for one s>0 as z tends to zero in the stated sectors, uniformly on the specified tangential domain.

Expanding the Poisson block above gives

    Z^2 V=(4/delta)ZV-(4/delta^2)V
          -(1/delta^2)partial_theta^2 V-(1/delta^2)R(U),

where R(U)=cos(theta)(1-delta Z)U-sin(theta)partial_theta U. The coefficient of partial_theta^2 V is the nonzero constant -1/delta^2. It is not O(|z|^s) for any s>0. Hence the direct scalar Poisson formulation fails that necessary hypothesis, even if U is provisionally regarded as a prescribed forcing. Treating the two equations as a system does not itself provide a scalar theorem with weaker assumptions.

Also, the change x=exp(i theta) maps a complex angular strip into an annulus. A sine polynomial is a Laurent polynomial in x, usually with poles at zero. Holomorphy near x=0 is therefore an additional issue for a theorem formulated there. This observation does not obstruct holomorphy on the annulus, and does not replace checking a proposed theorem's actual domain.

## Analytic arbitrary inputs with super-geometric stream norms

For k>=1 put

    n_k=q_0(k+1)+2,
    q_k=2h(k+1),
    m_k=q_k-1,
    s_0=2(1-delta)>0.

Prescribe F_(n_k)=t^k sin(m_k theta); take the other higher-order densities zero, with F_1=sin(theta). The sharper canonical density-degree bound is

    d_n=max(0,floor((n-1)/q_0)-epsilon),
    epsilon=1 if h=1, and epsilon=0 otherwise.

At n=n_k it equals k+1-epsilon, so k<=d_(n_k). The other bound k<=delta(n_k-2)/2 holds because the right side is h(k+1). The L=1 frequency bound holds since m_k=delta(n_k-2)-1<2n_k-1. These inputs satisfy all of those support bounds, even in the h=1 case.

Their selected output mode q_k has P_(n_k)+q_k=s_0. It is nonresonant, so its polynomial is exactly

    B_(n_k,q_k)=-J_(s_0)(t^k)/2,
    J_s=(D+s)^(-1).

There is no second density input at frequency q_k+1. Nor is there a resonant normalization subtraction at this mode. The constant coefficient of J_s(t^k) is (-1)^k k!/s^(k+1). Consequently

    M_(n_k)=1,
    N_(n_k)>=k!/(2s_0^(k+1)).

Since n_k=q_0 k+q_0+2, Stirling's elementary factorial asymptotics give N_(n_k)^(1/n_k) tending to infinity. In particular the stream sequence has no geometric coefficient bound.

Nevertheless the density has the analytic lift

    U(z,w,theta)=z F_1(theta)
       +z^(q_0+2) sum_(k>=1) w^k sin((2h(k+1)-1)theta),
    w=z^(q_0)t.

On every strip |Im theta|<=sigma this sum converges normally for |w|exp(2h sigma)<1, by the geometric-series bound on the sine factors. Thus it is holomorphic near (z,w)=(0,0), with theta in a smaller open strip. Since t=-delta^(-1)log z, it is also representable through z and z log z by substituting w=-delta^(-1)z^(q_0-1)(z log z).

This proves statement3. The shifted index n_k is deliberate. The unshifted example n=q_0 k+2 in the closing_loop response satisfies its stated weaker degree bounds but, when h=1, exceeds the sharper canonical density-degree bound by one. The shift repairs that issue without changing the mechanism.

## Dependencies, evidence and remaining scope

Topic01 supplies the sign convention; topics10 and17 supply the canonical inverse and degree bounds. Topic104 records the whole-mode resonant projection. The exact finite checks in verification/exact_checks.json test the nonresonant symbols, degree bounds and factorial constants independently through several rational examples.

The sources directory contains the original closing_loop bibliography, the publisher-deposited DOI metadata, and the original response reference note. The retained Tahara-Yamane preprint and extracted text remain in scratch with hashes recorded in the manifest. Its Theorem4.1 and C2(iii) were read directly. The 2003 publisher PDF was subsequently readable through the web document tool; the hypotheses, Proposition1 and Theorem2 were inspected there. Local direct download still returned challenge HTML, retained with an explicit content-type caveat in the access record. No challenge script was run. The earlier source-access limitation is superseded by V206; applicability after an unspecified change of variables remains OPEN.
