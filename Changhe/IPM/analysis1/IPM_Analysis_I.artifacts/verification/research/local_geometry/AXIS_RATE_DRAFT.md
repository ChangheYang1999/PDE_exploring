# Rate at the center supplied by the exact axis ODE

Status: freshly reconstructed proof, pending adversarial model review. This complements PROOF.md; it does not infer convergence merely from g~x^2.

Suppose an exact P_2 profile has rho in C^{2,alpha} locally, 0<alpha<1, strong continuous center factor a(0)=1, and canonical stream function solving -Delta psi=rho_x in distributions. Interior elliptic regularity gives psi in C^{3,alpha} and U in C^{2,alpha} locally. Here the local Schauder regularity theorem is an explicit analytical dependency; it gives regularity, not a quantitative global bound. Put A=2c_l-1 and assume A is nonzero.

On the x axis, w=V_1 is odd and C^{2,alpha}. The center normalization gives w'(0)=-A, and oddness gives w''(0)=0. Hence

w(x)=-A x+e(x),  |e(x)|<=C x^{2+alpha},  |e'(x)|<=C x^{1+alpha}.

The density factor implies g(x)=rho_y(x,0)=x^2 a(x,0), so g/x^2 tends to one. This follows directly by taking the derivative in y using the continuous factor, without differentiating a. In particular g>0 for sufficiently small positive x. The exact axis equation gives

(log(g/x^2))' = (w'-A)/w -2/x = (x e'-2e)/(x w).

For sufficiently small positive x, |w|>=|A|x/2. The right side is O(x^alpha), which is integrable at zero. Since log(g/x^2) tends to zero, integration gives log(g/x^2)=O(x^{1+alpha}), and therefore

g(x)=x^2(1+O(x^{1+alpha})).

Consequently (1/g-1/x^2)=O(x^{alpha-1}), an integrable function. If also g>0 up to x_*>0 and w(x_*)=0, the representation

w(x)=-A g(x) integral_x^{x_*}1/g(t) dt

holds. Writing J=integral_0^{x_*}(1/g-1/x^2)dt and using the derived rate yields

w(x)=-A x-A(J-1/x_*)x^2+o(x^2).

Odd C^2 regularity forces the quadratic coefficient to vanish, so J=1/x_*.

Thus the finite-part compatibility follows for an exact P_2 solution with A nonzero, a canonical distributional inverse, and a positive-g source interval. It does not follow from g~x^2 alone for an arbitrary trial. The unknown global source and positivity must still be proved for any exact solution claimed by an endpoint theorem.

Quantitative local version: if |e|<=C_0 x^{2+alpha}, |e'|<=C_1 x^{1+alpha}, |w|>=|A|x/2, then

|log(g/x^2)| <= 2(C_1+2C_0) x^{1+alpha}/(|A|(1+alpha)).

A numerical use must certify C_0,C_1 and the interval on which the lower bound for w holds.
