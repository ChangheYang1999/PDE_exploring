"""Pressure-operator eigenvalues of SPEC 3.4: lambda(l, m) = (-2 alpha + i m omega/c_l)(1 - 2 alpha + i m omega/c_l) - l(l+1)."""
import math


def pressure_eigenvalues(c_l, omega, L, m_parity="even"):
    alpha = (1 - c_l) / c_l
    out = {}
    for l in range(0, L + 1):
        for m in range(0, l + 1):
            if m_parity == "even" and m % 2:
                continue
            z = complex(-2 * alpha, m * omega / c_l) * complex(1 - 2 * alpha, m * omega / c_l) - l * (l + 1)
            out[(l, m)] = z
    return out


def min_pressure_eigenvalue(c_l, omega, L, m_parity="even"):
    ev = pressure_eigenvalues(c_l, omega, L, m_parity)
    (l, m), z = min(ev.items(), key=lambda kv: abs(kv[1]))
    return dict(min_abs=abs(z), l=l, m=m, value=[z.real, z.imag])
