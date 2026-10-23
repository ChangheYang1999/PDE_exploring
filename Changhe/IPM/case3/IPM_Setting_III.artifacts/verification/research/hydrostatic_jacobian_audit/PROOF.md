# Independent finite hydrostatic Jacobian

Written 2026-10-21T10:12:34.531004+00:00 before implementation. This result specifies a finite linearization and its independent numerical evaluation. It does not assert invertibility, a continuum spectral gap or a profile.

## Statement, notation and hypotheses

Fix c>1 and a finite real density space spanned by functions phi_j, smooth on the whole plane, even in x and odd in y. Suppose each function and its first two Cartesian derivatives have the common sublinear bounds needed for the hydrostatic vertical-tail inverse in result185. The finite Q basis from result187 has this property. Its saved map parameter P>1 and nodes tk are fixed independently of c. Let g_u=sum_j u_j phi_j. At each fixed sample X_i=(x_i,y_i), define

    T_1[g](x,y)=-int_y^infinity g_x(x,t)dt,
    T_2[g](x,y)=int_0^y t g_xx(x,t)dt+y int_y^infinity g_xx(x,t)dt

in the upper half-plane, with the established parity extension, and

    R_i(u)=(c X_i+T[g_u](X_i)).grad g_u(X_i)-g_u(X_i).

The finite vector R is a quadratic polynomial in u. Its exact directional derivative is

    J_u h=(c X+T[g_u]).grad g_h+T[g_h].grad g_u-g_h.        (1)

For any real t the exact remainder at each sample is

    R(u+t h)-R(u)-t J_u h=t^2 T[g_h].grad g_h.             (2)

These claims hold equally for any fixed linear quadrature approximation T_h. They do not equate two different quadrature approximations.

## Proof and constraint rows

The growth hypotheses make each defining improper integral convergent. The sum over basis functions is finite, so it commutes with the inverse without any limiting argument. Thus T[g_(u+th)]=T[g_u]+t T[g_h]. Expanding the transport product proves(1) and(2), including all cross terms. No linearized PDE has been solved in this computation.

Let G,Gx,Gy,V1,V2 be the rectangular matrices whose jth columns are phi_j, d_x phi_j,d_y phi_j,T_1 phi_j,T_2 phi_j at the chosen samples. The derivative matrix is therefore

    J=diag(c x+V1 u)Gx+diag(c y+V2 u)Gy-G
                      +diag(Gx u)V1+diag(Gy u)V2.         (3)

The two normalization rows are a(u)-1 and K(u)-1, both affine; their derivative rows are linear. In the shifted local Q basis, the k=0 block gives a=sum_j(-1)^j u_(0,j). The stored coordinate equation, checked directly in the independent reader before implementation, is

    r=L sqrt(sigma)/[2^P(1-sigma)^P],       t=2sigma-1,
    g=y(1-sigma)sum_k sigma^k q_k(t)cos(2k theta),
    q_k(t)=sum_j u_(k,j) T_j(z_k(t)), b_k(t)=sigma^k q_k(t).

Consequently 1-sigma~L^(1/P)/(2r^(1/P)), and the vertical tail coefficient is

    K=L^(1/P)/2 sum_k(-1)^k sum_j u_(k,j).

The shifted polynomial argument tends to1 at the exterior endpoint, so every Chebyshev polynomial there equals1. This proves the stated tail row without replacing the stored binary P by a nominal rational value. The initial pre-implementation draft contained an undecided coordinate-factor convention; the displayed equation was corrected by reading both branches of the independent Newton inversion before any checker or result used it.

The optional center row is c+C(u)-1, where C is the canonical center strain. Result185 proves its exact compact integral

    C(u)=-a(u)-sum_(k>=1) k^2(-1)^k int_(-1)^1
             [ (1-t)/2+2P(1+t)/2 ] [(1+t)/2]^(k-1) q_k(t)dt.

The integrand in each mode is a polynomial of degree at most N for the local finite space. A Gauss-Legendre rule exact through that degree therefore gives the row in exact arithmetic; numerical quadrature and polynomial evaluation still round. Comparison with187's exact rational value is required. If c is a variable while P and all sample coordinates stay fixed, the additional transport column is x g_x+y g_y and the center-row entry is1. Export200 used fixed-c Jacobians; the first comparison does the same.

## Independent implementation and verification plan

Construct every density basis column by a three-term Chebyshev recurrence, differentiating that recurrence once and twice. Transform those radial/angular derivatives analytically to Cartesian derivatives. This differs from the producer's sampled barycentric evaluation and finite-difference inverse. The scalar Cartesian evaluator185, which uses coefficient Clenshaw evaluation, provides a separately evaluated contraction check. Scalar multiprecision differentiation and the previously exact center functionals provide further checks.

Integrate each column over fixed physical subintervals with Gauss-Legendre quadrature, and integrate the entire exterior after t=R/v with the Jacobi weight v^(-p), p=1-1/P. There is no boundary condition at R: both pieces are evaluated. Change finite and exterior orders and the split R; record observed differences. The same exported Cartesian sample coordinates and stored coefficients are retained. Compare the resulting F and J diagnostics with the frozen exports. A changed spectrum is a discretization-sensitivity result, not evidence that one finite matrix has the exact continuum spectrum.

For any numerical J, compute the three residual projections exactly as defined in195, with the same stated Euclidean coefficient/row norms. Reconstruct the per-mode sampled visible space directly from its evaluation matrix and stated relative cutoff, without producer imports. A small singular value, a projection onto a restricted coefficient space, or an approximately null projected dilation vector is not an exact-rank or field-space coercivity certificate. The continuum kernel from scaling concerns exact solutions; at a trial state the identity includes the residual derivative. The K=1 row does not contain the dilation tangent.

Initially test small manufactured coefficient spaces and selected directional derivatives. Full-state matrix builds and SVDs are queued after the only active N44 solve and its primary audit. Only one heavy process runs, single-threaded at nice19; matrices may be deleted after their reproducible summaries are saved to respect the lane disk limit. Until those computations finish the exported spectral and projection claims remain open for independent recomputation.

## Dependencies and scope

Results185 and187 define and verify the Q reconstruction and full-tail hydrostatic inverse. Result190 gives a separate exact axis primitive;195 proves the finite-dimensional SVD interpretation and counterexamples to overclaims. Result200 freezes input arrays and checks export consistency. This proof establishes only(1)-(3) and the finite linear constraint rows under the displayed stored coordinate convention. It does not give an original SettingIII profile or an early-stop endpoint.

Review corrections and their complete argument: REVIEW_REPAIR_PROOF.md (2026-10-21T11:39:54.554626+00:00).
