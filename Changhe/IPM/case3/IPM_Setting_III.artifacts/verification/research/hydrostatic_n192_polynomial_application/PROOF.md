# Exact polynomial-axis application to the N192 auxiliary state

Written before the checker on 2026-10-21. This is Result279. It concerns the saved positive epsilon=0 hydrostatic trial, not the full-plane IPM inverse.

## Statement

For the frozen checkpoint hsG_c2.0_N192_log.pt with SHA256 5177b5ae4c8a480353f7d855e27cfb735accab264c56f53c1f54881476d737a0, take the exact binary coefficients as rational numbers. Use the independent polynomial reconstruction and complete axis primitive from Result265. With the compact coordinate w, the axis radius and density are

    y=C sqrt(1-w) w^(-P),  G(y)=y H(w),  0<w<1,
    C=L/2^P=1/4,  P=2,  V'(y)=k(w(y)).

Here V=V_2(0,y) is the canonical positive epsilon=0 inverse on the axis. The requested exact input facts are H(0)=k(0)=0, H'(0)!=0, deg H=deg k=193=N+1, P=2 and C>0. The checker establishes these facts from the rational data, with the complete Result265 input/result/code hash chain. Subject to those exact facts, the transport identity (c y+V)G'=G cannot hold on any nonempty open interval of y>0, for any constant c. In particular this state is not an exact auxiliary solution. The degree19 extension is not used.

## Polynomial axis primitive and gauge

To distinguish two coordinates, write q=1-2w, s=(1+q)/2=1-w and Q_0=w+2P s. The finite density is g(x,y)=y w sum_{j=0}^{M-1} s^j beta_j(q) cos(2j theta), with real polynomial beta_j. On the positive vertical axis,

    H(w)=w sum_j (-1)^j (1-w)^j beta_j(1-2w).

Let J_q=sum_{j>=1} j^2 (-1)^j Q_0 s^(j-1) beta_j(q), J(-1)=0. Then k(w)=-H(w)-J(1)+J(1-2w). Indeed, at x=0 direct polar differentiation gives g_xx=(H_logr+H_thetatheta)/y and dq/dlogr=4sw/Q_0. The angular term obeys H_thetatheta dlogr=-J_q dq. Integrating from0 to y gives integral_0^y g_xx=H(w)-a-J(q), where a=g_y(0). Since H tends to0 and J to J(1) at infinity, subtraction from the total integral yields integral_y^infinity g_xx=k(w). The tail is absolutely integrable because the finite density has p=1-1/P=1/2 and g_xx=O(y^(p-2)). Differentiating V(y)=integral_0^y t g_xx(0,t)dt+y integral_y^infinity g_xx(0,t)dt gives V'=k; its two moving-boundary terms cancel. Odd parity fixes V(0)=0. Thus no free strain or finite cutoff enters k.

The full exact coefficient reconstruction, differentiation of J, endpoint identities and independent numerical agreement were checked in Result265. This new check reuses that independently generated rational data, not producer code. It checks the old evidence hashes before extracting new facts. It does not rerun the costly exact conversion or claim that a hash alone proves its mathematical correctness. The above identity and the verified Result265 reconstruction supply that dependency.

## A direct contradiction for P=2

Write H(w)=w h(w). Since H'(0)!=0, h(0)!=0. Set t=sqrt(1-w), so 0<t<1 and w=1-t². Define

    F(t)=C t h(1-t²),  D(t)=w F'(t)+2t F(t),  Q(t)=1+3t².

F is a nonzero odd polynomial of odd degree d, with F(1)=C h(0)!=0 and F(-1)=-F(1). In the current data deg H=193, so d=385. We have G=F/w, dy/dt=C Q/w³ and dG/dt=D/w²; hence G'=wD/(C Q). Also D(1)=2F(1)!=0, so D is not the zero polynomial.

Suppose the transport identity holds on a nonempty open interval. Shrink the interval so D has no zero there. Solving for V gives V=Cw^(-2) A, where A=FQ/D-c t is rational. Using V'=k and differentiating with respect to t gives the rational identity

    w A'+4t A=k(w) Q.

It is an identity over the complex rational functions because it holds on a real open interval. A cannot have a pole away from t=+1,-1: a pole of order l has a nonzero derivative term of order l+1 on the left. At t=1, a leading Laurent coefficient a at a pole of order l>=1 produces coefficient 2(l+2)a at order -l. At t=-1 it produces -2(l+2)a. These are nonzero, whereas the right side is polynomial. Thus A has no finite poles and is polynomial. Consequently D divides FQ.

Let J be the monic gcd of F and D, and let s_F be the number of distinct complex roots of F. At any root alpha of F of multiplicity mu, w(alpha)!=0 because F(+-1)!=0. Thus D has multiplicity exactly mu-1 there. Hence J=gcd(F,F'), deg J=d-s_F, and F/J is coprime to D/J. It follows that D/J divides Q.

Because d is odd, d!=2, and the leading coefficient of D is (2-d) times that of F. Therefore deg D=d+1, and deg(D/J)=s_F+1<=2. Since F(0)=0, s_F>=1, hence s_F=1 and F=a t^d. Then D/J is a nonzero multiple of d+(2-d)t². Its divisibility into the quadratic Q forces 2-d=3d, or d=1/2, contrary to the positive odd integer degree d. This contradiction proves the statement. No high-degree resultant, limiting argument or numerical residual is needed.

## Exact verification and scope

The new checker binds the frozen checkpoint, the exact polynomial JSON, its enclosing Result265 state and pipeline, the previously reviewed summary and the active independent code/proof bytes. It reads every rational coefficient exactly, checks reduced positive-denominator form, endpoints, the first and highest nonzero coefficients, and P,L,C. It independently composes F using binomial coefficients and checks its odd parity, degree, F(+-1), the leading and endpoint coefficients of D, and the derivative identities by exact polynomial arithmetic. Large coefficients are retained in JSON, not manually copied into a source file. A passing extraction gate is evidence for this application, not a formal proof assistant certificate.

Dependencies: Result265 in ../hydrostatic_c2_resolved_192_audit/; the axis primitive proof in ../hydrostatic_axis_primitive/PROOF.md; elementary complex polynomial factorization and rational-function pole analysis, fully used above. The obstruction concerns exact finite polynomial axis data. It supplies no uniform residual floor, excludes no infinite-resolution auxiliary limit and proves no nonexistence for the full-plane SettingIII class.
