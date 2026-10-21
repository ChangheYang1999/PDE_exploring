# Every axis trace is smooth, while the packet is not jointly C1

2026-10-21T00:36:58.320500+00:00. CONFIRMED, AV156.

For the explicit noncompact packet ofAV152, every ordinary derivative G_j(s)=partial_y^j V(s,0) exists for every fixed s and defines a smooth function on the whole real line. All even traces vanish, and all G_j(0)=0. The same function is not C1 on any neighborhood of its origin byAV154.

The proof inserts exp(-epsilon t r^2) to justify absolute Fubini for higher odd derivatives, then removes the damping using uniform integration by parts away from s=0. The transformed amplitudes have every tail coefficient zero by the exact Gaussian moment identity with index m+n. Both low-frequency and high-frequency dominations justify all derivatives of the axis trace. At s=0, the fixed-s slice is identically zero.

Own symbolic checks pass81moment identities,9odd signs/Jacobians,9even traces,8exact damped radial integrals and81integrability exponents. These finite checks supplement the general proof. Actual ClaudeOpus5.5 review completed 2026-10-21T00:35:19.066100+00:00 with end_turn and confirmed the scoped result; all advice was independently verified.

This concerns one-variable traces of an explicit frozen-source packet. It does not prove jointly smooth mixed derivatives, vanishing coupled-profile B_j coefficients, a canonical nonlinear profile or either task endpoint. Pins and review resolution are in verification/acceptance.json.
