# A geometric density bound forces a geometric stream bound on the generated sequence

Status: PROVED after the theory part's independent reviews at2026-10-31T07:31Z and07:33Z and verifier closure V178. An all-order geometric bound for the computed rational sequence remains open.

## Exact statement

Let delta=a/b be reduced in(0,1), c=(1-delta)^(-1), q_0=2b/gcd(a,2), and let

    f_1(theta)=sum_(1<=k<=L, k odd) a_k sin(k theta), a_L!=0,

be a nonzero real finite S1 profile. Use the canonical polynomial-log stationary recursion, with resonant stream constants zero. Write p_n=1-n delta, P_n=2-n delta and

    M_n=sum_(q,m)|[t^q sin(m theta)]F_n|,
    N_n=sum_(q,m)|[t^q sin(m theta)]G_n|.

If M_n<=C A^n for all n>=1 and some C,A>0, then N_n<=H B^n for all n>=1 and some H,B>0. Together with topic93, geometric growth of the density norms, geometric growth of the stream norms, and convergence of all three fields on a sufficiently distant exterior are therefore equivalent for this generated sequence.

This implication uses the stationary equation at the next order. It is not a bound for the Poisson inverse on arbitrary admissible inputs. The general-input counterexamples in topics28,89,92 remain valid.

## An angular weight exposing the highest leading harmonic

Choose a fixed real rho>=4 so that

    S=sum_(k<L)|a_k|rho^k/(|a_L|rho^L)<=1/16.       (1)

Such a rho exists because there are finitely many lower frequencies. For example it suffices that rho>=4 and rho^2>=16 sum_(k<L)|a_k|/|a_L|, since distinct S1 frequencies differ by at least two. Put

    T=|a_L|rho^L/2,  r=rho^(-2)<=1/16.

For sine or cosine polynomials with log-polynomial coefficients define

    ||H||_rho=sum_(q,m)|h_(q,m)|rho^m,

where m>=0 and the constant cosine mode uses weight one. This is the weighted angular Fourier Wiener norm combined with the plain log-coefficient norm. Products are submultiplicative, because rho^|m+l|<=rho^|m|rho^|l|. The canonical frequency bound m<=(L+1)n implies

    M_n <= ||F_n||_rho <= rho^((L+1)n) M_n.        (2)

Thus geometric growth in the unweighted density norm gives geometric growth in this fixed weighted density norm. The same equivalence holds for stream norms once either bound is established.

## Coercivity of the leading-profile transport term

Let i delta>=16 and let G be any finite even-frequency sine polynomial, with log degree at most i/q_0. Set

    a=i delta-2>0, p=1-delta>0, D=partial_t,
    L_i G=(-a+D)G f_1' - p f_1 partial_theta G.    (3)

Then

    ||L_i G||_rho >= T L delta i/8 ||G||_rho.      (4)

Here the symbol L_i denotes this transport operator, not the highest frequency L.

To prove(4), first ignore D and retain only the top harmonic a_L sin(L theta). For a coefficient g_(q,m), m>=2 even, the upper-frequency contribution is

    -a_L(La+pm)g_(q,m) t^q sin((m+L)theta)/2.

The map(q,m) to(q,m+L) is injective, so its weighted norm is exactly

    T [La||G||_rho+p||partial_theta G||_rho].       (5)

The lower-frequency contribution has coefficient a_L(-La+pm)g_(q,m)/2 at signed frequency m-L. Its norm is at most r times(5): the coefficient modulus is at most |a_L|(La+pm)|g|/2 and

    rho^|m-L| / rho^(m+L)=rho^(-2 min(m,L))<=r.

This remains true when lower-frequency contributions overlap or when m-L is negative, because the triangle inequality only enlarges their norm.

For each lower leading harmonic k<L, both branches together have norm at most

    |a_k|rho^k(1+r)/2 [La||G||_rho+p||partial_theta G||_rho],

since k<=L and m>=2,k>=1. Summing them and using the reverse triangle inequality gives

    ||-aG f_1'-p f_1 partial_theta G||_rho
       >=T c_0 [La||G||_rho+p||partial_theta G||_rho],
    c_0=1-r-(1+r)S >=223/256.                    (6)

The remaining term is D G f_1'. If K=deg_t G, then ||DG||_rho<=K||G||_rho. The same upper/lower branch estimates, now with no angular derivative of G, give

    ||DG f_1'||_rho <=T d_0 L K||G||_rho,
    d_0=(1+r)(1+S)<=289/256.                     (7)

Discard the nonnegative angular-derivative term in(6). Since K<=i/q_0<=delta i/2, (6)-(7) imply

    ||L_iG||_rho
       >=T L [223(delta i-2)/256-289 delta i/512]||G||_rho
       =T L [157 delta i/512-223/128]||G||_rho.

For delta i>=16 this bracket is at least delta i/8: their difference is93 delta i/512-223/128, which is positive already at16. This proves(4). In particular, no inverse for the Poisson equation is used.

## Isolating G_i in the next stationary equation

Put X_n=||F_n||_rho and Y_n=||G_n||_rho. The density equation at n=i+1 reads

    (lambda_(i+1)-cD)F_(i+1)
      = L_iG_i + sum_(k+j=i+1, k<i)
          [(P_k+D)G_k partial_theta F_j
                 -partial_theta G_k(p_j+D)F_j],
    lambda_(i+1)=c delta i.                      (8)

The summand k=i,j=1 is exactly(3), since F_1=f_1 has no log terms and p_1=p. Every other stream index is smaller than i.

Let C_0=3-delta+2/q_0 and E=(L+1)C_0. The weighted algebra property and the canonical linear degree and frequency bounds give the same estimate as topic88,

    ||the (k,j) summand||_rho <= E k j Y_k X_j.   (9)

Also deg F_(i+1)<=(i+1)/q_0<=delta(i+1)/2, so

    ||(lambda_(i+1)-cD)F_(i+1)||_rho
       <=2c delta i X_(i+1), i>=1.              (10)

Define

    alpha=8/(T L delta), U=2 alpha c delta,
    V=alpha E, i_0=ceil(16/delta).

From(4),(8)-(10), for i>=i_0,

    Y_i <= U X_(i+1)
             +V sum_(k+j=i+1,k<i) j Y_k X_j,    (11)

where k/i<=1 was discarded. This is a linear renewal inequality in the unknown stream norms.

## A geometric majorant

Under the hypothesis of the theorem, let

    A_*=max(1,A rho^(L+1)),  K_*=V C A_*.

Equation(2) gives X_j<=C A_*^j. Choose H_* large enough that

    H_*>=U C A_*,
    H_*>=max_(1<=i<i_0) Y_i/A_*^i.

The maximum is over finitely many already defined polynomial coefficients. For every i>=1, including the finitely many early indices by this choice,

    Y_i <= H_* A_*^i
              +K_* sum_(l=1)^(i-1)(l+1)A_*^l Y_(i-l).       (12)

Take B=A_* max(4,8K_*) and y=A_*/B. Then0<y<=1/4 and

    K_* sum_(l>=1)(l+1)y^l
      =K_* y(2-y)/(1-y)^2 <=4K_*y<=1/2.

Induction in(12) now gives

    Y_i<=2H_* B^i,

because the forcing term is at most H_*B^i and the convolution term is at most H_*B^i. Since N_i<=Y_i, this proves the claimed geometric stream bound. Topic93 and its common-potential reconstruction then give the exterior solution.

## Dependencies, scope and remaining open step

The input facts are the exact stationary recurrence, finite support m<=(L+1)n, and canonical log degrees at most n/q_0, with delta q_0>=2. They are established in topics01,17,88. The reverse implication and exterior reconstruction are in topics93 and41. All additional inequalities and constants are proved above.

The argument does not show that M_n is geometric. It only makes that condition sufficient on the actual generated stationary sequence. It also does not bound the Poisson map on arbitrary inputs, does not prove that N_n/M_n is uniformly bounded, and does not justify the heuristic feedback cap from finite data. The angular weight can enlarge the resulting exponential base substantially.

## Finite exact verification

The independent signed-Laurent implementation in `../../code/transport_coercivity_exact.py` checks320 exact rational cases at the parameters2/3,4/9,2/5,3/7,5/8. Four finite profiles include mixed signs and a small top coefficient; four orders and four input patterns per parameter/profile cover basis and seeded mixed polynomials. Every tested output has the required sine symmetry and satisfies(4). Exact ratios are retained in `verification/exact_laurent_checks.json`. These checks support implementation consistency; they do not replace the proof or its independent review.
