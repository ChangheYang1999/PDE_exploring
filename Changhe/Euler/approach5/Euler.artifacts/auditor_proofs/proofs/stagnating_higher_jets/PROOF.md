# Higher-order admissible jets that cannot be limits of solution jets

## Exact statement

Fix 0<c<1/2, omega in R and k>=5. Put kappa=1+c, A=cI-omega J. At a fixed point y with a fixed pressure value p, write the velocity jet as

    z=(b,U_1,...,U_k), b=Ay+U_0,

where U_n is a divergence-free homogeneous vector polynomial of degree n in the displacement x. Set

    B_z=b+Ax+sum_{n=1}^k U_n,
    W_z=curl(sum_{n=1}^k U_n),
    V_z=[B_z,W_z]+kappa W_z.

Let Adm_k consist of those z for which the homogeneous terms of V_z of degrees 0 through k-2 vanish. Let N_k be its subset b!=0. These are the velocity parts of the admissible k-jets of the rotating Euler equation; the pressure derivatives through order k are uniquely determined by them, and p is free.

The C28 claims have the following exact conclusions.

1. N_k is a smooth semialgebraic submanifold of dimension 2k^2+6k+3.
2. Adm_k contains a semialgebraic family with b=0 of dimension 2k^2+8k-6. Its dimension is strictly larger than that of the closure of N_k.
3. There is a smooth scalar function Psi of (y,U_0,...,U_k,p) whose formal derivative along B vanishes at every admissible (k+1)-jet, yet whose value on Adm_k is not determined by (y,U_0,p).
4. This Psi is identically zero on the jets of every actual local Ck solution. The construction supplies no useful Lyapunov quantity for solutions, global or local.
5. Every nonstagnating admissible jet is realized by a local analytic solution. Thus the closure of N_k equals the closure, in these jet coordinates, of the jets of local analytic solutions, and also of the jets of local Ck solutions.

The finite-jet counterexample concerns exactly the literal all-admissible-jets classification. The corrected classification on the closure of N_k remains open for k>=3. No conclusion about decay, a global nonzero profile, or a scalar monotonicity obstruction on actual solutions follows from this counterexample.

## 1. Admissibility and two elementary surjections

Let E_n be the divergence-free homogeneous vector polynomials of degree n, and H_n the harmonic homogeneous scalar polynomials of degree n. Then

    dim E_n=(n+1)(n+3), dim H_n=2n+1.

The first formula follows by subtracting the dimension of homogeneous scalar polynomials of degree n-1 from three times the dimension in degree n; divergence is onto by integration of one component. The second follows from the surjectivity of the scalar Laplacian between homogeneous degrees n and n-2, or the elementary harmonic decomposition.

The map curl:E_{n+1}->E_n is onto. Indeed its kernel consists exactly of gradients of elements of H_{n+2}: a curl-free homogeneous polynomial has a homogeneous polynomial potential by the radial primitive, and its divergence-free condition makes that potential harmonic. The kernel has dimension 2n+5, and subtracting this from dim E_{n+1} gives dim E_n.

For any nonzero b, the map b.grad:E_{n+1}->E_n is onto as well. Rotate and scale so b.grad=partial_1. Given Q in E_n, first set L(x)=integral_0^{x1} Q(s,x2,x3) ds. Then

    partial_1 L=Q, div L=Q_1(0,x2,x3).

Subtract integral_0^{x2} Q_1(0,s,x3) ds from L_2. This removes the divergence without changing partial_1 L and preserves the homogeneous degree n+1.

The exact curl of the pressure-free Euler momentum expression is V_z. Its homogeneous momentum terms through degree k-1 have zero curl precisely when the V_z terms through degree k-2 vanish. A homogeneous curl-free vector polynomial has a unique homogeneous scalar primitive up to the separate constant. Consequently the pressure coefficients P_1,...,P_k exist and are unique exactly on Adm_k. This uses the full curl identity, not a pressure Poisson equation alone.

## 2. Dimension of the nonstagnating set

The degree-j constraint has the form

    (b.grad)curl U_{j+2}+R_j(b,U_1,...,U_{j+1})=0,
    0<=j<=k-2.

No higher coefficient enters it. Also div V_z=0, because div B_z=3c and div W_z=0, so this constraint takes values in E_j. By the two surjections, its diagonal map from U_{j+2} onto E_j is onto. The full constraint derivative is block triangular with onto diagonal blocks. It is a submersion wherever b!=0.

The ambient dimension is 3+sum_{n=1}^k dim E_n. Subtracting the dimensions of the constraints gives

    dim N_k = 3+sum_{n=1}^k dim E_n-sum_{j=0}^{k-2} dim E_j
            = dim E_{k-1}+dim E_k
            = 2k^2+6k+3.

All defining equations are polynomial, and b!=0 is a polynomial inequality. Thus N_k is semialgebraic as well as smooth.

## 3. A larger stagnating family

Set m=k-2 and choose

    lambda=-kappa/(m-1), mu=3c-2lambda, delta=mu-lambda>0,
    D0=[[mu,2omega,0],[0,lambda,0],[0,0,lambda]],
    T0=[[1,-2omega/delta,0],[0,1,0],[0,0,1]], S0=D0-A.

S0 is symmetric with trace zero, and D0=T0 diag(mu,lambda,lambda) T0^-1. Let R_theta be rotation about e3 and set

    S_theta=R_theta S0 R_theta^-1,
    T_theta=R_theta T0, D_theta=A+S_theta.

Since R_theta commutes with A, D_theta=T_theta diag(mu,lambda,lambda) T_theta^-1.

For arbitrary homogeneous scalar F,G of degree m in x2,x3 put

    Wtilde=(-x1(partial_2 F+partial_3 G),F,G),
    W_theta(x)=T_theta Wtilde(T_theta^-1 x).

Its divergence vanishes. Every monomial in Wtilde has bracket weight (m-1)lambda=-kappa under the diagonal field diag(mu,lambda,lambda)x, including its first component: its first-coordinate weight mu cancels the vector component's mu. Hence

    [D_theta x,W_theta]=-kappa W_theta.

Fix a linear right inverse rho:E_m->E_{m+1} of curl. Construct jets by

    b=0, U_1=S_theta x,
    U_j=grad h_{j+1}, h_{j+1} in H_{j+1}, 2<=j<=k-2,
    U_{k-1}=rho W_theta+grad h_k, h_k in H_k,
    U_k arbitrary in E_k.

Their first possibly nonzero vorticity degree is m. Thus the constraints below degree m vanish, while the degree-m constraint is exactly the displayed bracket identity. These jets belong to Adm_k.

The parameter dimension is

    1+(k^2-9)+2(k-1)+(2k+1)+(k+1)(k+3)
      =2k^2+8k-6.

Here k^2-9 is the sum of dimensions of H_3 through H_{k-1}; the separate 1 counts theta. This placement of parentheses avoids an ambiguous equality in the source's parameter-count sentence.

The parametrization is an immersion and is locally injective. Its derivative in theta is detected by U_1 because [J,S0] has entry12 equal to delta!=0. The successive U_j recover the lower harmonic polynomials. Given theta, curl U_{k-1} recovers W_theta and hence F,G, and subtraction recovers h_k. Finally U_k is a free coordinate. Use a sufficiently small theta interval and small boxes in the other parameters. Rationally parametrizing the rotation by t=tan(theta/2) makes the image semialgebraic, by the polynomial projection theorem, with precisely the displayed dimension.

The only general real-algebraic dimension facts used here are that a semialgebraic image is semialgebraic, an injective local immersion has the dimension of its parameter box, and the closure of a semialgebraic set has the same dimension as that set. These are standard semialgebraic dimension theorems, as explicitly identified in C28; no numerical rank check replaces them.

## 4. The scalar bump and its formal derivative

The dimension difference is 2k-9>0. Therefore the family from Part3 cannot be contained in cl(N_k). Choose z0 in the family outside that closed set and r>0 such that B(z0,r) is disjoint from cl(N_k). Let phi be a smooth function supported in B(z0,r/2) with phi(z0)=1, and put

    Psi(y,U_0,...,U_k,p)=phi(Ay+U_0,U_1,...,U_k).

At an admissible (k+1)-jet with b!=0, its k-truncation belongs to N_k and lies outside the closed support of phi. Every first derivative of Psi there is zero. At b=0, every term in the formal B derivative contracts a derivative with b and is zero. In particular the derivative of Ay+U_0 along B is (A+DU)b, also zero. Thus d_B Psi=0 at all the required jets.

The zero derivative jet z1=(0,0,...,0) is admissible and belongs to cl(N_k), approached by (b_n,0,...,0) with b_n!=0 tending to zero. At fixed y,p it has the same U_0=-Ay as z0. But Psi(z1)=0 and Psi(z0)=1. This proves failure of the literal classification on Adm_k.

## 5. Why actual local solutions never see this bump

For an actual local Ck profile on an open Q, the set B!=0 is dense: B=0 on a nonempty open subset would imply div B=0 there, contradicting div B=3c. At the nonstagnating points its k-jet is in N_k and Psi is zero. Continuity of the k-jet then gives Psi=0 everywhere on Q. In particular every stagnating jet of an actual Ck profile belongs to cl(N_k).

For completeness, the local analytic realization used to identify the closure can be checked at every finite order. Rotate coordinates so the first component b_1 is nonzero. The equation and divergence condition have analytic Cauchy-Kovalevskaya form

    partial_1 U_1=-partial_2 U_2-partial_3 U_3,
    partial_1 P=-[(1-c)U_1-b_1(partial_2 U_2+partial_3 U_3)
                  +b_2 partial_2 U_1+b_3 partial_3 U_1+omega(JU)_1],
    partial_1 U_i=-b_1^-1[(1-c)U_i+b_2 partial_2 U_i
                         +b_3 partial_3 U_i+omega(JU)_i+partial_i P], i=2,3.

Use polynomial Cauchy data with the prescribed tangential k-jets of U and P. The analytic existence theorem produces a local solution. Induction on the number of normal derivatives shows its full k-jet is the prescribed one: the differentiated normal equations impose exactly the same relations as finite-jet admissibility. This is the all-finite-orders argument already present in Proposition5.3/A090, not an inference from only first-order realization.

Hence N_k is contained in the analytic solution jets; all actual Ck solution jets lie in cl(N_k); analytic solutions are Ck. Taking closures proves the asserted equality of the three closures. The Cauchy-Kovalevskaya existence theorem is the named external analytic input. It says nothing about extension to a decaying entire solution.

## Verification record

The full C28 statement and proof, the normal-form realization proof and the higher-order warning were read. The dimension and monomial calculations above were redone by hand for arbitrary k,c,omega. The source's finite exact-arithmetic scripts were not executed: they are unnecessary for the universal proof and a few parameter checks would not establish it. Source snapshots and hashes are retained alongside this file. No formalization, server or remote computation was used.
