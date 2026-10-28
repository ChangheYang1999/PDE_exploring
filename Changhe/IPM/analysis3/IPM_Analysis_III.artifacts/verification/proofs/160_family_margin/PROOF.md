# Independent margins for two decoupled weights

## Statement being certified

Use the exact normalized modal trial and canonical velocity of topics15 and68. Let ell=1/k, k=1615536043799051/9007199254740992, and in cylinder coordinates put

 q=V.e_r/r, vtheta=V.e_theta/r, T=tan(theta)vtheta,
 b_plus=(|grad rho_bar|-partial_y rho_bar)/2.

For a>0 and Delta>=0 define, away from the radial weight join t=0,

 m_(a,Delta)=1+ell+(mu(t)/2-Delta 1_(t>0))q+a T-b_plus,
 mu(t)=-17/2 for t<0, mu(t)=-5/4 for t>0.               (1)

The one-sided values at t=0 are treated separately. A value at the single join itself has no effect on the weighted energy inequality. The candidate lower bounds are

 m_(4,3/10)>=113/100,
 m_(18/5,3/10)>=18/25.                                 (2)

They are not accepted until the complete certificate and independent coverage audit pass. These are pointwise energy-margin statements for the exact trial. They do not assert mapping properties or conformity of a new weighted space, nor an inverse estimate for a finite section.

## Independent finite-box computation

The calculation uses the original read-only NPZ through the independent Data loader in proof 15 and the independently checked Green boundary cache of proof 68. It does not import the numerics team's margin arrays. Its input hashes are saved in metadata.json. The finite radial partition is the exact rational partition of proof 68, from the inner join t_minus through t_plus+8, with every nonempty spline interval split in half and the analytic outer interval split into160 pieces. Any interval crossing zero is additionally split at zero.

For each radial interval, proof 82's independently checked Taylor enclosure supplies the full coefficient vectors P,Q,GR,GT on the whole interval. For theta/pi in [j/256,(j+1)/256], j=0,...,127, exact Arb trigonometric intervals give

 q=ell-sum_n P_n cos(2n theta),
 T=sum_n Q_n tan(theta)sin(2n theta),
 grad_r rho=sum_j GR_j sin((2j+1)theta),
 grad_theta rho=sum_j GT_j cos((2j+1)theta).

There is no division by a small cosine. The identity

 tan(theta)sin(2n theta)
 =-tan(theta)sin(2(n-1)theta)+2sin(theta)sin((2n-1)theta)

starts at zero for n=0 and is evaluated as a polynomial trigonometric recurrence. Thus it is valid at the vertical axis by continuity. Cartesian gradient components follow by the exact rotation.

Let gr,gt,gx,gy be the resulting intervals. The upper bound

 b_plus <= (sqrt(sup|gr|^2+sup|gt|^2)-inf gy)/2            (3)

is always valid. If inf gy>0, rationalizing |grad|-gy gives the additional bound

 b_plus <= sup|gx|^2 / [2(inf sqrt(gx^2+gy^2)+inf gy)],   (4)

where inf sqrt is formed from the separate minimum absolute values of gx and gy. The denominator is then strictly positive. The minimum of the two upper bounds is still an upper bound. Substitution in (1) gives a directed lower enclosure of both margins.

A box is accepted only when both lower enclosures exceed their targets in (2). Otherwise it is bisected in the larger of its angular and radial scales, with fixed deterministic tie handling. Reaching the maximum depth without both tests passing records an unresolved leaf and forbids a global certificate. All terminal leaves, their exact rational bounds, branch addresses and downward-rounded millionth lower bounds are retained in a compressed journal. Both pairs are evaluated on the same complete cover. The production result is initially marked COMPUTED_PENDING_AUDIT.

## The two infinite ends

The accepted end certificate of proof 68 supplies uniform error bounds E_P,E_T,E_grad on each end. On the inner end, after subtraction of the exact central strain,

 q=-A+Sigma sin(theta)^2+e_q,
 T=Sigma sin(theta)^2+e_T,
 |e_q|<=E_P, |e_T|<=E_T, |grad rho_bar|<=E_grad,
 A=2ell-1, Sigma=6ell-2.

Since a<=17/4 and Sigma>0, (1) has the lower bound

 1+ell+(17/4)A-(17/4-a)Sigma
                         -(17/4)E_P-a E_T-E_grad.      (5)

On the outer end t>=t_plus+8, q=ell+e_q and |T|<=E_T. Therefore

 m_(a,Delta)>=1+ell-(5/8+Delta)ell
                         -(5/8+Delta)E_P-a E_T-E_grad. (6)

The errors are taken from their exact saved upper endpoints, not decimal displays. Their source and cache hashes are rechecked. These are earlier independent original-data computations, reused as certified dependencies. Formulas(5)-(6) cover the two entire half-lines, including their finite endpoints. Parity then extends the first-quadrant finite-box calculation to the whole plane.

## Audit requirements

The separate checker must verify every source and code hash; that radial roots form a gap-free cover of [t_minus,t_plus+8]; that each root's angular leaves form a disjoint complete binary partition of [0,pi/2]; that every zero crossing is split; that all saved downward integer bounds meet the exact targets; and that no unresolved leaf remains. It must replay selected leaves from the original data at higher precision, including the minimum witnesses and the end formulas. Only after this audit may (2) be called certified.

## Accepted certificate

The independent audit completed on 2026-10-28T11:30:32.310502+00:00. It verified all 3276 radial roots and 423719 terminal leaves, including the exact zero split, complete binary angular/radial cover, source and dependency hashes, and the absence of failed leaves. It reconstructed 38 selected boxes at 640 bits from the original data, including both minimum witnesses, both spline ends, the radial weight join, and the analytic outer region. Every replay dominates its saved downward-rounded millionth. Both entire half-line formulas were independently reassembled from their exact error endpoints and exceed 1.41 for both pairs.

The smallest saved finite-region millionths are 1130089 and 1105344. Consequently the following convenient exact-decimal bounds are certified on the whole plane, apart from the immaterial origin and radial join convention:

 m_(4,3/10)>=1.13,
 m_(18/5,3/10)>=1.10534.

This also proves both original targets in (2). The margin statement is independent of any mapping or injectivity assertion. The producer used 512-bit Arb arithmetic, all 262 gradient modes and 261 velocity modes, and no floating numerics-team coefficient arrays. Source SHA-256: a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874. Journal SHA-256: 40bdf1150f714f9310ac87f8a9cfb8ebadec02bfc838f8718ef4294e9af28ece. Audit evidence is evidence/audit.json; the complete producer output is evidence/production/.

Verdict: CONFIRMED as a pointwise coefficient certificate for the exact normalized original-data modal trial.
