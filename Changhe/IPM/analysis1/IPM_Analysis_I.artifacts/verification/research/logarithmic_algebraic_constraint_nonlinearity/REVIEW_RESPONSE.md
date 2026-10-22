# Precision notes and response to the proof review

Date 2026-10-22T05:51:30.353779+00:00. The complete proof review confirms both finite eliminations and the absence of a hidden continuity requirement. This note resolves its minor velocity-order wording remark and states the finite evidence limits.

For the wave potential f=n^(-s-2)a cos(nphi), the exact canonical velocity has components

 U1=n^(-s)a phi_x phi_y cos(nphi)
   +n^(-s-1)(a_x phi_y+a_y phi_x+a phi_xy)sin(nphi)
   -n^(-s-2)a_xy cos(nphi),
 U2=-n^(-s)a phi_x^2 cos(nphi)
   -n^(-s-1)(2a_x phi_x+a phi_xx)sin(nphi)
   +n^(-s-2)a_xx cos(nphi).

These are the identities independently checked in209, obtained directly fromU=(-f_xy,f_xx). Each amplitude is fixed smooth compact. The three modulation orders therefore mean exactly the three displayed spatially constant powers ofn. They give uniformYbounds onU[h] and then onU[h].grad rho, so they DO enter the full graph upper bound. They are not needed for a separate lower bound onU[h].grad g, because that term is identically zero by compact support. The first review's minor remark correctly limited that observation to the lower bound. The text “supports for differenti” inPROOF.md means “supports for distincti”; it is a typographical error with no other change.

The primary eight identities include five formal Kronecker patch selectors. These are bookkeeping identities, not independent proof of disjoint physical supports or bounded fractional localization. The latter facts are supplied by the construction and inherited209proof. The independent code recomputes the three generic polynomial identities with the sparsefmpqring adapted from210. The new substantive finite checks are56 manufactured rational systems:24group systems and32wave systems across8fixtures;17rankzero,19positivedeficient,20fullrowrank. Both routes construct every matrix independently and find a nonzero kernel vector, normalize by its largest absolute coordinate, verify exact annihilation, and check that a selected active cross coefficient stays nonzero. Primary usesSympy.nullspace, secondary explicit rational row reduction. Both fresh parentrehashes cover2089files. These fixtures illustrate algebra only. They do not sample an actual discontinuous functional or prove a statement for allLambda; the general proof uses only dimension and normalization and works for the actual values whatever they are.

No interval enclosure, modal norm ceiling or numerical value of the analytic cross-growth constant is computed. No failure was recorded by either mathematical checker. The theorem'sMAXIMUM lower limit, every-ball quantifier and algebraic-codimension scope are unchanged.
