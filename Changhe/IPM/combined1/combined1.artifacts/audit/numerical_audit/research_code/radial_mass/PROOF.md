# Radial localization of exact residual mass

## Statement and hypotheses

Let F be an exact finite-generator S1 residual with the radial Fourier representation and endpoint checks in ../whole_plane_norms/PROOF.md. Assume F and rF belong to L2 on the full plane. For R>=0 define

T0(R)=integral_(|X|>=R) |F(X)|² dX,
T1(R)=integral_(|X|>=R) |X|² |F(X)|² dX.

The method below gives outward interval enclosures of both quantities for any exact rational R. Differences Tj(A)-Tj(B) enclose mass in A<=|X|<=B. The total norms are sqrt(T0(0)) and sqrt(T1(0)); the latter is only an upper proxy for Hdot^-1, not its value.

## Derivation

Put u=(1+r²)^(-1), U=(1+R²)^(-1). Exact full-circle angular orthogonality, including all cross terms within each harmonic, expresses the squared radial integrand for T0 as

(pi/2) sum_b u^b P_b(u) du,

with finite polynomials P_b and b>-1 after exact endpoint extraction. The b>-1 checks are made termwise for the actual diagonal branches; every cross exponent is the mean of two integrable diagonal exponents and is also greater than-1. This is the same expression as the independently checked whole-plane norm computation. If P_b(u)=sum_k p_(b,k)u^k, then

T0(R)=(pi/2) sum_(b,k) p_(b,k) U^(b+k+1)/(b+k+1).

The formula follows by integrating from0 toU. The point u=0 is r=infinity; no exterior region is omitted. For T1, replace each exponent b by b-1 and each P_b by(1-u)P_b. This is exactly multiplication by r²=(1-u)/u. The corresponding diagonal endpoint conditions are checked again.

Each coefficient is an exact rational before interval conversion. At a rational R, U is exact rational; rational positive powers are enclosed by Arb. Finite sums, products and differences are outward interval operations. Although individual polynomial terms can have either sign, their full sum is the nonnegative original squared field. A negative or inconclusive computed mass is therefore an arithmetic failure to be resolved, never discarded. Every reported annular mass has a nonnegative enclosure.

## Dependencies and scope

This result depends on the exact coefficient conversion, residual differentiation and angular integration in the cited proof. It uses no radial or angular quadrature and no asymptotic cutoff. The ratios of tail or annular mass to total mass are descriptive localization of these two norms only. They do not localize the nonlocal Hdot^-1 energy and do not constitute an existence certificate.
