# A nonvanishing highest-mode cascade in a formal far-field hierarchy

Written 2026-10-21 before the supporting checker. Status: a formal coefficient theorem, not an all-order asymptotic theorem for IPM solutions.

## Statement, notation, and hypotheses

Let 0 < p < 1, ell = 1/p, D = ell - 1, and let n be a positive odd integer. Put

    s_k = (k+1)p-k,             n_k = (k+1)(n+1)-1,
    k = 0,1,2,... .                                      (1)

Fix an integer J >= 1. Suppose a finite formal hierarchy has density terms
r^{s_k} Theta_k(theta), 0 <= k <= J, where every Theta_k is an odd-sine trigonometric polynomial supported on positive odd modes at most n_k. Write A_k for its sin(n_k theta) coefficient and assume A_0 = a != 0. Suppose its stream terms r^{s_i+1} Phi_i(theta), 0 <= i < J, are sine polynomials on positive even modes at most n_i+1 and satisfy the homogeneous Poisson equations

    -Delta(r^{s_i+1} Phi_i) = d_x(r^{s_i} Theta_i).         (2)

They need not be unique at lower resonant modes. At every level 1 <= k <= J assume the transport coefficient equation

    -k D Theta_k + sum_{i+j=k-1} T_{ij} = 0,              (3)
    T_{ij} = -s_j Phi_i' Theta_j + (s_i+1) Phi_i Theta_j'.

Primes here mean angular derivatives. These are precisely the corresponding formal coefficients of
(ell X+U).grad rho = rho with U=(-psi_y,psi_x).

Then all A_k are nonzero. More precisely,

    A_k = (-1)^k a^{k+1} b_k,  b_k > 0,                 (4)

where b_0 = 1. The top coefficient of Phi_i is uniquely

    phi_i = -A_i/[2(n_i+s_i+2)],                         (5)

and the top density recurrence is

    k D A_k = sum_{i+j=k-1} c_{ij} A_i A_j,
    c_{ij} = (1/4)[1 - 2(j+1)(n+1)/((i+1)(n+p)+2)].     (6)

Thus a pure-power hierarchy with the stated angular bounds cannot terminate at any finite order, or remain within a fixed finite angular space if such a hierarchy exists to all orders. These conclusions are conditional on the formal hierarchy. They do not say that every actual profile admits it.

## Proof of the modal coefficient

In polar coordinates U_r = -psi_theta/r and U_theta = psi_r. The angular source of a single density mode is

    d_x(r^s sin(m theta))
      = (r^{s-1}/2)[(s-m)sin((m+1)theta)
                            +(s+m)sin((m-1)theta)].     (7)

For the highest mode m=n_i, the top stream mode is n_i+1. Put u=i+1, B=n+p. Then

    n_i+s_i+2 = u B+2 > 0,
    n_i-s_i = u(n+2-p)-2 > 0.                          (8)

The last strict inequality follows already at u=1 from n-p>0. In particular n_i+1 > |s_i+1|, so the top stream coefficient is nonresonant at every level. Equation (2) gives

    [(n_i+1)^2-(s_i+1)^2] phi_i = (s_i-n_i) A_i/2.

Factoring the left side proves (5). Lower angular density modes cannot contribute to this stream mode. Any lower resonant homogeneous freedom allowed in (2) has no effect on (5).

For i+j=k-1, the largest possible frequency in T_{ij} is

    (n_i+1)+n_j = (k+1)(n+1)-1 = n_k.                   (9)

Only the product of the two top modes reaches it. The sine addition formulas give its coefficient as

    (A_j phi_i/2)[-(n_i+1)s_j+(s_i+1)n_j]
      = A_i A_j [(n_i+1)s_j-(s_i+1)n_j]
                          /[4(n_i+s_i+2)].             (10)

To simplify it, put v=j+1 and A=n+1. Then n_i+1=uA, n_j=vA-1 and n_j+s_j=vB. Hence the numerator in (10) is

    uA(vB) - (vA-1)(uB+2) = uB+2-2vA,

which proves c_{ij} in (6). The radial degree in this product is
s_i+s_j-1=s_k, and ell*s_k-1=-kD. This proves (3) is the correctly signed formal equation and proves recurrence (6).

## Strict negativity after pairing the interactions

The individual c_{ij} need not all be negative. Symmetrization is necessary. For u,v positive integers set S=u+v and t=uv. Here S=k+1 >= 2. From (6),

    c_{ij}+c_{ji}
       = 1/2 - (A/2)[v/(uB+2)+u/(vB+2)].              (11)

The bracket is

    [B(S^2-2t)+2S]/[B^2 t+2BS+4].                     (12)

For fixed S its derivative with respect to t is strictly negative: the numerator of that derivative is

    -2B(B^2t+2BS+4)
          -B^2[B(S^2-2t)+2S] < 0.                     (13)

Both brackets in (13) are positive for 0<t<=S^2/4. Since t<=S^2/4, expression (12) is therefore at least its value at u=v=S/2, namely

    2S/(BS+4).                                        (14)

Finally

    2AS > BS+4
       iff S(n+2-p)>4.

This is strict because S>=2, n>=1, p<1. Equations (11)-(14) show

    c_{ij}+c_{ji}<0                                   (15)

for every pair, including i=j (where the left side equals 2c_{ii}).

Assume (4) through k-1. Every product in (6), including paired ones, has the same sign factor:

    A_i A_j = (-1)^{k-1} a^{k+1} b_i b_j.

Using the symmetry b_i b_j=b_j b_i gives

    sum_{i+j=k-1} c_{ij} b_i b_j
      = (1/2) sum_{i+j=k-1}(c_{ij}+c_{ji}) b_i b_j < 0.

Division by kD>0 proves (4) at level k. The base case k=0 is the assumption. This completes the proof.

For k=1 the formula reduces to

    A_1 = a^2(p-n)/[4D(n+p+2)] != 0.                  (16)

In particular, if Theta_0 has highest mode n, its first necessary correction has highest mode 2n+1. This agrees with the two-term far-field calculation already established for exact profiles.

## Dependencies and limitations

The formal theorem above uses only polar differentiation, finite trigonometric polynomials, and the explicit equations (1)-(3). It needs neither an origin Taylor expansion nor a global inverse estimate. The reference to the first actual far-field correction uses the separately proved two-term result in ../far_field_second_term/PROOF.md, whose assumptions include the exact full-plane IPM equations and their canonical velocity.

Applying the induction to an actual profile would require a justified expansion to every needed order with the displayed angular support and with control of every additional term. The currently established two-term expansion alone does not provide this. At more negative homogeneity degrees the full-plane inverse can receive interior harmonic multipoles. Lower angular resonances can require logarithmic terms, so a pure-power hierarchy might fail to exist even though its top coefficient is never resonant. These issues have not been removed here.

Consequently this result does not yet exclude finite angular support only outside a disc, does not prove global nonexistence, and supplies no numerical candidate. An exactly finite angular density at every radius is a separate already proved restricted exclusion. The full smooth primary problem remains open.
