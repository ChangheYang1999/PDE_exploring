# The five-variable center determinant and its factor of two

Independent verification, 2026-10-21 UTC. This argument precedes the
associated exact polynomial check. It supplements the complete disc
construction in the parent PROOF.md; it makes no assertion about global
transport.

Fix c>1, D=c-1, a real, H>0, z=r^2, and
Y=(f,g,T,J,K), Y0=(a,0,a/4-D,a/4,0). Near the origin put k=L=0,
S=Hz, u=(T-J)/2, B=-u-K+S. The first and third transport projections
are equivalent to

    z(f',g')^t = -(1/2) M(Y,z)^-1 (F1,F3)^t,
    zT'=-g/2, zJ'=(f-4J)/2, zK'=(g-6K)/2,
    M=[[c+u,B],[B,c]],
    F1=(D+T)f-f^2/4+fg/2+(-J+2K+4S-2T)g,
    F3=(J+2S)f-f^2/4-fg/2+Dg.

These formulas follow from the independently derived angular equations
in the parent proof. They define zY'=Phi(z,Y). Write h=c^2+4c-1>0.
At (0,Y0), F1=F3=0 and

    M0=[[(c+1)/2,D/2],[D/2,c]], det M0=h/4.

The derivative of the inverse matrix contributes zero to D_Y Phi at
this point because it multiplies (F1,F3)=0. Direct differentiation gives

    L0=D_Y(F1,F3)
      =[[-a/4,2D-a/4,a,0,0],
        [-a/4,D-a/2,0,a,0]].

Let A=D_Y Phi(0,Y0). Its first two rows are
-(1/2) M0^-1 L0 and its last three rows are

    [0,-1/2,0,0,0],
    [1/2,0,0,-2,0],
    [0,1/2,0,0,-3].

We claim, as an identity in j,

    det(j I-A)=j(j+2)(j+3) I_c(a,2j)/(16h),             (1)
    I_c(a,lambda)=a^2-4[(c+2)lambda-D]a
                  +4h lambda^2-8D(c-3)lambda.

For j not equal to 0,-2,-3, multiply the first two rows of jI-A by
2M0. The determinant is thereby multiplied by det(2M0)=h. Eliminating
the three scalar rows gives T=-g/(2j), J=f/(2j+4),
K=g/(2j+6), times the respective scalar pivot product j(j+2)(j+3).
With lambda=2j the remaining two by two matrix is

    C(lambda)=[
      [(c+1)lambda/2-a/4,
       Dlambda/2+2D-a/4-a/lambda],
      [Dlambda/2-a/4+a/(lambda+4),
       c lambda+D-a/2]].

The off-diagonal entries factor as

    C12=(lambda+4)[D/2-a/(4lambda)],
    C21=lambda[D/2-a/(4(lambda+4))].

Their product is
D^2 lambda(lambda+4)/4-Da(lambda+2)/4+a^2/16.
Subtracting this from the diagonal product gives
16 det C(lambda)=I_c(a,lambda). This proves (1) away from the three
excluded j. Both sides of (1) are polynomials in j, so the identity
extends to every j. In particular the scalar pivots introduce no
positive-integer resonance.

This calculation also fixes the wording: the first two rows are
multiplied by **2M0**, not M0, when passing from the z-derivative
equations to the dot equations. The verifier's earlier result116
confirmed the correct two by two coefficient matrix but failed to flag
that erroneous factor in the prose. The literal earlier wording is
REFUTED; the matrix, its determinant, the nonresonance condition and
the analytic construction are unchanged.

For completeness, dilation by l preserves slope and center strain
while sending H to H/l^2 and the quintic residual coefficient C5 to
C5/l^4. Taylor expansion of the smooth local pair gives
rho_l=ay+O(l^-2 r^3) and psi_l=-Dxy+O(l^-2 r^4) on each fixed compact
set. Thus q_l tends to one, including its smooth extension to y=0.
The affine limiting density violates the primary sublinear growth
bound and its limiting strain velocity is not sublinear. This
dilation does not produce an admissible exact profile or decide the
all-radius projected problem.
