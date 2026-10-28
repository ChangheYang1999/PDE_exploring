# Closed-form upper bounds on the whole interval (Theorem 9.3 of the report)

`PROOF.md` states and proves $C_\alpha\le F^*(\alpha)$ and $D_\alpha\le G^*(\alpha)$ for every $0<\alpha<1$, with
$F^*(\alpha)=\frac{4\cdot2^{-\alpha/2}}{\pi\alpha(\alpha+2)}+\frac{0.418}{1-\alpha}+0.576$ and
$G^*(\alpha)=\frac{2^{1-\alpha}A_\alpha}{\alpha}+\frac{0.418}{1-\alpha}+1.076$. Commands (single-threaded, python-flint):

```
bash code/run_alpha0.sh
python3 code/make_remainders.py
python3 code/check_closed_form.py 0.418 0.576 4000 200
```

Outputs: `data/remainder_a0.json`, `data/remainders.json`, `results/closed_form_check.json`.
