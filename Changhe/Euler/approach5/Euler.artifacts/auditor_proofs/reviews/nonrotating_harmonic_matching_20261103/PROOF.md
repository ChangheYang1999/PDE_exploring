# Nonrotating harmonic-sector matching obstruction

## 1. Exact theorem

Fix 1/3<c<1/2, a=1-2c and m=(1-2c)/c in(0,1). On D=R3 minus{0}, suppose V in C2(D;R3), P in C2(D), div V=0, DV(cx)=-(1-c)V and Delta P=-tr((DV)^2). Let W=curl V, k=cx.V, E=|V|^2, S=P-E/2 and F=grad k cross grad S. Assume F=0 wherever W!=0. Then there is no nonempty open ball with W=0, P=-E/2 and V not identically zero. Rotation is exactly zero. Pressure homogeneity is not an assumption; C2 tail regularity and the zero harmonic remainder on the selected germ are assumptions.

## 2. A pointwise third-jet lemma

For a harmonic homogeneous potential f of degree -m, write g=grad f, H=D2f and T=D3f. At a point x!=0,

    x.g=-mf, Hx=-(m+1)g, T_x=-(m+2)H,
    tr H=0, tr T_v=0 for every v.

Here T_v is the symmetric matrix obtained by contraction. Suppose g!=0 and R=g cross(Hg) and DR both vanish. Put lambda=(g.Hg)/|g|^2 and z=Hg-lambda g. Since g.z=0 identically, at the point R=0 gives z=0, while differentiated R=0 and differentiated orthogonality give Dz=0. Thus

    T_g+H^2=lambda H+g tensor grad lambda.

Symmetry gives grad lambda=kappa g. Homogeneity of lambda gives x.grad lambda=-(m+2)lambda. Contracting Hx with g yields mf lambda=(m+1)|g|^2, so f and lambda are nonzero. Consequently kappa|g|^2=(m+2)/(m+1)lambda^2. The trace of the previous matrix identity gives

    |H|^2=(m+2)/(m+1)lambda^2.

If x is not parallel to g, the nonzero vector v=x+(m+1)g/lambda is orthogonal to g and Hv=0. The three eigenvalues of H are then lambda,0,-lambda. Their squared sum is 2lambda^2, contradicting the last formula because m>0.

Therefore x=-(m+1)g/lambda. Contracting T with x gives T_g=((m+2)/(m+1))lambda H. Compare this with T_g=lambda H-H^2+kappa g tensor g. On g-perp each eigenvalue mu of H obeys mu^2+lambda mu/(m+1)=0. Each is zero or -lambda/(m+1). Trace zero therefore forces m+1 to equal the number of nonzero transverse eigenvalues, an integer in{0,1,2}. But 1<m+1<2. This contradiction proves the lemma. Only the displayed jets are used, so it also applies to one-sided limits satisfying these identities.

## 3. A nonzero irrotational component must contact vorticity support

Suppose a forbidden ball exists and take its component O of int{W=0}. Dilation preserves O because each dilation orbit is continuous and preserves the irrotational set. The identity grad k=-aV+cx cross W gives V=-grad k/a on O and Delta k=0. Thus V and k are smooth harmonic there. Also Q=P+E/2 is harmonic on O, since DV is symmetric and Delta(E/2)=|DV|^2=tr((DV)^2). Unique continuation makes Q=0 throughout O from the starting ball.

There exists x* in the relative boundary of O in D with V(x*)!=0. Otherwise k is zero on that entire boundary. Write k(rn)=r^(-m)psi(n) on O. The continuous angular function on its compact closure solves (Delta_S2+m(m-1))psi=0 and is zero on the boundary. Since m(m-1)<0, positive and negative extrema are impossible. This argument also covers the full sphere and needs no boundary smoothness. It would give k=V=0 on O, a contradiction.

At x*, continuity gives W=0. The point lies in supp W: if an irrotational neighborhood existed, a connected such ball meeting O would be in the same component, contrary to x* being a boundary point. This is the full boundary-of-interior argument, not an assumption that every component boundary is supported without proof.

## 4. The contradiction uses only C2 tail derivatives

F is globally C1. Its value and first derivative vanish on the open vortical set and therefore on supp W, including x*. On O set f=k. Then g=-aV, H=-aDV and T=-aD2V. These have limits at x*, with g nonzero; their symmetry, traces and homogeneous jet identities follow by continuity from O. No global third derivative of k is assumed.

Since Q=0 on O, S=-E there and F=-(2/a^2)g cross(Hg). Its differentiated formula also has the one-sided limit provided by these jets. Hence at x* the limiting R and DR vanish. Section2 forbids that. This proves the exact theorem.

## 5. Verification and scope

All six source sections and all five independent sections were read. Every tensor contraction, the nonzero-contact argument and the one-sided derivative orders were checked by hand. Harmonic regularity, harmonic unique continuation and the elementary sphere maximum principle are the analytic inputs. No computation or formal build was used.

The theorem covers all three-dimensional harmonic germs with zero Q in this nonrotating class. It says nothing of nonzero Q or rotating germs. Natural C1,alpha tail regularity does not imply its C2 premise. It is a matching obstruction for reduced tails; whole-space nonrotating sublinear profiles are already excluded by the earlier theorem. The unrestricted rotating problem remains open.
