#!/usr/bin/env python3
"""Two offline coefficient-envelope figures from the frozen L2 export."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,csv,hashlib,json,time,shutil
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from piecewise_loading import load_piecewise
ROOT=Path(__file__).resolve().parent;LANE=ROOT.parent

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();out=a.output.resolve()
 if not out.is_relative_to(LANE) or out.exists():raise ValueError('Fresh lane output required')
 out.mkdir(parents=True);start=time.perf_counter();cpu=time.process_time()
 candidate=ROOT/'external_exports/T1_ladder_L2_20261028T235434Z/coeffs.npz';before=sha(candidate)
 (out/'FIGURE_NOTES.md').write_text('''# L2 coefficient envelopes\n\nIdea: the angular and radial coefficient tails of the saved L2 approximation behave differently. Question: where does the retained native expansion still carry appreciable coefficients near its truncation? A plot shows the parity oscillation and the relative decay over indices, which a final-index number hides.\n\nEncoding: each panel is one field and one radial element. The ordinate is the largest absolute native coefficient over the other index. Angular panels include all degrees, without assuming parity. Radial panels cover the ball and shell; exterior powers are not a polynomial index sequence. Element and field normalizations differ; these are coefficient envelopes, not energy spectra or rigorous truncation-error bounds. All data are the frozen numerical approximation, with no smoothing or fitted rate.\n\nThe coefficient arrays and table values are independently checked against the documented flat labels in the NPZ. PNG, PDF and SVG are rendered offline. Visual review follows rendering; the lead has requested the figure, and final manuscript selection remains with the lead.\n''')
 field=load_piecewise(candidate);raw=np.load(candidate,allow_pickle=False);metadata=json.loads(str(raw['meta_json']));checks=[];summaries={};tables={}
 for i,e in enumerate(metadata['elements']):
  for key in ['phi','q']:
   labels=e['labels'];cols=e.get(key+'_cols');labels=labels if cols is None else [labels[j] for j in cols]
   values=raw[f'{key}_el{i}'];angular={};radial={}
   for (n,k),v in zip(labels,values):
    angular[int(n)]=max(angular.get(int(n),0.),abs(float(v)));radial[float(k)]=max(radial.get(float(k),0.),abs(float(v)))
   C=field.matrices[i,key];env=np.max(abs(C),axis=1);renv=np.max(abs(C),axis=0)
   for n,v in enumerate(env):checks.append(v==angular.get(n,0.))
   for k,v in zip(field.radial_keys[i,key],renv):checks.append(v==radial.get(float(k),0.))
   m=float(max(env));nmax=len(env)-1;par=1 if key=='phi' else 0
   summaries[f'{key}_el{i}']=dict(maximum=m,nmax=nmax,top_dominant=max(float(env[n]/m) for n in range(nmax+1) if n%2==par and n>=nmax-4),top_other=max(float(env[n]/m) for n in range(nmax+1) if n%2!=par and n>=nmax-4),last_radial_relative=float(renv[-1]/np.max(renv)))
 if not all(checks):raise AssertionError('Matrix-to-flat-label envelope comparison failed')
 plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'axes.grid':True,'grid.alpha':.2})
 figures=[]
 for kind,ncols in [('angular',3),('radial',2)]:
  rows=[];fig,axs=plt.subplots(2,ncols,figsize=(10.5 if ncols==3 else 8.5,6.1))
  for i in range(ncols):
   for j,key in enumerate(['phi','q']):
    C=field.matrices[i,key];vals=np.max(abs(C),axis=1 if kind=='angular' else 0);indices=np.arange(len(vals)) if kind=='angular' else field.radial_keys[i,key];ax=axs[j,i]
    ax.semilogy(indices,np.maximum(vals,1e-20),'o-',ms=3);ax.set_title(f'{key}: {field.elements[i]["kind"]}');ax.set_xlabel('Legendre degree n' if kind=='angular' else 'Radial polynomial index k');ax.set_ylabel('Max |native coefficient|')
    rows.extend(dict(field=key,element=i,index=float(n),envelope=float(v),relative_to_element_maximum=float(v/max(vals))) for n,v in zip(indices,vals))
  name=kind+'_coefficients';fig.suptitle(f'T1 ladder L2, c_l={field.c_l:.3f}; {kind} coefficient envelopes');fig.tight_layout(rect=(0,.045,1,1));fig.text(.015,.008,'Numerical approximation; independent acceptance failed.',fontsize=9)
  for ext in ['png','pdf','svg']:fig.savefig(out/f'{name}.{ext}',dpi=160)
  plt.close(fig)
  with (out/f'{name}.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
  tables[name]=rows;figures.append(name)
 lead=LANE.parent/'e4-lead/checks/angular_envelope_output.json';lead_hash=sha(lead);lead_values=json.loads(lead.read_text())['L2'];delta={key:abs(value['top_dominant']-lead_values[key]['rel_at_top_dominant']) for key,value in summaries.items()};checks.extend(d<1e-15 for d in delta.values())
 if not all(checks):raise AssertionError('Lead envelope comparison failed')
 assert sha(candidate)==before and sha(lead)==lead_hash
 shutil.copy2(Path(__file__),out/'plot_source.py')
 record=dict(completed_utc=datetime.now(timezone.utc).isoformat(),wall_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu,candidate_sha256=before,candidate_path=str(candidate),source_sha256=sha(Path(__file__)),lead_comparison_sha256=lead_hash,checks=len(checks),all_pass=all(checks),summary=summaries,lead_absolute_differences=delta,figures=figures,artifact_sha256={p.name:sha(p) for p in out.iterdir() if p.is_file()})
 (out/'manifest.json').write_text(json.dumps(record,indent=2)+'\n')
 (out/'CAPTIONS.md').write_text('''# L2 spectral coefficient decay\n\nThe angular envelope is the maximum absolute native coefficient over radial columns at each Legendre degree. Both parities are retained. Element normalizations differ, so these curves are not a physical energy spectrum. Visible tails do not by themselves quantify the differential-equation error.\n\nThe radial envelope is the maximum absolute native coefficient over angular degrees. Ball indices obey the total-degree cutoff and therefore contain fewer angular modes at high radial index. The exterior consists of explicit decay powers and is omitted from the polynomial-index figure.\n\nThese figures describe the frozen L2 approximation, c_l=0.749, whose independently evaluated Euler residuals fail the acceptance thresholds. L1 and L2 are distinct reoptimized states; comparison is not a fixed-field convergence study.\n''')
 print(json.dumps(record,indent=2))
if __name__=='__main__':main()
