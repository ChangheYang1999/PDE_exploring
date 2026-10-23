# No exact primary profile has finite angular support outside a disc

Written 2026-10-21. Status at first writing: complete proposed informal proof, awaiting independent code checks and actual Opus5.5 adversarial review. This is a restricted nonexistence theorem, not a NO endpoint for the full primary problem.

## 1. Statement and established inputs

Suppose rho is an exact smooth primary profile on R^2:

    (ell X+U).grad rho = rho,   ell>1,
    U=(-psi_y,psi_x),          -Delta psi=rho_x,

rho is even in x and odd in y, rho_y(0)!=0, and for some 0<gamma<1,
|rho|+(1+r)|grad rho| <= C(1+r)^gamma. U is the canonical parity-preserving velocity with U=o(r). Then there do not exist R0>0 and a finite odd N>=1 for which

    rho(r,theta)=sum_{1<=j<=N, j odd} f_j(r) sin(j theta)
                         for every r>R0.                 (1)

No sign or equilibrium assumption is added. Finiteness is required with one common N on the whole exterior, not just on individual circles with a varying N.

The following already proved necessary properties of exact primary profiles are the inputs from the earlier research:

- Put p=1/ell in (0,1). All Cartesian derivatives satisfy
  |D^alpha rho|+|D^alpha U| <= C_alpha r^{p-|alpha|} for r>=1.
- r^{-p} rho(r,theta) tends uniformly to a nonzero angular function Theta_0. In particular its value on the upper y-axis is K!=0. The function Theta_0 is smooth.

The first input is the local-continuation/far-field theorem in ../local_ipm_continuation/PROOF.md. The second is the nonzero far-field theorem in ../nonzero_far_field/PROOF.md, together with that regularity theorem. Under (1), smoothness of Theta_0 also follows from finite-dimensional angular support and uniform convergence. The proofs and audits of those results are dependencies; no additional regularity is presumed here.

Write O_S(r^b) for an exterior function whose every Cartesian derivative of order j is O(r^{b-j}); constants may depend on j and on b. A finite polyhomogeneous expression means a finite sum

    r^s P(log r,theta),                                  (2)

where P is a polynomial in log r with finite trigonometric-polynomial angular coefficients. These are finite asymptotic expressions. No convergence of an infinite series will be claimed.

## 2. The exact radial transport identity

Let B=U.grad rho. The equation and p=1/ell give

    d_r(r^{-p}rho) = -(1/ell) r^{-p-1} B.

The symbol bounds give B=O_S(r^{2p-1}), and 2p-1<p. Integrating toward infinity yields, for X!=0,

    rho(X)=r^p Theta_0(theta)+T B(X),
    T f(X)=(1/ell) int_1^infinity t^{-p-1} f(tX) dt.       (3)

For f=O_S(r^b) with b<p, differentiation under the integral is valid at every order: t^j from j derivatives is cancelled by the derivative's order-j decay. Thus T f=O_S(r^b). In particular

    rho=r^p Theta_0+O_S(r^{2p-1}).                        (4)

If s<p and P is a polynomial, T maps r^s P(log r,theta) to another expression of the same degree s and no larger logarithmic degree. Indeed

    T[r^s (log r)^d G(theta)]
      = (r^s/ell) G(theta) sum_{j=0}^d
           binom(d,j) j! (log r)^{d-j}/(p-s)^{j+1}.       (5)

No radial resonance occurs in (3), because every source degree is strictly below p.

## 3. Exterior inverse lemma, including resonances and multipoles

Lemma. Let f be a smooth even-x/odd-y density of sublinear growth with symbol bounds outside a disc, and suppose its angular support is finite outside some disc. Suppose, for a number b<1,

    f = sum_{s>b} r^s P_s(log r,theta) + O_S(r^b),         (6)

where the sum is finite, all s<1, and b is not -m-1 for any positive even integer m. Its canonical velocity has a finite expansion above degree b, with remainder O_S(r^b). Every retained term is of one of the following two types:

(a) degree s inherited from a density term in (6), with stream angular frequency m=j-1 or j+1 when the density frequency is j; its logarithmic degree may increase at the resonance s=-m-1;

(b) a decaying harmonic stream r^{-m} sin(m theta), giving velocity of degree -m-1, for an even m>=2.

Only finitely many terms of type (b) have degree above b. The velocity is expressed in polar components in this statement; their angular frequencies are the corresponding stream frequencies m. The lemma includes derivative remainder bounds of every order.

Proof. Multiply each displayed density term by one fixed smooth radial cutoff equal to one in the exterior. This gives a globally smooth density with the same parities and sublinear growth. Subtract their sum from f. The resulting density E has exterior O_S(r^b) bounds and still has finite angular support outside a disc. The canonical inverse is linear, so it suffices to handle a cutoff term and E.

For a cutoff term, differentiation d_x sends a sine frequency j to j-1 and j+1. If its radial degree is s, the source degree is s-1, with polynomial logarithmic coefficients. For one positive even frequency m, put z=log r and seek a particular stream r^{s+1} Q(z) sin(m theta). Its radial equation is

    -[Q''+2(s+1)Q'+((s+1)^2-m^2)Q]=P(z).                (7)

When (s+1)^2!=m^2 this linear map is invertible on polynomials of degree at most deg P, by its nonzero diagonal in descending powers. If s+1=-m it becomes -Q''+2m Q'=P. It has a polynomial solution of degree at most deg P+1, unique after setting its additive constant to zero. The other resonance s+1=m would require s>=1 and is excluded. The exterior homogeneous solutions are r^m and r^{-m}; the coefficient of r^m is zero because its velocity has growth r^{m-1}, which violates U=o(r) for m>=2. A multiple of r^{-m} can remain. This proves the two asserted types for cutoff terms, including logarithms.

For E, the source g=E_x is O_S(r^{b-1}). At any fixed positive even frequency m its canonical stream is

    psi_m(r)=(1/(2m))[ r^{-m} int_0^r s^{m+1}g_m(s)ds
                     +r^m int_r^infinity s^{1-m}g_m(s)ds ]. (8)

The outer integral is O(r^{b-m+1}), since b<m-1; after multiplication by r^m and differentiation it gives velocity O(r^b). In the inner integral the exponent of the bound is m+b. If b>-m-1, the integral is O(r^{m+b+1}) plus a constant, and its velocity is O(r^b). If b<-m-1, its integral to infinity converges, and subtracting that integral leaves O(r^{m+b+1}); the subtracted constant gives exactly the decaying harmonic stream in (b). The equality case was excluded in the choice of b. Repeated radial differentiation follows from (8) and the symbol bounds on g. With finitely many source modes in the exterior, these estimates give every Cartesian derivative bound for their sum.

There can be infinitely many other stream modes, generated by the interior density. They are harmonic outside a fixed radius R1. Their coefficients in (8) obey a bound C R1^{m+2} times a fixed polynomial factor in m: the source is smooth and bounded on that disc, and one can bound its Fourier coefficients by its supremum. For r>=2R1, the series of streams r^{-m} and every differentiated series therefore converge geometrically. After any fixed number of low modes is removed, the tail has the corresponding arbitrarily negative power bound, with constants depending on the number of derivatives. Only finitely many low harmonic modes must be retained to reach degree b. This proves the lemma. The compact interior need not have finite angular support. End proof.

## 4. Finite expansions to arbitrary depth

Assume (1) toward a contradiction and put delta=1-p>0. We claim that rho and U admit finite expansions of the form (2) to every prescribed finite negative order, with O_S remainders, allowing logarithms and all the harmonic terms in the lemma.

Start with (4) and choose a threshold b with 2p-1<b<p that is not a resonance or an exponent of a retained term. This gives (6) for rho. Apply the inverse lemma to obtain an expansion of U above b. Both rho and U are O_S(r^p), with leading terms of degree p and no logarithms at that degree. Multiplying their finite expansions and differentiating the density, all errors in U.grad rho are O_S(r^{p+b-1})=O_S(r^{b-delta}). The reason is that each error is multiplied by an exact or finite leading expression of symbol size O(r^p), or by its gradient; any lower powers with logarithms are still O_S(r^p). A product of two errors is smaller since b<p.

Apply (3) and (5). We obtain a finite expansion for rho plus an O_S(r^{b-delta}) remainder. Choose a new threshold b' strictly between b-delta and b-delta/2, avoiding every exponent in the finite expression and every resonance -m-1. Discard terms of degree below b'. They are O_S(r^{b'}) even with their logarithms, because the inequality of degrees is strict. We now have (6) at threshold b'. The difference between rho and the finite expression still has finite angular support in the exterior, so the inverse lemma remains applicable. Repeating reduces the threshold by at least delta/2 each time. This proves the claim with finitely many steps for every prescribed depth.

The retained coefficients are unique on overlaps of such expansions. For if a nonzero finite difference were O(r^b) below all its degrees, take its highest degree and then highest logarithmic degree. After division by that power of r and log r its nonzero angular coefficient would tend to zero, a contradiction. This also proves that every density coefficient at every retained degree has only the frequencies in (1): take the angular projection onto any frequency above N. Thus the expansions may be compared coefficient by coefficient, including coincident exponents.

For later bookkeeping, every density degree has the form p-t with

    t in Lambda={k delta+2l : k,l nonnegative integers}.  (9)

This set is locally finite. Indeed k<=T/delta and l<=T/2 below any bound T. The leading density has cost t=0. An induced velocity has the same cost as its density source. A harmonic velocity of frequency m has degree -m-1, hence cost q=p+m+1. In (3) a product of an induced velocity and a density gradient has cost delta+t_i+t_j, and a product of a harmonic velocity and a density gradient has cost

    delta+(p+m+1)+t_j=m+2+t_j.                          (10)

Since m is even, these operations preserve (9). Logarithms introduce no new degrees. Formula (9) may include costs whose coefficients are zero; it is only an encompassing set. At each positive density cost the product uses strictly smaller density costs, by delta in the induced case and by at least 4 in the harmonic case. This makes induction on the ordered locally finite costs legitimate.

## 5. Angular grading separates the multipoles

Let n be the highest nonzero positive odd frequency of Theta_0 and a its nonzero coefficient. Put

    C=(n+1)/delta.

We claim that every angular frequency j of a density coefficient of cost t satisfies

    j <= n+C t,                                         (11)

and every induced stream or polar velocity frequency m at cost t satisfies

    m <= n+1+C t.                                       (12)

A harmonic velocity at cost q=p+m+1 lies strictly below its corresponding bound:

    m < n+1+C(p+m+1),                                   (13)

since all the quantities on the right except possibly m are positive and C>1. In fact C>2.

Prove (11)-(12) by increasing density cost. They hold at cost zero; differentiating a density in x changes its frequency by at most one, and the radial inverse, including a resonant logarithm, does not change that stream frequency, proving (12). An induced velocity at cost t_i acting on a density of cost t_j has frequencies no higher than

    (n+1+C t_i)+(n+C t_j)
       = n+C(delta+t_i+t_j),                            (14)

because C delta=n+1. Its radial degree gives exactly that density cost by (10). A harmonic velocity satisfies the same estimate strictly, by (13). The angular derivative in transport does not change frequencies, and angular products have frequencies bounded by their sum. This proves the induction. It also explains why a later logarithmic resonance cannot create an angular frequency above (11).

Equality in (11) can be created only when both factors in (14) attain their respective bounds, and the product uses the sum frequency. It cannot come from a harmonic velocity, by (13), from a lower angular source, or from the difference frequency. Starting with the leading top frequency n, it follows inductively that equality can occur only at costs

    t=k delta,   j=n_k=(k+1)(n+1)-1.                    (15)

At such a cost let A_k(z) be the polynomial in z=log r multiplying sin(n_k theta). We next prove that it is a nonzero constant. Contributions at the same radial degree from other representations of the cost in Lambda cannot change this conclusion: unless built entirely from equality cases they have strictly smaller angular frequency, even when exponents coincide.

## 6. The boundary coefficients cannot cancel

A_0=a is a nonzero constant. Suppose every earlier boundary coefficient is a constant. The density degree at cost k delta is

    s_k=p-k delta=(k+1)p-k.

For the induced stream of its boundary frequency n_k, the possible top frequency is n_k+1, and

    n_k-s_k=(k+1)(n+2-p)-2>0,
    n_k+s_k+2=(k+1)(n+p)+2>0.                           (16)

Thus that top stream mode is never resonant. Its coefficient is

    -A_k/[2(n_k+s_k+2)],                               (17)

as follows directly from (7), or from the modal derivative of r^{s_k}sin(n_k theta). In particular a logarithm cannot be introduced into a boundary stream when its density coefficient is constant.

At boundary cost k delta with k>=1, all source terms therefore have constant logarithmic coefficients. Formula (5) makes A_k constant too. Only interactions of boundary costs i delta and j delta with i+j=k-1 can reach its angular frequency. Polar transport gives the exact recurrence

    k D A_k=sum_{i+j=k-1} c_{ij} A_i A_j,
    D=ell-1,
    c_{ij}=(1/4)[1-2(j+1)(n+1)/((i+1)(n+p)+2)].          (18)

For completeness its sign argument is as follows. Put u=i+1, v=j+1, S=u+v>=2, B=n+p, and A=n+1. Then

    c_{ij}+c_{ji}=1/2-(A/2)[v/(uB+2)+u/(vB+2)]<0.       (19)

Indeed the bracket, at fixed S, decreases as uv increases to S^2/4, so it is at least 2S/(BS+4). This lower bound is strictly greater than 1/A because S(n+2-p)>4. Hence pairing i,j in (18) proves inductively

    A_k=(-1)^k a^{k+1} b_k,   b_k>0.                    (20)

The detailed polar derivation and the balanced-pair inequality are in ../formal_highest_mode_cascade/PROOF.md; equations (16)-(19) also state every ingredient needed here. This argument covers any sign of a and also i=j. Individual unpaired c_{ij} were not assumed negative.

Choose a finite k with n_k>N. Section 4 supplies the finite expansion through a threshold below s_k. Its coefficient at frequency n_k must be zero by (1) and uniqueness. Equation (20) says it is nonzero. This is the required contradiction and proves the theorem.

## 7. Scope and verification status

Only finite angular support on a fixed exterior is excluded. General smooth angular functions, infinite angular series, or a number of active modes growing with radius are not covered. The argument does not assume an infinite expansion converges; it uses finitely many terms for the chosen N. Interior multipoles and resonant logarithms are retained and separated by (11)-(14). Their presence is why the pure-power formal recurrence by itself was not a proof of this exterior theorem.

At the first writing, code checks and actual Opus5.5 adversarial follow-up are pending. The full primary existence question remains unresolved regardless of this restricted theorem's eventual audit verdict. There are no Lean/Lake sources or computer-assisted existence claims.
