# Independent radial partition of the complete Hessian energies

## Statement and notation

Fix the immutable reference016 or017 and all structural assumptions of ../scaled_hessian_audit/PROOF.md. Put r0=1/50 and R=4178237423365963/500000000000. These are exact rational radii. Partition the plane into D0={r<r0}, Dm={r0<=r<=R}, Df={r>R}. For each ab in {xx,xy,yy}, define E_ab(D)=integral_D |partial_ab rho|^2. This check encloses each of these nine energies and their sums over the whole plane. The preceding complete-plane check is a required input, not a substitute for checking the new primitives.

Set X_D^2=E_xx(D)+E_xy(D), Y_D^2=E_xy(D)+E_yy(D), H_D^2=X_D^2+Y_D^2, and

    kappa_D^2=((log2-1/2)X_D^2+(3log2-2)Y_D^2)/(16pi).

These nonnegative squared quantities add across D0,Dm,Df. Their square roots do not add. The full-plane kappa has the operator interpretation in the audited complete-plane proof. The restricted kappa_D are energy partitions only; no localized Hilbert-Schmidt kernel identity is claimed.

## Exact primitives and proof

The complete-plane proof derives E_ab=(pi/2)sum_ell integral_0^1 v^b(1-v)W_ell(1-v)dv, where b=ell delta/2-1>-1. Reconstruct every W_ell by the independent polar derivative recurrence and complete angular convolution. Let N(v)=(1-v)numerator(W_ell(1-v)) and D(v) its positive denominator. Exact polynomial division and the Chinese remainder identity give

    N(v)/D(v)=sum_j p_j v^j+sum_(a,k) c_(a,k)/(1+av)^k.

The identity is replayed with exact rational polynomials. For 0<V<=1 each polynomial term has primitive p_j V^(b+j+1)/(b+j+1). For every pole, the substitution v=Vu and the Euler integral yield

    integral_0^V v^b/(1+av)^k dv
      =V^(b+1) 2F1(k,b+1;b+2;-aV)/(b+1).

Here a>0 and b>-1, so the integrals converge and there are no singularities on the path. Direct Arb evaluation of this expression supplies outward enclosures, independently of the numerical lane's recurrence in k. Every primitive must have at least150 bits of accuracy at2048-bit working precision.

Write T_ab(V) for pi/2 times the full sum of these primitives. The exact change of variables v=1/(1+r^2) reverses radial order. Hence

    E_ab(Df)=T_ab(1/(1+R^2)),
    E_ab(Dm)=T_ab(1/(1+r0^2))-T_ab(1/(1+R^2)),
    E_ab(D0)=T_ab(1)-T_ab(1/(1+r0^2)).

These identities prove additivity, including boundaries of zero area. Positivity follows from their spatial definitions and is checked numerically for the actual candidates. Compare every complete primitive T-group at V=1 with the preceding independent full-plane calculation, and every primitive and final energy with the frozen peer record. Signed branch groups can cancel; no groupwise positivity assumption is used.

For a quantity Q in {X,Y,kappa}, the omitted squared fraction is (Q_D0^2+Q_Df^2)/Q_whole^2 and the far fraction of the omission is Q_Df^2/(Q_D0^2+Q_Df^2). The full-minus-annulus norm difference is a difference of the independently enclosed roots. Comparing the exact annulus norm to a saved FLOAT value does not identify the difference with quadrature error: the FLOAT computation also rounds coefficients and operations. No generic error bound for that computation follows.

## Mesh and scope

The nominal exact annulus above is unambiguous. The Gaussian nodes selected by a FLOAT cutoff are a separate object. A reconstruction of the stated Gaussian panels can establish how many panels the saved diagnostic selected, but cannot make the FLOAT quadrature into an interval certificate. This check uses no quadrature for the energies. A mesh audit, if included, is explicitly labeled FLOAT and compares the source text and selected nodes only.

The partition supplies neither a global theta bound nor an inverse estimate or existence proof. Exact source hashes, proof, code and numerical evidence are recorded alongside. The informal argument is checked before execution. All foreign code is read only as text.
