# Acceptance of the final T2 summary

## Exact claim and scope

The final summary at SHA25613cd15cdadfcc1ac07e94dd08157d5740f66e8ee98ab54ecc658fdcfb6722a0f differs from the accepted T4-499 summary in exactly four line blocks. Its new review row and erratum correctly record the residual identity, angular factor n, exact examples, local integrability qualification and review provenance. This statement accepts those additions. The earlier summary and its hypotheses remain those accepted in T4-499. No candidate existence theorem, complete017 upper norm or correction-distance ranking is added.

## Analytic statement inherited and checked

For odd integer n>=1, let F_n=f(r)sin(n theta) be real and locally integrable on the plane, and Q=||rF_n||_2^2<infinity. Let psi=u(r)sin(n theta), where u is a finite real sum of r^3(1+r^2)^(-beta)(r^2/(1+r^2))^k, beta>3/2, integer k>=-1, and 3+2k-n is even and nonnegative. For y=log r define

 d=pi int(u_y^2+n^2u^2)dy,
 a=pi int(u_y^2+u_yy^2/n^2)dy,
 p=pi int f u r dr,
 b=(pi/n^2)int f u_yy r dr.

At zero psi is smooth because each r^(3+2k)sin(n theta) is a harmonic polynomial times a nonnegative even radial power. At infinity u,u_y,u_yy are O(r^(3-2beta_min)); the strict beta condition makes all energies finite and u u_y vanish. Integrating u u_yy by parts and expanding the square gives

 ||rDelta psi||_2^2=n^2(a+d),
 int r^2F_n Delta psi=n^2(b-p),
 R^2:=||r(F_n+Delta psi)||_2^2=Q+2n^2(b-p)+n^2(a+d).

Thus Cauchy-Schwarz bounds the cross pairing by n sqrt(Q(a+d)). The omitted-n predecessor was false. A smooth radial cutoff approximates grad psi in L2 with error square O(R^(6-4beta_min)). Therefore, for H(G)=sup{|<G,phi>|:phi real C_c^infinity,||grad phi||_2<=1}, H(Delta psi)=sqrt(d). The tangential field -r g(r)cos(n theta)e_theta/n has divergence g(r)sin(n theta), no radial origin flux and L2 norm ||rG||_2/n. Local integrability supplies the distributional origin passage. Triangle inequalities and the normalized test psi give, for d>0,

 max(0,sqrt(d)-R/n,|p|/sqrt(d))<=H(F_n)<=sqrt(d)+R/n.

The beta condition is sufficient. The summary's beta=3/2 divergence example is the particular single trial n=1,k=0 in its linked review. It is not a necessity claim for every finite sum, since leading powers can cancel. The independently accepted proof T4-501 makes this scope explicit.

## Exact finite example verification

All quantities in this paragraph are divided by pi. The accepted T4-501 source integrations give the following exact inputs (n;d,p,a,b,Q):

 (1;3/8,2/35,3/8,-46/1155,1/60),
 (1;4/15,-1/36,12/35,1/60,1/135),
 (3;6/35,1/120,2/63,-1/840,1/210).

Substitution in the identity gives respectively R^2/pi=63/110,667/945,349/210. For the Riesz example F=-Delta(r(1+r^2)^-2 sin theta), with u=r(1+r^2)^(-3/2), the accepted exact quantities are d=3/8,p=32/105,a=3/8,b=-1632/5005,Q=64/105. They give R^2/pi=1959/20020. Here H(F)^2/pi=4/15 and H(F+Delta psi)^2/pi=9/280. The latter is below R^2/pi, and p^2<=d(4/15). To verify the two triangle inequalities without approximate radicals, set h=4/15. Since d+h-R^2>0, (d+h-R^2)^2<=4dh proves (sqrt(d)-sqrt(h))^2<=R^2, which implies both desired inequalities.

For the missing-n fixture n=3,u=r^3(1+r^2)^-3,F_n=Delta psi, the accepted exact d=6/35,a=2/63,Q=64/35 and cross=64/35 give sqrt(Q(a+d))=64/105. Multiplication by n restores equality. These are rational recompositions of previously accepted exact integrals, not repeated numerical integrations.

## Source and verdict boundaries

The current T2 review is exactly the revision accepted in T4-503; its historical18:07text is exactly the source preserved in T4-501. T4-503 inspected all2174 exact generators and positive radial denominators to discharge the017 origin condition. The final summary accurately says T2 itself did not inspect those source generators. Its review row reports analytic examples, not new017 numerical bounds. The accepted partial017 H lower and its two residual modes remain T4-495; complete017 H upper,E2 and its comparison with007 remain OPEN. All four changed blocks are inspected by diff, including the acknowledgement of499 and preservation of the corrected review's predecessor.

Dependencies are standalone PROOF.md files in ../t2_summary_repair_acceptance (499), ../candidate017_residual_review_acceptance (501), and ../candidate017_review_repair_acceptance (503). Exact frozen inputs and their source hashes are in source/ and data/. Verification checks hashes, changes, review identities, inherited result counts and the rational examples above. It executes no peer program and reconstructs no candidate integral. Hash equality alone is not mathematical proof; the accepted predecessor arguments supply that premise.
