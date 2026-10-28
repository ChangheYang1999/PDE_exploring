import subprocess,sys
base=[sys.executable,'-B','-u','proofs/68_independent_global_coefficients/code/global_check.py']
for args in [['ends'], ['finite', '--part', 'middle', '--start', '661', '--stop', '663', '--tag', 'smoke']]:
    subprocess.run(base+args,check=True)
