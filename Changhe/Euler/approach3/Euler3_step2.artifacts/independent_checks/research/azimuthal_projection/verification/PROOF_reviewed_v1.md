# Exact azimuthal projection on a resolved finite Fourier grid

## Statement, hypotheses and notation

Let J(x,y,z)=(-y,x,0), let Q_phi=exp(phi J), and let U be a real C1 vector field on a neighborhood of the spheres used below. For positive radii r_i and polar cosines mu_j in (-1,1), define

    n_j(phi)=(sqrt(1-mu_j^2) cos(phi), sqrt(1-mu_j^2) sin(phi), mu_j),
    V_ij(phi)=Q_{-phi} U(r_i n_j(phi)).

Suppose each component of every V_ij is a trigonometric polynomial with frequencies |m|<=M, for a fixed nonnegative integer M. Let N be an integer with N>2M. At each polar node use the same N azimuthal nodes phi_k=2pi(k+eta)/N, where eta is any fixed real number. Let b_ij be nonnegative weights with sum b_ij=1. The result allows some zero weights. Put

    A_ij=(1/N) sum_k V_ij(phi_k),
    E=(1/N) sum_ijk b_ij |V_ij(phi_k)|^2,
    E_non=(1/N) sum_ijk b_ij |V_ij(phi_k)-A_ij|^2,
    G=(1/N) sum_ijk b_ij |DU(r_i n_j(phi_k)) J(r_i n_j(phi_k))
                                      - J U(r_i n_j(phi_k))|^2.

Then A_ij is the exact continuous azimuthal mean of V_ij. The three discrete energies equal their continuous azimuthal integrals at the selected radii and polar nodes. In particular

    0 <= E_non <= E,
    E_non <= G <= M^2 E_non.

If all nonzero frequencies are even, replace the lower bound by 4 E_non <= G. If E>0, define e=E_non/E and N_U=sqrt(G/E). These obey

    sqrt(e) <= N_U <= M sqrt(e),

with lower constant 2 for even nonzero frequencies. If E=0, all sampled values vanish at positive-weight nodes and the ratios are undefined; do not report them as zero.

These are exact statements in real arithmetic. They assert no accuracy of a finite radial or polar quadrature as an approximation to a three-dimensional integral.

## Proof

For every integer q with 0<|q|<N, the sum of exp(2pi i q k/N) over k=0,...,N-1 is zero, by the finite geometric-series formula. Multiplying by exp(2pi i q eta/N) does not change its vanishing. Consequently the uniform rule integrates exactly every trigonometric polynomial with frequencies strictly below N in absolute value. It integrates constants correctly as well.

The field V_ij has frequencies at most M, so the sampled mean is its exact constant coefficient. Each of |V_ij|^2 and |V_ij-A_ij|^2 has frequencies at most 2M<N and is also integrated exactly. Fourier orthogonality gives

    mean |V_ij|^2 = |A_ij|^2 + mean |V_ij-A_ij|^2.

This proves 0<=E_non<=E after multiplication by b_ij and summation.

By the chain rule and the commutation of J with Q_phi,

    V_ij'(phi)=Q_{-phi} [DU(r_i n_j(phi)) J(r_i n_j(phi))
                                          - J U(r_i n_j(phi))].

A rotation preserves the Euclidean norm. The derivative V_ij' has the same frequency support as V_ij, so its squared norm is integrated exactly by the uniform rule. Write v_ij,m for the complex vector Fourier coefficients. Parseval's identity, or direct integration of the finite sum, gives

    mean |V_ij-A_ij|^2 = sum_{m!=0} |v_ij,m|^2,
    mean |V_ij'|^2 = sum_{m!=0} m^2 |v_ij,m|^2.

Every contributing m has 1<=|m|<=M. Multiplying each summand by the bounds on m^2 proves the stated inequalities. If every nonzero m is even, m^2>=4. Nonnegative weighted summation preserves all inequalities. Division by E>0 and taking square roots completes the proof.

## Application to the finite rotating representation

The vector rotation action commutes with curl, with multiplication of a scalar potential by y, and with radial scalar factors. Therefore a toroidal or poloidal potential of azimuthal frequency m produces a vector field of frequency m under the corotating action used above. A radial twist changes the phase at fixed radius and does not change m. The finite reduced coefficient expansion has the same property, provided its elimination only mixes coefficients with the same m. Thus M may be taken from the largest active azimuthal index of all channels, including correction channels. The main angular degree alone is not sufficient for choosing M.

The coordinate system Q_{-phi} differs from spherical vector components at fixed mu only by a phi-independent orthogonal matrix. Its azimuthal means and squared norms therefore implement the same projection as averaging the spherical components.

## Dependencies and scope

The proof uses the chain rule, finite Fourier sums, orthogonality and nonnegative weights. The vector generator and representation invariance are proved separately in ../rotation_generator/PROOF.md. In a numerical implementation, nonuniform azimuthal weights, insufficient N, a wrong reshape order, or omitted correction modes invalidate the exactness argument. Tests must check the node order, weights and the full frequency bound. Finite-precision agreement is a diagnostic, not a bound on roundoff. No Euler equation, existence claim, tail-onset claim or global axisymmetry conclusion is inferred from sampled values. This result has not been formalized.
