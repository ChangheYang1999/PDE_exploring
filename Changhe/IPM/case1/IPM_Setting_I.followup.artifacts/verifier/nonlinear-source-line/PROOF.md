# Nonlinear forcing at the singular line of the frozen source examples

Date: 2026-10-20. Status: independent local calculation and a restricted obstruction, submitted for Opus review. No fully coupled counterexample or global exclusion is claimed.

## Definitions and claims

Use the frozen examples and their specified homogeneous potentials from ../frozen-source/PROOF.md:

    v=V_(5/2), A=5/2, g=21/4;
    v=Q_(7/4), A=7/4, g=27/8;
    v=Q_2, A=2, g=5.

Their potentials satisfy Delta Phi=v. Put U[v]=(Phi_sy,-Phi_ss). Then div U=0, curl U=-v_s, and

    (A s partial_s+y partial_y-1)v+g U_2[v]=0.

For f=g y+epsilon v and W=(A s,y)+epsilon U[v], the exact transport defect is epsilon^2 h, where h=U[v].grad v. This statement concerns the specified local potentials, not the full-plane inverse of these superlinearly growing fields.

For fixed y>0 and s near0, write “analytic” for a function real analytic in s (and in y on compact positive intervals). Let C_V and C_Q be the nonzero constants in the transverse expansions

    V_(5/2)=analytic+C_V |s|^(5/2),
    Q_(7/4)=analytic+C_Q s|s|^(3/2).

Then the nonsmooth parts of h are exactly

    V_(5/2): -C_V/(A+1) (s^2+y^2)^((A-1)/2)|s|^A,       A=5/2;
    Q_(7/4): C_Q/(2A+1)(y^2-s^2)(s^2+y^2)^((2A-3)/2)|s|^(2A-2), A=7/4;
    Q_2: -(1/10)s^2(y^2-s^2)sqrt(s^2+y^2) log|s|.

Thus at every fixed y>0 the first forcing is C^(2,1/2) and not C^3; the second is C^(1,1/2) and not C^2; the third is C^(1,alpha) for every alpha<1 and not C^2. Reflection gives the corresponding conclusions at y<0. None has smooth forcing on a punctured neighborhood of the source.

A further rigorous restricted obstruction holds for either Q example. For epsilon!=0 there is no exact local pair (f,W), defined on a neighborhood of(s,y)=(0,0), with

    f=g y+epsilon Q_A+w,     w in C^(3,alpha)_loc for some0<alpha<1,
    W=(A s,y)+epsilon U[Q_A]+Z,
    W.grad f=f,   div W=A+1,   curl W=-f_s,

where Z is initially at least C^2 locally. No particular boundary condition or harmonic choice for Z is imposed. The claim excludes a smoother additive correction to these fixed singular-line examples. It does not exclude a correction in the original C^(2,alpha) class, a displacement of the singular curve, or any exact profile.

## 1. Exact quadratic remainder

Expand W.grad f-f. The order0 terms cancel because (A s,y).grad(g y)=g y. The order epsilon terms are the displayed frozen equation. Divergence and curl also hold exactly for the uncorrected pair, by linearity. The only remaining transport term is epsilon^2 U[v].grad v. This proves the stated remainder without assuming it is smooth or small in a derivative norm.

## 2. Transverse expansions and velocity components

The complete frozen proof gives, for I_m(s,y)=int_0^y(s^2+t^2)^(m/2)dt and positive fixed y,

    I_m=analytic+c_m |s|^(m+1),
    c_m=sqrt(pi)Gamma(-(m+1)/2)/(2Gamma(-m/2)),

when m is not an odd integer. The series converges with all derivatives for |s|<y away from the power term. C_V=c_(3/2) and C_Q=c_(1/2) are nonzero. For Q_2 its explicit formula gives

    Q_2=analytic-(s^3/2)log|s|.

Differentiating Phi_y, which is an elementary radial expression, gives

    U_1[V_A]=s (s^2+y^2)^((A-1)/2)/(A+1),
    U_1[Q_A]=(2A s^2+y^2)(s^2+y^2)^((2A-3)/2)/((2A-1)(2A+1)).   (1)

Both are analytic across s=0 for y!=0. The second is nonzero there:

    U_1[Q_A](0,y)=|y|^(2A-1)/((2A-1)(2A+1)),                 (2)

whereas U_1[V_A](0,y)=0.

By the frozen equation, U_2=(v-A s v_s-y v_y)/g. For the V singular term, its multiplier is(1-A^2)/g=-1. For the noninteger Q singular term, the multiplier is[1-A(2A-1)]/g=-1. Thus the singular part of U_2 is minus that of v in both cases. In Q_2, differentiating the logarithm adds a polynomial term, which can be absorbed into the analytic part; its logarithmic U_2 part is+(s^3/2)log|s|.

The derivatives v_y are (s^2+y^2)^((A-1)/2) for V and s(s^2+y^2)^((2A-3)/2) for Q, analytic across the line when y!=0. Therefore the singular contributions to h are obtained simply by multiplying (1) by the singular part of v_s and adding the singular part of U_2 times v_y. For V their coefficients combine as A/(A+1)-1=-1/(A+1). For Q the factor is

    (2A s^2+y^2)/(2A+1)-s^2=(y^2-s^2)/(2A+1).

For Q_2 the logarithmic coefficient is -3s^2 U_1/2+s^3 v_y/2, yielding the stated -s^2(y^2-s^2)sqrt(s^2+y^2)/10. All omitted terms are analytic in s. Nonzero coefficients at s=0 prove the stated optimal transverse regularities by differentiating |s|^(5/2), |s|^(3/2) and s^2 log|s|. The first has a bounded1/2-Holder second derivative; the second has an unbounded second derivative; the last has a logarithmically unbounded second derivative. These are fixed-y statements, which already disprove smoothness on any punctured neighborhood containing a line segment.

## 3. Why no C^(3,alpha) additive correction exists for Q

Suppose such a pair exists. Subtracting the divergence and curl equations for the homogeneous background and epsilon U[Q] gives

    div Z=0,   curl Z=-w_s,
    Delta Z_1=w_sy,   Delta Z_2=-w_ss.

As w is C^(3,alpha), the right sides are C^(1,alpha). Interior Poisson regularity, including the smooth harmonic remainder, gives Z in C^(3,alpha) on a smaller neighborhood. No global inverse choice is needed for this conclusion.

Fix y0!=0 in this neighborhood. The nonsmooth transverse part of Q_s is (5/2)C_Q |s|^(3/2) for Q_(7/4), and -(3/2)s^2 log|s| for Q_2, plus an analytic term. The function Q itself and U[Q] are C^2; Q_y is analytic in s at fixed y0. All terms of W.grad f-f, except a possible constant normal-velocity coefficient times this part of Q_s, are C^2 as functions of s. To check the only delicate remainder, W_1(s,y0)-W_1(0,y0)=O(s), with a C^2 quotient because W_1 is C^3 in s there by(1) and the proved Z regularity. Multiplication by |s|^(3/2) or s^2 log|s| then gives a C^2 function. Terms involving grad w are C^2; the other velocity component multiplies the analytic Q_y and remains C^2.

Hence the exact equation forces W_1(0,y0)=0: otherwise it contains a nonzero |s|^(3/2) or s^2 log|s| term that cannot equal a C^2 function. Since every sufficiently small y0!=0 is allowed, (2) implies

    Z_1(0,y)=-epsilon |y|^(2A-1)/((2A-1)(2A+1)).              (3)

For A=7/4 the right side is a nonzero multiple of |y|^(5/2), which is not C^3 at zero. For A=2 it is a nonzero multiple of |y|^3, whose third derivative has opposite one-sided limits. Either contradicts the C^3 regularity of the trace of Z_1. This proves the restricted obstruction.

The contradiction concerns a correction smoother than the original Q field. It is compatible with the possibility that the exact solution has a displaced singular curve, because subtracting the old fixed-line field would then leave its original nonsmooth component in the correction. No claim of nonlinear nonexistence follows in the original class.

## 4. A necessary first-order displacement calculation, not an existence proof

For orientation, suppose a perturbed invariant curve is represented for y>0 by s=epsilon sigma(y)+O(epsilon^2), and the velocity has the uncorrected first variation U[Q]. Tangency to W requires

    y sigma'(y)-A sigma(y)=U_1[Q](0,y).

A particular solution, plus the homogeneous freedom, is

    sigma(y)=y^(2A-1)/((A-1)(2A-1)(2A+1))+C y^A.

At A=7/4 the particular coefficient is16/135; at A=2 it is1/15. This only solves the first-order curve equation. It does not construct a coupled field or control a higher-order remainder. Formally translating epsilon Q(s,y) to epsilon Q(s-epsilon sigma(y),y) produces the second coefficient -sigma Q_s, which has precisely the reduced transverse regularity identified above. The translation itself preserves the regularity of Q for each fixed displacement; its Taylor expansion in the displacement need not be twice differentiable in the original C^(2,alpha) norm.

## Dependencies and verification

The input frozen formulas and their regularities are independently proved in ../frozen-source/PROOF.md. The additional proof uses exact differentiation, the elementary regularity of transverse powers, and local Poisson regularity. Symbolic identities in code/check.py verify the velocity and forcing coefficients and the displacement equation. They are checks of the algebra, not a formal proof of nonlinear existence. There is no use of a solver, global canonical integral for a superlinear field, or the separate r3 team's a posteriori construction.
