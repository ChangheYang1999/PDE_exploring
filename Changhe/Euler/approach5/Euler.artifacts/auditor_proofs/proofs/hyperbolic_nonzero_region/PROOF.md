# Uniform hyperbolicity away from the degeneracies

## Statement

Assume H0: U,P are C^2 entire rotating Euler profiles, div U=0. Put B=(cI-omega J)y+U, Omega=curl U, b=1+c and a=1-2c. Let 0<c<1/2. Let K be a compact set invariant for all times of the B flow, with B cross Omega nonzero at every point. Then K is a nonsingular hyperbolic set with continuous invariant splitting

    T_K R^3 = E^s + E^0 + E^u,
    E^0=R B,  E^u=R Omega,
    ||DPhi_t|E^s|| <= C exp(-a t),
    C^-1 exp(b t)|v| <= |DPhi_t v| <= C exp(b t)|v| on E^u,
    C^-1|v| <= |DPhi_t v| <= C|v| on E^0,  t>=0.

The constant C depends on K and the profile. The exponents are independent of omega. It suffices to assume B and Omega are separately nonzero on K: the degeneracy lemma below then makes their cross product nonzero.

Under H1-prime, every alpha-limit set exists and is compact. For a vortical point, its alpha-limit set is either a hyperbolic set as above, or meets {B=0}, or meets {Omega=0}. These alternatives need not be disjoint.

## Exact covector identity

Let alpha=(B cross Omega)^flat. Cauchy's formula, transport of B by its own flow, and det DPhi_t=exp(3ct) give, for every v,

    alpha_(Phi_t x)(DPhi_t v)=exp(-a t) alpha_x(v).       (1)

Indeed, the left side is det(B(Phi_t x),Omega(Phi_t x),DPhi_t v). Replace its first two vectors by DPhi_t B(x) and exp(-bt)DPhi_t Omega(x), and take the determinant.

## Degenerate orbits

The sets {B=0}, {Omega=0} and {B cross Omega=0} are invariant by the same transport identities. Suppose a bounded full orbit starts with nonzero B and Omega but Omega=lambda_0 B. Along it,

    Omega(Phi_t x)=lambda_0 exp(-bt) B(Phi_t x).

Boundedness of Omega gives |B(Phi_-t x)|<=C exp(-bt) as t tends to infinity. Boundedness of B gives |Omega(Phi_t x)|<=C exp(-bt). Therefore the alpha-limit set meets {B=0} (indeed lies in it), and the omega-limit set lies in {Omega=0}. In particular such a point cannot belong to a compact full invariant set avoiding both zero sets.

## Explicit construction of the stable complement

Let E=span(B,Omega). On K, compactness gives upper and positive lower bounds for |B|, |Omega| and |B cross Omega|. Thus the coefficients in v=pB+qOmega are uniformly comparable to |v|. The exact transport rule

    DPhi_t v=p B(Phi_t x)+q exp(bt)Omega(Phi_t x)

implies that DPhi_t on E has inverse norm bounded by a constant for every t>=0. Its quotient cocycle on T R^3/E contracts by at most C exp(-at), because alpha annihilates E and (1) holds.

For completeness, choose the continuous orthogonal complement N=E-perp. In E+N coordinates the time-T derivative has block form

    [ A_x  C_x ]
    [  0   D_x ],

where A_x acts on E and D_x represents the quotient action. Choose T so large that sup_x ||A_x^-1|| ||D_x||<1. This is possible by the preceding two estimates. On continuous bundle maps L_x:N_x->E_x, define

    (G L)_x=A_x^-1( L_(Phi_T x) D_x - C_x).

In the sup norm this is an affine contraction on the complete space of continuous sections. Its unique fixed point defines E^s_x as the graph of L_x. The fixed-point equation gives invariance under DPhi_T. Transporting this graph by any DPhi_t, 0<=t<=T, produces another continuous invariant complement for DPhi_T, so uniqueness gives invariance for all times. The graph norm is uniformly equivalent to the quotient norm on compact K; hence its derivative norm is at most C exp(-at). The other two lines have the stated exact exponential rates directly from Cauchy's formula and transport of B. This proves uniform hyperbolicity without an unverified graph-transform citation.

## Scope

This confirms CO5a, CO5b, CO5c and the stated alpha-limit trichotomy. It does not confirm the separate positive-measure basin claim CO5-prime, the isolating-neighborhood topology paragraph without its needed connectedness hypotheses, or the conjectural knot-exterior construction. In particular this proof deliberately excludes stagnation points; it supplies no domination estimate at them.

Audit recorded: 2026-11-02T18:53:25Z
