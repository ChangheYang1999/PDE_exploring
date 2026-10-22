# Canonical velocity ranges on nine selected polar rectangles

Written 2026-10-21T22:42:47.565878+00:00, before this topic's code. The numerical premise application remains OPEN until the checks, actual review and later own adjudication finish.

## Exact statement

Let rho be the distinguished exactly joined and exactly normalized modal_v2 trial of topic173. Its source JSON has SHA256 57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6. Its normalization is the particular real z_star enclosed by the pinned Z record, SHA256 0985679510dfa1fbfceccddd19566d85452599c4b37ecde4c84adbd5aa5f0a2a. Let psi be its canonical full-plane stream and U=(-psi_y,psi_x). Write k=1615536043799051/9007199254740992, c_l=1/k, X=(r cos theta,r sin theta), and V=c_l X+U.

Take radial cell c in {0,4102,7808} from the exact rational log partition in research/middle_residual/evidence/partition_exact.json, SHA256 56ce08f1b8d0ee7cf2508f23de5c29fff326167332021bdfd21fb5db005612f2. If its parent span has rational endpoints a,b, first child c0 and child count N, put t_c=a+(c-c0)(b-a)/N and w_c=(b-a)/N. For each (l,q) in {(0,1),(12800,12801),(25599,25600)}, define the closed polar rectangle

D_(c,l,q)={X: t_c<=log r<=t_c+w_c, l*pi/51200<=theta<=q*pi/51200}.

Let a_0=129/20, b_0=307/100, gamma=1129/1000 and

mu(r)=gamma+(a_0+b_0-gamma)/(1+(r/6)^4).

On each rectangle set s=X.V/r^2, v2=V_2/y, v1=V_1/x, and T=-(1+c_l)+a_0(v1-s)+b_0(v2-s)+mu(r)s. At an axis v1 or v2 means the continuous quotient extension, not division by zero.

The claim to be checked is that all four functions lie in the corresponding exact dyadic target_[name]_lo/hi arrays of the accepted topic125 packets, for all points of these nine rectangles. The packet files and hashes are:

- research/flow_composition/evidence/packet_0000.npz, 6905d8c29ea38679b60838efc428578be2c854e35c2d4c08e6910527428e32fa;
- remaining two exact packet hashes are specified by the SHA-bound topic125 preparation and its accepted verdict 83020eb2da815fe56e0f2d5e5eeef8c93042978dd36dd4be3a5720b3c1ec6009.

The new check must publish a complete exact JSON of all36 target intervals, their identities and the nine rectangle endpoints. Every coefficient and radius imported from these packets is an exact binary64 dyadic. This theorem is a premise substitution in the already verified topic125 range theorem; it does not reprove its numerical range calculations by counting them.

## Canonical radial inputs

Topic173, with its mandatory review resolution and own adjudication, supplies the canonical I/J premise of topic157 at z_star. Topic157 identifies all261 modes P_n=2n psi_n/r^2 and R_n=(d psi_n/dr)/r with the saved degree12 radial models of topic93 at exactly these three cells. Its ODE proof fixes the homogeneous constants by the canonical Green moments and uses uniqueness. Its bounds on [0,h] restrict to the actual child interval because w_c<=h. The artificial part beyond w_c is not used here.

The required packet identity is entrywise equality of P_mid,P_rad,P_rem,R_mid,R_rad,R_rem,scalar with the topic93 selected_v3_cell files. Topic157 binds those same files to the canonical result. Topic173 must have an accepted157 edge with its exact path, verdict hash and timestamp. Rehashing each transitive accepted source and comparing every selected array makes the substitution concrete; a common name is insufficient. All correlations between true canonical coefficients are harmless because the topic93 and topic125 enclosures contain the whole product of their input intervals.

## Angular and scalar inputs

For n>=1 let c_n(theta)=cos(2n theta), C_n(theta)=cot(theta)sin(2n theta), S_n(theta)=tan(theta)sin(2n theta), extended continuously through their finite trigonometric sums. The exact expansions use theta0=(l+q)pi/102400 and eta=theta-theta0. Topic73 verifies all coefficient and remainder boxes at these three depth7 nodes and an exported d at least (q-l)pi/102400. The new checker must match every angular coefficient and remainder against its actual accepted73 array and verify the selected node identity. No arbitrary point of an Arb center ball is used as the mathematical center.

Topic75 verifies the scalar row at each radial cell. Its h bounds w_c; its positive radial interval contains exp(t_c) through exp(t_c+w_c); its mu box encloses the above rational function throughout that radial interval. The present check repeats the exact c_l inclusion, mu endpoint inclusion and h/ell coverage and checks every scalar against both accepted75 and the packet. The inequalities a_0+b_0>gamma>0 imply mu'(r)<0 for r>0, so endpoints suffice. Two independent directed exponential calculations recheck actual radial endpoint coverage. The scalar partition and source hashes must agree with topic173/157. The normalization changes the trial, but does not change this exact k or c_l.

## Identification of the four physical functions

The canonical stream has the finite expansion psi=sum_(n=1)^261 psi_n(r)sin(2n theta). Polar differentiation gives U_r=-psi_theta/r and U_theta=psi_r. Therefore

s=c_l-sum_n P_n c_n,
v2=s+sum_n R_n C_n,
v1=s-sum_n R_n S_n.

Indeed U_2=U_r sin theta+U_theta cos theta and U_1=U_r cos theta-U_theta sin theta. Dividing on the open quadrant gives the displayed identities. The finite trigonometric expressions provide their continuous extensions to both axes, proving the stated boundary interpretation. Substitution into T yields

T=-(1+c_l)-a_0 sum_n R_n S_n+b_0 sum_n R_n C_n+mu(r)s,

which is exactly topic125's expression, including the sign of the S term. Topic125 uses the full mu interval in each polynomial coefficient, so no derivative or polynomial approximation of mu is assumed.

For completeness, if f=p_f+e_f, X=p_X+e_X with |e_f|<=E_f, |e_X|<=E_X, then

|fX-p_f p_X|<=E_f |p_X|+(|p_f|+E_f)E_X.

Summing this over all261 modes gives the complete analytic remainder used by topic125, including the cross error. Its exact translated power-to-Bernstein method and independent iv/de Casteljau method each enclose the tensor polynomials plus these errors. The valid containment direction is each reference interval inside the corresponding reported target. This direction is corrected by the mandatory topic125 ERRATUM_FINAL and its accepted joint supplemental adjudication. The new check re-evaluates all72 saved exact containments and margins in two exact rational implementations and publishes the unchanged36 targets. The reviewed actual topic125 execution, not saved interval overlap alone, supplies the underlying reference inclusions.

Combining the canonical radial membership, angular membership and scalar membership with that accepted range theorem proves the claimed physical ranges on exactly these nine rectangles, once all stated artifact identities and accepted dependencies are checked.

## Dependencies and limits

Mandatory dependencies are topics73,75,93,125 with all its corrections,157 and173. The accepted joint correction verdict notes/completion_review/extension_6000/verdict.json, SHA256 369421343dd42825bd546ab90934d9ae43f57465554db6b2c2dd9e1945a8d22d, is required with its FINAL_ADJUDICATION. Inherited arithmetic and analytic hypotheses remain. The new audit independently checks identities, scalar geometry and exact saved containments; it does not repeat topic125's274833 modal products per engine.

This covers only the nine stated contemporary rectangles for the distinguished canonical trial. It certifies no historical flow-run array identity, angular cover of a radial cell, adaptive classification, full annular flow hypothesis, derivative forcing norm, global inverse, X3 distance, nonlinear closure or decisive endpoint. No assertion is made for every z in the interval Z.
