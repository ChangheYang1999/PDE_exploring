# Exact limiting response for sin9 at delta4/7

Status: exact limit CONFIRMED in V544. No new convergence theorem is asserted.

## Statement and notation

Let delta=4/7 and f_1(theta)=sin(9theta). Use the stationary density and stream recurrence of01 and the tuned-response convention of131. For the free stream harmonic at order7k, let sigma_k be its linear contribution to the next forbidden density coefficient at7(k+1). The compact response of232 satisfies sigma_k=S(1/(4k-2)) whenever the positive and negative carriers are separated. Its limiting value is S(0). We compute S(0) by an exact rational recurrence and compare it with the stored directed point enclosure in231. A fit on finitely many k is not a proof of its limiting value.

## Exact finite argument

Use the signed Laurent convention of01: a sine coefficient a at mode m is encoded by a(z^m-z^-m)/2. The artificial Cartesian derivatives X,Y encode partial_x and partial_y/i with the common angular factors already accounted for. Generate f_r for1<=r<=7 and g_r for1<=r<7 by exact rational Cartesian differentiation and convolution. Put A_r=Xf_r+Yf_r and C_r=Xg_r+Yg_r.

After translation to the high positive carrier, the normalized limiting derivatives at t=0 satisfy X_high V=-zV and Y_high V=zV. The unit carrier has derivatives -z/2,z/2. Therefore the linearized density and stream responses satisfy

    U_r=(1-delta) z[-A_r/2
                   -sum_(s=1)^(r-1) V_s A_(r-s)
                   +sum_(s=1)^(r-1) U_s C_(r-s)],
    [z^(v+1)]V_r=-[z^v]U_r/[2(v+1-delta*r)],  1<=r<7.

The denominator cannot vanish: 1<=r<7 and7 does not divide4r. The negative shifted Poisson branch carries an explicit factor t and vanishes at t=0. These identities are obtained by inserting the displayed high derivative formulas directly into Xg Yf-Yg Xf and taking the Poisson inverse. Consequently

    S(0)=2 [z^3] U_7.

All terms are finite rational Laurent polynomials. Exact rational convolution and extraction give the exact limit; no asymptotic extrapolation is involved. The compact formula is analytic near zero because its finitely many denominators are nonzero there. Thus S(1/(4k-2)) tends to this rational number as k tends to infinity.

## Checks and scope

Independently initialize the exact prefix with the Cartesian rational implementation, verify its Poisson identities, evaluate the above t=0 recurrence using rational dictionaries, and compare each low prefix coefficient and the final limit against a fresh1536-bit compact-response calculation. Check containment in the original1024-bit point enclosure. Retain the exact rational limit, interval comparisons, operation counts, source hashes and actual time. Compare the interval with the proposed fitted range[5e-9,9e-8] as an exact rational interval. A mismatch refutes that range as a rigorous enclosure of the limit; it does not refute the archived finite floating observations or the convergent tuned-series theorem.

Dependencies:01,131,231,232,233. The proof does not assert a growth law for the tuned harmonics H_(7k), since their numerator obstruction also varies with k.

## Completed exact computation

V544 at 2026-10-31T19:22:20+00:00 gives

    S(0)=82651586141768218752124086777/415161675019179052311193843662848000
        =1.99082890148639075578687942292315115899...e-7.

All304 prefix-coefficient comparisons pass. The independent rational limiting recurrence uses4,360 scalar products. Its value is contained in the retained1024-bit enclosure and overlaps the fresh1536-bit compact evaluation. It is strictly larger than9e-8, so the earlier fitted range[5e-9,9e-8] cannot enclose the actual limit. Arithmetic took0.13818seconds. The previously admitted all-index response bound and convergence theorem remain valid.
