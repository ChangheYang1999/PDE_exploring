"""Portable resource decisions. This module does not collect OS telemetry."""
from dataclasses import asdict, dataclass, fields
import math


@dataclass(frozen=True)
class Policy:
    max_family_rss_mib: float = 2048.0
    min_available_mib: float = 4096.0
    min_available_pct: float = 20.0
    max_load_per_cpu: float = 1.5
    min_disk_free_gib: float = 10.0
    max_seconds: float = 600.0
    max_session_seconds: float = 3600.0
    sample_seconds: float = 1.0
    terminate_grace_seconds: float = 10.0
    max_pageout_mib_s: float = 8.0
    max_swapout_mib_s: float = 8.0
    max_swap_growth_mib: float = 512.0
    max_memory_psi_full_avg10: float = 5.0
    max_temperature_c: float = 95.0
    nice_increment: int = 15
    blas_threads: int = 1

    def __post_init__(self):
        for field in fields(self):
            value = getattr(self, field.name)
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
                raise ValueError('%s must be a finite positive number' % field.name)
        if self.min_available_pct > 100:
            raise ValueError('min_available_pct must be <= 100')
        if not isinstance(self.nice_increment, int) or not 1 <= self.nice_increment <= 19:
            raise ValueError('nice_increment must be an integer from 1 through 19')
        if self.blas_threads != 1:
            raise ValueError('one BLAS/OpenMP thread is required; blas_threads must be 1')
        if self.max_seconds > self.max_session_seconds:
            raise ValueError('max_seconds cannot exceed max_session_seconds')

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, values):
        unknown = set(values) - {field.name for field in fields(cls)}
        if unknown:
            raise ValueError('unknown policy settings: ' + ', '.join(sorted(unknown)))
        return cls(**values)


def evaluate(current, baseline, previous, policy, elapsed=0.0, session_seconds=0.0):
    """Return reasons to stop; missing mandatory telemetry fails closed.

    Allocated swap alone is not paging activity and does not establish that a
    worker caused memory pressure. A growth threshold stops only with reduced
    headroom. Paging and PSI describe system-wide contention, not attribution.
    """
    reasons, warnings, rates = [], [], {}
    required = ('family_rss_mib', 'available_mib', 'available_pct',
                'load_per_cpu', 'disk_free_gib', 'swap_used_mib')
    for key in required:
        value = current.get(key)
        if value is None or not isinstance(value, (int, float)) or not math.isfinite(value):
            reasons.append('required telemetry unavailable: ' + key)
    if reasons:
        return {'stop': True, 'reasons': reasons, 'warnings': warnings, 'rates': rates}
    comparisons = (
        ('family_rss_mib', policy.max_family_rss_mib, 'above', 'process-family RSS ceiling'),
        ('available_mib', policy.min_available_mib, 'below', 'available physical memory floor'),
        ('available_pct', policy.min_available_pct, 'below', 'available physical memory percentage floor'),
        ('load_per_cpu', policy.max_load_per_cpu, 'above', 'CPU load per logical CPU ceiling'),
        ('disk_free_gib', policy.min_disk_free_gib, 'below', 'disk capacity floor'),
    )
    for key, threshold, direction, reason in comparisons:
        if (current[key] > threshold if direction == 'above' else current[key] < threshold):
            reasons.append(reason)
    if elapsed >= policy.max_seconds:
        reasons.append('per-run wall-time budget exhausted')
    if session_seconds + elapsed >= policy.max_session_seconds:
        reasons.append('cumulative session wall-time budget exhausted')
    psi = current.get('memory_psi_full_avg10')
    if psi is not None and psi > policy.max_memory_psi_full_avg10:
        reasons.append('Linux memory PSI full pressure ceiling')
    pressure = current.get('memory_pressure_level')
    if pressure in ('critical', 'warning'):
        reasons.append('OS memory pressure level: ' + pressure)
    temperature = current.get('temperature_c')
    if temperature is not None and temperature >= policy.max_temperature_c:
        reasons.append('reported temperature ceiling')
    if current.get('thermal_warning'):
        reasons.append('OS thermal/performance warning')
    growth = current['swap_used_mib'] - baseline.get('swap_used_mib', current['swap_used_mib'])
    rates['session_swap_growth_mib'] = growth
    if growth >= policy.max_swap_growth_mib:
        warnings.append('system allocated swap increased; this is not worker attribution')
        if current['available_pct'] < max(policy.min_available_pct + 10.0, baseline.get('available_pct', 0) - 5.0):
            reasons.append('swap growth with deteriorating memory headroom')
    if previous:
        dt = current['monotonic_seconds'] - previous['monotonic_seconds']
        if dt > 0:
            for key, threshold in (('pageout_mib', policy.max_pageout_mib_s), ('swapout_mib', policy.max_swapout_mib_s)):
                now, before = current.get(key), previous.get(key)
                if now is not None and before is not None:
                    rate = max(0.0, now - before) / dt
                    rates[key + '_s'] = rate
                    if rate > threshold:
                        if key == 'pageout_mib' and current.get('pageout_semantics', '').startswith('Linux') and current['available_pct'] >= policy.min_available_pct + 10 and (current.get('memory_psi_full_avg10') or 0) <= policy.max_memory_psi_full_avg10:
                            warnings.append('Linux block paging/writeback elevated with good memory headroom')
                        else:
                            reasons.append('system ' + key.replace('_mib', '') + ' rate ceiling')
            for key in ('cgroup_oom', 'cgroup_oom_kill'):
                if current.get(key) is not None and previous.get(key) is not None and current[key] > previous[key]:
                    reasons.append('cgroup memory event: ' + key)
    return {'stop': bool(reasons), 'reasons': reasons, 'warnings': warnings, 'rates': rates}
