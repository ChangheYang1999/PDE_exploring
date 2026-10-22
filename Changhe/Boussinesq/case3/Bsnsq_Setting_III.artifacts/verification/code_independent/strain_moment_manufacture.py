"""Independent quadrature for packet34; no numerics-lane code imported.

The first calculation was performed inline at15:54Z. This source preserves
that calculation, including all radial scales, angular orders and tolerances.
A rerun writes a distinct result so the original evidence is retained.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad


def evaluate(length, angular_order):
    nodes, weights = leggauss(angular_order)
    angles = math.pi * (nodes + 1.0)
    weights = math.pi * weights
    cs, sn = np.cos(angles), np.sin(angles)

    def angular_integrals(radius):
        x, y = radius * cs, radius * sn
        expfactor = math.exp(-radius * radius / length**2)
        temperature = x * x * (1.0 + y) * expfactor
        temperature_x = 2.0 * x * (1.0 + y) * (1.0 - x*x/length**2) * expfactor
        phi = x*y / (math.pi * radius**4)
        direct = np.dot(weights, phi * temperature_x * radius)
        correct = np.dot(weights, temperature * np.sin(3.0*angles) / (math.pi * radius**2))
        wrong = np.dot(weights, temperature * np.sin(3.0*angles) / (math.pi * radius))
        return direct, correct, wrong

    values, estimates = [], []
    for component in range(3):
        value, error = quad(lambda r: angular_integrals(r)[component], 0.0, np.inf,
                            epsabs=1e-12, epsrel=1e-12, limit=300)
        values.append(float(value))
        estimates.append(float(error))
    return {'L':length,'angular_order':angular_order,
            'direct':values[0], 'correct_polar':values[1], 'erroneous_polar':values[2],
            'expected':length**2/8.0, 'wrong_expected':length**3*math.sqrt(math.pi)/16.0,
            'radial_quad_error_estimates':estimates}


if __name__ == '__main__':
    rows=[evaluate(length, order) for length in (0.5, 1.0, 2.0) for order in (32, 64, 128)]
    result={'utc':datetime.now(timezone.utc).isoformat(),
            'method':'Own Gauss angular quadrature and adaptive radial quadrature; independent of num code',
            'rows':rows}
    output=Path('research/34_center_strain_moment/verification/manufactured_rerun.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
