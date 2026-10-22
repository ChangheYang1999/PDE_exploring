# Prescribing the first nonlinear tail correction

Written UTC 2026-10-21T03:40:49.852793+00:00 before implementation. Status: complete calculation and trial-space construction below; independent algebraic, Cartesian, inverse and manufactured controls CONFIRMED 2026-10-21T04:03Z. Opus156 returned no written audit. The twelve subsequent stored fits are REFUTED by exact nonzero local PDE coefficients; see runs/first_ladder_search_20261021T0440Z/SUMMARY.md. This is not a profile or an exclusion theorem.

The first correction in powers of r^(-1/beta) cancels the leading nonlinear transport residual. It is distinct from the constant-velocity correction imposed in packet116. Both can be prescribed while keeping independent core coefficients for the center normalization. The formulas below concern this specific two-shift polynomial family with 2<beta<3.

## Statement and notation

Fix 2<beta<3, s=1/beta, m=1-2s, k=2-s and k1=2-2s. In polar coordinates x=r cos(theta), y=r sin(theta), put z=sin(theta). Let P and Q be arbitrary real polynomials of degree at most J-1, where J>=2. Define polynomial operators

    S_k H = -[(k^2-1)H - 3z H' + (1-z^2)H''],
    D_m H = [m+(2-m)z^2]H - z(1-z^2)H'.             (1)

Set A=S_k P and R0=zP-(1-z^2)P'. There are unique polynomials P10,Q10 such that

    S_k1 P10 = -s R0 A + k P[(1-z^2)A'-zA] - D_m Q,
    Q10 = m R0 Q + k P[(1-z^2)Q'-2zQ].              (2)

Both have degree at most 2J-1. For a stream function and temperature with differentiated expansions

    Psi = r^(2-s) cos(theta) P(z)
             +r^(2-2s) cos(theta) P10(z) + lower terms,
    Theta = r^m cos(theta)^2 Q(z)
             +r^(m-s) cos(theta)^2 Q10(z) + lower terms,

and V=(-Psi_y,Psi_x), Omega=-Delta Psi, equations(2) are precisely the vanishing of the coefficients of degrees -2s and 1-3s in

    R_Omega = (beta X+V).grad Omega + Omega - Theta_x,
    R_Theta = (beta X+V).grad Theta -(beta-2)Theta.    (3)

Here lower terms must have strictly lower degree after each derivative needed in(3). A constant velocity does not contribute at either stated degree because s<1.

These relations and packet116's first constant-induced relations can be imposed in a smooth full-plane trial family satisfying all four center conditions. Fix a0!=0, eta real, n>=4 and K=2J. Let R=sqrt(1+x^2+y^2), t=R^-s, z=y/R in the rest of the construction. Define

    B_i(t)=T_i(2t-1)-(-1)^i,                        i>=1,
    E_i(t)=T_i(2t-1)-(-1)^i-2(-1)^(i-1)i^2 t,      i>=2,
    L_c H=c z H+(1-z^2)H'.

Choose leading polynomials P,Q of degree<=J-1. The freely chosen core polynomials are sums of E_i(t)T_j(z), 2<=i<n, 0<=j<K, in shift0 and B_i(t)T_j(z), 1<=i<n, 0<=j<K, in shift1. Define

    p=x R^(1-s)[P(z)+t P10(z)+sum c_ij0 E_i(t)T_j(z)
         +R^-1{(eta/beta)L_(1-s)P(z)+sum c_ij1 B_i(t)T_j(z)}],
    Theta=x^2 R^(-1-2s)[Q(z)+t Q10(z)+sum d_ij0 E_i(t)T_j(z)
         +R^-1{(eta/beta)L_(-1-2s)Q(z)+sum d_ij1 B_i(t)T_j(z)}],
    Psi=p-x p_x(0), V=(-Psi_y,Psi_x), Omega=-Delta Psi.             (4)

Four core coefficients can be eliminated uniquely to impose

    p_x(0)=-eta, Psi_xy(0)=1+beta/2,
    Omega_x(0)=4a0/beta, Theta_xx(0)/2=a0.            (5)

The resulting fields are smooth with B2 parity, Theta(0,y)=0, V(0)=0, V=o(r), and polynomially decaying vorticity. V is the canonical relative full-plane inverse of Omega. The coefficients of degrees(-2s,1-3s) in(3), respectively, vanish exactly, as do the first constant-induced residual coefficients of degrees(-1-s,-2s). No other residual coefficient, positivity condition, or smallness estimate is asserted.

## First correction

Differentiate the leading stream function. Its angular factor is cos(theta)P(z), and

    d_theta[cos(theta)P(z)]=(1-z^2)P'(z)-zP(z),
    d_theta^2[cos(theta)P(z)]
       =cos(theta)[(1-z^2)P''(z)-3zP'(z)-P(z)].       (6)

The polar Laplacian of r^k times an angular factor is r^(k-2)(k^2+d_theta^2) applied to that factor. Thus the leading vorticity is r^-s cos(theta) A(z), with A=S_k P. The leading radial and tangential velocity components are

    V_r=r^(1-s)R0(z),
    V_theta=k r^(1-s) cos(theta) P(z).               (7)

Applying(7) to r^-s cos(theta)A gives

    V.grad Omega_lead
       =r^-2s cos(theta){-s R0 A+kP[(1-z^2)A'-zA]}.  (8)

For the leading temperature r^m cos(theta)^2 Q, the Cartesian x derivative is r^(m-1)cos(theta)D_m Q. Indeed d_x=cos(theta)d_r-r^-1 sin(theta)d_theta, and

    d_theta[cos(theta)^2Q(z)]
       =cos(theta)[(1-z^2)Q'-2zQ].                  (9)

The Euler transport plus linear vorticity term annihilates the leading vorticity because 1-beta s=0. On r^-2s it multiplies by 1-2beta s=-1. The coefficient of R_Omega at degree-2s is therefore cos(theta) times the right side of the first relation(2) minus S_k1 P10. This proves that relation with its sign.

The Euler temperature operator annihilates degree m because beta m=beta-2. It multiplies degree m-s by -1. By(7) and(9), the nonlinear leading temperature transport is r^(m-s)cos(theta)^2 times mR0Q+kP[(1-z^2)Q'-2zQ]. Hence the coefficient of R_Theta at degree1-3s is zero exactly when the second relation(2) holds. Terms involving the subleading velocity have at least one extra factor r^-s, and a constant velocity has an extra factor r^-1 in place of r^-s. Neither changes these coefficients.

## Polynomial inversion

Let U_l be Chebyshev polynomials of the second kind, determined by U_0=1, U_1=2z and U_(l+1)=2zU_l-U_(l-1). Direct differentiation of this recurrence, starting at l=0 and1, gives

    (1-z^2)U_l''-3zU_l'+l(l+2)U_l=0,
    S_k1 U_l=[(l+1)^2-k1^2]U_l.                    (10)

The first identity can alternatively be checked by differentiating U_l(cos(phi))=sin((l+1)phi)/sin(phi), with its polynomial continuation at the endpoints. Since 1<k1<4/3, every eigenvalue in(10) is nonzero. The U_l have nonzero leading coefficients 2^l and form a basis of every finite-degree polynomial space. Expand the right side of(2) in U_l and divide its coefficients by those eigenvalues. This gives the unique polynomial P10 without raising its degree.

The polynomial A has degree<=J-1, R0 has degree<=J, and the nonlinear terms in(2) have degree<=2J-1. D_m Q has degree<=J+1, which is at most2J-1 for J>=2. This proves the degree bound for P10; the degree bound for Q10 follows from its displayed formula. The inversion is not uniformly bounded as beta tends to2: the l=0 eigenvalue 1-k1^2 tends to0. No assertion is made at beta2.

## Center corrections

The functions E_i vanish together with their first derivatives at t=0. Their leading coefficients are those of T_i(2t-1), so E_2,...,E_(n-1) form a basis for polynomials of degree<=n-1 vanishing to order2. In particular

    E_2(t)=8t^2,  E_3(t)=32t^3-48t^2.               (11)

Consequently the shift0 cores change neither P,Q nor P10,Q10. The shift1 cores vanish at t=0 and do not change the first constant-induced coefficients. There is room for all prescribed angular terms because deg P10,deg Q10<=K-1 and deg L_cP,deg L_cQ<=J<=K-1.

Use the stream pivots c_(2,0,0), c_(3,0,0), c_(2,1,0). The moments (p_x,Psi_xy,Omega_x) of x R^q at0 are (1,0,-4q), as direct expansion through degree3 shows. Equations(11) therefore give their moment matrix

    M=[[8,-16,0],[0,0,8],[-32(1-3s),64(1-s),0]],
    det M=-8192s !=0.                               (12)

With these three coefficients zero, let gamma,c,b be the existing moments and put delta_gamma=-eta-gamma, delta_c=1+beta/2-c, delta_b=4a0/beta-b. The unique corrections are

    c_(3,0,0)=[delta_b+4(1-3s)delta_gamma]/(128s),
    c_(2,0,0)=delta_gamma/8+2c_(3,0,0),
    c_(2,1,0)=delta_c/8.                             (13)

The temperature pivot d_(2,0,0) has Theta_xx(0)/2=8. If Acenter is the coefficient before that pivot, set d_(2,0,0)=(a0-Acenter)/8. These adjustments impose(5) while preserving every prescribed tail coefficient.

## Full-plane and serialization scope

Smoothness follows from R>=1 and finite polynomial sums. Parity gives p and Omega odd in x and Theta even in x with its explicit x^2 factor. The affine subtraction in(4) makes V(0)=0 without changing Omega. The slowest velocity and vorticity terms have degrees1-s and-s, so V=o(r), Omega=O(r^-s), and D Omega=O(r^-s-1). The subtracted Biot-Savart kernel converges for this source. Its difference from V has zero divergence and curl, is entire harmonic and sublinear, and vanishes at0; the growing-ball gradient estimate forces it to vanish identically. The required growth estimate on the inverse follows by separating source radii below2|X| and above2|X| and using the subtracted kernel bound on the latter region, as in packet116.

Replacing r by R changes these expansions only at relative degree2. The leading B_i endpoint and E_i endpoint/derivative properties give exactly the stated r^-s coefficients. For noninteger beta in(2,3), none of the raw velocity powers has degree0. Its relative constant term is therefore (0,-p_x(0))=(0,eta). The first constant-induced relations are those of packet115, because no integer step in the r^-s ladder equals r^-1 here. The prescribed shifted leading polynomials in(4) satisfy those relations. No separation at beta2 or beta3 is claimed.

For rational beta,eta,a0 and free leading/core coordinates, all coefficients in(1),(2),(10),(13) are rational. Exact JSON input coordinates determine exact ordinary Chebyshev coefficients, so the center moments and the four residual-tail polynomial identities can be independently checked. The map is polynomial of degree at most2 in the leading P,Q coordinates for fixed beta, affine in each core coordinate and affine in eta. Its derivatives must account for the dependence of P10 on both P and Q. Finite floating-point fits need separate measurement of reconstruction defects.

Dependencies are elementary polar differentiation, the polynomial identities proved above, and the constant-induced identities and canonical inverse argument of packets115/116. The finite angular family remains excluded from exact profiles by packets83/84; this supplies no residual lower bound or obstruction to increasing-resolution limits. No Lean proof or formal build is claimed.

## Coefficient derivatives used in computation

For fixed beta let z consist of eta, the leading coefficients of P,Q and the remaining core coefficients. The ordinary coefficient map D(z) is polynomial of total degree at most two: P10 is quadratic in P plus linear in Q; Q10 is bilinear in P,Q; the shifted leading coefficients are bilinear in eta and P or Q; and the center corrections are linear functionals of these coefficients. Every core coordinate occurs affinely with a direction independent of z. Therefore

    partial_j D(z) = [D(z+e_j)-D(z-e_j)]/2

is an exact identity in rational arithmetic, with no truncation error. In floating arithmetic its rounding error still requires a separate check. For core coordinates the constant direction can be precomputed once. The chain rule through the independently implemented Cartesian differentiation matrices then gives the residual Jacobian. Only the beta derivative uses a centered finite difference in the solver, and it is checked against a five-point difference at a different step. No condition estimate is uniform as beta approaches2.
