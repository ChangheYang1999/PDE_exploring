# A signed seventh residual mode in the first-projection construction

Verifier result 105, written 2026-10-21 before its supporting checker. This is a quantitative supplement to result 101, not a new finite-angular-support nonexistence theorem. The latter was already proved in results 9 and 93.

## Statement

Use the first-projection construction of result 101. In its notation, fix ell>1, n>=0, a=(8n+6)(ell+1), M=a/4-(ell-1)>0 and any sufficiently small beta>0, in particular beta<=1/4. The prescribed mode is

    g(r)=2 beta M r^2(1+r^2)^(-beta-1),
    K(r)=r^-6 int_0^r s^5 g(s) ds.

For the complete density rho=r f sin(theta)+r g sin(3theta) and its canonical stream from result 101, define R=(ell X+U).grad rho-rho and R_7(r)=int_0^(2pi)R(r,theta)sin(7theta)dtheta. Then at every r>0,

    R_7/(pi r) = K (dot g+4g) - 3g^2/4
               < g^2 (d-2)/(4(d+6)) < 0,                  (1)
    d = dot g/g = 2-2(1+beta)r^2/(1+r^2),

where a dot denotes r d/dr. Moreover, with g2=2 beta M,

    lim_(r->0) R_7/(pi r^7) = -g2^2(1+beta)/10.           (2)

These statements do not require solving for f. They show directly that every member of this family is a nonprofile, including the n=0 value at which its cubic third residual coefficient vanishes. The main unbounded-slope assertion already follows from n>=1; no change to that assertion is needed.

## Dependencies and exact Fourier coefficient

Result 101 gives

    psi = r^2 Z2 sin(2theta) + r^2 Z4 sin(4theta),
    Z2=(T-J)/2,    Z4=-K/2,
    dot K=g-6K.

This formula is the canonical inverse there. The following calculation uses the defining velocity U=(-psi_y,psi_x), so U_r/r=-2Z2 cos(2theta)-4Z4 cos(4theta) and U_theta/r=(2Z2+dot Z2)sin(2theta)+(2Z4+dot Z4)sin(4theta). In

    R/r = ell (f+dot f) sin theta + ell (g+dot g) sin(3theta)
        + (U_r/r)[(f+dot f) sin theta+(g+dot g) sin(3theta)]
        + (U_theta/r)[f cos theta+3g cos(3theta)]
        - f sin theta-g sin(3theta),

only multiplication of modes 4 and 3 can produce mode 7. The coefficient of sin(7theta) is

    -2 Z4(g+dot g) + (3/2)g(2Z4+dot Z4)
      = Z4 g-2Z4 dot g+(3/2)g dot Z4
      = K(dot g+4g)-3g^2/4.

The orthogonality integral of sin(7theta)^2 is pi, proving the identity in (1). In particular all dependence on f, J, T and the scaling drift ell has dropped out. This cancellation follows from the angular supports; it is not an approximation.

## Strict sign for every radius

Put t=log r. Direct differentiation gives the displayed d, which is strictly decreasing in t, with -2beta<d<2 and d+4>0. The regular integral for K is

    K(t) = int_(-infinity)^t exp(-6(t-s))g(s) ds.

For s<t, strict decrease of d gives

    log[g(s)/g(t)] = -int_s^t d(v)dv < -d(t)(t-s).

Therefore

    0<K/g < int_0^infinity exp(-(6+d(t))u)du = 1/(6+d(t)).

The integrability is valid since d>-1/2 here. Multiplying the strict inequality by d+4>0 yields

    R_7/(pi r g^2) = (K/g)(d+4)-3/4
                  < (d+4)/(d+6)-3/4
                  = (d-2)/(4(d+6)) < 0.

This proves the global strict sign. It also gives a quantitative lower bound for the absolute seventh projection at each positive radius. It is not a uniform positive lower bound as beta decreases to zero.

## Center coefficient

Expanding only the explicitly prescribed functions,

    g=g2 r^2+g4 r^4+O(r^6),    g4=-(1+beta)g2,
    K=g2 r^2/8+g4 r^4/10+O(r^6),
    dot g+4g=6g2 r^2+8g4 r^4+O(r^6).

The r^4 coefficient of K(dot g+4g)-3g^2/4 cancels. The r^6 coefficient is

    (8/8+6/10-3/2)g2 g4 = g2 g4/10.

Multiplication by pi r proves (2). The resulting r^7 sin(7theta) term has the proper smooth Cartesian degree. Thus no singular angular interpretation is used.

## Scope and verification

The full family in result 101 is canonical, smooth and sublinear only after the origin, departure, trapping and far-field arguments there. The identity (1) is local algebra for that stream, but the use of this stream as the canonical inverse depends on those verified arguments. We do not replace them by a local Poisson computation.

The separate checker expands arbitrary first modes and the prescribed third mode as rational Cartesian polynomials, differentiates the stream and density, projects the polynomial residual onto sin(7theta), and compares every homogeneous coefficient with (1). It also checks (2) and exact sign algebra. Finite checks support the identities; the strict all-radius comparison is proved above.
