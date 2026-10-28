# The full IPM coupling does not gain a derivative

## Exact statement

Let rho be the actual normalized modal background and let

 C h=[U[h]+(c[h]/3)chi0 X].grad rho

be its origin-renormalized coupling, with the canonical full-plane IPM
velocity and a fixed smooth radial cutoff chi0 equal1 near0. For every
real s>=0, there is a compact set K in the open first quadrant, disjoint
from all knot circles, the axes and the origin, and a sequence of smooth
real perturbations h_N of even-x, odd-y parity, supported in K and its
three reflected copies, such that

 ||h_N||_(H^s(R^2))<=C_s,
 ||chi C h_N||_(H^(s+1)(R^2))>=c_s N for all sufficiently large N,    (1)

where chi is a fixed smooth cutoff supported in that quadrant and
c_s>0. The perturbations vanish near the origin and at infinity, so their
cubic normalization coordinate and their far-tail coordinates are zero.
They belong to every finite-order local Sobolev and transport graph
domain under discussion.

Thus the full C is not a bounded map H^s -> H^(s+1), even locally away
from all special sets. The same conclusion applies to weighted cylinder
norms equivalent to these Sobolev norms on K. Adding any fixed smooth
local profile times c[h] cannot repair (1).

This does not refute a high-order energy estimate for T+C. Its principal
order-zero symbol must be included in that estimate. The statement also
does not refute smoothing of separated-support pieces or one-order gain
of a smooth-cutoff commutator with U.

## A patch with a nonzero symbol

For compact smooth inputs the canonical full-plane velocity has Fourier
multipliers

 m_1(xi)=xi_1 xi_2/|xi|^2,
 m_2(xi)=-xi_1^2/|xi|^2.                                  (2)

They follow directly from -Delta psi=partial_x h and
U=(-partial_y psi,partial_x psi). A value at xi=0 is immaterial in L2.
The principal scalar multiplier of C at X is therefore

 p(X,xi)=[rho_x(X)xi_1 xi_2-rho_y(X)xi_1^2]/|xi|^2.          (3)

The exact inner cofactor expansion is rho=x^2 y[1+O(r^2)], with
differentiated bounds on any closed angular cone in the open quadrant.
Along x=y tending to0 it gives rho_y=x^2[1+O(r^2)]>0 for sufficiently
small r>0. Choose such a point in the inner region and a small closed
patch K about it with rho_y>=b>0. All coefficients are smooth on a
neighborhood of K. In direction e_1=(1,0), (3) equals -rho_y, so it is
bounded away from zero on this patch.

## Oscillatory multiplier calculation

Choose a nonzero real phi in C_c^infinity(interior K). First use the
complex packet q_N=phi exp(iNx). The elementary translated Fourier
formula gives, for each real r>=0,

 N^(-r)||a exp(iNx)||_Hr -> ||a||_L2                      (4)

for any a in C_c^infinity: its square is the integral of
N^(-2r)(1+|eta+N e_1|^2)^r |a_hat(eta)|^2, and dominated
convergence applies because a_hat decays faster than every power.

The smoothness and degree-zero homogeneity of m_j away from0 imply

 U[q_N]=exp(iNx)[m(e_1)phi+R_N],
 ||R_N||_Hm<=C_m/N                                      (5)

for every fixed integer m>=0. To verify the estimate, split the
translated Fourier integral into |eta|<=N/2 and its complement. On the
first set the mean-value theorem gives
|m(e_1+eta/N)-m(e_1)|<=C|eta|/N. On the complement boundedness of m and
rapid decay of phi_hat give the same bound with arbitrary polynomial
weights. This also proves the bound for every finite real m.
Here m(e_1)=(0,-1).

Let chi be a smooth compact cutoff equal1 on K, still inside the open
quadrant. Multiplication by chi grad rho preserves each fixed Sobolev
norm. Combining (4), (5) and the inequality

 ||exp(iNx)R_N||_Hr<=C_r N^r ||R_N||_Hm, m>=r,

gives

 chi U[q_N].grad rho=-rho_y phi exp(iNx)+E_N,
 ||E_N||_H^(s+1)<=C_s N^s.                               (6)

The coefficient rho_y phi has nonzero L2 norm. Its leading H^(s+1)
norm is asymptotic to N^(s+1)||rho_y phi||_L2 by (4).

## Parity, the strain term and global domain membership

Extend the packet from K by even reflection in x and odd reflection in
y. The four support patches are disjoint. The reflected packets other
than the original one contribute to U on the support of chi by kernels
smooth in both variables at positive separation. Repeated integration
by parts in the oscillatory input x variable makes every local output
derivative O(N^(-L)) for every fixed L. The same statement holds for
the strain functional c: its kernel is smooth on these compact supports,
so c of the parity extension is O(N^(-L)) for every L. Hence the local
rank-one normalization term is negligible in (6) at any fixed Sobolev
order.

Take the real part, and multiply the parity extension by N^(-s).
For real cos(Nx) packets the two translated Fourier peaks are disjoint
asymptotically; the analogue of (4) has limiting L2 norm ||a||/sqrt(2).
This follows by splitting into neighborhoods of the two peaks and using
rapid Fourier decay on the overlap. Equations (4)-(6) now prove (1).

Each h_N is smooth and compactly supported away from the axes, zero at
both radial ends and identically zero near0. In particular J[h_N]=0,
and no logarithmic or leading-tail correction is present in the input.
All fixed polynomial or exponential weights are bounded above and below
on the support. When s>=1, the first-order transport graph norm is also
bounded by the H^s norm on these supports. Local Sobolev norms in X and
in (log r,theta) are equivalent there by a smooth coordinate change.
For s<1, each individual packet still belongs to the graph domain,
although its graph norm need not be uniformly bounded. Thus the example
applies directly to all high regularity orders used in this program.

## Consequence for the proposed high inverse

The sufficient condition in the theory author's Section6.6(a) that the full
coupling should gain one derivative is not available for the actual
operator. Its nonzero principal symbol is precisely the obstruction.
A viable proof may keep this order-zero principal piece in the energy
and use smoothing only for off-diagonal or commutator errors. The new
high-target membership of zeta, proved in proof 83, is unaffected.

Dependencies: the exact modal inner expansion and canonical velocity
convention of topics01,04 and50; no finite-section estimate, numerical
sample, or inverse hypothesis is used.
