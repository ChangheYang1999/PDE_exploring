# Compatible tuning at a general rational exponent

Status: PROVED conditional convergence theorem, with its exact positive-response-infimum hypothesis. The theory part independently checked the full majorant and potential reconstruction at11:34Z; recorded in V299.

## Statement and hypotheses

Let h>=2and Q>2h be coprime integers. Set delta=2h/Q and c=Q/(Q-2h). Fix an even integer bandwidth B>=2and a nonzero real S1 sine polynomial f_1 supported on the positive odd frequencies below B. Define p_n=1-n delta and P_n=2-n delta. The pure formal density and stream expansions use radial powers r^(p_n)and r^(P_n), respectively, and their angular coefficients satisfy

    -[partial_theta^2+P_n^2]g_n
       =p_n cos(theta)f_n-sin(theta)f_n',
    lambda_n f_n=sum_(i+j=n) T(g_i,f_j),
    lambda_n=delta(n-1)/(1-delta),
    T(g_i,f_j)=-p_j g_i' f_j+P_i g_i f_j'.

At each stream resonance n=kQ,k>=1, delete the entire resonant output from the particular Poisson inverse. Its free coefficient H_n multiplies sin((2hk-2)theta). Assume the first compatibility coefficient

    O_Q=[sin((2h-3)theta)]f_Q

vanishes. For each k>=1let sigma_k be the Q-step response to a unit H_(kQ), measured in the density coefficient of sin((2h(k+1)-3)theta) at the next resonance. Its exact definition and limiting formula are144. Assume

    s=inf_(k>=1)|sigma_k|>0.                                  (1)

Then there is a unique compatible pure S1 density/stream formal pair in this normalization, and finite constants C,A>0such that

    ||f_n||_1+||g_n||_1 <= C A^n.

The series and every weighted derivative converge absolutely and uniformly on each sufficiently large closed exterior and give a smooth stationary self-similar IPM solution. The common potential can be chosen with the same geometric base A. For h=2it needs at most one finite logarithmic correction lambda log r at orderQ; for h>=3it is a pure angular polynomial series. Every strict radius R>A^(Q/(2h)) is sufficient for the density, stream and reconstructed potential after increasing C if necessary. Multiplying a fixed leading shape by epsilon!=0scales any sufficient radius by |epsilon|^(Q/(2h)). No global stationary continuation is claimed.

The constants can be chosen uniformly for bounded B,Q,h,||f_1||_1and1/s with the stated discrete constraints. The coefficients depend holomorphically on finite-dimensional compatible profile parameters on which these bounds hold.

## 1. Resonance, affinity and norm estimates

The resonance argument144shows that exactly n=kQ,k>=1has a positive even stream kernel. The next obstruction is affine in H_n because two H_n-dependent factors first contribute at order2n+1>n+Q. Thus H_n=-R_k/sigma_k is uniquely determined. The assumed O_Q=0handles the only obstruction without a preceding free harmonic. Induction constructs the unique compatible pure series.

Every nonzero factored Poisson denominator is an element of(2/Q)Z and has modulus at least2/Q. Consequently the full inverse, or the particular inverse deleting the whole resonant output, obeys

    ||Pi_n f||_1 <= L ||f||_1,                  L=Q/2.

The support bounds are Bn-1for density and Bnfor stream; the free frequency delta n-2lies within that support. As in131,

    ||T(g_i,f_j)||_1 <= B(3-delta) i j ||g_i||_1||f_j||_1.

Indeed |p_j|<=j and |P_i|<=(2-delta)i, and angular differentiation costs at most the support frequency. For n>=2,

    n/lambda_n <= 2(1-delta)/delta=(Q-2h)/h.

Put kappa=B(Q-2h)(3-2h/Q)/h, x_n=n||f_n||_1and eta_n=n|H_n| at resonances, zero otherwise. Then

    x_n <= kappa sum_(i+j=n)(L x_i+eta_i)x_j.                 (2)

Here eta_j=0for j<Qbut eta_Qis generally nonzero. Nevertheless x_1,...,x_Qhave no eta contribution, since each convolution has two positive indices. They are bounded by the first QCatalan coefficients

    x_j=Cat_(j-1)(kappa L)^(j-1)a^j,  1<=j<=Q,
    a=||f_1||_1.

These displayed x_jand the later x_nbelow denote scalar majorants; they need not equal the actual norms.

## 2. Lookahead and the triangular coefficient construction

Fix a true resonance n=kQand provisionally set H_n=0. Define u_(n,r)=(n+r)||f_(n+r)^(0)||_1for1<=r<Q. Every earlier harmonic has index at most n-Q, so its density partner in a product at ordern+rhas index at least Q+r. It is therefore safe to enlarge the harmonic sums to partners j>=Q+1. Separate all density-density pairs having an index below r; they are exactly the terms involving smaller provisional lookahead indices. The same two-orientation estimate as131gives

    u_(n,r) <= kappa [L sum_(i+j=n+r, i,j>=r)x_i x_j
                       +sum_(i+j=n+r, j>=Q+1)eta_i x_j
                       +2L sum_(j=1)^(r-1)x_j u_(n,r-j)],    (3)

and the next obstruction gives

    eta_n <= (kappa/s)[L sum_(i+j=n+Q, i,j>=Q)x_i x_j
                       +sum_(i+j=n+Q, j>=Q+1)eta_i x_j
                       +2L sum_(j=1)^(Q-1)x_j u_(n,Q-j)].    (4)

Impose equality as a nonnegative artificial majorant for every base index n>=Q, allowing eta at nonresonant indices as well. In(3)-(4), the restricted density indices are at most n, and the harmonic index is at most n-1. The remaining uterms have smaller r. Starting with the known x_Q, compute u_(Q,1),...,u_(Q,Q-1),eta_Q; next compute x_(Q+1)from(2), and repeat. This is a triangular scalar recursion. Induction in that order dominates the actual coefficients and lookahead blocks. In particular, the first harmonic eta_Qis included and never set to zero.

## 3. Exact generating shifts

Use the same finite polynomial P(z)=sum_(j=1)^Q x_j z^j as131, but different starting degrees for the unknowns:

    X=P+z^(Q+1)W,
    sum_(n>=Q)eta_n z^n=z^Q E,
    sum_(n>=Q)u_(n,r)z^n=z^Q V_r.

Put P_r=sum_(j=r)^Q x_j z^j and

    A_r=[P_r^2]_(>=Q+r)/z^(Q+r)
               +2z(P_r/z^r)W+z^(Q+2-r)W^2.

The notation [.]_(>=d)means deleting lower-degree terms. Direct summation of(2)-(4)now gives the polynomial system

    W=kappa L [P^2]_(>=Q+1)/z^(Q+1)
       +2kappa L P W+kappa L z^(Q+1)W^2
       +kappa E(P/z+z^Q W),

    V_r=kappa[L A_r+z^(Q+1-r)E W
                    +2L sum_(j=1)^(r-1)x_j V_(r-j)], 1<=r<Q,

    E=(kappa/s)[L A_Q+z E W
                    +2L sum_(j=1)^(Q-1)x_j V_(Q-j)].       (5)

For example, the eta product in the W equation has total starting degree Q+1, so it contributes E(P/z), not E P. In a lookahead equation the harmonic product is (z^Q E)(z^(Q+1)W), divided by z^(Q+r), giving z^(Q+1-r)E W. These shifts are the essential difference from131.

All coefficients are nonnegative. At z=0each A_r is a fixed scalar [z^(Q+r)]P_r^2; it has no W dependence. Thus V_1(0),...,V_(Q-1)(0)are determined successively, then E(0), then W(0). The only unknown in the W equation at z=0is the linear term kappa a E. Hence Phi(0,Y)=c0+JYwith Jstrictly lower triangular in the order

    V_1,...,V_(Q-1),E,W.

In particular, no nonlinear unknown term survives at z=0. The alternate split with Pof degreeQ-1would leave a quadratic constant-level term; the present split avoids it while retaining the correct eta_Q.

The implicit function theorem gives an analytic solution near z=0, because I-Jis invertible. The coefficients obey the already unique triangular scalar recurrence, so they are exactly its nonnegative majorants. Cauchy estimates prove the geometric bounds. This is an all-order argument, not an inference from a finite prefix.

The exact supersolution certificate134also applies to(5), with this ordering: T=(I-J)^(-1),Y0=T c0, G=Y0+T(Phi-c0-JY). All terms of Phi-c0-JYhave positive zdegree. Any nonnegative box b>=Y0with G(z0,b)<=b gives geometric base z0^(-1)and strict exterior radius z0^(-Q/(2h)).

## 4. Spatial convergence and parameter dependence

The Fourier support is at most Bn. An angular strip costs exp(Bn tau), and each fixed Cartesian derivative costs a polynomial in n after its natural radial weight is removed. A strict inequality A exp(B tau)R^(-delta)<1therefore gives absolute uniform convergence of every weighted derivative. All sufficiently late radial powers are negative, so their unweighted tails also converge uniformly on the same exterior. Absolute convergence justifies both the Poisson identity and all products in stationary transport.

Finite coefficients are rational functions of the leading amplitudes with fixed Poisson divisors and the nonzero responses in their denominators. Bounded input norms and response inverses give one common positive majorant. Normal convergence on a smaller parameter neighborhood then proves holomorphic dependence. Exact first compatibility remains required.

## 5. Common potential without increasing the geometric base

Write S_n=p_n+3=4-2hn/Q. For n>=4Qput x=hn/Q-1>=3and K=(Bn-2)/2. If f_n=sum_(m=0)^K a_m sin((2m+1)theta), the descending density primitive used in132is

    a_0=2x d_0+(1-x)d_1,
    a_m=(m+x)d_m+(m+1-x)d_(m+1), m>=1,
    d_(K+1)=0.

Its proof is unchanged and gives ||d||_1<=(2BQ/(3h))||f_n||_1. The Laplace multiplier is S_n^2-4m^2. A zero occurs only at n=kQ, and then m=hk-2. Pure-stream compatibility forces the corresponding d_mto vanish, exactly as in132with j=hk-1. Set that potential coefficient initially to zero.

Every other multiplier has modulus at least2h n/Q^2: its distance to an even integer is at least2/Qand |S_n|>=hn/Q. The resulting potential C_n^0obeys

    ||C_n^0||_1 <= BQ^3/(3h^2 n)||f_n||_1.

At resonance add the harmonic r^(-ell)cos(ell theta), ell=2hk-4, to match the prescribed stream. Its mixed derivative is ell(ell+1)r^(-ell-2)sin((ell+2)theta). Since ell>=hn/Qat n>=4Q, the same estimate gives

    ||C_n||_1 <= [1+(Q^2/h^2)(B+1)^2]||C_n^0||_1
                              +(Q^2/(h^2 n^2))||g_n||_1.

Thus the geometric base Ais preserved. The added degree ell is below Bn-2.

For the finite prefix, the descending primitive can fail only at x=0, meaning hn=Q. Coprimality and h>=2exclude this. The Laplace inverse can fail only at n=kQ. When hk>=3the same compatibility and harmonic correction work with x=hk-1>=2and ell=2hk-4>=2. The sole remaining case is h=2,k=1, when S_Q=0and ell=0. Compatibility forces the density sin(theta)coefficient to vanish. Pure positive even cosine potential columns match the other density modes, and lambda log r adjusts the missing resonant stream because

    Delta log r=0,
    partial_x partial_y log r=-r^(-2)sin(2theta).

No other logarithm is required. These finite inverse norms enter Cbut not A. The potential series and all weighted derivatives then converge on the same strict radius R>A^(1/delta). All potential terms have even reflection symmetry. The same argument as132shows the resulting common potential solves the original formulation. A closed Darcy one-form has zero circle period by reflection, so exterior pressure can also be chosen single valued.

## Dependencies and limitations

The independent Cartesian recurrence and resonance identities are01,119and144. The elementary scalar estimates and potential matrices are checked in131/132; the changed start indices and every generating shift are derived here. The proof requires(1). Nonzero limiting response alone does not supply it without excluding every finite response zero. No compatibility polynomial irreducibility or genericity conclusion at h>=2is assumed.

## Independent finite verification of the generating shifts

The exact equality majorant was implemented twice within the independent verification: direct ordered coefficient sums indexed by (n,r), and truncated polynomial construction of (5). For (h,Q)=(2,5),(2,7),(3,7),(3,8),(2,9),(3,13), with B=4, a=2/3 and assumed s=3/5, all six coefficient levels of every component agree exactly, totaling 330 rational coefficient identities. The affine identity at zero and strict triangularity also pass in every case. Exact boxes 2Y0 pass at z=2^(-q) with q=45,96,61,91,146,221. The evidence is verification/generating_shift_checks.json. These are checks of the stated map and certificate method; the chosen s is an assumed input and does not certify any new leading profile.
