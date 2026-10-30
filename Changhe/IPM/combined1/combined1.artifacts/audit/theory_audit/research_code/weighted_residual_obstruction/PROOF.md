# A residual tail outside the weighted correction class cannot be cancelled

Status: independent audit of T2 the review of T4-189, Remark R3. The theorem
below is analytic; individual candidate applications require an exact
nonzero leading residual and a uniform remainder estimate.

## Statement

Let gamma<1, a<=2 and c be real. Put w_a=(1+|X|^2)^(-a/2).
Let rho,u be smooth fields on R2 with div u=0 and, for |X|>=1,

    |u(X)|<=C_u |X|^gamma,
    |grad rho(X)|<=C_rho |X|^(gamma-1).

Define F=(cX+u).grad rho-rho. Suppose for some q>=a-1,

    F(r,theta)=r^q E(theta)+o(r^q)

uniformly in angle, where E is a smooth nonzero real angular function.
There do not exist h,v in L2(w_a^2 dX), with div v=0 in distributions,
satisfying

    F+c div(Xh)-(2c+1)h+div(uh)+v.grad rho+div(vh)=0

in distributions. This applies in particular to v=U[h] whenever its
canonical weighted definition has the stated norm. No smallness is needed.
Parity is unnecessary for the stated conditional result.

## Proof

Take smooth eta>=0, supported in 1<r<2 and nonzero, and set
psi(Y)=eta(|Y|)E(arg Y), phi_R(X)=R^-1 psi(X/R). Then

    int F phi_R = R^(q+1)(A+o(1)),
    A=int |Y|^q E(arg Y)^2 eta(|Y|) dY>0.

Put m_R=||w_a h||_(R<r<2R), n_R=||w_a v||_(R<r<2R).
Both tend to zero. For R>=1 and r in this annulus,

    w_a^-1 <= C_a R^a,  C_a=5^(max(a,0)/2).

For a<0 this follows from (1+r^2)^(a/2)<=r^a<=R^a;
for a>=0 it follows from 1+r^2<=5R^2.
The four correction contributions are bounded as follows:

    |int h[c X.grad phi_R+(2c+1)phi_R]|
       <=C_a R^a m_R (|c| ||Y.grad psi||2+|2c+1| ||psi||2),
    |int h u.grad phi_R|
       <=C_a C_u max(1,2^gamma) R^(a+gamma-1) m_R ||grad psi||2,
    |int phi_R v.grad rho|
       <=C_a C_rho R^(a+gamma-1) n_R ||psi||2,
    |int h v.grad phi_R|
       <=C_a^2 R^(2a-2) m_R n_R ||grad psi||infinity.

The second estimate uses r^gamma<=max(1,2^gamma)R^gamma;
the third uses gamma-1<0. The test norms follow by X=RY.
Divide the correction equation by R^(q+1). Because q+1>=a,
a+gamma-1<a and 2a-2<=a, every displayed power after division
is nonpositive. Each term contains m_R or n_R and therefore vanishes.
The residual term tends to A>0, a contradiction.

## Meaning of the threshold and scope

The uniform nonzero leading term r^q E belongs to the exterior weighted
L2 space exactly when q<a-1: its radial square integral is comparable to
int_R^infinity r^(2q-2a+1) dr. At q=a-1 it diverges logarithmically.
Thus throughout a<=2 a residual outside this space cannot be removed by
any correction with h and v inside it. This is a nonexistence theorem
for that entire affine class, not merely failure of a contraction estimate.
It is not global nonexistence of a profile with different asymptotic data.

The same proof works for a>2 if q>=max(a-1,2a-3); that is a separate
stronger hypothesis and does not assert the membership-threshold result
for a>2. No candidate number is certified by this abstract proof alone.

Dependencies: weighted Cauchy-Schwarz, local products of L2 functions,
uniform leading-tail convergence and the displayed scaling calculation.
