# Quantitative persistence of the actual zero geometry under C1 perturbations

## Statement

Let V be the actual normalized modal field of proof 79. Use its exact source rectangles Qplus and Qminus and source P=(p,0). Let W:R2->R2 be globally C1, with vector parities

 W1(-x,y)=-W1(x,y), W1(x,-y)=W1(x,y),
 W2(-x,y)=W2(x,y), W2(x,-y)=-W2(x,y),

and suppose sup_X ||DW(X)||_op<=epsilon=1/100000. Set Vnew=V+W. Then:

1. Vnew has exactly three zeros: 0 and (+/-pnew,0), with (pnew,0) in Qplus.
2. Outside Qplus union Qminus and away from zero, |Vnew(X)|/|X|>=23/100000=0.00023.
3. Throughout Qplus, S(DVnew)>=18009/100000 times I. Thus its unique zero is a hyperbolic repeller and
   |Vnew(X)|>=(18009/100000)|X-(pnew,0)|.
4. The source displacement satisfies |pnew-p|<=1/1801.
5. The origin remains a hyperbolic saddle with the x-axis stable and the y-axis unstable. The quadrant orbit descriptions and qualitative compact escape assertion of proof 79 continue to hold, with p replaced by pnew.

This gives a concrete sufficient radius in global velocity C1 norm for the geometry. It does not provide the high inverse, uniform high-derivative constants, or a numerical bound converting a proposed correction norm into this C1 norm.

## Proof

The parities imply W(0)=0. The fundamental theorem of calculus on the segment from zero to X gives |W(X)|<=epsilon |X|. Proof 79 proves |V(X)|/|X|>=3/12500=0.00024 outside the two source rectangles. Subtracting epsilon proves assertion2, so all nonzero zeros remain in those rectangles.

On Qplus, the accepted source-patch estimate is S(DV)>=1801/10000 times I. Since ||S(DW)||_op<=epsilon, its perturbed lower bound is 18009/100000. Integrating the derivative on a straight segment proves strict monotonicity of Vnew on this convex rectangle. Hence it has at most one zero there.

Write the rectangle's x endpoints as qminus and qplus, as in proof 79. Their distance from every point in the certified bracket for p is at least1/2. Also |X|<10 throughout Qplus. The first component of the unperturbed field on the x-axis therefore obeys

 V1(qminus,0)<=-(1801/10000)(1/2),
 V1(qplus,0)>=(1801/10000)(1/2).

The perturbation at either endpoint is at most10 epsilon=1/10000, strictly smaller than the displayed magnitudes. By parity, Vnew2(x,0)=0. The intermediate value theorem supplies a zero (pnew,0) between the endpoints. Strict monotonicity gives uniqueness throughout Qplus, including its boundary. Reflection gives the unique zero in Qminus. Assertion2 and Vnew(0)=0 prove assertion1. The same integrated monotonicity and Cauchy-Schwarz give the lower bound in assertion3. At the axis zero the derivative is diagonal by parity and has both eigenvalues positive, proving that it is a hyperbolic repeller.

At the new source the old monotonicity estimate gives

 (1801/10000)|pnew-p| <= |V(pnew,0)|
 =|W(pnew,0)| <=10 epsilon=1/10000.

This is assertion4. At zero both DV and DW are diagonal by parity. The old eigenvalues are -A and D with A>10,D>21, and each changes by at most epsilon. Thus zero stays a saddle. The invariant axes and uniqueness of the local stable and unstable manifolds identify those manifolds as the respective axis segments.

The globally bounded derivative of V is established in proof 52; W is globally Lipschitz by hypothesis. Thus Vnew is globally Lipschitz and its flow is complete. Moreover

 div Vnew>=2 ell-2 epsilon>0,
 Vnew(X).X/|X| >=(ell-epsilon)|X|-C|X|^k,

where the second assertion uses the actual far bound U[rho]=O(r^k), k<1. Hence Vnew is strictly outward for all sufficiently large r. Each quadrant is invariant by parity and flow uniqueness. No periodic orbit exists, since positive divergence contradicts the divergence theorem on the enclosed region. The zero set, hyperbolic types, invariant axes and the outward far field now satisfy the same planar limit-set proof as proof 60: backward interior orbits have limit the source; forward interior orbits escape; scalar signs on each axis give the listed axis orbits. A bounded heteroclinic cycle is also excluded by the positive divergence theorem, while the origin's stable and unstable branches lie on the axes and the sources have no nontrivial incoming branch.

The compact escape argument of proof 60 applies unchanged: a failure of a positive directional derivative on a compact set free of equilibria would yield an invariant probability measure there by separation; its compact invariant support would contain a periodic orbit by the planar limit-set theorem, a contradiction. Thus a smooth compactly supported escape function exists for every such compact set. This argument gives no derivative bound for that function. No use of C1 control as a high-regularity estimate is made.

## Exact inputs and scope

The only numerical inputs are already independently accepted in V070 and V080: the global complement bound3/12500, the rectangle derivative lower bound1801/10000, the exact bracket and rectangle endpoints, and the origin rates. code/check.py verifies the rational endpoint and radius comparisons. No new modal enclosure or sampling grid is required. A correction family W[h] satisfying C_V||h||_H<=1/100000 would meet the geometric hypothesis, but neither a value of C_V nor a high inverse is asserted here.
