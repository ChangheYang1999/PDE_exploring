"""Unchanged historical core plus genuinely new linear potential functions.

The core matrix products and center-stabilized ratio retain their original
arithmetic. Only the extra potential fields are new. At zero extra coefficients
the original residual path is used verbatim.
"""
from concurrent.futures import ProcessPoolExecutor
import multiprocessing as mp
from stage12_common import *
from spectral_basis import evaluate_modes

KEYS = ('f', 'fx', 'fy', 'psi', 'psix', 'psiy', 'ratio')
FIT_KEYS = ('f', 'fx', 'fy', 'psix', 'psiy', 'ratio')


def core_fields(p, x, y, core_coefficients=None):
    p = np.asarray(p)
    block = e.a.Raw24(np.asarray(x), np.asarray(y))
    mats, strain = block.data(p[0])
    c = block.coefficients(p) if core_coefficients is None else np.asarray(core_coefficients)
    ff = {key:e.a.dot(value, c) for key, value in mats.items()}
    ff['q'] = e.a.dot(mats['ratio']-strain[None, :], c)
    return ff


def total_fields(p, extra, modes, x, y, core_coefficients=None):
    x, y = np.asarray(x, dtype=float).ravel(), np.asarray(y, dtype=float).ravel()
    result = {k:np.empty(len(x)) for k in KEYS+('q',)}
    active = np.flatnonzero(np.asarray(extra) != 0)
    for lo in range(0, len(x), 1024):
        hi = min(len(x), lo+1024)
        ff = core_fields(p, x[lo:hi], y[lo:hi], core_coefficients)
        if len(active):
            for start in range(0, len(active), 64):
                inds = active[start:start+64]
                values = evaluate_modes(x[lo:hi], y[lo:hi], float(p[0]), [modes[i] for i in inds])
                for key in KEYS: ff[key] += values[key]@np.asarray(extra)[inds]
                ff['q'] += values['ratio']@np.asarray(extra)[inds]
        for key in result: result[key][lo:hi] = ff[key]
    return result


def total_fields_saved(candidate, x, y):
    p = candidate.get('core_parameters', [candidate['cl']]+candidate['coefficients'][1:])
    return total_fields(np.asarray(p), np.asarray(candidate.get('extra_coefficients', [])),
                        candidate.get('modes', []), x, y, candidate['coefficients'])


def residual_from_fields(p, ff, x, y, root, derivatives=None):
    wx, wy = p[0]*x-ff['psiy'], p[0]*y+ff['psix']
    a, b, c = wx*ff['fx'], wy*ff['fy'], ff['q']*ff['f']
    w = (1+x*x+y*y)**((1/p[0]-1)/2)
    den = np.sqrt(a*a+b*b+c*c+(1e-8*w)**2)
    raw = (a+b+c)/den
    if derivatives is None: return root*raw
    d = derivatives
    da = wx[:,None]*d['fx']-ff['fx'][:,None]*d['psiy']
    db = wy[:,None]*d['fy']+ff['fy'][:,None]*d['psix']
    dc = ff['q'][:,None]*d['f']+ff['f'][:,None]*d.get('q', d['ratio'])
    result = root[:,None]*((da+db+dc)/den[:,None]
            -raw[:,None]*(a[:,None]*da+b[:,None]*db+c[:,None]*dc)/den[:,None]**2)
    return result


def _basis_job(args):
    x, y, cl, modes = args
    values, derivatives = evaluate_modes(x, y, cl, modes, cl_derivative=True)
    return ({key:values[key] for key in FIT_KEYS},
            {key:derivatives[key] for key in FIT_KEYS})


class SpectralProblem:
    """Blocked field cache, coefficient-analytic J/Jv/JT and native-cl FD.

    Full Jacobians are allocated only for the current model; none are saved
    per trial. LSMR uses the matrix through products, avoiding normal equations.
    """
    def __init__(self, modes, n=97, workers=1):
        self.modes, self.n, self.workers = list(modes), n, workers
        self.original = e.GridProblem(n)
        self.x, self.y, self.root = self.original.x, self.original.y, self.original.root
        self.cache_cl = None; self.extra_matrices = None; self.extra_cl_matrices = None
        self.fun_calls = self.jac_calls = self.cache_calls = 0

    def basis(self, cl):
        if self.cache_cl == float(cl): return self.extra_matrices
        began = time.time()
        columns = len(self.modes)
        values = {key:np.empty((len(self.x), columns)) for key in FIT_KEYS}
        derivatives = {key:np.empty((len(self.x), columns)) for key in FIT_KEYS}
        jobs = [(self.x, self.y, float(cl), self.modes[lo:lo+32])
                for lo in range(0, columns, 32)]
        if self.workers == 1:
            iterator = map(_basis_job, jobs)
            for lo, result in zip(range(0, columns, 32), iterator):
                for target, source in zip((values, derivatives), result):
                    for key in target: target[key][:,lo:lo+source[key].shape[1]] = source[key]
        else:
            with ProcessPoolExecutor(max_workers=self.workers, mp_context=mp.get_context('spawn')) as pool:
                for lo, result in zip(range(0, columns, 32), pool.map(_basis_job, jobs)):
                    for target, source in zip((values, derivatives), result):
                        for key in target: target[key][:,lo:lo+source[key].shape[1]] = source[key]
        self.cache_cl, self.extra_matrices = float(cl), values
        self.extra_cl_matrices = derivatives
        self.cache_calls += 1
        self.last_basis_seconds = time.time()-began
        return values

    def fields(self, p, extra):
        ff = {key:np.empty(len(self.x)) for key in FIT_KEYS+('q',)}
        for lo in range(0, len(self.x), self.original.batch):
            hi = min(len(self.x),lo+self.original.batch)
            core = core_fields(p,self.x[lo:hi],self.y[lo:hi])
            for key in ff: ff[key][lo:hi] = core[key]
        if np.any(extra):
            values = self.basis(p[0])
            for key in FIT_KEYS: ff[key] += values[key]@extra
            ff['q'] += values['ratio']@extra
        return ff

    def fun(self,p,extra):
        self.fun_calls += 1
        if not np.any(extra): return self.original.fun(p)
        return residual_from_fields(p,self.fields(p,extra),self.x,self.y,self.root)

    def jacobian(self,p,extra):
        self.jac_calls += 1
        # Precompute new coefficient fields at the exact current cl.
        values = self.basis(p[0]); ff = self.fields(p,extra)
        j = np.empty((len(self.x),24+len(extra)))
        for lo in range(0,len(self.x),self.original.batch):
            hi=min(len(self.x),lo+self.original.batch)
            block=e.a.Raw24(self.x[lo:hi],self.y[lo:hi]);mats,strain=block.data(p[0])
            d={k:m[:,1:]-m[:,:1]*strain[None,1:]/strain[0] for k,m in mats.items()}
            qm=mats['ratio']-strain[None,:]
            d['q']=qm[:,1:]-qm[:,:1]*strain[None,1:]/strain[0]
            f={k:v[lo:hi] for k,v in ff.items()}
            j[lo:hi,1:24]=residual_from_fields(p,f,self.x[lo:hi],self.y[lo:hi],self.root[lo:hi],d)
            d={k:v[lo:hi] for k,v in values.items()}
            j[lo:hi,24:]=residual_from_fields(p,f,self.x[lo:hi],self.y[lo:hi],self.root[lo:hi],d)
        # Four-point native core FIELD derivatives preserve rounded exponents
        # and c0. New-mode cl derivatives are analytic, including all spatial
        # derivative factors. Explicit cl transport and denominator dependence
        # are then differentiated by the chain rule.
        h=e.v.CL_STEP*max(1,abs(p[0]))
        for lo in range(0,len(self.x),self.original.batch):
            hi=min(len(self.x),lo+self.original.batch); xx=self.x[lo:hi];yy=self.y[lo:hi]
            probes=[]
            for factor in [2,1,-1,-2]:
                pp=p.copy();pp[0]+=factor*h; probes.append(core_fields(pp,xx,yy))
            d={key:(-probes[0][key]+8*probes[1][key]-8*probes[2][key]+probes[3][key])/(12*h)
               for key in FIT_KEYS+('q',)}
            for key in FIT_KEYS: d[key] += self.extra_cl_matrices[key][lo:hi]@extra
            d['q'] += self.extra_cl_matrices['ratio'][lo:hi]@extra
            f={key:value[lo:hi] for key,value in ff.items()}
            wx,wy=p[0]*xx-f['psiy'],p[0]*yy+f['psix']
            a,b,c=wx*f['fx'],wy*f['fy'],f['q']*f['f']
            da=(xx-d['psiy'])*f['fx']+wx*d['fx']
            db=(yy+d['psix'])*f['fy']+wy*d['fy']
            dc=d['q']*f['f']+f['q']*d['f']
            w=(1+xx*xx+yy*yy)**((1/p[0]-1)/2)
            den=np.sqrt(a*a+b*b+c*c+(1e-8*w)**2); raw=(a+b+c)/den
            dw=w*(-np.log1p(xx*xx+yy*yy)/(2*p[0]**2))
            j[lo:hi,0]=self.root[lo:hi]*((da+db+dc)/den-raw*(a*da+b*db+c*dc+1e-16*w*dw)/den**2)
        return j


def objective_saved(candidate,n=97):
    prob=e.GridProblem(n)
    ff=total_fields_saved(candidate,prob.x,prob.y)
    p=np.asarray(candidate.get('core_parameters',[candidate['cl']]+candidate['coefficients'][1:]))
    r=residual_from_fields(p,ff,prob.x,prob.y,prob.root)
    return objectives(r,n)
