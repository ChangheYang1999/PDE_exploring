# The circulation resolvent is not differentiable at the center

Status: CONFIRMED. This independently verifies the nondifferentiability observation in lead astra/auditH/answer.md and gives its precise one-sided exponent. It is a property of an auxiliary integral, not a loss of smoothness of the physical fields.

## Statement

Assume the complete smooth B2 flow W with beta>=2, vertical-axis invariance, W(0)=0, DW(0)=diag((beta-2)/2,mu), mu=1+3beta/2, and U-U(0)=o(r). Define the continuous auxiliary function from research/17 by

    H(X)=int_0^infinity e^(-(beta+1)t) (phi_t X)_2 dt.

Put lambda=beta+1 and q=lambda/mu, so 2/3<q<=3/4<1. There are constants C_plus,C_minus>0 such that, as b decreases to0,

    H(0,b)=C_plus b^q - b/(mu-lambda)+O(b^(q+1)),
    H(0,-b)=-C_minus b^q + b/(mu-lambda)+O(b^(q+1)).

In particular H is not locally Lipschitz and has no finite vertical derivative at the origin. Smoothness of W does not justify differentiating the defining improper integral there. The constants depend on the global axis flow.

## Proof

Write w(y)=W2(0,y). Axis invariance gives the scalar equation y'=w(y), with w(y)=mu y+O(y^2). Fix b1>0 small enough that w>0 on (0,b1]. Define the smooth local linearizing coordinate

    zeta(y)=y exp[int_0^y (mu/w(s)-1/s) ds].

The integrand has a smooth extension at zero: w(s)=s a(s), a(0)=mu, so (mu/w(s)-1/s)=(mu-a(s))/(s a(s)). Hence zeta=y+O(y^2), zeta'(0)=1, and w zeta'=mu zeta. Restrict b1 further so zeta'>0. The travel time from b to z, with 0<b<=z<=b1, is

    t(b,z)=mu^(-1)log[zeta(z)/zeta(b)].

Split the integral defining H at the first time the axis orbit reaches b1, and change variables from time to position on the initial segment. The exact identity is

    H(0,b)=zeta(b)^q [ H(0,b1)/zeta(b1)^q
                         +int_b^b1 zeta(z)^(-q) z/w(z) dz ].     (1)

The coefficient obtained by replacing the lower integration limit b by0 is finite, since the integrand is mu^(-1)z^(-q)(1+O(z)) and q<1. It is strictly positive: positive axis trajectories never hit zero in finite time, so H(0,b1)>0, and the integral is positive. Call that coefficient C_plus. The omitted small interval satisfies

    zeta(b)^q int_0^b zeta(z)^(-q) z/w(z) dz
       = b/[mu(1-q)]+O(b^2).

Also zeta(b)^q=b^q+O(b^(q+1)). Substitution into(1), and mu(1-q)=mu-lambda, proves the first expansion; the O(b^2) term is absorbed by O(b^(q+1)). The second follows by applying the same proof to the positive coordinate b=-y and the smooth scalar velocity -w(-b). Its auxiliary integral is -H(0,-b), so its positive coefficient is C_minus.

Continuity and finiteness of H on compact sets use only the growth estimate from research/17: for any eta in(0,1), |phi_t X|<=C_K e^((beta+eta)t), whose product with e^(-(beta+1)t) is integrable uniformly on K. Thus the splitting and improper integral above are justified. The leading terms imply H(0,b)/b tends to positive infinity from either side, proving nondifferentiability.

For a shorter independent check of the same conclusion, positivity and the variational identity d_b(phi_t(0,b))_2 at b0 = e^(mu t) allow Fatou's lemma:

    liminf_(b down to0) H(0,b)/b
       >=int_0^infinity e^((mu-lambda)t)dt=infinity.

## Scope

The original fields U,Omega,Theta remain assumed smooth. H combines arbitrarily long forward flow times; its center singularity does not contradict that smoothness. Circulation proofs in research/17 and18 used only continuity, so remain valid. Any pointwise formula involving grad H must be restricted to a region where that derivative has separately been justified, such as the escaping set under a suitable variational-flow hypothesis. No assertion of grad H at the center is permissible.

Dependencies: research/17's flow bound and definition of H, the B2 center eigenvalue, smooth division, one-dimensional separation of variables, and optional Fatou's lemma. No computation is used as proof.
