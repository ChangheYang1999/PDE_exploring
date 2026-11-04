# Exact finite jets at one helicity-free vortical zero

This audit confirms the finite algebra in the submitted `in the team records` at its stated scope. It also corrects the dimension count in the theory summary. The computations are exact algebra, not a formal proof-assistant verification.

## Statement and conventions

Take \(c=1/4\), \(\omega=0\), \(p_0=(-4,0,0)\), \(u=e_1\), and

\[
M=\begin{pmatrix}-1/2&-1/2&0\\1/2&-1/2&0\\0&0&1\end{pmatrix},
\qquad N=cI+M.
\]

Write \(X=(x,y,z)=y-p_0\), \(V_0=u\), \(V_1=MX\), and \(V_n\) for a homogeneous velocity polynomial of degree \(n\), without factorials. Put \(W_j=\operatorname{curl}V_{j+1}\). Then \(cp_0+u=0\), \(\operatorname{tr}M=0\), \(W_0=e_3\), and \(Ne_3=(1+c)e_3\). The first jet is admissible at a vortical carrier zero. The eigenvalues of \(N\) are \(5/4,-1/4\pm i/2\).

A finite extension through velocity degree \(n\) means that divergence vanishes identically, and the vorticity and helicity equations vanish through homogeneous degree \(n-1\). Pressure can then be chosen so that momentum vanishes through degree \(n\). This definition concerns jets, not an exact profile on an open set.

The following are confirmed:

1. At this first jet the full homogeneous operator ranks, for \(n=2,\ldots,6\), are \(14,27,43,61,82\). They attain analytic upper bounds and hence hold on a nonempty Zariski-open set of the stated nonrotating first-jet family.
2. In the reflection class specified below, with the stated fixed quadratic term, the degree-five extension condition is exactly \(F=0\).
3. On its specified \(\gamma=0\) branch, degree-six extensions exist, but no degree-seven extension in this class exists.

No other quadratic jet, arbitrary first jet, rotating branch, infinite formal series, convergent solution or general \(C^2\) exclusion is covered by these statements.

## Derivation of the equations

For an admissible first jet in general, set \(A=cI-\omega J\), \(N=A+M\), \(w=\operatorname{curl}V_1\), and \(\kappa=1+c\). At the carrier zero,

\[
B=NX+\sum_{j\geq2}V_j,\qquad
W=w+\sum_{j\geq1}W_j.
\]

Extract degree \(n-1\) from \([B,W]+\kappa W=0\). Its terms linear in \(V_n\) are

\[
\mathcal L_nV_n=(NX\cdot\nabla)\operatorname{curl}V_n
+(\kappa I-N)\operatorname{curl}V_n-(w\cdot\nabla)V_n.
\]

The remaining terms use lower jets. Divergence and helicity give the full linear extension system

\[
\begin{aligned}
\operatorname{div}V_n&=0,\\
\mathcal L_nV_n
&=-\sum_{\substack{i,j\geq2\\i+j=n+1}}
\left((V_i\cdot\nabla)W_{j-1}-(W_{j-1}\cdot\nabla)V_i\right),\\
u\cdot\operatorname{curl}V_n
&=-\sum_{i=1}^{n-1}V_i\cdot W_{n-1-i}.
\end{aligned}
\tag{1}
\]

Every term on the right has the required degree and depends only on already chosen jets. At the sample first jet, \(\kappa I-N=I-M\) and \(w\cdot\nabla=\partial_z\), matching the submitted implementation.

If \(E_m\) is a curl-free homogeneous momentum coefficient of degree \(m\), differentiating \(X\cdot E_m\) gives

\[
\partial_k(X\cdot E_m)=(E_m)_k+
\sum_jX_j\partial_k(E_m)_j
=(m+1)(E_m)_k.
\]

The second equality uses curl-freeness and homogeneity. Thus \(P_{m+1}=-X\cdot E_m/(m+1)\) cancels it. This includes \(m=0\). Consequently pressure supplies no further finite-order compatibility condition after the curl equation.

## Analytic bounds and independent rank certificates

There are \(C_n=3\binom{n+2}{2}\) velocity coefficients and \(R_n=5\binom{n+1}{2}\) output coefficients in (1). Since the divergence of a commutator is \(F\cdot\nabla\operatorname{div}G-G\cdot\nabla\operatorname{div}F\),

\[
\operatorname{div}\mathcal L_nV+
(w\cdot\nabla)\operatorname{div}V=0.
\tag{2}
\]

The coefficient relations in (2) are independent and number \(\binom n2\): the divergence map from vector polynomials of degree \(n-1\) onto scalar polynomials of degree \(n-2\) is surjective, as can be seen by integrating any scalar polynomial in one coordinate.

For \(w\ne0\), the gradients of harmonic homogeneous polynomials of degree \(n+1\) in the plane perpendicular to \(w\) form a two-dimensional subspace of the kernel. Their curl and divergence vanish, and their derivative along \(w\) vanishes. Hence

\[
\operatorname{rank}\leq
\min\left(C_n-2,\ R_n-\binom n2\right).
\tag{3}
\]

The exact rational reconstruction gave:

| Degree | Rows | Columns | Rank | Kernel | Compatibility beyond (2) |
|---:|---:|---:|---:|---:|---:|
| 2 | 15 | 18 | 14 | 4 | 0 |
| 3 | 30 | 30 | 27 | 3 | 0 |
| 4 | 50 | 45 | 43 | 2 | 1 |
| 5 | 75 | 63 | 61 | 2 | 4 |
| 6 | 105 | 84 | 82 | 2 | 8 |

An independent checker, in the team records, reconstructs (1) using sparse monomial differentiation over \(\mathbb F_{101}\). It imports neither the submitted solver nor SymPy. For each degree it selects a square minor of the claimed rank and evaluates its determinant directly. The determinants modulo 101 are respectively \(10,4,46,96,51\), all nonzero. Exact row and column indices are recorded in JSON. The rational matrix has denominators dividing powers of two, so reduction modulo 101 is legitimate. These minors prove lower bounds equal to (3), independently certifying all ranks.

The matrix coefficients depend polynomially on \(c,a,b,q\) in the family

\[
\omega=0,\quad u=e_1,\quad w=qe_3,\quad
M=\begin{pmatrix}a&b&0\\b+q&-1-a&0\\0&0&1\end{pmatrix},
\qquad q\ne0.
\]

Each certified nonzero minor is therefore a nonzero polynomial in these parameters. The simultaneous nonvanishing locus of the five minors is a nonempty Zariski-open subset, containing the sample datum. The same analytic upper bounds hold there. This proves the asserted finite-degree generic statement, with no assertion at every datum or at higher degrees.

## The reflection class and degree-five condition

Require the first two components of every \(V_j\) to be even in \(z\), and the third odd. Fix

\[
V_2=\left(
\frac{25x^2}{16}+\frac{25y^2}{8}-\frac{19z^2}{16},
-\frac{25y^2}{32}+\frac{41z^2}{32},
-\frac{25xz}{8}+\frac{25yz}{16}
\right).
\]

It satisfies (1) at degree two. The parity of the five output polynomials in (1), in their displayed order, is even, odd, odd, even, odd. Thus retaining precisely those monomials loses no equation.

The complete cubic solution has three free coefficients

\[
\alpha=[x^2y](V_3)_2,\quad
\beta=[x^3](V_3)_2,\quad
\gamma=[x^2z](V_3)_3.
\]

Every such cubic admits quartic extensions, with free coefficients
\(\eta=[x^3y](V_4)_2\) and \(\theta=[x^4](V_4)_2\).
All remaining coefficients are uniquely determined by (1) and these named coefficients. Their exact values are retained in the team records.

At degree five the parity matrix has 36 rows, 33 columns and rank 31. Exact augmented row reduction of the lower-jet right side leaves the single nonzero compatibility polynomial \(F/3456\), where

\[
\begin{aligned}
F={}&193536\alpha\gamma-1493280\alpha
-152064\beta\gamma+1019520\beta\\
&-995328\gamma^2+13832144\gamma-48500415.
\end{aligned}
\tag{4}
\]

There is no dependence on \(\eta,\theta\). Vanishing of every transformed zero-row right side is necessary and sufficient for solvability of a finite linear system. Thus (4) is an exact necessary and sufficient condition. When it holds, the two free quintic coefficients are \(\mu=[x^4y](V_5)_2\), \(\nu=[x^5](V_5)_2\).

The copied solver was inspected and rerun from (1), including its monomial parities, parameter conventions, exact row reduction and direct substitution into every preceding system. The recomputed degree-five output agrees with the submitted output after omitting newly added empty `imposed` metadata objects. No coefficient or compatibility expression differs.

## Degree six and the exact degree-seven obstruction

Restrict to \(\gamma=0\), so (4) requires

\[
\alpha=(1019520\beta-48500415)/1493280.
\]

The degree-six compatibility equations uniquely fix

\[
\beta=\frac{382954920413016027}{4160999632469440},\quad
\eta=\frac{657863206696985940102949061}{88624398836031287938560},\quad
\theta=-\frac{31994004467357074464350371}{19694310852451397319680}.
\]

After this substitution every degree-six compatibility expression vanishes. The parameters \(\mu,\nu\) remain free, and two more coefficients in \(V_6\) are free.

At degree seven, row reduction gives affine compatibility equations in \(\mu,\nu\), independent of the two degree-six free coefficients. The coefficient rank is two and the augmented rank is three. An exact short certificate uses the first three integer numerators of these equations. Their columns, in the order coefficient of \(\mu\), coefficient of \(\nu\), constant, reduce modulo 101 to

\[
\begin{pmatrix}3&13&55\\15&66&69\\57&80&96\end{pmatrix}.
\]

Its determinant over the integers is \(-106053\), congruent to \(98\pmod {101}\). Thus the original integer augmented matrix has a nonzero three-by-three minor, while its two-column coefficient matrix has rank at most two. The system is inconsistent over \(\mathbb R\), as well as over \(\mathbb Q\).

The degree-seven reconstruction agrees exactly with the submitted JSON. A separate direct checker sets all remaining degree-six parameters to zero, reconstructs pressure from the momentum polynomial, and checks divergence identically, momentum through degree six, and helicity through degree five. It also independently reads and checks the augmented rank and modular inconsistency certificate. Its output agrees exactly with the submitted check. Thus the concrete polynomial satisfies momentum \(O(|X|^7)\) and helicity \(O(|X|^6)\). Neither residual is asserted to vanish to all orders.

## Corrections to the theory summary

The general kernel statement is “a kernel of dimension at least two.” Its dimension at the sample data is four at degree two and three at degree three.

The raw difference between unknowns and equations is

\[
C_n-R_n=(n+1)(3-n)=-n^2+2n+3.
\]

After removing the \(\binom n2\) structural row relations, it is

\[
C_n-\left(R_n-\binom n2\right)=(-n^2+3n+6)/2.
\]

The printed expression \((8+n-n^2)/2\) is neither count. When the rank equals \(C_n-2\), the number of compatibility functionals beyond (2) is

\[
\left(R_n-\binom n2\right)-(C_n-2)
=(n^2-3n-2)/2,
\]

which gives \(1,4,8\) at degrees \(4,5,6\). These are linear conditions on an abstract right side. They need not be algebraically independent after that right side is expressed through lower jets.

Solvability through degree three for every compatible lower right side follows at the sample first jet, and where the same maximal ranks hold. No universal rank assertion for every admissible first jet was checked.

A high-order obstruction, even if proved for every smooth formal jet, does not by itself exclude a \(C^2\) profile. Such a conclusion requires the corresponding additional differentiability or a separately proved bootstrap. This sample is nonrotating and is much narrower still.

## Exact affine obstruction, independent of the computation

For any \(c,\omega\), suppose an exact \(C^2\) profile has a vortical carrier zero \(p\), with \(u=U(p)\), \(w=W(p)\ne0\), and \(M=DU(p)\). The vorticity equation at \(p\) gives

\[
(cI-\omega J+M)w=(1+c)w,\qquad
Mw=(I+\omega J)w.
\]

If helicity is identically zero near \(p\), its derivative along \(w\) is zero. Hence

\[
u\cdot((w\cdot\nabla)W)(p)=-w\cdot Mw=-|w|^2.
\tag{5}
\]

Thus \(u\ne0\), and the indicated component of the vorticity derivative is nonzero. If \(U\) were affine, \(W\) would be constant and (5) would be impossible. This is an exact argument for arbitrary rotation. A floating-point minimization residual is unnecessary and supplies no universal substitute for it.

## Evidence and limits

The plan, source snapshots, exact outputs, comparison record and independently constructed modular minors are retained in the team records. Each algebra job ran on one assigned CPU with one thread and a finite timeout.

The complete proof consists of the homogeneous derivation, analytic rank bounds, explicitly indexed finite algebra and pressure reconstruction above. The degree-five and degree-seven compatibility identities remain computer-assisted exact algebra; they are not merely numerical rank estimates. The calculation does not decide the local helicity-free problem at a general vortical zero or the global decaying-profile problem.
