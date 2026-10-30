# Independent audit of weighted principal packet caps

## Statement and exact scope

Let c>0, 0<gamma<1, and let rho be a smooth real S1 background, even in x and odd in y. Its smooth canonical IPM velocity is U[rho]=u, where U=(-R1 R2,R1^2), with multiplier (xi1 xi2,-xi1^2)/|xi|^2. Set V=cX+u and Lh=V.Dh-h+U[h].D rho. Assume

    |D^k rho(X)|+|D^k u(X)| <= C_k <X>^(gamma-k)

for every nonnegative integer k. The finite rational campaign profiles have these bounds, as proved in the earlier homogeneity audit. They imply div V=2c, bounded DV, and smooth complete transport.

For any real q and p<3-gamma, take a smooth positive weight w, even in both coordinates, comparable to <X>^p, with |D^k w|<=C_k <X>^(p-k). The campaign weights (1+r^2/R^2)^(p/2), R>0, and omega=(1+4r^2)^(2/5) satisfy these assumptions. Either of the energies

    E(h)=||w J^q h||_2^2,      E(h)=||J^q(w h)||_2^2,
    J=(1-Delta)^(1/2),

has the following necessary condition. If

    Re <Lh,h>_E <= -beta E(h)                              (1)

for every compact smooth real S1 h with canonical strain c[h]=partial_y U2[h](0)=0, then

    beta <= inf_X lambda_min M_(q,w)(X),
    M_(q,w)=(1+c+V.D log w)I-q Sym DV+A,
    A=[[rho_y,-rho_x/2],[-rho_x/2,0]].                    (2)

The same assertion holds for unweighted homogeneous Hdot^-1 energy, with q=-1 and w=1. It also holds for the campaign's weighted order-q top energy with additional lower-order terms, provided those terms and their L-pairings are lower order on the packets below. In particular the finite weighted Sobolev hierarchy with top term ||omega D^2 J^s h||_2 has q=2+s.

This is the version of T1 TP-4 independently established here. The broader statement for arbitrary weights and arbitrary homogeneous orders requires a separate global packet-domain assertion. In particular an arbitrary compact S1 function has Fourier transform O(|xi|) at zero, so homogeneous Hdot^q membership is not automatic when q<=-2. One must not apply that extension without its domain conditions.

## Local packet calculation

Fix X0 away from both axes, a compact real smooth amplitude a supported in a small disk about X0, and a unit frequency direction e. For f_N=exp(iN e.X)a, Fourier translation and expansion near Ne give

    J^q f_N=exp(iN e.X)N^q[a-iq N^-1 e.Da+O(N^-2)].        (3)

The remainder holds in every fixed polynomially weighted L2 norm after taking enough terms and derivatives. To verify this, split translated frequency into |eta|<=N/2 and its complement. The former has the usual Taylor remainder with symbol derivatives bounded by constants times N^(q-k). On the complement the Fourier transform of the compact smooth amplitude and all its derivatives decrease faster than any polynomial. Applying frequency derivatives also controls polynomial spatial weights. The Bessel symbol is smooth at zero, so this works for every real q.

For transport, all amplitudes a, (V.e)a, and V.Da are compact. Apply (3) to L0 f_N, where L0=V.D-1, and to f_N. The order N^(2q+1) term is purely imaginary. At real order N^(2q), the cross terms involving (V.e)(e.Da) cancel and leave

    (V.Da)a-a^2+q(e^T DV e)a^2.

With the weight W=w^2, integration by parts gives

    integral W(V.Da)a
       = integral[-c W-(V.DW)/2]a^2.

Consequently the transport quotient tends, as the amplitude disk shrinks, to

    -c-1-V.D log w(X0)+q e^T Sym DV(X0)e.                (4)

For the other order of w and J^q, write b=wa and use

    w L0 f_N = (V.D-1-V.D log w)(w f_N).

The same calculation gives (4). This direct calculation establishes the sign and coefficient of the weight term without relying on a convention for the Poisson bracket.

## Coupling and exterior control

Near Ne the velocity multiplier is smooth. Its leading value is U(e)=(e1 e2,-e1^2), so the coupling contribution tends to

    U(e).D rho(X0)=rho_x e1 e2-rho_y e1^2=-e^T A(X0)e.

Here it is essential to keep the signed coupling; an absolute Riesz bound would not give the principal matrix.

There is no unaccounted exterior contribution in this calculation. Outside a fixed neighborhood of the amplitude support, the velocity kernel is smooth in the source variable. Integration by parts against exp(iN e.Y) makes U[f_N] and every fixed derivative smaller than every power of N. Its far-field bound is O(N^-M r^-2) for a single unsymmetrized packet; after S1 symmetrization the zeroth source moment vanishes and the bound is O(N^-M r^-3). Multiplying by D rho gives O(N^-M r^(gamma-4)). The restriction p<3-gamma makes this tail and its needed derivatives square integrable after multiplication by w. Bessel operators preserve these polynomial estimates: split their kernels into a local singular part, controlled by derivatives, and an exponentially decreasing exterior part. Alternatively the same assertion follows by the weighted Fourier-derivative argument for a smooth exterior cutoff. Thus the coupling expansion is valid in either energy, not only pointwise near X0.

## S1 symmetry, normalization, and passage to the cap

Reflect the packet into the four coordinate quadrants, reflecting its frequency at the same time and assigning the signs for even x and odd y parity. Use the real part or imaginary part with nonzero amplitude. The four disks are disjoint. The even weight and S1 background make all four local quotients equal. Cross terms are negligible to every algebraic order, using either separated frequencies or the smooth off-diagonal kernel between disjoint supports. For a constant direction on an axis the latter argument still applies. Thus the real S1 packet has quotient tending to the sum of (4) and the coupling value.

These packets vanish near zero. The strain functional away from zero is integration against sin(3theta)/(pi r^3), a smooth kernel on their supports. Repeated integration by parts gives c[h_N]=O(N^-M) for every M. Choose g=-4y eta(r), with eta a smooth radial cutoff equal to one near zero. Its exact strain is1, including the contact term -g_y(0)/4. The sin(3theta) integral annihilates its mode1. Equivalently the local Poisson particular solution is -r^3 sin(theta)/2, whose relevant third derivative gives1.

Replace h_N by h_N-c[h_N]g. This enforces the canonical normalization exactly. The energy of g and Lg is finite under the stated assumptions. Since the uncorrected L-packet grows by at most one power of N relative to the packet norm, this correction changes neither limiting quotient. The resulting quotient is

    -e^T M_(q,w)(X0)e.

Inequality(1), then minimization over e and shrinking the disk, proves beta<=lambda_min M(X0). Continuity reaches the axes and origin; taking the infimum proves(2). Additional lower-order hierarchy terms vanish after division by the top packet energy, so they do not change this necessary condition.

## Homogeneous negative energy

For w=1 and q=-1 use |xi|^-1 in (3). Near Ne the expansion is unchanged. At low frequency the S1 packet has zero mean. Its Fourier transform and its first derivatives there are smaller than every power of N, and the mean-zero identity supplies the additional factor |xi|. Thus the apparent singularity of |xi|^-2 in the squared energy is integrable in two dimensions and contributes a negligible quantity. The same argument applies to Lh_N: its compact transport part is S1, while D rho.U[h_N] is S1 and has an integrable first moment since gamma<1. The exterior estimates above make that first moment negligible to every needed power after removal of the local oscillatory expansion. The corrector g is also mean zero and belongs to Hdot^-1. This proves the stated homogeneous case. No claim for all negative homogeneous orders follows from it.

## Matrix identities and limits

Write chi_ab=partial_x^a partial_y^b chi. For the campaign potential,

    Du=[[-chi22,-chi13],[chi31,chi22]],
    rho_x=-chi31-chi13,      rho_y=-chi22-chi04.

Substitution in(2) gives exactly:

* q=-1,w=1: M=(2c+1)I+Sym Du+A, the A2(B1) matrix.
* q=1,w=1: M1=I-Sym Du+A, the A2(B4) matrix.
* q=1,w=(1+r^2)^(-1/10): the A2 weighted first matrix.
* q=2,w=omega: the A2(B5) matrix.
* q=3,w=omega: the A2(B6) matrix.

The full Cartesian identities for the first three weighted matrices were independently derived in ../global_matrix_audit/PROOF.md. They also follow immediately from the displayed Du and A. With t=r^2/(1+r^2), e0=(X.u)/r^2, the two weight derivatives are -t(c+e0)/5 and16t(c+e0)/[5(1+3t)]. Only their smooth products appear at zero.

At the normalized origin, V=0 and DV=diag(2c-1,1). Testing the vertical direction gives beta<=c+1-q for every weight. More generally, for an elliptic positive homogeneous principal energy symbol m(X,xi) of order2q, the origin bracket term in the vertical direction is q: V=0 removes the X derivative and DV^T e2=e2 permits Euler's homogeneous identity. Thus ordinary classical anisotropic principal symbols do not remove that particular cap.

For power weight exponent p, Du and D rho tend to zero and V.D log w tends to pc. Therefore

    lambda_min M_(q,w) -> 1+c+pc-qc.

A strictly positive contractive gap requires q<1+gamma+p when gamma=1/c. The endpoint also excludes a strictly positive gap. For the A2 top weight p=4/5, q=2+s requires s<gamma-1/5.

## Scope of a gap and of a coefficient weight

A packet cap bounds an available contractive energy rate. It does not lower-bound the norm of an arbitrary stationary inverse. For example L=-aI+bJ on R^2, a>0, J=[[0,-1],[1,0]], has exact numerical-range rate a but ||L^-1||=(a^2+b^2)^(-1/2), arbitrarily smaller than1/a. Thus T1's K_H>=1/0.6115 consequence is justified only for K_H defined as the reciprocal energy-rate certificate, not as a lower bound on the actual inverse norm.

A growing weight also changes the background coefficient hypotheses. Suppose rho=r^gamma G(theta)+o(r^gamma), with its differentiated expansion, G not identically zero and0<gamma<1. Then

    partial_r^2 rho=gamma(gamma-1)r^(gamma-2)G(theta)+o(r^(gamma-2)).

The Frobenius norm of D^2 rho bounds the absolute radial second derivative. Hence for w comparable to r^p with p>2-gamma, ||w D^2 rho||_infinity is infinite. State131 has a nonzero leading G. Therefore the trial p=3/2, although favorable for its sampled principal matrix, fails the existing finite weighted-D2rho background requirement because gamma>1/2. This does not exclude a different hierarchy that redistributes the coefficient weights.

## Verdict and evidence

The campaign-specific principal cap, all five A2 matrix identifications, the origin and far-field consequences, and the coefficient-weight obstruction are independently established here. The broader TP-4 statement is OPEN without adequate packet-domain hypotheses, especially for homogeneous orders. Independent rational-point evaluations in code/check.py give upper caps only. A finite grid never gives a global lower bound, and a cap alone does not certify a contraction or existence.
