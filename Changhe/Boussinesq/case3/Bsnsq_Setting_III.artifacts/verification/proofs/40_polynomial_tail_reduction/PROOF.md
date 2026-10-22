# Polynomially bounded vorticity reduces to the decaying class

Date:2026-10-20. Status: CONFIRMED by the independent verifier after a substantive actual Opus5.5 audit.
This is a classification of possible exact profiles, not an existence or
nonexistence theorem.

## 1. Exact statement and hypotheses

Let beta>=2. Let U,Omega,Theta be smooth real fields on R2 satisfying

    div U=0, partial_y U1-partial_x U2=Omega,
    W=beta X+V, V=U-U(0),
    W.grad Omega+Omega=partial_x Theta,
    W.grad Theta=(beta-2)Theta.                          (1)

Assume U(X)=o(|X|), uniformly outside large balls, and assume that for
some finite k>=0 and C,

    |Omega(X)|<=C(1+|X|)^k.                              (2)

No derivative growth assumption and no growth assumption on Theta is
made. Then, for every delta with0<delta<1/beta,

    |Omega(X)|<=C_delta (1+|X|)^(-delta).                (3)

Moreover, V is the canonical relative full-plane inverse

    V(X)=int_R2 [K(X-Y)-K(-Y)] Omega(Y) dY,
    K(Z)=(Z2,-Z1)/(2 pi |Z|^2),                          (4)

with an absolutely convergent integral. Theta has polynomial growth.
Thus, after retaining the B2 parity, axis and nontrivial center hypotheses
when they are imposed, the broad polynomial-tail target with U=o(r)
coincides with the power-decaying class A. No restriction on the absolute
vertical observer velocity is introduced.

A separate assertion at beta=2 requires no bound at all on Omega:
every smooth solution of(1) with U=o(r) satisfies(3),(4). Neither assertion
requires parity or center data for the decay conclusion itself. Such data
are required for identification with the nontrivial B2 class and for
further conclusions such as a nonzero leading angular coefficient.

Constants below may depend on the fixed profile, beta, a chosen positive
loss parameter and the indicated exponent, but never on the exterior
point or on the orbit's starting point on a fixed sphere.

## 2. Uniform radial escape and temperature growth

The smooth vector field W has at most linear growth, so its flow phi_t
is complete for every finite positive or negative time. Fix
0<eps<min(1,beta). For all sufficiently large r=|X|,

    (beta-eps)r <= X.W(X)/r <= (beta+eps)r,
    (beta-eps)r <= |W(X)| <= (beta+eps)r.                (5)

The norm bounds follow from |V|<=eps r. The radial derivative bounds
are the same inequality applied to X.V/r. Every exterior point lies on
a unique outgoing orbit from S_R, with R chosen so(5) holds outside it.
Indeed backward radius decreases at a rate at least beta-eps until it
reaches R, and it must reach R in finite time; the strict radial derivative
also gives uniqueness of the crossing. Therefore, for Z in S_R and t>=0,

    R exp((beta-eps)t) <= |phi_t Z|
                       <= R exp((beta+eps)t).          (6)

The same bounds apply between any two times t>=s>=0. Put
w(t)=|W(phi_t Z)|. It follows from(5),(6) that

    C_eps^-1 exp((beta-eps)(t-s)) <= w(t)/w(s)
                  <= C_eps exp((beta+eps)(t-s)).        (7)

Equation(1) gives Theta(phi_t Z)=exp((beta-2)t)Theta(Z). Since beta>=2,

    |Theta(X)| <= C_eps r^p, p=(beta-2)/(beta-eps)<1.     (8)

The strict inequality holds because eps<1<2. All initial values and
all initial derivatives used below are uniformly bounded on S_R by
smoothness. Equation(8) uses no initial bound at infinity.

## 3. A local logarithmic strain estimate

We establish, for all sufficiently large X and r=|X|,

    |DV(X)| <= C [M+A/r] log(2+M),                      (9)
    M=max(1,sup_{B(X,r/2)}|Omega|),
    A=sup_{B(X,r/4)}|Theta|.

Only (1), |V|<=C r on these annular balls, and |W(X)|>=c r are used.
In particular there is no assumption on DOmega or on DV in(9).
All cutoffs in this section are centered at a fixed evaluation point X
and are held fixed when taking derivatives at that point. The escape radius depends on eps; increase the lower bound on |X| so the whole ball B(X,r/2) lies in the region where |V|<=C r and |W|<=C r. The latter constants can be fixed uniformly there.

First choose a smooth chi' equal to1 on B(X,3r/8), supported in
B(X,r/2), with its jth derivatives bounded by C_j r^-j. Decompose

    V=Z'+H', Z'=K*(chi' Omega).

The convolution has |Z'|<=C r M on B(X,3r/8). There H' is divergence
free and curl free, hence componentwise harmonic. The interior harmonic
gradient estimate gives |DH'|<=C M on B(X,r/4), since M>=1 and
|V|<=C r. Splitting the difference kernel at distance2h and bounding
its derivative by C/distance^2 gives the elementary local modulus

    |Z'(P)-Z'(Q)| <= C M h[1+log(r/h)]

for P,Q in B(X,r/4), h=|P-Q|<=r/2. The near part is C M h by
integrability of K, and the distant annular part is
C M h int_h^{C r} d rho/rho. Adding the harmonic part gives the same
bound for V. The separate amplitude estimate |V(P)-V(Q)|<=C r yields

    |W(P)-W(Q)| <= C h
                     +min(C r,C M h[1+log(r/h)]).       (10)

Consequently, for the frozen X,

    (1/r) int_{B(X,r/4)} |DK(X-Y)| |W(X)-W(Y)| dY
                                      <= C log(2+M).   (11)

To verify the logarithm, set z=|X-Y|/r. Apart from a bounded term the
integral is bounded by C int_0^{1/4} min(1,M z[1+log(1/z)]) dz/z.
Split at z0=(2+M)^-2<1/4. The part below z0 is bounded by
C M z0[2+log(1/z0)]<=C, and the other part is at most
C log(1/z0)<=C log(2+M). This is why the bound grows logarithmically,
rather than linearly, with the local vorticity amplitude.

For a smooth f supported in B(X,r/4), the distributional identity

    W(X).grad(K*f)(X)
      = K*div(W f)(X)
        + int DK(X-Y)[W(X)-W(Y)] f(Y) dY               (12)

holds. The second integral is absolutely convergent by(10). For a direct justification, commute the derivative with the smooth compactly supported f and subtract K*div(W f). The result is int K(X-Y)[W(X)-W(Y)].grad f(Y)dY minus int K(X-Y)(div W)f(Y)dY. Integrate the first integral by parts with a radius-rho ball about X removed. Qualitative smoothness gives K(X-Y)[W(X)-W(Y)]=O(1), so its boundary term is O(rho) and vanishes. Differentiating the bracket produces the displayed DK commutator and a div W term which cancels the subtracted integral. No quantitative derivative bound on W is used in this limiting justification. The commutator estimate itself uses (10). All first terms below are ordinary integrals of K against smooth compact sources.

For any divergence-free vector field Z with -curl Z=f, rotate the
oriented basis so its first vector is e=W(X)/|W(X)|. Its derivative
matrix has the form [[a,b],[c,-a]], with c-b=-f. Hence

    |DZ(X)| <= C (|DZ(X)e|+|f(X)|).                    (13)

Suppose |f|<=F and |W.grad f|<=C F. As div W=2 beta, the first term of
(12) is bounded by C r F. The second is at most
C r F log(2+M) by(11). Divide by |W(X)|>=c r and use(13), obtaining

    |D(K*f)(X)| <= C F log(2+M).                       (14)

Now choose chi equal to1 on B(X,r/8), supported in B(X,r/4), with
|D^j chi|<=C_j r^-j. For f=chi Theta, equation(1) gives
|W.grad f|<=C A. Thus, with Z_Theta=K*(chi Theta),

    |D Z_Theta(X)| <= C A log(2+M).                    (15)

For f=chi Omega, equation(1) gives instead

    div(W f)=(2 beta-1)chi Omega
                    +Omega W.grad chi+chi partial_x Theta.

In(12) the first two pieces and the commutator, after division by w,
are bounded by C M log(2+M). The remaining piece is treated without
estimating DTheta directly:

    K*(chi partial_x Theta)
          =partial_x Z_Theta-K*((partial_x chi)Theta).

At X this is bounded by C A log(2+M)+C A, by(15) and the integrability
of K. Therefore(13) yields

    |D(K*(chi Omega))(X)|
                  <=C[M+A/r]log(2+M).                 (16)

Finally H=V-K*(chi Omega) is harmonic on B(X,r/8), and its size on
that ball is at most C r(1+M). Applying the harmonic gradient estimate
on a smaller concentric ball gives |DH(X)|<=C M. Adding this to(16)
proves(9).

By(8), A/r is bounded, indeed tends to0. Under(2), M<=C r^k, so(9)
implies

    |DV(X)| <= C r^k log(2+r).                         (17)

When k=0 the sharper conclusion |DV|<=C follows from(9), since M is
bounded. The weaker logarithmic version(17) suffices for the iteration.
This argument is local; it has not assumed that the full-plane inverse
of a polynomially growing vorticity is already absolutely convergent.

## 4. Exact triangular equations for the temperature gradient

Fix an outgoing orbit from S_R. Let e=W/w and n=(-e2,e1), and express
N=DV in the oriented orthonormal basis(e,n):

    N=[[a,b],[c,-a]].

The trace is zero. Differentiation along the orbit gives

    w'/w=beta+a, e'=c n, n'=-c e.                      (18)

For q=grad Theta, differentiation of(1) gives
q'=-(2 I+N^T)q. Write p=q.e and ell=q.n. Accounting for differentiation
of the basis itself gives the exact triangular equations

    p'=-(2+a)p,
    ell'=(-2+a)ell-(b+c)p.                             (19)

For example q'.e=-(2+a)p-c ell, while q.e'=c ell, so the off-diagonal
term cancels in the first equation. In the second, both b and c appear.
No derivative bound is needed to establish these identities.

By(7),(18), for t>=s>=0,

    |int_s^t a(sigma)d sigma| <= eps(t-s)+log C_eps.    (20)

Solving the first equation and the homogeneous part of the second,
then applying variation of constants, gives

    |q(t)| <= C exp(-(2-eps)t)
                         [1+int_0^t |DV(phi_sigma Z)|d sigma].    (21)

Indeed the first component is bounded by C exp(-(2-eps)t). The
homogeneous multiplier of the second component from s to t is at
most C exp(-(2-eps)(t-s)); multiplication by the first-component
bound at s yields the same global exponential independent of s.
All constants are uniform over Z in S_R.

Substituting(17) and(6) in(21) gives for k>=0

    |q(t)| <= C(1+t^2)
                         exp([k(beta+eps)-2+eps]t).     (22)

This formula also covers k=0: the integral of C(1+sigma) is O(1+t^2).
For k>0 the sharper factor1+t would suffice, but is not needed.

## 5. Improvement of a polynomial exponent and finite iteration

The first transport equation yields

    Omega(phi_t Z)=exp(-t)Omega(Z)
            +int_0^t exp(-(t-sigma)) partial_x Theta(phi_sigma Z)d sigma.

Using(22) and bounding the elementary exponential integral gives

    |Omega(phi_t Z)| <= C(1+t^3) exp(E_eps t),
    E_eps=max(-1,k(beta+eps)-2+eps).                    (23)

The polynomial factor covers equality of the two exponents as well.
If E_eps>=0, use the lower bound in(6) to convert the exponential
in(23) into r^{E_eps/(beta-eps)}. If E_eps<0, use the upper bound
in(6) to convert it into r^{E_eps/(beta+eps)}. Also t<=C log(r/R),
so every fixed polynomial factor in t is bounded by C_zeta r^zeta
for any zeta>0.

Both conversion exponents tend, as eps tends to0, to
max(-1/beta,k-2/beta). Therefore, for every zeta>0,

    |Omega(X)| <= C_zeta
                 r^{max(-1/beta+zeta,k-2/beta+zeta)}.   (24)

For precision, first choose eps sufficiently small that the converted
exponent differs from its limit by less than zeta/2, and then absorb
1+t^3 with a loss less than zeta/2. All estimates are uniform outside
a fixed sphere chosen for this eps, so(24) is a uniform spatial bound.

Set s=1/beta and use zeta=s/2. Starting with any nonnegative exponent k,
(24) implies a new nonnegative polynomial bound with exponent

    k_new=max(0,k-s),                                  (25)

because max(-s/2,k-3s/2)<=max(0,k-s). Enlarge the constant on the
compact core after each step. After at most ceil(k/s) steps, Omega is
bounded. Reapply(24) with k=0 and arbitrary zeta in(0,s); it gives
|Omega|<=C r^{-s+zeta}. This is exactly(3). The iteration has finitely
many steps; no uniformity of constants over infinitely many iterations
is asserted or required.

## 6. Identification of the canonical relative inverse

Choose any delta in(0,1/beta), so0<delta<1. The integral B on the
right of(4) is absolutely convergent. Near Y=X and Y=0 use smoothness
of Omega and local integrability of |K|; at infinity the kernel
difference is O_X(|Y|^-2), and radial integration gives
int_1^infinity rho^-1-delta d rho<infinity.

The same three-region split |Y|<r/2, r/2<=|Y|<=2r, |Y|>2r gives

    |B(X)| <= C(1+r^(1-delta)).                         (26)

For the first region the subtracted kernel contributes
C int_0^{r/2}(1+rho)^-delta d rho and the other kernel contributes
C r^-1 int_0^{r/2}rho(1+rho)^-delta d rho. For the middle region use
|Omega|<=C r^-delta and the integral of |K| over radius O(r). For the
exterior use the difference bound C r |Y|^-2, giving C r^(1-delta).

To verify the div-curl identities, first multiply Omega by a smooth cutoff equal to1 on B_N and supported in B_2N. The corresponding relative velocities B_N satisfy div B_N=0 and -curl B_N=chi_N Omega. The difference-kernel tail estimate gives B_N->B locally uniformly, so distributional differentiation gives div B=0 and -curl B=Omega. Local elliptic regularity
then makes B smooth since Omega is smooth. Therefore V-B has zero
divergence and zero curl on the whole plane, so its components are
entire harmonic. It is sublinear by U=o(r) and(26). The harmonic
interior gradient bound on expanding balls implies its gradient is
zero: at any fixed X0, |D(V-B)(X0)|<=C R^-1 sup_{B(X0,R)}|V-B| tends
to0. Hence V-B is constant. Both vanish at0, so the constant is zero.
This proves(4), without appending any straining or harmonic field.

## 7. The beta-two assertion without vorticity growth assumptions

At beta=2, the second equation of(1) gives q.W=0. On every exterior
orbit w>0, so p=0 exactly. Equations(18),(19) then give

    ell(t)=ell(0) exp(-(beta+2)t) w(t)/w(0).

By(7) with beta=2,

    |q(t)| <= C exp(-(2-eps)t).

Choose eps<1. The exponentially weighted forcing in the vorticity
transport equation is integrable, so |Omega(phi_t Z)|<=C exp(-t).
The upper radius bound in(6) gives

    |Omega(X)| <= C_eps r^{-1/(2+eps)}.

For every delta<1/2 choose sufficiently small eps. This proves(3)
without using(2), the local strain estimate, or a bound on DV. Theta
is bounded because it is constant on the escaping orbits and smooth
on their compact starting sphere and on the compact core. Section6
again identifies the canonical relative inverse.

## 8. Dependencies, scope and audit status

Dependencies: exact profile equations, complete flows for smooth vector
fields of at most linear growth, local elementary Biot-Savart kernel
bounds, the harmonic gradient estimate, distributional div-curl
identities and local elliptic regularity. The moving-frame calculation
and the logarithmic bound are proved explicitly above. No derivative
decay hypothesis or integrability condition is imported.

The actual Opus28 response (claude-opus-5-5,175.697410s, completed16:35:57Z) independently checked sections2-7 and found no error, counterexample, hidden derivative hypothesis or circularity. The verifier checked the entire response and adopted its clarifications concerning the commutator integration by parts, truncation, cutoff radii and dependence on eps. Its audit explicitly did not cover the downstream identification with class A or packet33. The verifier separately checked SPEC v8(A1)-(A6): the standing parity, axis and center hypotheses are retained; (8) supplies A2 growth, (3) supplies A3 and (4) supplies A4. An initially C1 div-curl velocity is automatically smooth locally when Omega is smooth, by the elliptic identities. The observer convention is unchanged. Packet01 excludes beta<2 in the same broad target. Thus packet33 applies to
the broad polynomial target after the B2 nontriviality data are restored.
It yields the generic r^-1/beta nonzero angular vorticity tail and its
improved derivative estimates. This removes the tail-class gap between the
original broad target and class A, but it does not exclude class A or
produce a numerical candidate. The smooth beta>=2 endpoint remains open.
