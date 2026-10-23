# A globally capped exact profile cannot have a flat affine defect

Status: CONFIRMED. Independent informal proof complete; supporting exact symbolic, rational and 65-digit moment checks passed at 21:00:50Z after the preserved checker repair. Date: 2026-10-20.

## Statement and hypotheses

Let ell>1, D=ell-1, A=2ell-1. Let rho,psi be a smooth exact primary profile on R^2:

    W.grad rho=rho, W=ell X+U, U=(-psi_y,psi_x), -Delta psi=rho_x.

Assume the prescribed even-x/odd-y density parity, odd-in-both stream parity, canonical U=o(r), sublinear density growth, and a=rho_y(0)!=0. Add the EXTRA global hypothesis

    ||S(X)||op <= D for every X, S=(DU+DU^T)/2.

Then h=rho-ay is not flat at zero. Combined with the independently proved all-degree Taylor obstruction, its first nonlinear Taylor term has a finite odd degree n>=3 and

    a >= (n-1)A >= 2A=4ell-2 > 0.

In particular the capped subclass has no negative-slope profile. If 2A<=a<4A, its first nonlinear term is cubic. The global cap has not been proved for the principal admissible class, so this is a conditional exclusion, not principal nonexistence.

## Consequences of the cap

The exact origin identity gives DU(0)=diag(D,-D) and W(0)=0. For all X,

    X.U(X) = int_0^1 X^T S(tX) X dt,
    r^2 <= X.W(X) <= A r^2.                                  (1)

The first identity follows by integrating DU along the radial segment; the skew part has zero quadratic form. Local smoothness and (1) give complete trajectories in both time directions: their radii cannot escape a bounded ball in finite time. A nonzero backward trajectory satisfies r(t)<=e^t r(0) for t<=0, so it tends to the origin.

Let g=grad rho. Differentiating exact transport gives

    W.grad g=-Dg-(DU)^Tg,
    (1/2) W.grad |g|^2=-D|g|^2-g^T Sg <= 0.                  (2)

The backward limit of g is a e_y. Hence |grad rho|<=|a| everywhere. Integrating vertically from rho(x,0)=0 yields |rho(x,y)|<=|a||y|. These implications use transport and the cap; they are not consequences of parity alone.

The diagonal entries of DU equal those of S. Parity gives U1(0,y)=U2(x,0)=0, so integration in the corresponding coordinate proves

    1 <= W1/x <= A,  1 <= W2/y <= A,                          (3)

with continuous quotients on the axes. Put V=U2+D y. Then 0<=V/y<=2D. Near zero, the origin Taylor expansion and parity give V/y=O(r^2). Off y=0, q=rho/(a y) tends to 1 on backward trajectories and satisfies W.grad q=-q V/y. Since V/y is integrable backwards by (1), this also proves 0<q<=1. Only the weaker sign below is needed for the contradiction.

Define

    H=y-rho/a=-h/a.

The Lipschitz estimate already proves yH>=0. Exact transport and Poisson give

    W.grad H-H=V,                 Delta V=a H_xx.             (4)

The sign of a in the second identity is essential.

## Weighted moments and their boundary terms

Suppose H is flat. Equation (4) then makes V flat as well, including all fixed-order derivatives. For any real m>2 define

    I_m=int_R2 H y r^(-2m) dX,
    J_m=int_R2 V y r^(-2m) dX.                               (5)

Both integrals converge absolutely. At infinity H,V=O(r), and their radial absolute integrands are O(r^(3-2m)). At zero flatness supplies arbitrarily high powers. Also I_m>0: yH>=0, and H identically zero would make rho=a y, contrary to sublinear growth.

All following integrations are first made on epsilon<r<R. Their outer boundary terms are O(R^(4-2m)); their inner boundary terms vanish by flatness. For the elliptic integrations, use w0=y r^(2-2m), with w0=O(r^(3-2m)) and grad w0=O(r^(2-2m)). First derivatives of H are bounded by (2). First derivatives of V are bounded too: the symmetric part of DU is bounded by the cap, and its skew part is bounded by curl U=-rho_x and (2). Thus the claimed elliptic boundary estimate uses no hidden higher derivative bound at infinity. Twice integrating with smooth annular cutoffs gives the same identities without assuming separate absolute integrability of the unintegrated second-derivative expressions. There is no boundary along the symmetry axis.

Direct differentiation yields

    Delta w0=4(m-1)(m-2) y r^(-2m),
    (w0)_xx=2(m-1)y r^(-2m)(2m x^2/r^2-1).

Applying these to Delta V=a H_xx proves

    J_m = a/[2(m-2)] int H y r^(-2m)(2m x^2/r^2-1) dX.        (6)

The nonnegative measure H y r^(-2m)dX therefore gives

    J_m/I_m <= a(2m-1)/[2(m-2)]       if a>0,
    J_m/I_m <= |a|/[2(m-2)]          if a<0.                  (7)

For negative a, the lower bound 2m x^2/r^2-1>=-1 must be used before multiplying by a; using the upper bound would reverse the conclusion incorrectly.

Integrating the transport identity (4) against y r^(-2m), using div W=2ell, gives

    J_m = int H y r^(-2m)
          [2m X.W/r^2-2ell-W2/y-1] dX.                      (8)

The quotient W2/y extends smoothly to the axis. Bounds (1) and (3) and the positive measure imply

    J_m/I_m >= 2m-4ell.                                      (9)

## Contradiction and scope

As m tends to infinity, the lower bound (9) diverges, whereas (7) stays bounded. An explicit finite choice avoids a limit: for a>0 take m=3+2ell+2a. Then the lower bound is 6+4a, while the upper bound is less than 2a. For a<0 take m=3+2ell+|a|. Then the lower bound is 6+2|a|, while the upper bound is less than 1/2. Both are impossible. Thus H, and equivalently h, is nonflat.

Smoothness and parity give a finite first odd Taylor degree n>=3. The theorem in ../all_degree_strain_cap/PROOF.md applies with precisely the same cap and yields a>=(n-1)A. This proves the remaining conclusions. No analyticity, positivity of an initially prescribed density, finite critical-point assumption, or numerical maximum is substituted for a hypothesis.

Under spatial dilation rho_lambda(X)=lambda rho(X/lambda), H and V scale in the same way, I_m and J_m both scale by lambda^(4-2m), and the cap, a, ell, n and flatness are invariant. The exclusion is therefore independent of the representative.

## Dependencies and verification

The independent origin/parity proof, the canonical curl identity, elementary ODE continuation, and the independently checked all-degree Taylor theorem are the only dependencies. The external source audited is the lead's scap2 Sections 1-2, discussed with actual Claude Opus 5.5 at 20:45 UTC. Its source checker is not reused. The flat-moment argument has been reconstructed here, including the cutoff justification and the negative-slope inequality. Optional non-profile examples in that source are not included in this verdict yet.
