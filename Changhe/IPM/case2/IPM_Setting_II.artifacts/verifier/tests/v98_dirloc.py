"""V98: tests/v68_div.py with d_th beta taken by a local centred difference (order 2 or 4) instead of the FFT. Question: is the
512 -> 1024 sensitivity of my direct-form D (up to 0.11; V79, report Section 5.8(vi)) an artifact of the spectral derivative of beta
across its angular layer? (The numerics' direct form agrees with their divergence form to 0.007 at 512 and 1024 angles, their
note 09:40Z.) Only the line computing dth_be is changed; everything else is v68_div.py.
Usage: python3 tests/v98_dirloc.py STATE.npz [order (4)]"""
import sys
order = int(sys.argv[2]) if len(sys.argv) > 2 else 4
src = open('tests/v68_div.py').read()
old = "dth_be = np.real(np.fft.ifft(1j*mm*np.fft.fft(be, axis=1), axis=1))"
assert src.count(old) == 1
h = "(2*math.pi/nt)"
new = {2: "dth_be = (np.roll(be, -1, 1) - np.roll(be, 1, 1))/(2*%s)" % h,
       4: "dth_be = (8*(np.roll(be, -1, 1) - np.roll(be, 1, 1)) - (np.roll(be, -2, 1) - np.roll(be, 2, 1)))/(12*%s)" % h}[order]
src = src.replace(old, new)
print('V98 order', order, flush=True)
sys.argv = [sys.argv[0], sys.argv[1]]
exec(compile(src, 'v68_div_dirloc', 'exec'))
