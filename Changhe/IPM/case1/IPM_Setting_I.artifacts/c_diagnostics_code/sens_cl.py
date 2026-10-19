"""dB_3/dc_l along consistent perturbations: w -> w * A(c_l + e)/A(c_l) (keeps w'(0) = -A), and
w -> w (1 + s (x/x*)^2)-type shape changes combined; construct1 final. Natural units."""
import sys
sys.argv = ['sens.py']
src = open('sens.py').read().split("B0 = b3(")[0]
exec(src)
B0 = b3(w0, wp0, wpp0, cl0)
for e in (1e-4, 1e-3, -1e-3):
    cl = cl0 + e; s = (2 * cl - 1) / (2 * cl0 - 1)
    B = b3(lambda t: s * w0(t), lambda t: s * wp0(t), lambda t: s * wpp0(t), cl)
    print(f'scaled w, dc_l {e:+.0e}: B_3 {B:.5f}  dB3/dc_l {(B - B0) / e: .3f}')
