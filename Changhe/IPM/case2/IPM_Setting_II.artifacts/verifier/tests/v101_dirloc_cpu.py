"""V101 aux: tests/v98_dirloc.py on the CPU, i.e. tests/v95_div_cpu.py (the one-thread copy of tests/v68_div.py) with d_th beta
by the local centred difference of order 4 (the only changed line, as in V98). Usage: python3 tests/v101_dirloc_cpu.py STATE.npz"""
import sys, math
src = open('tests/v95_div_cpu.py').read()
old = "dth_be = np.real(np.fft.ifft(1j*mm*np.fft.fft(be, axis=1), axis=1))"
assert src.count(old) == 1
h = "(2*math.pi/nt)"
src = src.replace(old, "dth_be = (8*(np.roll(be, -1, 1) - np.roll(be, 1, 1)) - (np.roll(be, -2, 1) - np.roll(be, 2, 1)))/(12*%s)" % h)
print('V101 dirloc cpu order 4', flush=True)
exec(compile(src, 'v95_div_cpu_dirloc', 'exec'))
