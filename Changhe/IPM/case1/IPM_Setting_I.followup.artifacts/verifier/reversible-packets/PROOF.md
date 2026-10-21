# Reversible transport does not bound the high source derivatives

Date: 2026-10-20. Status: independent verification of the lead's external fred42 construction. This is an exact counterexample for transport and constant divergence. It violates curl and is not an IPM profile. The actual lead model, Claude Opus 5.5, has checked the coordinate identities; this lane independently checks them and the regularity and large-derivative estimates.

## Statement and notation

For every A>1, g>0 and 0<alpha<1, there are local fields f,W near the source P=(0,0), with f odd in y, W_1 even in y and W_2 odd in y, such that W.grad f=f, div W=A+1, f is C^{3,alpha}, W is C^{2,alpha}, and both are smooth off P. Their jets are f_y(P)=g, W(P)=0, DW(P)=diag(A,1). They equal f=g y and W=(A s,y) on a fixed downstream neighborhood on the negative s axis. There is no finite polynomial bound in 1/r for D^4 f or D^5 f on any left cone, or on any horn |y|<=kappa r^beta with kappa,beta>0, where r=-s>0. The assertion is absence of a bound: derivatives are zero between the packets and need not be large at every point.

The theorem has only the reflection in y around this source. An extension using the explicit center-source pair can preserve both original reflections, but no such extension is needed for this statement. No conclusion about the fully coupled curl equation is made.

## Coordinates and equations

Choose smooth compact cutoffs phi,psi on (-1,1) with phi(sigma)=sigma and psi(t)=t^5 for absolute arguments below1/4, and psi odd. For n sufficiently large put r_n=2^{-n}, h_n=exp(-r_n^{-2}), lambda_n=r_n h_n^{4+alpha} and

    F(s,v)=sum_n lambda_n phi((s+r_n)/h_n) psi(v/h_n).

The s supports are disjoint. Put delta_n=lambda_n/h_n^2=r_n h_n^{2+alpha}. Then |F_sv|<=C delta_n. Starting at a sufficiently large n ensures J=1+F_sv>=1/2. Define y=v+F_s and u=s+F_v. For fixed s, v maps monotonically and onto y; for fixed v, s maps monotonically and onto u. The map (s,y)->(u,v) is consequently invertible, being the composition of these two invertible triangular maps. Its derivatives are

    v_s=-F_ss/J, v_y=1/J,
    u_s=J-F_vv F_ss/J, u_y=F_vv/J.

Their determinant is one. Pull back (A u,v) and define f=g v. Solving the two component equations gives

    a=[A(s+F_v)-v F_vv]/J,
    b=J v+F_ss a,       W=(a,b).

It follows that a v_s+b v_y=v and hence W.grad f=f. Area preservation gives div W=A+1. Alternatively, apply the physical differential operators D_s=partial_s-(F_ss/J)partial_v and D_y=J^{-1}partial_v to a,b; the mixed derivatives of F cancel and D_s a+D_y b=A+1. Oddness of F in v gives the stated parities.

## Uniform regularity through the accumulation point

Within packet n rescale sigma=(s+r_n)/h_n, Y=y/h_n and t=v/h_n. The implicit equation is Y=t+delta_n phi'(sigma)psi(t). For all sufficiently small delta_n the implicit inverse and every fixed number of derivatives have bounds uniform in n, since its derivative in t is bounded below by1/2. The inverse is the identity outside a fixed compact set in (sigma,Y). Its difference from the identity has each fixed derivative bounded by a constant times delta_n, by differentiating also with respect to delta_n and integrating from zero.

The perturbations f-g y and W-(A s,y) therefore have derivative bounds of order j at most

    C_j h_n delta_n h_n^{-j},
    C_j r_n delta_n h_n^{-j},

respectively. The r_n factor in the second bound is necessary: the term A s(J^{-1}-1) is larger than the coordinate displacement. On the support |s|<=r_n+h_n, the other velocity terms satisfy the same bound. These bounds apply to each whole smooth perturbation extended by zero. The implicit coordinate change is identity outside the support, so no nonsmooth boundary gluing occurs.

The C^{3,alpha} norm of the density perturbation is bounded by C delta_n h_n^{-2-alpha}=C r_n, and the C^{2,alpha} norm of the velocity perturbation by C r_n delta_n h_n^{-2-alpha}=C r_n^2. This includes the seminorm by rescaling the fixed support. Both sums converge. Completeness of these Holder spaces gives the asserted regularity at P, and uniform derivative convergence shows that every perturbation jet through order3 for f and order2 for W vanishes at P, since each separate packet vanishes in a neighborhood of P. Away from P only finitely many packets occur locally, so the fields are smooth there. Transport and divergence hold at P by continuity of the first derivatives.

## Fourth and fifth derivatives and curl failure

On the polynomial core near s_n=-r_n, let d_n=lambda_n/h_n^6=r_n h_n^{alpha-2}. The exact coordinate equations reduce to

    y=v+d_n v^5,    u=s+5d_n(s-s_n)v^4.

At s=s_n the inverse series v=y-d_n y^5+O(y^9) gives exactly

    f_yyyyy(s_n,0)=-120 g r_n h_n^{alpha-2}.

At v=h_n t0, with fixed0<t0<1/4, Y=t0+delta_n t0^5. The uniform implicit inverse t(Y,delta) satisfies D_Y^4 t=-120 delta Y+O(delta^2), obtained by differentiating partial_delta t at delta=0, which is -Y^5. Thus for all large n,

    |f_yyyy(s_n,h_n(t0+delta_n t0^5))|>=c g r_n h_n^{alpha-1}.

Multiplication by any fixed power r_n^P still leaves these bounds tending to infinity. Also h_n/r_n^beta tends to zero for every fixed beta>0, so both derivative sequences lie in each prescribed horn for all large n. On the axis a=A s and b_y=1. The formal fifth homogeneous weight is r^{-4/A}; its normalized fifth trace is zero between packets and unbounded along the packet centers, so even the endpoint limit need not exist for this uncoupled construction.

In this core J=1+5d_n v^4 and b=J v. At s=s_n, a=A s_n/J and b_s=f_s=0, because v is independent of s there. Since D_y=J^{-1}partial_v,

    b_s-a_y+f_s=20 A s_n d_n v^3/(1+5d_n v^4)^3.

This is nonzero for v!=0. Thus the curl equation explicitly excludes the example.

## Downstream smoothness and the contraction condition

Put all supports in0<r<r0/4. The map H:(s,y)->(u,v) is identity near the fixed section s=-r0. Its exact flow is H^{-1} diag(exp(A t),exp(t)) H. At a packet core point, T_n=A^{-1}log(r0/r_n) sends it into the fixed linear neighborhood. For nearby initial points and this fixed time the final slow coordinate is exp(T_n)v(s,y). Its kth derivative is exp(T_n)D^k v. The high derivatives of the flow therefore contain precisely the large derivatives above, even though DH and its inverse are uniformly close to identity and the first flow derivative has exponential bounds. Four differentiations of f(X)=exp(-t)f(Phi_t X) include Df(Phi_t X)D^4 Phi_t X; estimating only D Phi_t cannot remove that term.

Separately, if N_n,e_n>=0 satisfy N_n<=theta N_{n+k}+e_n, sum e_n<infinity,0<theta<1 and N_n<=C 2^{beta n}, iteration gives

    N_n<=theta^j N_{n+jk}+sum_{i=0}^{j-1}theta^i e_{n+ik}.

The first term tends to zero from this bound when theta 2^{beta k}<1. In that case summing the remaining terms gives sum N_n<=(1-theta)^{-1}sum e_n. Without the quantitative inequality finite beta alone is insufficient: N_n=theta^{-n/k},e_n=0 satisfies the recurrence with equality and is not summable. This is a limitation of this estimate, not a necessary condition on every sequence or a nonexistence theorem for the coupled equations.

Dependencies: inverse function theorem with a uniform denominator, scaling of Holder norms, convergence in Banach spaces, area preservation, and elementary differentiation. The proof precedes the independent symbolic check in code/check.py. No formalization or numerical packet sampling is needed; the extremely small widths are handled analytically.
