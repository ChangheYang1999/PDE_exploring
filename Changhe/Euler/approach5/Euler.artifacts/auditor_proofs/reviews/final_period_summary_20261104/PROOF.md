# Period-bound summary and its zero-rotation case

Date: 2026-11-04T12:53:49.745526+00:00.

## 1. Exact statement and dependencies

Let c be real with c!=1/2 and omega real. Let U in C2 and P in C1 solve the divergence-free rotating Euler profile equation on an open neighborhood of a nonstationary periodic orbit Y of B=(cI-omega J)y+U. If T>0 is a period, then omega!=0 and T>=2pi/|omega|. This is the already confirmed A030, not a new theorem. No decay, global growth condition or completeness away from the orbit is needed.

## 2. Complete argument

Write a=1-2c and alpha=U.dot dy. Directly from the profile equation and DB=cI-omega J+DU, the Lie derivative satisfies L_B alpha=-a alpha+d(|U|^2/2-P). Integrating on a transported closed curve gives circulation(s)=exp(-as)circulation(0). The periodic orbit maps onto itself with the same orientation under every time shift, so its circulation is zero. This use of flow is complete on the compact orbit itself.

Since U(Y)=Y'-cY+omega JY and the integral of Y.dot Y' over a period is zero,

    I := integral_0^T |Y'|^2 = -omega integral_0^T JY.dot Y'.

Nonstationarity gives I>0, so omega cannot be zero. Subtract the mean from Y to obtain Z. Constant translations do not change the last integral. Cauchy-Schwarz, |JZ|<=|Z| and the mean-zero periodic Wirtinger inequality give

    |integral JY.dot Y'| <= ||Z||_2 ||Y'||_2 <= (T/(2pi)) I.

Division by I proves the bound. The affine profile U=(-cx,-cy,2cz) with P=(c-c^2)(x^2+y^2)/2-(c+2c^2)z^2 has B=(-omega J(x,y,0),3cz). Its circles at z=0 attain the bound, but its velocity grows linearly. It is not a counterexample in the decaying profile class.

## 3. Precise editorial finding

In the captured report8e92740b, the AppendixA row now states that nonconstant periodic B-orbits require omega!=0 before giving the period bound. Its common range 0<c<1/2 lies within c!=1/2. H0 suffices for this part because the periodic orbit itself supplies the flow used above. C's complete12:52:40Z comparison makes the same point and was checked analytically; provider execution is independently unattested.

All41 lines of the cumulative delta from the approved9836a8ea were read and independently reproduced byte for byte. Its other changes record status, prior approval and dated history. This note confirms only the period-row wording against existing A030. It does not independently approve all contents of the descendant assembly. The approved assembly remains9836a8ea, and the planned final cumulative review remains pending. The main conjecture remains OPEN.
