Prepared 2026-10-22T09:26:47.014948+00:00, before controls.

# Exact formal factorization at the simple endpoint

## Statement
Work over the real formal power-series ring R[[r,s]], where r and s are algebraically independent. Let V be the derivation

    V = r A(r,s) partial_r + P(r,s) partial_s,
    A(0,0)=10,    P(r,s)=k r-s+terms of total degree at least 2.

Here k is real. Suppose a nonzero formal first integral Theta=r F belongs to r R[[r,s]], satisfies V Theta=0, and

    F(0,s)=(C/2)s^10+terms of order at least 11,    C!=0.

Then there is a unique formal series h(r) with h(0)=0 such that the graph s=h(r) is invariant: P(r,h)=r A(r,h) h'(r). Its linear coefficient is k/11. There is a unique Z(r,s) with linear part s-(k/11)r and

    Theta=(C/2) r Z(r,s)^10.

Moreover V Z=-(A/10)Z. On setting r=x^2, the formal vector field W=(x A(x^2,s)/2, P(x^2,s)) has the odd-in-x first integral I(x,s)=x Z(x^2,s)^5, and

    W I=0,    Theta(x^2,s)=(C/2) I(x,s)^2.

Uniqueness of Z means uniqueness among formal series with the stated linear part. No convergence or actual invariant graph is asserted.

## Proof of the invariant formal graph
Write h(r)=sum_(m>=1) h_m r^m. In P(r,h)-r A(r,h)h', the coefficient of r is k-11h_1, so h_1=k/11. For m>=2 the coefficient involving the new unknown h_m is -(10m+1)h_m. Indeed, the linear term -s contributes -h_m and the constant part 10 of A contributes -10m h_m. Every nonlinear term of P and every term of A-10 has total degree at least 2 and 1, respectively; after s=h(r), its degree-m coefficient depends only on h_j with j<m. The nonzero denominator 10m+1 therefore determines h_m uniquely from earlier coefficients. This recursive coefficient argument constructs a formal series, and each coefficient uses only finitely many input coefficients. It proves existence and uniqueness without a convergence claim.

## Divisibility of the temperature
Use the invertible formal coordinate q=s-h(r). In these coordinates V=r a(r,q) partial_r+q d(r,q) partial_q, where a(r,q)=A(r,q+h(r)), a(0,0)=10 and d(0,0)=-1. The factor q divides its q component because this component vanishes when q=0 by the graph equation. The formal inverse of this change is s=q+h(r). Write Theta=r f(r,q). Dividing its invariance equation by r in the integral domain R[[r,q]] gives

    r a partial_r f + q d partial_q f + a f=0.

Expand f=sum_(j>=0) f_j(r)q^j. Suppose inductively f_0,...,f_(j-1) vanish. Then its q^j equation is

    r a(r,0) f_j'(r) + [a(r,0)+j d(r,0)] f_j(r)=0.

If f_j were nonzero and its lowest r power were r^m, the coefficient of that power would be (10m+10-j) times its nonzero leading coefficient. For 0<=j<10 and m>=0 this factor is positive and cannot vanish. Starting at j=0 proves f_0=...=f_9=0. Thus f=q^10 K(r,q). Since h(0)=0, the hypothesis on F(0,s) gives K(0,0)=C/2. Consequently U=2K/C is a formal unit with constant 1.

The binomial series L=U^(1/10)=sum_(n>=0) binomial(1/10,n)(U-1)^n is well defined in the maximal-ideal topology: each coefficient involves finitely many terms. It has constant 1 and L^10=U. Such a root is unique, since if L_1/L_2=1+H with H nonzero of smallest positive degree d, the degree-d term of (1+H)^10-1 is 10H_[d], nonzero. Put Z=q L, and substitute q=s-h(r). This proves Theta=(C/2)r Z^10 with the required linear part. If Z_1 and Z_2 had that same linear part and the same tenth power, then in the fraction field their quotient has tenth power 1. Factoring a^10-b^10 over C shows Z_1=zeta Z_2 for a tenth root of unity zeta; their common nonzero linear part forces zeta=1. The real-series uniqueness follows.

Differentiating the factorization and using V r=r A gives

    0=(C/2)r Z^9 [A Z+10 V Z].

The ring is an integral domain and the displayed nonconstant factors are nonzero, so V Z=-A Z/10. Under r=x^2, W x=x A/2 and WZ=VZ. The product rule gives W(xZ^5)=xZ^5(A/2-5A/10)=0. This proves the last assertions without taking a square root of C. The parity follows because Z(x^2,s) is even in x.

## Boussinesq application and dependencies
P321 supplies a formal hierarchy for Ck!=0. Its realness for real C,k follows from the construction below. P326 supplies a common complex s disk for individual coefficients as context only. Its beta=2 thermal equation is V Theta=0, with

    A=2[4+B'(s)+sum_(j>=1) v_j'(s)r^j/(2j+1)],
    P=-B(s)-sum_(j>=1) v_j(s)r^j,
    B=s+k s^2-(Ck/260)s^13,    v_1(0)=-k.

Thus A(0)=10, P=k r-s+O((r,s)^2), and theta_1=(C/2)t(s) with t=s^10(1+O(s)) gives the required axis condition. Every coefficient has a Taylor series in s, so these define elements of R[[r,s]]. The theorem applies. P328's leading polynomial is recovered immediately, but the present result supplies an exact factorization in the formal ring, a strictly stronger statement in the formal ring, still local. The proof uses no vorticity or curl equation except through the existence of the formal hierarchy.

## Explicit match to the P321 hierarchy
The dependency is P321 PROOF.md, whose displayed coefficient convention is

    W1=(4+B')x+sum_(j>=1) v_j' x^(2j+1)/(2j+1),
    W2=B+sum_(j>=1) v_j x^(2j),    partial_y=-partial_s,
    Theta=sum_(l>=1) theta_l x^(2l),
    theta1=Ct/2,    t=s^10(1+O(s)).

For a scalar G(r,s) pulled back by r=x^2 and s=y_*-y, the physical derivative W1 partial_x+W2 partial_y becomes (2x W1) partial_r-W2 partial_s. Its two components are exactly rA and P displayed above. Expanding VTheta=0 at r^l gives

    B theta_l' - [8l+2lB']theta_l
      =sum_(a=1)^(l-1) [2(l-a)v_a' theta_(l-a)/(2a+1)-v_a theta_(l-a)'],

which is precisely P321's displayed thermal recurrence, with no remaining factor or sign change. PROMPT.md, equation (B2-P), states W dot grad Theta=(beta-2)Theta. At beta=2 its right side vanishes, so the displayed chain rule identifies precisely that local formal thermal equation. Its identification with the physical B2-P field beta X+U-U(0) is conditional on that field having the displayed P321 components. This application concerns the coefficient field just displayed; it does not identify any globally defined velocity with the canonical full-plane inverse or assert an actual B2 profile. The sum starts at l=1, hence Theta=rF, and F(0,s)=theta1(s). Finally P321 gives omega0=eta=Y(H-CJ), Y of order 6 and J of order 4. Thus eta(0)=0, and its Poisson recurrence gives v1(0)=-(eta(0)+B''(0))/2=-k. These facts give both linear coefficients needed here.

Take C and k real with Ck nonzero. P321's construction then has real germs: B, H=-k^7/231 and the normalized scalar units t,Y,J have real coefficients; the initial scalar equations have real coefficients and admit real normalized particular germs. At each later step, real prior germs give real forcing and real compatibility residues. The displayed real triangular matrix has nonzero determinant, so its unique E,F are real. Choose a real normalized particular representative of each compatible scalar equation, for example by setting its free homogeneous coefficient to zero before the next tuning step. The subsequent compatibility solve selects the real homogeneous constants; arbitrary final choices are not asserted to satisfy later compatibility equations. Integration and differentiation preserve real Taylor coefficients, so induction proves the required realness for every germ. This is a consequence of the explicit construction, not an additional attribution to the wording of P321. Taylor expansion at s=0 is an injective ring map from these germs into R[[s]], commutes with partial_s and with all finite sums and products, and each r coefficient of the displayed equations uses only finitely many transverse indices. Consequently it produces the required identity in R[[r,s]]. A common disk is not required for this step; P326 provides one but no estimate in the transverse index. Thus the present theorem needs only P321's coefficientwise analytic germ assertion and displayed base data. The source hashes and exact coefficient matches are recorded with the controls. No finite-jet computation is being used to infer the existence of the hierarchy.

## Scope and finite verification
The graph h, factor Z and first integral I are formal series only. This is not an actual separatrix, an analytic square-root theorem for an unknown two-dimensional solution, a convergence assertion, a sign theorem for an unevaluated formal series, or a B2 profile. General B2 remains OPEN. The independent sparse bivariate evaluator constructs graph coefficients and tests divisibility and the tenth root using exact rational arithmetic on P324 stated-exact jets, within explicit source coverage. Its thermal, factorization and manufactured transport residuals are consistency tests of assembly, coordinate change and truncation, not independent confirmation of the physical equations. Simple negative examples are smoke tests. Further controls perturb a deep temperature coefficient, a velocity coefficient and a thermal weight; compare recovered C,k with declared parameters and B; and compare two truncation rectangles from distinct P324 runs at the same parameters. The deep temperature perturbation is detectable through graph mixing for the tested k!=0. The proof above establishes the all-order statement; no finite control does so. P326 is context only, not a dependency of this theorem.

No JavaScript/TypeScript, servers/listeners, RLScience cluster, Lean/Lake builds or external posts. Write only in verification.
