# Constructive component bounds for an arbitrary resonance period

Status: PROVED. The independent theory-part implementation reproduced every all-k lower bound and component radius on2026-10-31T10:51Z. V277 records the review and source evidence.

## Statement and notation

Fix an integer Q>=3 and an even bandwidth B>=2. Put delta=2/Q, c=Q/(Q-2), L=Q/2, and choose kappa>=B(Q-2)(3-2/Q). Let f_1 be an S1 sine polynomial of bandwidth below B satisfying the first compatibility condition O_(2Q)=0. Assume ||f_1||_1<=a and |sigma_k(f_1)|>=s>0 at every resonance k>=2. Here sigma_k is the Q-step response to a unit free stream harmonic, as defined in130. The numbers a,kappa,s are fixed bounds, not asymptotic estimates.

Use the polynomial majorant system of131, denoted by Y=Phi(z,Y) in the order Y=(W,V_1,...,V_(Q-1),E). Its coefficients are nonnegative. Set c0=Phi(0,0) and let J be the constant matrix such that Phi(0,Y)=c0+JY. This J is nonnegative and strictly lower triangular. Define

    T=(I-J)^(-1)=I+J+...+J^Q,
    Y0=T c0,
    G(z,Y)=Y0+T[Phi(z,Y)-c0-JY].

If z0>0 and a finite nonnegative vector b satisfy

    b>=Y0,                 G(z0,b)<=b,                    (1)

then the tuned density and stream series and every weighted spatial derivative converge absolutely and uniformly on each closed exterior r>=R with R>z0^(-Q/2). The common potential of132 has the same strict radius and its only logarithmic corrections are at orders Q and2Q. For amplitude epsilon!=0 multiplying a normalized profile, a sufficient radius is z0^(-Q/2)|epsilon|^(Q/2).

The conclusion is conditional only on131 and132 and the stated exact inequalities. It requires no inferred limit of computed coefficients. An unsuccessful choice of b or z0 implies nothing about divergence.

## Proof of the certificate

The Q+1 dimensional matrix J is strictly lower triangular, hence J^(Q+1)=0 and T is nonnegative. The remainder Psi(z,Y)=Phi(z,Y)-c0-JY has nonnegative coefficients, each with a strictly positive power of z. Multiplying the equation (I-J)Y=c0+Psi by T proves that the original polynomial system is equivalent to Y=G(z,Y).

Starting with Y^(0)=0, iterate Y^(j+1)=G(z,Y^(j)) as formal series. All coefficients are nonnegative and the iterates are coefficientwise increasing. Because every monomial of G-Y0 contains z, the coefficient of z^n depends only on coefficients of lower z degree. Induction on n therefore proves stabilization to the unique formal solution. This is the formal majorant solution constructed in131.

For 0<=z<=z0 and 0<=Y<=b, positivity gives G(z,Y)<=G(z0,b)<=b. Thus every iterate evaluated at z0 is bounded by b. Monotone convergence of nonnegative series implies that the limiting formal series converges at z0, with each vector coefficient bounded componentwise by b z0^(-n). The finite shifts and fixed low coefficients that reconstruct the scalar majorants preserve a geometric coefficient bound with base z0^(-1). The coefficient domination in131 transfers it to the tuned density and stream.

The Fourier bandwidth is at most Bn. Each fixed angular or radial derivative costs only a polynomial in n after the natural radial weight is factored out. On any strict subdisk |z|<z0 these polynomial factors are summable against (|z|/z0)^n. A small positive angular strip can also be absorbed by requiring exp(B tau)|z|<z0. Since z=r^(-2/Q), the stated strict exterior radius follows. Topic132 reconstructs the common potential without increasing the geometric base, so it gives the same radius for its weighted derivatives. The absolutely convergent products and derivatives satisfy the original stationary potential equation term by term.

Finally, every order-n coefficient, including the tuned harmonic, is homogeneous of degree n in the leading amplitude. Multiplying the leading profile by epsilon therefore replaces z by epsilon z in absolute majorants. This gives the radius factor |epsilon|^(Q/2).

## Exact construction and independent indexing comparison

The implementation uses rational arithmetic only. It forms x_j=Cat_(j-1)(kappa L)^(j-1)a^j for1<=j<=Q and evaluates every polynomial in131 directly from coefficient arrays. It obtains c0 and the columns of J by evaluating Phi(0,0) and Phi(0,e_j). It explicitly checks strict lower triangularity. Forward substitution computes T and Y0, avoiding a numerical matrix inverse.

For the proposed box b=2Y0, test z0=2^(-q) on the nonnegative even integers q. The implementation retains each failed trial, the successful exact component ratios, and the preceding failed trial. For even q, the sufficient radius is exactly2^(qQ/2). All root-specific input inequalities are checked against the exact isolating intervals and the certified response lower bounds from133.

As a separate indexing check, specialize this general construction to Q=3 and compare J,T,Y0 and G(z0,b) exactly with all four previously checked cases in124. Those four equations were derived and implemented separately. Equality checks the general shifts, truncated low-order products and boundary terms against the established construction.

Dependencies:130 for the exact response,131 for coefficient domination,132 for the same-radius common potential,133 for the Q5 profile and response certificates, and124 for the independent Q3 comparison.

## Completed exact applications

The general-Q implementation agrees exactly with all four previously certified Q3 matrices, preconditioners, initial vectors and transformed-map values. All six Q5 input norm bounds and response bounds pass. The successful dyadic certificates are:

| Root in increasing order | Norm bound a | Response lower bound s | z0 | Sufficient normalized radius |
| --- | --- | --- | --- | --- |
| 1 | 149/100 | 1/32 | 2^(-56) | R>2^140 |
| 2 | 1049/1000 | 1/8388608 | 2^(-70) | R>2^175 |
| 3 | 563/500 | 1/65536 | 2^(-64) | R>2^160 |
| 4 | 1213/1000 | 1/32768 | 2^(-64) | R>2^160 |
| 5 | 329/250 | 1/16384 | 2^(-64) | R>2^160 |
| 6 | 39/25 | 1/2048 | 2^(-62) | R>2^155 |

A common bound a=8/5 and s=1/8388608 gives z0=2^(-74), hence R>2^185 for all six normalized profiles. Each inequality is strict. These are sufficient, conservative radii; no optimality claim is made. The output retains exact rational component ratios and all preceding failed even powers. Multiplication by |epsilon|^(5/2) gives the amplitude-scaled radii.
