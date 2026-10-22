# Formal center recursion and smooth flat-residual realization

Written UTC 2026-10-21T03:52:41.409755+00:00 before the packet119 implementation. Independent audit of the lead's draft4.28, read from its lane on2026-10-21. Status: complete informal argument and exact higher-order controls CONFIRMED; actual Opus155 returned no written audit, recorded in verification/SUMMARY.md. This is a construction satisfying only the temperature equation globally. It does not construct a Boussinesq profile or prove nonexistence.

## Statement and notation

Fix beta>2 and a0!=0. Write l=(beta-2)/2, m=1+3beta/2, c=1+beta/2, A=diag(l,m). For a formal series let f_n denote its homogeneous part of degree n. Let O_n be the homogeneous polynomials of degree n odd in x. The relative stream gauge is

    V=(-Psi_y,Psi_x)-(-Psi_y(0),Psi_x(0)),
    W=beta X+V, Omega=-Delta Psi.

An affine x term in Psi has no effect on these fields and can be set to zero. Take Psi_2=cxy and Theta_2=a0x^2, with lower temperature terms zero. There is a unique formal temperature series solving

    R_T=W.grad Theta-(beta-2)Theta=0.                (T)

For each n>=1 its vorticity residual has the triangular form

    (R_O)_n=(A X.grad+1)Omega_n+N_n,
    R_O=W.grad Omega+Omega-Theta_x,                 (V)

where N_n uses only beta,a0,Psi_3,...,Psi_(n+1). Once Psi_3 satisfies -Delta Psi_3=(4a0/beta)x, every sequence of harmonic coordinates for Psi_j, j>=4, determines one formal Psi for which all (R_O)_n vanish. A complement to the harmonic line in each O_j must be fixed to define those coordinates. No convergence of the formal series is asserted.

For every beta>2 and a0>0, there also exists a smooth full-plane realization with the following properties: (T) holds exactly; Theta has B2 parity, is positive off the axis, vanishes on it and has quadratic jet a0x^2; Omega>0 for x>0; V is the canonical relative full-plane inverse of Omega; the center strain and vorticity derivative are c and4a0/beta; every backward orbit of W tends to0; V is sublinear and Omega has a nonzero r^(-1/beta) tail; and R_O is flat at0. The vorticity equation away from0 is not established. The construction preserves the exterior velocity and vorticity of the explicit base field below.

## Formal recursion

For degree d>=3, the temperature equation reads

    (A X.grad-2l)Theta_d
      =-sum_(k=2)^(d-1) W_k.grad Theta_(d+1-k).     (1)

On x^i y^j of degree d its left operator is multiplication by i l+j m-2l. If j=0 this is(d-2)l>0. If j>=1 it is at least m-2l=3+beta/2>0. Thus(1) uniquely determines Theta_d using W_2,...,W_(d-1), hence Psi_3,...,Psi_d. Induction preserves evenness in x and the factor x^2: W_1 is divisible by x, W_2 is even in x, and differentiating a polynomial divisible by x^2 followed by multiplication by W_1 or W_2 preserves that divisibility. Here W_1 and W_2 in this divisibility sentence denote the Cartesian components, not homogeneous degrees.

Because Omega_0=0, the degree-n vorticity residual is

    (A X.grad+1)Omega_n
      +sum_(k=2)^n W_k.grad Omega_(n+1-k)
      -d_x Theta_(n+1).                            (2)

In the sum the stream indices are k+1 and n+3-k, both<=n+1. Formula(1) shows that the last term also uses stream degrees only through n+1. This proves the triangular dependence. The diagonal multiplier of A X.grad+1 on x^i y^j is i l+j m+1>0, so Omega_n is uniquely determined by the lower data if(R_O)_n=0. At n=1 it is(4a0/beta)x.

For completeness, -Delta maps O_(n+2) onto O_n with a one-dimensional kernel. An elementary right inverse is obtained by excluding the domain monomial with largest odd x exponent and solving coefficients in descending odd x exponents. If H in O_n is prescribed and D in the chosen complement satisfies -Delta D=H, then for i odd and j=n-i,

    D_(i,j+2)=[-H_(i,j)-(i+2)(i+1)D_(i+2,j)]/[(j+2)(j+1)],        (3)

starting with the excluded coefficient equal to0. This always determines D. Counting monomials leaves exactly one kernel dimension. Direct differentiation shows that its generator is Re(x+iy)^(n+2) when n is odd and Im(x+iy)^(n+2) when n is even; this generator is odd in x and nonzero. Other complements give the same unique solution after adding the specified harmonic multiple. Induction in(2) proves the formal claim. The coefficients are rational when beta,a0 and the prescribed coefficients are rational.

## A positive slow-tail base field

Put s=1/beta, p=(1-s)/2, L=3c sqrt(beta)/(4a0), h=sqrt(beta)L, S=L^2+x^2+(y-h)^2, S0=L^2+h^2, and

    B=c/[2ph S0^(p-1)],
    Psi^e=-Bx S^p,
    Omega^e=4Bp x S^(p-2)[2L^2+(p+1)(x^2+(y-h)^2)].            (4)

Direct differentiation verifies the second formula from -Delta Psi^e. It proves Omega^e/x>0 everywhere, including its continuous axis extension. The strain is2Bph S0^(p-1)=c. Its central vorticity derivative is3c/h=4a0/beta. The velocity, its derivative and vorticity have bounds O(r^(1-s)), O(r^-s), O(r^-s), respectively, with a nonzero vorticity tail.

Let W^e=beta X+grad^perp Psi^e-grad^perp Psi^e(0), and b^e(y)=W^e_2(0,y). Then

    W^e_1/x=beta+2Bp(y-h)S^(p-1),
    (b^e)'=beta-2Bp(y-h)[L^2+(y-h)^2]^(p-1).       (5)

The maximum of |u|(L^2+x^2+u^2)^(p-1) over u occurs at u^2=beta(L^2+x^2). The resulting maximum decreases as|x| increases because its factor in L^2+x^2 has exponent p-1/2<0. Thus its global maximum occurs at x=0,|u|=h and, after multiplication by2Bp, equals c. Both quantities in(5) are therefore at least l>0. All first derivatives of the velocity are bounded. The canonical inverse statement follows from the harmonic uniqueness argument below.

## Realizing the formal stream series while preserving the inequalities

Fix a complement at each degree and keep the harmonic coordinates of Psi^e. The formal construction yields corrections D_j in O_j, j>=4. Choose one fixed smooth radial cutoff chi equal to1 on the unit ball and0 outside the ball of radius2. Such a cutoff can be made from the smooth function exp(-1/t) on t>0, extended by0 on t<=0. For each j choose0<eps_j<=1 sufficiently small that

    ||chi(X/eps_j)D_j(X)||_(C^(j-1)) <= 2^-j eta.   (6)

The C^k norm here is the maximum of suprema of all partial derivatives through order k. For k<j, scaling and homogeneity give a bound C_(j,k) eps_j^(j-k), so(6) is possible for each j, with no growth restriction on the formal coefficients. Define

    delta=sum_(j>=4) chi(X/eps_j)D_j(X).            (7)

For fixed k, all sufficiently large j satisfy j-1>=k and their C^k norms are summable by(6). The finitely many other terms are smooth. Hence(7) converges in every C^k, is smooth, odd in x, supported in the ball of radius2, and ||delta||_C3<=eta. Since each cutoff is locally constant at0, termwise differentiation at0 shows that its Taylor series is exactly sum D_j. It vanishes through degree3.

Set Psi=Psi^e+delta, Omega=-Delta Psi and V=grad^perp Psi-grad^perp Psi(0). The center data are unchanged. Let c_* be the positive minimum of Omega^e/x on the closed ball of radius2. Oddness of Delta delta and the fundamental theorem of calculus along horizontal segments give

    |Delta delta(x,y)/x|<=sup|d_x Delta delta|<=2eta.

The segments remain in that ball for endpoints there; outside it the perturbation is zero. Choosing eta<c_*/2 preserves Omega>0 for x>0. Similarly, oddness of delta_y gives |delta_y/x|<=eta, and |delta_xy(0,y)|<=eta. Choosing eta<=l/2 leaves

    W_1/x>=l/2, b'(y)>=l/2, b(0)=0,               (8)

where b=W_2(0,y). Bounded derivatives imply a complete flow. If kappa=l/2 and M=sup|Psi_xx|, then along backward time tau,

    |x(tau)|<=|x(0)|e^(-kappa tau),
    D^+|y(tau)|<=-kappa|y(tau)|+M|x(tau)|.

The second inequality follows from y b(y)>=kappa y^2 and |W_2(x,y)-b(y)|<=M|x|. Integration gives

    |y(tau)|<=e^(-kappa tau)(|y(0)|+M|x(0)|tau).

Every backward orbit tends to0, as claimed.

The relative Biot-Savart integral for Omega converges: the subtracted kernel at large source radius is O(|X||Y|^-2), multiplied by Omega(Y)=O(|Y|^-s), whose radial integral converges. Local singularities are integrable for the velocity. Splitting at radii comparable to|X| also gives sublinear growth O(1+|X|^(1-s)). Its difference from V is an entire divergence-free and curl-free vector field, hence harmonic, sublinear and zero at0. The gradient estimate on balls of radius R bounds its gradient at any fixed point by o(R)/R, so the difference is constant and therefore0. Thus V is canonical. Outside the perturbation support the raw velocity and vorticity equal those of(4), and their relative velocities also agree because grad delta(0)=0.

## Smooth temperature and flat residual

Write the horizontal component as W_1=x(l+B_1(X)), with B_1 smooth, even in x and B_1(0)=0. The global source property and local contraction give the well-defined expression

    xi(X)=x exp[-int_0^infinity B_1(phi_(-t)X)dt].  (9)

Here is a direct smoothness argument, avoiding an unproved linearization claim. In a sufficiently small backward-invariant ball, for any fixed0<mu<l, the symmetric part of DW is bounded below by mu times the identity. The backward flow and its first variational equation contract at rate mu. Inductively, every higher variation solves the same stable linear equation with a forcing made from at least two lower variations. Those products are O(e^(-2mu t)); variation of constants bounds every variation by C_k e^(-mu t). The chain rule therefore bounds each derivative of B_1 composed with the backward flow by C_k e^(-mu t), and its value has the same bound since B_1(0)=0. This justifies differentiating the integral in(9) to every order locally. Every compact subset of the global basin enters this ball after a uniform finite backward time, so the same conclusion holds globally.

Shifting time in(9) gives xi(phi_tX)=e^(lt)xi(X). Also xi=x+O(|X|^2), it is odd in x, and its multiplier of x is positive. Therefore Theta=a0xi^2 is smooth, solves(T) exactly, is positive precisely off the axis, and has the prescribed quadratic jet. Its Taylor series is the unique series from(1) for the actual stream Taylor series. Since the latter is the constructed formal series, every Taylor coefficient of R_O vanishes. This proves the smooth realization.

## Scope and audit points

This realization changes the original example in its compact core. It does not make the original unperturbed example satisfy its failed third-order vorticity condition. The defensible conclusion is that no collection of center Taylor equalities, together with the listed configuration properties, excludes every such smooth configuration. A proof would still need the vorticity equation on points outside the center, or a further global constraint. No convergence of the formal series, local analytic solution, exact vorticity equation on an open set, or full profile is proved here. Conversely, the construction does not prove that R_O must be nonzero away from0; that issue is left open.

For exact computational controls, the base Taylor series can be written without irrational coefficients when sqrt(beta),a0 are rational:

    Psi^e= -cS0/(2ph) x [1+(x^2+y^2-2hy)/S0]^p.

The own implementation will expand this generalized binomial series, solve(1)-(3), and verify the complete polynomial PDE independently after each recursion. The complement for the reported D_j excludes the monomial with largest odd x exponent. This convention is required when comparing individual corrections from different computations.

Dependencies: elementary homogeneous polynomial algebra, the explicit field(4), the cutoff construction(6)-(7), elementary flow/variation estimates and harmonic uniqueness. Packet04 proves the corresponding source-basin formula at lower regularity; the argument above supplies the all-orders statement used here. No Lean proof or build is claimed.

## Entered-report additions, independently checked 2026-10-21T04:13:50.745939+00:00

For the constructed field, U is sublinear and the temperature equation holds. Choose R0 so that X.W >= (beta/2)|X|^2 outside R0. Under backward flow r'(t) <= -(beta/2)r until entry, hence the entry time is at most (2/beta)log(r/R0). Transport gives Theta(X)=exp((beta-2)t)Theta(phi_(-t)X). The continuous temperature is bounded on the entry sphere, so |Theta(X)| <= C(1+r)^[2(beta-2)/beta]. This is a polynomial bound, not the sharper profile asymptotic obtained using both equations.

Set b=W2(0,y), q=Omega_x(0,y), a=Theta_xx(0,y)/2, M=2beta+1, Lambda=3beta+2. Parity and div W=2beta give the two axis equations

    b a'=(2b'-Lambda)a,
    d_x R_Omega=bq'+(M-b')q-2a.

Write H=bq'+(M-b')q and F=bH'-(2b'-Lambda)H. If d_x R_Omega vanishes on an open interval then H=2a there and F=0 there. In the base example b(0)=0, b'(0)=Lambda/2, b''(0)=0. Consequently H'(0)=M q'(0) and F'(0)=(Lambda/2)M q'(0). Direct differentiation of the explicit base field gives

    q'(0)=32 a0^2(3beta+5)/(9 beta^2(beta+1)(beta+2))>0.

Thus F is real analytic and nonzero. It cannot vanish on any open interval. The compact stream perturbation constructed above vanishes to order four at the center, so U(0) is unchanged. Outside its support b,q equal the base b,q. Thus its d_x R_Omega cannot vanish on any exterior axis interval. This proves that these particular fields are not profiles, independently of an uncomputed temperature outside the center.

Scope of the formula matters: equality of U and Omega outside a compact set does not alone imply equality of the relative b unless U(0) also agrees. A general compact vorticity perturbation has a separate lower-axis obstruction, proved in packet121. The entered 4.28 construction itself does preserve U(0), so the displayed F argument applies to it.
