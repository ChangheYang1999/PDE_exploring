"""Print the per-region residual table of one independent evaluation file (read-only) as markdown.

Usage: python3 selected_table.py <evaluation.json>
Momentum: relative RMS, absolute RMS, absolute q99.9 and sampled maximum; then the relative RMS of the vorticity
equation, the pressure-Poisson equation and the divergence. Values are sampled statistics, not whole-space bounds.
"""
import json, sys

NAMES = {'shell_0_0.25': 'R < 0.25', 'shell_0.25_1': '0.25 < R < 1', 'shell_1_2': '1 < R < 2',
         'shell_2_4': '2 < R < 4', 'shell_4_8': '4 < R < 8', 'shell_8_16': '8 < R < 16',
         'shell_16_32': '16 < R < 32', 'shell_32_64': '32 < R < 64',
         'cartesian_grid_core': 'core grid', 'axis_line': 'axis'}


def g(x):
    return f"{x:.3g}"


d = json.load(open(sys.argv[1]))
print("| Region | Momentum rel. RMS | Momentum abs. RMS | Momentum abs. q99.9 | Momentum sampled max | "
      "Vorticity rel. RMS | Pressure-Poisson rel. RMS | Divergence rel. RMS |")
print("|---|---|---|---|---|---|---|---|")
for k, name in NAMES.items():
    r = d['regions'].get(k)
    if r is None:
        continue
    m = r['momentum']
    print(f"| {name} | {g(m['relative_rms'])} | {g(m['absolute']['rms'])} | {g(m['absolute']['q999'])} | "
          f"{g(m['absolute']['sampled_max'])} | {g(r['vorticity']['relative_rms'])} | "
          f"{g(r['pressure_poisson']['relative_rms'])} | {g(r['divergence']['relative_rms'])} |")
