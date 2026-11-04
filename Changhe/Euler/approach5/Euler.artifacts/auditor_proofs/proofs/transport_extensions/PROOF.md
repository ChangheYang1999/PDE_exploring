# Transport identities and the averaged-strain criterion

## Exact statements and scope

Let c>0, omega be real, U in C^2(R^3), P in C^1(R^3), div U=0, and

    (1-c)U + (B.grad)U + omega JU + grad P = 0,
    B=cy-omega Jy+U, X=cy+U, Omega=curl U, S=sym DU.

Put a=1-2c, M=(Jy).U, q=|U|^2/2,

    H=P+q+c y.U-c a |y|^2/2-omega M,
    H0=H+omega M, Htil=H+c a |y|^2/2.

Then

    B.grad(y.U)=(2c-1)y.U+|U|^2-y.grad P,
    B.grad H0=-a|X|^2-omega d_theta P,
    Omega x B=-a U-grad Htil,
    B.grad Htil=-a U.B.

If additionally U=o(|y|) uniformly, every C^1 field W satisfying
[B,W]=-(1+c)W is divergence-free. This assertion needs no decay of W.

Under the same sublinearity, if

    liminf_(t->infinity) (1/t) int_0^t lambda_max(S(Phi_-s(x))) ds < 1,

then Omega(x)=0. For any vortical x, every weak limit of its backward empirical
measures has integral of lambda_max(S) at least 1. If every invariant probability
on the compact set Lambda of bounded full B-orbits has that integral strictly
less than 1, then U is constant. Decay makes that constant zero. These conclusions
hold for every c>0, although the campaign uses 0<c<1/2.

## Proof of identities

Apply the product rule to y.U and substitute the momentum equation. The terms
-omega (Jy).U and -omega y.JU cancel because J is skew. This gives the first
identity. The already verified identities B.grad H=-a(|X|^2-omega M) and
B.grad M=-aM-d_theta P give the second by addition. Subtract a cy from the
rotating Bernoulli identity aX+Omega x B+grad H=0 to obtain the third; dot it
with B for the fourth. No integration or pressure normalization is used.

## Automatic divergence-free property with only C^1 W

The bracket equation is equivalent to

    W(Phi_s x)=exp(-(1+c)s) D Phi_s(x) W(x).

The flow is complete under uniform sublinearity and div B=3c, so
J_s=det D Phi_s=exp(3cs) is spatially constant. For a C^1 vector field, the
change-of-variables formula for divergence gives

    div(Phi_s*W)(Phi_s x)=div W(x).

For completeness, test against a compactly supported C^1 function f and write
int(Phi_s*W).grad f in the x variable. The constant factor J_s can be pulled
through the integration by parts; changing variables back proves the formula
in distributions, and both sides are continuous. Since Phi_s*W=exp((1+c)s)W,

    div W(Phi_s x)=exp(-(1+c)s) div W(x).

Each backward orbit is bounded, while div W is continuous there. Let s tend to
minus infinity. Since 1+c>0, div W(x)=0. Differentiating W twice is unnecessary.

## Averaged-strain proof

For x(t)=Phi_-t(x), the exact magnitude identity yields, wherever Omega is
nonzero,

    d/dt log|Omega(x(t))| = 1 - n(t).S(x(t))n(t)
                         >= 1-lambda_max(S(x(t))),

where n=Omega/|Omega|. Nonvanishing persists by the Cauchy formula. Integrating,

    |Omega(x)| <= |Omega(x(t))|
        exp(int_0^t [lambda_max(S(x(s)))-1] ds).

The backward orbit lies in one compact ball, so the prefactor is bounded. A
subsequence of averages bounded by 1-eta, eta>0, forces Omega(x)=0.

Backward empirical measures are probabilities on that compact orbit closure.
Any weak limit is invariant: the difference between the averages of f composed
with a fixed time shift and f is bounded by 2|s| sup|f|/t. The limit is supported
on the alpha-limit set because every tail is eventually in every neighborhood
of that set. Continuity of lambda_max(S) identifies its integral with the
corresponding subsequence average, which is at least 1 at a vortical point.
If all invariant measures on Lambda have integral less than 1, a vortical point
would give a contradiction. Thus Omega=0. The components of U are harmonic
because div U=curl U=0. An entire harmonic function of uniformly sublinear
growth is constant, by the interior gradient estimate on larger and larger
balls. This proves the final claim.

## Correction and dependencies

At a vortical B-zero, only Omega.S Omega=|Omega|^2 is automatic. The vector
identity S Omega=Omega is generally false when omega is nonzero. The theorem
does not require that identity. Dependencies: the directly verified momentum,
vorticity and flow identities in the team records. These are conditional
criteria, not a proof that the required average is less than 1.

Audit recorded: 2026-11-02T18:42:51Z
