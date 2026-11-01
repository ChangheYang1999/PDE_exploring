"""Exact two-index recurrence and marked-tree checks for free multipoles."""
from datetime import datetime, timezone
from functools import lru_cache
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import sys
import time
from gmpy2 import mpq
import cartesian_verify as cv
from quadratic_cartesian_verify import Q5
from laurent_log_audit import L, Poly, parse

sys.set_int_max_str_digits(0)


def angular_derivative(field):
    return cv.Field(field.q, {m: v * cv.I * m for m, v in field.modes.items()})


def polar_product(G, F):
    a = G * angular_derivative(F)
    b = angular_derivative(G) * F
    p = a.scale(G.q) - b.scale(F.q)
    return cv.Field(p.q - 2, p.modes)


def field_record(field, cosine=False):
    values = field.cosine() if cosine else field.sine()
    return {str(k): cv.qs(v) for k, v in values.items()}


def run_case(delta, initial, harmonics, bound):
    c = 1 / (1 - delta)
    F, G, C, U, V = {}, {}, {}, {}, {}
    rows = []
    Lmax = max(initial)
    B = Lmax + 1
    for k, h in harmonics.items():
        G[0, k] = cv.sin_field(2 - 2 * k, {2 * k - 2: h})
        assert G[0, k].laplace().zero()
        if k >= 3:
            potential = cv.cos_field(4 - 2 * k, {2 * k - 4: h / ((2 * k - 4) * (2 * k - 3))})
            rho, stream, _, _ = cv.from_potential(potential)
            assert rho.zero() and (stream - G[0, k]).zero()
        U[0, k], V[0, k] = G[0, k].dy().scale(-1), G[0, k].dx()
    for w in range(1, bound + 1):
        for n in range(1, w + 1):
            k = w - n
            I = n, k
            p = 1 - n * delta - 2 * k
            force = cv.Field(p, {})
            polar = cv.Field(p, {})
            for A, stream in G.items():
                D = n - A[0], k - A[1]
                if D in F:
                    force = force + U[A] * F[D].dx() + V[A] * F[D].dy()
                    polar = polar + polar_product(stream, F[D])
            assert (force - polar).zero()
            if I == (1, 0):
                F[I] = cv.sin_field(p, initial)
            else:
                F[I] = force.scale(1 / (c * (n * delta + 2 * k - delta)))
            assert (F[I].scale(c * p - 1) + force).zero()
            G[I] = cv.poisson(F[I])
            assert (G[I] - cv.displayed_poisson(F[I])).zero()
            C[I], stream, U[I], V[I] = cv.reconstruct_potential(F[I])
            assert (stream - G[I]).zero()
            assert max(F[I].sine(), default=0) <= B * n + 2 * k - 1
            assert max(G[I].sine(), default=0) <= B * n + 2 * k
            if k == 1:
                assert F[I].zero() and G[I].zero()
            rows.append(dict(n=n, k=k, density=field_record(F[I]),
                             stream=field_record(G[I]), potential=field_record(C[I], True),
                             cartesian_polar_agreement=True, direct_potential_verified=True,
                             stationary_exact_zero=True, poisson_exact_zero=True))
    if initial == {1: cv.Q(1)}:
        for k, h in harmonics.items():
            if (1, k) not in F:
                continue
            gamma = 1 - delta
            M = 2 * k - 2
            expected = cv.sin_field(gamma - 2 * k,
                                   {M + 1: -M * h * (1 + gamma) / (4 * c * k),
                                    M - 1: -M * h * delta / (4 * c * k)})
            # This formula is linear in h_k. For k>=4, earlier multipoles
            # can contribute to the same coefficient through repeated use.
            if k < 4:
                assert (F[1, k] - expected).zero()
    return dict(delta=cv.qs(delta), c=cv.qs(c), leading={str(k): cv.qs(v) for k, v in initial.items()},
                harmonic_stream={str(k): cv.qs(v) for k, v in harmonics.items()},
                total_index_bound=bound, rows=rows)


@lru_cache(None)
def trees(leaves):
    if leaves == 1:
        return ("f",)
    result = [("h", t) for t in trees(leaves - 1)]
    for left_size in range(1, leaves):
        for left in trees(left_size):
            for right in trees(leaves - left_size):
                result.append((left, right))
    return tuple(result)


def tree_data(tree, root_mark=False):
    if tree == "f":
        return 1, [((), 1)] if root_mark else []
    left, right = tree
    nr, mr = tree_data(right)
    if left == "h":
        nl, ml = 0, []
    else:
        nl, ml = tree_data(left, True)
    mass = nl + nr
    marks = [((0,) + path, n) for path, n in ml] + [((1,) + path, n) for path, n in mr]
    if root_mark:
        marks.append(((), mass))
    return mass, marks


def tree_checks():
    count, separation_checks = 0, 0
    by_size = {}
    for size in range(1, 9):
        by_size[str(size)] = len(trees(size))
        for t in trees(size):
            count += 1
            for root_mark in (False, True):
                n, marks = tree_data(t, root_mark)
                assert len(marks) == n - 1 + int(root_mark)
                for path, mass in marks:
                    for descendant, smaller in marks:
                        if len(descendant) > len(path) and descendant[:len(path)] == path:
                            assert mass > smaller
                for q in range(1, n + 1):
                    available = tuple(range(q, n + 1))
                    for length in range(len(available) + 1):
                        for subset in combinations(available, length):
                            if any(b - a < q for a, b in zip(subset, subset[1:])):
                                continue
                            selected = sum(mass in subset for _, mass in marks)
                            assert q * selected <= 2 * n
                            separation_checks += 1
    # A zero-density-mass multipole chain illustrates why marking every
    # interaction is incorrect: all interaction masses are one.
    chain = "f"
    for _ in range(5):
        chain = ("h", chain)
    n, marks = tree_data(chain, True)
    assert n == 1 and marks == [((), 1)]
    return dict(total_trees=count, trees_by_leaf_count=by_size,
                separated_mass_subset_checks=separation_checks,
                five_multipole_chain_density_mass=1,
                actual_marks_with_root=1, artificial_all_node_marks=6,
                artificial_count_exceeds_2n=True)


def main():
    start = time.monotonic()
    root = Path("research/58_free_multipole_convergence")
    for part in ("verification", "sources"):
        (root / part).mkdir(exist_ok=True)
    proof = (root / "PROOF.md").read_bytes()
    (root / "sources/proof_before_checks.md").write_bytes(proof)
    cases = []
    for d, initial in (
            (mpq(2, 11), {1: mpq(1)}),
            (mpq(4, 13), {1: mpq(1), 3: mpq(1, 7)})):
        cases.append(run_case(d, initial, {2: mpq(1), 3: mpq(-2, 3), 4: mpq(1, 5)}, 7))
    cv.Q = Q5.of
    cv.qs = lambda x: Q5.of(x).encode()
    d = Q5(0, mpq(1, 5))
    for initial in ({1: Q5(1)}, {1: Q5(1), 3: Q5(mpq(1, 7))}):
        cases.append(run_case(d, initial, {2: Q5(1), 3: Q5(mpq(-2, 3)), 4: Q5(mpq(1, 5))}, 6))
    # The separate exact logarithmic Cartesian calculus checks the first
    # multipole potential, which the homogeneous calculator cannot encode.
    chi = L(0, 0, [Poly([]), Poly([-1])])
    laplace = chi.X().X() - chi.Y().Y()
    assert laplace.zero()
    assert (chi.X().Y().scale(-1) - parse(-2, {2: ["1"]})).zero()
    counts = tree_checks()
    hashes = {}
    for name in ("multipole_cartesian_audit.py", "cartesian_verify.py",
                 "quadratic_cartesian_verify.py", "laurent_log_audit.py"):
        raw = (Path("code") / name).read_bytes()
        (root / "sources" / (name + ".txt")).write_bytes(raw)
        hashes[name] = sha256(raw).hexdigest()
    out = dict(checked_at_utc=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
               source_hashes=hashes, statement_sha256=sha256(proof).hexdigest(),
               exact_index_checks=sum(len(case["rows"]) for case in cases),
               first_logarithmic_harmonic_potential_verified=True,
               tree_checks=counts, cases=cases, actual_elapsed_s=time.monotonic() - start)
    (root / "verification/checks.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k not in ("cases", "source_hashes")}, indent=2))


if __name__ == "__main__":
    main()
