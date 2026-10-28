# The actual global high-frequency and compact-error estimates

## Exact statement

Let rho be the exact normalized C6-joined case1 modal trial verified in topics15 and68, with k=1615536043799051/9007199254740992 and c_l=1/k. Let U, c, C_R and T have the signs and realizations of proof 123. Set delta=9/5, gamma=-1/2, sigma=25/4 and s_0=41/20. Choose the smooth reflection-invariant order s and bounded smooth escape Lambda constructed in topics128 and130, including the constant-order vertical neighborhood and far end, with W.grad s>=0 and W.grad Lambda>0 off the compactified critical set.

Fix b and the nested vertical cutoffs as in topics123 and144. The Hilbert space X_s consists of the prescribed even-x, odd-y perturbations for which v=h/b belongs to H^(s(.))(R times S1) and u=chi h/(b cos^2(theta)sin(theta)) belongs to H^sigma, with zero traces at both vertical axes. Its norm is the square sum of these two norms. Set

 D_s={h in X_s:T h in X_s},    S=T+C_R,

with distributional derivatives and graph norm ||h||X_s+||Th||X_s. For every finite L>=0 and epsilon=1/32 there are a constant C<infinity and a compact map J:X_s->X_s such that

 ||h||X_s<=C[||(S-lambda)h||X_s+||h||X_(s-epsilon)+||Jh||X_s],
                    h in D_s, 0<=lambda<=L.             (1)

There are also a Hilbert target W_0, a compact map K:X_s->W_0 and C_1<infinity with

 ||h||X_s<=C_1||(S-lambda)h||X_s+||Kh||W_0,
                    h in D_s, 0<=lambda<=L.             (2)

Thus the actual compact-error assertion H3 holds on this X_s. All constants and compact maps are qualitative. Neither injectivity nor a numerical bound for the inverse is asserted.

## Inputs and their scopes

Proof 142 gives a common positive matrix margin for the two energy symbols after adding N W.grad Lambda and L_0(W.nu)^2. Fix, for example, mu=1/2<m_x and the finite N,L_0 supplied there. Their numerical values are not needed or claimed. They are fixed before any approximation or small-error parameter below.

Proof 144 gives bounded order reductions A_v,A_u, the elliptic lower estimates with an added lower norm, and the negative-norm comparison. It also controls the nonlocal cofactor tails outside a larger angular sector. Proof 145 gives the coupling principal forms modulo a compact map and arbitrarily small X_s operator errors. Proof 146 gives the penalty estimate with an arbitrarily small high-norm error. Topics147-148 give the transport energy inequality on the exact maximal domain, with an arbitrarily small high error and a lower-norm product. Proof 143 supplies the sign of the logarithmic form with its lower remainder. Every one of these statements applies to the actual finite regularity; no smoothness of the modal trial beyond the verified coefficients is imposed.

## The two energy inequalities

Write

 H=||h||X_s, Y=||h||X_(s-epsilon), F=||(S-lambda)h||X_s,
 V=||v||H^s, U_0=||u||H^sigma, w=A_v v, z=A_u u.

The bulk equation is f/b=P_v v-lambda v+C_R h/b. Combine the maximal-domain transport inequality and the coupling form. Since lambda>=0, its energy contribution has the favorable sign and can be discarded. Matrix positivity and the exact identity ||Rw||_2^2=||w||_2^2-||w||H^-1^2 give

 mu||w||_2^2
 <= C F||w||_2+L_0||W.Rw||_2^2
       +e H^2+C_e YH+||J_e h||H.                       (3)

Here e>0 can be chosen arbitrarily small, J_e is compact, and constants are uniform in lambda in the displayed interval. All negative ordinary Sobolev terms have been absorbed into C_e YH by proof 144. The scalar logarithmic term was handled on the actual maximal domain in proof 148, rather than left as a possibly undefined limiting quadratic form.

The cofactor equation has the additional forcing -(W.grad chi)v/p. It is supported in the fixed overlap where p does not vanish and s=sigma. Its H^sigma norm is at most C_chi V. Proof 144 handles the part of Rz outside the positivity sector. The resulting inequality is

 mu||z||_2^2
 <= C F||z||_2+C_chi V||z||_2+L_0||W.Rz||_2^2
       +e H^2+C_e YH+||J_e h||H.                       (4)

Enlarge the compact map by a finite direct sum if the maps arising from (3) and (4) differ. Its norm can be represented by a compact operator on X_s, as in proof 145. The cutoff constant C_chi is fixed independently of e and of the approximation parameters.

For every a>0, proof 146 gives

 ||W.Rw||_2+||W.Rz||_2<=C F+a H+C_a Y.                 (5)

After squaring, the coefficient of a^2H^2 can be made arbitrarily small because L_0 has already been fixed. The coefficient of F^2 in this step can be chosen independent of a.

## Triangular absorption, with the order of choices

The elliptic estimates of proof 144 give V^2<=C_A(||w||_2^2+Y^2) and U_0^2<=C_A(||z||_2^2+Y^2). Use Young's inequality on F||w|| and F||z|| with a fixed fraction of mu, and on C_chi V||z|| with another fixed fraction. The latter produces a coefficient C_1 V^2, with C_1 independent of e,a and all later Young parameters.

Choose any d>0. First make e and a^2 sufficiently small relative to d and these fixed constants. Then use Young's inequality on C_e YH and ||J_e h||H, assigning their H^2 coefficients a total at most d. Their remaining constants may grow; they multiply only Y^2 and the compact seminorm. Equations(3)-(5) now imply

 V^2<=C_0 F^2+d H^2+C_d(Y^2+||J_e h||^2),              (6)
 U_0^2<=C_1 V^2+C_0 F^2+d H^2+C_d(Y^2+||J_e h||^2).    (7)

The coefficient C_0 may be enlarged but is finite; C_1 remains independent of d. Insert (6) into (7), then add V^2. Since H^2=V^2+U_0^2, the high error is at most (C_1+2)d H^2. Choose d<1/[2(C_1+2)] and absorb it. The resulting squared estimate implies (1). All small choices are now fixed, so the compact map J is fixed and independent of lambda.

This argument checks a point that an unspecified appeal to Young's inequality could hide: the triangular overlap coefficient must be fixed before choosing the small errors. No constant that grows as d decreases is allowed to multiply the high norm in the final absorption.

## Removing the global lower norm

Apply the double-factor reduction of proof 139. That proof remains valid with the additional compact term in (1). For completeness, put N_0(h)=||h/(b cos^4(theta))||_2. Its proved interpolation bound is

 ||h||X_(s-epsilon)<=eta H+C_eta N_0(h).

On sufficiently distant radial ends the exact N_0 transport energy has a positive coefficient c_0, uniform in angle. The full C_R output tail in N_0 tends to zero. With end cutoff psi_E and psi_m=1-psi_E, the same argument as proof 139 gives, after its two small absorptions,

 H<=2C_s(1+C_eta C_H/c_0)F
       +2C_s||psi_m h||X_(s-epsilon)
       +2C_s C_eta c_0^(-1)N_0(q psi_E' h)+2C_s||Jh||X_s. (8)

The first two localized maps on the right are compact by the local Rellich and double-Hardy proofs in proof 139. The third map J is compact by construction. Take their direct sum as K, with the displayed scalar factors, and use the sum norm on the target

 W_0=X_(s-epsilon) plus N_0-completion plus X_s.

This proves (2), uniformly for lambda in [0,L]. An equivalent Hilbert norm on the finite direct sum changes only its constant.

## What has and has not been proved

Equations(1)-(2) apply to the exact modal background and exact closed normalized remainder space, with finite coefficient regularity and the actual maximal transport domain. They do not identify a numerical value of C,C_1,N,L_0 or the compact operators. The earlier first-order graph perturbation counterexample remains valid; this proof does not use that invalid perturbation step. Low injectivity, a certified finite-dimensional complement, an explicit high inverse norm and nonlinear closure remain separate questions. Fredholm continuation is a further functional-analytic consequence checked separately.
