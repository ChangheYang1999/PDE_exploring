# Cubic normalization is not closed in the local Holder graph

## Statement

Fix 0<alpha<1 and E_2 as in proof 203. Let L_delta be either the normalized frozen operator of proof 200 or the localized variable-origin operator of proof 202, with delta small enough for proof 203 to apply. Give its maximal domain the graph norm

 ||h||_graph=||h||_(E_2)+||L_delta h||_(E_2).

On smooth parity-compatible inputs define J(h) as the coefficient of x^2y at0. There are compactly supported smooth inputs k_epsilon, all with

 J(k_epsilon)=1, c[k_epsilon]=0,
 ||k_epsilon||_graph<=C epsilon^(1-alpha) ->0.        (1)

Consequently J has no continuous or closable extension from these smooth inputs to this graph space. The smooth J=0 subspace is not closed even after imposing c=0. The local inverse of proof 203 therefore does not justify restriction to a fixed cubic normalization in this topology.

The word closable concerns J as a linear map from its smooth domain, equipped with the L_delta graph norm, into R: its graph closure contains (0,1). No claim about another stronger topology is made.

## Scaled smooth packets

Choose a smooth radial chi, equal1 near0 and supported in B1. Put

 H(Z)=Z_x^2 Z_y chi(Z),
 h_epsilon(X)=epsilon^3 H(X/epsilon)=x^2 y chi(X/epsilon).

These functions have the required parity, J=1 and support B_epsilon. Choose epsilon<delta/4 and sufficiently small to stay in the fixed coefficient neighborhood. Exact scaling gives

 ||h_epsilon||_infinity=epsilon^3||H||_infinity,
 [h_epsilon]_x=epsilon^(3-alpha)[H]_x,
 [h_epsilon]_(y,2)=epsilon^(1-alpha)[H]_(y,2).         (2)

All fixed norms of H are finite, because H/Z_x^2=Z_y chi is compact smooth. Thus ||h_epsilon||_(E_2)<=C epsilon^(1-alpha).

Write the transport as T_delta=-x A_delta partial_x+y D_delta partial_y-1. For the frozen case A_delta=A0 and D_delta=D0. For the variable case they are the C2 bounded cutoff coefficients of proof 202. Substitution X=epsilon Z gives

 T_delta h_epsilon(epsilon Z)=epsilon^3 Z_x^2 Z_y
  [(-2 A_delta(epsilon Z)+D_delta(epsilon Z)-1)chi(Z)
    -Z_x A_delta(epsilon Z)partial_(Z_x)chi(Z)
    +Z_y D_delta(epsilon Z)partial_(Z_y)chi(Z)].      (3)

The expression in square brackets is compactly supported and has a uniformly bounded C1 norm in Z as epsilon tends to0. Hence the entire rescaled expression, divided by Z_x^2, has uniformly bounded C1 norm and compact support. Its ordinary x alpha seminorm and its weighted y seminorm are uniformly bounded. The same scaling as(2) proves

 ||T_delta h_epsilon||_(E_2)<=C epsilon^(1-alpha).     (4)

The normalized coupling B_delta=L_delta-T_delta is a fixed bounded E_2 operator by proof 203. Equations(2)-(4) prove ||h_epsilon||_graph<=C epsilon^(1-alpha). In particular these smooth packets and their full images are in the actual stated maximal domain and target, rather than merely satisfying a formal scaling argument.

## Exact zero-strain correction

Choose a nonnegative nonzero smooth radial function beta supported in a fixed annulus strictly inside B_(delta/2), and set q_raw=x^2 y beta(r). It is compact smooth, J(q_raw)=0, and the exact strain formula gives

 c[q_raw]=(1/4) integral_0^infinity r beta(r)dr>0.

Indeed cos^2(theta)sin(theta)=(sin(theta)+sin(3theta))/4, so its sin(3theta) angular integral is pi/4. Define q=q_raw/c[q_raw]. Then c[q]=1 and q has finite graph norm by the same product and bounded-coupling arguments.

Homogeneity of the strain kernel gives c[h_epsilon]=epsilon^2 c[H] exactly. Therefore

 k_epsilon=h_epsilon-epsilon^2 c[H]q

has J=1 and c=0. Its graph norm is at most C epsilon^(1-alpha)+epsilon^2|c[H]| ||q||_graph, proving(1).

## Failure of closed normalization

The sequence k_epsilon converges to0 in graph norm, while J(k_epsilon)=1. Thus no continuous extension can agree with J on the smooth inputs, and the graph closure of J contains (0,1), proving nonclosability.

To see directly that the normalized kernel is not closed, fix one packet k_* with J(k_*)=1 and c[k_*]=0. The smooth functions k_*-k_epsilon satisfy J=0 and c=0 and converge in graph norm to k_*, which has J=1. This is a concrete failure of closedness of the proposed normalization subspace. It is compatible with invertibility of L_delta on E_2 itself.

Dependencies: proof 203 for boundedness of the complete normalized coupling, proof 202 for the explicitly defined maximal variable domain, and proof 201 for the canonical strain formula. All scaling, membership and correction steps are given above. No numerical claim or formal proof-assistant build is involved.
