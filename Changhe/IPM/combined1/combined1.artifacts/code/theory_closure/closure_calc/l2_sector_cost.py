"""Far-field cost of an exact sector in the L2 component versus the Hdot^-1 component (c1-t1, theory_v01).

Sector F = r^e E(theta) exactly on r > T, E odd in y, full-circle angular norm A = ||E||_(L2(0,2pi)).
  L2 (exact):   ||F||_(L2(r>T))^2 = A^2 T^(2e+2)/(-2e-2), e < -1, so G0 >= A T^(e+1)/sqrt(-2e-2).
  Hdot^-1 (T4-014, CLAIMED c1-t4): for E = sum_(n in I) a_n sin(n theta), sigma = -2-e > 0, N = max I,
                ||F||_H >= A T^(-sigma)/(sqrt(2 sigma)(N + sigma)).
Sector exponents e(h,k) = gamma - h delta - 2k (state 131 exponents; (h,0) principal, (h,1) first descendants).
Tolerances (component requirements of the registered frameworks): see TOL below.
Section 5 uses the fixed-sector norms E_n of c1-n4 l2_family_floor/verification/floors.json (sha256 29ddfd1c...,
CONFIRMED by T4-027), copied below to 9 digits.
Usage: python3 -B l2_sector_cost.py > l2_sector_cost.out
"""
import math

c = 4076476460239181 / 2 ** 51
gam = 1 / c
dl = 1 - gam
# T4-019: X_s(F) >= (1 - 34 s) 512 G0 at s = 2^-17; rebal: N_s(F) >= (1 - 34 s) 512 sqrt(20/21) H at s = 2^-16
TOL0 = {"T4-019 scalar (G0 <= eta/(512(1-34s)))": 1 / 163840 / (512 * (1 - 34 / 2 ** 17)),
        "gradedL2 c1-t1 box (gamma_0 <= 3.4774e-8)": 3.47739e-8}
TOLH = {"FW-T-TB-rebal-v1 (H <= 1.8332e-8)": 3 / 327680 / ((1 - 34 / 2 ** 16) * 512 * math.sqrt(20 / 21)),
        "graded c1-t1 box (gamma_H <= 3.5378e-8)": 3.53781e-8}
print(f"gamma = {gam:.6f}, delta = {dl:.6f}")
print()
print("1. Exponents and L2 membership of the sectors (h,k), e = gamma - h delta - 2k")
secs = sorted(((gam - h * dl - 2 * k, h, k) for h in range(0, 9) for k in range(0, 2)), reverse=True)
for e, h, k in secs:
    if e < -3.2:
        continue
    mem = "must vanish (not in L2)" if e >= -1 else "in L2"
    memH = "must vanish (not in Hdot^-1)" if e >= -2 else "in Hdot^-1"
    print(f"  ({h},{k}): e = {e:8.4f}   L2 route: {mem:24s}  H routes: {memH}")
print()
print("2. Largest full-circle amplitude A of a surviving sector with exact onset T, L2 component only")
print("   A_max = tol * sqrt(-2e-2) * T^(-(e+1))")
for name, tol in TOL0.items():
    print("  ", name)
    for e, h, k in secs:
        if -3.2 < e < -1:
            print(f"     ({h},{k}) e={e:7.4f}: " + "  ".join(f"T={T:>5}: {tol * math.sqrt(-2 * e - 2) * T ** (-(e + 1)):9.3e}" for T in (10, 100, 1000)))
print()
print("3. Necessary onset radius T for the known fixed sectors")
known = [("six-branch fixed (6,0)", gam - 6 * dl, 3081.27), ("seven-branch fixed (7,0)", gam - 7 * dl, 9679.97),
         ("b6 first surviving (2,1)", gam - 2 * dl - 2, 5042.13)]
for lab, e, A in known:
    print(f"  {lab}: e = {e:.4f}, A = {A}")
    for name, tol in TOL0.items():
        T = (A / (tol * math.sqrt(-2 * e - 2))) ** (1 / (-(e + 1)))
        print(f"     L2 [{name}]: T >= {T:.3e}")
    sig = -2 - e
    for name, tol in TOLH.items():
        for N in (1, 39):
            T = (A / (tol * math.sqrt(2 * sig) * (N + sig))) ** (1 / sig)
            print(f"     H  [{name}], N = {N:2d}: T >= {T:.3e}")
print()
print("4. Decay rates of the exterior contribution: L2 ~ T^(e+1), H ~ T^(e+2) (T4-014)")
for n in (4, 5, 6, 7):
    e = gam - n * dl
    print(f"  fixed sector after {n} stationary branches: ({n},0), e = {e:.4f}: L2 exponent {e + 1:.4f}; H exponent "
          + (f"{e + 2:.4f}" if e < -2 else "not in Hdot^-1"))

print()
print("5. Fixed sector after n stationary principal branches: exterior cost on r > T (sector exact there)")
print("   L2:  G0_ext(T) = E T^(e+1)/sqrt(-2e-2) (exact identity);  H: T4-014 LB E T^(e+2)/(sqrt(2 sigma)(N+sigma)), N = max harmonic,")
print("        and the parity-Hardy UB E T^(e+2)/sqrt(-2e-4) (A2 P7.7 applied to the exterior piece; HEURISTIC as a cost of F)")
EN = {4: 345.672183, 5: 1045.34677, 6: 3081.27440, 7: 9679.96558, 8: 35192.4228}
for n, E in EN.items():
    e = gam - n * dl
    print(f"  n = {n}: sector ({n},0), e = {e:.4f}, E_n = {E:.6g}")
    print("     L2 cost G0_ext(T): " + "  ".join(f"T={T:>5}: {E * T ** (e + 1) / math.sqrt(-2 * e - 2):9.3e}" for T in (10, 100, 1000)))
    for name, tol in TOL0.items():
        T = (E / (tol * math.sqrt(-2 * e - 2))) ** (1 / (-(e + 1)))
        print(f"     L2 T_min [{name}]: {T:.3e}")
    if e >= -2:
        print("     H cost: infinite (sector not in Hdot^-1; H frameworks require it to vanish exactly)")
        continue
    sig = -2 - e
    for N in (1, 39, 159):
        print(f"     H LB (T4-014, N = {N:3d}): " + "  ".join(f"T={T:>5}: {E * T ** (-sig) / (math.sqrt(2 * sig) * (N + sig)):9.3e}" for T in (10, 100, 1000)))
    print("     H UB (Hardy):         " + "  ".join(f"T={T:>5}: {E * T ** (-sig) / math.sqrt(2 * sig):9.3e}" for T in (10, 100, 1000)))
    for name, tol in TOLH.items():
        for N in (1, 159):
            T = (E / (tol * math.sqrt(2 * sig) * (N + sig))) ** (1 / sig)
            print(f"     H T_min [{name}], N = {N:3d}: {T:.3e}")

print()
print("6. Branches 9..12 (L2 only): E_n = 2 x quarter n(c_l-1)||G_n|| from c1-n1 numerics_v01 section 3")
print("   (FLOAT print of an EXACT recursion, 5-6 digits, PENDING-N4); same exact tail identity as section 5")
EN2 = {9: 2 * 314247, 10: 2 * 455376, 11: 2 * 1.7933e6, 12: 2 * 5.3698e6}
for n, E in EN2.items():
    e = gam - n * dl
    line = f"  n = {n:2d}: e = {e:.4f}, E_n = {E:.5g}, G0_ext T=100: {E * 100 ** (e + 1) / math.sqrt(-2 * e - 2):9.3e}"
    for name, tol in TOL0.items():
        T = (E / (tol * math.sqrt(-2 * e - 2))) ** (1 / (-(e + 1)))
        line += f"; T_min[{name.split(' (')[0]}] = {T:.3e}"
    print(line)

print()
print("7. Candidate C1-N1-003-8branch-frf (c1-n4 N4-044 CONFIRMED structure): pure-exterior-power model, L2 only")
print("   (the identity is exact for a pure exterior power; it is not a lower bound for a full residual, N4-041)")
for lab, h, k, E in (("(3,1)", 3, 1, 11957.6685869645), ("(8,0)", 8, 0, 35192.4228046200)):
    e = gam - h * dl - 2 * k
    line = f"  sector {lab}: e = {e:.6f}, E = {E:.10g}, G0_ext T=100: {E * 100 ** (e + 1) / math.sqrt(-2 * e - 2):.4e}," \
           f" T=1e4: {E * 1e4 ** (e + 1) / math.sqrt(-2 * e - 2):.4e}"
    for name, tol in TOL0.items():
        T = (E / (tol * math.sqrt(-2 * e - 2))) ** (1 / (-(e + 1)))
        line += f"; T_min[{name.split(' (')[0]}] = {T:.3e}"
    print(line)
print("   numerics_v01 R = 1e4 list check (N = n - 1 branches cancelled, sector (n,0), full circle):")
for n in (4, 5, 6, 7, 8, 9, 10):
    E = EN[n] if n in EN else EN2[n]
    e = gam - n * dl
    print(f"   N = {n - 1}: G0_ext(1e4) = {E * 1e4 ** (e + 1) / math.sqrt(-2 * e - 2):.4e}")
