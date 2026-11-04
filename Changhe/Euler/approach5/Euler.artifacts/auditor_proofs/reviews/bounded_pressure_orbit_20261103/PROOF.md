# Bounded pressure gradient and inverse-radius orbit-direction decay

Status: CONFIRMED A485 at the exact hypotheses below. Complete postwrite including Section5a read at 2026-11-03T05:08:10.253124+00:00 and repeated in full after the configured-model author response. No computation is required. This strengthens the first read of C37; it does not prove full derivative decay.

## 1. Exact statement

Let 0<c<1 and omega be any finite real number. Let J(x1,x2,x3)=(-x2,x1,0), A=cI-omega J and B(y)=Ay+U(y). Suppose U:R3->R3 is C2, P:R3->R is C1, and

    div U=0,
    (1-c)U+DU B+omega J U+grad P=0.                       (1)

Assume M=sup|U|<infinity and L=sup||DU||<infinity. No decay or prescribed pressure normalization is assumed. Write G=DU, W=curl U and e(y)=Ay/|Ay| for y!=0. There is a finite constant C depending only on c,omega,M,L such that

    sup_R3 |grad P| <= C,    sup_R3 |G Ay| <= C,
    |G(y)e(y)|+|W(y).e(y)| <= C/|y|,  |y|>=1.             (2)

An additive constant in P is irrelevant. In particular the original submitted C37 little-o statements and every rate with exponent -1/2+epsilon follow. The full norm ||DU|| is only assumed bounded; it is not proved to tend to zero.

Define P_e=I-e tensor e and

    g=G^T e-(e.G e)e,
    H=P_e G P_e,
    S_h=(H+H^T)/2-(tr H/2)P_e.

Then S_h is symmetric, S_h e=0, tr S_h=0, g.e=0, and uniformly for |y|>=1,

    G=S_h+e tensor g+O(|y|^-1),
    W=g cross e+O(|y|^-1),
    G W=S_h W+O(|y|^-1).                                (3)

The strain in direction e means its Rayleigh quotient e.sym(G)e, which is O(|y|^-1). It need not be an eigenvalue with eigenvector e. If W->0, (3) implies g->0 and G=S_h+o(1), without excluding the remaining planar strain.

## 2. The pressure source and its possible harmonic part

The right side of (1) gives grad P in C1, so P is C2. Put F_ij=U_i U_j. Differentiating (1) and using div U=0, the two rotation terms cancel and

    f:=Delta P=-tr(G^2)=-sum_ij partial_i partial_j F_ij.  (4)

Thus F is bounded and f is bounded continuous, with bounds controlled by M^2 and L^2. Equation (1) also gives

    grad P=-G Ay+E,
    E=-(1-c)U-GU-omega JU,   |E|<=C(c,omega,L)M.          (5)

Consequently |grad P(y)|<=C(1+|y|). This is all the initial pressure growth needed.

Take N(y)=-1/(4pi|y|), so Delta N=delta_0. Fix a smooth radial cutoff chi equal to1 on the unit ball and0 outside the ball of radius2. For d>0 set

    N_0(y)=chi(y/d)N(y),    N_infty(y)=(1-chi(y/d))N(y).

All convolution formulas below are on R3. Define the vector field

    Q=(grad N_0)*f
             -sum_ij (partial_i partial_j grad N_infty)*F_ij.   (6)

This formula consists of absolutely convergent integrals. The first kernel is supported in the radius2d ball and behaves as |y|^-2 near0. Its L1 norm is at most C d. The second is smooth near0, is supported outside the radius d ball, behaves as |y|^-4 at infinity, and has L1 norm at most C/d. These bounds follow by scaling each kernel from d=1. Therefore

    ||Q||_infinity <= C(d||f||_infinity+d^-1 max_ij||F_ij||_infinity).
                                                               (7)

Each convolution is uniformly continuous: translation of its L1 kernel tends to0 in L1 and its input is bounded. In particular Q is continuous. If M,L>0 choose d=M/L, obtaining ||Q||<=C M L. If L=0, U is constant and the theorem follows directly from (1); if M=0 it is immediate. Using d=1 would also suffice for finiteness.

Here are the distributional identities in (6), including the far-field terms. Set a=Delta N_0-delta_0. This is smooth, supported in the annulus d<=|y|<=2d, and Delta N_infty=-a. Every convolution with a or its derivatives is well-defined. The kernels in (6) are gradients, so curl Q=0 in distributions. Moreover, using (4),

    div Q=(delta_0+a)*f+sum_ij (partial_i partial_j a)*F_ij
         =f+a*f+sum_ij a*(partial_i partial_j F_ij)=f.    (8)

The last equality uses a compactly supported smooth kernel, so there is no boundary at infinity in the integrations by parts. Thus Delta Q=grad f. These identities can equivalently be obtained by distributional testing against compactly supported functions; no integral of P at infinity has been used.

Let Z=grad P-Q. It is continuous and distributionally harmonic by (4),(8), hence smooth harmonic componentwise. For completeness this regularity follows by local mollification and the mean-value identity for harmonic functions, then uniform convergence of the mollified continuous functions on compact sets. By (5),(7), |Z(y)|<=C(1+|y|). Each component of Z is affine. Indeed the interior estimate for the second derivatives of a harmonic function on a ball gives |D^2 Z(x)|<=C R^-2 sup_{B(x,R)}|Z|=O(R^-1) as R->infinity. This estimate follows by differentiating the Poisson formula on the ball of radius R. Hence

    Z(y)=K y+b                                             (9)

for a constant matrix K and vector b. Curl and divergence would imply K is symmetric and trace-free, but those facts are unnecessary for the next step.

## 3. The profile equation eliminates the linear gradient

For R>=1 and z in any fixed bounded annulus away from0 put

    V_R(z)=U(Rz)/R,    G_R(z)=G(Rz)=D_z V_R(z).

The V_R tend uniformly to0, so G_R tends to0 distributionally: integrate D_z V_R against any compactly supported smooth test function. Multiplication by the smooth bounded matrix Az preserves distributional convergence. Equation (5) therefore gives

    grad P(Rz)/R=-G_R(z)Az+E(Rz)/R ->0

in distributions on the annulus. On the other hand (7),(9) give

    grad P(Rz)/R=Kz+b/R+Q(Rz)/R ->Kz

uniformly there. Thus Kz=0 on an open annulus, and K=0. The actual pressure gradient satisfies

    grad P=Q+b.                                           (10)

There is no unspecified growing harmonic pressure left. Its constant gradient b is allowed, as is necessary for a nonzero constant velocity profile. At y=0, (5) bounds grad P(0) by C(c,omega,L)M, while (7) bounds Q(0) by CML. Thus |b| and sup|grad P| are bounded by C(c,omega)M+CML. Equation (5) now also bounds |G Ay| uniformly. Since |Ay|>=c|y|, this proves the first directional estimate in (2).

This argument is independent of the previously submitted fractional-power OD estimate. It uses its weak distributional blowdown idea only to remove the finite-dimensional harmonic ambiguity, after the explicitly constructed bounded field Q handles the Poisson source. No Calderon-Zygmund endpoint theorem or assumed pressure normalization is needed.

## 4. Axial vorticity transport and its complete characteristics

The curl of (1) gives the classical C1 equation

    B.grad W=G W-W-omega J W.                            (11)

Both U and G are bounded, so B is globally Lipschitz with linear growth. Its flow exists uniquely for all finite positive and negative times. Let a(y)=W(y).e(y). The homogeneous field e satisfies

    (Ay).grad e=-omega J e,    ||De(y)||<=C(c,omega)/|y|.  (12)

The first identity follows by differentiating Ay/|Ay| along Ay, using e.Ae=c and A e=c e-omega J e. In an oriented orthonormal frame with e=e3, writing G_ik=partial_k U_i,

    W=(G32-G23,G13-G31,G21-G12),
    e.G W=G32(Ge)_1-G31(Ge)_2+W3(Ge)_3.

Consequently |e.G W|<=C||G|| |Ge|. Differentiating a by (11),(12), the rotation terms cancel exactly and

    B.grad a=-a+epsilon(y),
    epsilon=e.G W+W.(U.grad e),
    |epsilon(y)|<=C/|y|,  |y|>=1.                        (13)

The bound uses (2)'s already established estimate for Ge, bounded W and bounded U. This cancellation works for every fixed omega.

Choose R1>max(1,2M/c). On the exterior, the radius r=|Y| of a B-characteristic satisfies

    cr-M<=r'<=cr+M.                                      (14)

Every exterior point y is reached in a finite time tau>=0 from the sphere r=R1 by a forward characteristic that stays outside this sphere. Indeed backward motion decreases r at least at rate cr/2 until it crosses the sphere; if it never crossed, integrating that inequality would force r below R1. Completeness gives the entire finite segment. For 0<=s<=tau,

    r(s)>=M/c+(R1-M/c)e^(cs)>=(R1/2)e^(cs),
    r(tau)+M/c<=(R1+M/c)e^(c tau).                      (15)

Integrating (13) on the segment gives

    |a(y)|<=||W||_infinity e^-tau
             +C integral_0^tau e^(s-tau)e^(-cs) ds
           <=C[e^-tau+e^(-c tau)/(1-c)]
           <=C/|y|.                                    (16)

The last inequality uses (15) and 0<c<1. A larger constant covers 1<=|y|<=R1. This proves the second directional estimate in (2), including the uniformity over all directions. At c=1 the displayed integral would have a logarithm; that endpoint is not part of the theorem.

## 5. Pointwise matrix form and physical interpretation

At each point put h=Ge. The exact block decomposition relative to the oriented plane e^perp is

    G=H+e tensor g+h tensor e.

Its trace gives tr H=-e.h=O(|y|^-1). Its planar antisymmetric part has scalar W.e=O(|y|^-1). Hence H=S_h+O(|y|^-1), proving the first identity of (3). The antisymmetric vector of e tensor g is g cross e; that of S_h is0. This proves the second identity. Finally g.(g cross e)=0, so

    (e tensor g)W=O(|y|^-1)

because g is bounded. Combining with the first two identities proves the third. All error bounds are uniform; no spatial derivative of the pointwise moving frame is used in this linear algebra.

For the rotating self-similar physical field, let tau=T-t>0, s=-log tau, Q_s=exp(omega J s), y=exp(sA)x. The standard convention is

    u(x,t)=tau^(-(1-c))Q_s U(y),
    p(x,t)=tau^(-2(1-c))P(y).

Then |y|=tau^-c |x|, Q_s^T Ax=tau^c Ay and

    tau^2 |grad_x p|=tau^c |grad P(y)|=O(tau^c),
    tau |grad_x u Ax|=tau^c |G(y)Ay|=O(tau^c).

These bounds hold locally uniformly for x away from0. They do not bound all components of grad_x u by an integrable function. No physical continuation theorem or nonexistence conclusion follows from them.

## 5a. Additional consequence when U tends uniformly to zero

If, in addition, U(y)->0 as |y|->infinity, then

    grad P(y)->0,    G(y)Ay->0,
    |y|[|G(y)e(y)|+|W(y).e(y)|]->0.                    (17)

Here is a proof that also fixes the constant-gradient pressure ambiguity in this subclass. Denote the bounded field in (6) by Q_d to remember the cutoff radius. Formula (8) and the profile blowdown show grad P=Q_d+b_d for every d>0. For any two choices d1,d2, Q_d1-Q_d2 is bounded entire harmonic and hence constant. The difference is also

    grad[(chi(./d1)-chi(./d2))N]*f
      +sum_ij partial_i partial_j grad[(chi(./d1)-chi(./d2))N]*F_ij.

The bracket is smooth and compactly supported away from0 when d1,d2 are fixed, and f=-partial_ij F_ij. Moving the derivatives onto this compact kernel shows the difference is identically0. Thus Q_d is the same Q for every d, and b_d is one b.

For fixed d, the far kernel in (6) is L1, while F_ij tends uniformly to0. Its convolution with F_ij therefore tends to0: split the kernel into a compact part and an arbitrarily small L1 tail. The near part is bounded by C d L^2. Consequently

    limsup_{|y|->infinity}|Q(y)|<=C d L^2

for every d>0. Sending d to0 gives Q->0. Hence grad P->b by (10). Equation (5) has E->0 because U->0 and G is bounded, so G Ay->-b. Along a linear orbit y(s)=exp(sA)y0 with y0!=0,

    d/ds U(y(s))=G(y(s))Ay(s)->-b.

Since U is bounded, dividing its integral by s as s->infinity gives b=0. This proves the first two limits in (17), uniformly at infinity. Division by |Ay|>=c|y| gives |y|Ge->0.

The forcing in (13) now satisfies |y|epsilon(y)->0: its first term is bounded by CL|y|Ge and its second by C|W||U|. To obtain the last limit in (17), fix eta>0 and start the exterior characteristic on a sufficiently large sphere R_eta such that |epsilon(y)|<=eta/|y| beyond it. Formula (15) then bounds the contribution from the forcing, after multiplication by r(tau), by C eta/(1-c), with C independent of R_eta once R_eta>2M/c. The initial term multiplied by r(tau) is at most C(R_eta)e^{-(1-c)tau}, which tends to0. First let |y|->infinity and then eta->0. This proves |y||W.e|->0. No decay of the full G has been inserted.

## 6. Dependencies, review and scope

Dependencies are the exact Euler curl/divergence identities; absolutely integrable cut-off Newtonian kernels; distributional integration by parts with compactly supported kernels; harmonic mean-value and Poisson formulas; classical C1 characteristics; and finite-dimensional linear algebra. All uses, including the harmonic pressure ambiguity and flow completeness, are proved or specified above. The exact kernel estimates are analytic, not numerical observations.

The separately submitted H-measure localization corollary is not needed here and is not certified by this proof. Its statement must distinguish a full sequence from an extracted subsequence carrying a particular defect measure. General far-field decay, boundedness of DU from U->0, the high-strain alternatives and the arbitrary-omega nonexistence conjecture remain OPEN.

## 7. Focused response and final audit

The complete revised Theory Agent A ORBIT_LAYERS source and Note A18 were read after their 05:22 and 05:26 updates. The configured-model author explicitly checked Sections2-3 and Section5a and incorporated the stronger pressure and directional conclusions. The two separate external referee (a second model) referees also obtained the bounded pressure splitting, but their presence is not substituted for the author response. The complete independent literature-agent reconstruction agrees. All three source records are pinned.

A485 confirms only Sections1-5a above and the exact pointwise algebraic consequences. The subsequent mean-decay claim C38 is a separate submission and is not covered by this verdict. In particular no assumption sup|DU|<infinity has been removed. The actual model evidence is the existing Theory Agent A configuration, the primary model, not independent provider attestation. No remote model client or computation was used by this audit.
