# Negative pressure source for the circulating Volterra carrier

Status: LIT305 is confirmed after the complete ten-item coordinator comparison. This tests the specified carrier family against the complete common-flat system, with its strict scalar sign and zero set.

## 1. Exact theorem

Let 0<c<1/2, omega be any finite real number, Jx=e3 cross x, A=cI-omega J, X(x)=Ax, L=(1-c)I+omega J, a=1-2c and b0=2(1-c). Let sigma:D_R->R3 minus {0} be a smooth transverse section, with sigma(0)=x0 and det(sigma_1,sigma_2,X(sigma)) nonzero. All assertions hold after shrinking the disc and a finite X-flowbox about it. Set

    j=|det(sigma_1,sigma_2,X(sigma))|,
    beta_i=X(sigma).sigma_i/|X(sigma)|^2,
    b=(3c-1)beta.

Let f:(0,R)->(0,infinity) be smooth and nondecreasing, with f^(k)(r)=O(r^N) for every pair of nonnegative integers k,N. Assume also

    r f'(r)>=f(r)                                           (1)

for every sufficiently small r>0. Define the carrier by the exact formulas in Section2. It is smooth and flat on precisely its central X orbit Gamma, and

    tr((DV)^2)(sigma(y))=-2 f(r)f'(r)/(j(y)^2 r)+O(f(r)f'(r)),
    tr((DV)^2)<0 off Gamma, tr((DV)^2)=0 on Gamma.           (2)

The error is uniform in the angle, on a sufficiently small disc. All constants may depend on the fixed c, omega and section; there is no uniform-in-omega assertion. The second line holds on a whole smaller flowbox, not just on the section.

Consequently this V has no smooth scalar completion S on a neighbourhood of x0 satisfying all of

    div V=0, W=curl V, k=X.V=0, DV X=-LV,
    X.grad S=-b0 S, grad k=X cross W-aV, W.grad S=0,
    P=S+|V|^2/2, -Delta P=tr((DV)^2),                       (F)

with S=0 on Gamma, S<0 off Gamma, and S flat at x0. This exact non-completability is distinct from the earlier observation that no completion was supplied. It does not exclude a Poisson pressure alone, another scalar sign or zero set, or a different carrier.

The non-completability step uses the exact C61 theorem confirmed in A2233-A2234: every neighbourhood of a common-flat point under all F premises contains positive tr((DV)^2). Its complete eight-section independent proof and the exact six ledger entries A2230-A2235 were reread. Sections2-5 below prove (2) directly; no numerical computation is used.

## 2. Carrier construction and bounds which do not differentiate the radial factor

Write y=r e_r, e_r=(cos theta,sin theta), e_theta=(-sin theta,cos theta), b_r=b.e_r and b_theta=b.e_theta. Put

    q(r,theta)=r^-1 integral_0^r t b_theta(t,theta) f(t)
                         exp(integral_t^r b_r(u,theta)du)dt,
    w=f e_theta+q e_r, v=w/j, h=-beta.v,
    Phi(y,s)=exp(sA)sigma(y),
    V(Phi(y,s))=exp(-s)D Phi(y,s)(v(y),h(y)).                (3)

The positive j, bounded smooth coefficients and monotonicity of f give

    |q|<=C r f, |q_theta|<=C r f,
    q_r=b_r q+b_theta f-q/r, |q_r|<=C f,
    |D_y(q e_r)|<=C f.                                    (4)

For the first bound, use f(t)<=f(r) and integrate t from 0 to r. Angular differentiation acts only on smooth coefficients and bounded integrals in the kernel, giving the second bound. The third is the differentiated Volterra identity and implies the fourth. The last follows from the polar derivative formula, with q_theta/r and q/r both O(f). In particular these bounds contain no f' term. All fixed higher mixed derivatives are flat: angular derivatives retain the same integral form, and repeated radial differentiation of the displayed ODE introduces only fixed powers of 1/r, smooth bounded coefficient derivatives and derivatives of f. This proves smooth flat extension in Cartesian coordinates by difference quotients.

The tangential component f is positive, so w is nonzero for r>0. Invertibility of the coordinate map gives the stated exact zero set for V. The coordinate volume density is exp(3cs)j and X=partial_s. Thus

    div w=(r q)'/r=b.w,
    div V=exp(-s)j^-1[div(jv)+(3c-1)jh]=0,
    [X,V]=-V, DV X=(A-I)V=-LV.

On the section X.V=|X|^2(beta.v+h)=0. Since exp(sA) is a dilation times an orthogonal rotation, this equality transports to the flowbox. Differentiating it gives DV^T X=-A^T V and therefore

    X cross W=DV^T X-DV X=(L-A^T)V=aV.

This verifies every carrier identity used in F. No pressure or scalar equation is imposed in the construction.

## 3. The leading transverse matrix and its exact squared trace

Let nu=1/j. The derivative of the main tangential field is

    T=D_y(f e_theta)=f' e_theta tensor e_r-(f/r)e_r tensor e_theta.

In the orthonormal basis (e_r,e_theta), T has the matrix

    [[0,-f/r],[f',0]],
    tr(T^2)=-2ff'/r, |T|<=f'+f/r.                          (5)

Here f'>=0. Bounded derivatives of nu and (4) give

    D_y v=nu T+E1, |E1|<=C f.

Consequently

    tr((D_y v)^2)=-2nu^2ff'/r+O(ff'+f^2/r+f^2).             (6)

Indeed the mixed trace terms are bounded by C|T|f and the remaining square by Cf^2. The potentially large rank-one term f' e_theta tensor e_r squares to zero because e_r.e_theta=0. It therefore produces no (f')^2 term. All errors differentiate only a smooth chart coefficient or the corrected radial field, and those derivatives are O(f).

Also |v|+|h|<=Cf, and |D_y h|<=C(f'+f/r+f), by h=-beta.v. These bounds include every block of the coordinate derivative needed next.

## 4. The moving coordinate frame contributes only a lower-order term

Write z=(y1,y2,s), Fmat(z)=D Phi(z) and Z(z)=exp(-s)(v(y),h(y)). Then V composed with Phi equals Fmat Z. Differentiating this identity column by column gives exactly

    Fmat^-1 DV(Phi(z)) Fmat=D_z Z+K,
    K_j=Fmat^-1 (partial_j Fmat) Z.                         (7)

On a fixed compact smaller flowbox, Fmat, its inverse and its first derivatives are bounded. Hence |K|<=Cf. At s=0,

    D_z Z=[[D_y v,-v],[D_y h,-h]],
    tr((D_z Z)^2)=tr((D_y v)^2)-2(D_y h).v+h^2.              (8)

Its norm is at most C(f'+f/r+f). Since trace of a square is invariant under conjugation, (7) changes (8) by at most C(ff'+f^2/r+f^2). Inserting (6) proves

    tr((DV)^2)(sigma(y))=-2ff'/(j^2r)+O(ff'+f^2/r+f^2).

By (1), f^2/r<=ff' and f^2<=R ff', so this is the first line of (2). The ratio of the error to ff'/r is O(r). The positive function 1/j has a positive lower bound on the closed disc, and ff'>0 by (1). The trace is therefore strictly negative on a sufficiently small punctured disc. Flatness gives zero trace at its centre.

This is an exact tensor calculation followed by an explicit error bound. Dropping K without estimating it would not establish the Euclidean pressure-source sign.

## 5. Transport and the precise pressure contradiction

The carrier transport integrates to V(exp(sA)x)=exp(-s)exp(sA)V(x). Differentiating with respect to x yields

    DV(exp(sA)x)=exp(-s)exp(sA)DV(x)exp(-sA),
    tr((DV)^2)(exp(sA)x)=exp(-2s)tr((DV)^2)(x).              (9)

Thus the section sign extends to every point off Gamma in a smaller flowbox, while V and DV vanish on Gamma. This proves the second line of (2).

If S completed V to F with the exact strict sign, one-orbit zero set and infinite flatness in Section1, C61 would give positive trace in every neighbourhood of x0, contradicting (2). All its hypotheses agree: the carrier identities were checked in Section2, the scalar and pressure equations are the proposed completion, both fields are smooth and flat at x0, and c, omega are in its full allowed range. This is local non-completability of the specified family only.

To make the dependence explicit, the C61 argument uses E=|V|^2, H=-S and nonpositive trace to obtain |grad E|<=lambda|grad log H|E with lambda=2a/b0<1. A positive semidefinite tensor center-flux argument for V tensor V+P I gives a sequence E/H<3 approaching the common flat point. A projected logarithmic-gradient flow transports that sequence to a fixed transverse circle while a logarithmic combination tends to minus infinity. Compact continuation and positivity on that circle give the contradiction. The full proof, including its center flux and every continuation alternative, is the previously confirmed dependency; no pressure normalization or maximum principle is added here.

## 6. Applications, comparison scope and remaining questions

For C69, f=exp(-t log t), t=log(1/r), has r f'/f=log t+1. It meets (1) and derivative flatness on a sufficiently small disc. For the C71 factor f=exp(-G(t)), G'=Lambda(t)->infinity, one has r f'/f=Lambda(t), so (1) again holds after shrinking. Its explicit smooth-minorant construction supplies derivative flatness. The pressure sign therefore applies to both the logarithmic and arbitrarily slow families, at every finite omega.

All six LIT305 source sections were read. Their first-derivative estimates, block trace, coordinate correction and transport factor agree with the independent calculation above. The complete C61 dependency was reread at its exact hypotheses. The complete ten-item coordinator comparison was read and checked. It agrees on the Volterra bounds, exact carrier identities, squared-trace cancellation, moving-chart correction, error absorption, transport, every C61 premise and both applications. The actual provider execution is independently unattested.

The result closes neither the general common-flat problem nor the unrestricted smooth decaying rotating Euler conjecture. It does not prove a universal sign for other carriers. It also does not justify claiming that earlier A2485 OPEN had already proved non-completability: that earlier inference remains invalid, whereas the present argument supplies a distinct pressure-based obstruction for this particular family. No computation, new client, server or formal build is used.
