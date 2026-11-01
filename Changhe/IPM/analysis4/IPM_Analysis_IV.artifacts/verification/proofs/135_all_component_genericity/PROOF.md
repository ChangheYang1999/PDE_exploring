# Generic tuning on every regular normalized compatibility component

Status: PROVED, with independent theory-part confirmation dated2026-10-31T10:38Z, recorded in V273. The Q=3, Q=4 and Q=5 applications use the independently reviewed recurrence and convergence theorems130-133 and 142. The Q=4 extension was checked in V285.

## Statement

Choose Q in {3,4,5}, delta=2/Q and c=Q/(Q-2). Fix an even bandwidth B>=6 and write normalized leading profiles as

    f(b,t)=sin(theta)+b sin(3theta)
              +sum_(j odd, 5<=j<B) t_j sin(j theta).

The real parameter vector t has d=B/2-2>=1 coordinates. Let O(b,t) be the coefficient of sin(theta) in f_(2Q), computed by the pure nonresonant recurrence through order2Q-1. No stream resonance occurs before2Q. Let

    M={ (b,t): O(b,t)=0 and grad O(b,t)!=0 }

be its regular real compatibility hypersurface. For k>=2 let sigma_k(b,t) be the Q-step resonant response defined in130; when Q=3 it is the response already proved in119. Define

    G={ (b,t) in M: inf_(k>=2)|sigma_k(b,t)|>0 }.

Then G is relatively open and dense in every connected component of M, and its complement has measure zero in every smooth coordinate chart. No component is required to contain a previously verified profile. Every point of G has the unique tuned convergent pure density and stream series, with all weighted derivatives and the common potential. Each compact subset of G has a common sufficient exterior radius.

When B=6, the exceptional set M\G is countable and relatively closed in M. Its accumulation points in M lie among a finite set where sigma_infinity=0. The set contains only failures of the sufficient response condition; this theorem does not assert divergence or nonexistence at those points.

For any nonzero first sine coefficient, divide all leading coefficients by it to apply this normalized statement. Scaling back gives the usual factor |epsilon|^(Q/2) in the sufficient radius. Profiles with zero first sine coefficient and singular points of O=0 are outside this statement.

## 1. Polynomial structure and irreducibility

Set m=2Q. Every order-n coefficient below the first resonance is a homogeneous polynomial of degree n in the full leading amplitudes, with rational coefficients, because all divisors are fixed nonzero rationals. After fixing the first amplitude to1, O(b,t) is a rational polynomial of total degree at most m.

Its restriction O(b,0) is the degree-m irreducible polynomial already certified in119 for Q3, 142 for Q4 and130 for Q5, multiplied by a nonzero rational constant. Therefore the coefficient of b^m in O is nonzero. Total degree at most m forces that coefficient to be a constant independent of t. Divide by it and call the resulting monic polynomial P(b,t). Then P has degree m in b and P(b,0) is monic irreducible over Q.

We claim that P is irreducible in Q[t,b]. Suppose P=A C were a proper factorization there. The leading coefficients of A and C as polynomials in b multiply to1 in Q[t]. Hence both are nonzero rational constants; after rescaling, both factors are monic in b. Specialization t=0 therefore preserves both b degrees and gives a factorization of P(b,0). Its irreducibility forces one factor to have b degree0. That monic factor is the constant1. This contradicts properness and proves the claim. Gauss's lemma then gives irreducibility in Q(t)[b].

For every k, sigma_k is a rational polynomial of total degree at most Q in(b,t). The uniform response estimate and eventual rational dependence on k in129or131 imply that sigma_k converges locally uniformly, over complex parameters, to a rational polynomial sigma_infinity of total degree at most Q. The restriction of every sigma_k and of sigma_infinity to t=0 is nonzero by the exact two-mode response calculations119, 142 and130. Hence none is the zero polynomial.

Since their b degree is less than m, irreducibility of P implies that each sigma_h, with h=k or infinity, is coprime to P in Q(t)[b]. The univariate resultant

    R_h(t)=Res_b(P(b,t),sigma_h(b,t))

is therefore a nonzero polynomial in Q[t]. If P and sigma_h vanish at the same real(b,t), then R_h(t)=0. This implication holds even when the response loses degree at that t, because P is monic and its degree never drops.

## 2. No response vanishes on a regular component

First, the points of M where partial_b P!=0 form an open dense subset of M. Openness is immediate. To prove density, suppose partial_b P=0 throughout a nonempty open piece of M. At one of its regular points some partial_(t_j)P is nonzero. The implicit function theorem represents that piece as t_j=phi(b,t_hat). Differentiation gives

    partial_b phi=-(partial_b P)/(partial_(t_j)P)=0.

After shrinking to a connected coordinate box, phi is independent of b. Fixing the other coordinates then makes P(b,t)=0 for an interval of b with the entire vector t fixed. A monic polynomial of positive degree cannot vanish on an interval. This contradiction proves density.

Suppose some sigma_h vanished throughout a nonempty open subset of M. That subset contains a point with partial_b P!=0. Near this point the implicit function theorem represents P=0 as b=beta(t), with t varying over an open set in R^d. The common-zero implication then gives R_h(t)=0 throughout that open set. A nonzero real polynomial cannot vanish on an open set, contradicting Section1. Thus no sigma_h restricts identically to any connected component of M, and each of its zero sets has empty interior there.

This argument uses rational irreducibility only to produce the nonzero resultants. It does not incorrectly infer irreducibility over R or C from irreducibility over Q. The regular real component may have any permitted topology.

## 3. Openness, density, measure and convergence

Local uniform convergence sigma_k->sigma_infinity yields

    inf_k|sigma_k|>0
      iff sigma_infinity!=0 and every sigma_k!=0.           (1)

For the reverse implication, the tail is bounded below by half the nonzero limit modulus and the finitely many preceding nonzero moduli have a positive minimum. The forward implication follows by taking the limit. The same local uniform convergence and continuity show that the condition in(1) is open: keep the limiting response away from zero on a bounded neighborhood, choose one uniformly controlled tail, and shrink the neighborhood for the remaining finite responses.

By Section2 the zero set of each response, finite or limiting, is a closed nowhere dense subset of each regular component. Baire's theorem makes their countable union have dense complement in every coordinate neighborhood. This complement is precisely G by(1).

Each nontrivial analytic function on a connected real analytic chart has a null zero set. Here is the elementary argument needed: at a zero, choose the first nonzero derivative in its Taylor series. A derivative of one lower order vanishes there and has a nonzero first derivative. The point therefore lies on a regular zero hypersurface of some derivative. The countably many such derivatives and a countable chart cover contain the entire zero set in a countable union of smooth hypersurfaces. Each has measure zero. The identity theorem excludes a point where all Taylor coefficients vanish, unless the original analytic function vanishes on the whole component. Section2 excludes that possibility. Taking the countable union over all responses proves the measure assertion.

For each point in G, the exact first compatibility condition and positive uniform response bound are precisely the hypotheses of119or131. They give the uniquely tuned convergent series. The corresponding potential theorem121or132 gives the common potential and all weighted derivatives. Openness provides a positive local response lower bound; a finite cover of any compact subset of G, together with its bounded leading norms, gives a common majorant and sufficient radius.

## 4. The three-mode curve

If B=6, t is a single real coordinate. Each nonzero resultant R_h(t) has only finitely many zeros. Above each such t, the monic polynomial P(b,t) has at most m roots. Thus each individual response has only finitely many common zeros with P, even including singular points. Their countable union is countable. Since G is relatively open, M\G is relatively closed.

Let points of M\G accumulate at a point x in M with sigma_infinity(x)!=0. Local uniform response convergence gives a neighborhood of x and an index K on which every k>=K response stays nonzero. Only finitely many earlier response zero sets remain, and each is finite by the preceding paragraph. Such a set cannot have infinitely many distinct points accumulating at x. This contradiction proves the claimed accumulation restriction. The zeros of sigma_infinity on P=0 are themselves finite by its nonzero resultant. Accumulation at infinity or outside M is not covered by this local statement.

## Dependencies and scope

The exact irreducible polynomials and nonzero two-mode responses are in119, 142 and130. Polynomial homogeneity is proved directly by the recurrence and response block. Local uniform limiting responses are proved in129for Q3 and131for Q4 and Q5. The convergence and potential conclusions use119/121 and131/132 respectively. No numerical experiment or claim about an unknown compatibility component is assumed. The new point is that monicity and an irreducible two-mode specialization rule out an identically vanishing response on every regular normalized component.
