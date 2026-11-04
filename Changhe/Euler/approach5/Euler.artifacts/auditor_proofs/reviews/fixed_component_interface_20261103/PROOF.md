# A fixed component at an irrotational interface

## 1. Statement and scope

Fix 0<c<1/2 and finite real omega. Put Jx=e3 cross x, X=(cI-omega J)x, a=1-2c, b=2-2c, q=b/a>2 and L=(1-c)I+omega J. On an open G contained in R3 minus {0}, let smooth V,P satisfy

    div V=0, W=curl V, k=X.V, S=P-|V|²/2,
    X.grad V=-LV, X.grad P=-bP,
    -Delta P=tr((DV)^2),
    k grad S=qS grad k on {W!=0}.

No scalar transport W.grad S=0 is needed. Let C be one connected component of {W!=0,k!=0}, and O=int_G{W=0}. Then S=D|k|^q on C for one finite real constant D. At any z in closure_G C intersect boundary_G O, either

    V(z)!=0, k(z)!=0, D<0, S(z)<0,
    |D||k(z)|^(q-2)=2|DV(z)|²/[b|V(z)|²]
                      >=3(1-c)/[2|X(z)|²],
    |D||V(z)|^(q-2)>=3(1-c)/[2|X(z)|^q],

or V(z)=k(z)=S(z)=0 and both V and S vanish to infinite order at z. These alternatives cover k(z)=0 as well as V(z)=0. This is an interface dichotomy under local equations, not continuation through a common-flat point.

## 2. Constants, pressure and the first dichotomy

Differentiating S/|k|^q on C makes its gradient zero. Connectedness supplies a single finite D, evaluated at any point of C. Because q>2, |t|^q is C2 also at zero, and on C

    grad S=qD|k|^(q-2)k grad k,
    Delta S=q(q-1)D|k|^(q-2)|grad k|²
                   +qD|k|^(q-2)k Delta k.

All W jets vanish at z by smoothness from the open irrotational side. Thus M=DV(z) is symmetric and trace free. The identities

    grad k=X cross W-aV,
    Delta k=X.Delta V-2omega W3, Delta V=-curl W,
    MX=-LV

give all Delta k and Delta V jets zero, and Delta S(z)=-2|M|² by Poisson.

If k(z)=0, continuity of S=D|k|^q gives S(z)=0, and the displayed Laplacian tends to zero along C. Hence M=0 and invertibility of L gives V(z)=0. Conversely V(z)=0 gives k(z)=0. If both are nonzero, grad k=-aV and q(q-1)a²=b give

    bD|k|^(q-2)|V|²=-2|M|².

Here M!=0 since MX=-LV. Thus D<0 and the exact equality in Section1 follows. For symmetric trace-free M with Me=w and |e|=1, minimizing the remaining 2 by2 block gives |M|²>=2|w|²-(w.e)²/2>=3|w|²/2. Apply e=X/|X|, w=-LV/|X| and |LV|²>=(1-c)²|V|². This proves the first lower bound; |k|<=|X||V| proves the second. This step uses no unknown uniform constant across different components.

## 3. Projecting points without a geometric thickness premise

Since X(z)!=0, choose a small flowbox with the transverse affine disk z+X(z)^perp. Integrated homogeneity gives along short flow segments

    V(exp(tA)x)=exp(-(1-c)t)exp(-omega tJ)V(x),
    W(exp(tA)x)=exp(-t)exp(-omega tJ)W(x),
    k(exp(tA)x)=exp(-at)k(x), A=cI-omega J.

The curl scaling follows by differentiating the similarity, whose spatial scale is exp(ct). A path projecting a point of C near z to the disk stays in G and keeps W and k nonzero. It therefore stays in the same component C. Since z is in its closure, there is a sequence z+h_j in C on the disk with h_j->0 and h_j!=0. This needs no cone, width estimate or regularity of the boundary.

## 4. Finite velocity order is impossible

Suppose V(z)=0 and its first nonzero homogeneous Taylor polynomial is V_n of degree n>=1. All W jets zero imply curl V_n=0; divergence gives div V_n=0. The lowest order of X.grad V=-LV gives X(z).grad V_n=0. Use an orthonormal coordinate with the third axis along X(z). The polynomial is independent of that coordinate; curl zero makes its third component constant and hence zero. It is the planar gradient of a nonzero homogeneous harmonic polynomial of degree n+1.

Write that harmonic polynomial as Re(B(x1+i x2)^(n+1)), B!=0. Its Hessian squared norm is exactly

    |DV_n(h)|²=2[n(n+1)|B|]² |h|^(2n-2)

on the disk. In particular no angular direction loses the leading coefficient. Poisson and Taylor's theorem now give

    Delta S(z+h)=-2|DV_n(h)|²+O(|h|^(2n-1)).

The term V.Delta V has arbitrarily high order because Delta V is flat. Also grad k=X cross W-aV=O(|h|^n), so integration from z gives k=O(|h|^(n+1)), and Delta k is flat. On the sequence inside the same C, the second formula of Section2 therefore gives

    Delta S(z+h_j)=O(|h_j|^(q(n+1)-2)).

For its second term choose a sufficiently high Taylor bound for Delta k. Since q(n+1)-2>2n-2, these two asymptotics contradict the strictly positive angle-independent Hessian norm. Thus V has no finite first nonzero jet and is infinitely flat at z. Only two derivatives of |k|^q were used.

## 5. Finite scalar order is also impossible

The pressure identity and flatness of V make every Delta S jet zero. Every k jet is also zero, and S(z)=0 was established in Section2. If S had a first nonzero homogeneous Taylor polynomial S_l of degree l>=1, it would be harmonic, and the lowest order of X.grad S=-bS would make it independent of the third coordinate. Thus S_l=Re(B_l(x1+i x2)^l), with B_l!=0, and

    |grad S_l(h)|=l|B_l||h|^(l-1).

On C, however, grad S=qD|k|^(q-2)k grad k is smaller than every spatial power, because k and grad k are flat and D is fixed. Evaluate on the projected sequence from Section3. The nonzero angle-independent leading gradient contradicts that decay. Therefore S is infinitely flat. This argument does not invoke the separate nonzero-scalar continuation theorem or W.grad S.

## 6. A precise accumulating-contact consequence

Suppose z_j are contacts of the type in Section1 for possibly different C_j, V(z_j)!=0, z_j->x0 in G and V(x0)=0. Then |V(z_j)|->0 while |X(z_j)| is bounded, so the lower bound forces D_(C_j)->-infinity. A fixed component or uniformly bounded family cannot have such nonzero-velocity interface contacts approaching a velocity zero.

The statement does not exclude approaching a zero through the vortical interior, where there need not be adjacent open irrotational points. It also does not exclude contacts which are already common flat zeros. Those are the remaining alternatives. The exact small local swirl has no such interface and is consistent with, rather than a counterexample to, the amplitude-normalized lower bound.

## 7. Verification

All seven submitted sections were read and independently reconstructed above. The C2 power limit, trace-of-square sign, local flow-component preservation and angularly uniform polynomial norms were checked without computation. The theorem is confirmed for all 0<c<1/2 and finite omega at precisely the stated local scope. It supplies no full momentum, canonical pressure, global decay or arbitrary-helicity conclusion. The general campaign remains open. Existing configured model agents are requested to compare the cusp scope; runtime remains unattested and no new client or formal build was used.
