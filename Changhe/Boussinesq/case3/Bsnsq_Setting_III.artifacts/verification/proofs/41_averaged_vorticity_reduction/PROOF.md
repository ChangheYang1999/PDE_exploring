# Reduction under bounded macroscopic absolute vorticity averages

Date:2026-10-20. Status: CONFIRMED by the independent verifier;
actual Opus5.5 audit29 independently checked, with the clarifications below adopted. This verifies the precise
averaged extension in lead astra/auditL, not an unspecified signed-average
condition. No existence or nonexistence endpoint is claimed.

## 1. Statement

Let beta>=2 and U,Omega,Theta be smooth on R2, satisfying

    div U=0, -curl U=Omega, U=o(|X|),
    V=U-U(0), W=beta X+V,
    W.grad Theta=(beta-2)Theta,
    W.grad Omega+Omega=Theta_x.                        (1)

Suppose, for some finite p>4 and R0>0,

    M=sup_{|X|>=R0} |X|^(-2/p)
                   ||Omega||_{Lp(B(X,|X|/2))}<infinity.             (2)

Then for every eta>0, |Omega(X)|<=C_eta(1+|X|)^(-1/(beta+eta)).
Theta is polynomially bounded and V is the absolutely convergent
canonical relative Biot-Savart inverse. With the standing B2 parity,
axis and nonzero center data, this identifies a class A profile.
No pointwise bound on Omega or its derivatives is assumed.

The hypothesis is an absolute Lp average, not a signed average.
The threshold p>4 is sufficient for this proof; no sharpness claim
and no p=4 conclusion is made.

## 2. Escape estimates

Let eps in(0,min(1,beta)). Outside a large sphere S_R,
|V|<=eps r. Every point there lies uniquely on an outgoing orbit
phi_t Z, Z in S_R, t>=0. Radius and speed w=|W| satisfy

    R e^((beta-eps)t)<=|phi_t Z|<=R e^((beta+eps)t),
    C_eps^-1 e^((beta-eps)(t-s))<=w(t)/w(s)
                    <=C_eps e^((beta+eps)(t-s)), t>=s. (3)

This follows by integrating (beta-eps)r<=r'<= (beta+eps)r and
using (beta-eps)r<=w<= (beta+eps)r. A backward orbit reaches S_R in
finite time because r' >= (beta-eps)R throughout the exterior.
W has at most linear growth, so its smooth flow is complete at finite
times. The temperature equation gives

    |Theta(X)|<=C_eps r^gamma,
    gamma=(beta-2)/(beta-eps)<1.                       (4)

All initial data and derivatives on S_R are uniformly bounded.

## 3. Bounded strain in the W direction

We prove the directional bound

    |DV(X)e(X)|<=C, e(X)=W(X)/|W(X)|,                  (5)

for large |X|. Enlarge the starting radius R so R>=2R0 and the
sublinear bound holds on every ball B(X,|X|/2), |X|>=R. This does not
affect the escape estimates or compact bounds on S_R.
We do not initially assert a full pointwise bound on DV.
Set r=|X|, alpha=1-2/p, and A_X=sup_{B(X,r/4)}|Theta|.
Choose chi' supported in B(X,r/2), equal to1 on B(X,3r/8),
with derivative bounds at scale r. Write V=K*(chi' Omega)+H',
where K(z)=(z2,-z1)/(2pi|z|^2). The local source has Lp norm at most
M r^(2/p). Holder's inequality, with p>2, gives

    ||K*(chi' Omega)||_{Linfty(B(X,3r/8))}<=C M r.

Indeed ||K||_{Lp'(B(0,Cr))} is finite and scales like r^(1-2/p).
The harmonic remainder H' has derivative bounded by C(1+M) on
B(X,r/4), using |V|<=C r. Splitting a difference kernel at radius2h
and taking its Lp' norm gives

    |K*(chi' Omega)(P)-K*(chi' Omega)(Q)|
                      <=C M r^(2/p) h^(1-2/p).

The near contribution is ||K||_{Lp'(B(0,Ch))} times the source norm;
the far contribution is h||DK||_{Lp'(|z|>c h)}, with the same power
h^(1-2/p). Adding the harmonic and beta X terms gives

    |W(P)-W(Q)|<=C r^(2/p)|P-Q|^alpha                 (6)

on B(X,r/4). Constants can depend on M but not on X.

For smooth compact f in B(X,r/4), use the exact identity

    W(X).grad(K*f)(X)=K*div(W f)(X)
                    +int DK(X-Y)[W(X)-W(Y)]f(Y)dY.    (7)

It follows by commuting the derivative to f, subtracting the first
convolution and integrating by parts. More explicitly, the difference
first equals int K(X-Y)[W(X)-W(Y)].grad f(Y)dY
minus int K(X-Y)(div W)f(Y)dY. Integration by parts in the first
term produces the displayed DK commutator plus int K(div W)f.
The latter cancels the preceding term, including div W=2beta.
Thus(7) holds without assuming W divergence-free. The small-circle boundary term
vanishes because W is qualitatively smooth; the difference factor
cancels the singular derivative's delta contribution. The estimates
below also show absolute convergence of each commutator.

Take chi equal to1 in B(X,r/8), supported in B(X,r/4), with
|Dchi|<=C/r. First apply(7) to f=chi Theta. Its magnitude and
|W.grad f| are bounded by C A_X by(1). The first convolution is
bounded by C r A_X. Using(6), its commutator is bounded by

    C A_X r^(2/p) int_0^{r/4}rho^(-1+alpha)d rho
                                                    <=C r A_X.

After division by |W(X)|>=c r, we control the derivative of K*f
in the direction e by C A_X. The full derivative is then controlled:
for a divergence-free field Z with -curl Z=f, its matrix in the basis
(e,e-perp) has form [[a,b],[c,-a]], b=c+f. Its first column and f
therefore control the whole matrix. In particular

    |D(K*(chi Theta))(X)|<=C A_X.                     (8)

For f=chi Omega, its commutator is instead bounded by Holder:

    C r^(2/p) ||Omega||_{Lp(B(X,r/2))}
                    || |z|^(-1-2/p)||_{Lp'(B(0,r/4))}
                                                    <=C M r.      (9)

The kernel norm is finite exactly when (1+2/p)p'<2, which is
p>4. Its scaling is r^(1-4/p), giving the last expression in(9).
The first convolution in(7) has

    div(W f)=(2beta-1)chi Omega+Omega W.grad chi+chi Theta_x.

The first two pieces convolved with K are bounded by C M r, again
by the Lp bound. The last is

    K*(chi Theta_x)=partial_x(K*(chi Theta))
                                -K*((partial_x chi)Theta),

bounded by C A_X by(8). Thus (7), divided by w, gives

    |D(K*(chi Omega))(X)e|<=C M+C A_X/r.

Here no full-matrix reduction is used, since Omega(X) is not assumed
bounded. The harmonic remainder V-K*(chi Omega) has derivative
bounded by C(1+M) at X, exactly as above. Since A_X/r is bounded
by(4), this proves(5).

## 4. Coupling the transverse gradient to vorticity

Along an exterior orbit, express N=DV in the oriented basis(e,n),
n=(-e2,e1), as [[a,b],[c,-a]]. Divergence gives trace zero and
-curl V=Omega gives b-c=Omega. Directional bound(5) implies
|a|+|c|<=C, while b may contain the unknown pointwise Omega.
The exact frame identities are

    w'/w=beta+a, e'=c n, n'=-c e.

For q=grad Theta the differentiated temperature equation is
q'=-(2I+N^T)q. With P=q.e and L=q.n it becomes

    P'=-(2+a)P,
    L'=(-2+a)L-(b+c)P,
    b+c=2c+Omega.                                     (10)

By(3), |int_s^t a|<=eps(t-s)+log C_eps. Solving(10) therefore gives

    |q(t)|<=C e^(-(2-eps)t)
                    [1+t+int_0^t |Omega(phi_sigma Z)|d sigma].    (11)

This follows from the homogeneous multiplier bound
C e^(-(2-eps)(t-s)) and |P(s)|<=C e^(-(2-eps)s), together with
|b+c|<=C+|Omega|. The bounded constant part supplies the t term.
All constants are uniform over Z in S_R.

Put h(t)=e^t|Omega(phi_t Z)|. Duhamel's formula for the vorticity
transport and(11), with eps<1, imply

    h(t)<=C+C int_0^t e^(-(1-eps)s)
                             int_0^s e^-u h(u)du ds.   (12)

The integral of the independent term e^(-(1-eps)s)(1+s) is finite
and is absorbed in C. Tonelli's theorem applies to the nonnegative
finite-time integrands. After reversing the two integrals,

    h(t)<=C+C_eps int_0^t e^(-(2-eps)u) h(u)du.          (13)

Let the right side be H(t). Then h<=H and
H'<=C_eps e^(-(2-eps)t)H. The coefficient is integrable on[0,infinity),
so Gronwall gives a uniform bound for H and h. Therefore

    |Omega(phi_t Z)|<=C e^-t.

The upper radius bound in(3) proves exponent-1/(beta+eps). Taking
eps smaller than a prescribed eta yields the claimed estimate.
This closes the feedback without assuming Omega bounded in advance.

## 5. Inverse identification and scope

Choose d in(0,1/beta), so0<d<1, and eta>0 with
1/(beta+eta)>d. The proved decay gives an absolutely
convergent B(X)=int[K(X-Y)-K(-Y)]Omega(Y)dY. Local singularities are
integrable because Omega is smooth, and the tail is bounded by
C_X int_1^infinity rho^-1-d d rho. Splitting into |Y|<r/2,
r/2<=|Y|<=2r and |Y|>2r gives B=O(1+r^(1-d)). Truncate the source
smoothly, pass to the local uniform relative-integral limit, and obtain
div B=0 and -curl B=Omega distributionally. Local elliptic regularity
makes B smooth. V-B is entire harmonic and sublinear; its gradient
vanishes by the harmonic estimate on expanding balls. Both vanish
at0, so V=B. Equation(4) supplies temperature's polynomial growth.

For contrast, signed macroscopic averages are already small under
U=o(r): Stokes gives |int_{B(X,c r)}Omega|<=2pi c r sup_boundary|U|
=o(r^2), for fixed0<c<1. That fact does not imply(2), because it
allows cancellation. This proof makes no claim under signed averages
alone, and does not prove the endpoint p=4. The full broad prompt is
already covered by the separate polynomial reduction40, so the present
result is a checked extension to another vorticity-tail hypothesis.

Dependencies: elementary Holder and kernel bounds, local harmonic
estimates, the exact profile equations, complete exterior flow,
Tonelli/Gronwall and local elliptic regularity. The full argument above
was independently rederived before comparison with lead astra/auditL.
No fitting-lane code or numerical inference is used.

Audit29 provenance: the permitted Python Bedrock request returned model
claude-opus-5-5, completed2026-10-20T16:42:51Z in153.265218s.
Its detailed positive audit was checked against every displayed estimate.
The four requested nonblocking clarifications (divergence cancellation,
exterior radius, finite exit bound, and exponent choice) are adopted above.
Class A identification was independently checked against lead SPECv8,
conditions A1-A6; the external reviewer was not supplied that definition.
