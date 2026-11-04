# Classification of first-order formal local Lyapunov functions

## Exact statement

Let 0<c<1/2, omega be finite, and V be a connected open subset of R3. Let Psi be C1 on V x R3 x sl(3) x R, with arguments (y,u,M,p). Set b=(cI-omega J)y+u. A formal second jet consists of g in R3, T_ijk=T_ikj with sum_i T_iik=0, and symmetric Pi, satisfying

    (1-c)u+Mb+omega Ju+g=0,
    (Tb)_ij=sum_k T_ijk b_k=-M-M^2-omega[J,M]-Pi.

Suppose the formal derivative

    Psi_y.b+Psi_u.Mb+Psi_p(g.b)+Psi_M:(Tb)

is nonpositive for every such jet at every point. Then Psi is independent of M. If omega=0, Psi=f(H) with f C1 and f'>=0, where H=p+|cy+u|^2/2+c(c-1)|y|^2/2. If omega!=0, Psi is constant. This confirms C15.

This is an algebraic classification on the full jet space. No assertion is made that every such jet extends to a globally decaying profile. Thus it does not exclude inequalities obtained using global constraints on actual solutions.

## Realizability of the differentiated equation

For b!=0 the map T -> Tb from the stated divergence-free symmetric-last-index tensors onto sl(3) is surjective. Orthogonal covariance reduces to b=t e1, t=|b|. For a prescribed N in sl(3), assign T_i11=N_i1/t, T_i1j=T_ij1=N_ij/t for j=2,3, then T_222=-N_12/t and T_333=-N_13/t; all remaining independent entries are zero. Directly, Tb=N and each sum_i T_iik vanishes. Thus Pi can have an arbitrary trace-free symmetric part, subject only to tr Pi=-tr M^2.

The second jet equation is indeed the spatial derivative of momentum: (1-c)M+M(cI-omega J+M)+omega JM=M+M^2+omega[J,M]. No pressure compatibility beyond symmetric Pi and this trace is omitted.

## Elimination of strain

Write M=S+A(w), where S is symmetric trace-free and A(w) is the skew matrix with axial vorticity w_i=epsilon_ijk M_kj. For fixed (y,u,M,p) with b!=0, vary Pi by an arbitrary symmetric trace-free matrix. The formal derivative is affine in this variation and bounded above, so its coefficient vanishes. Hence Psi has zero derivative in every S direction. By continuity this remains true at b=0. Thus Psi=psi(y,u,w,p).

Taking the axial part of the second jet equation gives

    b.grad w=-w-omega Jw+Sw.

Indeed A(w)w=0, the axial part of M^2 is -Sw, and that of [J,M] is Jw. Put a0=psi_u-psi_p b and k=psi_w. The coefficient of the freely variable S is

    C=sym(b tensor a0)+sym(w tensor k).

Nonpositivity for all trace-free S forces C=mu I. Each sym(v tensor z) has at most one positive and at most one negative eigenvalue. Their sum has at most two positive and at most two negative eigenvalues by the min-max principle. It cannot equal a nonzero multiple of the three-dimensional identity. Therefore C=0, or

    (b.v)(a0.v)+(w.v)(k.v)=0 for every v.

## Elimination of vorticity

When b and w are independent, the linear forms b.v and w.v are coprime. The last polynomial identity forces k=beta b and a0=-beta w, including beta=0. For fixed (y,u,p) with b!=0, continuity extends the assertion that psi_w is parallel to b across w in Rb. Thus psi is constant on every plane b.w=sigma and can be written

    psi(y,u,w,p)=Phi(y,u,p,b.w),

where Phi is C1, for example by evaluating at w=sigma b/|b|^2. Differentiating gives psi_w=Phi_sigma b and psi_u=Phi_u+Phi_sigma w. Therefore

    Phi_u-Phi_p b=-2 Phi_sigma w.

The left side depends on w only through sigma. Varying w within a fixed plane b.w=sigma forces Phi_sigma=0. So psi is independent of w wherever b!=0, and continuity extends this to b=0. Psi is independent of all of M.

## Zeroth-order conclusion

For b!=0 every first jet extends to a second jet by the construction above. At b=0 the zeroth-order formal derivative vanishes. Hence the hypothesis of the already proved zeroth-order classification applies. For completeness, varying trace-free M gives Psi_u=Psi_p b. Integrating these directions yields Psi=f(y,H_omega), where H_omega is the rotating Bernoulli value. The remaining inequality for all X=cy+u is

    f_y.(X-omega Jy)-(1-2c)f_h X.(X-omega Jy)<=0.

Completing the quadratic square forces f_h>=0 and f_y=(1-2c)omega f_h Jy. If omega=0, connectedness of V gives f=f(h). If omega!=0, the horizontal vector fields d_y1+(1-2c)omega y2 d_h and d_y2-(1-2c)omega y1 d_h annihilate f. A small rectangular composition of their flows translates h by a nonzero constant times the rectangle area. Since f is C1, it follows that f_h=0 and then f_y=0. Thus f is constant.

## Dependencies and regularity

Only finite-dimensional linear algebra, polynomial factorization and C1 differentiation are used. The proof audits in the team records Section 5.2. It invokes neither decay nor pressure normalization, a characteristic completeness theorem, or an actual-profile realization theorem. Higher finite-order versions remain open.
