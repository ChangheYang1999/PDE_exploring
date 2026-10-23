# Differentiated transport and the limits of a scalar coefficient

Date: 2026-10-20. Status: the identities and domain qualifications below are independently checked by differentiation and the proved symbol bounds. Exact algebra tests are queued. These facts give no existence or nonexistence endpoint.

## 1. Statement and domain

Let (rho,ell) be an exact smooth primary full-plane IPM profile. Thus ell>1, rho is even in x and odd in y, a=rho_y(0)!=0, U=(-psi_y,psi_x) is the canonical sublinear inverse of -Delta psi=rho_x, and W=ell X+U satisfies W.grad rho=rho. Assume the primary value and gradient growth condition with some exponent gamma in (0,1). Put A=2ell-1 and p=1/ell. The independently proved origin relation gives DW(0)=diag(A,1). Result32 gives |D^k U|+|D^k rho|<=C_k r^(p-k) for large r and every k.

For smooth h,g solving

    W1 h_x+W2 h_y=h+g,                                    (1)

on the open set W2!=0 the exact differentiated equation is

    W.grad h_x=d h_x-(W2_x/W2)h+g_x-(W2_x/W2)g,
    d=1-W1_x+W1 W2_x/W2.                                 (2)

The smooth quotient b=W2/y, extended to y=0 by b(x,0)=W2_y(x,0), is defined on the whole plane. Wherever b!=0, (2) has the extension

    d=1-W1_x+W1 b_x/b.                                   (3)

In particular b>0 near zero and sufficiently far out. Equation (3) gives

    d(0)=1-A=2-2ell,
    d(X)=1-ell+O(r^(p-1)) as r tends to infinity,          (4)

uniformly in angle, including the x-axis. The latter is a limit of the extended expression. Formula (2) itself is undefined on W2=0.

An interior zero of b is not covered by (3). No theorem in the current work excludes such zeros for every exact profile. Even Hdyn is a statement about zeros of the vector W, not about the sign of its second component. A scalar elimination at a zero of b cannot be used without a separate cancellation argument. The universally valid differentiated system is

    W.grad grad h=(I-(DW)^T)grad h+grad g.                 (5)

Where W1!=0 one may instead eliminate h_x, obtaining the equation for h_y with coefficient 1-W2_y+W2 W1_y/W1. At a zero of W, keep the coupled system. None of these scalar signs alone supplies a global coercivity or nonexistence argument for the nonlocal linearization.

## 2. Differentiation and source extension

Differentiate (1) in x:

    W.grad h_x+(W1_x-1)h_x+W2_x h_y=g_x.

Insert h_y=(h+g-W1 h_x)/W2 to get (2), with all signs as displayed. Differentiating in both variables without division gives (5). For the linearized IPM equation, g contains the nonlocal term -V[h].grad rho and any parameter or residual source. These terms must still be differentiated in (2); d is not the complete linearized operator.

Parity gives W2=y b with

    b(x,y)=integral_0^1 W2_y(x,ty)dt.

It is smooth and even in x and y. Near zero b=1+O(r^2), b_x=O(r), W1=Ax+O(r^3), W1_x=A+O(r^2). Thus d=1-A+O(r^2), proving the first assertion in (4). At an axis point with W2_y!=0, the same extension is W2_x/W2=b_x/b=W2_xy/W2_y. This last formula is an axis limit, not a division by the zero value W2 itself.

## 3. Uniform large-radius bound through the axis

Write b=ell+U2/y. If |y|>=r/2, the symbol estimates give |U2/y|<=C r^(p-1) and |U2_x/y|<=C r^(p-2). If |y|<r/2, then |x|>=sqrt(3)r/2. Every point (x,ty), 0<=t<=1, has comparable radius, so the integral formula and its x derivative give the same estimates from U2_y and U2_xy. Consequently

    b=ell+O(r^(p-1)), b_x=O(r^(p-2))                     (6)

uniformly for all directions. Hence b>=ell/2 sufficiently far out. Since W1=O(r) and W1_x=ell+O(r^(p-1)), (3) and (6) give the second assertion in (4). A pointwise estimate at fixed nonzero angle would not justify this uniform axis conclusion; the two-region argument is needed.

## 4. A canonical nonprofile countertest for division at interior zeros

The following construction illustrates the algebraic risk without claiming a counterexample that solves nonlinear transport. Fix ell>1 and let rho0=4(ell-1)y exp(-r^2). Its canonical stream psi0 has c0=-(ell-1), by the first-mode strain identity; the slope is a0=4(ell-1). Thus the center normalization and source jet hold.

In a small disk about P=(1,1) put

    psi_loc=-ell x y+(x-1)^2/2.

Choose a smooth cutoff equal to one near P and supported in that disk, so that the disk and its three reflected copies are disjoint and stay away from y=0. Extend the patch (psi_loc-psi0) times this cutoff by odd reflection in both axes, and call the resulting compactly supported stream zeta. Define

    eta(x,y)=-integral_(-infinity)^x Delta zeta(s,y)ds.

Because zeta is odd in x, its integral over the x-line is zero. Therefore the integral of Delta zeta is also zero, and eta is compactly supported, smooth, even in x and odd in y. It vanishes near y=0. The pair rho=rho0+eta, psi=psi0+zeta satisfies -Delta psi=rho_x, the canonical gauge, the growth condition and exactly the same a0 and c0. Near P it gives W1=2ell x and W2=x-1. Consequently

    1-W1_x+W1 W2_x/W2=1+2ell/(x-1),

which has a pole at P although W(P)=(2ell,0) is nonzero. These are canonical smooth nonprofile test fields. They show that parity, inverse and center data alone do not justify extending (2) through an interior component zero. No claim about the existence of such a zero in an exact profile is made.

## 5. Two related energy checks

For a compactly supported real potential Phi set h=-Delta Phi. The independently proved potential identity has matrix

    M=(1+2ell)I+sym DU
                   +[[rho_y,-rho_x/2],[-rho_x/2,0]].      (7)

Result32 now gives M=(1+2ell)I+O(r^(p-1)) at infinity, without Hdyn. The earlier derivative caveat was a limitation of the estimates then available, not an obstruction after result32. The spatial scaling sends M_lambda(X) to M(X/lambda), so this conclusion is invariant under the actual scaling.

For a smooth incompressible background with W_b=ell X+U_b, the same source jet and grad rho_b=a e2+O(r^2), define P_b h=W_b.grad h-h+V[h].grad rho_b. If a>=0 and h is smooth, compactly supported in the disk of radius epsilon, then

    ||P_b h||_2 >= [(A+3)/2-C epsilon^2] ||h||_2.          (8)

Indeed incompressibility gives Re< W_b.grad h-h,h>=-(1+ell)||h||_2^2 exactly. The canonical multiplier V2=-xi1^2/|xi|^2 makes a Re<V2[h],h> nonpositive. The remaining pairing is bounded by C epsilon^2 ||V[h]||_2 ||h||_2, and the canonical Fourier multipliers are bounded on L2. Cauchy-Schwarz yields (8). Global boundedness sufficient to define P_b h in L2 is understood, as it holds for the primary backgrounds. This local estimate does not require replacing W_b by its linear Taylor polynomial and does not assert a small operator norm for their transport difference.

Dependencies: inverse, origin, phi_energy, frozen_sobolev and local_ipm_continuation proofs. No external theorem about the scalar coefficient is imported.
