# Lead check of the verifier's result (finite physical angular support): coefficient formula, T identity, classification.
import sympy as sp
r, th, a, b, cl = sp.symbols('r theta a b c_l', positive=True)
for N in [1, 3, 5, 7]:
    h = sp.Function('h')(r); T = sp.Function('T')(r)
    rho = h*sp.sin(N*th); psi = T*sp.sin((N+1)*th)
    # U = (-psi_y, psi_x) = grad-perp psi: U.grad rho = (psi_r rho_th - psi_th rho_r)/r
    adv = (sp.diff(psi, r)*sp.diff(rho, th) - sp.diff(psi, th)*sp.diff(rho, r))/r
    c = sp.integrate(sp.expand(sp.expand_trig(0)+adv*sp.sin((2*N+1)*th)), (th, 0, 2*sp.pi))/sp.pi
    target = (N*h*sp.diff(T, r) - (N+1)*T*sp.diff(h, r))/(2*r)
    ok1 = sp.simplify(c - target) == 0
    # d_x(h sin N th) top mode
    dx = sp.cos(th)*sp.diff(rho, r) - sp.sin(th)/r*sp.diff(rho, th)
    cN1 = sp.integrate(dx*sp.sin((N+1)*th), (th, 0, 2*sp.pi))/sp.pi
    ok2 = sp.simplify(cN1 - (sp.diff(h, r) - N*h/r)/2) == 0
    # T from (1) solves -(T'' + T'/r - (N+1)^2 T/r^2) = (h' - N h/r)/2, test on h = r^N/(1+r^2)
    hh = r**N/(1 + r**2); t = sp.symbols('t', positive=True)
    TT = -sp.Rational(1, 2)*r**(-N-1)*sp.integrate((t**N/(1+t**2))*t**(N+1), (t, 0, r))
    lhs = -(sp.diff(TT, r, 2) + sp.diff(TT, r)/r - (N+1)**2*TT/r**2)
    ok3 = sp.simplify(lhs - (sp.diff(hh, r) - N*hh/r)/2) == 0
    ok3b = sp.simplify(sp.diff(TT, r) - (-(N+1)*TT/r - hh/2)) == 0
    # classification: h = (a r + b/r)^N, T = K v^(N+1), K = -1/(4(N+1)a)
    v = a*r + b/r; K = -1/(4*(N+1)*a); h4 = v**N; T4 = K*v**(N+1)
    ok4 = sp.simplify(sp.diff(T4, r) + (N+1)*T4/r + h4/2) == 0
    ok5 = sp.simplify(N*h4*sp.diff(T4, r) - (N+1)*T4*sp.diff(h4, r)) == 0
    print(N, ok1, ok2, ok3, ok3b, ok4, ok5)
