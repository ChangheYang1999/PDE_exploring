# Discontinuity of the third obstruction in the critical weighted norm

Date: 2026-10-20. Status: complete informal proof. This is a theorem about compatible axis data, not coupled profiles.

## Statement and hypotheses

Fix A>2, beta=2/A in(0,1), and L>0. Let w_0 be smooth on[0,L], odd and analytic near0, with

    w_0(0)=w_0(L)=0, w_0'(0)=-A, w_0'(L)=A,
    w_0<0 on(0,L).

Let g_0 be the positive solution of w_0 g_0'=(w_0'-A)g_0 normalized by g_0/x^2->1 at0, and suppose g_0 extends smoothly and positively toL. These hypotheses hold for the R12 rational axis data. Fix0<r_0<min(1,L)/2. For perturbations supported in(0,r_0), define the critical weighted norm

    ||v||_crit=sum_(i=0)^2 sup_(0<x<=r_0) x^(i-7-beta)|v^(i)(x)|.

Taylor coefficients of orders1,3,5,7 and every fixed tail norm can be added: they are unchanged in the construction below. For each compatible w define g in the same way, a=(g'-w'')/2, Q=a/g^3, m=-w/g, h=A+1-w', F=-a g'+a'g/3, H=A^beta g^3 m^(-beta), and

    B[w]=-FP int_0^L F/(wH) dx.

The finite part at0 removes divergent powers with no added constant. Then there are smooth compatible perturbations v_N, each vanishing on a neighborhood of both endpoints, such that

    ||v_N||_crit ->0,
    B[w_0+v_N]-B[w_0] -> kappa_A,
    kappa_A=(1-beta)(6+beta)(7+beta)/(6A)>0.               (1)

Thus B is not continuous at w_0 in this critical norm, even on smooth compatible traces sharing all center Taylor coefficients and the same source segment. A single shrinking bump at critical amplitude does not prove this: its critical norm is constant. The construction here spreads amplitude1/N over a logarithmic interval of lengthN.

## The finite-part formula

The first axis equation gives m'=-A/g. Direct differentiation gives F=g^4 Q'/3 and wH=-A^beta g^4 m^(1-beta). Therefore

    B[w]=1/(3A^beta) FP int_0^L Q' m^(beta-1) dx
         =(beta-1)A^(1-beta)/3
                FP int_0^L [Q-Q(L)]m^(beta-2)/g dx.      (2)

For completeness, integrate by parts using Q-Q(L). AtL this difference is O(L-x), m is comparable toL-x, and their boundary product is O((L-x)^beta), which tends to0. At0, odd analyticity of w and normalized g imply g=x^2(1+O(x^2)), Q is a Laurent series beginning at worst with x^(-5) in steps of2, and m=(A/x)(1+O(x^2)). The product(Q-Q(L))m^(beta-1) has no constant term since0<beta<1; its finite part is0. This proves(2). Its source integral converges. All traces constructed below equal w_0 near0, so their finite parts exist and their lower Taylor terms coincide.

## The perturbations and their norm

Choose a fixed smooth chi onR with0<=chi<=1, chi(t)=0 for t<=0 and chi(t)=1 for t>=1. For integers N>=3 define

    t=log(r_0/x),
    a_N(x)=chi(t)chi(N+2-t),
    v_N(x)=N^(-1)x^(7+beta)a_N(x),   0<x<L,

extended by0 outside its support. It is supported in[r_0 exp(-(N+2)),r_0], is flat at its two support endpoints, and its odd extension is smooth and unchanged from0 near the center. All derivatives of the two cutoff factors in t up to each fixed order are bounded uniformly inN. Since d/dx=-x^(-1)d/dt, for i=0,1,2,

    |v_N^(i)(x)|<=C_i N^(-1)x^(7+beta-i).                (3)

This proves ||v_N||_crit<=C/N. Since |w_0| is comparable tox near0 and positive away from the endpoints, |v_N/w_0|<=C/N uniformly. For sufficiently largeN, w_N=w_0+v_N remains negative in(0,L). It has the same endpoint values and derivatives, the same analytic center germ, and the same source germ as w_0. Its reconstructed g_N is positive and smooth atL by the formula in the next paragraph. Thus these are compatible traces in the domain ofB.

## Uniform control of the reconstructed density

Write epsilon=1/N and sigma=v_N/w_0. On(0,r_0], (3) and the fixed smooth base give

    |sigma^(i)|<=C epsilon x^(6+beta-i),  i=0,1,2.

Normalization at0 and the first axis equation give exactly

    eta=log(g_N/g_0)
       =log(1+sigma)-A int_0^x (1/w_N-1/w_0)du.

The integrand is O(epsilon u^(5+beta)); its first derivative is O(epsilon u^(4+beta)). Differentiating the displayed formula therefore proves

    |eta^(i)|<=C epsilon x^(6+beta-i), i=0,1,2.           (4)

The constants in this proof depend on the fixed base, cutoff andr_0, but never onN. On[r_0,L], w_N=w_0 and eta is constant eta(r_0)=O(epsilon). Consequently g_N=e^(eta(r_0))g_0 there, and Q_N-Q_0 together with its fixed-order derivatives is O(epsilon) on that closed tail interval. In particular Q_N(L)-Q_0(L)=O(epsilon).

## Expansion with a uniform integrable error

Put W_0=m_0^(beta-2)/g_0 and W_N=m_N^(beta-2)/g_N. On(0,r_0],

    W_0=A^(beta-2)x^(-beta)(1+O(x^2)), Q_0=O(x^(-5)),
    W_N-W_0=O(epsilon x^6),
    Q_N-Q_0=-v_N''/(2g_0^3)+O(epsilon x^(1+beta)).       (5)

The first line follows from the base Taylor expansions. For the second line, m_N/m_0=(1+sigma)e^(-eta), and(4) gives a relative change O(epsilon x^(6+beta)) inW. For the last line use Q=(g'-w'')/(2g^3): the change ofg' is O(epsilon x^(7+beta)), division byg_0^3 costsx^(-6), and the relative change ofg^(-3) times the base numerator O(x) has the same bound. Its product withv_N'' has size O(epsilon^2 x^(5+2beta)), which is also bounded byC epsilon x^(1+beta) after increasing a fixed constant.

Substitute(5) into the difference of the integrands in(2). The result is

    [Q_N-Q_N(L)]W_N-[Q_0-Q_0(L)]W_0
       =-(A^(beta-2)/2)v_N'' x^(-6-beta)+E_N(x),
    |E_N(x)|<=C epsilon (x+x^(-beta)),  0<x<=r_0.        (6)

To account for all terms: the lower term in deltaQ timesW_0 is O(epsilon x); (Q_0-Q_0(L))deltaW is O(epsilon x); the change ofQ(L) timesW_N is O(epsilon x^(-beta)); replacingg_0^(-3)W_0 by A^(beta-2)x^(-6-beta) costs O(epsilon x); the remaining product of changes is bounded by these quantities. Sincebeta<1 the error is integrable with integral O(epsilon), uniformly inN.

On[r_0,L], the tail relations in(4) give an integrand difference bounded byC epsilon (L-x)^(beta-1) nearL and byC epsilon elsewhere. Its integral is also O(epsilon). Each difference in(6) is integrable at0: below the support ofv_N, only the Q(L) subtraction changes, by an integrable multiple ofx^(-beta). Thus the difference of the finite parts equals the ordinary integral of their difference. Formula(2) yields

    B[w_N]-B[w_0]
       =(1-beta)/(6A) int_0^r_0 v_N'' x^(-6-beta)dx+O(1/N).

Twice integrating by parts, with zero boundary terms becausev_N is compactly supported away from both endpoints, gives

    int v_N''x^(-6-beta)dx
       =(6+beta)(7+beta) int v_N x^(-8-beta)dx.

Finally,

    int v_N x^(-8-beta)dx
       =N^(-1)int_0^(N+2) chi(t)chi(N+2-t)dt
       =1+(2/N)int_0^1 chi(t)dt.

The middle plateau has lengthN, while each end contributes the same fixed integral. This proves(1), including its nonzero sign.

## Dependencies and scope

The proof uses only the exact axis equations, ordinary differential equations on intervals, the stated normalized finite part, smooth cutoff functions, elementary estimates and integrations by parts with justified endpoint terms. It does not use a numerical response limit. Any later calculation checks formulas or illustrates the limit; it is not the proof.

This establishes discontinuity in the explicitly stated critical weighted supremum norm. It neither changes the above-critical continuity theorem nor asserts a coupled realization of any perturbation. It does not place numerical data in a norm ball, determine a family of PDE profiles, or reach a strong-setting endpoint. It also does not retroactively make a single-bump computation a critical-norm proof.
