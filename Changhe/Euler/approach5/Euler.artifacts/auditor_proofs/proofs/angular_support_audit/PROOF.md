# Angular support, odd transformations and the mean-swirl source

## Statements and hypotheses

Let c>0 and omega be finite. Let U in C2(R3;R3), P in C1(R3) solve the whole-space rotating profile equation with div U=0 and U tending uniformly to zero at infinity. Define

    Lambda V=(1-c)V+((cI-omega J)y dot grad)V+omega J V,
    N(V)=(V dot grad)V,
    (T_theta V)(y)=R_theta V(R_-theta y).

The exact linear-kernel theorem A046 says Lambda V+grad p=0, div V=0 and V tending to zero imply V=0. It holds for complex V by taking real and imaginary parts.

1. Let V_m=(2*pi)^(-1) integral exp(i*m*theta) T_theta U dtheta, and S={m:V_m is not identically zero}. Every m in S has curl N_m not identically zero, where N_m is the corresponding projection of N(U). Thus S is contained in S+S. This confirms C10.
2. If sigma is any orthogonal transformation commuting with J, and sigma U(sigma^-1 y)=-U(y), then U=0. No finite-order hypothesis is needed. This confirms and modestly strengthens C11.
3. For 0<c<1/2, one may replace decay by uniform sublinearity in the following separate assertion. Put Ubar=angular mean, Gamma=Jy dot U, Gamma0=Jy dot Ubar and E=mean[(U-Ubar)(Gamma-Gamma0)]. Then with Bbar=cy+Ubar and its flow Ybar,

    Gamma0(x)=-integral_-infinity^0 exp((1-2c)*s)
                         (div E)(Ybar(s,x)) ds.

In particular div E=0 implies Gamma0=0. This confirms C13.

## Exact projection and support proof

Rotations preserve divergence, decay, regularity and the linear equation. For fixed y, the functions theta -> (T_theta U)(y) and theta -> D(T_theta U)(y) are square-integrable on the circle. The Fourier coefficient of each scalar product is the convolution of its coefficient sequences. For fixed m, Cauchy-Schwarz gives absolute convergence of that convolution. Summing the three vector components therefore gives the exact, untruncated identity

    Lambda V_m + grad P_m + N_m=0,
    N_m=sum_(k+l=m) (V_k dot grad)V_l.

The projected field N_m is C1. If its curl vanishes, the whole-space Poincare lemma gives N_m=grad q_m with q_m C2, componentwise over the complex numbers. Applying A046 to V_m and pressure P_m+q_m gives V_m=0. If m is absent from S+S, every term in the absolutely convergent convolution vanishes, so N_m=0, proving the support rule.

Reality gives S=-S. The rule excludes support entirely in L times the odd integers, including a single pair of nonzero modes. It says nothing further when zero belongs to S, because then S subset S+S is automatic. It does not exclude every finite spectrum or every zero-mean spectrum.

An additional exact identity in the source also checks. Taking curl and integrating the resulting linear equation along y(s)=exp(c*s)R_-omega*s y gives

    curl V_m(y)=-integral_-infinity^0 exp(s)R_omega*s
                                      curl N_m(y(s)) ds.

The term at minus infinity vanishes because y(s) tends to zero and curl V_m is bounded nearby. The integral converges absolutely and yields norm(curl V_m)_(sup B_r)<=norm(curl N_m)_(sup B_r). It does not produce a high-mode gain.

## Odd transformation proof without finite order

Let T V=sigma V(sigma^-1 y), and T p=p(sigma^-1 y). Orthogonality and commutation with J give T Lambda=Lambda T, T grad p=grad T p and T N(U)=N(TU). If TU=-U, applying T to the equation gives

    -Lambda U+N(U)+grad(TP)=0.

Subtracting this from the original equation gives

    2 Lambda U+grad(P-TP)=0.

A046 now gives U=0. This proof does not use any order of sigma. For sigma=-I it excludes even velocity fields U(-y)=U(y). For sigma=diag(1,1,-1) it excludes the corresponding horizontal-odd, vertical-even reflection class. These remain symmetry-conditional statements and are not imposed on the target class.

## Mean-swirl representation

The exact angular-momentum equation is

    (1-2c)Gamma+(cy-omega Jy+U) dot grad Gamma=-partial_theta P.

Average it equivariantly. The angular derivatives of Gamma and P average to zero. Divergence-free U and the product decomposition give

    (1-2c)Gamma0+Bbar dot grad Gamma0=-div E.

All fields here are defined globally in Cartesian coordinates; cylindrical coordinate singularities play no role. Ubar is C2, divergence-free and uniformly sublinear. Consequently Bbar has a complete flow with compact backward orbits by the same radial estimate as A006. Both Gamma0 and div E are bounded on each such orbit closure. Multiplying the scalar equation along it by exp((1-2c)*s), then integrating from minus infinity to zero, gives the claimed absolutely convergent integral. This argument uses the mean flow Bbar, not the full B-flow and not the frozen vorticity flow.
