import sys,json
from pathlib import Path
name=sys.argv[1];chunk=sys.argv[2]
data=json.loads(Path(name+"_shape.npz.run.json").read_text())
data["squared_objective_change"]=1-(data["final_norm"]/data["initial_norm"])**2
Path(name+"_chunk"+chunk+".json").write_text(json.dumps(data,indent=2))
with Path("REPORT.md").open("a") as f:
    f.write(f"\n### {name}, chunk {chunk}\n\n")
    f.write(f"Command: `timeout 540 bash bounded.sh python3 centre_fit.py {data['input']} {data['output']} "
            f"--iterations {data['configuration']['iterations']} --seconds {data['configuration']['seconds']} "
            f"--nfev {data['configuration']['nfev']} --nr {data['configuration']['nr']} --nt {data['configuration']['nt']}"
            f"{' --recycle' if data['configuration'].get('recycle') else ''}`; stdout: `{name}_chunk{chunk}.log`; "
            f"record: `{name}_chunk{chunk}.json`.\n\n")
    f.write("| start norm | best norm | fractional improvement | E | D2 | c_l | x* | h(P) |\n"
            "| --- | --- | --- | --- | --- | --- | --- | --- |\n")
    h=data["history"][-1]
    f.write(f"| {data['initial_norm']:.12g} | {data['final_norm']:.12g} | {data['change']:.8g} "
            f"| {h['E']:.9g} | {h['D2']:.9g} | {h['cl']:.12g} | {h['xstar']:.12g} | {h['hP']:.12g} |\n\n")
    f.write(f"Termination: {data['message']}; this alone is not stagnation. "
            f"Elapsed {data['elapsed']:.1f} s; evaluations {data['nfev']}. "
            f"Squared least-squares objective reduction: "
            f"{100*data['squared_objective_change']:.6g}%.\n")
print(json.dumps(data))
