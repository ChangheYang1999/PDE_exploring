# Fifth-order axial rank obstruction for every transverse Hessian

Independent audit of LIT284. The new argument covers distinct transverse eigenvalues with arbitrary signs. The complete conclusion for all transverse Hessians also uses the separately confirmed isotropic theorem.

## 1. Exact theorem and the finite scalar jet

Let 1/3<c<1/2 and omega in R. Set

    a=1-2c, b=2(1-c), m=a/c in (0,1), sigma=omega/c,
    q=b/a=2(m+1)/m, h=m(m+1), Jx=e3 cross x,
    X=(cI-omega J)x, x*=e3.

Let f,Q be real analytic and harmonic on a neighborhood of x*, satisfying

    X.grad f=-af, X.grad Q=-bQ,
    f(x*)=1, f_1(x*)=f_2(x*)=0.

Define E=|grad f|^2/a^2, S=Q-E and F=grad f cross grad S. Some Cartesian derivative of F of order at most five is nonzero at x*. No assumption on the signs or multiplicities of the two transverse Hessian eigenvalues is needed.

First assume the transverse eigenvalues are distinct. Suppose the asserted conclusion fails. At x*, homogeneity gives grad f=-m e3!=0. In analytic coordinates (f,u,v), the coefficients of df wedge dS are S_u,S_v. Vanishing of its five-jet therefore implies that the scalar six-jet of S contains only f derivatives. Invertible coordinate changes preserve this vanishing order. Choose a one-variable function H matching that six-jet. Since E and Q both have scalar homogeneity weight b, applying X.grad+b to S-H(f) gives, through degree five,

    a H^(j+1)(1)=(b-aj)H^(j)(1), j=0,...,5.

These are precisely the derivatives of D f^q for some real D, with f>0 near x*. Thus the six-jet of Q-B vanishes, where B=E+D f^q. Harmonicity of Q implies

    G=Delta B has zero jet through order four at x*.       (1)

This only identifies a finite jet. It does not assert S=D f^q on a neighborhood.

## 2. The forced low tensors and the two root branches

Diagonalize the transverse Hessian by a rotation commuting with J, ordering its distinct eigenvalues so that t>0. Differentiated homogeneity and harmonicity give

    g=grad f=(0,0,-m),
    H=D^2f=h diag(-(1+t)/2,-(1-t)/2,1),
    K=(3+t^2)/2.

In particular the transverse trace is -h, the mixed normal entries vanish, and |H|^2=h^2K. Write r=q-2. Since

    G=2|H|^2/a^2+Dq(q-1)f^r|g|^2,

equation (1) at order zero gives D=-(m+1)(m+2)K.

The free transverse harmonic cubic of f is Re(C3(x1+i x2)^3). The two transverse derivatives of G are

    G_1=-(24ht/a^2)Re C3, G_2=(24ht/a^2)Im C3.

Since t>0, C3=0. The nonzero entries of T=D^3f, with symmetric permutations understood, are

    T113=h(m+2)(1+t)/2, T223=h(m+2)(1-t)/2,
    T123=sigma ht, T333=-h(m+2).                         (2)

These formulas follow by differentiating homogeneity; pure transverse cubic entries vanish. They are algebraic for every t>0 and do not require negative transverse eigenvalues.

Bochner and product differentiation give

    Delta G=(4h^2/a^2)Psi(K),
    Psi(K)=-(m+1)^2K^2+3(m+1)(m+2)K
             -2(m+2)^2+6sigma^2(2K-3).

Writing T0=t^2, its vanishing is equivalent to

    P(T0)=-(m+1)^2T0^2+[6(m+1)+24sigma^2]T0
                         +(m-1)(m+5)=0.                 (3)

At zero sigma the two positive roots are Tminus=(1-m)/(m+1) and Tplus=(m+5)/(m+1). For general sigma the value at each of these points increases by 24sigma^2 times that point. The polynomial is strictly concave, negative at zero and at sufficiently large positive arguments, and nonnegative at both displayed points. Consequently every positive root belongs to

    0<T0<=Tminus<1, or T0>=Tplus>1.                       (4)

There are no other roots. In particular P(1)=8m+24sigma^2>0 excludes a zero transverse eigenvalue. On the small branch H has distinct negative transverse eigenvalues. The complete independently checked LIT282 theorem, A2049-A2053, then contradicts (1). Its exact hypotheses are those in Section 1 plus these distinct negative eigenvalues. The remaining sections exclude the large branch directly.

## 3. The fourth tensor and the free higher modes

Put alpha=(1+t)/2, beta=(1-t)/2 and Z=D^4f(x*). Every entry with a normal index follows from differentiated homogeneity:

    Z_ijk3=-(m+3)T_ijk
       +sigma sum_l(J_li T_ljk+J_lj T_ilk+J_lk T_ijl).

Thus the nonzero such entries are

    Z3333=h(m+2)(m+3),
    Z1133=-h[(m+2)(m+3)alpha-2sigma^2t],
    Z2233=-h[(m+2)(m+3)beta+2sigma^2t],
    Z1233=-h sigma t(2m+5).

The pure transverse quartic is fixed by harmonicity up to Re((A+iB4)(x1+i x2)^4). Explicitly put

    A0=h(m+2)(m+3)/64,
    Br=ht[(m+2)(m+3)-4sigma^2]/48,
    Bi=-ht sigma(2m+5)/24.

Then

    Z1111=24(A0+Br+A), Z2222=24(A0-Br+A),
    Z1122=8A0-24A,
    Z1112=-12Bi-24B4, Z1222=-12Bi+24B4.                   (5)

These identities can be checked by applying the transverse Laplacian to

    A0(x1^2+x2^2)^2
      +Re((Br+iBi)(x1+i x2)^2(x1^2+x2^2))
      +Re((A+iB4)(x1+i x2)^4)

and comparing with the negative normal second derivative. The response of the transverse Hessian of G to A,B4 is

    -(96ht/a^2) [[A,-B4],[-B4,-A]].

It is invertible on trace-free symmetric matrices. Equating its trace-free part to zero forces

    A=h[m^2+9m+2+4(m+1)t^2+24sigma^2]/192,
    B4=-h sigma[(m+1)t^2+m-4]/48.                        (6)

The earlier Cartesian derivation verifies (5)-(6) as rational identities without a restriction t<1; it was reread in full. The remaining trace equation is (3).

For completeness, the free fifth transverse harmonic term Re(C5(x1+i x2)^5) contributes

    -(80ht/a^2)Re(C5(x1+i x2)^3)

to G's transverse cubic. All lower terms are even in the transverse variables because C3=0. Hence its zero third jet forces C5=0. The coefficient follows from the xx Hessian entry 20Re(C5(x1+i x2)^3), the opposite yy entry, their contraction with H, and the factor four in the cross term of 2|D^2f|^2/a^2.

The free sixth term similarly contributes -(120ht/a^2)Re(C6(x1+i x2)^4) to the transverse quartic of G. It is transverse harmonic and disappears from the test below. Higher terms cannot contribute. The independent computation instead differentiates Delta G first; its Bochner formula only needs derivatives of f through order five, so no sixth derivative can enter it.

## 4. Independent Cartesian computation of the decisive derivative

Define

    Dcal=(partial_11-partial_22)Delta G(x*)/2.

By (1), Dcal would be zero. Here is a complete finite tensor procedure for evaluating it. Let V5=D^5f. If an index is normal, differentiate homogeneity once more:

    V5_ijkl3=-(m+4)Z_ijkl
       +sigma sum_p[J_pi Z_pjkl+J_pj Z_ipkl
                     +J_pk Z_ijpl+J_pl Z_ijkp].           (7)

The pure transverse entries are zero after C5=0. The resulting tensor is symmetric and satisfies every harmonic trace identity; the independent checker verifies these exact identities.

For each i=1,2 define

    v_i=H e_i, T_i=(T_jki)_(jk), Z_ii=(Z_jkii)_(jk),
    t_ii=(T_jii)_j, e0=|g|^2, k0=|H|^2, l0=g.Hg,
    e2_i=|v_i|^2+g.t_ii,
    k2_i=sum_(j,k)[T_jki^2+H_jk Z_jkii],
    l2_i=v_i.Hv_i+t_ii.Hg+2v_i.T_i g+(1/2)g.Z_ii g,
    n2_i=sum_(j,k,l)[Z_jkli^2+T_jkl V5_jklii].

These are the coefficients of s^2 in |grad f|^2, |D^2f|^2, grad f.D^2f grad f, and |D^3f|^2 along x*+s e_i, respectively. For example grad f=g+s v_i+s^2 t_ii/2+O(s^3). Since f_i=0, f=1+s^2 H_ii/2+O(s^3). Bochner's identity gives on the whole local domain

    Delta G=4|D^3f|^2/a^2
      +Dq(q-1)[r(r-1)f^(r-2)|grad f|^4
         +4r f^(r-1)grad f.D^2f grad f
         +2f^r|D^2f|^2].                                (8)

The coefficient of s^2 in (8) along e_i is therefore

    Li=4n2_i/a^2+Dq(q-1){
        r(r-1)[2e0 e2_i+(r-2)H_ii e0^2/2]
       +4r[l2_i+(r-1)H_ii l0/2]
       +2[k2_i+rH_ii k0/2]}.

Thus Dcal=L1-L2. This avoids expanding G into harmonic modes. Substituting (2),(5)-(7) gives the exact identity

    Dcal=t(m+1)^2(m+2)^2 R,
    R=5m^3t^4+16m^3t^2+3m^3
      +40m^2sigma^2t^2+24m^2sigma^2+15m^2t^4+14m^2t^2-69m^2
      -48m sigma^2t^2-432m sigma^2+15m t^4-16m t^2-87m
      -672sigma^4-88sigma^2t^2-336sigma^2+5t^4-14t^2+9.   (9)

Equation (3) gives

    sigma^2=[(m+1)^2t^4-6(m+1)t^2-(m-1)(m+5)]/(24t^2).

Since t>0 the substitution is valid. After it, (9) is

    Dcal=(m+1)^2(m+2)^2 N(m,t^2)/(6t^3),                 (10)

with

    N(m,T0)=(3m^4+10m^3+12m^2+6m+1)T0^4
       +(6m^4+24m^3+54m^2+84m+48)T0^3
       +(4m^4+38m^3+122m^2+70m+126)T0^2
       +(-6m^4+126m^2-120m)T0
       -7m^4-56m^3-42m^2+280m-175.

The exact checker derives (9) from (7)-(8), then checks (10). Every remainder is identically zero. There is no numerical evaluation of a sign or an optimizer.

## 5. Positivity, isotropic completion and a failed scalar test

On the large branch write T0=(m+5)/(m+1)+v with v>=0. The exact expansion is

    (m+1)^4 N(m,T0)=sum_(j=0)^4 C_j v^j,
    C0=48(m+1)^2(m+2)(m+5)^2(3m^2+2m+4),
    C1=4(m+1)^3(m+5)(8m^4+95m^3+273m^2+310m+268),
    C2=2(m+1)^4(20m^4+193m^3+598m^2+707m+498),
    C3=2(m+1)^5(9m^3+47m^2+60m+34),
    C4=(m+1)^7(3m+1).

All five coefficients are strictly positive for m>0. Therefore N>0 throughout this branch. The prefactor in (10) is positive, so Dcal>0, contradicting (1). This completes the distinct-eigenvalue case, including mixed signs.

If the transverse eigenvalues coincide, their trace forces both to equal -h/2. This is exactly the negative isotropic axial class of LIT283, independently confirmed A2055-A2060. That theorem excludes vanishing through order five under the same hypotheses, including its exceptional c=5/11,omega=0 case, where only the weaker order-four obstruction fails. Thus it completes the all-Hessian theorem in Section 1. Neither dependency covers off-axis points, and no such conclusion is inferred.

The scalar test Delta^2G alone does not extend the earlier small-branch proof: at sigma=0 on the large branch its previously computed value is

    16(m+1)(m+2)^3(3m^3+15m^2+10m-4),

whose last factor is negative at m=0 and positive at m=1. This does not supply an example meeting the full jet conditions. The decisive test here instead reduces at sigma=0 to

    Dcal=8t(m+1)^2(m+2)^3(3m^2+2m+4)>0.

The new check verifies this second identity directly. The first scalar expression is retained from the prior exact trace audit; its change of sign explains why a different contraction was needed.

## 6. Verification and scope

All six submitted proof sections and the complete prior Cartesian anisotropic audit were read, including every derivative-count and free-jet argument. The independent checker uses the previously derived H,T,Z definitions, reconstructs V5 from (7), verifies its symmetry and all ten independent harmonic traces, computes (8) in the two Cartesian directions, and checks (9), (10), all five positive coefficients and the zero-rotation reduction. All nineteen exact checks pass.

The computation ran with one local worker on CPU55. Its actual start and finish were 2026-11-03T18:56:07.237785+00:00 and 2026-11-03T18:56:08.542924+00:00; its monotonic duration was 1.3051401092670858 seconds. The prior theoretical question and pass/fail criteria, script, JSON result and pinned sources are in the team records. No formal build or numerical search was used.

This is a local rank-jet obstruction at an axial point with f=1 and zero transverse gradient, for 1/3<c<1/2 and every real finite omega. It does not prove that a matching interface contains such a point. No original-profile pressure normalization, flow completeness or far-field decay theorem enters the local calculation. Off-axis points, nonzero transverse gradients, general supported matching and the whole-space decaying-profile conjecture remain open.
