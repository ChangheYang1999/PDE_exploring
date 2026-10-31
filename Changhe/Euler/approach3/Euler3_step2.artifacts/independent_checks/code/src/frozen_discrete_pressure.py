"""Independent extended contractions of explicitly exported fixed kernel constants.

This intentionally preserves the production radial interpolation and kernel
entries, whose accuracy is not independently established by this class.
"""
import numpy as np

class FrozenDiscretePressure:
    def __init__(self,data,dtype=np.longdouble):
        self.D=dtype;self.a={k:np.asarray(v,dtype=dtype) for k,v in data.items() if k.startswith('pressure_')}
        self.r=np.asarray(data['radii'],dtype=dtype);self.n=np.asarray(data['directions'],dtype=dtype)
        self.labels=np.asarray(data['pressure_modes'],dtype=int);self.partner=np.asarray(data['pressure_partner'],dtype=int)
        self.ell=self.labels[:,0];self.m=self.labels[:,1];self.sign=self.a['pressure_sign']
        self.qc=self.a['pressure_Qc'][self.ell,self.m];self.qs=self.a['pressure_Qs'][self.ell,self.m]
        self.ns=self.a['pressure_sfac'].size
    def coefficients(self,source):
        a=self.a;f=np.asarray(source,dtype=self.D)[:self.ns];flm=f@a['pressure_A0pw']
        ftw=(flm*a['pressure_cosb']-self.sign[None,:]*flm[:,self.partner]*a['pressure_sinb'])*a['pressure_sfac'][:,None]*a['pressure_lfac']
        t=[]
        for k in range(2):
            t.append(np.einsum('qrk,kq->rq',self.qc[:,k],ftw)+self.sign[None,:]*np.einsum('qrk,kq->rq',self.qs[:,k],ftw[:,self.partner]))
        p=t[0]+t[1];dp=(-(self.ell+1)[None,:]*t[0]+self.ell[None,:]*t[1])/self.r[:,None]
        return p,dp,flm,ftw
    def values(self,source):
        p,dp,flm,ftw=self.coefficients(source);a=self.a
        pv=p@a['pressure_A0p'].T
        radial=(dp-self.ell[None,:]*p/self.r[:,None])@a['pressure_A0p'].T
        gp=radial[:,:,None]*self.n[None,:,:]+np.einsum('rq,iaq->rai',p/self.r[:,None],a['pressure_A1p'])
        return pv,gp,{'p_lm':p,'dp_lm':dp,'f_lm':flm,'f_tw':ftw}
