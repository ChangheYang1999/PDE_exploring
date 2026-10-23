"""Independent exact finite-part axis constant. Proof: hydrostatic_axis_core_moment/PROOF.md."""
import gmpy2
import mpmath as mp
Q=gmpy2.mpq

def cheb_to_w(coeff):
    out=[Q(0)]*len(coeff);old=[Q(1)]
    for j,c in enumerate(coeff):
        if j==0:cur=old
        elif j==1:cur=[Q(1),Q(-2)]
        else:
            nxt=[Q(0)]*(j+1)
            for k,v in enumerate(cur):nxt[k]+=2*v;nxt[k+1]-=4*v
            for k,v in enumerate(old):nxt[k]-=v
            old,cur=cur,nxt
        for k,v in enumerate(cur):out[k]+=Q(c)*v
    return out

def exactmp(v):
    v=Q(v);return mp.mpf(int(v.numerator))/int(v.denominator)

def horner(coeff,x):
    value=mp.mpf(0)
    for a in coeff[::-1]:value=value*x+a
    return value

def guard(coeff):
    bits=max([0]+[int(abs(t.numerator).bit_length()-t.denominator.bit_length()) for t in coeff if t])
    return int(bits*.30103)+30

def beta_moment(coeff,P,L):
    P=exactmp(P);L=exactmp(L)
    if not 1<P<2:raise ValueError('Finite m0 formula requires1<P<2')
    if coeff[0]!=0:raise ValueError('k(0) must vanish exactly')
    b=mp.beta(2-P,mp.mpf('.5'))/(2*(1-P));terms=[]
    for j in range(1,len(coeff)):
        terms.append(j*exactmp(coeff[j])*b)
        b*= (j-P)/(j-P+mp.mpf('1.5'))
    return L/2**P*mp.fsum(terms),mp.fsum(abs(v) for v in terms)

def integral_moment(coeff,P,L):
    P=exactmp(P);L=exactmp(L);a=list(map(exactmp,coeff));k1=a[1]
    polynomial=[j*a[j] for j in range(2,len(a))]
    def f(u):
        v=u**(1/(2-P));root=mp.sqrt(1-v)
        return (root*horner(polynomial,v)-k1/(root+1))/(2-P)
    return L/2**P*(mp.quad(f,[0,mp.mpf('.25'),mp.mpf('.75'),1])-k1/(P-1))

def logarithm_coefficient(coeff,P,L):
    if Q(P)!=2:raise ValueError('Logarithm formula requires exact P=2')
    return Q(L)/4*(coeff[2]-coeff[1]/4)

def endpoint_second(cheb):
    first=sum((j*j*Q(a)for j,a in enumerate(cheb)),Q(0))
    second=sum((Q(j*j*(j*j-1),3)*Q(a)for j,a in enumerate(cheb)),Q(0))
    return first,second
