# The secondary branch with a finite nonzero axis jet

Status: CONFIRMED after independent derivation and checked Opus 5.5 review 06. Date: 2026-10-20.

## Statement

Assume the same smooth full-plane PDE, parities, canonical inverse, c_l>1 and sublinear density/gradient growth as PROMPT.md. Suppose the first nonzero Taylor coefficient of G(y)=rho(0,y) at zero is

    G(y)=a_k y^k+O(y^(k+2)),   a_k nonzero,

where k>=1 is an odd integer. The primary branch is k=1. The finite-order secondary branches have odd k>=3. Then

    c_l+c=1/k,   c=psi_xy(0),
    DW(0)=diag(2c_l-1/k,1/k).

Moreover the entire leading Taylor polynomial of rho is a_k y^k: all terms of total degree less than k vanish, and no other term has degree k. The origin is a source. The y-axis velocity v(y)=W_2(0,y) is positive for y>0, G and G' have the sign of a_k there, and

    G(y)=K y^p(1+O(y^(gamma-1))),
    p=1/c_l, K nonzero, sign K=sign a_k.

## Proof of the center and leading jet statements

The parities give W_1(0,y)=0, vanishing off-diagonal entries of DW(0), and W(-X)=-W(X). With c=psi_xy(0), U_1=-psi_y and U_2=psi_x give partial_x U_1(0)=-c and partial_y U_2(0)=c, consistently with div U=0. The density is odd under X -> -X and has only odd total Taylor degrees. The axis equation is vG'=G. Smooth symmetry gives v(y)=(c_l+c)y+O(y^3). Comparing the nonzero coefficient of y^k proves k(c_l+c)=1. Thus W has the stated linear part and, by oddness under X -> -X, a remainder O(r^3).

Let n<=k be the smallest total Taylor degree of rho with a nonzero homogeneous term P_n. Such a degree exists because of the prescribed axis jet. The degree-n part of the PDE is

    [(2c_l-1/k)x partial_x+(1/k)y partial_y]P_n=P_n.

Its permitted monomials are x^i y^j with i even, j odd and i+j=n. Since 2c_l-1/k>1>0, if i>=2 their weighted degree is at least

    2(2c_l-1/k)+1/k=4c_l-1/k>1.

Hence those coefficients vanish. If i=0, the weight is j/k, which equals 1 precisely at j=k. Therefore n=k and P_k=a_k y^k. This also proves that all preceding Taylor degrees vanish; it did not assume their absence from the axis condition alone.

## Global axis argument

Near zero v(y)>0 and G(y) has the sign of a_k for y>0. If v had a first positive zero y*, the equation G'/G=1/v on (0,y*) would preserve nonzero G and make |G| increase. Continuity would give |G(y*)|>0, whereas v(y*)G'(y*)=G(y*) forces G(y*)=0. Thus v>0 for every y>0, and G,G' retain the same sign.

From U=O(y^gamma), the difference 1/v(y)-p/y is O(y^(gamma-2)) at infinity and is integrable. Integrating the logarithmic derivative gives the claimed nonzero K and relative error. The growth assumption then implies p<=gamma. This argument is identical to the primary global axis argument once the positive center eigenvalue 1/k has been derived.

## Scaling and scope

The genuine scaling sends a_k to lambda^(1-k)a_k and K to lambda^(1-p)K. Consequently

    L_k=(K/a_k)^(1/(k-p))>0

transforms as L_{k,lambda}=lambda L_k and selects one representative on every such finite-order axis orbit. For k>=3 the coefficient a_k is not invariant; this differs from the primary coefficient a0=rho_y(0). Its sign, k and c_l are invariant.

This theorem does not exhaust the secondary branch in the prompt. A smooth axis trace may be flat at zero but not identically zero. The scalar axis equation alone allows, locally, G(y)=sign(y)exp(-1/y^2), extended by zero at y=0, and v(y)=y^3/2. This example is only an axis ODE example, not a coupled IPM profile. It has a zero axial eigenvalue at the origin and is not covered by the finite-jet theorem. Axis traces vanishing on a neighborhood and becoming nonzero past another equilibrium also require a separate coupled analysis. No existence or nonexistence claim for these cases follows here.
