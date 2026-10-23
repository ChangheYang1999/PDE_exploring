"""Versioned local continuation of the original fixed Stage XI C5 chart.

The original c5_chart.py and frozen N/E maps are unchanged. A physical feasible
base point supplies both Newton seeds and the affine origin, eliminating the
unreliable global zero-normal Newton selection. All operations require a guard.
"""
import os
if not os.environ.get('IPM_RESOURCE_SESSION'):
    raise RuntimeError('C5 continuation arithmetic requires the hardware supervisor')

import numpy as np
from c5_chart import C5Chart, constraints, hp_report, hp_values


class ContinuationChart(C5Chart):
    """Fixed N/E geometry with explicit feasible-base and local-delta lifting.

    `set_base(p)` retains the original nominal global coordinate label of p.
    An optional q supplies an explicit label, without changing N or E.
    `lift_delta(dq)` is preferred for small steps: it never subtracts two global
    coordinate vectors. `lift(q)` is compatibility syntax for q-base_q.
    """
    def __init__(self,record,base=None,q=None):
        super().__init__(record)
        self.version='stage11_local_offset_continuation_chart_v1'
        self.max_subdivision_depth=16
        self.max_path_steps=512
        self.maximum_relative_corrector=.5
        initial=self._geometry(self.anchor,check_sign=False)
        self.required_pair_sign=initial['pair_sign']
        self.required_normal_sign=initial['normal_sign']
        if self.required_normal_sign!=1.:
            raise ValueError('frozen starting chart does not have the audited positive normal determinant')
        self.set_base(self.anchor if base is None else base,q)

    def _geometry(self,p,check_sign=True):
        _,g=constraints(p,True)
        self._pair_check(p,g)
        pair=g[:2,self.zpair]
        pair_sign,pair_logdet=np.linalg.slogdet(pair)
        r=np.zeros((24,22));r[self.free22]=np.eye(22)
        r[self.zpair]=-np.linalg.solve(pair,g[:2,self.free22])
        a,g=self._normal_check(p,r)
        normal_sign,normal_logdet=np.linalg.slogdet(a)
        if check_sign and (pair_sign!=self.required_pair_sign or normal_sign!=self.required_normal_sign):
            raise ValueError('implicit determinant changed sign; a different root or fold is refused')
        zq=-np.linalg.solve(a,g[2:]@r@self.n)
        tangent=r@(self.n+self.e@zq)
        singular=np.linalg.svd(a,compute_uv=False)
        if not all(np.all(np.isfinite(value)) for value in (g,r,a,zq,tangent,singular)):
            raise ValueError('nonfinite continuation geometry')
        return {'G':g,'R':r,'A':a,'Zq':zq,'T':tangent,
                'pair_sign':float(pair_sign),'pair_logdet':float(pair_logdet),
                'normal_sign':float(normal_sign),'normal_logdet':float(normal_logdet),
                'pair_condition':float(np.linalg.cond(pair)),
                'normal_condition':float(singular[0]/singular[-1]),
                'normal_singular_values':singular.tolist()}

    @staticmethod
    def _public_geometry(geometry):
        return {key:value for key,value in geometry.items() if key not in ('G','R','A','Zq','T')}

    def _verify(self,p):
        self._bounds(p)
        report=hp_report(p)
        if (report['max_abs']>=self.tolerance or report['center_abs']>=self.tolerance
                or report['poisson_max_abs']>=self.tolerance or report['a0']<=1e-12
                or not report['physical_bounds']):
            raise ValueError('local C5 point fails unchanged HP, center, Poisson, bound or positive-branch conditions')
        return report

    def set_base(self,p,q=None):
        p=np.asarray(p,dtype=float)
        if p.shape!=(24,) or not np.all(np.isfinite(p)):
            raise ValueError('continuation base must have 24 finite physical parameters')
        report=self._verify(p)
        geometry=self._geometry(p)
        q=super().coordinates(p) if q is None else np.asarray(q,dtype=float)
        if q.shape!=(19,) or not np.all(np.isfinite(q)):
            raise ValueError('base coordinate label must have 19 finite values')
        self.base=p.copy();self.base_p=self.base
        self.base_q=q.copy()
        self.base_geometry=geometry
        self.base_tangent=geometry['T'].copy()
        self.base_report=report
        self.base_global_coordinates=np.linalg.solve(self.complete,p[self.free22]-self.anchor[self.free22])
        # Quantify the parameter change implied by independent feasibility
        # tolerance and binary64 storage. This is only a continuity diagnostic;
        # it never changes the absolute Taylor acceptance tolerance.
        c=hp_values(p)
        pair_correction=np.zeros(24)
        pair_correction[self.zpair]=np.linalg.solve(geometry['G'][:2,self.zpair],c[:2])
        normal_correction=geometry['R']@self.e@np.linalg.solve(geometry['A'],c[2:])
        rounding=128*np.finfo(float).eps*max(1.,np.linalg.norm(p))
        self.base_parameter_feasibility_indicator=float(np.linalg.norm(pair_correction)+np.linalg.norm(normal_correction)+rounding)
        self.last_diagnostics={'version':self.version,'base_bitwise_preserved':True,
                               'base_HP_defect':report['max_abs'],
                               'base_geometry':self._public_geometry(geometry)}
        return self

    def coordinates(self,p):
        p=np.asarray(p,dtype=float)
        if p.shape!=(24,) or not np.all(np.isfinite(p)):
            raise ValueError('expected 24 finite physical parameters')
        if np.array_equal(p,self.base):return self.base_q.copy()
        local=np.linalg.solve(self.complete,p[self.free22]-self.base[self.free22])
        return self.base_q+local[:19]

    def _pair_geometry(self,p):
        _,g=constraints(p,True)
        self._pair_check(p,g)
        sign,_=np.linalg.slogdet(g[:2,self.zpair])
        if sign!=self.required_pair_sign:
            raise ValueError('quadratic Newton attempted another implicit branch')
        r=np.zeros((24,22));r[self.free22]=np.eye(22)
        r[self.zpair]=-np.linalg.solve(g[:2,self.zpair],g[:2,self.free22])
        return g,r

    def _c2_warm(self,free_values,seed):
        p=np.asarray(seed,dtype=float).copy();p[self.free22]=free_values
        self._bounds(p)
        best=None;best_norm=float('inf');history=[]
        for iteration in range(self.record['inner_max_iterations']):
            c=hp_values(p)[:2];norm=float(np.linalg.norm(c))
            g,r=self._pair_geometry(p)
            row={'iteration':iteration,'C2_HP':c.tolist(),
                 'pair_condition':float(np.linalg.cond(g[:2,self.zpair])),'line_search':[]}
            if norm<best_norm:best=(p.copy(),r.copy());best_norm=norm
            if np.max(abs(c))<=self.target:
                row['target_reached']=True;history.append(row)
                return p,r,history
            dz=np.linalg.solve(g[:2,self.zpair],-c)
            accepted=False
            for fraction in (1.,.5,.25,.125,.0625,.03125,.015625,.0078125):
                trial=p.copy();trial[self.zpair]+=fraction*dz
                probe={'fraction':fraction}
                try:
                    self._bounds(trial);_,tr=self._pair_geometry(trial)
                    trial_c=hp_values(trial)[:2];trial_norm=float(np.linalg.norm(trial_c))
                    probe.update(C2_HP=trial_c.tolist(),decreases=bool(trial_norm<norm))
                except (ValueError,np.linalg.LinAlgError) as exc:
                    probe['refused']=str(exc);row['line_search'].append(probe);continue
                row['line_search'].append(probe)
                if trial_norm<norm:
                    p,r=trial,tr;accepted=True
                    if trial_norm<best_norm:best=(p.copy(),r.copy());best_norm=trial_norm
                    break
            row['accepted']=accepted;history.append(row)
            if not accepted:break
        if best is None or np.max(abs(hp_values(best[0])[:2]))>=self.tolerance:
            raise ValueError('warm quadratic corrector failed unchanged HP feasibility')
        return best[0],best[1],history

    def _correct(self,dq,normal_seed,physical_seed):
        z=np.asarray(normal_seed,dtype=float).copy()
        pseed=np.asarray(physical_seed,dtype=float)
        best=None;best_norm=float('inf');history=[]
        for iteration in range(self.record['outer_max_iterations']):
            if np.linalg.norm(self.base_global_coordinates[19:]+z)>self.record['normal_branch_field_radius']:
                raise ValueError('original global normal branch radius exceeded')
            free_values=self.base[self.free22]+self.n@dq+self.e@z
            p,r,inner=self._c2_warm(free_values,pseed)
            geometry=self._geometry(p);c=hp_values(p);norm=float(np.linalg.norm(c[2:]))
            row={'iteration':iteration,'normal_offset':z.tolist(),'C5_HP':c.tolist(),
                 'geometry':self._public_geometry(geometry),'C2_iterations':inner,'line_search':[]}
            if norm<best_norm:best=(p.copy(),z.copy(),geometry);best_norm=norm
            if np.max(abs(c))<=self.target or (np.max(abs(c[2:]))<=self.target and np.max(abs(c[:2]))<self.tolerance):
                row['target_reached']=bool(np.max(abs(c))<=self.target);history.append(row)
                return p,z,geometry,history
            dz=np.linalg.solve(geometry['A'],-c[2:]);accepted=False
            for fraction in (1.,.5,.25,.125,.0625,.03125,.015625,.0078125):
                zz=z+fraction*dz;probe={'fraction':fraction,'normal_offset':zz.tolist()}
                try:
                    if np.linalg.norm(self.base_global_coordinates[19:]+zz)>self.record['normal_branch_field_radius']:
                        raise ValueError('original global normal branch radius exceeded')
                    trial,tr,tinner=self._c2_warm(self.base[self.free22]+self.n@dq+self.e@zz,p)
                    trial_geometry=self._geometry(trial);trial_c=hp_values(trial)
                    trial_norm=float(np.linalg.norm(trial_c[2:]))
                    probe.update(C5_HP=trial_c.tolist(),geometry=self._public_geometry(trial_geometry),
                                 C2_iterations=tinner,decreases=bool(trial_norm<norm))
                except (ValueError,np.linalg.LinAlgError) as exc:
                    probe['refused']=str(exc);row['line_search'].append(probe);continue
                row['line_search'].append(probe)
                if trial_norm<norm:
                    p,z,pseed=trial,zz,trial
                    accepted=True
                    if trial_norm<best_norm:best=(p.copy(),z.copy(),trial_geometry);best_norm=trial_norm
                    break
            row['accepted']=accepted;history.append(row)
            if not accepted:break
        if best is None or np.max(abs(hp_values(best[0])))>=self.tolerance:
            raise ValueError('warm fourth-order corrector failed unchanged HP feasibility')
        return best[0],best[1],best[2],history

    def _continuity(self,previous,predicted_step,candidate):
        actual=candidate-previous
        correction=actual-predicted_step
        # This empirical continuity allowance only affects whether a path is
        # subdivided. It cannot turn a Taylor-infeasible point into a feasible
        # one and is not a claim of an interval-certified unique root.
        floor=20*self.base_parameter_feasibility_indicator
        allowance=self.maximum_relative_corrector*np.linalg.norm(predicted_step)+floor
        error=float(np.linalg.norm(correction))
        return error<=allowance,{'parameter_step':float(np.linalg.norm(actual)),
                                'linear_parameter_step':float(np.linalg.norm(predicted_step)),
                                'predictor_correction_norm':error,
                                'continuity_allowance':float(allowance),
                                'parameter_feasibility_floor_allowance':float(floor)}

    def lift_delta(self,dq,derivative=False):
        dq=np.asarray(dq,dtype=float)
        if dq.shape!=(19,) or not np.all(np.isfinite(dq)):
            raise ValueError('local lift requires 19 finite coordinate increments')
        if np.all(dq==0):
            p=self.base.copy();self._verify(p)
            self.last_diagnostics={'version':self.version,'zero_delta_bitwise':True,
                                   'normal_offset':[0.]*3,'path':[],
                                   'base_q':self.base_q.tolist(),
                                   'maximum_HP_defect':self.base_report['max_abs'],
                                   'geometry':self._public_geometry(self.base_geometry)}
            return (p,self.base_tangent.copy()) if derivative else p
        fraction=0.;step_fraction=1.;p=self.base.copy();z=np.zeros(3)
        geometry=self.base_geometry;path=[];refusals=[];attempts=0
        while fraction<1.:
            if len(path)>=self.max_path_steps or attempts>=4*self.max_path_steps:
                self.last_diagnostics={'version':self.version,'path':path,'refusals':refusals}
                raise ValueError('local continuation path exceeded its explicit diagnostic budget')
            next_fraction=min(1.,fraction+step_fraction)
            increment=(next_fraction-fraction)*dq
            target=next_fraction*dq
            normal_seed=z+geometry['Zq']@increment
            predicted=geometry['T']@increment
            attempts+=1
            try:
                candidate,newz,new_geometry,newton=self._correct(target,normal_seed,p)
                report=self._verify(candidate)
                continuous,displacement=self._continuity(p,predicted,candidate)
                if not continuous:
                    raise ValueError('corrected root is not local to its feasible tangent predictor')
            except (ValueError,np.linalg.LinAlgError) as exc:
                refusals.append({'from_fraction':fraction,'to_fraction':next_fraction,
                                 'step_fraction':step_fraction,'reason':str(exc)})
                step_fraction*=.5
                if step_fraction<2.**(-self.max_subdivision_depth):
                    self.last_diagnostics={'version':self.version,'path':path,'refusals':refusals}
                    raise ValueError('local continuation cannot cross a fold/branch failure or unresolved feasibility floor: '+str(exc)) from exc
                continue
            path.append({'from_fraction':fraction,'to_fraction':next_fraction,
                         'p':candidate.tolist(),'normal_offset':newz.tolist(),
                         'maximum_HP_defect':report['max_abs'],
                         'geometry':self._public_geometry(new_geometry),
                         'predictor_corrector':displacement,'Newton_history':newton})
            p,z,geometry=candidate,newz,new_geometry
            fraction=next_fraction
            step_fraction=min(1.-fraction,2*step_fraction) if fraction<1. else 0.
        global_free=self.anchor[self.free22]+self.n@(self.base_global_coordinates[:19]+dq)+self.e@(self.base_global_coordinates[19:]+z)
        direct_free=self.base[self.free22]+self.n@dq+self.e@z
        offset=direct_free-global_free
        self.last_diagnostics={'version':self.version,'zero_delta_bitwise':False,
                               'base_q':self.base_q.tolist(),'delta_q':dq.tolist(),
                               'normal_offset':z.tolist(),'path':path,'refusals':refusals,
                               'maximum_HP_defect':self._verify(p)['max_abs'],
                               'geometry':self._public_geometry(geometry),
                               'affine_offset_from_global_formula':offset.tolist(),
                               'affine_offset_parameter_norm':float(np.linalg.norm(offset)),
                               'affine_offset_complete_coordinates':np.linalg.solve(self.complete,offset).tolist(),
                               'fixed_N_E_geometry_unchanged':True}
        return (p,geometry['T'].copy()) if derivative else p

    def lift(self,q,derivative=False):
        q=np.asarray(q,dtype=float)
        return self.lift_delta(q-self.base_q,derivative)


# Explicit alternative name for callers that prefer to emphasize the C5 family.
LocalC5Chart=ContinuationChart
