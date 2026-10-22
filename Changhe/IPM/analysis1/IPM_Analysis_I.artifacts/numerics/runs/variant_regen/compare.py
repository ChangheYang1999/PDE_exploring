"""Compare the regenerated trial files (runs/variant_regen/*.npz) with the stored ones, array by array, and by SHA-256 of the whole file.
When a stored reference is not present (the three variant trials are not shipped in the artifacts folder), the regenerated file's SHA-256 is printed
for comparison with the hash table of NUM_REPORT section 8. Exit status 0 only if every available comparison is an exact match."""
import numpy as np, hashlib, os, sys
TABLE = {"data/trial_v2_h0.008.npz": "a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874",
         "data/trial_v3_h0.004.npz": "1e4ee66f1919e08de07fb0c9e85846aedf973c7872eda50f8881a57194b6a2dd",
         "data/trial_v4_M230.npz":   "11c97a14ac42f67da2696b440d70db112cbb3b667d06afaa0c1bb8ddfe43bde8",
         "data/trial_v5_R0knot2.npz":"74345bd9957269ad16a433e37a130f940f66cff79a579de01d6faf5cd3523f31"}   # NUM_REPORT section 8 (2026-10-22)
pairs = [("data/trial_v2_h0.008.npz", "runs/variant_regen/trial_v2_h0.008.npz", "python3 src/modal_fit.py MODES 0.008 0.02 OUT"),
         ("data/trial_v3_h0.004.npz", "runs/variant_regen/trial_v3_h0.004.npz", "python3 src/modal_fit.py MODES 0.004 0.01 OUT"),
         ("data/trial_v4_M230.npz",   "runs/variant_regen/trial_v4_M230.npz",   "python3 src/modal_fit.py MODES 0.008 0.02 OUT 230"),
         ("data/trial_v5_R0knot2.npz","runs/variant_regen/trial_v5_R0knot2.npz","python3 src/modal_fit.py MODES 0.008 0.02 OUT - -2")]
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
fail = 0
for stored, regen, cmd in pairs:
    print("==", stored, "<-", cmd)
    if not os.path.exists(regen):
        print("   regenerated file MISSING (run runs/variant_regen.sh first)"); fail += 1; continue
    hr = sha(regen); print("   regenerated sha256 %s" % hr)
    print("   table sha256       %s  -> %s" % (TABLE[stored], "EQUAL (byte-identical to the file hashed in the report)" if hr == TABLE[stored] else "DIFFERENT"))
    if hr != TABLE[stored]: fail += 1
    if not os.path.exists(stored):
        print("   stored reference not present here (not shipped): array comparison skipped, the hash comparison above stands"); continue
    hs = sha(stored); print("   stored sha256      %s  -> %s" % (hs, "byte-identical" if hs == hr else "DIFFERENT BYTES"))
    if hs != hr: fail += 1   # (verifier 07:14Z: a stored/regenerated hash mismatch must fail even when the table hash matches one side)
    a = np.load(stored); b = np.load(regen)
    if sorted(a.files) != sorted(b.files): print("   KEY SETS DIFFER", sorted(a.files), sorted(b.files)); fail += 1
    allexact = True
    for key in sorted(a.files):
        x = np.asarray(a[key], dtype=float); y = np.asarray(b[key], dtype=float)
        if x.shape != y.shape:
            print("   %-9s SHAPE DIFFERS %s vs %s" % (key, x.shape, y.shape)); allexact = False; continue
        if np.array_equal(x, y):
            print("   %-9s shape %-12s identical" % (key, x.shape))
        else:
            allexact = False; d = np.abs(x - y); print("   %-9s shape %-12s max|diff| %.3e  rel-to-max %.3e" % (key, x.shape, d.max(), d.max() / max(np.abs(x).max(), 1e-300)))
    print("   ALL ARRAYS IDENTICAL" if allexact else "   NOT ALL IDENTICAL (see above)")
    if not allexact: fail += 1
print("RESULT:", "all comparisons exact" if fail == 0 else "%d comparison(s) failed or missing" % fail)
sys.exit(1 if fail else 0)
