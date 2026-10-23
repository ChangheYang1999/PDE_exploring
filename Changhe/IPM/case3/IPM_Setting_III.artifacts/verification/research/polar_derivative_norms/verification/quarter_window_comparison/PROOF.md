# Quadrant versus full-annulus derivative norms

2026-10-21. Let f be even in x and odd in y and C^k on the annulus a<r<b. Define |D^k f|^2 as the binomially weighted sum of all squared Cartesian partial derivatives of total order k. Each squared derivative is even in both coordinates, regardless of the parities of the derivative itself. Reflections therefore give exactly

    integral_{a<r<b}|D^k f|^2 dX
       =4 integral_{a<r<b,x>0,y>0}|D^k f|^2 dX.

Whenever the integrals are finite, the full-annulus norm is twice the first-quadrant norm. The same is true of the transport residual, which has the same density parity. The quotient of two such norms is unchanged. This proof uses no PDE, inverse error claim, or convergence assumption.

The frozen producer eta_k.py uses angles in (0,pi/2) and angular weights pi/(2 nth), with no final factor4 in the squared integral. Its returned absolute numbers are first-quadrant window norms. To label them full-annulus window norms they must be multiplied by2. This distinction does not alter any reported ratio. The producer's finite windows and finite differences are separate from our full-plane canonical calculation, so this factor alone does not predict equality of the absolute numbers.
