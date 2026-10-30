# Joint origin and far-field inverse floors

This is an independent audit of the T2 theory worker's review of T4-146, Remark R1. The conclusion is a necessary scalar condition on a registered closure scheme. It does not assert that a residual below the ceiling closes the scheme.

## Exact statement

Let 1<c<2, 0<a<1+1/c, d=c-1 and b=1+c-ca>0. For 0<s<d set

    C1(s)=(4pi s(1+s))^(-1/2).

Suppose real numbers eta>=0, R>0, M>0, C_U>=1 and beta>0 satisfy

    M eta <= R,
    (C_U+a) C1(s) R < beta <= b,
    M >= max(1/(d-s),1/b).                              (1)

Then

    eta < b/(1+a) J(d,b),                               (2)

where

    s_star=(2d-3+sqrt((2d-3)^2+16d))/8,
    H(d)=(d-s_star)sqrt(4pi s_star(1+s_star)),

and

    J(d,b)=H(d),                         if b>=d-s_star,
    J(d,b)=b sqrt(4pi(d-b)(1+d-b)),       if 0<b<d-s_star. (3)

In particular this ceiling is no larger than either separate ceiling

    b H(d)/(1+a),   sqrt(8pi) b^2/(1+a).                 (4)

For fixed c, the second branch starts at a=(2+s_star)/c. As a tends to 1+1/c from below, the ratio of (2)'s right side to the second expression in (4) tends to sqrt(c(c-1)/2).

## Proof

From the strict second inequality of (1), C_U>=1 and beta<=b,

    eta <= R/M < b/((1+a)C1(s)M)
       <= b/(1+a) min(d-s,b) sqrt(4pi s(1+s)).           (5)

Define f(s)=(d-s)sqrt(4pi s(1+s)). Its square has derivative

    4pi(d-s)[-4s^2+(2d-3)s+d].

The quadratic has one positive root s_star and one negative root, with 0<s_star<d. Thus f strictly increases up to s_star and decreases afterwards. It vanishes at both endpoints.

If b>=d-s_star, then min(d-s,b)sqrt(4pi s(1+s)) is at most f(s), and equality holds at s_star. Its maximum is H(d).

If 0<b<d-s_star, put s0=d-b>s_star. On (0,s0), the expression equals b sqrt(4pi s(1+s)), which is strictly increasing. On (s0,d), it equals f(s), which is strictly decreasing because s0>s_star. Its maximum is therefore at s0 and is b sqrt(4pi(d-b)(1+d-b)). This proves (2)-(3), including equality at the branch boundary.

The first comparison in (4) follows from min(d-s,b)<=d-s. For the second, use min(d-s,b)<=b and s<d<1, so sqrt(4pi s(1+s))<sqrt(8pi). Solving b=d-s_star gives a=(2+s_star)/c. On the second branch the ratio to sqrt(8pi)b^2/(1+a) is exactly

    sqrt((d-b)(1+d-b)/2).

As b decreases to0, this tends to sqrt(d(1+d)/2)=sqrt(c(c-1)/2).

## Application and scope

For the registered FW-T-DYADIC-Y-v1 framework, eta is exactly its forcing norm Y_(a,s,Rw)(F); R is the same norm's correction radius; C_U is its low velocity multiplier constant; and M is its high inverse bound. The existing audited origin theorem supplies s<d and M>=1/(d-s), under its exact normalized-origin and coefficient assumptions. The audited far-field theorem supplies M>=1/b and beta<=b, under its far-field, domain and input-range assumptions. The framework's contraction inequalities supply the remaining parts of (1).

Consequently (2) applies only when both audited inverse-floor hypotheses apply to the same realization and norm. No norm is changed in taking the maximum of the floors. The low-weight radius Rw remains any fixed positive number allowed by those hypotheses.

The exact candidate007 was already excluded throughout the registered parameter range by the simpler origin ceiling. This sharper joint ceiling changes no current closure verdict. T2's displayed decimal table is labelled FLOAT and is not certified by this analytic audit; the formula itself is independently confirmed here.

Dependencies: the scalar inequalities (1), elementary differentiation, and, for the stated application only, T4-097, T4-146 and the registered dyadic closure conditions. No numerical computation is used.
