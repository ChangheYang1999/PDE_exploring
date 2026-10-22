# Mixed-chart reformulation with its resonant correction

Status: CONFIRMED by own direct proof, exact algebra and separate Cartesian finite differences. Additional written model audit OPEN. Written UTC: 2026-10-21T01:09:58.719418+00:00.
This is a reformulation and a scope audit, not an existence or nonexistence result.

## Statement, notation and hypotheses

Let beta>2, lambda=beta/2-1, mu=3beta/2+1, and a0>0. Thus lambda+mu=2beta.
Let S(q,y) be smooth on the whole mixed-coordinate plane, odd in q, with
S_q(0,0)=0 and J(0,0)=1, where J=S_qy. Suppose J>0 everywhere and the
map Phi(q,y)=(S_y(q,y),y) is proper. Then Phi is a global orientation
preserving diffeomorphism: at fixed y its first component is strictly
increasing and, by properness, tends to both infinities at the two ends.
All physical fields below are defined using its inverse.

One may set kappa=0. Alternatively let k>=4 be an even integer with
mu=k lambda, and let kappa be real. In the latter case retain the displayed
kappa terms. Set x=S_y, eta=S_q and

    B = (mu S_q + kappa q^k - lambda q S_qq)/J,
    W_1 = lambda q J + S_yy B,    W_2=B,
    Theta = a0 q^2,
    Psi = 2beta S - lambda q S_q - beta y S_y
          + kappa q^(k+1)/(k+1).

For kappa=0 omit the terms containing k and no integer k is selected.
The physical differentiation operators are

    D_x=J^(-1) partial_q,
    D_y=partial_y-(S_yy/J)partial_q.

Then, exactly,

    div W=2beta, W(0)=0, DW(0)=diag(lambda,mu),
    W=beta(x,y)+(-D_y Psi,D_x Psi),
    W.grad Theta=(beta-2)Theta,
    W.grad eta=mu eta+kappa q^k.

The remaining B2 equation is precisely

    (lambda q partial_q+B partial_y)Omega+Omega=2a0 q/J,
    Omega=-(D_x^2+D_y^2)Psi.

The physical parities are the prompt's x reflection. Near the center
Theta=a0 x^2+O(|X|^3), and Psi_xy(0)=1+beta/2. The vorticity jet is
not automatic: the remaining equation implies Omega_x(0)=4a0/beta.

For this construction to belong to the prompt one must still prove that
W-beta X=o(|X|), that the resulting Omega is polynomially controlled,
and that the remaining equation holds globally. Under those bounds,
the smooth sublinear inverse is canonical up to a constant; the center
normalization fixes its relative representative. The identities alone do
not establish any of those three additional facts.

## Direct proof of the formulas

From dx=J dq+S_yy dy one obtains the displayed physical derivatives.
Also d eta=S_qq dq+J dy, so dx wedge dy=dq wedge d eta. In particular
the transformation to (q,eta) has unit physical Jacobian wherever
it is a coordinate chart. Its proposed vector field is
(lambda q,mu eta+kappa q^k), with divergence lambda+mu. This proves
the physical divergence identity locally at every point, which suffices
globally. Solving eta'=S_qq lambda q+J y' gives y'=B. Differentiating
x=S_y along this flow gives x'=lambda q J+S_yy B.

Let P denote the displayed mixed-coordinate expression for Psi. Then

    P_q=mu S_q-lambda q S_qq-beta y J+kappa q^k=J(B-beta y),
    P_y=beta S_y-lambda q J-beta y S_yy.

Consequently D_x P=B-beta y and
-D_y P=-P_y+(S_yy/J)P_q=lambda q J+S_yy B-beta x.
This proves the velocity identity with exactly the task's curl sign.
The temperature and eta equations follow by differentiating a0 q^2
and S_q. Since -curl W=-curl(W-beta X)=-Delta Psi, the remaining
vorticity equation is exactly the displayed scalar equation. No field
from an artificial boundary is present in this calculation.

Oddness in q gives S_y odd, S_q even, J even and S_yy odd. Hence
Phi(-q,y)=(-x,y); B is even and W_1 odd, as required. At the center
S_yy=S_qq=0, S_q=0 and J=1. It follows that W=0 and that the linear
flow has diagonal derivative (lambda,mu). Moreover x=q+O(|(q,y)|^2),
which proves the temperature jet and strain. At linear order the scalar
vorticity equation is (lambda+1)b0 x=2a0 x, so b0=4a0/beta.

## Coverage and the omitted resonance in the lead's initial formulation

Assume now an actual profile in the global-source subclass G, normalized
a0>0, with Theta_x>0 at every x>0. Packet48 proves the existence of
smooth area coordinates (q,eta) tangent to the identity with
Theta=a0 q^2, whose flow is linear except possibly for the even
resonance above. Packet66 gives Theta/x^2>0 everywhere and the positive
far-field rate. Thus q_x>0 on x>0, by the strict derivative hypothesis,
and q_x>0 on the axis by Theta/x^2>0. Reflection extends this to x<0.
At fixed y, the positive horizontal tail has Theta(x,y) tending to
infinity with |x|, since its growth exponent 1-2/beta is positive.
Thus (x,y)->(q,y) is a global diffeomorphism. Its inverse is proper.

In these mixed coordinates the area identity is eta_y=x_q. The smooth
one-form eta dq+x dy is closed. The plane is simply connected, so it
has a global primitive S; choose S(0,0)=0. Reflection makes this primitive
odd in q. It satisfies S_q=eta, S_y=x and all center normalizations.
This proves coverage of G with the strict horizontal temperature
monotonicity assumption, when the resonant kappa term is retained.

The exceptional values are

    beta=2+8/(k-3),    k=4,6,8,... .

A smooth linearizing chart at these values requires kappa=0; packet48
does not prove it automatically. Without that restriction, one can
linearize by eta_linear=eta-(kappa/lambda)q^k log|q|, but this chart is
in general only C^(k-1), not smooth. The lead note's initial assertion
of a smooth linear chart for all of G_+ is therefore unsupported.
This is a gap in claimed coverage, not a constructed full B2 profile
with nonzero kappa. At beta=3 the ratio mu/lambda=11 is odd, so parity
removes this particular resonance and kappa=0 is justified.

There is a related chart freedom at an even resonance. Replacing
S by S+d q^(k+1) leaves x, J, W and Psi unchanged when kappa is fixed:
its stream contribution is [2beta-lambda(k+1)]d q^(k+1)=0, and the
numerator of B changes by (k+1)[mu-lambda k]d q^k=0. Thus the S
representation has a genuine coordinate kernel at those parameters.
The conditions S_q(0)=0 and J(0)=1 do not remove it. This is separate
from physical spatial scaling, already fixed by a0.

## Limits of the discrete chart test

Checking J>0 only at collocation points does not prove that Phi is a
global diffeomorphism. Even global J>0 without properness is insufficient:
S(q,y)=y tanh(q) has J=sech(q)^2>0 and the stated center constraints,
but x=tanh(q) does not cover the physical plane. This explicit example
is smooth and odd; it is a chart counterexample, not a B2 profile.

Dividing the physical vorticity residual by its pointwise sum of term
magnitudes has the specified meaning where the denominator is nonzero.
A small mean squared ratio cannot bound either the maximum ratio or
absolute residuals when the chart becomes ill-conditioned. The prompt
requires separate maxima and independent chart, inverse and tail tests.
The leading weighted degree of S alone also does not prove the physical
sublinear-velocity condition without quantitative nondegeneracy and
control of differentiated lower-order terms. No index or existence
claim follows from counting the formal unknowns and constraints.

## Dependencies and verification

Packet48 supplies the independently proved source coordinates, including
the even resonance. Packet66 supplies positivity and the horizontal tail
only for the coverage statement. All differential formulas above are
proved directly and apply without any source-coordinate theorem.
No Lean or Lake build is performed. Verification files belong beside
this proof; numerical tests supplement, and do not replace, the proof.

## Verification record 2026-10-21T01:13:30.486246+00:00
The independent script code_independent/mixed_chart_checks.py proved six general differential identities symbolically, checked twelve resonant-kernel identities at six even k, and verified an exact polynomial B2 manufacture whose velocity fails the required tail condition. Its two global proper chart manufactures use beta3 with kappa0 and beta10 with kappa2/7. Seven-point physical Cartesian differentiation at three steps gives approximately sixth-order convergence: the finest inverse/divergence/temperature errors are <=1.7e-12 and the vorticity residual agreement <=1.1e-10. Their residuals are nonzero, as expected. Runtime1.296791s; details in verification/checks.json.

Actual claude-opus-5-5 request121 returned no written audit after151.944681s (max_tokens; response contains no audit text). This supplies no endorsement. The lead has been notified of the resonance and properness issues for its own review.
