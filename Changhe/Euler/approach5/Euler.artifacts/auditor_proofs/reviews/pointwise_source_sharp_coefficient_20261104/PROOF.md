# Sharp infimum for the pointwise positive-source coefficient

Status: independent reconstruction and the existing C comparison are complete.
The designated verdict below concerns kinematic sharpness, not construction
of an Euler profile.

## 1. Statement, notation and scope

Let0<beta<1,L>0. Let J(y1,y2,y3)=(-y2,y1,0). The full rotating equation means
(1-c)U+(((cI-omega J)y+U).grad)U+omega JU+grad P=0, with div U=0.
Hb means U(R.) tends to zero in distributions. For C1 divergence-free U on R3 define

    E_a(R)=integral_(B_R(a))|U|^2,
    q=tr((DU)^2), q_+=max(q,0),
    H_a(R)=integral_(1<|y-a|<R)|y-a|^(2-beta)q_+(y)dy,
    k_beta=beta(2-beta)(1-beta).

If E_0(R)=LR^beta+O(R^(beta-1)), then for every fixed a,
H_a(R)>=k_beta L log R-C_a at all sufficiently large R. A ratio limit
alone gives only liminf H_a(R)/log R>=k_beta L.

For every epsilon>0 there is a smooth divergence-free uniformly decaying
U with E_0(R)=LR^beta for R>=2 and
E_a(R)=LR^beta+O_a(R^(beta-2)) for every fixed a, such that

    lim_(R->infinity) H_a(R)/(L log R)<k_beta+epsilon

for all fixed centers. It admits a smooth solution of -Delta P0=q but
fails the full rotating Euler equation for every real c and omega and
every C1 pressure. Thus k_beta is the infimum over this smooth
kinematic class. No single-field attainment, uniform angular regularity
of the family, or optimality in the class of full profiles is asserted.

## 2. Lower bound including both cutoff errors

The distributional identity q=partial_i partial_j(U_i U_j) gives
integral q psi=integral U^T D2 psi U for compact smooth psi. Choose
f>=0 smooth radial, zero on B1 and equal to r^(2-beta) outside B2,
and0<=chi<=1 smooth radial, one on B1 and zero outside B2. Set
psi=f chi(y/R). For r>2, with m=2-beta,

    D2 f=m r^(-beta)(I-beta e_r tensor e_r),
    U^T D2 f U=m r^(-beta)[(1-beta)|U|^2+beta|U_tan|^2].

The possibly negative contribution from B2 is bounded by a fixed
finite constant. The Hessian terms differentiating chi are bounded by
C R^(-beta) on the outer annulus and hence contribute at most
C R^(-beta)E_0(2R)=O(1). The nonnegative source test is at most
r^(2-beta) outside B2. Consequently, for
F(R)=integral_(2<r<R)r^(-beta)|U|^2 and the analogous F_tan,

    H_0(2R)>=m(1-beta)F(R)+m beta F_tan(R)-C.        (1)

Finite integration by parts gives

    F(R)=R^(-beta)E_0(R)-2^(-beta)E_0(2)
             +beta integral_2^R r^(-beta-1)E_0(r)dr
        =beta L log R+O(1).

The last error is integrable because it is O(r^(-2)); no remainder
is differentiated. Both F and F_tan increase by O(1) between R and2R.
Thus (1), with its radius halved, gives the stated coefficient and also
retains beta(2-beta)F_tan(R). Under only the ratio limit the analogous
formula is F(R)=beta L log R+o(log R). Ball inclusions transfer the
ratio or the precise O_a(R^(beta-1)) law to every fixed center. Apply
only this kinematic argument to the translated field.

## 3. A smooth periodic oscillator with negligible negative mass

Set t=(beta-3)/2, k=t+2, A=2(t^2+t+1), D=-2tk and
C=A-D=(2-beta)(1-beta). Here D>0,C>0. Choose a fixed
1<p<min(A/D,3), which is possible because A>D.
For0<delta<=1/2 put V_delta(z)=(delta^2+z^2)^(-p)(1-z^2).
Solve z''=V_delta'(z)/2 with z(0)=0,z'(0)=delta^(-p).
The smooth ODE has conserved z'^2-V_delta(z)=0. It reaches z=1 in
finite time

    T_delta/4=integral_0^1 (delta^2+s^2)^(p/2)/sqrt(1-s^2) ds.

This quarter period is bounded above uniformly and bounded below by
its integral over[1/2,3/4], uniformly in delta. At z=1 the acceleration
is -(delta^2+1)^(-p)<0. Reflection and uniqueness produce a smooth
periodic oscillation between-1 and1. Evenness of V_delta and the initial
conditions make z odd. The finite periodic orbit also ensures global
existence. Define Z(theta)=z(T_delta theta/(2pi)), an odd smooth
2pi-periodic function.

In the original time variable, the derivative energy per period is
4 integral_0^1 (delta^2+s^2)^(-p/2)sqrt(1-s^2)ds. Its integral over
[delta,1/2] diverges as delta tends to0 since p>1. Meanwhile direct
differentiation gives

    A z'^2+D z z''
      =[A-Dp z^2/(delta^2+z^2)]z'^2
          -D z^2(delta^2+z^2)^(-p).

The bracket is at least A-Dp>0. Thus the integral of the negative part
is at most

    4D integral_0^1 s^2(delta^2+s^2)^(-p/2)/sqrt(1-s^2)ds
       <=4D integral_0^1 s^(2-p)/sqrt(1-s^2)ds<infinity.

This bound is uniform in delta since p<3. Rescaling multiplies both
derivative energy and source integrals by T_delta/(2pi), bounded above
and below. Write M_delta=integral_0^(2pi)Z'^2 and
N_delta=integral_0^(2pi)[A Z'^2+D Z Z'']_-. Then M_delta tends to
infinity and N_delta stays bounded. Periodic integration by parts gives

    integral [A Z'^2+D Z Z'']_+=C M_delta+N_delta.

Therefore its ratio to M_delta tends to C. The integrand need not be
pointwise nonnegative; its negative mass is simply negligible in this
ratio.

## 4. Angular fields, the derivative matrix and order of limits

Choose nonzero smooth chi(theta), supported inside(pi/4,3pi/4), even
about pi/2. For fixed delta and integer n>0 let

    g=-(k/n)chi Z(n(theta-pi/2)),
    h=-(g'+cot(theta)g)/k.

Thus kh+g'+cot(theta)g=0 and the homogeneous field
r^t(h e_r+g e_theta) is divergence-free. It vanishes near both polar
axes and is smooth away from the origin. Equatorial parity is h even,
g odd; under y->-y, e_r changes sign and e_theta does not, so the field
is odd and its squared norm is even.

For fixed delta, uniformly on the angular support,

    h=chi Z'+O_delta(1/n),
    g'=-k chi Z'+O_delta(1/n),
    h'=n chi Z''+O_delta(1).

The spatial derivative divided by r^(t-1), in the orthonormal
spherical frame, is the matrix

    [ t h   h'-g       0             ]
    [ t g   h+g'       0             ]
    [ 0     0          h+cot(theta)g ].

Its trace square q_n equals

    t^2 h^2+2t g(h'-g)+(h+g')^2+(h+cot(theta)g)^2
       =chi^2[A Z'^2+D Z Z'']+O_delta(1/n).         (2)

In particular the cross coefficient is D=-2tk. Products involving
h'=O_delta(n) still have the stated error: g is exactly of order1/n,
and the omitted part of h' is O_delta(1).

For any continuous periodic F and smooth compact weight w, subtract
F's mean and use its bounded periodic primitive. Integration by parts
shows that integral w(theta)F(n(theta-pi/2)) differs from the mean of
F times integral w by O(1/n). Apply this with w=chi^2 sin(theta).
For K_n=integral_(S2)(h^2+g^2) and G_n=integral_(S2)g^2,
K_n tends to a positive multiple of M_delta, and G_n=O_delta(1/n^2).
The map x->x_+ is1-Lipschitz, so (2) and the same averaging give

    lim_n integral_(S2)[q_n]_+/K_n
       =integral_0^(2pi)[A Z'^2+D Z Z'']_+/M_delta.

First choose delta so this limit is below C+epsilon/(2beta), then
choose n large so the actual ratio is below C+epsilon/beta. The same
large n can make G_n/(K_n-G_n) as small as desired. No estimate is
required to be uniform as both parameters vary together.

## 5. Smooth radial completion with exact energy

Fix these angular functions and set K=K_n,G=G_n,H=K-G>0. For a smooth
radial f define

    W_f=f h e_r+[(r f'+2f)/k]g e_theta.

Its divergence vanishes by the angular relation. Choose0<=chi0<=1
smooth radial, zero for r<=1 and one for r>=2. Let f0=chi0 r^t,
b=sqrt(beta L/K), and

    C0=integral_1^2 r^(beta-1)[chi0+r chi0'/k]^2dr.

The energy of bW_f0 inside B2 is at most
b^2[H(2^beta-1)/beta+C0 G]. The desired value is L2^beta, so its
positive deficit D0 satisfies

    D0>=b^2[H/beta-C0 G]>0

if n was chosen additionally so C0 G<H/(2beta). This is compatible
with all the previous conditions since G/H tends to0.

Choose a smooth radial eta, equal to1 near0 and zero for r>=1/2.
The field W_c=eta(r)Jy is smooth, compact, divergence-free and odd,
with I_c=integral|W_c|^2>0. Define

    a0=sqrt(D0/I_c), U=b W_f0+a0 W_c.

The supports are disjoint. Their energies add exactly, and the tail
has shell energy b^2K r^(2t+2)=beta L r^(beta-1). Consequently
E_0(R)=LR^beta for every R>=2. The field is smooth on R3, has infinite
total energy, and decays uniformly because t<-1. Its squared density
is even. For fixed a, the first center derivative of E_a at a=0
vanishes. A second center derivative is a boundary integral of one
spatial derivative of |U|^2. On the distant sphere that derivative is
O_a(R^(beta-4)); multiplying by area gives O_a(R^(beta-2)). Taylor's
formula along the fixed center segment proves the stated stronger
all-center energy remainder. No bound uniform over the field family
is needed for this argument.

## 6. The logarithmic coefficient and translation invariance

On r>=2, q=b^2 r^(beta-5)q_n(theta). Therefore

    H_0(R)=b^2 integral_(S2)[q_n]_+ log R+O(1),
    lim H_0(R)/(L log R)=beta integral_(S2)[q_n]_+/K_n
                        <beta C+epsilon.

The compact radial completion changes only the O(1) term. For each
fixed a, smooth angular dependence and homogeneity give
|q(a+x)-q(x)|<=C_a |x|^(beta-6) for all sufficiently large |x|.
Taking positive parts preserves this bound. The critical weight and
radial volume element produce the integrable error C_a r^(-2)dr.
After translating the variable in H_a, both integrals have the same
annular domain1<|x|<R. Their remaining bounded parts are finite. Hence
H_a(R)-H_0(R)=O_a(1), and the coefficient is the same at every fixed
center. Combined with Section2, this proves precisely the infimum
claim for the pointwise positive part.

## 7. Poisson pressure and the local momentum obstruction

Let N(y)=1/(4pi|y|) and define P0=sum partial_i partial_j N*(U_i U_j)
through its principal-value Hessian and the local term -|U|^2/3.
The Hessian kernel has zero spherical mean. Subtracting the local
smooth tensor density makes its singularity integrable. A distant
dyadic annulus contributes at most C R^(-3)E_y(2R)=O(R^(beta-3)),
which is summable. On any compact observation set, split into a compact
smooth source and a distant source. Every derivative of the latter
falls on the kernel and improves its distant decay. Thus P0 is smooth.
Truncate the tensor source, apply -Delta to the resulting potentials,
and pass to the locally convergent limit to obtain
-Delta P0=partial_i partial_j(U_i U_j)=q. This imposes no global
bound on derivatives of U.

Near0, U=a0 Jy and M=a0 J commutes with J. The pressure-free momentum
for any real c,omega is

    (1-c)My+M(cI-omega J)y+M^2y+omega JMy
        =(M+M^2)y.

Since M^2 is symmetric, its curl is zero, whereas curl(My)=2a0 e3.
The nonzero residual curl cannot be canceled by the gradient of any
C1 pressure, even distributionally. It also excludes every harmonic
addition to P0. Thus no member is a full Euler profile.

## 8. Verification and full-profile interpretation

All eight source sections at01c99ad4, all42manual checks and the formal
scope note were read and independently reconstructed. No mathematical
computation or formal build was used. The existing configured model C comparison of08:58:26Z was read in full
and checked as detailed in Section9. Actual provider execution is
independently unattested.

For nonzero bounded C1/C1 full profiles with Hb,2/5<c<1/2 and any
finite omega, A3053 supplies beta=5-2/c and the energy law. Thus the
lower bound applies with weight2-beta=2/c-3. Its sharpness in the
larger kinematic class does not prove sharpness for full profiles and
does not settle automatic source integrability or nonexistence.


## 9. Independent check of the C comparison and its refinements

The complete nine-part C comparison agrees with the construction, including
the necessary order of limits, exact derivative cross term, all-center
error and local momentum obstruction. Its reported numerical and symbolic
runs were not executed here and are not the proof. Only the algebraic and
analytic statements verified below are incorporated.

The choice p<3 is redundant but harmless in the stated window. In fact

    A/D=(beta^2-4beta+7)/(-beta^2+2beta+3),
    (A/D)'=-2(beta^2-10beta+13)/(-beta^2+2beta+3)^2<0

for0<beta<1. Its endpoint values are7/3 and1, so1<A/D<7/3<3.
This proves the parameter window without a grid.

For the unrescaled oscillator, write I_p=integral_0^infinity
(1+u^2)^(-p/2)du<infinity. The substitution s=delta u, followed by
splitting the integral at s=1/2, gives

    integral_over_period z'^2=4 I_p delta^(1-p)+O(1).

To check the bounded error, the missing tail of I_p contributes O(1)
after multiplying by delta^(1-p). On s<=1/2 use
|sqrt(1-s^2)-1|<=C s^2; its error is bounded by
C integral_0^(1/2) s^2(delta^2+s^2)^(-p/2)ds, uniformly finite for p<3.
On s>=1/2 everything is uniformly integrable. The period remains bounded
above and below. Since the negative source integral is uniformly bounded,
its ratio to derivative energy is O(delta^(p-1)). No numerical convergence
rate is needed to choose a sufficiently small positive delta.

The tangential term in Section2 gives a useful consequence for any field
with the precise energy law, not only the constructed examples. If
limsup H_a(R)/(L log R)<=k_beta+epsilon, then

    limsup F_tan,a(R)/F_a(R)
       <=epsilon/[beta^2(2-beta)].

Indeed H_a>=k_beta L log R+beta(2-beta)F_tan,a-C_a and
F_a=beta L log R+O(1). Divide these inequalities by L log R.
The compact difference between lower radial cutoffs1 and2 is immaterial.
This says that near-minimal source coefficient forces small tangential
energy fraction in the logarithmic average. It asserts neither pointwise
radiality nor automatic bounds on the gradient moment. For the constructed
family, F_tan/F tends to G_n/K_n=O_delta(n^(-2)), consistently with this
consequence.

No minimizer or optimal full-Euler coefficient is established. The generic
profile question, automatic critical integrability and the behavior at
beta=0 or beta=1 remain outside this result.
