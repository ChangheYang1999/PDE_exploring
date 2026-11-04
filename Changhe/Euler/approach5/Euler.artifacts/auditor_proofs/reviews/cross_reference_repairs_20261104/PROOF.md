# Targeted audit of the 2C and 2D cross-reference repairs

Status: complete targeted comparison with the Theory Agent C notes of 2026-11-04 at 01:47 and01:55. This is not a fresh audit of the entire dynamical proof or of its cited external papers.

## 1. Exact object and method

The report inspected is the pinned b16c72f4 version, full SHA256 b16c72f4410dd09ff65dfcf62729e9f0b543bb584c164b810d2a21e952dddda7. The source excerpts and the Theory Agent C notes are retained under verification. The method is direct comparison of each reference with its actual heading and use, including the neighboring proof passage.

## 2. The three repairs

After the 2C.1 dependency table the report calls its external theorems "section 3" and its elementary facts "3.7". Actual section3 is Assumptions and regularity, with subsections3.1-3.4. The intended external list is 2C.3, where an unnumbered paragraph still begins "3.7 Elementary facts used". The unambiguous replacements are "External theorems (2C.3)" and "the elementary facts listed at the end of 2C.3"; delete the stray3.7 prefix from that paragraph. This changes no cited theorem statement or proof premise.

In 2C.3, X3's "Used" list omits Lemma27. Its proof explicitly invokes absolute continuity and Ruelle's inequality to obtain h_nu(Psi_1)=kappa-d, citing [LS], X3 and the analogous Lemma20 argument. Adding "Lemma27 ([LS] and Ruelle, as in Lemma20)" accurately records the existing use. It adds no new theorem dependency. This audit verifies the use in the report, not those primary-source statements afresh.

The proof of Corollary L.2 says "Remark2.23 for the A312 class". Its intended item is headed "2D.2.23 Remark L_A312 (finite regularity under a strain bound)" and states the same r>=3, decay, C1 pressure and (r-1)a>3L class used by the corollary. Writing "Remark L_A312 (2D.2.23)" gives a unique reference. No extension to the C2 baseline or to the unrelated (C)/(G) classes follows.

## 3. Scope

All target passages, their neighboring headings, the full X1-X6 list and the two relevant Theory Agent C notes were read. Each proposed reference correction is valid. The optional addition of the scalar limit L to a notation-clash list is not required because Lemma7(a) defines it locally. This targeted audit neither certifies every claim in the Theory Agent C second read nor revisits unexamined originals, high-regularity constants or the unrestricted conjecture.
