# Separation of amplitude and normalized shape in a relative field distance

Status: an exact identity in a real Hilbert space. Numerical application to rounded quadrature norms remains an empirical diagnostic. No Euler solution claim follows.

Let H be a real Hilbert space, let u,v be nonzero elements of H, and let T_gamma be any family of linear isometries. Set a=||u||>0, b=||v||>0 and q=min(a,b)>0. Define

d(gamma)=||T_gamma u-v||/q,
h(gamma)=||T_gamma u/a-v/b||,
d_amp=|a-b|/q.

Then, for every gamma,

d(gamma)^2=d_amp^2+(ab/q^2)h(gamma)^2.

Proof. Write c=<T_gamma u,v>. Isometry gives d(gamma)^2=(a^2+b^2-2c)/q^2 and h(gamma)^2=2-2c/(ab). Substitution and (a-b)^2=a^2+b^2-2ab give the identity. Every denominator is positive by hypothesis.

The quantities d_amp and ab/q^2 are independent of gamma. Consequently the minimizing angle sets of d and h are equal whenever minima exist. Also h=0 if and only if T_gamma u/a=v/b. At that angle the entire distance d is caused by unequal amplitudes. Conversely d>d_amp if and only if the normalized shapes differ at that angle. Cauchy-Schwarz implies h^2 is in [0,4].

For example, for any unit vector e and c>1, u=c e and v=e have identical normalized shape but d=c-1. Thus even an arbitrarily large relative distance does not by itself imply a normalized shape difference. A rotation-invariant lower bound from norms alone cannot supply that implication either.

For the shell comparisons in this campaign, H=L2 of the shell with normalized volume measure and T_gamma is constant axial rotation of the vector field. The same statements hold for exactly rotation-invariant discrete quadrature, including the finite Fourier representation of ../axial_rotation/PROOF.md. The shell norms and optimized difference may be reconstructed from separate rounded numerical records, but then any rounding or quadrature discrepancy must be reported. A calculation using the producer's minimizing distance is not an independent field evaluation merely because its final scalar arithmetic is recomputed independently.

Dependencies: the Hilbert-space inner product, the equality case of a norm, Cauchy-Schwarz, and the rotation-isometry proof in ../axial_rotation/PROOF.md. This decomposition changes no registered branch threshold or gauge.
