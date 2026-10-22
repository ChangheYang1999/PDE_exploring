# Axis quotients and finite weighted identities for the full target class

Date:2026-10-20. Status: CONFIRMED by independent proof and checked actual Opus38 audit.
This extends several estimates and identities of lead astra/gsrc1
beyond its global-source hypothesis. It is not a nonexistence theorem.

## Statement, hypotheses and notation

Let beta>=2, nu=1/beta, and let a smooth exact B2 profile satisfy the
prompt's x parity, Theta(0,y)=0, nonzero quadratic center temperature,
sublinear relative velocity V, and any polynomial bound on Omega.
Use W=beta X+V, div V=0, V(0)=0, Omega=-curl V and the canonical
relative inverse. Confirmed packets33,36,40 give, at large r, for
all finite derivative orders j,

    D^j Theta=O(r^{1-2nu-j}), D^j Omega=O(r^{-nu-j}),
    D^j V=O(r^{1-nu-j}),
    r^{-(1-2nu)}Theta(r,theta)->h(theta),
    r^nu Omega(r,theta)->a(theta) in every C^j(S1).       (1)

These derivative and tail conclusions are dependencies, not additional
assumptions narrowing the full polynomial-tail target. Let D={x>0}.
The smooth quotients on the closed half-plane are

    P=Theta/x^2, Q=Omega/x, v=V1/x, S=Theta_x/x=2P+xP_x.

They need not have either sign. For every j>=0,

    D^j P=O(r^{-1-2nu-j}), D^j Q=O(r^{-1-nu-j}),
    D^j v=O(r^{-nu-j}), D^j S=O(r^{-1-2nu-j}).          (2)

In particular the gsrc1 quadratic and critical horizontal-weight
identities hold on this entire class without a unique-zero assumption:

    int_D (1+v)P^2=0,
    int_D (1+v)Q^2=int_D Q S,                           (3)

    beta int_{-pi/2}^{pi/2} a(theta)cos(theta)^{-alpha}dtheta
        =alpha int_D x^{1-alpha}(P-vQ), alpha=2-nu.    (4)

Every bulk integral in(3)-(4) is absolutely convergent. The angular
integral in(4) is integrable at both endpoints; its sign is not fixed.

There are also smooth quotient tail coefficients

    p0(theta)=h(theta)/cos^2(theta),
    q0(theta)=a(theta)/cos(theta),                       (5)

where removable axis values are defined by smooth division. Uniformly,

    r^{1+2nu}P(r,theta)->p0(theta),
    r^{1+nu}Q(r,theta)->q0(theta).                       (6)

For every real p>pT=2beta/(beta+2),

    int_D v |P|^p=[beta/p-(beta+2)/2] int_D |P|^p.        (7)

At the two critical powers pT>=1 and pQ=2beta/(beta+1)>1, the outer
flux survives instead:

    beta int_{-pi/2}^{pi/2}|p0|^{pT}
       =-2pT int_D v|P|^{pT},                           (8)

    beta int_{-pi/2}^{pi/2}|q0|^{pQ}
       =pQ int_D [|Q|^{pQ-2}Q S-v|Q|^{pQ}].            (9)

The weighted bulk integrals in(8)-(9) converge absolutely. Values
|Q|^{pQ-2}Q at Q=0 mean0. No unweighted critical Lp norm is claimed
finite, and no flux is discarded.

## 1. Smooth division retains all radial decay bounds

The velocity parity also follows directly from the inverse convention.
The reflected field Vtilde(x,y)=(-V1(-x,y),V2(-x,y)) is smooth, sublinear,
divergence free, zero at0, and has the same negative curl Omega. Its
difference from V is an entire sublinear harmonic field vanishing at0,
hence zero. Thus V1 is odd and V2 is even in x.

For r large and |x|>=r/2, differentiate the defining quotient directly
and use(1). Every x derivative of x^{-k} costs at most a factor C/r,
so(2) follows in this region for P,Q,v. If |x|<r/2, then |y| is
comparable to r along the entire segment (tx,y),0<=t<=1. Smoothness,
evenness and Theta(0,y)=0 imply Theta_x(0,y)=0. Taylor's integral
formula and oddness of Omega,V1 give

    P(x,y)=int_0^1 (1-t)Theta_xx(tx,y)dt,
    Q(x,y)=int_0^1 Omega_x(tx,y)dt,
    v(x,y)=int_0^1 (V1)_x(tx,y)dt.                       (10)

Differentiate under each finite integral. Every derivative is bounded
by the corresponding higher derivative in(1), uniformly on this
segment. This proves(2) everywhere, including the axis. The identity
S=2P+xP_x gives its bounds and also

    |Theta_x|<=C |x|(1+r)^{-1-2nu},
    |Omega|<=C |x|(1+r)^{-1-nu}.                        (11)

Replacing r by1+r absorbs the compact region. No sign, global source,
or nonvanishing-temperature assumption was used.

## 2. Uniform smooth tails of the quotients

At each of the two axis angles the scaled temperature on a circle
has a zero of order at least2, and the scaled vorticity has a zero of
order at least1. These zeros persist in the smooth limits h and a.
In a local angle coordinate z vanishing at the axis, smooth division
by z or z^2 is the integral formula(10) in one variable. It is a
continuous map from C^{j+1} to C^j or C^{j+2} to C^j respectively.
Since cos(theta)/z is smooth and nonzero there, the same holds for
division by cos or cos^2. Away from the axes division is ordinary.
This proves(5)-(6), indeed in every finite C^j norm, from(1).
In particular |a|<=C|cos theta| and |h|<=C cos^2 theta globally.
These statements do not imply positivity of h or nonvanishing off
axis. Those stronger facts used G in packet48.

## 3. Horizontal strain as a convergent full-plane kernel

For X=(x,y) in D and source Y=(s,eta) in D put

    D_-=(x-s)^2+(y-eta)^2, D_+=(x+s)^2+(y-eta)^2.

Pair the x-odd source in the once-subtracted whole-plane inverse.
The horizontal center-subtraction terms cancel between s and-s,
and elementary subtraction of the two remaining denominators gives

    v(x,y)=(2/pi) int_D s^2(y-eta)/(D_-D_+) Q(s,eta)dsdeta. (12)

This integral is absolutely convergent. Indeed
s^2/D_+<=1 and |y-eta|/D_-<=1/|X-Y|. The source Q decays as
(1+|Y|)^{-1-nu}; convolution with1/|X-Y| is locally integrable,
converges at infinity, and is O((1+|X|)^{-nu}). The last bound follows
by splitting into |Y|<r/2, the middle annulus and |Y|>2r: the three
bounds are respectively C r^{-1}r^{1-nu}, C r^{-1-nu}r and
C int_{2r}^infinity rho^{-1-nu}d rho.

The same formula extends to x=0. In a fixed small neighborhood of the
target, the absolute integral is bounded uniformly by C times its
radius, using bounded Q and the 1/distance bound. Outside that
neighborhood dominated convergence applies, with the preceding tail
bound. Hence the smooth axis value agrees with the limiting integral.
This checks the inverse sign and the convergence needed for later
weighted uses. Its kernel changes sign with y-eta.

## 4. Quadratic equations and vanishing boundary flux

Divide the exact transport PDEs smoothly by their parity factors:

    W.grad P=-(beta+2+2v)P,
    W.grad Q=S-(beta+1+v)Q.                            (13)

Using div W=2beta gives the pointwise identities

    div(WP^2)=-4(1+v)P^2,
    div(WQ^2)=2QS-2(1+v)Q^2.                          (14)

Integrate over a right half-disk. The straight boundary contributes
zero because W1=0 on x=0. Its semicircle contributions are bounded by
C R^2 sup P^2=O(R^{-4nu}) and C R^2 sup Q^2=O(R^{-2nu}).
All bulk terms are absolutely integrable by(2). Let R grow to prove(3).
For example the omitted exterior absolute integrals are bounded by
C R^{-4nu} for P^2, C R^{-5nu} for vP^2, C R^{-2nu} for Q^2,
and C R^{-3nu} for vQ^2 or QS.

## 5. Critical horizontal weight and its nonzero possible flux

Since alpha beta=2beta-1, the undivided vorticity equation gives

    div(W Omega x^{-alpha})
           =Theta_x x^{-alpha}-alpha v Omega x^{-alpha}. (15)

Use the half-disk with x>epsilon first. At fixed R the vertical
boundary flux tends to0 as epsilon->0: W1 Omega x^{-alpha}
contains x^{2-alpha} times a smooth bounded function. The bulk
integrands are locally bounded by C x^{1-alpha}, integrable since
alpha<2. For the outer limit, (11) gives absolute bulk radial bounds
C r^{-1-nu}dr times the finite angular integral of cos^{1-alpha}.
Thus the two right-hand terms in(15) converge separately.

On the semicircle the flux integrand is

    (beta+O(R^{-nu}))[R^nu Omega(R,theta)]cos^{-alpha}theta.

It tends pointwise to beta a(theta)cos^{-alpha}theta. By(11), its
absolute value is bounded by C cos^{1-alpha}theta, whose integral
is finite because 1-alpha=-1+nu>-1. Dominated convergence therefore
retains the angular term on the left of(4).

Finally integrate the first bulk term of(15) by parts in x.
The vertical boundary from Theta x^{-alpha} vanishes as epsilon^{2-alpha};
after integrating in y its coefficient remains bounded by(2).
The semicircle boundary is O(R^{-nu}) using Theta=x^2P. Therefore

    int_D Theta_x x^{-alpha}=alpha int_D Theta x^{-alpha-1}
                           =alpha int_D x^{1-alpha}P.

Substitution yields(4), with every boundary contribution accounted for.

## 6. Temperature quotient powers

For p>pT>=1, (13) gives

    div(W |P|^p)=[2beta-p(beta+2)-2pv]|P|^p.            (16)

The absolute bulk integrals converge because p(1+2nu)>2. The
semicircle flux is O(R^{2-p(1+2nu)}), hence tends to0; the axis flux
vanishes. Integration proves(7), including sign-changing P.

At p=pT the first two coefficients in(16) cancel. The remaining
v-weighted bulk term has absolute radial tail O(r^{-1-nu})dr.
The semicircle flux converges by(6) to the left side of(8), giving
that identity. When beta=2, pT=1 and |P| is locally Lipschitz.
The chain rule holds almost everywhere, with grad P=0 almost everywhere
on {P=0}. Thus div(W|P|)=-2v|P| at beta2. Equivalently use smooth convex
regularizations of |P| and pass to the distributional limit on fixed
half-disks before letting R grow. Thus the divergence theorem for
Lipschitz fields proves(8) at this endpoint too. There is no need for
P to have a fixed sign or a regular zero set.

## 7. Vorticity quotient at its critical power

For every p>1 the second equation in(13) gives

    div(W |Q|^p)
      =p|Q|^{p-2}Q S+[2beta-p(beta+1)-pv]|Q|^p.        (17)

Set p=pQ, so the constant coefficient vanishes. The term
|Q|^{pQ-1}|S| is O(r^{-2-nu}); so is |v||Q|^{pQ}. These are
absolutely integrable at infinity and locally integrable at zeros
because pQ>1. The straight boundary has no flux. By(6) the outer
flux is beta int |q0|^{pQ}. Integrate(17) to obtain(9).

## 8. Scope and audit record

The new observation is that the all-derivative class-A bounds already
prove the axis vanishing estimates without the global-source geometry.
Therefore(3)-(4), which gsrc1 proved in G, hold on the entire polynomial
B2 target. The smooth quotient tails and critical identities(8)-(9)
provide further necessary checks. None has an automatically contradictory
sign: v is a signed nonlocal kernel, and P,Q,S can also change sign.
The result neither constructs a profile nor excludes the target.

Dependencies: packets33,36,40 for(1), elementary smooth division,
full-plane kernel pairing, chain rules, divergence theorem and dominated
convergence. No formal proof assistant, numerical solver, or interval
claim is involved in this argument.

## 9. Review and manufactured verification

Actual Opus38 (claude-opus-5-5,219.372655seconds,completed17:34:50Z)
confirmed every stated identity and the extension beyond G. The verifier
checked the response and made velocity parity explicit. Packets33,36,40
were separately reread: they do include beta2, and in that case no
polynomial vorticity hypothesis is needed by packet39. The review had
one transcription error at pT=1, writing -4v in the divergence equation
while keeping the correct -2 in its final identity. The correct
coefficient is -2v, as(16) and the revised paragraph explicitly state.
No erroneous review coefficient was adopted.

Own code code_independent/quotient_flux_manufacture.py tests(7)-(8)
on the exact smooth temperature-transport construction20, using a
separate Cartesian change of variables and both infinite tails. The
manufacture intentionally fails vorticity transport; it tests only
the identities following from the temperature equation. Orders24,48,96
converge to the nonzero critical flux7.5, with highest-order discrepancy
1.60e-14; powers1.5,2,3 agree through7.55e-15. This0.057634second
calculation is not an interval certificate and is not a profile candidate.
See verification/manufacture.json and MANUFACTURE.md.
