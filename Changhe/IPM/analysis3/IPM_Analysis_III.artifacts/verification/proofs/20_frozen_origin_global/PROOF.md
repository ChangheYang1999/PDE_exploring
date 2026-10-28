# The global frozen origin operator with an explicit jet coordinate

Status: proved. This audits Theorem O in the fixed theory author snapshot stored in
`evidence/lead_snapshot.md`. The global domain is essential.

## Exact spaces and statement

Let A>0, D=2A+1, b0=(A+3)/2. Assume
5/2<a<9/2, 0<=b<3/2, a+b>4, and
kappa=b0+aA-bD>0. Put sigma=a+b-4>0,
w(x,y)=|x|^{-2a}|y|^{-2b}, and let R=L2(w dxdy) in the real parity class
h(-x,y)=h(x,y), h(x,-y)=-h(x,y). Derivatives below are distributional on
open quadrants. Put Y0=-Ax partial_x+Dy partial_y and
D_R={u in R:Y0u in R}, with its graph norm. Let
G=L2(R,e^{-2sigma t}dt).

For J in R, v in G, u in D_R, define
 beta(t)=J+integral_{-infinity}^t v(s)ds,
 h(x,y)=x^2 y beta(log r)+u(x,y).
The integral converges at every finite t by Cauchy-Schwarz. Give these
objects the norm
 ||h||_Z^2=|J|^2+||v||_G^2+||u||_R^2+||Y0u||_R^2.
Define F={x^2 y gamma(log r)+f:gamma in G,f in R}, with squared norm
||gamma||_G^2+||f||_R^2. Both decompositions are unique modulo almost
everywhere equality. They are Hilbert spaces via the displayed coordinates.

The operator T0=Y0-1 maps Z boundedly onto F. Its kernel is precisely
span{x^2 y}; J is a continuous coordinate of norm1. The inverse selected
by J=0 is

 v=gamma/D,
 u=T0_R^{-1}(f+(A+D)x^2 y cos^2(theta)gamma(log r)/D).

On R the closed maximal operator T0_R:D_R->R is bijective and
||T0_R^{-1}||_{R->R}=1/kappa. The same sharp bound holds if both spaces
carry the norm formed from all conormal derivatives
(x partial_x)^i(y partial_y)^j of total order at most an integer m>=0.

## Closed realization and sharp inverse

On the positive quadrant put u1=log x,u2=log y and
 alpha=1-2a, beta0=1-2b.
The unitary map to L2(R2,du1du2) multiplies h(e^{u1},e^{u2}) by
exp((alpha u1+beta0 u2)/2). It conjugates T0 to

 -A partial_{u1}+D partial_{u2}-kappa.

Parity copies this realization to the other quadrants. Fourier transformation
therefore gives the multiplier -kappa+i(-A xi+D eta), on its maximal
multiplication domain. That domain is closed; compact smooth functions in
logarithmic coordinates form a core by cutoff and convolution. The inverse
multiplier has modulus at most1/kappa. By Fourier functions supported in
an arbitrarily narrow strip about -A xi+D eta=0, this bound is sharp.
The transport resolvent is equivalently the Bochner integral

 T0_R^{-1}f=-integral_0^infinity exp(-s) f(x exp(-As),y exp(Ds)) ds.

Indeed the integrand's R norm is exp(-kappa s)||f||_R, and differentiation
on the core gives T0_R times this integral equal to f. Closure then gives
the formula on R. Conormal derivatives conjugate to constant coefficient
derivatives minus constants; they commute with this multiplier. The upper
bound passes to their sum-of-squares norm, and Fourier localization near
the same line gives sharpness for each finite m.

## Jet decomposition, image and right inverse

If x^2 y gamma(log r) is in R, Tonelli's theorem in polar coordinates
shows that gamma=0 almost everywhere: its angular norm includes
integral |cos theta|^{4-2a}|sin theta|^{2-2b}dtheta=infinity.
This proves uniqueness. The primitive operator v -> beta-J is bounded on
G with norm1/sigma. For example, writing v(t)=exp(sigma t)z(t), its
weighted primitive is convolution with exp(-sigma s)1_{s>=0}, whose L1
norm is1/sigma. It also tends to0 at negative infinity since
|beta(t)-J| <= exp(sigma t)||v||_{G,(-infinity,t)}/sqrt(2sigma).

Since T0(x^2 y)=0, direct differentiation gives

 T0(x^2 y beta(log r))
 =x^2 y Dv(log r)-(A+D)x^2 y cos^2(theta)v(log r).

The remainder term has R norm C_ang||v||_G, where

 C_ang^2=2 B((9-2a)/2,(3-2b)/2).

The radial exponent is exactly8-2a-2b=-2sigma. The angular beta integral
is finite under the stated strict inequalities. Thus T0 maps Z into F
boundedly, and matching its two unique coordinates gives the claimed
right inverse. In particular

 ||u||_R <= kappa^{-1}(||f||_R+(A+D)C_ang||gamma||_G/D),
 ||Y0u||_R <= (1+kappa^{-1})(||f||_R+(A+D)C_ang||gamma||_G/D).

These inequalities and ||v||_G=||gamma||_G/D prove boundedness of the
selected inverse in the full graph norm. If T0h=0, uniqueness of the image
decomposition gives v=0 and T0_Ru=0; hence h=Jx^2 y. No approximate kernel
exists on the selected subspace J=0 in this norm. This is a statement on
all of R2 with the specified product weight, not a boundary-free theorem
on a bounded origin neighborhood.

## Local strain as a continuous extension

For h in Z define the truncated strain functional by its absolutely
convergent integral

 c_<[h]=(1/pi) integral_{r<1} h(X) sin(3theta) r^{-3} dX.

Then

 |c_<[h]| <= |J|/8
   + ||v||_G/[8 sqrt(sigma(sigma+1)(sigma+2))]
   + C_R ||u||_R,

where
 C_R^2 = 2[9 B(a+1/2,b+3/2)-24 B(a+1/2,b+5/2)
                    +16 B(a+1/2,b+7/2)]
                /[pi^2(2a+2b-4)].

For the jet, the angular integral is pi/4. Fubini gives
c_<[x^2 y(beta-J)]=(1/8)integral_{-infinity}^0(1-exp(2s))v(s)ds.
Its G dual norm is the stated constant, using
integral_{-infinity}^0(1-exp(2s))^2exp(2sigma s)ds
=1/[sigma(sigma+1)(sigma+2)]. The remainder follows by weighted
Cauchy-Schwarz, the radial integral1/(2a+2b-4), and
sin^2(3theta)=9sin^2(theta)-24sin^4(theta)+16sin^6(theta).
For a smooth admissible density with vanishing first origin jet this is
the usual Biot-Savart strain of h1_{r<1}. On the whole abstract Z space
it is the bounded extension of that functional. One must not claim a
classical derivative h_y(0) for every equivalence class in Z.

For completeness, the latter regularity issue is real. In logarithmic
coordinates set
 s=(-A u1+D u2)/(A^2+D^2), z=D u1+A u2,
so Y0s=1 and Y0z=0. Center disjoint smooth tubes at(u1,u2)=(-nL,-nL),
with fixed small s width and z width
 epsilon_n=exp(-(2(a+b)+2)nL).
Choose height1, product cutoffs in s and z, and extend by parity. Their
R norms squared and Y0 graph norms squared are O(exp(-4nL)); differentiation
along Y0 never differentiates the narrow z cutoff. The sum is in D_R,
smooth away from the origin, but takes value1 along points tending to the
origin and value0 along other such points. Thus D_R need not consist of
continuous functions. Axis values on null sets are not defined by its norm.

## The earlier sequences

The uncut homogeneous angular profile of the degree2 quasimode has
x exponent p approximately1.3227; it fails R membership since2p-2a<-1.
Each angularly and radially cut-off smooth member of the earlier sequence
can belong to D_R; it cannot remain an approximate kernel after normalization
in the present Z and F norms, by the proven bounded inverse. Distinguish the
uncut limiting profile from those actual cut-off members.

For a nonconstant smooth cutoff chi equal1 near0 and0 past a finite radius,
let B_delta=x^2 y[4chi(r/delta)-chi(r/(2delta))]/3. Then J=1,u=0.
Translation in t gives ||v_delta||_G=delta^{-sigma}||v_1||_G, so

 ||T0B_delta||_F
 =sqrt(D^2+(A+D)^2 C_ang^2) delta^{-sigma}||v_1||_G.

This diverges as delta decreases and hence the old nonclosed-J packets do
not converge in this image norm.

For a=7/2,b=6/5: sigma=7/10, C_ang^2=20/3 and
kappa=(8/5)A+3/10. Its value for the modal background is approximately
16.54116. The number16.5 is a permissible lower bound after certification,
not the exact kappa or the sharp inverse norm's exact denominator.
