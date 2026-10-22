# Source archive dependency table

Read PROOF.md for definitions and the exact scope. Prepared pending the new pin audit and completed actual review. Labels(a),(b),(c) concern the recorded mathematical route, not every file in its provenance manifest.

| Item | Label | Reason and exact source path |
|---|---|---|
|84, M_rho<0.5059 on every disc centered in the fixed bracket |(b)|Only H,Hprime,Hsecond; n8_density_hessian/code/export_density.py and check_hessian.py. Topic99 independently checks H. No moment anchor.|
|85, M_V<0.2972 |(c)|n8_velocity_hessian/code/export_moments.py imports i_left,j_right; both local engines use them.|
|86, C_V<13.91094, E<0.22953051, K1<0.3181 |(c)|n8_coefficient_closure/code/check_closure.py substitutes84 and85.|
|89, source-instance calculation of P,A,mu,g |(c) by89; separate(a) by25|source_instance/code/check_source_v2.py uses85 moment_inputs.json. The fine25 root and point intervals separately fit the stated coarse box.|
|89, ||DV-DV(P)||op<0.0147114 and cutoff sign |(c)|Uses85 via the segment bound and the positive source matrix; point data alone cannot certify the disc variation.|
|92, actual K1(3.06)<0.313753 |(c)|source_order_family/code/check_constants.py uses M_V from85 and M_rho from84.|
|94, quantitative moving-source theorem and source box |(c)|moving_source/code/check_constants.py has m=A_lower-M_V R0 and propagated derivative bounds.|
|94, radius2.1886e-8 |(c)|Requires eps2+M_V eps0/m<|mu-1|. Only the fine mu defect in that comparison is(a).|
|95, actual auxiliary inverse norm<1.2e35 |(c)|source_explicit_inverse/code/check_bounds.py uses85 moment_inputs.json for high velocity derivatives and the lower derivative bounds.|
|96, isolated dilation/norm/domain theorem |(a), conditional analytic statement|source_dilation/PROOF.md and PUBLICATION.md. It produces no actual scaled R by itself.|
|97, actual Hs inverse<1.223e11 and N500<922 |(c)|source_integrated_inverse/PROOF.md imports84/85/89/95; integrating the cutoff anew does not remove those inputs.|
|76, four-point D>6.70197e-7 and30.0229<C<30.0230 |(a)|source_jet_corrections/evidence/checks.json exact_ranges; source_jet_corrections/code/check_jets.py uses25 source_result.json.|
|102, universal CU,Csigma,Cy,CH |(a)|sobolev_source_box/code/engine_rational.py derives whole-plane Fourier constants without the archive.|
|102, coefficient0.06970585 and radius3.2318e-7 |(c)|b1=c1+(M_V/m0)c0; source m0 also uses M_V. See engine_rational.py and check_constants.py.|
|102, actual source box and K1<0.32123200 |(c)|Imports the velocity Hessian and source-disc hypotheses.|
|2/8, X3 central strain, axis velocity/strain constants and conditional axis uniqueness |(a)|canonical_inverse and axis_control use original X3, exact kernel identities and separate strain integration.|
|10, original X3 axis values at7 and10 |(a)|axis_points/code/axis_arb.py uses direct paired-kernel integration of X3; no modal archive.|
|25, fine trial root and all recorded point scalars |(a)|modal_source/code/certify_source.py constructs its own exact polynomials, analytic anchors and canonical moment propagation from modal_v2.json.|

For the report: qualify actual(c) claims as conditional on the shared I/J moment archive until156 is fully accepted. No such qualification is needed for(a) specifically on account of topic31. For(b), cite99 for the density-polynomial check while retaining all original regularity and scope conditions. A generic conditional analytic theorem stays proved even when one prospective physical application still has an open numerical input.
