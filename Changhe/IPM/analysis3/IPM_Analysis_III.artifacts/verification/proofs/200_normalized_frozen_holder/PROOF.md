# The normalized frozen Holder operator with localized coupling

## Statement

Fix 0<alpha<1 and1<=p<2. Use the Banach space E_p, canonical full-plane velocity U, C4 parity-compatible background rho and cutoff chi_delta of proof 199. Thus h is bounded, even in x and odd in y, h(0,y)=0, and

 ||h||_(E_p)=||h||_infinity+[h]_x+[h]_(y,p).

The central strain is the absolutely convergent integral

 c[h]=(1/pi) integral_(R^2) sin(3theta) r^(-3)h(X)dX.

Let A>0,D=2A+1, kappa_p=1+pA-Dalpha>0, and define

 T0=-Ax partial_x+Dy partial_y-1,
 H_delta=chi_delta X.grad rho/3,
 L_delta h=T0h+chi_delta U[h].grad rho+c[h]H_delta.    (1)

Its domain is D(T0)={h in E_p:T0h in E_p distributionally}. There are finite constants C_B and C_H, depending only on alpha,p and the fixed local background and cutoff, such that

 ||chi_delta U[h].grad rho||_(E_p)
                   <=C_B delta^(2-p)||h||_(E_p),
 ||H_delta||_(E_p)<=C_H delta^(3-p-alpha).             (2)

The first is proof 199. The strain satisfies the explicit bound

 ||c||_(E_p*)<=(4/pi) max(1,1/(p+alpha-1))=:C_c.       (3)

Consequently, if

 q=max(1,1/kappa_p)
      [C_B delta^(2-p)+C_c C_H delta^(3-p-alpha)]<1,   (4)

then L_delta:D(T0)->E_p is an isomorphism and

 ||L_delta^(-1)||_(E_p->E_p)
                  <=max(1,1/kappa_p)/(1-q).           (5)

For every alpha<1, one can choose1<=p<2 with kappa_p>0, and then choose delta small enough for(4). This is a qualitative inverse theorem for the normalized frozen operator with the entire coupling localized by the given cutoff. No derivative of h is in the input norm.

## Strain continuity

Oddness in y gives

 |h(x,y)|<=[h]_(y,p)|x|^p |y|^alpha.

On r<1 insert this bound into the kernel. The radial integral equals1/(p+alpha-1), and the angular factor is

 A_(p,alpha)=integral_0^(2pi)|sin(3theta)|
                  |cos theta|^p |sin theta|^alpha dtheta<=4.

On r>=1 use ||h||_infinity, the angular integral4 and integral_1^infinity r^(-2)dr=1. Therefore

 |c[h]|<=(4/pi)
       ([h]_(y,p)/(p+alpha-1)+||h||_infinity),

which implies(3) for the specified sum norm. The near integral is finite because p+alpha>1. At the origin h=O(r^(p+alpha)); in particular its linear y coefficient is0, so the local distributional correction -h_y(0)/4 is absent. The canonical strain identity and its parity are those of proof 01; no boundary flux or added harmonic velocity enters this functional.

## Norm of the localized strain column

The C4 factorization from proof 199 is

 rho_x=x a1, rho_y=x^2 a2,
 ||a1||_(infinity,B_delta)<=C delta,
 ||D a1||+||a2||+||D a2||<=C.

Thus

 H_delta=(x^2/3) chi_delta(a1+y a2).                  (6)

For each fixed x the supported coefficient on the right has supremum at most C delta and alpha seminorm in y at most C delta^(1-alpha). These bounds follow from the product difference rule and |Dchi_delta|<=C/delta. They apply after extension by0; pairs across the support boundary use the same cutoff differences. Hence

 [H_delta]_(y,p)<=C delta^(2-p) delta^(1-alpha).

Also ||H_delta||_infinity<=C delta^3. Its x Lipschitz bound is at most C delta^2, so the x alpha seminorm is at most C delta^(3-alpha), by splitting differences at length delta. Since0<delta<=1 and p>=1, both terms are bounded by a constant times delta^(3-p-alpha). This proves the second estimate in(2).

## Closed-domain inversion

Let B_norm h=chi_delta U[h].grad rho+c[h]H_delta. Equations(2)-(3) make it a bounded operator E_p->E_p, with norm at most the bracket in(4). Proof 25 proves that T0 on D(T0) is a closed bijection and that its inverse R0 has norm at most max(1,1/kappa_p). Thus

 L_delta=(I+B_norm R0)T0

on the identical domain. Under(4), the Neumann series of I+B_norm R0 converges in operator norm and gives a bounded inverse. Composing with R0 proves(5), surjectivity into D(T0), injectivity there, and closedness of L_delta. There is no changing-domain step in this argument.

Finally Dalpha-1<D-1=2A. Choose p in[1,2) strictly larger than(Dalpha-1)/A. Then kappa_p>0. Both2-p and3-p-alpha=(2-p)+(1-alpha) are positive, so the left side of(4) tends to0 as delta tends to0.

## Scope

This adds the localized scalar strain column to proof 199's localized velocity coupling. The complete expression in(1) is chi_delta(U[h]+c[h]X/3).grad rho plus T0. It keeps the normalization identity and its leading origin cancellation; its boundedness proof does not need to discard either term. It does not include the first-order difference between the actual transport and the frozen saddle. Proof 25's failure of the claimed anisotropic conjugacy transfer therefore remains relevant.

The inverse acts on E_p, which does not have a closed cubic coefficient. It is not an inverse on a space with fixed J=0, a certificate for the full-plane moving-tail operator, a nonlinear closure result or an unconditional existence theorem. C_B,C_H and a usable delta have not been numerically certified. The actual low injectivity(I) and nonlinear smallness(S) remain OPEN.

Dependencies: topics01 and25 for the strain and frozen resolvent, proof 197 for the corrected angular factor, and proof 199 for the directional Holder coupling bound. This proof is a direct consequence once those inputs are accepted. The independent cross-audit is pending together with proof 199.
