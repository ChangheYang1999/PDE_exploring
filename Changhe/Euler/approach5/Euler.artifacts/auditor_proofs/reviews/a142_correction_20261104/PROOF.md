# A142: repair of the mixture upper-bound inference

## 1. Exact object

The new A comparison retained as in the team records has SHA256 b13f5a146a794400d434157e39c82f7de8400f9fe2d1f4901097b1fd79021a94. Its complete difference from524dd668 has been read. Apart from the read/version history, the mathematical change is the replacement of the R4 inference rejected in A3143. The earlier comparison's other analytical claims retain their A3140/A3142 scope. No diagnostic script or numerical tolerance is certified.

## 2. Correct implication and necessary distinction

Use 0<beta<1, m=2-beta, C=m(1-beta), K_beta=beta C and h_beta=(3-beta)^(3/2)/sqrt(5-beta). The already checked inequality h_beta>C is valid. For the constructed block, the estimate

    d_j <= beta L[(1-epsilon_j)(C+delta_j)+epsilon_j h_beta]

approaches beta L C on the right when the chosen sequences epsilon_j and delta_j tend to0. This upper bound alone cannot force an arbitrary attaining field's toroidal coefficient to vanish. The revised comparison now says exactly that.

Separately, for any C1 divergence-free U with E(R)/(LR^beta)->1 and I(R)/log R->K_beta L, radial testing gives

    I(R)>=m[(1-beta)F(R)+beta T(R)]-C_0,
    F(R)/log R->beta L.

Since T>=0 and m beta>0, division by log R yields T(R)/log R->0. This is an average of the entire tangential energy over logarithmic radius. It is not a claim that the toroidal coefficient vanishes at each large radius. The repaired R4 keeps precisely this distinction. No additional theorem follows from the note's informal phrase that the statement does not hold radius by radius; a counterexample to a stronger radiuswise statement is not proved here.

## 3. Version transfer and scope

The source change2056b6a9 to6fde407a was already confirmed in A3142: its only mathematical clarification makes the block index in the increasing half-transition explicit, using the new block's parameters. The new read paragraph accurately records that revision. Thus the corrected comparison is confirmed at its analytical scope. The full-Euler conjecture, actual-profile optimality and automatic gradient control remain OPEN. The configured A agent is model according to the run; actual provider execution is independently unattested. No external model client, formal build, mathematical computation or retrieval was used.
