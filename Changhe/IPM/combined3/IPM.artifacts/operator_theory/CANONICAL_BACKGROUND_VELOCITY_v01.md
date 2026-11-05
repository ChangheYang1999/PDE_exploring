# The growing background has a canonical whole-plane IPM velocity

Status: proved from the exact finite-potential structure. This identifies
the velocity convention in a final existence theorem; it supplies no new
numerical energy bound.

Let rho be smooth and central odd, with all-order bounds
|D^alpha rho(X)|<=C_alpha< X >^(s-|alpha|), where0<s<1. Let theta_R be
any smooth radial cutoff equal to one on r<=R and zero on r>=2R. Then
\[
u_can=\lim_{R\to\infty}U[\theta_R\rho]
\]
exists in C-infinity on compact sets and is independent of the choice of
radial cutoff. It has u_can(0)=0, is central odd, grows at most as< X >^s,
and satisfies
\[
\operatorname{div}u_can=0,\qquad
\operatorname{curl}u_can=-\rho_x,\qquad
\Delta u_can=(\rho_{xy},-\rho_{xx}).
\tag{1}
\]
The multiplier convention is the campaign's
\(m_U(\xi)=(\xi_1\xi_2/|\xi|²,-\xi_1²/|\xi|²)\).

## Convergence and growth

The nonlocal kernels obtained by differentiating -(2pi)^-1 log r are even,
homogeneous of degree-2, and their first derivatives are O(r^-3). The
second component also has its usual local multiple of rho; that causes
no issue because rho(0)=0. On every centered radial annulus,
\(\int K(-Y)\rho(Y)dY=0\) by central oddness. Thus the far part can be
written with K(X-Y)-K(-Y), and is absolutely integrable, bounded by
\(C|X|\int_{2|X|}^\infty r^{s-2}dr\).
For X in a fixed compact set its omitted tail is O(R^(s-1)). Every positive
X-derivative has an absolutely integrable tail directly, with bound
O(R^(s-m)) at derivative orderm>=1. This proves the local smooth limit
and cutoff independence. Principal values near X are legitimate because
rho is smooth and the kernels have zero angular mean.

For |X|=r large, the near principal value uses the difference
rho(X-z)-rho(X), giving a bound Cr^(s-1) integral_0^(r/2) dz=O(r^s).
The rest of |Y|<=2r is O(r^s) after excluding that near region. The
renormalized far bound displayed above is O(r^s). The local kernel term
has the same growth. This proves the claimed sublinear velocity growth.

The Fourier multiplier identities for each compact rho cutoff give(1).
Passing to the local limit proves them for u_can. Central oddness and
the value at zero hold for every cutoff and survive the limit.

## Identification with the actual Candidate013 finite formulas

The exact structural verifier gives s=1/c in(0,1), rho* in S^s and
u* in S^s, with their required parities. The two explicit potential pieces
are
\[
\rho_{007}=-\Delta\partial_y\chi_{007},\quad
u_{007}=(-\chi_{xyy},\chi_{xxy}),
\]
\[
h_*=-\Delta\phi,\quad U[h_*]=(-\phi_{xy},\phi_{xx}).
\]
Direct differentiation proves (1) for their sum u*, with rho=rho*.
Consequently u_can-u* is entire harmonic and O(< X >^s). The standard
mean-value derivative estimate at radiusR bounds its gradient at every
fixed point by C R^(s-1), which tends to zero. The difference is constant;
central oddness forces that constant to be zero. Therefore
\[
\boxed{u_*=U_can[\rho_*].}
\]
This identification does not assign an undefined multiplier product at zero
frequency and does not leave an arbitrary affine velocity in the theorem.

For a correction k in the Q ball, k belongs to Hq withq>2. Its ordinary
L2 Riesz velocity belongs to Hq and is C1,alpha for everyalpha<q-2.
Radial cutoffs converge to k in Hq, so their velocities converge to U[k]
there and locally in C1. Hence the total density rho*+k has canonical
velocity u*+U[k]. This is exactly the velocity used in the maximal
generator and fixed-point equation.

Finally div u=0 and curl u=-rho_x imply that -u-(0,rho) is curl free.
The simply connected plane therefore admits a pressure p with
u=-grad p-(0,rho). Thus a fixed point satisfying the stationary transport
equation supplies the full whole-plane stationary IPM system, with the
same exact c and the canonical central-odd velocity normalization.

For the actual finite center there is also a direct pressure formula,
supplied by the finite-rank agent and checked here:
\(p_*=\partial_{yy}\chi_{007}+\partial_y\phi\).
Indeed -partial_x p*=u*1, while -partial_y p*-rho*=u*2 by the defining
Laplacian identities. Thus the actual center Darcy relation can be checked
without any Fourier extension at all. The correction pressure is then
obtained from the ordinary L2 multiplier as above; the canonical-velocity
argument additionally identifies the symmetric-radius convention.
