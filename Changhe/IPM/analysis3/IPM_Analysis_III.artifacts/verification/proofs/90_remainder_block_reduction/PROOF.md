# Elimination of the remainder block and its adjoint certificate

## Spaces and hypotheses

Use the actual Hilbert spaces B,G,R,D_R,Z,Y of proof 76, with their Hilbert product norms and the maximal transport graph norm on D_R. The proved decomposition of Lren is

 Lren(beta,u)=((A+Gamma_B)beta+Gamma_R u, X beta+S u),
 S=T_R+C_R:D_R->R.

Here A:B->G is an isomorphism; X:B->R is bounded; Gamma_B:B->G and Gamma_R:D_R->G are compact; C_R is bounded on R; and S is Fredholm of index zero. Write c(beta,u)=c_B beta+c_R u, where both functionals are bounded on the indicated spaces. Fix zeta=(zeta_J,zeta_R) in Y and Lred=Lren+c[.]zeta.

Assume S is injective. It is then an isomorphism from D_R to R. Denote s1=||S^(-1)||_(R->D_R). Define

 A'=A+Gamma_B-Gamma_R S^(-1)X,
 zJ=zeta_J-Gamma_R S^(-1)zeta_R,
 l=c_B-c_R S^(-1)X,
 d=1+c_R S^(-1)zeta_R,
 M(beta,s)=(A' beta+s zJ, l beta-d s).                 (1)

Then M:B direct-sum scalar -> G direct-sum scalar is Fredholm of index zero. For f=(fJ,fR), the equation Lred(beta,u)=f is equivalent to

 M(beta,s)=(fJ-Gamma_R S^(-1)fR,-c_R S^(-1)fR),
 u=S^(-1)(fR-X beta-s zeta_R),
 s=c(beta,u).                                         (2)

In particular the kernel map (beta,u)->(beta,c(beta,u)) is a bijection onto ker M. Lren is invertible if and only if A' is. When A' is invertible, M, and hence Lred, is invertible if and only if

 Delta=1+c_R S^(-1)zeta_R+l A'^(-1)zJ
       =1+c[Lren^(-1)zeta]                            (3)

is nonzero.

## Proof of the elimination and compactness

Solve the remainder equation for u, then insert the result into the jet equation and into s=c_B beta+c_R u. The latter becomes l beta-ds=-c_R S^(-1)fR, giving both signs in (2). Conversely the second row of M recovers exactly s=c(beta,u), so the reconstruction solves the original equation. This proves the equivalence and kernel bijection.

Gamma_R S^(-1)X is compact because X and S^(-1) are bounded into D_R and Gamma_R is compact on that graph space. Gamma_B is compact, but need not have finite rank. The zJ column, l row and scalar correction have finite rank. Thus M differs compactly from diag(A,-1), proving index zero. The usual bounded triangular elimination of Lren leaves diagonal blocks A' and S, proving their invertibility equivalence. With A' invertible, eliminating beta from (1) gives scalar coefficient -Delta. Finally Lren^(-1)zeta has components A'^(-1)zJ and S^(-1)(zeta_R-X A'^(-1)zJ). Applying c proves the equality in (3). No determinant of an infinite matrix is used.

## Correct norm bounds

Set a=(||Gamma_R||+||c_R||)s1, with the two norms taken on D_R. The right side g_f in (2) obeys

 ||g_f||_(G direct-sum scalar) <=(1+a)||f||_Y.

Therefore, with Hilbert operator norms,

 sqrt(||beta||_B^2+|s|^2) <=||M^(-1)||(1+a)||f||_Y,     (4)
 ||beta||_B+|s| <=sqrt(2)||M^(-1)||(1+a)||f||_Y.         (5)

The reconstruction also gives exactly

 ||u||_D_R <=s1(||fR||_R+||X||||beta||_B+|s|||zeta_R||_R). (6)

If M^(-1) is instead measured into the sum norm ||beta||+|s|, then the factor sqrt(2) in (5) is unnecessary. That convention must be stated. With the Hilbert convention, the theory author's displayed sum-norm bound without this factor is false as an abstract lemma: take all spaces one-dimensional, A=S=1, Gamma_B=Gamma_R=X=c_R=zeta_R=0, c_B=zeta_J=1. Then M=[[1,1],[1,-1]], its Hilbert inverse norm is1/sqrt(2), and fJ=1,fR=0 gives beta=s=1/2. The proposed bound would read1<=1/sqrt(2).

## Closedness, density and adjoint witnesses for the remainder block

T_R is the closed maximal transport realization on R. Smooth parity functions with compact support away from the axes are contained in its domain and dense in R, by truncation and mollification on regular patches. Since C_R extends boundedly on R, S=T_R+C_R on the same domain is closed and densely defined. Its Hilbert adjoint satisfies D(S*)=D(T_R*) and S*=T_R*+C_R*. This adjoint includes the complete axis-subtracted remainder coupling C_R; it is not obtained by dropping that subtraction from the raw velocity formula.

The accepted Gårding estimate in proof 76, strengthened by V086, and the transport energy give for any epsilon in(0,5/2)

 (5/2-epsilon)||u||_R <=||Su||_R+||K_epsilon u||_R,
 u in D_R,                                           (7)

with a compact operator on R, after absorbing its fixed numerical coefficient into K_epsilon. Indeed the quadratic energy lower bound has the form (5/2-epsilon)||u||^2 <=||Su||||u||+||K_epsilon u||||u||; division proves (7), with the zero vector trivial.

Thus proof 37's unbounded-operator adjoint certificate applies directly to S on R. It requires a proved finite-rank split K_epsilon=Ksmall+E Phi*, ||Ksmall||<=delta, orthonormal output columns E, and witnesses psi_i in D(S*) whose complete residuals S*psi_i-phi_i have aggregate norm e. If delta+e<5/2-epsilon, it gives

 ||S^(-1)||_(R->R) <=k1=(1+Psi)/(5/2-epsilon-delta-e).

The Fredholm index zero already proved supplies surjectivity. For the Hilbert transport graph norm a corresponding bound needed in (1)-(6) is

 s1 <=sqrt(k1^2+(1+||C_R||k1)^2),                     (8)

because T_R u=Su-C_Ru. The raw L2 inverse constant must not be substituted for s1 without this conversion. There are no jet rows in S's adjoint certificate, but the actual C_R adjoint, all compact-defect errors and all witness domains remain mandatory.

## Scope

The algebra, compactness reduction and conditional adjoint criterion are proved. The actual S injectivity, compact-defect split, witnesses, A' inverse, Delta and all quantitative bounds remain open. This is an exact reduction to a two-dimensional remainder equation and a coupled one-dimensional jet system, not a completed inverse certificate.
