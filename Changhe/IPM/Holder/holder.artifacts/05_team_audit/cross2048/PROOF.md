# Finer cross-pole disk enclosure

## Statement and scope

Fix0<alpha<1 and the homogeneous Euclidean Holder seminorm. For increments of length1, put x=(1/2,0), y=-x. The trace-free kernels and the diagonal local term are those of ../../01_setup/PROOF.md. This note bounds only the smooth other-pole kernels on the two radius1/2 pole disks. It supplies no operator bound until combined with the accepted local projection, middle and exterior contributions.

For z=X+iY in B_(1/2)(1/2) with Y>0, let

    Q(z)=1/[2pi(z+1/2)^2],
    h=(2X)^alpha, v=(2Y)^alpha, d=(2|z|)^alpha.

At phase phi in[0,pi/2], define a=|Re Q(z)|cos phi and b=|Im Q(z)|sin phi. The exact four-point reflection plan of ../../08_improved_upper_bounds/reflection_orbits/PROOF.md has cost

    P(z,phi)=2 max{a h+b(d-h), a(d-v)+b v}.

The smooth cross contribution is bounded by

    X_alpha(phi)=integral_(B_(1/2)(1/2),Y>0) P(z,phi) dA(z).

The integral is finite because |z+1/2|>=1/2 on the closed disk. The full local identity term is outside this regular contribution. Scalar complex inputs obey the same bound by their absolute increment inequality.

The proposed refinement evaluates the six exponents1/5,3/10,1/2,3/4,9/10,99/100 at phases j*pi/32,0<=j<=16, with2048 cells in each integration coordinate. Only a completed independent acceptance record may supply numerical upper endpoints. At the time this proof was written the source had been frozen during the producer run; its output was not yet accepted.

## Rectangle enclosure and normalization

Write z=1/2+r exp(i theta), with0<=r<=1/2 and0<=theta<=pi. A radial cell has width1/(2n) and an angular cell widthpi/n. Its area element is r dr dtheta. On each closed rectangle, interval arithmetic encloses r,theta,z,Q, every nonnegative power, and both expressions in the maximum. Fractional powers at zero use the already audited nonnegative-range enclosure.

If V is the rectangle enclosure of the maximum without its prefactor2, its integral contribution is enclosed by

    r*pi*V/n^2,

because the coordinate-cell area is pi/(2n^2) and P=2V. This is exactly the prefactor in the frozen producer code. Summation over all0<=i,j<n covers the half disk; boundaries have measure zero. No principal value occurs in these smooth disks. Both signs and every reflected copy have already been incorporated in the four-point cost, so no additional symmetry factor is needed.

The frozen code is byte-for-byte identical to the V052 source used in the512-cell calculation. The only new inputs are n=2048 and the six selected exact rational exponents. It uses160-bit Arb intervals, all17 exact phase balls, and every rectangle. The radial loop has no adaptive omissions. The prelaunch record at11:52:35Z and the verifier snapshot record at12:11:56Z bind all four imported source files. A post-run comparison must check those hashes again.

## Independent checks and their limits

An independent Cartesian quadrature uses0<X<1 and0<Y<sqrt(X(1-X)). In real coordinates,

    Re Q=[(X+1/2)^2-Y^2]/[2pi((X+1/2)^2+Y^2)^2],
    Im Q=-(X+1/2)Y/[pi((X+1/2)^2+Y^2)^2].

Using these expressions avoids the producer's complex arithmetic and polar disk parameterization. Two Gaussian resolutions recompute every one of the102 nodal costs and must lie inside the saved interval enclosures. These are consistency diagnostics, not proofs of integral enclosure; the rectangle argument and verified interval code supply that proof. A selected interval replay or full rerun may be retained as additional evidence, with its exact scope stated.

For downstream recombination, parse the printed interval endpoints as exact decimal rationals and use their upper endpoints. The formatting may widen a ball, which remains safe. Do not replace these endpoints by a printed midpoint or a floating diagnostic. At every phase one may take the smaller of the old accepted upper endpoint and the newly accepted upper endpoint, since both bound the same functional. Add middle and exterior upper endpoints before applying the accepted unequal-node interpolation theorem. Add the uniform local projection and identity estimate afterward. A separately accepted strict projection saving can then be subtracted from that uniform local term, with no interaction with the cross-disk quadrature.
