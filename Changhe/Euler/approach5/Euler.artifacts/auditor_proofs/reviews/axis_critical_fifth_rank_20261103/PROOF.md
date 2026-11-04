# Axial fifth-order rank obstruction: independent audit

Status: CONFIRMED A2049-A2053 after a full six-section final read. Extensions in Section 6 remain OPEN A2054. LIT282 is a local obstruction in the explicit class below. Its exact-order consequence concerns the LIT281 examples only.

## 1. Exact hypotheses and finite-jet reduction

Fix 1/3<c<1/2 and omega in R. Set a=1-2c, b=2(1-c), m=a/c in (0,1), sigma=omega/c, q=b/a=2(m+1)/m. Thus c=1/(m+2) and a=m/(m+2). Let Jx=e3 cross x and X=(cI-omega J)x. Suppose f,Q are real analytic and harmonic in a neighborhood of x*=e3 and satisfy

    X.grad f=-af, X.grad Q=-bQ,
    f(x*)=1, partial_1 f(x*)=partial_2 f(x*)=0.

Assume the symmetric transverse block of D2f(x*) is negative definite with distinct eigenvalues. Define E=|grad f|^2/a^2, S=Q-E and F=grad f cross grad S. Then not every derivative of F of order at most five can vanish at x*. All statements refer to ordinary Cartesian derivatives.

Suppose otherwise. At x*, homogeneity gives f_3=-m!=0. In local coordinates (f,u,v), vanishing of the jet of df wedge dS through order five is equivalent to vanishing of every derivative of S of order at most six containing a u or v derivative. Indeed df is exactly the first coordinate differential, so the two-form coefficients are S_u,S_v. Finite jet vanishing is preserved by an analytic coordinate change and multiplication by its invertible Jacobian. Choose h so that its derivatives through order six at f=1 equal the remaining pure-f derivatives of S. Then S-h(f) has zero jet through order six.

The scalar homogeneity of E is X.grad E=-bE. This follows by differentiating f's equation: X.grad(grad f)=-(a+c)grad f-omega J grad f, and J is skew. Hence (X.grad+b)S=0. Applying this first-order operator to the six-jet remainder gives, through order five in f,

    a h^(j+1)(1)=(b-aj)h^(j)(1), j=0,...,5.

These are exactly the derivatives of h(f)=D f^q for a real D, locally where f>0. Thus Q-B has zero jet through order six for B=E+D f^q. Since Q is harmonic,

    G=Delta B has zero jet through order four.             (1)

This is a statement about finite jets, not a local functional identity S=D f^q.

## 2. Forced first three derivatives and the root constraint

Use a transverse rotation in SO(2) to diagonalize D2f on span(e1,e2); it commutes with J. Homogeneity determines the mixed normal entries and harmonicity fixes the transverse trace. With h0=m(m+1), an ordering of the distinct negative eigenvalues gives

    g=grad f=(0,0,-m),
    H=D2f=h0 diag(-alpha,-beta,1),
    alpha=(1+t)/2, beta=(1-t)/2, 0<t<1,
    K=(3+t^2)/2, |H|^2=h0^2 K.                             (2)

The equation G=2|H|^2/a^2+D q(q-1)f^(q-2)|g|^2 and G(x*)=0 imply

    D=-(m+1)(m+2)K.                                       (3)

Every derivative containing a normal index is determined from lower transverse jets by differentiating homogeneity. The free pure transverse cubic is harmonic, since its transverse traces are the negatives of the fixed normal derivatives, here zero. Write it as Re((A3+iB3)(x1+i x2)^3). It contributes T111=6A3,T122=-6A3,T112=-6B3,T222=6B3 to T=D3f. The transverse derivatives of G are

    G_1=-(24h0 t/a^2)A3, G_2=(24h0 t/a^2)B3.

The other terms vanish since g_i=H_3i=0 for i=1,2. Since t>0, (1) gives A3=B3=0. The nonzero entries of T, up to permutation, are therefore

    T113=h0(m+2)alpha, T223=h0(m+2)beta,
    T123=sigma h0t, T333=-h0(m+2),
    |T|^2=h0^2[(m+2)^2(3K-2)+6sigma^2t^2].                 (4)

Bochner's identity and product differentiation now give

    Delta G=(4h0^2/a^2)Psi_sigma(K),
    Psi_sigma(K)=-(m+1)^2K^2+3(m+1)(m+2)K
                  -2(m+2)^2+6sigma^2(2K-3).              (5)

For example Delta|H|^2=2|T|^2, Delta|g|^2=2|H|^2 and grad|g|^2=2Hg suffice to obtain (5). It is also the transverse trace of the Hessian formula in Section 3, since G and grad G vanish and X.grad G=-2G force all Hessian entries with a normal index to vanish.

Psi is strictly increasing for 3/2<=K<=2: its derivative is at least (m+1)(2-m)>0. At 3/2 its value is (m-1)(m+5)/4<0, and at 2 it is 2m+6sigma^2>0. Thus (1) forces the unique root in (3/2,2). The zero-rotation root is K0=(m+2)/(m+1); adding the nonnegative rotation term gives K<=K0. Equivalently,

    0<t^2<=(1-m)/(m+1), u=(m+1)t^2/(1-m) in (0,1],
    -(m+1)^2t^4+[6(m+1)+24sigma^2]t^2
                         +(m-1)(m+5)=0.                  (6)

No bound on finite omega is used.

## 3. The fourth tensor, determined without a fifth derivative

Set Z=D4f(x*). Differentiating homogeneity a third time gives, in indices i,j,k,

    Z_ijk3=-(m+3)T_ijk
           +sigma sum_l(J_li T_ljk+J_lj T_ilk+J_lk T_ijl).

Consequently its entries containing normal indices are

    Z3333=h0(m+2)(m+3),
    Z1133=-h0[(m+2)(m+3)alpha-2sigma^2t],
    Z2233=-h0[(m+2)(m+3)beta+2sigma^2t],
    Z1233=-h0 sigma t(2m+5),                               (7)

and entries with one or three transverse indices vanish. The latter uses the zero transverse cubic and the first transverse gradient, not a parity assumption on f itself.

The transverse quartic polynomial has a two-dimensional harmonic freedom. Harmonicity determines its transverse Laplacian from (7), so it is uniquely of the form

    A0(x1^2+x2^2)^2
      +Re((Br+iBi)(x1+i x2)^2(x1^2+x2^2))
      +Re((A+iB4)(x1+i x2)^4),

where

    A0=h0(m+2)(m+3)/64,
    Br=h0t[(m+2)(m+3)-4sigma^2]/48,
    Bi=-h0t sigma(2m+5)/24.                                (8)

To check this directly, the transverse Laplacians of the first two displayed quartics are 16A0(x1^2+x2^2) and 12Re((Br+iBi)(x1+i x2)^2). Their sum is the negative of the normal quadratic term (1/2)sum_(i,j<=2) Z_ij33 x_i x_j. Thus (8) follows without an existence theorem for analytic modes.

The remaining entries of Z are

    Z1111=24(A0+Br+A), Z2222=24(A0-Br+A),
    Z1122=8A0-24A,
    Z1112=-12Bi-24B4, Z1222=-12Bi+24B4.                    (9)

Here is an explicit way to solve for A,B4. Put r=q-2 and e=|g|^2,k=|H|^2. At f=1,

    e_i=2(Hg)_i,
    e_ij=2 sum_v(H_vi H_vj+g_v T_vij),
    k_ij=2 sum_(v,w)(T_vwi T_vwj+H_vw Z_vwij),
    G_ij=2k_ij/a^2+Dq(q-1)[r(r-1)g_i g_j e+rH_ij e
                             +r g_i e_j+r g_j e_i+e_ij].  (10)

Substitution of (2)-(4),(7)-(9) in G_11-G_22=G_12=0 gives

    A=h0[m^2+9m+2+4(m+1)t^2+24sigma^2]/192,
    B4=-h0 sigma[(m+1)t^2+m-4]/48.                        (11)

The response to a change of A,B4 in the transverse Hessian of G is

    -(96h0t/a^2) [[A,-B4],[-B4,-A]],

which is invertible because t>0. Hence (11) is forced, rather than merely one choice. The remaining scalar trace is exactly (5). Formula (10), the exact solutions (11) and all harmonic trace identities are independently checked in check_algebra.py (accompanying artifacts). The displayed formulas make this a finite algebra identity, not a numerical optimization.

## 4. A trace depending only on the forced fourth tensor

At x*, let l=g.Hg, w=|Hg|^2 and z3=T(g,g,g). Since f is harmonic,

    Delta(f^r e)=2f^r k+r(r-1)f^(r-2)e^2+4r f^(r-1)l.

Apply Delta to each term, using

    Delta k=2|T|^2, Delta(e^2)=4e k+8w,
    grad(e^2)=4e Hg, Delta l=2tr H^3+2g.grad k,
    g.grad l=2w+z3.

At f=1 this yields

    L2=Delta^2(f^r e)
      =4|T|^2+6r(r-1)e k+24r(r-1)w
       +r(r-1)(r-2)(r-3)e^3
       +12r(r-1)(r-2)e l+12r g.grad k
       +8r tr H^3+8r(r-1)z3.                             (12)

Also Delta^2 k=4|Z|^2. Therefore

    Delta^2 G=8|Z|^2/a^2+Dq(q-1)L2.                       (13)

All invariants in this expression are fixed:

    e=m^2, k=h0^2K, l=m^2h0, w=m^2h0^2,
    g.grad k=2m(m+2)k,
    tr H^3=3h0^3(1-t^2)/4, z3=m^3h0(m+2),
    |Z|^2=Z1111^2+Z2222^2+Z3333^2
       +4(Z1112^2+Z1222^2)
       +6(Z1122^2+Z1133^2+Z2233^2)+12Z1233^2.             (14)

The norm multiplicities count all permutations of symmetric indices. Formula (12) has no fifth or higher f derivative: harmonicity removes all traces of those terms. In particular it is valid without any assumption on those unspecified jets.

Eliminate sigma^2 in (13) by (6) and substitute t^2=(1-m)u/(m+1). Direct algebra gives

    Delta^2 G=(m+1)(m+2)^2 P(m,u)/(9u^2),                  (15)

where

    P=C0+m C1+m^2 C2+m^3[(1-m)C3+m C34]+m^5 C5,
    C0=(1-u)(-4u^4+14u^3+205u^2+520u+225),
    C1=-4u^5+102u^4+221u^3-471u^2+539u+765,
    C2=-8u^5-42u^4+256u^3-120u^2+256u+954,
    C3=8u^5-126u^4-136u^3-144u^2+92u+522,
    C34=12u^5-66u^4-273u^3-357u^2+189u+639,
    C5=(1-u)(4u^4-20u^3-7u^2+26u+9).                   (16)

An independent exact rational computation forms (10), solves (11), sums the Cartesian tensor norm in (14), and verifies (15) after precisely the substitution in (6). Every remainder is zero. The actual elapsed time is 3.0015333332121372 seconds, recorded with start/end times in the team records. The theoretical question and pass criteria were written before execution. No floating-point samples or optimization enter this argument.

## 5. Strict positivity and the exact vanishing order

For 0<=u<=1, C0>=0 because -4u^4+14u^3>=0. In C1, the pair 539u-471u^2 is nonnegative and -4u^5>=-4, giving C1>=761. In C2, discard positive terms and bound the three negative terms below by -8,-42,-120, respectively, to get C2>=784.

For C3, use u^2,u^3,u^4<=u and discard 8u^5 to obtain C3>=522-(126+136+144-92)u>=208. The same argument gives C34>=639-(66+273+357-189)u>=132. Finally the factor in C5 satisfies

    4u^4-20u^3-7u^2+26u+9
       >=4u^4-27u^2+26u+9>=4u^4-u+9>=8,

so C5>=0. Since 0<m<1 and 0<u<=1, every grouped term in P is nonnegative and m C1 is strictly positive. Equations (15)-(16) give Delta^2G>0. This contradicts the vanishing four-jet of G in (1). The theorem follows.

The confirmed LIT281 analytic examples have exactly the hypotheses of Section 1: g=-m e3, transverse Hessian -h0 diag(alpha,beta), and t from the unique root above lies strictly between zero and one. Their F and all derivatives through order four vanish by A2028-A2032. The theorem shows that some fifth derivative is nonzero. Thus their first nonzero Taylor term has degree exactly five for every stated c and finite omega. This is an exact conclusion about the constructed germs, not a sampled numerical observation.

## 6. Dependencies and scope

The local obstruction was rederived by Cartesian differentiation, harmonic traces, the finite-jet coordinate argument and elementary positivity. The only previously audited existence input is the LIT281 family for the exact-order corollary. Its analytic convergence and exact sector momentum were already fully checked in A2028-A2032; no new global realization is claimed here. All six source sections and all six independent sections were read before the designated verdict. The source SHA256 and retained snapshot are in the team records.

The hypotheses exclude an isotropic transverse Hessian, an indefinite or degenerate transverse Hessian, an off-axis point and a nonzero transverse gradient. The proof divides by t and cannot silently include the isotropic case. It does not identify a universal fifth-order obstruction, establish general supported-vorticity matching, or prove nonexistence of a whole-space decaying rotating profile. The original arbitrary-helicity conjecture remains open. No pressure normalization, global decay or characteristic completeness is needed for this local analytic assertion; such conditions would be additional in any proposed global transfer.
