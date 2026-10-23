# Area preserving characteristic labels on the source basin

Status: CONFIRMED after independent derivation/checking and completed Opus 5.5 review 11. Date: 2026-10-20. The actual returned model was claude-opus-5-5; the review is in ../../evidence/opus_review_11/answer.md. Its suggestions were independently checked.

## Exact statement

Let A>1. Suppose W is a smooth vector field on R^2, of at most linear growth, equivariant under the two coordinate reflections, with div W=A+1 and DW(0)=diag(A,1). Suppose eta is smooth, even in x and odd in y, satisfies W dot grad eta=eta, and grad eta(0)=e2. Let B be the set of points whose backward trajectories tend to zero. Then there is a smooth diffeomorphism

    Phi=(xi,eta):B -> R^2,
    det D Phi=1, D Phi(0)=I,
    W dot grad xi=A xi.

Here xi is odd in x and even in y. There is no exception at integer A. For an exact primary IPM profile a0!=0, eta=rho/a0, A=2c_l-1, W=c_l X+(-psi_y,psi_x), -Delta psi=rho_x and curl W=partial_x W2-partial_y W1=-rho_x. The curl equation becomes, on B,

    eta Delta xi-A xi Delta eta-(A-1)grad xi dot grad eta
                              +a0 eta_x=0.                    (1)

This is a basin statement; B is not assumed to be the whole plane. Canonical reconstruction from labels is valid globally only if the identities and the required growth and parities hold globally.

Dependencies: the local inverse function theorem, completeness and differentiability of smooth ODE flows of at most linear growth, determinant evolution under divergence, and the inverse uniqueness in ../inverse/PROOF.md. The lead's source was referee/nogo1/ipm-referee/01-labels/PROOF.md; the argument below was reconstructed independently.

## Local construction

Near zero eta_y>0, so coordinates (x,b), b=eta(x,y), are valid on a sufficiently small centered rectangular chart in (x,b). Write y=Y(x,b), and set

    xi(x,Y(x,b))=integral_0^x Y_b(s,b) ds.

The inverse Y is even in x and odd in b. Its b derivative is even in both, giving the claimed parities of xi. Direct differentiation at fixed b gives

    xi_x eta_y-xi_y eta_x=Y_b eta_y=1,

and D Phi(0)=I. In these area preserving coordinates W=(f(a,b),b), where a=xi. Divergence is unchanged, so f_a=A and f=Aa+h(b). Reflection in x sends a to -a and leaves b fixed. Equivariance forces f to be odd in a, hence h=0. This removes every possible h, including a term b^A when A is integer.

## Globalization on the basin

Choose a small centered rectangle in label coordinates, whose inverse image lies in the local chart. The linear label flow (a,b) -> (e^(At)a,e^t b) keeps the rectangle invariant for negative time. Completeness of the physical flow follows from at most linear growth. For X in B and sufficiently large t>0, define

    Phi(X)=diag(e^(At),e^t) Phi(flow_(-t)(X)).

The local evolution law makes this independent of t once the trajectory has entered the rectangle. It is smooth. The determinant is e^((A+1)t) times e^(-(A+1)t), hence one. Two equal labels can be moved backward into the local rectangle, proving injectivity. Given any proposed label (a,b), shrink it by diag(e^(-At),e^(-t)) into the rectangle and flow its local inverse image forward for time t. That point remains in B and has the proposed label, proving surjectivity. A bijective local diffeomorphism is a diffeomorphism.

## Curl and limitations

Solving D Phi W=(Axi,eta) using det D Phi=1 gives

    W=(Axi eta_y-eta xi_y, -Axi eta_x+eta xi_x).

Differentiate to obtain

    curl W=eta Delta xi-Axi Delta eta-(A-1)grad xi dot grad eta.

Since curl W=-rho_x=-a0 eta_x, this is (1). In divergence form,

    div(eta grad xi-Axi grad eta+a0 eta e1)=0.

For eta>0, setting z=xi eta^(-A) gives div(eta^(A+1)grad z+a0 eta e1)=0. This equation retains the independent area constraint det D Phi=1; solving it with eta fixed does not solve the coupled label system. The determinant also shows grad rho is nonzero on B for an exact primary profile. It does not exclude critical points outside B or prove that B is the whole plane.
