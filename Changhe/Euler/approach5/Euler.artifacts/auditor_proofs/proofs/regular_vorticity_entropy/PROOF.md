# Entropy with nonvanishing vorticity on the core

## Statement and scope

Let U be C2 and P be C1 on R3, with div U=0, solving the rotating profile equation. Assume U=o(|y|) uniformly, 0<c<1/2 and finite omega. Write B=(cI-omega J)y+U, Omega=curl U, a=1-2c and F=Phi_{-1}, where Phi is the complete B-flow. For a sufficiently large closed backward-trapping ball K0 define Lambda=intersection_{n>=0} F^n(K0). If Omega never vanishes on Lambda, then

    h_top(F|Lambda) >= a.

This confirms LIT18. The nonvanishing assumption is additional. This is not unconditional nonexistence or an unconditional C2 entropy theorem.

## Flow and transported form

Sublinearity gives |B(y)|<=C(1+|y|), hence completeness, and B(y).y>=c|y|^2/2 outside a ball. Thus F(K0) is contained in int K0, Lambda is compact and F-invariant, and the nested sets F^n(K0) eventually enter every neighborhood of Lambda.

The C1 form beta=i_Omega vol=d(U.dy) satisfies Phi_s^* beta=e^{(2c-1)s} beta. Consequently F^*beta=e^a beta, and F preserves its kernel line field R Omega where Omega is nonzero. Compactness and the extra hypothesis give N with K=F^N(K0) in a neighborhood on which Omega is nonzero. K contains a small C1 embedded disk S transverse to Omega, oriented so beta is positive on it. Put A0=int_S beta>0. Then

    int_{F^n(S)} beta=e^{an} A0.

## Uniform bound in a Bowen ball

We give the step that cannot be replaced by counting all atoms of an arbitrary partition.

Choose finitely many C1 flow boxes for Omega covering K, each with a smaller relatively compact box. In coordinates (q1,q2,z), local plaques are q=constant. Coordinate maps and inverses have bounded derivatives. There are uniform C, eta>0 such that points in one smaller box on the same larger-box plaque can be joined in that plaque by an arc of length <=C times their ambient distance, while any arc shorter than eta starting in the smaller box stays in the larger box. Include one fixed box for S, with S meeting each plaque at most once.

Choose a compact neighborhood of K on which DF^{-1} is bounded by L. Shrink delta>0 so every subset of K of diameter <=2delta lies in one smaller box, all relevant arcs lie in that neighborhood, and 2LCdelta<eta. These choices are independent of n.

Let E be the intersection of S with a Bowen ball of radius delta for times 0,...,n. Every F^j(E) has diameter <=2delta. If x_n,y_n in F^n(E) lie on the same plaque of the chosen terminal larger box, join them there by an arc of length <=2Cdelta. Its F^{-1} image is a leaf arc of length <=2LCdelta<eta. Its endpoints lie in the preceding smaller box, so the entire image arc lies in the preceding larger box. The endpoints are therefore on a common local plaque. Replace this arc by the bounded-length vertical-coordinate arc and repeat backward. At time zero both endpoints lie in S and on one plaque of its fixed box, hence coincide. Therefore projection to q is injective on F^n(E).

In each flow box beta=g(q,z)dq1 wedge dq2, with g bounded. Projection to q is a local C1 diffeomorphism on the transverse disk F^n(S). Its injectivity on F^n(E), the change-of-variables formula and bounded q-domains give

    int_{F^n(E)} beta <= M,

with M independent of n and the Bowen ball. Open Bowen balls give relatively open pieces of the disk apart from its boundary, which has zero two-dimensional area. Equivalently one can disjointify a finite cover into measurable pieces. Positivity of the transported orientation permits summing without cancellation.

If r_{n+1}(K,delta) Bowen balls cover K, they cover S. Hence

    e^{an} A0 <= M r_{n+1}(K,delta),

so h_top(F|K)>=a.

## Restriction to Lambda

Every F-invariant Borel probability mu on K has mu(F^m K)=1: F^{-m}(F^m K)=K within the domain K. It therefore gives Lambda full measure. The variational principle for a continuous map on the compact metric space K gives h_top(F|K)=h_top(F|Lambda), proving the assertion.

## Source and audit boundary

The independent proof above follows the characteristic-foliation idea in Arnaud and Fejoz, Invariant submanifolds of conformal symplectic dynamics, JEP 11 (2024), 159-185, Theorem 5, printed pages 167-170, DOI 10.5802/jep.252. The actual manuscript in the team records and its text were read. That printed theorem assumes a C2 foliation on a compact manifold; the present trapping-set proof explicitly uses only C1 flow boxes and a minimal Bowen-ball cover. The argument does not silently invoke the printed result with weakened hypotheses. It needs no derivative bound at infinity, pressure normalization, or absence of B-stagnation points.
