"""Independent rational far-field coefficients for scaled radial generators."""
from flint import fmpq as Q, fmpq_poly as Poly

V = Poly([0,1])

def choose(a, k):
    answer = Q(1)
    for j in range(k):
        answer *= (a-j)/(j+1)
    return answer


def homogenized_legendre(n):
    if n == 0:
        return Poly([1])
    previous, current = Poly([1]), 1-V
    for k in range(1,n):
        previous,current = current, ((2*k+1)*(1-V)*current-k*(1+V)**2*previous)/(k+1)
    return current


def coefficients(p,m,w,n,Qd,R,order):
    assert min(m,w,n,Qd,order) >= 0 and R > 0
    a = homogenized_legendre(n)(R*R*V)
    result = [Q(0)]*(order+1)
    if Qd > order:
        return result
    first = [choose(p-m,k) for k in range(order-Qd+1)]
    second = [choose(Q(-w-Qd-n),k)*R**(2*k) for k in range(order-Qd+1)]
    for k in range(order-Qd+1):
        result[k+Qd] = R**(2*Qd)*sum((a[h]*first[j]*second[k-h-j]
                            for h in range(min(k,a.degree())+1)
                            for j in range(k-h+1)),Q(0))
    return result
