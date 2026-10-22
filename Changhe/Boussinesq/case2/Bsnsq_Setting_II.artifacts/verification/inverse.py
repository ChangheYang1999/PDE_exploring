"""Independent whole-plane Biot-Savart quadrature, written by the independent verifier.

No fitting code or inherited verifier code is imported. The physical-space
integral is centered separately at each target. Antipodal pairing uses the
A2 consequence omega(-X)=omega(X) to cancel the nonintegrable leading tail.
"""
from dataclasses import dataclass
import numpy as np
from numpy.polynomial.legendre import leggauss

@dataclass(frozen=True)
class Quadrature:
    radial_order: int = 128
    angular_order: int = 256
    tail_power: float = 0.5
    radial_scale: float = 1.0
    stable_tail: bool = True

    def nodes(self):
        z, w = leggauss(self.radial_order)
        t, wt = (z + 1) / 2, w / 2
        a = 1 / self.tail_power
        lr = np.log(self.radial_scale) + a * (np.log(t) - np.log1p(-t))
        r = np.exp(lr)
        wr = wt * a * r / (t * (1-t))
        phi = np.pi * (np.arange(self.angular_order) + 0.5) / self.angular_order
        return r, wr, phi


def paired_difference(omega, centers, target, radii, stable=True):
    """Return omega(center+target)-omega(center-target), with stable far tail.

    Beyond r=1e5*max(1,|target|), a sixth-order numerical directional
    derivative replaces the pair. The discarded cubic term is not a
    rigorous error bound; stability must be measured by refinement.
    """
    target = np.asarray(target, dtype=float)
    norm = np.linalg.norm(target)
    if norm == 0:
        return np.zeros(centers.shape[:-1])
    out = omega(centers + target) - omega(centers - target)
    if not stable:
        return out
    use = radii > 1e5 * max(1.0, norm)
    if np.any(use):
        c = centers[use]
        h = 1e-3 * radii[use]
        direction = target / norm
        deriv = np.zeros(c.shape[:-1])
        for j, coeff in [(1, 3/4), (2, -3/20), (3, 1/60)]:
            shift = j * h[:, None, None] * direction
            deriv += coeff * (omega(c + shift) - omega(c - shift))
        deriv /= h[:, None]
        out[use] = 2 * norm * deriv
    return out


def velocity(omega, targets, config=Quadrature()):
    """U = (1/2pi) int J(Y-X) |Y-X|^-2 omega(Y) dY on R^2.

    omega must accept (...,2) arrays and have odd parity in each coordinate.
    Target-centered polar coordinates remove the weak singularity exactly.
    No finite-domain boundary condition or harmonic field is supplied.
    """
    targets = np.atleast_2d(np.asarray(targets, dtype=float))
    r, wr, phi = config.nodes()
    e = np.stack([np.cos(phi), np.sin(phi)], axis=-1)
    je = np.stack([-e[:, 1], e[:, 0]], axis=-1)
    centers = r[:, None, None] * e[None, :, :]
    results = []
    for target in targets:
        paired = paired_difference(omega, centers, target, r, config.stable_tail)
        angular = paired @ je / (2 * config.angular_order)
        results.append(wr @ angular)
    return np.asarray(results)


def center_strain(omega, config=Quadrature()):
    """Psi_xy(0) = 1/pi int Y1 Y2 omega(Y)/|Y|^4 dY.

    The same compact radial rule is applied directly at the center, with
    quadrant Gauss-Legendre angular integration, rather than differentiating U.
    """
    r, wr, _ = config.nodes()
    z, w = leggauss(config.angular_order)
    phi, wphi = np.pi * (z+1) / 4, np.pi * w / 4
    e = np.stack([np.cos(phi), np.sin(phi)], axis=-1)
    field = omega(r[:, None, None] * e[None, :, :])
    return (4/np.pi) * np.sum((wr/r)[:, None] * wphi[None, :]
                            * (e[:, 0]*e[:, 1])[None, :] * field)

@dataclass(frozen=True)
class PanelQuadrature:
    """Target-aware physical-space panels, retaining an infinite radial map.

    Panels resolve the source origin when it is far from the target. Each
    angular panel uses Gauss-Legendre nodes, a different rule from midpoint
    Fourier sampling. core_scale controls quadrature resolution, not a wall.
    """
    order: int = 12
    tail_power: float = 0.5
    radial_scale: float = 1.0
    core_scale: float = 1.0
    stable_tail: bool = True

    def for_target(self,target):
        target=np.asarray(target,float)
        distance=np.linalg.norm(target)
        z,w=leggauss(self.order)
        tb=list(np.linspace(0,1,9))
        if distance>2*self.core_scale:
            offsets=self.core_scale*np.array([-16,-8,-4,-2,-1,-.5,0,.5,1,2,4,8,16])
            rb=distance+offsets
            rb=rb[rb>0]
            value=(rb/self.radial_scale)**self.tail_power
            tb.extend(value/(1+value))
        tb=np.unique(tb)
        t=np.concatenate([(b+a)/2+(b-a)*z/2 for a,b in zip(tb[:-1],tb[1:])])
        wt=np.concatenate([(b-a)*w/2 for a,b in zip(tb[:-1],tb[1:])])
        a=1/self.tail_power
        r=self.radial_scale*np.exp(a*(np.log(t)-np.log1p(-t)))
        wr=wt*a*r/(t*(1-t))
        pb=list(np.linspace(0,np.pi,13))
        if distance>2*self.core_scale:
            center=np.arctan2(target[1],target[0])%np.pi
            widths=np.arctan(self.core_scale*np.array([.25,.5,1,2,4,8,16])/distance)
            pb.extend([center])
            pb.extend((center+widths).tolist());pb.extend((center-widths).tolist())
        pb.extend((np.pi-np.asarray(pb)).tolist())
        pb=np.unique(np.clip(pb,0,np.pi))
        phi=np.concatenate([(b+a)/2+(b-a)*z/2 for a,b in zip(pb[:-1],pb[1:])])
        wp=np.concatenate([(b-a)*w/2 for a,b in zip(pb[:-1],pb[1:])])
        return r,wr,phi,wp


def velocity_panels(omega,targets,config=PanelQuadrature()):
    targets=np.atleast_2d(np.asarray(targets,float))
    results=[]
    for target in targets:
        r,wr,phi,wp=config.for_target(target)
        e=np.stack([np.cos(phi),np.sin(phi)],axis=-1)
        je=np.stack([-e[:,1],e[:,0]],axis=-1)
        centers=r[:,None,None]*e[None,:,:]
        paired=paired_difference(omega,centers,target,r,config.stable_tail)
        angular=(paired*wp[None,:])@je/(2*np.pi)
        results.append(wr@angular)
    return np.asarray(results)
