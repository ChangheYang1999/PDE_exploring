## Note 36 (2026-10-28T11:19Z): cross-read of the middle-arc balanced residual (V163): no error found

To the verification work. I read 08_improved_upper_bounds/middle_circle_transport/balanced_residual/PROOF.md
(sha256 e00bc7fb02978cb18fd32688e8fb21bfba2515eb05e1abf135e6ca9ca918fb94) against the parent ../PROOF.md. Every step checks:

1. Geometry. |z|=r=sin t meets |z-1/2|=1/2 at Re z=r^2, i.e. z_R=r^2+i r cos t=r e^{i(pi/2-t)}, and z_L=-conj(z_R). The upper arc has
   angular width 2t<=pi, so its diameter is its chord 2r sin t=2 sin^2 t; antipodal distance 2r.
2. Normalization. In the parent, m_j, T_j and R are per unit t (cell masses at every t of the bin, extraction by proportional
   scaling pointwise in t), so at fixed t the residual on the upper arc has variation V<=tau=R and signed mass
   int_{-1}^1 w_phi ds - S with S=sum_j m_j. The integral of w_phi in s equals r cos t Re[e^{i phi} int_{pi/2-t}^{pi/2+t} G(r e^{i theta}) dtheta].
3. Cost. Product sub-couplings of the balanced parts (mass (V-|q|)/2 each sign on each arc) cost (V-|q|)(2 sin^2 t)^alpha in total; the
   one-signed remainders (mass |q| each) are paired antipodally, |q|(2 sin t)^alpha. Rearranged: V A_t+|q|(B_t-A_t) with A_t<=B_t since
   sin^2 t<=sin t. Both A_t, B_t increase on [0,pi/2], coefficients V-|q|>=0, |q|>=0, so the bin bound (2) holds with A=A_b, B=B_b, and
   |q|<=V<=tau gives min(tau,Q). (2) <= (b-a) tau B.
4. Primitive. F'(z)=(2z^2+1/2)/(z^2-1/4)^2-2(z^2-1/4)/(z^2-1/4)^2=1/(z^2-1/4)^2. w=(1+2z)/(1-2z) maps the upper half-plane to itself
   (i to i, real line to real line), so the principal-log branch of atanh(2z) is analytic there, and the arc lies in the open upper
   half-plane. F(-conj z)=-conj F(z) follows from 2(-zbar)/(zbar^2-1/4) and log(1/conj w)=-conj(log w). dtheta=dz/(iz) gives
   int G dtheta=[F(z_L)-F(z_R)]/(i pi)=2i Re F(z_R)/pi, and Re(i e^{i phi})=-sin phi.
5. Real arithmetic, with s=r^2: |z_R^2-1/4|^2=(2s^2-s-1/4)^2+4s^3(1-s)=s/2+1/16; Re[z_R conj(z_R^2-1/4)]=s^2-s/4, so
   Re[-2z_R/(z_R^2-1/4)]=8s(1-4s)/(1+8s); |1+2z_R|^2=1+8s, |1-2z_R|^2=1, so Re 4atanh(2z_R)=log(1+8s).
6. Independent 30-digit quadrature (scratch/xread_v163.py) at t=0.1,0.7,1.3,1.55 and phi=0,0.4,pi/2,2.5: the formula for M_phi agrees
   to below 1e-31 in all 16 cases.

Verdict from my side: the analytic statement and proof are correct as written. The numerical replay and its acceptance
remain yours. Remark: since the same coupling is valid at every t, Q may also be replaced by an endpoint or convexity bound on each of
several subintervals of a bin, as in the radial residual of Theorem 3.7; whether this matters depends on how large tau is in the
middle-circle certificates. If the replay lowers D upper bounds, I will integrate them into Theorem 3.6 and Table 1.

Also: V165 (v24 confirmed) and V164 (D_1/2 >= 2.4531232777) are noted; V164 goes into v25 with the a30v7 (and a10v7) results once
those are accepted. a10v7 is still running (p2 of 4 pieces at 11:17Z); its result will be Note 37.

## Note 35 (2026-10-28T11:12Z): report v24 (V160 repairs, V161 values), please audit the diff
