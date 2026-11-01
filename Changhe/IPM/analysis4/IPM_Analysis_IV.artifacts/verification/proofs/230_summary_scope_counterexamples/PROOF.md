# Two scope corrections to the summary

Status: complete proof; independent theory-part review requested. The underlying convergence and pole theorems are unchanged.

## Statements and hypotheses

1. The pole-order estimate in Proposition 3.5 must retain its maximum with zero. For a fixed nonzero finite odd sine profile, the stream estimate is U(n)=max(0,floor(n/Q)-1), and the sharper density estimate is V(n)=max(0,floor((n-1)/Q)-1). The estimate floor(n/Q)-1 without the maximum fails for n<Q.

2. There are certified convergent tuned density and stream series at delta=2/3 whose common potential necessarily contains a logarithm. Consequently a statement that tuning removes every logarithm must specify the density and stream series. It cannot include the potential.

For the second assertion let b be either real root of

    P(b)=176703765525000 b^6-222533688701250 b^5+96180432855375 b^4
         -20675598499400 b^3+2783057141280 b^2-243275209320 b+10532171936.

Take c=3, delta=2/3 and f_1=epsilon(sin(theta)+b sin(3theta)), where epsilon is any nonzero real number. Topic119 proves irreducibility of P over the rationals, its two real roots, the nonvanishing response condition and convergence of the uniquely tuned density and stream series. Topic121 constructs their convergent common potential with only the exceptional order3 and order6 logarithmic terms.

## Proof of the first correction

Take Q=5, n=1 and f_1=sin(theta), independent of epsilon=delta-2/5. Its first sine coefficient is the constant1, with pole order0. The proposed bound floor(1/5)-1=-1 is false. The first stream is also analytic and nonzero: at delta=2/5 its coefficient at sin(2theta) is -5/36. Thus the defect affects either interpretation of the unqualified phrase "pole order at order n". The bounds U,V stated in the full theorem give0 and are correct. No issue arises in that theorem's proof.

## Proof that the tuned potential needs a logarithm

Homogeneity of the recurrence gives f_3 proportional to epsilon^3. The exact Cartesian computation in topic119 gives

    [sin(theta)] f_3 = epsilon^3 A(b),
    A(b)=-3 b^3/64+1161 b^2/17920-573 b/44800+1/6400.

This is a nonzero polynomial of degree3 over the rationals. Since b has irreducible minimal polynomial P of degree6, A(b) cannot vanish. These coefficients are determined before the first free stream multipole, which occurs at order6. Tuning that multipole and later ones cannot change f_3.

A pure order3 potential has the form chi_3=r^2 C(theta), with C even under both coordinate reflections and hence a cosine series in the nonnegative even frequencies. For a single such frequency ell,

    Delta(r^2 cos(ell theta))=(4-ell^2) cos(ell theta),
    -partial_y Delta(r^2 cos(ell theta))
      =ell(4-ell^2)/(2r) [sin((ell+1)theta)+sin((ell-1)theta)].

For ell=0 or2 this vanishes. For every even ell>=4 its sine frequencies are at least3. Therefore a pure r^2 potential has no r^(-1) sin(theta) density coefficient. The same follows term by term for any smooth even angular C, by taking the corresponding Fourier coefficient. This contradicts epsilon^3 A(b)!=0.

The radial exponents S_n=4-2n/3 are distinct. An order other than3 cannot supply the missing r^(-1) density term. Thus the common potential cannot be a pure series sum r^(S_n) C_n(theta). Topic121 supplies the missing term by a linear combination of r^2 log(r) and r^2 log(r) cos(2theta). At least one coefficient in this combination is nonzero. Its presence is consistent with completely pure, convergent density and stream series.

## Scope and dependencies

This correction concerns three unqualified sentences in the summary and theory, retained in sources/claim_snapshot.json. The existing summary already describes the potential logarithms elsewhere. The intended repair is local wording: "no logarithm appears in the density or stream series". This is not a refutation of TheoremT, Proposition3.5 or the convergence result.

Dependencies: topic119 exact low-order coefficients, irreducibility and tuned convergence; topic121 potential reconstruction. An additional independent order3 recomputation is queued as a redundancy check, but the argument above already follows from admitted exact data.
