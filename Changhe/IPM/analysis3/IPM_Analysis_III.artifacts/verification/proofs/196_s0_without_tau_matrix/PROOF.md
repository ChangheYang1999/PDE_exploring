# Independent S0 matrix bound after deleting TAU

## Exact conditional theorem

Take the immutable S0_M4_s60_o12 export audited in proof 62. It has169 ordinary conforming columns, a separate TAU column,12 angular output modes and69 radial test functions. Assume that every exported interval contains the exact pairing identified in the export metadata. Remove TAU and retain all169 ordinary columns, including the J coordinate and their exact KP compensation. In the domain and test norms of that metadata, the projected finite operator has smallest singular value at least4137/200000=0.020685, provided the interval positivity checks specified below pass.

This is a conditional matrix theorem. The premise that the exported entries enclose the original-data exact continuum pairings is not established by this calculation. No inverse for the infinite-dimensional complement is obtained. In particular, the continuum realization of S0 is already obstructed by proof 36.

## Exact reduction of the exported Grams

Let G and B_N be the full170-column matrices constructed in proof 62, and let H be the radial test Gram. With k exact, D=3/k+k c[KP] and d_j=-k c_j/D, G consists of the ordinary weighted domain Gram, the J and TAU scalar coordinates, and d d^T. B_N contains the ordinary pairings plus the compensation d_j times the KP pairing. Each B_N already contains its angular weight w_N=1+(2N+1)^2, so the projected image Gram is

 K=sum_(N=0)^11 B_N^T H^(-1) B_N / w_N.

Define the coordinate injection I:R^169 -> R^170 by I x=(x,0). Then the exact restricted Grams are G_r=I^T G I and K_r=I^T K I, and the restricted pairings are B_(r,N)=B_N I. No re-normalization or diagonal approximation is permitted. In particular the KP strain compensation on every retained column remains. TAU's cross pairings disappear because its coordinate is exactly zero.

The first and last radial test functions are identically zero in the represented support. As in proof 62, they can be deleted or replaced by isolated unit diagonal entries of H with zero pairing rows. These operations give identical projected norms on the active tests.

## Validated congruence

From exact dyadic midpoints choose invertible triangular matrices T and S approximating the inverse Cholesky transposes of G_r and H. Their diagonal entries must be nonzero. Calculate in outward ball arithmetic

 G_1=T^T G_r T, H_1=S^T H S,
 C_N=S^T B_(r,N) T,
 K_1=sum_N C_N^T H_1^(-1) C_N/w_N.

The checks ||G_1-I||_infinity<1 and ||H_1-I||_infinity<1 establish positive definiteness. Indeed every actual exact symmetric Gram inside the enclosure is within that induced norm of the identity, and its spectral radius is bounded by that norm. The interval inverse of H_1 encloses its exact inverse. Symmetrizing the enclosed expressions conservatively preserves every actual symmetric value.

Set s=4137/200000 exactly and M=K_1-s^2 G_1. A floating Cholesky factor of its midpoint is only a way to choose an exact dyadic invertible triangular matrix L. The accepting interval check is

 ||L^(-1) M L^(-T)-I||_infinity<1.

It proves M positive definite for every compatible exact entry choice and hence ||Q L_operator h||_Y >= s ||h||_X on the169-column space. All finite column combinations and projections are understood in the exact spaces defined by the metadata. The continuity of the original basis and original-data enclosure of its pairings remain distinct input hypotheses.

## Provenance and precision

The companion script is adapted from the verifier's independent decoder and interval-inversion proof in proof 62, with the coordinate restriction performed before whitening. It does not import the numerics team's certification code. Immutable copies of the metadata, dyadic matrix export and original no-TAU certificate are hashed. The original NPZ hash is checked against the metadata. The exact positive target s is supplied as a rational, rather than inferred from a shortened decimal in a report. Every accepting bound uses384-bit Arb, with100-digit approximate midpoint Cholesky choices whose errors are subsequently validated.

The archived one-team no-TAU certificate reports0.020684559081906594. Rounding it to0.020685 increases its lower endpoint and is not a valid outward rounding. Our target0.020685 must therefore be independently checked; it does not follow merely by rounding that archive. If the new check passes, the stronger conditional matrix statement is established directly. Failure would leave that target open. Neither outcome certifies the original operator pairings or the complement inverse.
