# Full Laplacian norm by exact differentiation and ball polynomial products

## Statement and hypotheses

Let c=4076476460239181/2251799813685248, delta=1-1/c, and let chi be the exact rational potential of C1-N1-007-d2w-j7-e2bal. The canonical coefficient file has SHA256 153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316. Define rho=-partial_y Delta chi, u=(-chi_xyy,chi_xxy), and F=(cX+u).grad rho-rho. For a>=0 the target is the whole-plane norm

    N(a)^2 = integral_R2 (1+r^2)^(2-a) |Delta F|^2 dX.

This note proves a second evaluation route for exactly the same finite expression used in ../candidate007_weighted_laplacian/PROOF.md. It replaces large exact rational polynomial products by outward ball products after differentiation and endpoint cancellation have been checked exactly. It does not replace the exact candidate by rounded coefficients.

The input is the complete exact residual cache, whose source hash and assembly hash must match its retained assembly record. This cache contains every sine mode through the maximum nonlinear frequency. It has representation

    F = r sum_(ell,n) v^(ell delta/2) P_(ell,n)(t) sin(n theta),
    v=(1+r^2)^(-1), t=1-v,

with rational polynomials P and positive odd frequencies n. No frequency is dropped.

## Exact differentiation and endpoint cancellation

For d=ell delta/2 define

    T_d P = (1-2dt)P + 2t(1-t)P'.

The identity r partial_r(r v^d P(t))=r v^d T_d P follows from r partial_r t=2t(1-t) and r partial_r v=-2tv. Applying the polar Laplacian gives

    Delta [r v^d P(t) sin(n theta)]
       = r v^(d+1) L(t) sin(n theta),
    t L = T_d(T_d P)-n^2 P.

The code forms the right hand polynomial exactly, divides by t exactly, and requires zero remainder. It then composes L(1-v) exactly and factors its exact first nonzero power v^q:

    L(1-v) = v^q Q(v), Q(0) != 0.

For every component it requires ell delta+2q-2>0. This is precisely diagonal integrability at a=0, because the radial density below is v^(ell delta+2q-3)(1-v). It implies integrability for all a>=0. Cross terms are integrable by Cauchy-Schwarz, and the code also checks each cross-term exponent directly.

The independent slower route forms the Cartesian Hessian and compares its trace with the polar identity. All completed slower-mode energies are compared with the corresponding results of this route. The algebraic identity above, rather than a sampled agreement, is the justification for using the polar formula on the remaining modes.

## Complete integral and outward arithmetic

Full-circle sine orthogonality gives a factor pi for each frequency n; r dr=dv/(2v^2) in absolute value. Therefore

    N(a)^2 = (pi/2) sum_n sum_(ell,k) integral_0^1
       v^[a+(ell+k)delta/2+q_ell+q_k-3]
       (1-v) Q_(ell,n)(v) Q_(k,n)(v) dv.

The implementation uses each unordered pair once, with multiplicity two for distinct ell. Within each n all radial cross terms are included. Terms with the same exponent are added. If a grouped polynomial is sum_j z_j v^j with exponent b, its integral is

    sum_j z_j/(a+b+j+1).

Each denominator is a strictly positive rational number. Convert each exact Q coefficient to a containing Arb ball, multiply and add polynomials by outward Arb arithmetic, divide by outward positive rational balls, and multiply by the outward value of pi/2. These operations enclose the exact expression. Taking the outward square root encloses the norm whenever the computed energy lower bound is positive. Failure of positivity or of an accuracy check aborts that mode; it never produces a claimed certificate.

The finite expression includes v=0, which is spatial infinity. No finite-radius cutoff, numerical quadrature or asymptotic tail replacement occurs. Endpoint cancellations are established before ball arithmetic; a ball containing zero is never treated as an exact cancellation.

## Completeness, comparison and scope

A write-once manifest records the input hashes, all frequencies, requested rational weights, arithmetic precision, code and this proof. Every completed mode record carries that manifest hash. A full upper norm is produced only after every manifest frequency has a matching record. Until then sums over completed modes provide lower bounds only.

Comparisons with the slower Cartesian method and with the independently supplied N3 norm file are consistency checks between proved algorithms and matched inputs. Interval overlap alone is not a proof. New full candidate values remain N4-origin and OPEN pending a peer computation or review. No nonlinear existence or inverse estimate follows from any of these norm values.
