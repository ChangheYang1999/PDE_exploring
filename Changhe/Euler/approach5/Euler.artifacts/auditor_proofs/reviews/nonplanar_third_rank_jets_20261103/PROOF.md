# Nonplanar harmonic germs with vanishing rank derivatives through order four

Independent audit of LIT281. Status: CONFIRMED A2028-A2032; the proposed general pointwise obstruction is REFUTED A2033; global and higher-order extensions remain OPEN A2034. All seven source sections have been read. The stronger fourth-order rank vanishing follows from the parity argument already present in its Section 5. The source is pinned in the team records.

## 1. Exact claim

Fix 1/3<c<1/2 and any finite real omega. Set a=1-2c, d=1-c, b=2d, m=a/c, sigma=omega/c, q=b/a=2(m+1)/m and n=b/c=2m+2. Then 0<m<1, c=1/(m+2) and a=m/(m+2). Let Jx=e3 x x, X=(cI-omega J)x and L=dI+omega J.

There is an invariant cone C_delta={z=x3>0, sqrt(x1^2+x2^2)<delta z} and real-analytic harmonic f,Q there, with X.grad f=-af, X.grad Q=-bQ, f>0, grad f!=0, and Q not identically zero. At x*=e3, f=1 and D^2f is invertible. With

    E=|grad f|^2/a^2, S=Q-E, F=grad f x grad S,

there are fixed positive finite r_-,r_+ such that S<0 and r_-|S|<=E<=r_+|S| throughout the cone, and every derivative of F through order four vanishes at x*. In particular the third-order rank-jet condition alone does not extend the planar obstruction to nonplanar harmonic germs.

Moreover phi=-f/a+Q, U=grad phi and P=Q-|U|^2/2 solve the full profile equation LU+DU(X+U)+grad P=0, div U=0 on this cone. For all sufficiently large radii in the cone they have the exact natural decay with p=(1-c)/c=m+1:

    C1|x|^(-p)<=|U(x)|<=C2|x|^(-p),
    |DU(x)|<=C2|x|^(-p-1).

The constants and the aperture may depend on c and omega. No whole-space extension or supported-vorticity interface is asserted. The construction has curl U=0 on its domain.

## 2. Convergent harmonic modes

Write zeta=x1+i x2 and rho^2=x1^2+x2^2. For real M>0 and integer j>=0 define kappa_j=-M+i sigma j and

    H_j^(M)=zeta^j z^(kappa_j-j)
               sum_{k>=0} A_k (rho^2/z^2)^k,
    A_0=1,
    A_(k+1)=-(kappa_j-j-2k)(kappa_j-j-2k-1)
                   A_k/[4(k+1)(j+k+1)].                 (2)

Powers of z use the real logarithm on z>0. The consecutive coefficient ratio tends in modulus to one unless the series terminates. Thus the power series has radius at least one. On every compact subset of rho/z<1, its derivatives converge uniformly. One can see joint real analyticity directly by locally choosing the analytic logarithm of z and complexifying the convergent power series in x1,x2,z about any real point. There is no axis singularity: every term is a polynomial in x1,x2 times an analytic function of z.

The identity Delta_xy(zeta^j rho^(2k))=4k(j+k)zeta^j rho^(2k-2) makes the transverse Laplacian of one term cancel the z Laplacian of the preceding term under (2). Hence H_j^(M) is harmonic. Every summand has ordinary complex degree kappa_j and angular frequency j, so

    X.grad H_j^(M)=(c kappa_j-i omega j)H_j^(M)
                 =-cM H_j^(M).                         (3)

The j=0 mode is real. The lowest transverse term of the j-th mode is zeta^j z^(kappa_j-j); all others have higher transverse degree. These facts give exact analytic functions with the stated twisted homogeneity.

## 3. The root and the lower derivatives

Put h=m(m+1), and consider

    Psi(K)=-(m+1)^2 K^2+3(m+1)(m+2)K-2(m+2)^2
                                      +6sigma^2(2K-3).

Its values at 3/2 and 2 are (m-1)(m+5)/4<0 and 2m+6sigma^2>0. Its derivative on that interval is at least (m+1)(2-m)+12sigma^2>0. Thus there is a unique K in (3/2,2) with Psi(K)=0. Set

    t=sqrt(2K-3), alpha=(1+t)/2, beta=(1-t)/2,
    A2=-ht/4,
    f0=H_0^(m)+Re(A2 H_2^(m)).

Then 0<t<1 and alpha,beta>0. At e3,

    f0=1, g=grad f0=(0,0,-m),
    H=D^2 f0=h diag(-alpha,-beta,1).

For example the transverse quadratic coefficient of H_0^(m) is -h/4; the leading quadratic term of A2 H_2^(m) gives the eigenvalue split. The nonzero independent third derivatives are

    T113=h(m+2)alpha, T223=h(m+2)beta,
    T123=sigma ht, T333=-h(m+2).

The mixed sign follows by differentiating Re(A2 zeta^2 z^(-m-2+2i sigma)): at z=1 its x1x2z coefficient is -4sigma A2=sigma ht. Therefore

    |H|^2=h^2 K,
    |T|^2=h^2[(m+2)^2(3K-2)+6sigma^2 t^2],
    det H=h^3 alpha beta>0.                            (4)

Adding any real part of A4 H_4^(m) preserves every derivative through order three at e3.

## 4. Canceling the second jet of the harmonicity defect

For f with these lower jets define D=-(m+1)(m+2)K<0 and

    B=|grad f|^2/a^2+D f^q,
    G=Delta B=2|D^2f|^2/a^2
                         +Dq(q-1)f^(q-2)|grad f|^2.     (5)

Initially use f=f0; it is positive near e3, so noninteger powers cause no loss of analyticity. Since q(q-1)m^2=2(m+1)(m+2), equation (4) makes G(e3)=0. Transverse half-turn parity gives G_1=G_2=0. Homogeneity gives X.grad B=-bB and X.grad G=-2G. At the axis X=cz e3, so G_3=0; differentiating the same identity once then gives G_13=G_23=G_33=0. Thus only the transverse Hessian of G remains.

Write r=q-2=2/m and e=|g|^2=m^2. The harmonic identities are

    Delta |D^2f|^2=2|D^3f|^2,
    Delta(f^r|grad f|^2)=2f^r|D^2f|^2
        +r(r-1)f^(r-2)|grad f|^4
        +4r f^(r-1)grad f.D^2f grad f.

At e3, g.Hg=m^2h. Dividing Delta G by 4h^2/a^2 and inserting (4) gives

    (m+2)^2(3K-2)+6sigma^2(2K-3)
                   -K[(m+1)^2 K+3m+6]
      =Psi(K)=0.                                      (6)

This displays the algebraic cancellation explicitly. In particular the transverse Hessian M of the initial G is trace-free, and (6) is unchanged by adding a fourth mode, since it uses only derivatives of f through order three.

Let A4=A+iB4. The leading added quartic polynomial at e3 is

    A(x1^4-6x1^2x2^2+x2^4)
                        -4B4(x1^3x2-x1x2^3).

In D^2G only the first term of (5) changes: the change is (4/a^2)H_ab partial_abij of this polynomial. Since H11-H22=-ht, the transverse change is exactly

    -(96ht/a^2) [[A,-B4],[-B4,-A]].                     (7)

Take A=a^2 M11/(96ht) and B4=-a^2 M12/(96ht). The trace-free transverse Hessian is canceled, and all the normal components remain zero by homogeneity. For f=f0+Re(A4 H_4^(m)), this proves

    G(e3)=DG(e3)=D^2G(e3)=0.                           (8)

The denominator is nonzero for every allowed c and finite omega. Large coefficients only require shrinking the eventual cone; no uniform aperture was claimed.

## 5. An actual harmonic Q matching five scalar derivatives

Use the same mode family with M=n=2m+2 and seek

    Q=Q0 H_0^(n)+Re(Q2 H_2^(n)+Q4 H_4^(n)).             (9)

Every term has scalar weight b. For any residual R of that weight, homogeneity reads

    cz R_z+(cx1+omega x2)R_1+(cx2-omega x1)R_2=-bR.      (10)

At the axis this identity recursively expresses every jet with z derivatives through pure transverse jets of no greater order. More precisely, transverse differentiation of order j gives a linear combination of transverse jets of the same order on the right of the solved R_z equation; repeated z differentiation stays within that transverse order. Therefore vanishing of all transverse jets through a given order also makes all mixed jets through that order vanish.

First choose Q0=B(e3). The residual has zero value and all pure z derivatives. Its first transverse derivatives vanish by parity. Its quadratic transverse trace is zero by G(e3)=0, since its zz derivative is already zero. Thus its transverse quadratic polynomial is the real part of a multiple of zeta^2. Choose Q2 to cancel it, using the leading term of the second mode. All jets through order two now vanish; all pure transverse cubic jets vanish by parity, and (10) removes the remaining cubic jets.

For i,j transverse, equation (8) gives partial_ij Delta R=0. The term R_33ij is zero by (10) and the already canceled quadratic transverse jet. Thus the remaining quartic transverse polynomial is two-dimensional harmonic, and is the real part of a multiple of zeta^4. Choose Q4 to cancel it. Equation (10) cancels all mixed fourth derivatives. Consequently Q-B has zero jet through order four.

It has zero jet through order five as well. Its pure transverse fifth derivatives are zero by the same half-turn parity; all derivatives containing z follow from the matched lower transverse jets and (10). Therefore S-D f^q has zero jet through order five. Since grad f x grad(D f^q)=0 identically, every derivative of F=grad f x grad S through order four vanishes. This is a finite-jet conclusion; no identity S=D f^q on an open set has been deduced.

The harmonic Q is nonzero. If sigma!=0, let K0=(m+2)/(m+1). The sigma=0 part of Psi(K0) is zero, and 2K0-3=(1-m)/(m+1)>0. Thus Psi(K0)>0 and monotonicity gives K<K0. Then

    Q(e3)=B(e3)=(m+2)[(m+2)-(m+1)K]>0.

If sigma=0, K=K0 and D=-(m+2)^2, so Q(e3)=0. But direct second differentiation of B gives

    Q11(e3)-Q22(e3)=2m(m+1)(m+2)^2 t>0.

Indeed the difference of the energy derivatives is -2(m+1)(m+2)^2t, and that of D f^q is 2(m+1)^2(m+2)^2t; their sum is the displayed expression. The fourth mode has no effect on either of these second jets. Thus Q is nonzero in both cases.

## 6. Cone, full momentum and decay

At e3, f=1, E=(m+2)^2>0 and S=D<0. On a sufficiently small compact disk z=1, rho<=delta, these strict inequalities persist and E/|S| has positive finite bounds. The complete flow exp(t(cI-omega J)) preserves rho/z, crosses z=1 exactly once, and gives the exact scalar homogeneities. It therefore propagates the signs and comparison bounds to C_delta. This also gives grad f!=0. The invertible Hessian at e3 proves that f cannot be locally independent of a fixed Euclidean direction: such a direction would belong to the Hessian kernel.

For phi=-f/a+Q, U=grad phi and P=Q-|U|^2/2, use L-A^T=aI to get

    L grad phi+D^2phi X=grad(X.grad phi+a phi)=-grad Q,

because b-a=1. Harmonicity gives div U=0, and DU U=grad(|U|^2/2). These identities prove full momentum exactly.

With V=-grad f/a and Phi_t=exp(tA), differentiated homogeneity gives

    exp(tL)U(Phi_t x)=V(x)+exp(-t)grad Q(x),
    exp(bt)P(Phi_t x)=Q(x)-|V(x)+exp(-t)grad Q(x)|^2/2.

The compact section has a positive minimum of |V| and finite derivative bounds. The correction tends uniformly to zero there; hence the two-sided exterior bound for U and the derivative bound in Section 1 follow throughout the cone. Its pressure tail is P2=Q-E/2, so Q=P2+E/2 is precisely the harmonic remainder.

In the campaign interval 2/5<c<1/2, p=m+1<3/2. The cone has fixed positive solid angle, and the energy lower bound gives a divergent integral of r^(2-2p) over all large radii. Thus these sector profiles have infinite exterior energy. Nothing is claimed about the missing origin or angular complement.

## 7. Verification and limits

All seven source sections and every section of this independent proof were read. The series recurrence, lower jets, polynomial reduction (6), matrix coefficient (7), parity and normal-jet recurrence, nonzero Q and exact momentum were rederived by hand. No numerical calculation or source symbolic script was used. The existence proof is the convergent series construction, not its optional eleven-identity computation.

The example refutes a general nonplanar version of the planar pointwise obstruction with either third- or fourth-order rank vanishing alone. It leaves open still higher-order obstruction, actual matching at supported vorticity, global ranked tails and whole-space profiles. It does not contradict the earlier planar or Q=0 theorems: f is nonplanar and Q is nonzero. All conclusions hold for every fixed finite omega, with constants permitted to depend on omega.
