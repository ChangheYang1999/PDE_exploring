# A torus diffeomorphism with a prescribed stable derivative

Date: 2026-11-02T22:17:24Z. Verdict: CONFIRMED, A224. This verifies the literature agent LIT45, including its explicitly conditional trapping conclusion. It does not construct the trapping disk.

## Statement

On T2=R2/Z2 with area one set A=((2,1),(1,1)), q=(1+sqrt(5))/2, K=(3+sqrt(5))/2, ell=1/K, v=(1,-q), and eta=q dx+dy. Fix 0<rho<ell. If g is any nonnegative smooth function with integral ell-rho, there is a unique real smooth mean-zero h satisfying D_v h=g-(ell-rho). For every b in R2, f([x])=[Ax+h(x)v+b] is a smooth orientation-preserving torus diffeomorphism, with

    f*eta=K eta, Df(v)=(rho+g)v, det Df=K(rho+g).

If supp g is compactly contained in a smoothly bounded open disk D, these equations reduce on a neighborhood of N=T2 minus D to f*eta=K eta and Df(v)=rho v. IF f inverse(closure D) is compactly contained in D, then f(N) is compactly contained in int N and Lambda=intersection_(n>=0) f^n(N) is a nonempty locally maximal hyperbolic attracting set. No such disk inclusion is proved here. For 0<c<1/2 and rho=K^(-(1+c)/(1-2c)), the multipliers and roof log(K)/(1-2c) agree with A204.

## Proof

The identities Av=ell v, eta A=K eta, and eta(v)=0 follow by substituting q^2=q+1. For k=(m,n) nonzero, the product (m-q n)(m-q' n)=m^2-mn-n^2 is a nonzero integer, where q'=(1-sqrt(5))/2. Its nonvanishing follows from irrationality of q (or directly when n=0). Consequently |k.v|>=C/(1+|k|) for a fixed C>0.

For the Fourier convention exp(2 pi i k.x), set h_0=0 and h_k=g_k/(2 pi i k.v) for k!=0. Smoothness of g gives decay of its Fourier coefficients faster than every power, and division loses at most one power. Each differentiated series therefore converges absolutely and uniformly. It defines a smooth solution, real because h_-k is the conjugate of h_k. A second mean-zero solution has every coefficient zero. This is an exact series argument, not a Fourier truncation.

The lift respects integer translations since A has integer entries. Its derivative is A+v tensor dh. Thus f*eta=eta A+eta(v)dh=K eta and Df(v)=(ell+D_v h)v=(rho+g)v. In the constant basis (v,w), where eta(w)=1, the derivative is triangular with diagonal rho+g and K. It has positive determinant. The map is a local diffeomorphism of a compact connected torus, hence a finite covering. It is homotopic to A and has degree det A=1, so it is a one-sheeted covering and a global diffeomorphism.

The support condition gives the two constant tensor laws near N. The additional disk inclusion is equivalent, by complements and compactness, to f(N) compactly contained in int N. The nested nonempty compact sets f^n(N) have a nonempty intersection Lambda, invariant under f and its inverse. On it write Df(x)w=K w+a(x)v, with a bounded continuous. The series

    z(x)=sum_(j>=1) rho^(j-1) K^(-j) a(f^(-j)x)

converges uniformly and satisfies K z(fx)=a(x)+rho z(x). Hence the complementary invariant lines are E^s=R v and E^u_x=R(w+z(x)v), with exact scalar multipliers rho and K. Boundedness on compact Lambda supplies equivalent continuous norms, and therefore uniform hyperbolicity. The trapping neighborhood supplies local maximality. None of this asserts transitivity of all of Lambda or any suspension topology.

Finally, a bump g with g(p)>1-rho and the translation b=p-Ap-h(p)v makes p a source, since both multipliers exceed one. A small repelling neighborhood of that point need not contain the entire support of g. The missing disk inclusion does not follow from this local source construction.

## Dependencies and scope

Read and checked the entire submitted proof in the team records. The argument uses Fourier series, the quadratic irrational norm, elementary covering theory and the displayed convergent invariant-line series. No affine-attractor source theorem or numerical evidence is needed. The construction does not impose Euler curl coupling and does not yet produce A204's surface triple on a trapping once-holed torus.
