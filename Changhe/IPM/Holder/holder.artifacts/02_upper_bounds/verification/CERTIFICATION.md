# Reproducing the interval evaluations

The script `../../code/check_explicit_bounds.py` uses Python 3.12 and python-flint ball arithmetic at 256-bit precision. Its exact rational alpha inputs and output enclosures are in `../../data/explicit_bounds_intervals.json`. These enclose the explicit formulas in the proof; they do not assert that the formulas are exact operator norms.

The quantities $a_1$ and $a_2$ are evaluated from

$$a_1(\alpha)=\frac{2^{\alpha-1}}{\sqrt\pi}
\frac{\Gamma((\alpha+2)/2)}{\Gamma((\alpha+3)/2)},\qquad
a_2(\alpha)=\frac{2^{1+\alpha/2}}{\pi(\alpha+2)}.$$

The first identity follows by substituting into the beta integral for $\int_0^{\pi/2}\sin^{\alpha+1}t\,dt$.

For $a_3$, substitute $s=\sin t$ and use $\sin3t=3s-4s^3$:

$$a_3(\alpha)=\frac{3\,2^\alpha}{\pi}(3J_0-4J_1),\qquad
J_p=\int_0^{1/2}\frac{s^{\alpha+1+2p}}{\sqrt{1-s^2}}\,ds.$$

The binomial series has coefficients $c_0=1$ and $c_{k+1}=c_k(2k+1)/(2k+2)$. They satisfy $0<c_k\le1$. Termwise integration of this nonnegative series gives

$$J_p=\sum_{k=0}^\infty
c_k\frac{2^{-(\alpha+2+2p+2k)}}{\alpha+2+2p+2k}.$$

For the first $N=120$ terms, the omitted tail is nonnegative and at most

$$\frac43\frac{2^{-(\alpha+2+2p+2N)}}{\alpha+2+2p+2N}.$$

This follows by replacing $c_k$ by 1, replacing all tail denominators by the first one, and summing a geometric series with ratio $1/4$. The script adds the full interval from zero to this upper bound before forming $3J_0-4J_1$. All remaining operations use outward ball arithmetic. Exact rational alpha values enter through `fmpq`.

The script also compares $a_3$ with 65-digit mpmath quadrature. That comparison is a diagnostic independent of the series implementation. It is not part of the certificate: the tail inequality and ball operations supply the enclosure.

Reproduction command, from the artifacts root:

```
python3 code/check_explicit_bounds.py
```

The displayed decimal midpoints are convenient approximations. The `intervals` fields, which include radii, are the certified output. Rounded decimal upper bounds for publication must be rounded upward beyond the entire corresponding enclosure.
