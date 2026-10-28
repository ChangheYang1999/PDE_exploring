# Exact interpolation of unequal phase bounds

## Statement

Let X be a real seminormed vector space and let M_phi=cos(phi)M_0+sin(phi)M_(pi/2) be real linear functionals whose norms are finite. Suppose the norms are even and pi-periodic in phi. Let m>=1, delta=pi/(2m), and let u_j>=0 be certified upper bounds for the norms at phi_j=j delta, j=0,...,m. For u,v>=0 define

    H_delta(u,v) = u, if v<=u cos(delta);
                    v, if u<=v cos(delta);
                    sqrt(u^2+v^2-2uv cos(delta))/sin(delta), otherwise.

When both first conditions hold, u=v=0 and either choice is zero. Then

    sup_phi ||M_phi|| <= max_(0<=j<m) H_delta(u_j,u_(j+1))
                       <= sec(delta/2) max_j u_j.

Thus an operator estimate S+sec(pi/(4m))max_j u_j may be replaced by S+max_j H_delta(u_j,u_(j+1)), whenever S bounds the removed part uniformly in phase. In particular this applies to the C construction of ../paired_local_circles/PROOF.md and the D construction justified in ../../05_team_audit/phase_identity_reread/PROOF.md, with the same homogeneous Holder space, 0<alpha<1 and the same circular-principal-value operators modulo constants. It does not move any identity term into a smaller phase grid.

## Proof

Evenness and pi-periodicity reduce the supremum to[0,pi/2]. For phi=j delta+t, 0<=t<=delta,

    M_phi = sin(delta-t)/sin(delta) M_(j delta)
             + sin(t)/sin(delta) M_((j+1)delta).

Both coefficients are nonnegative. The norm is therefore at most

    g(t) = [u sin(delta-t)+v sin(t)]/sin(delta)
         = u cos(t)+(v-u cos(delta))sin(t)/sin(delta).

The function g is nonnegative on the interval and satisfies g''=-g<=0, so g' is nonincreasing. Its endpoint derivatives are (v-u cos(delta))/sin(delta) and (v cos(delta)-u)/sin(delta). If the first is nonpositive, the maximum is u. If the second is nonnegative, the maximum is v. Otherwise there is a unique interior stationary maximum, except for the trivial zero function. The amplitude of the cosine-sine combination is sqrt(u^2+v^2-2uv cos(delta))/sin(delta), giving the displayed formula.

The coefficient sum is cos(t-delta/2)/cos(delta/2)<=sec(delta/2), proving the comparison. Add the phase-uniform bound S after this argument. This preserves the order in which the local identity-bearing part and the regular functional were bounded.

## Certification rule

All input u_j are exact rational upper endpoints from already accepted certificates. The cosine, sine and square root may be enclosed by ball arithmetic. A certified endpoint derivative sign chooses the corresponding endpoint formula. If a sign cannot be decided, both the amplitude and sec(delta/2)max(u,v) are valid universal upper bounds, so their smaller certified upper endpoint is safe. Taking the maximum of the interval upper endpoints gives a rigorous result. The formula is increasing in each input because it is the maximum of positive linear combinations; adverse input endpoints therefore suffice.

The proof was written before any numerical evaluation of the proposed improvement. A separate independent cross-read and numerical acceptance are required before adding any new decimal to the verified table.
