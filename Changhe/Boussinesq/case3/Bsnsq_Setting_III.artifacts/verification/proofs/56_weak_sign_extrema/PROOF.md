# Weak vorticity sign and degenerate angular temperature extrema

Date:2026-10-20. Status: CONFIRMED by own derivation and checked actual Opus5.5 review47 at2026-10-20T18:16:18.225546+00:00.
This is a restricted obstruction, not a full NO endpoint.

## 1. Exact hypotheses and conclusions

Consider a smooth whole-plane B2 profile in the full polynomial-tail target,
with beta>=2, V=U-U(0), W=beta X+V, div V=0, and

    Omega=-curl V,
    W.grad Omega+Omega=Theta_x,
    W.grad Theta=(beta-2)Theta.

Use the prompt's x-reflection, axis temperature condition, nonzero quadratic
center temperature jet, canonical full-plane inverse and sublinear velocity.
Assume in addition either Omega>=0 everywhere in x>0 or Omega<=0 everywhere
there. The sign may be weak and zeros are allowed.

A. No complete forward-escaping orbit in x>0 is contained in a horizontal
line.

B. At beta=2, let h be the smooth angular temperature limit furnished by
packets33,36,39. At every critical angle alpha in (-pi/2,pi/2),

    hprime(alpha)=0 implies hsecond(alpha)=0.

In particular a profile with the extra weak vorticity sign cannot have a
nondegenerate interior angular temperature extremum. A nonzero interior
extremum exists by packet55, so a Morse angular temperature function is
excluded in this subclass. Degenerate extrema and plateaus are not excluded.
No single-axis-zero or global equilibrium-set hypothesis is imposed.

## 2. Far-field dependencies and conventions

Packets33,36,38,40 prove for this full target, with nu=1/beta and k=2-nu,

    Omega(r e(alpha))=r^{-nu}(a(alpha)+o(1)),
    V(r e(alpha))=r^{1-nu}(u0(alpha)+o(1)),
    u0_r=Pprime, u0_theta=-k P,
    Psecond+k^2 P=a.

The remainders are uniform in angle. The angular functions are smooth and
a is not identically zero. Here P is the leading coefficient of the NEGATIVE
physical stream -Psi. These signs give -curl V=Omega. A possible bounded
observer constant is lower order and does not affect these formulas.

The stipulated odd x-reflection of Omega and Psi gives the same odd reflection of a and P, hence a(pi/2)=a(-pi/2)=0 and P(pi/2)=P(-pi/2)=0.
For beta>=2, 3/2<=k<2, so k is not an integer and this Dirichlet problem on
the angular interval J=(-pi/2,pi/2) is invertible. This angular boundary
condition expresses x-reflection of the full-plane solution. It is not a
physical wall or a finite-box elliptic inverse.

If Omega has one weak sign in x>0, then a has that same weak sign on J by
taking its pointwise scaled limit. The function a cannot vanish identically
on J: reflection would then make it vanish on the full circle, contrary to
the nonzero-tail theorem. Hence its integral against a strictly positive
continuous weight on J has the strict prescribed sign.

## 3. The middle-row angular Green kernel

For L=d^2/dalpha^2+k^2 with Dirichlet data at +-pi/2, take

    u(s)=sin(k(s+pi/2)), v(s)=sin(k(pi/2-s)).

Their Wronskian u vprime-uprime v=-k sin(k pi) is positive. The Green
kernel G(alpha,s)=u(min(alpha,s))v(max(alpha,s))/[-k sin(k pi)] has unit
first-derivative jump at alpha=s, vanishes at both endpoints, and solves
L G=delta. At the middle angle,

    G(0,s)=sin(k pi/2) sin(k(pi/2-|s|))/[-k sin(k pi)] >0
                                                        for every s in J.

Every factor is positive because 3/2<=k<2 and 0<k(pi/2-|s|)<pi. Although
the full Green kernel need not be positive, this one row is positive.
Consequently

    P(0)=int_J G(0,s)a(s) ds

is strictly positive for nonnegative a and strictly negative for
nonpositive a. This is an exact angular integral identity, not a numerical
sign inference.

Fix a horizontal line y=y0. As x tends to positive infinity, its radius
r satisfies r/x->1 and its angle tends to0. The uniform velocity limit
therefore gives

    V2(x,y0)/x^{1-nu} -> -k P(0) !=0.

Since beta y0/x^{1-nu}->0, the same limit holds for W2. Thus W2 cannot
vanish at all sufficiently large x on this line. A forward-escaping orbit
which remains on y=y0 in x>0 has x(t)->infinity and W2(x(t),y0)=0 at every
time, a contradiction. This proves A. No claim that W2 has one sign
throughout the right half-plane is made.

## 4. The beta-two critical-orbit argument

At beta=2 the established scattering map Phi:E->R2 minus{0} is a C1
diffeomorphism, where E is the open forward escape set. The limit definition makes Phi reflection-equivariant. It conjugates the flow
to dilation. Write X(t,alpha)=Phi^{-1}(e^{2t}e(alpha)). Packet54 proves

    Theta(X(t,alpha))=h(alpha),
    det(X_t,X_alpha)=2e^{4t},
    grad alpha(X(t,alpha))=(-W2,W1)/(2e^{4t}).

In particular grad alpha never vanishes. Reflection and injectivity of Phi
identify x>0 in E with alpha in J. Every alpha in J labels a complete
escaping orbit in the open right half-plane.

Fix alpha_star in J with hprime(alpha_star)=0. The first formula and the
C1 chain rule give grad Theta=0 everywhere on this orbit. Its negative semiorbit is contained in a compact ball, which bounds Omega. Sublinearity gives strictly outward radial flow outside a fixed disk, so the reversed trajectory stays in a bounded disk. The vorticity ODE there is Omega_dot=-Omega,
so boundedness backward forces Omega=0 on the entire orbit.

The additional weak sign now matters. Each point of this orbit is an
interior minimum of Omega when Omega>=0, or an interior maximum when
Omega<=0. Thus grad Omega=0 along the entire orbit. Differentiate the
vorticity PDE in the coordinate direction j. On this orbit,

    d/dt(partial_j Omega)
      +partial_j W . grad Omega +partial_j Omega=partial_j partial_x Theta.

Every term on the left is zero. Hence both entries in the first row of
the Hessian of Theta vanish there.

Only C1 regularity of Phi is needed to identify this Hessian. At a point Y
on the orbit, take a local real-valued angle coordinate alpha(Y+z). Since
hprime(alpha_star)=0, Taylor expansion gives

    Theta(Y+z)=h(alpha_star)
       +(hsecond(alpha_star)/2)(grad alpha(Y).z)^2+o(|z|^2).

Theta is smooth, so its Hessian equals
hsecond(alpha_star) grad alpha tensor grad alpha at Y. The vanishing first
row implies

    hsecond(alpha_star) alpha_x(Y) grad alpha(Y)=0.

If hsecond(alpha_star) were nonzero, the nonvanishing gradient of alpha
would force alpha_x(Y)=0 and hence W2(Y)=0. This conclusion would hold at
every point of the complete escaping orbit. It would be a horizontal
orbit, contradicting A. Thus hsecond(alpha_star)=0, proving B.

## 5. Scope, gaps and verification plan

This argument does not divide by hprime at its zeros. It assumes no
continuity of an infinite orbit integral at a slowly approached endpoint,
and does not replace a vanishing hprime times a divergent integral by zero.
Those issues prevent an unsupported extension to all degenerate extrema.
The required nonzero angular vorticity tail is a full-PDE theorem; an
arbitrary kinematic manufacture need not satisfy it.

The proof preceded a small manufactured kernel check, now complete. For a(alpha)=cos(alpha)(1+.7 sin(alpha))^2 on J, the exact middle value is (1+.7^2/4)/(k^2-1)-(.7^2/4)/(k^2-9). Independent Gauss-Legendre integration on the two half intervals used orders12,24,48 and beta2,2.5,3,4,10,100. The maximum absolute discrepancy was1.67e-15, runtime0.012852078seconds. Raw values and source hash are in verification/kernel_check.json. This tests conventions and code, and constructs no B2 solution. No formalization is claimed;
Lean and Lake builds are prohibited. General sign-changing profiles, and
weak-sign profiles with only degenerate interior critical values, remain
open. This partial result cannot authorize an early finish.

Actual claude-opus-5-5 review47 returned in88.410596138seconds at18:14:49Z and confirmed the proof under its stated dependencies. The verifier read and checked the entire response, adopted the precompact-orbit wording and explicit scattering/parity hypotheses, and retained the full Hessian argument. The reviewer’s broader parity wording was not used: Omega and Psi oddness are separately stipulated hypotheses, not consequences of Theta evenness alone. No full endpoint follows.
