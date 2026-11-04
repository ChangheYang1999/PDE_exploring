# Excluding a fixed component with a flat vorticity boundary

## 1. Exact local theorem

Fix 0<c<1/2 and any finite real omega. Write Jx=e3 cross x, X=(cI-omega J)x, a=1-2c, b=2-2c, q=b/a>2. On an open G in R3 minus{0}, suppose smooth V,P satisfy

    div V=0, W=curl V, k=X.V, S=P-|V|²/2,
    X.grad V=-(1-c)V-omega JV, X.grad P=-bP,
    -Delta P=tr((DV)²),
    k grad S=qS grad k wherever W!=0.

Let C be one connected component of {W!=0,k!=0}. There is no x0 in its relative closure with V(x0)=0 such that every derivative of W vanishes at every point of boundary_G C in some neighbourhood of x0. A sufficient condition for that boundary premise is boundary_G C locally contained in closure_G(int_G{W=0}). No condition on boundary thickness, number of components, or approach angle is assumed. The field need not have zero helicity, and W.grad S=0 is not used.

## 2. The fixed power law and boundary algebra

On C the rank relation implies S=D|k|^q for one finite real D. This follows by differentiating S|k|^(-q); the expression has zero gradient on a connected open set, and k has one sign there. At a boundary point z where all W jets vanish, homogeneity and vector calculus give

    grad k=X cross W-aV, Delta V=-curl W,
    Delta k=X.Delta V-2omega W3.

Thus M=DV(z) is symmetric and trace free, Delta V(z)=Delta k(z)=0, and

    MX=-LV, L=(1-c)I+omega J,
    Delta S(z)=-2|M|_F².

The power law has twice differentiated form on C

    grad S=qD|k|^(q-2)k grad k,
    Delta S=q(q-1)D|k|^(q-2)|grad k|²
                   +qD|k|^(q-2)k Delta k.             (1)

Because q>2, these expressions have continuous limits as k tends to zero. They do not require high derivatives of the fractional power at zero. If k(z)=0, (1) and the preceding identity force M=0 and then V(z)=0 since L is invertible. Conversely V(z)=0 implies k(z)=0.

If V(z)!=0, then k(z)!=0, M!=0, grad k=-aV, and q(q-1)a²=b. Hence

    bD|k|^(q-2)|V|²=-2|M|_F².                        (2)

In particular D<0. For a symmetric trace-free matrix M and unit e, minimizing the remaining two-by-two block after fixing Me gives

    |M|_F²>=2|Me|²-(e.Me)²/2>=3|Me|²/2.

Use e=X/|X|, MX=-LV, |LV|²>=(1-c)²|V|² and |k|<=|X||V| in (2). The resulting necessary bound is

    |D||V(z)|^(q-2)>=3(1-c)/(2|X(z)|^q).             (3)

It applies to this fixed D and these boundary points only.

## 3. Every jet vanishes at a zero boundary value

Suppose V(z)=0 at such a boundary point. Short X-flow segments preserve C: the factors for V,W,k are respectively exp(-(1-c)t)Q_t, exp(-t)Q_t and exp(-at), with Q_t=exp(-omega tJ). Project a sequence from C tending to z along this flow onto the affine plane through z perpendicular to X(z). This gives z+h_j in C with h_j perpendicular to X(z), h_j nonzero and tending to zero. A point projecting exactly to z would lie on its zero-velocity orbit and could not belong to C.

If V has a first nonzero homogeneous Taylor term V_n of degree n>=1, the vanishing W jets and divergence give curl V_n=div V_n=0. The lowest degree of homogeneity gives X(z).grad V_n=0. In coordinates with third axis X(z), the third component is constant by curl freedom and hence zero. The planar field is the gradient of a nonzero harmonic homogeneous polynomial of degree n+1. Writing that polynomial as Re(B(x1+i x2)^(n+1)) shows

    |DV_n(h)|_F²=C_n |h|^(2n-2), C_n>0

on the transverse plane, uniformly in direction. Since Delta V and W are flat at z, the pressure equation implies

    Delta S(z+h)=-2C_n|h|^(2n-2)+O(|h|^(2n-1)).       (4)

Also grad k=-aV plus a flat field, so grad k=O(|h|^n), k=O(|h|^(n+1)) and Delta k is flat. Along h_j, (1) instead makes Delta S=O(|h_j|^(q(n+1)-2)). Its exponent is larger than 2n-2, contradicting (4). Therefore every V jet vanishes.

It follows that k and Delta S are flat and S(z)=0. If S has a first nonzero homogeneous term S_l, scalar homogeneity makes it independent of the third coordinate and Delta S makes it harmonic. Its planar gradient has norm c_l|h|^(l-1), with c_l>0. But grad S in (1) is flat along the same sequence, a contradiction. Thus S and P=S+|V|²/2 also have every jet zero. This argument uses no cone inside C and no uniform Taylor constants across boundary points.

## 4. A full neighbourhood of zero boundary jets

If the configuration of Section1 existed, first bound |X|<=K on a relatively compact neighbourhood of x0. Continuity of V and V(x0)=0 allow a smaller ball B centred at x0 on which

    |D|sup_B|V|^(q-2)<3(1-c)/(2K^q),
    |D|K^q sup_B|V|^(q-2)<=1/4.                     (5)

These conditions are immediate for D=0. At every boundary point of C in B, a nonzero V would contradict (3). Thus V is zero on that whole boundary portion, and Section3 makes every derivative of V and P zero there. The point x0 itself belongs to the boundary, because k=0 there prevents membership in C.

## 5. Smooth extension from the one component

Define v=1_C V and p=1_C P on B. These are smooth despite the arbitrary boundary. Indeed each candidate derivative 1_C D^beta V is continuous because its inside value vanishes at the boundary. At a boundary point z, both D^beta V(z) and its first derivatives vanish, so Taylor's formula gives D^beta V(z+h)=o(|h|). Replacing this by zero outside C preserves the estimate. Induction proves differentiability to every order and identifies the derivatives with the indicated extensions. The same proof applies to P.

On the full ball,

    div v=0, -Delta p=tr((Dv)²), p>=|v|²/4.           (6)

The differential equations hold inside and outside C and at its boundary, where all jets vanish. The inequality follows from |S|<=|D|K^q|V|^q<=|V|²/4 in (5). There is no surface distribution. Both fields are infinitely flat at x0. Yet v is nonzero in every ball about x0, since those balls meet C and k!=0 on C.

## 6. Pressure doubling on a full ball

Let T=v tensor v+pI. Equation(6) gives partial_i partial_j T_ij=0: divergence freedom makes the double divergence of v tensor v equal tr((Dv)²). Twice integrate against (r²-|x-x0|²)/2 on B_r(x0). The test vanishes on the sphere, has gradient -rn there, and Hessian -I. The exact identity is

    integral_Br(|v|²+3p)
       =r integral_boundaryBr(p+(v.n)²).            (7)

No steady momentum equation or div T=0 is required. Set h=|v|²+3p and M(r)=integral_Br h. The inequality p>=|v|²/4 implies h>=|v|² and h<=7p. Consequently M(r)>=(r/7)M'(r), so M(R)<= (R/r)^7 M(r) for 0<r<R. This follows directly by differentiating r^(-7)M(r), without dividing by M.

Flatness gives M(r)<=C_N r^(N+3) for every N. Choose N>4 and let r decrease to zero. Then M(R)=0, hence v=0 on B_R, contradicting Section5. This proves the theorem.

## 7. Verdict and sharp scope of the conclusion

LIT245 is confirmed at Section1's full boundary-jet hypothesis. Its entire eight-section source and this entire independent argument were read. In contrapositive form, a fixed component approaching a velocity zero must have, in every neighbourhood of that zero, some boundary point with some nonzero finite W derivative. That point cannot lie in the closure of an open irrotational set. The derivative order need not be uniform.

The theorem does not exclude boundaries with finite nonzero vorticity jets, a sequence of distinct components with unbounded D, or a pair lacking the full smooth pressure equation in a neighbourhood. Only W=0 on the boundary is insufficient for this proof. The general conjecture is open. All omega are retained. No computation or formal build was needed; configured model comparison is through existing working files, with provider runtime unattested.
