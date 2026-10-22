# Exact global thermal transport with a bounded axis component

## Statement

For every beta >= 2, A != 0 and c0 in R there are smooth real functions Psi, Omega, Theta on R^2 such that:

1. Psi and Omega are odd in x, Theta is even in x, and Theta(0,y)=0. Psi and Omega have compact support, Omega=-Delta Psi, and U=(-Psi_y,Psi_x) is the exact full-plane Biot-Savart inverse of Omega. U(0)=(0,c0).
2. With W=beta(x,y)+U-(0,c0), the thermal equation W.grad Theta=(beta-2)Theta holds everywhere. Every mixed derivative of R_Omega=W.grad Omega+Omega-Theta_x vanishes at every point of x=0.
3. Near the origin, Theta=A x^2/2, Omega=2Ax/beta and W=((beta-2)x/2,d y-Ax^2/beta), where d=(3beta+2)/2. Thus the center identities and a0=A/2 hold.
4. The central component of {Theta_xx(0,y)!=0} is J=(-3,3). Every thermal and vorticity axis coefficient is flat at the two endpoints. For T=Theta_xx(0,y), D=Theta_xxxx(0,y), I2=D/T^2 and s=3-|y| inside J,

       D/T=-(6d/beta)s^-2(1+o(1)),    A I2 -> -infinity.

5. Outside a sufficiently large ball centered at (0,c0/beta), Theta is homogeneous of degree alpha=(beta-2)/beta about that center. For each fixed derivative order k it is O(r^{alpha-k}) there. In particular Theta is bounded when beta=2. The vorticity equation fails somewhere off the axis.

These are manufactured non-solutions. They show that exact global thermal transport, the exact inverse, the center and parity conditions, sublinear velocity, and every axis Taylor equation of vorticity do not together exclude a bounded J. They impose no positivity of Omega on x>0. They do not decide existence or nonexistence of B2 profiles.

## A correction lemma for a residual flat on an invariant axis

Let W be smooth on R^2, grow at most linearly, have bounded derivatives of every positive order, and respect x reflection. Its flow Phi_t exists for all real t by the linear growth bound. Let c be real and Theta0 be smooth with compact support. Put R=(W.grad-c)Theta0 and suppose every derivative of R vanishes on the entire axis. Suppose there are C>=1 and kappa>0 such that

    |x(Phi_s Z)| >= C^-1 exp(kappa s)|x(Z)|

for every Z in supp R and every s>=0. Then

    F(X)=integral_{-infinity}^0 exp(-ct)R(Phi_t X)dt

is smooth, flat on the axis, and (W.grad-c)F=R. If Theta0 is even, so is F.

Here is a proof including convergence. Taylor's formula in x and compact support give, for all l,N, |D^l R(Z)|<=C_{l,N}|x(Z)|^N on R^2. The variational equations and Gronwall give |D Phi_t|<=exp(L|t|). Differentiating them inductively shows that each fixed higher derivative is bounded by C_k exp(L_k|t|), uniformly in X for t<=0: its inhomogeneous terms are finite products of lower derivatives and bounded derivatives of W, so a larger exponential majorizes their integrals. The chain rule has finitely many such terms.

If a derivative of R at Phi_t X is nonzero, Phi_t X lies in supp R. Apply the assumed forward estimate for time -t to obtain |x(Phi_t X)|<=C exp(kappa t)|x(X)|. A differentiated integrand is consequently bounded by

    C_{k,N}|x(X)|^N exp((N kappa-c-L_k)t),  t<=0.

Choose N so the coefficient of t is positive. This bound is integrable, locally uniformly in X, after every differentiation. Taking N arbitrarily large proves every derivative of F is flat on x=0. A change of variables gives

    F(Phi_s X)=exp(cs) integral_{-infinity}^s exp(-cu)R(Phi_u X)du.

Differentiating at s=0 proves the equation. Reflection commutes with the flow and preserves R, proving parity. Thus Theta=Theta0-F has exact thermal transport and the same axis jets as Theta0. Also replacing Theta0 by Theta changes R_Omega by F_x, which is flat on the axis.

## Axis data and a choice of exterior drift

Let h(t)=exp(-1/t) for t>0 and zero otherwise, and chi(y)=h(y-1)/(h(y-1)+h(2-y)). On 0<=y<=4 define

    b_*(y)=(1-chi(y))d y+chi(y)(y-3)^2,

and extend oddly to [-4,4]. Thus b_*=dy on [-1,1] and is sign(y)(|y|-3)^2 on 2<=|y|<=4. Its only zeros there are -3,0,3. Because (y-3)^2-dy<=0 and its derivative is negative on [1,2], chi'>=0 gives b_*'<=d everywhere on [-4,4]. For beta=2 a sharper bound is b_*'<=2 on 3/2<=|y|<=4: on [3/2,2], chi>=1/2 and

    b_*'=4+chi'[(y-3)^2-4y]+chi(2y-10)<=y-1<=1;

on [2,4] the derivative is 2(y-3)<=2. Also for 1<=y<=3/2,

    0 <= b_*(y)-2y <= 2y.

Indeed chi<=1/2 and (y-3)^2-4y<=0, so the lower bound is at least (y-3)^2/2.

Choose an odd smooth exterior extension bbar that agrees with b_* on [-4,4] and equals beta y outside a compact interval. For beta>2 it can satisfy sup bbar'<2beta; for beta=2 it can satisfy bbar'<=4 everywhere and bbar'<=3 for |y|>=3/2. To justify existence, prescribe its derivative after y=4. Initially keep the derivative 2(y-3) for a short interval, then use a smooth convex transition to a constant L with beta<L<2beta (choose L=3beta/2 if beta>2, L=5/2 if beta=2). The initial interval and transitions can be sufficiently short that bbar-beta y is still negative. Retain slope L for a variable length, then transition smoothly to beta. The total increase in bbar-beta y depends linearly with positive slope L-beta on that length; choose the length to make the difference zero at the end. Short transitions guarantee that the required length is positive. Thereafter use slope beta. The slope bounds stated above hold, and all derivatives match because the transitions are constant near their endpoints. Odd reflection preserves the derivative bounds. This also proves bbar and its derivatives are bounded on the finite transition region.

Choose an even smooth eta with 0<=eta<=1, equal to1 on a neighborhood of supp(bbar-beta y), and zero sufficiently far out. Its transition lies where bbar=beta y. It can be made arbitrarily wide, so |c0 eta'| can be bounded by any prescribed positive number. Put

    b=bbar+c0 eta-c0.

On [-4,4] this is b_*; outside a compact interval it is beta y-c0. No division by b will be made outside J.

## Smooth realization with quantitative control of the velocity

We recall explicitly the axis construction used here. Set rho=1 on [-1,1] and solve rho'/rho=(d-b')/b on the remaining parts of J. Set a1=A/(2rho^2). With formal series Theta0~sum_{n>=1}a_n x^{2n}, W2~b+sum_{j>=1}v_j x^{2j}, put

    W1~(2beta-b')x-sum_{j>=1}v_j' x^{2j+1}/(2j+1),
    Omega~sum_{n>=0}q_n x^{2n+1}.

The curl recurrence and the two transport recurrences are

    q_n=-v_n''/(2n+1)-(2n+2)v_{n+1},  v_0''=b'',
    b a_n'+[(4n-1)beta+2-2n b']a_n
      =sum_{j=1}^{n-1}[2(n-j)v_j'a_{n-j}/(2j+1)-v_j a_{n-j}'],
    b q_n'+[(4n+2)beta+1-(2n+1)b']q_n
      =2(n+1)a_{n+1}+sum_{j=1}^n[(2(n-j)+1)v_j'q_{n-j}/(2j+1)-v_j q_{n-j}'].

They follow by multiplying the displayed power series in the PDE, and div W=2beta identically. Start with q0=2A/beta near0, solve its nonsingular ODE on each side, set v1=-(b''+q0)/2, solve a2 with zero inner data, and then successively q_n,v_{n+1},a_{n+2}. On [-1,1] only a1=A/2,q0=2A/beta,v1=-A/beta remain. All others are zero. The attachment points +/-1 are nonsingular for b, and the coefficients match smoothly there.

At either endpoint tau=1/(3-|y|) gives b partial_y=partial_tau, b'=-2/tau and rho=C tau^2 exp(d tau). Every fixed derivative of a1 is a polynomially bounded factor times exp(-(3beta+2)tau). Let E_sigma denote this class of exponentially decreasing functions with the same type of bound for every fixed derivative. The equation z_tau+(mu+nu/tau)z=g, mu>sigma>0, sends g in E_sigma to solutions in E_sigma by its integrating factor and differentiation. The separate q0 equation gives q0 in E_{2beta+1}, because its integrating-factor forcing is integrable. Thus v1 approaches -1 at3 and +1 at-3 with an E_{2beta+1}error. Induction in the displayed construction order gives a_n in E_{3beta+2}, q_n in E_{2beta+1} and v_j in E_{2beta+1} for j>=2. The constant part of v1 only multiplies lower derivatives and does not weaken these estimates. All a_n,q_n extend smoothly by zero outside J. Define v_j outside by the curl recurrence, giving v_j=(-1)^j b^{(2j)}/(2j)! there. Each coefficient has compact support. These arguments also appear with full integrating-factor bounds in the proved P278 construction.

Let chi0,chic,chi_j and zeta_n be smooth even horizontal cutoffs, between0and1 and equal to1 near0. Realize

    Psi=(bbar-beta y)x chi0(x)+c0 eta(y)x chic(x)
         +sum_{j>=1} v_j(y)x^{2j+1}chi_j(x)/(2j+1),
    Theta0=sum_{n>=1}a_n(y)x^{2n}zeta_n(x).

Choose the widths in the sums tending to zero. For compactly supported f, the C^k norm of f(y)x^m chi(x/epsilon) is at most C epsilon^{m-k} for k<m. Require the jth/nth summand's C^k norm to be at most 2^{-j}/2^{-n} for k<=j/n. This gives convergence in every C^k, common compact support, and exactly the prescribed axis coefficients. Additionally the jth higher stream term contributes at most C_j epsilon_j^{2j} both to |W1/x| and to |W2|. Thus its width can satisfy arbitrary summable positive budgets for those two quantities at the same time as all C^k conditions. The phrase W1/x denotes the smooth even extension at x=0.

## Expansion estimate when beta>2

Put m=min(beta,2beta-sup bbar')>0. Choose |c0 eta'|<=m/4 and make the total higher contribution to |W1/x| at most m/4. Take any chi0,chic between0and1. The leading transverse coefficient is

    beta-(bbar'-beta)chi0-c0 eta' chic >= m-m/4.

Therefore W1/x>=m/2 everywhere, including the axis. Integrating the scalar equation for |x| proves the correction lemma's hypothesis with C=1 and kappa=m/2. The residual R of Theta0 is compactly supported and flat on the entire axis by the transport recurrences. Apply the lemma with c=beta-2.

## Expansion from the residual support when beta=2

Uniform transverse expansion fails at the center and is not assumed. Fix r>0. Choose chi0 even, between0and1, equal to1 near0, zero for |x|>=r, with

    chi0+x chi0'>=-1/4.

For an explicit existence argument, apply a fixed decreasing smooth cutoff to (log|x|-log a)/L between a=r exp(-L) and r. Taking L at least four times its derivative bound gives |x chi0'|<=1/4, and constant extension near0 is smooth. Let chic=1 on [-r,r] and remain between0and1 with compact support. Put all higher stream cutoffs inside [-r,r] and all thermal cutoffs inside the interval where chi0=1. Choose |c0 eta'|<=1/4 and make each of the two total higher velocity contributions at most1/4.

These choices give

    W1/x>=-1/4 everywhere,
    W1/x>=1/2 if |y|>=3/2 or |x|>=r.            (A)

Where eta'=0, the leading coefficient 2-(bbar'-2)chi0 is nonnegative. Where eta'!=0, bbar=2y and it is at least7/4 after the c0 term. This proves the first bound after subtracting the higher budget. If |y|>=3/2, bbar'<=3 gives the stronger bound1 before the two budgets; if |x|>=r, chi0 and all higher terms vanish, giving at least7/4. This proves(A).

In 1<=y<=3/2 and |x|<=r, eta=chic=1. The center constant cancels, and

    W2=2y+(bbar-2y)(chi0+x chi0')+higher terms
       >=2y-(2y)/4-1/4>=5/4>1.

The reflected lower band has W2<=-1 by the same estimate with bbar-2y odd and a possibly signed higher error of size1/4. Reflection in y of the full fields is not assumed or needed.

On |y|<=1 the higher thermal coefficients vanish, a1=A/2, all v_j'=0 and eta'=0. Thus Theta0=(A/2)x^2 zeta1(x) and W1=2x(1-chi0). Its entire support lies where chi0=1. Consequently R=0 throughout that strip, and

    supp R subset {|x|<=r, |y|>=1}.

A forward trajectory starting in this support with x!=0 either starts where the second bound in(A) holds, or traverses a passage band 1<=|y|<=3/2. It leaves the latter through |y|=3/2 or |x|=r within time at most1/2, since |W2|>=1 with outward sign. During this passage |x| contracts by at most exp(-s/4). Afterwards it never returns: at |y|=3/2 with |x|<=r the field points outward, and at |x|=r it has strictly outward transverse component at every y. Hence subsequently d(log|x|)/ds>=1/2. For all s>=0,

    |x(Phi_s Z)|>=exp(-3/8)exp(s/2)|x(Z)|.

For x=0 the same inequality is trivial. This proves the lemma with C=exp(3/8), kappa=1/2. Applying it gives exact thermal transport at beta2 as well.

## Center, endpoint, inverse and far-field conclusions

In both cases set Theta=Theta0-F and Omega=-Delta Psi. The lemma preserves every axis coefficient and all parities. Near0 the uncorrected fields are exactly the polynomials in the statement. The backward trajectory of a sufficiently small point stays in this polynomial region: with c=beta-2 and K=A/[beta(d-c)],

    x(t)=exp(ct/2)x(0),
    y(t)=exp(dt)(y(0)-K x(0)^2)+K exp(ct)x(0)^2, t<=0.

Since d>0 and c>=0, these remain uniformly small when the initial point is small. In that region R=0, so F=0 there. This also covers beta2, where x stays constant and y tends to A x^2/8. The exact center fields are unchanged.

The endpoint calculation depends only on the preserved jets. Here T=2a1,D=24a2,v=v1 and

    bD'+(7beta+2-4b')D=8v'T-12vT'.

Near either end v=-sign(y)-q0/2 and T'/T=-sign(y)(4tau+2d tau^2). Thus K0=D/T obeys

    (K0)_tau+(4beta+4/tau)K0=-24d tau^2-48tau+E_{2beta+1}.

Subtract a degree-two polynomial whose leading coefficient is -6d/beta. Its remaining forcing is O(1/tau); the integrating factor tau^4 exp(4beta tau) gives an O(1/tau) remainder. Hence K0~-(6d/beta)tau^2. Since A I2=rho^2 K0 and rho^2 tends to positive infinity, the claimed limits follow. The component J and flatness persist because every thermal axis coefficient was unchanged.

For Gamma=-(1/(2pi))log|X|, -Delta Gamma=delta. Compact support of Psi permits distributional integration by parts to give Gamma*(-Delta Psi)=Psi, with no harmonic remainder. Differentiation gives the canonical velocity kernel, whose local singularity is integrable against the smooth compact source. Thus U=K*Omega, U(0)=(0,c0), and U is compact. U-U(0) is generally constant outside the support, not compact when c0!=0, but is sublinear.

Outside a ball centered at Xc=(0,c0/beta), U=0 and W=beta(X-Xc). The now exact thermal equation gives, for r>=R,

    Theta(Xc+r omega)=(r/R)^alpha Theta(Xc+R omega), alpha=(beta-2)/beta.

Smoothness on the fixed sphere yields the stated derivative bounds by differentiating in polar coordinates, which are nonsingular for r>=R>0.

Finally suppose the vorticity equation held globally. Outside a rectangle containing supp Omega and supp U it implies Theta_x=0. On every horizontal line with |y| large this holds for all x, so Theta(0,y)=0 gives Theta=0 on that line. For x sufficiently large of either sign, Theta is a function f_+(y) or f_-(y) with compact y support. There exact thermal transport says (beta y-c0)f'=(beta-2)f. Uniqueness on each half-line separated by c0/beta, using its zero values for large |y|, makes f zero; continuity gives zero at the separating point as well. Thus Theta would have compact support. Integration by parts with div W=2beta would then give

    0=integral Theta R_Theta=2(1-beta)integral Theta^2<0,

a contradiction to A!=0 and beta>=2. The vorticity residual is therefore nonzero somewhere, necessarily off the axis. Also integral x Omega=0 by integration by parts against the harmonic function x. Since Omega is nonzero and odd, it cannot have one sign throughout x>0. This identifies a concrete hypothesis absent from the example.

## Dependencies and evidence

The coefficient induction is the proved P278 construction, repeated above with the altered exterior extension and additional summable cutoff bounds. Its low-order endpoint argument is also rederived above. The new ingredient is the globally justified flat-residual correction lemma and the beta2 passage estimate. The proposal appeared in the lead's A162publicreview; none of its claims is accepted without the argument here. Independent symbolic/manufactured controls and an actual Opus5.5review are recorded separately. They supplement the proof and are not numerical evidence of a B2profile. No formalization is claimed.

Complete informal argument written 2026-10-22T05:28:19.168943+00:00 before controls.
