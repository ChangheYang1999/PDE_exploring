# Local audit of the proposed diagonal linear remainder

Checked 2026-10-28T08:33:03.795934+00:00. Independent lead cross-read is still pending.

The min/max construction preserves both the fixed two-point distortion bound and the bound for pairs meeting the complement of B(x,20rho). The lower half-plane clamp is compatible with the pole cone because -h<=-1/2+r^a. This compatibility is essential: without the cone, the envelope repair need not vanish rapidly at the pole.

For the envelope, every q with |p-q|>=r gives F(q)+L_a|p-q|^a>=-1/2+r^a>=F(p). The remaining q lie in B(x,2r), so the repair is at most 8 C L_a a r^(a+3). This is integrable against the pole kernel with an O(a) integral. The repair keeps both pole values and hence the local identity contribution.

In the fixed-delta expansion, the own local integral is A(a)delta^a/a at each pole. Directly, its angular factor is (1/(4pi)) integral_0^(2pi)|sin(2theta)|^(1+a)dtheta=A(a). The local constant -1/2 has zero circular principal value.

The signed-power comparison must subtract the curved-sign limiting jump. The vertical zero displacement is O(r^3) in angular coordinates. Its weighted logarithmic integral is O(r^3), while the opposite-sign strip has weighted size O(r^6). Both are integrable against dr/r. The horizontal roots stay fixed. The additional clamps cost O(a r)+O(a r^(a+3)), also integrable.

The remaining density equals the smooth other-pole kernel inside each disk and decays as O(r^-3) outside. The displayed logarithmic majorant is locally integrable across each zero graph and the half-plane boundary. At infinity, a bounded-slope graph comparison and its two simple angular intersections give the asserted uniformly integrable angular logarithms.

The exact identity V(delta)+Delta(delta)=1/2-(2/pi)log(delta) has the stated sign. It follows by adding the annular own-kernel integral before taking the epsilon cutoff to zero. The identity contribution is +1/2 because f(x)=-1/2 and f(y)=+1/2. Normalizing by 1+2a^2 changes the 1/a leading term by O(a).

Result of this local audit: no defect found. This file is a verification note, not a replacement for the requested independent cross-read or an accepted numerical lower-error constant.
