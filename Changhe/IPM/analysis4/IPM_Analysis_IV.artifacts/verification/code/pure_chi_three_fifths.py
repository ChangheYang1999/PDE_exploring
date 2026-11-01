"""Pure-potential reconstruction for delta=3/5, with Cartesian identity checks."""
from gmpy2 import mpq
from flint import arb
from pure_cartesian_ball import Field, ball


def cosine(degree, frequency, amplitude):
    if frequency == 0:
        return Field(degree, 0, [amplitude])
    values = [arb(0)] * (2*frequency+1)
    values[0] = values[-1] = amplitude/2
    return Field(degree, -frequency, values)


def reconstruct(n, density, stream):
    p = mpq(1)-mpq(3*n,5)
    q = p+1
    t = p+3
    assert density.degree == p and stream.degree == q and q != 0 and t != 0
    K = 2*n-1
    D = [arb(0)] * (K+2)
    for k in range(K, 0, -1):
        D[k] = (2*density.sine(2*k+1)-ball(q+2*k+2)*D[k+1])/ball(2*k-q)
    D[0] = (ball((q+2)/2)*D[1]-density.sine(1))/ball(q)
    potential = Field(t)
    resonance = None
    for k in range(K+1):
        denominator = t*t-4*k*k
        if denominator:
            potential = potential + cosine(t, 2*k, D[k]/ball(denominator))
        else:
            assert D[k].contains(0), ('potential_resonance', n, k)
            assert t < 0 and k > 0 and n % 10 == 0
            resonance = 2*k
    if resonance is not None:
        particular_stream = potential.derivative().derivative(True).scale(-1)
        target = resonance+2
        correction = (stream.sine(target)-particular_stream.sine(target))/ball(mpq(resonance*(resonance+1)))
        potential = potential + cosine(t, resonance, correction)
    laplacian = potential.derivative().derivative()-potential.derivative(True).derivative(True)
    density_residual = laplacian.derivative(True)-density
    stream_residual = potential.derivative().derivative(True).scale(-1)-stream
    counts = dict(density=0, stream=0, resonant_coordinate=int(resonance is not None))
    for label, residual in [('density', density_residual), ('stream', stream_residual)]:
        for j, value in enumerate(residual.poly.coeffs()):
            assert value.contains(0), ('chi_identity', n, label, residual.lo+j, value.str(30))
            counts[label] += 1
    norm = abs(potential.coefficient(0)) + potential.norm()
    return potential, norm, counts
