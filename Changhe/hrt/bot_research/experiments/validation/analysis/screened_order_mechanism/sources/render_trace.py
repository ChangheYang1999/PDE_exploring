"""Render retained engine observations without calling a policy or game routine."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
A=Path('bot_research/experiments/validation/analysis/screened_order_mechanism')
receipt=A/'verification/full_check.json'
data=json.loads(receipt.read_text())
assert data['all_checks_passed'] and data['policy_calls']==0
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
inputs={str(receipt):sha(receipt)}
for p,h in data['evidence_sha256'].items():
    assert sha(p)==h
    inputs[p]=h
fig,(ax,bx)=plt.subplots(1,2,figsize=(11.6,5.2),gridspec_kw={'width_ratios':[1,1.25]})
first=data['cases'][0]
path=first['route']
ax.plot([p[0] for p in path],[p[1] for p in path],color='#82909d',linewidth=2.8,zorder=1)
for b in first['buildings']:
    x,y=b['x'],b['y']
    if b['type']=='wall':
        ax.add_patch(Rectangle((x-.43,y-.43),.86,.86,facecolor='#d6dce2',edgecolor='#8b96a1',linewidth=.6,zorder=2))
    else:
        ax.add_patch(Circle((x,y),.38,facecolor='#e6a84b',edgecolor='#654715',linewidth=.8,zorder=3))
        ax.text(x,y,'8',ha='center',va='center',fontsize=8,zorder=4)
ax.scatter([0,11],[0,11],s=70,c=['#387f5b','#a14252'],zorder=5)
ax.text(.35,-.42,'spawn',fontsize=9)
ax.text(10.75,11.6,'base',ha='right',fontsize=9)
ax.set(xlim=(-.7,11.7),ylim=(11.8,-.8),xticks=range(12),yticks=range(12),xlabel='x',ylabel='y')
ax.grid(color='#edf0f3',linewidth=.6)
ax.set_aspect('equal')
ax.tick_params(labelsize=7)
ax.set_title('Same route and five gun1 turrets',loc='left',fontsize=11,pad=12)
colors={'screen':'#227354','middle':'#a95723','front':'#466aa6'}
labels={'screen':'2, 2, 3: arrives with 12 HP','middle':'2, 3, 2: dies at tick 42','front':'3, 2, 2: dies at tick 37'}
for case in data['cases']:
    rows=json.loads(Path(case['trace']).read_text())
    observations=[(r['tick'],c['hp_after']) for r in rows for c in r['copies'] if c['type']=='tier3']
    assert observations
    born=observations[0][0]
    xs=[born-.5]+[x for x,y in observations]
    ys=[180]+[y for x,y in observations]
    color=colors[case['order_label']]
    bx.step(xs,ys,where='post',color=color,linewidth=2,label=labels[case['order_label']])
    bx.scatter([xs[-1]],[ys[-1]],color=color,s=30,zorder=4)
bx.axhline(0,color='#444444',linewidth=.8)
bx.set(xlim=(-1,49),ylim=(-22,192),xlabel='Combat tick',ylabel='Tier3 HP after turret damage',yticks=[0,30,60,90,120,150,180])
bx.grid(axis='y',color='#e9edf0',linewidth=.6)
bx.legend(loc='upper right',frameon=True,fontsize=8.5,title='Purchase order (tier numbers)',title_fontsize=9)
bx.set_title('Order changes which copy receives each shot',loc='left',fontsize=11,pad=12)
fig.subplots_adjust(left=.06,right=.985,top=.9,bottom=.18,wspace=.27)
fig.text(.06,.065,'Fixed C02 round-six state and best_v9e action. Each roster costs 180 gold. All 750 original combat ticks checked.',fontsize=9,color='#333333')
fig.text(.06,.025,'Numbers inside turret circles are damage per shot. The route has 44 steps; arrivals resolve before turret attacks.',fontsize=9,color='#333333')
outputs={}
for extension in ('svg','png'):
    p=A/'figures'/('purchase-order.'+extension)
    if p.exists():raise FileExistsError(p)
    fig.savefig(p,dpi=180,facecolor='white')
    outputs[str(p)]=sha(p)
plt.close(fig)
inputs[str(Path(__file__))]=sha(__file__)
# Normalize the tool's source name for the published receipt.
source='bot_research/experiments/validation/analysis/screened_order_mechanism/sources/render_trace.py'
inputs.pop(str(Path(__file__)))
inputs[source]=sha(source)
result=dict(time_utc=datetime.now(timezone.utc).isoformat(),matplotlib_version=matplotlib.__version__,inputs_sha256=inputs,outputs_sha256=outputs,new_policy_calls=0,new_component_calls=0)
p=A/'verification/figure.json'
with p.open('x') as stream:json.dump(result,stream,indent=2,sort_keys=True);stream.write('\n')
print(json.dumps(result))
