# A smooth transport layer with a nonzero fifth source coefficient

Date: 2026-10-20. Status: proved local counterexample for transport and constant divergence. It is not an IPM profile. This independently audits fred33 and the proposed D5 text in the lead's s53 draft.

## Statement and notation

For every $1<A<4$, there are a neighbourhood of $P=(0,0)$ and fields $f,W=(a,b)$ of class $C^3$ there such that
\[
 W\cdot\nabla f=f,\quad \operatorname{div}W=A+1,\quad
 DW(P)=\operatorname{diag}(A,1),\quad f_y(P)=1.
\]
The functions $f,b$ are odd in $y$, and $a$ is even. They are smooth off $P$. On the incoming axis $s=-r<0$, put $G_j=\partial_y^jf/j!$ and normalize the homogeneous solution as $H_j=r^{-(j-1)/A}$. Then $G_3=0$ and $G_5/H_5=-1$. In particular, $C^{2,\alpha}$ regularity for every $0<\alpha<1$, together with these transport hypotheses, does not imply vanishing of the fifth normalized source limit.

The pair violates the necessary IPM identity $b_s-a_y=-f_s$. It gives no counterexample to a theorem using the full velocity law.

## Construction and exact identities

Set $q=4/A\in(1,4)$ and $c=(q-1)^{-1}$. Let $\chi$ be a smooth even cutoff, one on $[-1,1]$ and zero outside $(-2,2)$. For $s<0$, define
\[
 F(s,v)=c r^{1-q}v^5\chi(v/r^3),\quad r=-s,
 \qquad F(s,v)=0\quad(s\geq0).
\]
Introduce $u=s+F_v$ and $y=v+F_s$, and write $J=1+F_{sv}$. Shrinking the neighbourhood makes $J$ positive. The map $(s,v)\mapsto(s,y)$ is therefore invertible; denote its inverse second coordinate by $v(s,y)$. Set
\[
 f=v,\quad a=\frac{A(s+F_v)-vF_{vv}}{J},\qquad
 b=Jv+F_{ss}a,
\]
where the last expressions are evaluated at $v(s,y)$.

Since $f_s=-F_{ss}/J$ and $f_y=1/J$, one has $af_s+bf_y=v=f$. Moreover $du\wedge dv=J\,ds\wedge dv=ds\wedge dy$. The field in $(u,v)$ coordinates is exactly $(Au,v)$: its first component is
$u_sa+u_v\dot v=Ja+F_{vv}v=Au$ and its second is $\dot v=v$. Change of coordinates preserving area preserves divergence. Thus $\operatorname{div}W=A+1$. Equivalently, differentiating the displayed formulas directly proves the same identity. Evenness of $\chi$ makes $F$ odd in $v$, $F_v$ even, and $F_s$ odd; inverse uniqueness gives all asserted parities.

## Regularity of the coordinate change and fields

Write $z=v/r^3$, $\phi(z)=z^5\chi(z)$ and $M=16-q$. Then
\[
 F=c r^M\phi(z),\quad F_s=r^{15-q}B(z),\quad
 B=c(3z\phi'-M\phi),\quad F_{sv}=r^{12-q}B'(z).
\]
All $B$ and $\phi$ derivatives are bounded and supported in $|z|\leq2$. For $i+j\leq4$,
$|\partial_s^i\partial_v^jF|\leq C r^{16-q-i-3j}$.
The smallest exponent is $4-q>0$. All these derivatives extend continuously by zero at the origin. The usual derivative induction is valid since on their supports the distance to the origin is comparable to $r$, and lower derivatives vanish faster than that distance. Consequently $F$ is $C^4$ across the origin.

Put $Y=y/r^3$ and $\epsilon=r^{12-q}$. The inverse equation is $Y=z+\epsilon B(z)$. For sufficiently small $r$, its derivative in $z$ stays bounded away from zero. Its inverse and all needed derivatives in $(Y,\epsilon)$ are uniformly bounded. Outside $|Y|\leq3$, the inverse is exactly $z=Y$. The formulas above therefore have the form
\[
 f-y=r^{15-q}\Phi_0(Y,\epsilon),\quad
 a-As=r^{13-q}\Phi_1(Y,\epsilon),\quad
 b-y=r^{15-q}\Phi_2(Y,\epsilon),
\]
with smooth uniformly bounded functions supported in $|Y|\leq3$. Every $s$ derivative lowers these powers by at most one and every $y$ derivative by at most three. The smallest exponent for a derivative of total order at most three is $4-q>0$, from three $y$ derivatives of $a-As$. Derivatives of order at most two have size $o(r)$ on the support. Induction proves that the perturbations extend as $C^3$ functions with zero derivatives up to order three at $P$. Thus the fields have the claimed regularity and jets. Bounded third derivatives on a smaller neighbourhood imply $C^{2,\alpha}$ for every $\alpha<1$.

Away from $P$, the formulas are smooth. At points $s=0,y\ne0$, the perturbation vanishes on a neighbourhood. This also proves the claimed off-source smoothness.

## Fifth coefficient and limits of the example

For each fixed $r>0$, the cutoff is one near $v=0$. There,
\[
 y=v+r^{-q}v^5,\quad J=1+5r^{-q}v^4,\quad F_{ss}=q r^{-q-1}v^5.
\]
Using $Aq=4$ in the formula for $a$ gives $a=As$. Substitution gives $b=y$. Inverting the first relation at fixed $r$ yields $f=y-r^{-q}y^5+O_r(y^9)$. Hence $G_3=0$ and $G_5=-r^{-q}$. The axis equation for a homogeneous $j$th coefficient is $ArG_r+(j-1)G=0$, giving $H_j=r^{-(j-1)/A}$ and the stated limit.

In this same region $b_s-a_y=0$, while
\[
 f_s=-\frac{q r^{-q-1}v^5}{1+5r^{-q}v^4}\ne0\quad(v\ne0).
\]
The curl law therefore fails on an open set. A harmonic stream-function correction has zero curl and cannot repair this fixed pair. Neither the global origin normalization nor the growth hypotheses of $P_\infty$ are addressed.

For the cutoff-layer fourth derivative, define
$T=z\phi''-4\phi'=6z^5\chi'+z^6\chi''$.
Direct algebra gives
\[
 a-As=\frac{c(3A-1)r^{13-q}T(z)}{1+\epsilon B'(z)}.
\]
The compactly supported function $T$ is nonzero: $T=(z^6\chi')'$ could vanish identically only if $\chi$ were constant. Thus $T^{(4)}$ is nonzero somewhere. At such a $z_0$, with $y_r=r^3(z_0+\epsilon B(z_0))$,
\[
 \partial_y^4a(-r,y_r)=c(3A-1)r^{1-q}
 \bigl(T^{(4)}(z_0)+O(\epsilon)\bigr).
\]
It diverges for every $1<A<4$. Relative to a proposed bound $r^{\alpha-2}$, it diverges only when $\alpha>3-q$. This latter failure holds for every positive $\alpha$ when $A<4/3$, and for the threshold range $\alpha>3-4/A$ when $4/3\leq A<2$. No such $\alpha<1$ exists when $A\geq2$. The extension of the construction to $2\leq A<4$ preserves its nonzero endpoint coefficient and $C^3$ regularity; it does not extend every weighted-bound failure from the smaller range.

Likewise, $\partial_y^5f=-120r^{-q}$ violates $O(r^{-3})$ exactly when $q>3$, and violates $O(r^{\alpha-3})$ when $\alpha>3-q$. It always violates $o(r^{-q})$.

## Higher odd orders

For odd $j\geq5$ and $1<A<(j-1)/(j-2)$, replace $5$ by $j$ and $q$ by $q_j=(j-1)/A$ in $F$. The same area argument proves the equations, and the inner identity uses $Aq_j=j-1$. Thus all lower odd coefficients above one vanish, while $G_j=-r^{-q_j}$ and $G_j/H_j=-1$. The perturbations of $f,b$ have power $3j-q_j$, and that of $a$ has power $3j-2-q_j$. The smallest third-derivative exponent is $3j-11-q_j>0$, since $q_j<j-1$ and $j\geq5$. This proves the stated $C^3$ extension without any frozen or IPM theorem.

Dependencies: elementary inverse function theorem, area-preserving change of variables and differentiation. The symbolic code independently checks the two exact equations and the inner field. No formal build is run. The coupled IPM question remains open.

## Sharp common Holder regularity and the wider higher-order range

This supplements the C^3 statement and audits the new claims in the lead's D5 version 2. For 1<A<4 let m=4-q, so 0<m<3. Every third derivative h of a perturbation has |h|<=C r^m and |grad h|<=C r^(m-3), with zero extension for s>=0. The latter estimate uses the explicit smooth formulas off P and holds uniformly across the cutoff boundary.

For two points at distance d, let R be the larger left depth. If d>=R^3/2, the amplitude bound gives |h(X)-h(X')|<=C d^(m/3). If d<R^3/2, the depths along the segment are comparable to R in a sufficiently small neighborhood. The gradient bound gives C d R^(m-3), at most C d^(m/3). If both left depths vanish then h is zero at both points. Thus all third derivatives are Holder continuous of exponent beta*=m/3, including at pairs that straddle the support boundary or s=0.

The exponent is sharp for the pair (f,W), specifically for the horizontal component a. The nonzero compactly supported function T=(z^6 chi')' has T''' nonzero at a point z1 in the transition layer. At the corresponding physical point y_r=r^3(z1+epsilon B(z1)), one has

    partial_y^3 a(-r,y_r)=c(3A-1)r^(4-q)[T'''(z1)+O(epsilon)].

At (-r,0) this derivative is zero because a=As throughout the inner region. Their distance is comparable to r^3. An exponent beta>beta* would bound a nonzero multiple of r^(4-q-3beta), which diverges. This proves sharpness for a and hence for the pair.

It does not prove the same sharpness for f separately. In fact, the sharper amplitude bound for third derivatives of f-y is C r^(6-q), and their gradients are bounded by C r^(3-q). The same two-point argument, or a uniform gradient bound when q<=3, gives

    f, b in C^(3, min(1,(6-q)/3)).

Here exponent 1 means Lipschitz third derivatives. This exponent is strictly greater than beta*. Therefore the report should say that the pair belongs to no higher common class, rather than say unambiguously that f itself belongs to no higher class.

The physical support can be sharpened to |y|<=2r^3: for fixed s the increasing map v -> v+F_s fixes both endpoints +/-2r^3 and is the identity outside them. Its inverse maps the interval onto itself.

For the higher odd order j, the proof in the preceding section works throughout 1<A<j-1, not just its previously stated smaller subinterval. Indeed q_j=(j-1)/A lies in (1,j-1). The least third-derivative exponent is m_j=3j-11-q_j. For j=5 this is 4-q_j>0; for j>5 it is greater than 2j-10>0. The least lower-derivative exponent exceeds 1, so the differentiability induction still applies. The inner identities W=(As,y) and y=v+r^(-q_j)v^j are checked symbolically for arbitrary j by code/higher_checks.py. The same proof also permits q_j<1, with a negative but finite prefactor (q_j-1)^(-1), giving the construction for every A>1 except A=j-1. This latter optional extension is not needed for the draft's stated range.

## Failure of a smooth frozen forcing for the scalar fluctuation

For the nonresonant construction above, eta=f-y obeys (As partial_s+y partial_y-1)eta=0 in the open inner region. Suppose its frozen equation had a smooth forcing H near P, with the usual localized velocity satisfying -Delta U_2[eta]=eta_ss. Since g*=1, that equation would give U_2[eta]=H in the inner region. Consequently -Delta H=f_ss there. But the exact axis coefficient gives

    partial_y^5 f_ss(-r,0)=-120 q(q+1) r^(-q-2),

which is unbounded as r tends to zero. The same derivative of -Delta H would be bounded by smoothness on a neighborhood of P. This contradiction proves that eta has no smooth forcing for the stated frozen equation. A harmonic change of the localized inverse leaves its Laplacian unchanged and cannot alter the argument. This scalar assertion is separate from the already proved curl defect of the particular transport pair.

## Removing the exceptional parameter by a logarithmic primitive

The denominator q_j-1 in the power construction does not create a genuine exception to the local transport counterexample. For every odd j>=5 and every A>1 there is such a local C^3 pair with G_i=0 for odd 3<=i<j and G_j/H_j=-1. For A!=j-1 this follows from the already proved power construction, including q_j<1. Here is a complete construction for the remaining value A=j-1.

Let r=-s>0 and set

    F(s,v)=-log(r) v^j chi(v/r^3) for s<0, and F=0 for s>=0.

Use exactly the same coordinate change u=s+F_v, y=v+F_s and pullback formulas for f,a,b as above. Write phi(z)=z^j chi(z), z=v/r^3. Then

    F=-r^(3j) log(r) phi(z),
    F_s=r^(3j-1) B(r,z),
    B=phi+3 log(r)(j phi-z phi'),
    F_sv=r^(3j-4) B_z.

Thus J=1+F_sv is positive after shrinking the neighborhood, uniformly in z. The inverse exists, fixes the endpoints +/-2r^3 and has the same support property. The area calculation proves transport and constant divergence exactly for this F too. It also proves the same y parities.

To verify regularity explicitly, the derivatives of F of orders p in s and k in v have bounds

    |partial_s^p partial_v^k F| <= C r^(3j-p-3k)(1+|log r|).

For total order at most four the smallest power is 3j-12>=3. The zero extension is C^4 by the earlier difference-quotient induction. For the physical fields introduce the two small parameters epsilon=r^(3j-4) and eta=epsilon log r. The inverse equation for Y=y/r^3 is

    Y=z+epsilon phi(z)+3 eta (j phi(z)-z phi'(z)).

Its inverse is smooth jointly in (Y,epsilon,eta), with uniform derivatives near (epsilon,eta)=(0,0). Substituting in the field formulas shows that the bounds for f-y and b-y have leading radial power 3j-1, and that for a-As has leading power 3j-3, multiplied by finite powers of 1+|log r| after differentiation. Each s derivative costs at most one radial power and each y derivative at most three. Consequently the least power for a third derivative is 3j-12>=3; for a derivative of order at most two it is at least 3j-9>=6. These bounds prove the C^3 extension, zero perturbation jets through order three, and the prescribed source matrix. Off the source the construction is smooth, for the same support reason as before.

One can also see the leading horizontal term directly. Put T_j=z phi''-(j-1)phi'. Since A=j-1, exact algebra gives

    a-As = r^(3j-3)[A phi'+(1-3A)log(r) T_j]/J.

Together with the smooth inverse formula, this verifies the preceding derivative bounds without assuming bounded derivatives of a formal inverse series.

In the open inner region chi=1, the identities are

    y=v+r^(-1)v^j,        J=1+j r^(-1)v^(j-1),
    a=As/J,              b=y+A j r^(-2)v^(2j-1)/J.

They follow by direct substitution and are independently checked in code/higher_checks.py. In particular a is not As off the axis at this parameter. Nevertheless the axis data remain w=As, g=1 and b_y=1. Inversion at fixed r gives

    f=y-r^(-1)y^j+O_r(y^(2j-1)).

Hence all the stated lower G_i vanish, while G_j=-r^(-1) and H_j=r^(-1). The normalized source coefficient is -1.

The pair still fails the velocity law. At fixed r and small y,

    a-As=A j y^(j-1)+O_r(y^(2j-2)),
    b-y=O_r(y^(2j-1)),   f_s=-r^(-2)y^j+O_r(y^(2j-1)).

Thus b_s-a_y+f_s has the nonzero leading term -A j(j-1)y^(j-2). This cannot be canceled by a harmonic stream-function correction with f fixed.

The separate smooth-frozen-forcing obstruction also survives. Although W differs from (As,y), direct differentiation of y=v+r^(-1)v^j gives

    (As partial_s+y partial_y)f=f.

Equivalently, W-(As,y)=(partial_y(A f^j),-partial_s(A f^j)) is tangent to the level sets of f in the inner region. Therefore the frozen transport part of f-y still vanishes there. The exact derivative partial_y^j f_ss=-2 j! r^(-3) again contradicts a smooth forcing's Laplacian. At j=5 this is -240 r^(-3).

For j=5, this resonant pair is C^(3,beta) for every beta<1 but a is not C^(3,1). The upper bound follows from the two-point argument with r^3 times logarithmic factors. For sharpness, T_5=(z^6 chi')' is nonzero and has a nonzero third derivative in the layer. The third y derivative of a there contains a nonzero r^3 log r term, whereas it vanishes on the axis at the same s. Their separation is comparable to r^3, so a Lipschitz bound would require bounded |log r|. This regularity refinement is not needed for the all-A C^3 statement.

This is a local transport theorem only. It does not solve the coupled IPM endpoint question, and it does not produce a globally normalized or admissible profile.

## Fourth derivatives above the resonant parameter

For j=5 and A>4 put q=4/A in (0,1). The same nonresonant construction has a-As=r^(13-q) Phi_1(y/r^3,r^(12-q)), with the smooth uniformly controlled inverse functions already established above. Thus each fourth derivative h of a-As has |h|<=C r^(1-q) and |grad h|<=C r^(-2-q). At two points separated by d>=R^3/2, with R the larger depth, use the amplitude bound. For d<R^3/2, integrate the gradient along the segment, whose depths are comparable to R. Both cases give |h(X)-h(X')|<=C d^((1-q)/3). The zero extension is C4 since fourth derivatives vanish and lower derivatives have the required extra radial power. A nonzero fourth derivative T^(4)(z0) gives sharpness by comparison with the same-depth axis, where the horizontal perturbation vanishes. Hence the pair is C^(4,(1-q)/3) and a has no greater fourth-derivative Holder exponent.

For f-y and b-y, the fourth-derivative amplitude is r^(3-q) and its gradient is r^(-q). The same argument gives C^(4,1-q/3). Thus the density alone has a higher class than the pair. This distinction is consistent with the conditional endpoint theorem requiring a common exponent beta>1-q. A canonical IPM velocity would preserve the density's local Holder class up to a smooth harmonic remainder, whereas these particular pairs violate curl directly.

At j=5,A=4, the exact horizontal expression above is r^12[4 phi'+(1-12) log(r)T_5]/J. Four y derivatives have upper bound C(1+|log r|). At a point with T_5^(4) nonzero, their magnitude is bounded below by a positive multiple of |log r| for all sufficiently small r. Since q=1, the weighted annular d_n is of exact order 1+n. This is a statement about the already constructed transport-only example.

Audit correction, 2026-10-20: the homogeneous radial equation in the earlier Fifth coefficient section had a minus sign typo. With s=-r and w=-Ar, w partial_s=Ar partial_r, so the displayed equation is ArG_r+(j-1)G=0. Its stated solution H_j=r^(-(j-1)/A) and all subsequent calculations were already correct.
