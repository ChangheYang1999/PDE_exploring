# Lead check: for integer c, 4^d P_d(2j, a) is an integer polynomial in a with leading coefficient (-1)^d,
# so every rational root is an integer (rational root theorem).  Recursion as in r365_local.py.
import sympy as s
a=s.Symbol('a')
def Prec(c,l,d):
    D=c-1; Pl=[s.Integer(1),(c+1)*s.Integer(l)/2-a/4]
    for k in range(2,d+1):
        Q=((2*D*(l+2)-a)**2-16*D**2*(k-1)**2)/s.Integer(16)
        Pl.append(s.expand((c*l+D-a/2)*Pl[k-1]-Q*Pl[k-2]))
    return Pl[d]
ok=True; nroots=0
for c in (2,3,4,7):
    for j in range(1,9):
        for d in range(1,j+2):
            p=s.Poly(s.expand(4**d*Prec(c,2*j,d)),a)
            ok&= all(cf.is_integer for cf in p.all_coeffs()) and p.LC()==(-1)**d
            for rt in s.Poly(p,a).ground_roots(): nroots+=1; ok&= rt.is_integer
print('integer coefficients, leading (-1)^d, rational roots integral (c in 2,3,4,7; j<=8; d<=j+1):',ok,'rational roots found:',nroots)
