"""Check the 'current SHA-256' table of NUM_REPORT section 8.
Run from the lane root (checks the lane files AND the artifacts/ copies) or from a copy of the artifacts folder (checks the local files only).
Gzipped copies (name.gz) are hashed after decompression. The files documented as not shipped are reported as NOT SHIPPED, not as failures.
Exit status: 0 if every present file matches, 1 otherwise."""
import hashlib, gzip, os, sys
NOT_SHIPPED = {"data/trial_v3_h0.004.npz", "data/trial_v4_M230.npz", "data/trial_v5_R0knot2.npz", "data/trial_n7.npz"}
rep = open("NUM_REPORT.md").read()
i = rep.index("| file | SHA-256 (current")
rows = []
for line in rep[i:].splitlines()[2:]:
    if not line.startswith("|"): break
    cells = [c.strip() for c in line.strip("|").split("|")]
    rows.append((cells[0], cells[1]))
def sha_any(path):
    """sha256 of path, or of path.gz decompressed; None if neither exists."""
    if os.path.exists(path):
        return hashlib.sha256(open(path, "rb").read()).hexdigest()
    if os.path.exists(path + ".gz"):
        return hashlib.sha256(gzip.open(path + ".gz", "rb").read()).hexdigest()
    return None
package_mode = not os.path.isdir("artifacts")
bad = 0
for f, h in rows:
    local = sha_any(f)
    art = None if package_mode else sha_any(os.path.join("artifacts", f))
    parts = []
    if local is None: parts.append("MISSING" if not package_mode else ("NOT SHIPPED (documented)" if f in NOT_SHIPPED else "MISSING"))
    elif local != h: parts.append("MISMATCH")
    if not package_mode:
        if art is None: parts.append("artifacts: NOT SHIPPED (documented)" if f in NOT_SHIPPED else "artifacts: MISSING")
        elif art != h: parts.append("artifacts: MISMATCH")
    st = "OK" if not parts else "; ".join(parts)
    if any(w in st for w in ("MISMATCH", "MISSING")) and not (f in NOT_SHIPPED and "MISMATCH" not in st): bad += 1
    print("%-40s %s" % (st, f))
print("%d rows, %d failures (documented omissions excluded), mode: %s" % (len(rows), bad, "package copy" if package_mode else "lane + artifacts"))
sys.exit(1 if bad else 0)
