# Directed savings from five disjoint disk pairs

## Statement and hypotheses

Use the operators and homogeneous Holder seminorm of the parent proof. The independently accepted disjoint-disk theorem and its exact geometry certificate must hold before the numerical endpoints below are admitted. Keep the main disk pair and its first eight reflection moments exactly as certified in V231. Add the four rational pairs

    (c,a)=(41/100,3/40), (29/100,1/25), (9/40,3/125), (7/40,7/500).

For each pair use the first eight positive even reflection moments. For each table row start from the exact rational upper endpoint in V231. Subtract only the savings from these four new pairs. Thus the main-disk saving is never counted twice. For retained-cutoff rows use the density correction of the parent proof. For the uniform coefficient on 0<alpha<=1/100, divide the even-binomial coefficient by alpha and evaluate it at 1/100; all its remaining factors decrease in alpha, so this gives a uniform lower saving.

The endpoint data, rather than this statement, supply the final rational decimals. Every upper endpoint is rounded upward by exact rational arithmetic. The finite choices of centers and radii are feasible choices, with no claim of global optimality.

## Positive series for a disk not tangent to the outer circle

Put M=(c+a)^2, q=2ca/M. On 0<=x<=a,

    c^2+2cx+a^2 = M-2c(a-x),  0<=2c(a-x)/M<=q<1.

The reflected moment is consequently the positive series

    I_n(c,a)=sum_(k>=0) (2c/M)^k / M
                  * integral_0^a x^(2n)(a-x)^k sqrt(a^2-x^2) dx.

Writing j_m=integral_0^1 t^m sqrt(1-t^2)dt, the kth term is

    (2c/M)^k a^(2n+k+2)/M
          * sum_(l=0)^k (-1)^l binom(k,l) j_(2n+l),
    j_0=pi/4, j_1=1/3, j_(m+2)=(m+1)j_m/(m+4).

Each term is a rational linear combination of 1 and pi. The integral proves its strict positivity. The ratio of successive terms is at most q, directly from the positive integrands. Use terms k=0,...,63 as a lower bound; the omitted tail is at most the kth term with k=64 divided by 1-q. The program checks positive lower endpoints for every term despite the cancellations in the rational expression.

## Independent moment evaluation

Put A=c^2+a^2, B=2c, Delta=c^2-a^2. For

    F_m=integral_0^a x^m sqrt(a^2-x^2)/(A+Bx) dx,

substitution x=a sin(theta), followed by the half-angle substitution, gives

    F_0=[A*pi/2-Ba-2Delta*atan((c-a)/(c+a))]/B^2,
    F_m=[a^(m+1)j_(m-1)-A F_(m-1)]/B, m>=1.

Here Delta>0 because a<c/2. The recurrence gives I_n=F_(2n). At 768-bit precision this independently computed ball must be contained between the positive-series partial-sum interval and its explicit tail upper bound. This is a separate check of the moment formula and normalization.

## Recombination

With A_n(alpha)=2alpha product_(k=1)^(2n-1)(k-alpha)/(n!)^2, define

    Btilde_(2n+1)=2^(2n+1) I_n/[pi binom(2n,n)].

Then A_n(alpha)s^(2n)Btilde is exactly H_(i,n) in the parent theorem. In a retained-cutoff row replace Btilde by

    Btilde - kappa a^(2n+2)/(2n+2), kappa=s^2/(1-s)^2.

This follows by evaluating the constant-density integral using
j_(2n)=pi binom(2n,n)/(4^(n+1)(n+1)). The parent theorem guarantees positivity of the retained density; the program also checks the directed retained moments. Original and transformed summation orders at 384 and 768 bits must give nested enclosures and identical upward ten-place decimals. Every dependency, proof, source, and geometry certificate is bound by a SHA256 digest in the acceptance record.
