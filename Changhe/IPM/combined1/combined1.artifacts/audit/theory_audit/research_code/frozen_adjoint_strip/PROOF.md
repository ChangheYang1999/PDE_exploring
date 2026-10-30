# The increasing frozen spectral strip is residual spectrum

Status: independent confirmation of the T2 theory worker the review of T4-145 Remark R1 for the natural frozen realization only. No transfer to a variable-coefficient adjoint domain is asserted.

## Exact statement

Let d>0, alpha real and B>0. On H=L2(R2,du dv), define

    A=-partial_u-d partial_v+W(v),
    W(v)=alpha+B p(v), p(v)=exp(2v)/(1+exp(2v)),
    D(A)={g in L2: (partial_u+d partial_v)g in L2 distributionally}.

This is the closed densely defined transport operator plus bounded multiplication. For every lambda=sigma+i tau with alpha<sigma<alpha+B, A-lambda is injective and bounded below but has nondense range. In fact ker(A*-conj(lambda)) is infinite-dimensional. Consequently lambda belongs to the spectrum but not the approximate point spectrum of A.

In the frozen IPM logarithmic chart, d=2c-2, alpha=q-c-1 and B=2q(c-1)-a0. The unitary chart in T4-145 identifies this statement with the frozen homogeneous Sobolev realization. It does not identify the adjoint of a separately chosen variable-coefficient or pinned operator.

## Proof by straightening transport

Make the determinant-one coordinate change

    r=u-v/d, z=v, g(u,v)=G(r,z).

Then partial_u+d partial_v=d partial_z. Thus A is unitarily equivalent to

    T=-d partial_z+W(z)

on L2(R_r;L2(R_z)), with domain consisting of L2 functions whose distributional z derivative is L2. Its adjoint is d partial_z+W(z) on the same domain.

For any f in L2(R_r), set

    G_f(r,z)=f(r) exp((conj(lambda)-alpha)z/d)
                         (1+exp(2z))^(-B/(2d)).

At negative infinity the modulus decays with exponent (sigma-alpha)/d>0; at positive infinity it decays with exponent (sigma-alpha-B)/d<0. The z derivative is a bounded multiplier of G_f, so G_f belongs to D(T*). Direct differentiation gives

    (T*-conj(lambda))G_f=0.

The map f to G_f is injective, proving the infinite-dimensional adjoint kernel and nondensity of the range of T-lambda.

It remains to justify the stronger statement that lambda is not an approximate eigenvalue. Put delta=sigma-alpha in (0,B). Multiplication by exp(-i tau z/d) reduces T-lambda to T-sigma. For a compact smooth scalar test h, integration by parts gives

    ||(-d partial_z+W-sigma)h||_2^2
      = d^2||h'||_2^2 + integral [(W-sigma)^2+d W'] |h|^2 dz.

The sign of the last term is positive: the cross term is -d integral(W-sigma)(|h|^2)' = d integral W'|h|^2. Since W'=2B p(1-p), the potential is

    V(p)=(Bp-delta)^2+2dB p(1-p), 0<=p<=1.

This polynomial is strictly positive on the compact interval. At p=0 and p=1 its values are delta^2 and (B-delta)^2, respectively; in the open interval its second summand is positive. Hence nu=min_[0,1] V>0. The identity yields

    ||(T-sigma)h||_2 >= sqrt(nu)||h||_2.

Density extends this estimate to the z-derivative domain; integration in r and the unitary phase change extend it to T-lambda. Therefore T-lambda, and hence A-lambda, is bounded below and injective. Its range is closed by closedness of T. The nonzero adjoint kernel already proves that this range is not dense, so no bounded inverse exists.

The proof confirms the peer's distinction between the two signs of B. For B>0 an adjoint obstruction supplies the interior spectrum. It does not supply a singular sequence for the operator itself. Extending this conclusion through shrinking to a variable-coefficient realization requires a justified adjoint test domain and adjoint convergence argument, neither of which follows from T4-145's primal-domain hypothesis.

Dependencies: the determinant-one change of variables, distributional first-derivative domains, integration by parts and Hilbert-space adjoints. No numerical computation or external spectral theorem is used.
