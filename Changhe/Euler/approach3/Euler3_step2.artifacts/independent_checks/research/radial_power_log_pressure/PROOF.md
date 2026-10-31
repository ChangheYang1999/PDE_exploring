# Radial power and logarithmic pressure references

Status: proved exact Newton-potential formulas. These are Poisson tests, not Euler fields.

## Statement and notation

Let beta>3, r=|y| and f_beta(y)=(1+r)^(-beta) on R^3. Define

I_beta(r)=integral_0^r s^2(1+s)^(-beta) ds,
J_beta(r)=integral_r^infinity s(1+s)^(-beta) ds,
P_beta(r)=I_beta(r)/r+J_beta(r) for r>0.

Set P_beta(0)=J_beta(0). Then P_beta(|y|) belongs to C^2(R^3), tends to zero at infinity, and is the decaying full-space Newton pressure satisfying -Delta P_beta=f_beta. Its radial derivative is P_beta'(r)=-I_beta(r)/r^2. Explicitly,

I_beta(r)=[u^(3-beta)/(3-beta)-2u^(2-beta)/(2-beta)+u^(1-beta)/(1-beta)] evaluated from u=1 to u=1+r,

J_beta(r)=(1+r)^(2-beta)/(beta-2)-(1+r)^(1-beta)/(beta-1).

Also define g_beta(y)=(1+r)^(-beta) log(1+r). Its decaying Newton pressure and radial derivative are -partial_beta P_beta and -partial_beta P_beta', respectively. Both pressure identities are classical, including at the origin. The sources are continuous radial functions, not asserted to be C^infinity at the origin.

For beta=4, f_4(r)=r^(-4)+O(r^(-5)) and g_4(r)=r^(-4)log r+O(r^(-5)(1+log r)) as r tends to infinity. Thus the leading-tail subtraction code can be tested with alpha=1, zero azimuthal mode, and either constant or logarithmic leading coefficient. Alpha=1 is a manufactured Poisson test value, not a campaign parameter proposal.

## Proof

Substitution u=1+s in the integrals gives the explicit antiderivatives. The assumption beta>3 makes both integrals finite, including I_beta(infinity). Differentiation for r>0 gives P_beta'=-I_beta/r^2 because the boundary contributions I_beta'/r and J_beta' cancel. Therefore (r^2P_beta')'=-r^2f_beta, proving the radial Poisson equation. Since I_beta(r)=r^3/3+O(r^4) at zero, P_beta'=-r/3+O(r^2) and P_beta''=-1/3+O(r). The radial Cartesian Hessian consequently extends continuously as -I/3 at zero, proving C^2 regularity and the equation there. At infinity I_beta is bounded and J_beta tends to zero, hence P_beta tends to zero.

The spherical average of the Newton kernel 1/(4pi|y-z|) over the sphere |z|=s is 1/max(r,s). Splitting the radial source integral at s=r gives I_beta/r+J_beta. Alternatively the radial equation, regularity at zero and decay at infinity determine the same function: the difference is a radial harmonic function A+B/r, and regularity and decay force A=B=0. Uniqueness among all decaying C^2 solutions follows from the maximum principle on expanding balls.

Fix beta0>3 and choose epsilon>0 with beta0-epsilon>3. The source and its beta derivative are dominated for beta near beta0 by (1+r)^(-beta0+epsilon)(1+log(1+r)), integrable with the radial volume weight at infinity. The Newton integrals and the finite-radius radial derivatives can therefore be differentiated in beta. Since -partial_beta f_beta=g_beta, the formulas for the logarithmic source follow. At zero g_beta(r)=O(r), giving I_g=O(r^4), P_g'=O(r^2) and P_g''=O(r); hence the logarithmic pressure is C^2 with zero Hessian there. The tail expansions follow from (1+1/r)^(-4)=1+O(1/r) and log(1+r)=log r+O(1/r).

## Dependencies and scope

The radial Newton kernel formula, elementary integration, differentiation under an integrable majorant, and the maximum principle. No formal proof or numerical error enclosure is claimed. Finite quadrature of the source remainder must still be tested; removing the leading term does not remove that remainder.
