# Actual candidate020: dimension and the current analytic objective span

## Statement and exact inputs

Fix c=4076476460239181/2251799813685248, gamma=1/c and delta=1-gamma.
Use the exact raw generator list C1-N1-020-legqs25p50-quot013, SHA256
bddbd3120852a815cfe850635564cb09ab52a98ec596a4cce3b72c98cf04f7cf.
The potential generators and their densities are exactly those in
../joint_scaled_rank_audit/PROOF.md: the old1922 quotient shapes and
504 functions at R in{25,50}, j in{1,2,3}, m in{9,...,15}, N in{0,...,11},
with spec(legqs,0,N,4,R). Consequently the potential span and its image
under chi -> -partial_y Delta chi both have dimension2426.

The candidate metadata, inspected launch and completed log specify the
same67 analytic weak rows:27 first-mode powers
{0,1,2,3,4,5,6,7,8,12,16,24,32,48,64,96,128,192,256,384,512,
768,1024,1536,2048,3072,4096}, and40 rows n in{3,5,...,17},
K=(n-1)/2+s with s in{0,8,32,128,512}.
For phi_(n,K)=r(1+r^2)^(-2)t^K sin(n theta), t=r^2/(1+r^2),
every probe n in{19,23,25,29,31}, K in{600,900,1200,1800,2400},
and(21,522), is outside the real span of those67 rows.

These claims concern the exact generator space and the current recorded
analytic objective. They give no conditioning, optimization lower bound,
residual upper norm or existence theorem. No independence from sampled
residuals, statistical independence or unrecorded optimization history
is claimed. N4's stronger recorded-history audit is retained as source,
but earlier launch histories are not independently replayed here.

## Dimension argument

The audited abstract theorem348 has exactly the same c and old basis.
It separates angular harmonics and fractional radial branches. At the
two distinct rational poles v=-1/624 and v=-1/2499, the new functions
have successively increasing nonzero pole orders4+N. Descending pole
order eliminates every new coefficient, leaving the independent old
basis. Its density-kernel argument uses fourth-derivative decay and
harmonic interior estimates, then branch separation to exclude a
quadratic polynomial. Thus both abstract dimensions are2426.

The present finite check compares every actual tuple(j,m,spec), in
order and as a set, against that accepted abstract list. It also verifies
that the first2174 tuples are exactly the accepted raw016 list and the
last252 are precisely the appended radius50 block. The rational c is
unchanged. Therefore the abstract theorem applies to this actual space,
regardless of which raw coefficients vanish. The checker hash-binds the
accepted proof, result, old basis and abstract list; it does not infer
rank from a numerical singular-value calculation.

## Objective span and source check

Divide any proposed linear relation by the positive radial factor
r(1+r^2)^(-2), for r>0. Its sine-n Fourier coefficient is zero for every
objective row when n>=19. The proposed probe contributes t^K>0 for
0<t<1, a contradiction. The same reasoning applies to almost-everywhere
or distributional equality, using smoothness away from the origin.
The condition2K+1>=n gives smoothness at zero by factoring out the
harmonic polynomial r^n sin(n theta). At infinity the probe is O(r^-3)
and its gradient O(r^-4). No measured pairing is inferred from this
finite-span argument.

The complete54-line optimizer wrapper,12-line launch and37-line log
are read as text. The checker compares the parsed row list, parent
filename,12 iterations, MID16,180 angular points, weight10^12, the
addition spec and final raw hash to the actual metadata. The wrapper
shows how these arguments are recorded and the zero initialization of
the new block. Textual agreement does not prove historical execution
of particular bytes. No publisher source is executed. The standalone
whole-plane theorem and actual interval certificate are separate.
