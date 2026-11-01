# The sharp factorial scale for a uniform canonical Poisson bound

Status: PROVED. Independent theory-part review at 2026-10-31T07:00Z confirmed the complete argument; closure recorded in V162. This is a statement about all admissible polynomial inputs, not the generated nonlinear sequence.

## Statement

Let delta=a/b be reduced, with 0<a<b, and put g=gcd(a,2), mu_*=g/b and P_n=2-n delta. At order n, let F be any odd sine polynomial in theta with polynomial coefficients in t. Let T_n F be its polynomial stream obtained from the factored Poisson inverse, setting the constant of every resonant stream mode to zero. The input space may be restricted to the support |m|<=2n-1 and the degree bound

    deg_t F <= max(0,floor((n-1)/q_0)-epsilon),
    q_0=2b/g, epsilon=1 if a/g=1 and epsilon=0 otherwise.

All conclusions below still hold under that restriction. For s>0, define

    ||H||_{!,s} = sum_q q! s^q ||[t^q]H||_{l1}.

There is a constant C independent of n and the polynomial input such that

    ||T_n F||_{!,s} <= C ||F||_{!,s}

if and only if s>b/g. For s>b/g, one may take

    C = max{s, 1/(g/b-1/s)}.                         (1)

More generally, if positive weights omega_q, independent of n and angular frequency, give a uniform Poisson bound C in the norm sum_q omega_q ||[t^q]H||_{l1}, then

    omega_k >= omega_0 k! / (2C mu_*^(k+1))          (2)

for every k>=0.

At delta=2/3, the norm with weights q!2^q has the uniform bound C=6. The stationary density inverse is also bounded in this norm: for n>=2,

    ||(2(n-1)-3D)^(-1)|| <= 1/(2(n-1)-3/2) <= 2,

where D=partial_t. Thus it is false that every common column norm with uniformly bounded linear inverse steps must dominate q!b^q. In this example b=3 and 2^q/3^q tends to zero. The correct necessary geometric scale is b/g, here3/2.

## Poisson factors and their arithmetic

Write the input as sum_j A_j(t) sin((2j+1)theta) and the stream as sum_(j>=1) B_j(t) sin(2j theta). At m=2j the nonresonant formula is

    B_j = -1/2 (D+P_n+m)^(-1) A_(j-1)
          -1/2 (D+P_n-m)^(-1) A_j.                 (3)

The shifts have the form (2bk-an)/b, so every nonzero shift has magnitude at least g/b. Conversely, the congruence an=-g mod2b is solvable because gcd(a,2b)=g. It has arbitrarily large positive solutions n. For each such n, put m=(an+g)/b-2. Then m is an even positive integer for all sufficiently large n, and

    P_n+m=mu_*.

Also m-1<=2n-1. The allowed input degree tends to infinity along this progression. Hence for every k we can choose an admissible order and the single input F=t^k sin((m-1)theta) at the fixed shift mu_*.

## Sufficient bound and resonant constants

In the factorial norm, ||D||<=1/s. If v is a nonzero shift and s>1/mu_*, its finite polynomial inverse obeys

    ||(D+v)^(-1)|| <= 1/(|v|-1/s)
                       <= 1/(mu_*-1/s).

A zero shift uses integration from zero, whose norm is exactly s. If the stream output is resonant, deleting its constant is a contraction in the coefficient norm. In particular this operation does not require a factor2 estimate from the triangle inequality.

Each input sine coefficient enters at most two outputs in(3), each with a factor1/2. Applying the bounds above to these two channels and summing over input coefficients proves(1), including the resonant modes and their canonical constants. The missing frequency-zero stream output can only reduce the norm.

For delta2/3 and s2, mu_*=2/3 and the bound is max(2,6)=6. The stationary inverse estimate follows from ||3D||<=3/2 and its finite Neumann series, proving the stated counterexample to the scale b.

## Necessary bound and the endpoint scale

Use the admissible input constructed in the arithmetic step. Its contribution to the output at m is exactly

    -1/2 (D+mu_*)^(-1)t^k
    = -1/2 sum_(h=0)^k (-1)^h k! t^(k-h)
                         / ((k-h)! mu_*^(h+1)).    (4)

There is no other input in this output mode, and this mode is nonresonant. Its constant coefficient has absolute value k!/(2mu_*^(k+1)). Comparing that coefficient alone with the input norm omega_k proves(2).

For the special weights omega_q=q!s^q, retaining every coefficient of(4) gives the stronger lower bound

    ||T_n F||_{!,s}/||F||_{!,s}
       >= 1/(2mu_*) sum_(h=0)^k (mu_*s)^(-h).       (5)

This diverges with k when mu_*s<1, and equals(k+1)/(2mu_*) when mu_*s=1. Hence the uniform bound fails also at the endpoint s=b/g. Together with(1), this proves the sharp threshold.

## Scope and dependencies

The factored inverse and canonical convention are derived in topics10 and17. The only arithmetic input is the elementary linear congruence above. The proof makes no assertion about the size of the actual nonlinear inputs, or about convergence or divergence of their far-field series. A bound verified only on that generated sequence can be much better than the operator bound on all admissible inputs.

This corrects the scale sigma>=b stated in version14, Section14.15(d), of the theory part's theory report. Its scalar inverse formula is valid; the passage from the rational shift to the scale b omitted gcd(a,2).
