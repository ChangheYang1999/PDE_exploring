# Independent polar reproduction of the loose high-angular probe

## Claim and assumptions

Use the exact candidate013, the real S1 L2 correction class, canonical
velocity and compact-cutoff weak identity specified in
../high_power_weak_probe/PROOF.md. Put N=21, K=522,
t=r^2/(1+r^2), v=1-t, and phi=r v^2 t^K sin(N theta).
The peer N4-200 uses the looser denominator A+B+C and a larger gradient
bound H. We reproduce that denominator from the independent polar
potential reconstruction, then compare the complete pairing, all three
terms, their sum and the resulting radius. A match validates the peer's
particular weaker distance; it does not by itself validate the sharper
combined norm of T4-255.

## Polar formula

The independently derived finite expansions are

    rho=r sum_(j,n) v^a_j R_jn(t) sin(n theta),
    psi=r^2 sum_(j,n) v^a_j S_jn(t) sin(n theta),
    a_j=(j+1)delta/2, delta=1-1/c.

Let T_d(P,a,d)=(d-2at)P+2tvP'. Then

    u_r=-r sum n v^a_j S_jn cos(n theta),
    u_theta=r sum v^a_j T_d(S_jn,a_j,2) sin(n theta),
    rho_r=sum v^a_j T_d(R_jn,a_j,1) sin(n theta),
    rho_theta/r=sum n v^a_j R_jn cos(n theta).

All frequencies here are positive. Set Q=(2K+1)-(2K+4)t. The two
components of grad phi are v^2 t^K Q sin(N theta) and
v^2 t^K N cos(N theta). The exact drift polynomial is
A0=(2c+1)+cQ. Angular orthogonality and r dr=dt/(2v^2) give

    A^2=(pi/2) integral t^(2K+1) v A0^2 dt.

For ordered pairs of terms of equal angular frequency n, form

    U_jk=n^2 S_jn S_kn+T_d(S_jn) T_d(S_kn),
    G_jk=T_d(R_jn) T_d(R_kn)+n^2 R_jn R_kn.

The peer's bounds are exactly

    B^2=(pi/2) sum_(j,k,n) integral t^(2K+1)
                              v^(1+a_j+a_k) U_jk (Q^2+N^2) dt,
    C^2=(pi/2) sum_(j,k,n) integral t^(2K+1)
                              v^(1+a_j+a_k) G_jk dt.

Indeed |grad phi|^2<=v^4 t^(2K)(Q^2+N^2) and
|phi|^2<=r^2 v^4 t^(2K). These upper bounds retain the complete background
angular energy. Cross terms between unequal frequencies integrate to
zero; every ordered equal-frequency pair is retained. The signed
pairing is independently computed in T4-255 directly and by parts and
must match the peer's complete Cartesian projection.

The bound max(|Q|,N)<=max(2K+1,3) follows from N<=2K+1. Since
max t^K(1-t)^2=4K^K/(K+2)^(K+2), the exact rational

    H=max(2K+1,3) 4K^K/(K+2)^(K+2)

bounds the full gradient. The necessary radius is the positive root
2|I|/(D+sqrt(D^2+4H|I|)), D=A+B+C. All scalar integrals are evaluated
through the positive beta recurrence proved in T4-255; endpoints have
exponent greater than -1. Exact source hashes bind both calculations
to the same raw generator file.

## Status and limits

This is a comparison of two distinct Cartesian and polar assemblies,
including different radial integration orders. The source and output
checks are recorded in verification/result.json. No approximate mesh,
far-field cutoff or inferred cancellation is used. It supplies a
necessary correction distance only, not a residual upper bound or a
stationary solution.
