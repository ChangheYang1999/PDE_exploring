"""Posthoc, read-only authentication of completed D evidence. Standard library only.

No policy, Engine, replay, checker or subprocess is imported or executed. This is
not part of the original declaration. Run only after the parent authorizes the
completed campaign and its post-D checks. Reports are written only below HERE.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from copy import deepcopy
from datetime import datetime, timezone
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
A = E / 'analysis/terminal_reserved_validation'
HERE = E / 'reviews/terminal_final_independent_001'
DECL = E / 'terminal-candidate-declaration-001.json'
DECL_SHA = '2b5fa9c56b6219233731c8559b012ff12ebe0be43b86395ebee4e51b8fa325e1'
CANDIDATE_SHA = '70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87'
MANIFEST_SHA = '9267cb4367f21dc0a572594c3523a466769ef1ea3185beb4dd94d632270e07b7'
GATE = datetime.fromisoformat('2026-10-31T23:00:00+00:00')
CORE = {'td_game/engine.py', 'td_game/combat.py', 'td_game/actions.py',
        'td_game/config.py', 'td_game/state.py', 'td_game/pathfinding.py',
        'td_game/balanced.json', 'td_bots/protocol.py',
        'bot_research/experiments/validation/evaluate.py'}


def now():
    return datetime.now(timezone.utc).isoformat()


def require(value, label):
    if not value:
        raise ValueError(label)


def path(value):
    p = Path(value)
    require(not p.is_absolute() and '..' not in p.parts and bool(p.parts), 'Nonrelative input path')
    require(p.parts[0] in ('bot_research', 'td_game', 'td_bots', 'configs'), 'Input outside permitted evidence/source roots')
    return p


def reject_constant(value):
    raise ValueError('Nonfinite JSON constant: ' + value)


def unique_object(pairs):
    out = {}
    for k, v in pairs:
        require(k not in out, 'Duplicate JSON object key: ' + k)
        out[k] = v
    return out


def parse(raw):
    return json.loads(raw, object_pairs_hook=unique_object, parse_constant=reject_constant)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def stamp(value):
    d = datetime.fromisoformat(value)
    require(d.tzinfo is not None, 'Timestamp lacks timezone')
    return d


class Reader:
    def __init__(self):
        self.inputs = {}
        self.issues = []
        self.sections = []
        self.facts = {}
        self.hash_cache = {}
        self.started = time.monotonic()

    def digest(self, value, expected=None):
        p = path(value)
        require(time.monotonic() - self.started < 550, 'Independent reader exceeded 550 second limit')
        stat = p.stat()
        key = (str(p), stat.st_size, stat.st_mtime_ns)
        h = self.hash_cache.get(key)
        if h is None:
            h = hashlib.sha256()
            with p.open('rb') as f:
                for block in iter(lambda: f.read(1024 * 1024), b''):
                    h.update(block)
            h = h.hexdigest()
            self.hash_cache[key] = h
        require(str(p) not in self.inputs or self.inputs[str(p)] == h, 'Input changed during independent read: ' + str(p))
        self.inputs[str(p)] = h
        if expected is not None:
            require(h == expected, 'SHA256 mismatch: ' + str(p))
        return h

    def read(self, value):
        p = path(value)
        self.digest(p)
        raw = p.read_bytes()
        require(hashlib.sha256(raw).hexdigest() == self.inputs[str(p)], 'Input changed while loading: ' + str(p))
        return parse(raw)

    def maps(self, mapping):
        require(isinstance(mapping, dict) and bool(mapping), 'Missing nonempty hash map')
        for p, h in mapping.items():
            self.digest(p, h)

    def section(self, label, function):
        try:
            result = function()
            self.sections.append({'section': label, 'status': 'CONFIRMED'})
            return result
        except (OSError, ValueError, KeyError, TypeError, IndexError, OverflowError) as exc:
            # Never retain an absolute path from an OSError or a traceback.
            message = str(exc) if isinstance(exc, (ValueError, KeyError)) else type(exc).__name__
            if any('/' + root + '/' in message for root in ('mnt', 'home', 'tmp', 'efs')):
                message = type(exc).__name__ + ': local path omitted'
            item = {'section': label, 'diagnostic': message}
            self.issues.append(item)
            self.sections.append({'section': label, 'status': 'OPEN', 'diagnostic': message})
            return None


def declared_jobs(d, manifest, campaign):
    """Independent literal reconstruction from the declared data, after execution gate."""
    require(manifest['pool'] == 'D' and manifest['planned_conditions'] == 96, 'Manifest pool/count')
    opponents = [{'profile': p} for p in manifest['profiles']] + [{'spec': s} for s in manifest['factory_specs']]
    require(len(opponents) == 16 and len(manifest['scenarios']) == 2, 'Expected 16 opponents and two prefixes')
    result = []
    for scenario in [None] + manifest['scenarios']:
        name = 'standard' if scenario is None else scenario['name']
        for index, opponent in enumerate(opponents):
            for side in (0, 1):
                ident = f'{name}-{index:02d}-side{side}'
                bots = [{'spec': d['candidate']}, deepcopy(opponent)]
                names = [d['candidate'], f'holdout_D_{index:02d}']
                if side:
                    bots.reverse()
                    names.reverse()
                cond = dict(scenario=name, candidate_side=side, opponent=deepcopy(opponent),
                            engine_seed=None, pool='D', strength_score_eligible=scenario is None,
                            initial_state='standard' if scenario is None else 'candidate-relative legal prescribed prefix')
                job = dict(id=ident, names=names, bots=bots, condition=cond,
                           replay_path=str(campaign / 'replays' / (ident + '.jsonl')))
                if scenario is not None:
                    prefixes = deepcopy(scenario['prefixes'])
                    require(len(prefixes) == 2 and all(isinstance(p, list) for p in prefixes), 'Prefix schema')
                    job['prefixes'] = prefixes if side == 0 else list(reversed(prefixes))
                    cond['prefix_lengths_candidate_first'] = list(map(len, prefixes))
                    cond['prefix_policy_calls'] = 'skipped'
                result.append(job)
    require(len({j['id'] for j in result}) == 96, 'Repeated declared job ID')
    require(len({(j['condition']['scenario'], canonical(j['condition']['opponent']), j['condition']['candidate_side']) for j in result}) == 96, 'Repeated declared condition')
    return result


def source_and_selection(r, args):
    r.digest(DECL, DECL_SHA)
    d = r.read(DECL)
    require(d['candidate'] == 'bot_research.bots.best:decide' and d['candidate_sha256'] == CANDIDATE_SHA, 'Selected candidate identity')
    require(d['manifest_sha256'] == MANIFEST_SHA and d['expected_conditions'] == 96, 'Manifest identity/count')
    require(len(d['source_sha256']) == 85 and d['candidate_and_opponent_calls'] == 0, 'Original declaration scope')
    r.maps(d['source_sha256'])
    r.digest(d['selection_record'], d['selection_record_sha256'])
    require(d['selection_excerpt'] in path(d['selection_record']).read_text(), 'Archived selection quotation missing')
    require(stamp(d['selection_time_utc']) <= stamp(d['time_utc']) < GATE == stamp(d['not_before_utc']), 'Selection/declaration/gate chronology')
    supplement_path = A / 'verification/dependency_supplement_001.json'
    s = r.read(supplement_path)
    require(s['declaration_sha256'] == DECL_SHA and s['original_declaration_source_sha256'] == d['source_sha256'], 'Supplement changed original declaration')
    require(s['original_declaration_source_count'] == 85 and len(s['source_sha256']) == 95, '85 original / 95 later pins')
    require(s['candidate_sha256'] == CANDIDATE_SHA and s['manifest_sha256'] == MANIFEST_SHA, 'Supplement candidate/manifest')
    require(stamp(s['started_utc']) <= stamp(s['sealed_utc']) < GATE, 'Supplement was not separately sealed before gate')
    require(s['policy_calls'] == s['game_calls'] == 0 and not s['reserved_parameters_parsed'], 'Supplement call scope')
    r.maps(s['source_sha256'])
    require(all(s['source_sha256'].get(p) == h for p, h in d['source_sha256'].items()), 'Supplement original pins changed')
    added = set(s['source_sha256']) - set(d['source_sha256'])
    require(added == set(s['newly_covered_files']) == set(s['source_archive']) and len(added) == 10, 'Supplement added archive coverage')
    for p, archive in s['source_archive'].items():
        r.digest(archive, s['source_sha256'][p])
    require(set(s['input_archive']) == set(s['input_sha256']), 'Supplement supporting archive coverage')
    for p, h in s['input_sha256'].items():
        r.digest(p, h)
        r.digest(s['input_archive'][p], h)
    for identity in s['earlier_source_identities']:
        r.digest(identity['earlier_receipt'], identity['earlier_receipt_sha256'])
        earlier = r.read(identity['earlier_receipt'])
        require(earlier[identity['map_field']][identity['source']] == identity['earlier_source_sha256'], 'Earlier receipt source pin differs')
        require(stamp(earlier['started_utc']) == stamp(identity['recorded_utc']) < GATE, 'Earlier receipt chronology')
        if identity['original_archive_verified']:
            r.digest(identity['original_archive'], identity['earlier_source_sha256'])
        require(identity['same_bytes'] and identity['earlier_source_sha256'] == identity['current_sha256'] == s['source_sha256'][identity['source']], 'Earlier source identity mismatch')
    pre, post = r.read(args.supplement_pre), r.read(args.supplement_post)
    for phase, record in [('pre-d', pre), ('post-d', post)]:
        require(record['phase'] == phase and record['all_passed'] and not record['issues'], 'Supplement verification failed')
        require(record['seal_sha256'] == r.digest(supplement_path) and record['declaration_sha256'] == DECL_SHA, 'Supplement verification binding')
        require(record['source_files_verified'] == 95 and record['original_pins_verified'] == 85, 'Verification pin counts')
        require(record['policy_calls'] == record['game_calls'] == 0 and not record['reserved_parameters_parsed'], 'Verification call scope')
        r.digest(E / 'terminal_dependency_supplement.py', record['verifier_sha256'])
    require(stamp(s['sealed_utc']) <= stamp(pre['time_utc']) < GATE <= stamp(post['time_utc']), 'Pre/post source verification chronology')
    r.facts['provenance'] = dict(original_declaration_utc=d['time_utc'], source_pins_original=85,
        supplemental_seal_utc=s['sealed_utc'], source_pins_after_supplement=95,
        additional_archived_files=10, earlier_identity_count=len(s['earlier_source_identities']),
        no_selected_earlier_pin=s['files_without_selected_earlier_pin'], post_source_check_utc=post['time_utc'],
        limit='Earlier receipts bind recorded bytes, not continuous historical monitoring. The supplemental seal is later than declaration001.')
    return d, s, post


def primary_case(r, job, case, freeze):
    require(case['condition'] == job['condition'] and case['job'] == job['id'] and case['status'] == 'valid', 'Primary condition binding')
    row = r.read(case['result_path'])
    require(row['condition'] == job['condition'] and row['bot_specs'] == job['names'], 'Result job binding')
    require(row['replay_path'] == job['replay_path'] == case['replay_path'], 'Primary replay location')
    require(not any(row['bot_errors']) and not any(row['rejected_actions']) and not row['source_changed_during_match'], 'Primary policy error/rejection/drift')
    required = set(CORE)
    for bot in job['bots']:
        module = bot['spec'].partition(':')[0] if 'spec' in bot else 'bot_research.bots.counters.archetypes'
        source = module.replace('.', '/') + '.py'
        if source not in freeze['source_sha256']:
            source = module.replace('.', '/') + '/__init__.py'
        required.add(source)
    for key in ('source_sha256', 'source_sha256_at_end'):
        loaded = row[key]
        require(required <= set(loaded) and all(freeze['source_sha256'].get(p) == h for p, h in loaded.items()), 'Loaded source attestation incomplete or unsealed')
    n = row['rounds']
    require(type(n) is int and 0 < n <= 50, 'Primary round range')
    r.digest(row['replay_path'], row['trajectory_sha256'])
    records = [parse(line) for line in path(row['replay_path']).read_bytes().splitlines()]
    require(len(records) == 2 * (n + 1), 'Truncated or extra primary records')
    require([(x['round'], x['player']) for x in records] == [(turn, side) for turn in range(n + 1) for side in (0, 1)], 'Record order or boundary')
    require(all(x['result'] == row['result'] for x in records[-2:]), 'Final result/log disagreement')
    require([x['snapshot']['hp'] for x in records[-2:]] == row['hp'], 'Final HP/log disagreement')
    require(all(not x.get('result') for x in records[:-2]), 'History continues after a terminal record')
    raw = ''.join(canonical(x) + '\n' for x in records).encode()
    require(hashlib.sha256(raw).hexdigest() == row['trajectory_sha256'], 'Canonical full log bytes')
    accepted = [Counter(), Counter()]
    for turn in range(1, n + 1):
        for side in (0, 1):
            events = records[2 * turn + side]['event']
            require(not any(x['kind'] == 'bot_error' for x in events), 'Bot error omitted from result')
            actions = [x['action'] for x in events if x['kind'] == 'action']
            for x in events:
                if x['kind'] == 'action':
                    require(x['accepted'], 'Rejected action omitted from result')
                    accepted[side][x['action']['op'] + ':' + x['action'].get('type', '')] += 1
            prefix = job.get('prefixes', [[], []])[side]
            if turn <= len(prefix):
                require(actions == prefix[turn - 1], 'Recorded prescribed prefix changed')
    require(row['accepted_actions'] == [dict(x) for x in accepted], 'Accepted totals differ from logs')
    history = []
    for turn in range(1, n + 1):
        players = []
        for side in (0, 1):
            rec = records[2 * turn + side]; snap = rec['snapshot']
            item = {k: snap[k] for k in ('hp', 'gold', 'n_factories', 'n_turrets', 'n_walls', 'length_path')}
            item['roster'] = dict(Counter(x['type'] for x in snap['roster']))
            for kind in ('combat', 'income'):
                events = [x for x in rec['event'] if x['kind'] == kind]
                require(len(events) == 1, 'Missing/duplicate combat or income event')
                item[kind] = events[0]
            players.append(item)
        history.append(dict(round=turn, players=players))
    require(row['history'] == history, 'Result abbreviated history differs from full logs')
    require(all(rec['match']['rules'] == row['rules'] and rec['match']['bots'] == row['bot_specs'] for rec in records[:2]), 'Initial metadata rules/bot binding')
    side = job['condition']['candidate_side']
    outcome = 'D' if row['result']['winner'] is None else ('W' if row['result']['winner'] == side else 'L')
    require(case['outcome'] == row['candidate_outcome'] == outcome, 'Perspective outcome mismatch')
    hp = row['hp'][::1 if side == 0 else -1]
    require(case['hp_candidate_first'] == hp and case['rounds'] == n, 'Primary HP/round summary')
    require(row['hp_difference_p0'] == row['hp'][0] - row['hp'][1], 'Physical HP difference')
    require(case['runtime_seconds'] == row['runtime_seconds'] and case['completed_utc'] == row['time_utc'], 'Timing summary binding')
    require(stamp(row['time_utc']) >= stamp(freeze['started_utc']), 'Completion before campaign')
    for timing in row['decision_seconds']:
        require(timing['calls'] == n and all(math.isfinite(timing[k]) and timing[k] >= 0 for k in ('max', 'total')), 'Wrapper timings/calls invalid')
        require(timing['max'] <= timing['total'] + 1e-12, 'Wrapper maximum exceeds total')
    require(case['decision_seconds_candidate_first'] == row['decision_seconds'][::1 if side == 0 else -1], 'Timing seat inversion')
    normalized = deepcopy(records)
    for rec in normalized:
        rec.pop('match', None)
        rec['player'] ^= side
        rec['snapshot']['name'] = 'counter' if rec['player'] == 0 else 'opponent'
        for event in rec['event']:
            event.pop('order', None)
        if 'result' in rec and rec['result']['winner'] is not None:
            rec['result']['winner'] ^= side
    normalized.sort(key=lambda x: (x['round'], x['player']))
    require(hashlib.sha256(canonical(normalized).encode()).hexdigest() == case['canonical_replay_sha256'], 'Canonical paired trajectory mismatch')
    return row


def campaign_and_audits(r, d, supplement, post, args):
    campaign = R / d['campaign_name']
    final = r.read(A / 'verification/final_candidate.json')
    require(final['all_passed'] and final['conditions'] == 96 and final['candidate_sha256'] == CANDIDATE_SHA, 'Final candidate receipt incomplete')
    require(stamp(post['time_utc']) >= stamp(final['time_utc']), 'Post-D source check predates final publication')
    r.maps(final['input_sha256'])
    freeze, jobs, summary = (r.read(campaign / p) for p in ('freeze.json', 'jobs.json', 'summary.json'))
    require(freeze['candidate'] == d['candidate'] and freeze['candidate_sha256'] == CANDIDATE_SHA and freeze['pool'] == 'D' and freeze['stress'], 'Campaign frozen candidate/start kind')
    require(stamp(freeze['started_utc']) >= GATE and stamp(freeze['started_utc']) > stamp(d['time_utc']), 'Campaign starts before gate/declaration')
    require(freeze['manifest_sha256'] == MANIFEST_SHA, 'Campaign manifest drift')
    r.maps(freeze['source_sha256'])
    for p, h in freeze['source_sha256'].items():
        require(supplement['source_sha256'].get(p) == h, 'Campaign source absent from later pre-D seal: ' + p)
        r.digest(campaign / 'sources' / p, h)
    manifest = r.read(d['manifest'])
    r.digest(d['manifest'], MANIFEST_SHA)
    r.digest(campaign / 'sources' / d['manifest'], MANIFEST_SHA)
    require(jobs == declared_jobs(d, manifest, campaign), '96 jobs differ from declared parameters/prefixes/physical seats')
    require(summary['complete'] and summary['all_completed_successfully'] and summary['planned_conditions'] == summary['completed_conditions'] == summary['resolved_conditions'] == 96, 'Primary summary incomplete')
    require(not summary['failed_conditions'] and not summary['conditions_with_errors_or_rejections_or_drift'], 'Primary failures present')
    strict = r.read(R / (d['campaign_name'] + '-strict.json'))
    replay = r.read(R / (d['campaign_name'] + '-replay.json'))
    entry = r.read(R / (d['campaign_name'] + '-entrypoint-summary.json'))
    losses = r.read(R / (d['campaign_name'] + '-losses.json'))
    for rec in (strict, replay, entry, losses):
        r.maps(rec['input_sha256'])
    r.maps(entry['source_sha256'])
    require(strict['expected_conditions'] == strict['valid_conditions'] == 96 and not strict['unresolved'] and not strict['repeat_disagreements'], 'Strict incomplete/repeated disagreement')
    require(strict['source_archive_verified'] and strict['jobs_match_predeclared_manifest'] and not strict['current_source_drift'], 'Strict source/job check')
    require(strict['candidate'] == replay['candidate'] == final['candidate'] == d['candidate'], 'Receipt candidate spec mismatch')
    require(strict['candidate_sha256'] == replay['candidate_sha256'] == entry['candidate_sha256'] == CANDIDATE_SHA, 'Receipt candidate hash mismatch')
    cases = {c['job']: c for c in strict['cases']}
    require(len(cases) == len(strict['cases']) == 96 and set(cases) == {j['id'] for j in jobs}, 'Missing/duplicate primary case')
    require(final['cases'] == strict['cases'], 'Published condition list altered')
    actual_attempt_counts = dict(Counter(x['status'] for x in strict['attempts']))
    require(actual_attempt_counts == strict['attempt_counts'] == replay['match_attempt_counts'], 'Failure accounting mismatch')
    require(final['nonvalid_attempts'] == [x for x in strict['attempts'] if x['status'] != 'valid'], 'Hidden nonvalid attempts')
    # The declared fixed pipeline performs one retained attempt per condition.
    require(len(strict['attempts']) == 96 and actual_attempt_counts == {'valid': 96}, 'Separate recovery/retry campaign needs a separate independent review')
    result_files = {p.name for p in (campaign / 'results').glob('*.json')}
    require(result_files == {j['id'] + '.json' for j in jobs}, 'Extra, failed or missing primary result files')
    primary = {}
    for job in jobs:
        require(r.read(campaign / 'jobs' / (job['id'] + '.json')) == job, 'Individual job/list mismatch')
        value = r.section('primary:' + job['id'], lambda job=job: primary_case(r, job, cases[job['id']], freeze))
        if value is not None:
            primary[job['id']] = value
    require(len(primary) == 96, 'One or more primary source/log inspections failed')
    matches_path = campaign / 'matches.jsonl'
    r.digest(matches_path)
    stream = [parse(line) for line in matches_path.read_bytes().splitlines()]
    require(stream == [primary[j['id']] for j in jobs], 'Primary JSONL stream differs or omits conditions')
    require(replay['all_primary_conditions_completed_and_replayed'] and replay['verified_primary_replays'] == 96 and not replay['missing_primary_replays'] and not replay['unresolved_matches'], 'Replay coverage incomplete')
    require(entry['all_passed'] and entry['count'] == 96 and entry['groups'] == {'standard': 32, 'continuation': 64}, 'Fresh entry coverage incomplete')
    selected = {x['job']: x for x in replay['selected_replay_receipts']}
    fresh = {x['job']: x for x in entry['cases']}
    require(len(selected) == len(replay['selected_replay_receipts']) == len(fresh) == len(entry['cases']) == 96 and set(selected) == set(fresh) == set(cases), 'Audit result coverage/duplicates')
    for suffix, mode in [('-replays', 'replay'), ('-entrypoints', 'entry')]:
        auditdir = R / (d['campaign_name'] + suffix)
        bounded, meta = r.read(auditdir / 'summary.json'), r.read(auditdir / 'metadata.json')
        require(bounded['all_passed'] and bounded['counts'] == {'passed': 96} and bounded['planned_jobs'] == 96, 'Bounded audit incomplete')
        require(bounded['campaign'] == meta['campaign'] == str(campaign) and meta['shard'] == 0 and meta['shards'] == 1, 'Bounded audit campaign/shard mismatch')
        r.maps(meta['inputs'])
        failures = sorted((auditdir / 'failures').glob('*.json'))
        require(not failures, 'Bounded audit computational failures need separate recovery review')
        require({p.name for p in (auditdir / 'audits').glob('*.json')} == {j['id'] + '.json' for j in jobs}, 'Bounded audit file coverage')
        require([c['job'] for c in bounded['cases']] == [j['id'] for j in jobs], 'Bounded audit job order/coverage')
        for item in bounded['cases']:
            ident = item['job']; job = next(j for j in jobs if j['id'] == ident); original = primary[ident]
            require(item['status'] == 'passed', 'Failed bounded case')
            r.digest(item['audit_path'], item['audit_sha256'])
            audit = r.read(item['audit_path'])
            require(audit['all_passed'] and audit['count'] == len(audit['cases']) == 1 and not audit['source_changed_during_run'], 'Per-case audit failed')
            r.maps(audit['source_sha256']); r.maps(audit['input_sha256'])
            require(audit['input_sha256'].get(cases[ident]['result_path']) == r.digest(cases[ident]['result_path']), 'Audit not bound to original result')
            detail = audit['cases'][0]
            require(detail['passed'] and detail['input'] == cases[ident]['result_path'] and detail['row_index'] == 0, 'Audit selects other input/row')
            for key in ('condition', 'hp', 'result', 'rounds', 'trajectory_sha256'):
                require(detail[key] == original[key], 'Per-case audit/result mismatch: ' + key)
            log = auditdir / 'logs' / (ident + '.log')
            r.digest(log)
            require(log.stat().st_size > 0, 'Missing child diagnostic log')
            child_events = []
            for line in log.read_text().splitlines():
                try:
                    event = parse(line)
                except ValueError:
                    continue
                if isinstance(event, dict):
                    child_events.append(event)
            require(child_events and child_events[-1].get('all_passed') is True, 'Child log lacks final successful audit event')
            if mode == 'replay':
                needed_engine = {p for p in CORE if p.startswith('td_game/')}
                require(needed_engine <= set(audit['source_sha256']), 'Replay receipt omits protected engine dependencies')
                require(str(E / 'replay_audit.py') in audit['source_sha256'], 'Replay receipt omits its checker identity')
                require(detail['records'] == 2 * (original['rounds'] + 1), 'Replay terminal-boundary count')
                require(selected[ident]['audit_path'] == item['audit_path'] and selected[ident]['result_path'] == cases[ident]['result_path'] and selected[ident]['trajectory_sha256'] == original['trajectory_sha256'], 'Selected replay binding')
            else:
                require(all(audit['source_sha256'].get(p) == h for p, h in freeze['source_sha256'].items()), 'Fresh receipt omits frozen source/data identity')
                require(str(E / 'check_best_entrypoints.py') in audit['source_sha256'], 'Fresh receipt omits its checker identity')
                require(audit['candidate_module'] == 'bot_research.bots.best' and audit['candidate_sha256'] == CANDIDATE_SHA, 'Fresh entry candidate')
                require(not detail['differences'] and detail['observations_unchanged'] and detail['all_fresh_actions_legal'], 'Fresh entry mutation/illegal/different actions')
                side = job['condition']['candidate_side']; prefix = len(job.get('prefixes', [[], []])[side])
                require(detail['skipped_prefix_rounds'] == prefix and original['rounds'] >= prefix, 'Skipped prefix accounting')
                rounds = detail['entrypoint_rounds']
                require(len(rounds) == original['rounds'], 'Fresh decisions/rounds coverage')
                for turn, row in enumerate(rounds, 1):
                    require(row['round'] == turn and row['policy_invoked'] == (turn > prefix), 'Prefix counted as policy invocation')
                    require(row['direct_matches_record'] and row['factory_matches_record'] and row['entrypoints_agree'], 'Recorded/direct/factory mismatch')
                    require(all(math.isfinite(row[k]) and row[k] >= 0 for k in ('direct_seconds', 'factory_seconds')), 'Invalid fresh timing')
                expected = dict(campaign=str(campaign), job=ident, condition=job['condition'], rounds=original['rounds'], prefix_rounds=prefix, policy_rounds=original['rounds'] - prefix, audit_path=item['audit_path'], passed=True)
                require(fresh[ident] == expected, 'Fresh summary case accounting')
    require(not replay['replay_computational_failures'] and all(x['valid'] for x in replay['replay_attempts']), 'Replay failure omitted from summary')
    groups = defaultdict(list)
    for c in strict['cases']:
        groups[c['condition']['scenario']].append(c)
    require(len(groups) == 3 and 'standard' in groups and all(len(v) == 32 for v in groups.values()), 'Three groups of 32')
    metrics = {}
    for name, rows in groups.items():
        seats = [dict(Counter(c['outcome'] for c in rows if c['condition']['candidate_side'] == s)) for s in (0, 1)]
        require(all(sum(x.values()) == 16 for x in seats), 'Each group must have 16 per physical seat')
        timed = [c['decision_seconds_candidate_first'][0] for c in rows]
        metrics[name] = dict(games=32, outcomes=dict(Counter(c['outcome'] for c in rows)), outcomes_by_seat=seats,
            worst_hp_difference=min(c['hp_candidate_first'][0] - c['hp_candidate_first'][1] for c in rows),
            ending_rounds=sorted({c['rounds'] for c in rows}),
            timed_decision_wrapper_calls=sum(t['calls'] for t in timed),
            actual_policy_calls=sum(fresh[c['job']]['policy_rounds'] for c in rows),
            prescribed_prefix_turns=sum(fresh[c['job']]['prefix_rounds'] for c in rows),
            total_timed_wrapper_seconds=sum(t['total'] for t in timed),
            maximum_timed_wrapper_call_seconds=max(t['max'] for t in timed))
    require(metrics == final['metrics'], 'Published WDL, HP, rounds, maximum or wrapper/policy count differs')
    require({k: v['outcomes'] for k, v in metrics.items()} == strict['scores_by_scenario'] == replay['scores_by_scenario'], 'Grouped outcome summary differs')
    require(summary['standard_initial_state'] == metrics['standard']['outcomes'], 'Primary standard score mismatch')
    continuation = Counter()
    for name, values in metrics.items():
        if name != 'standard':
            continuation.update(values['outcomes'])
    require(summary['continuation_stress'] == dict(continuation), 'Primary continuation score mismatch')
    latest = max(c['completed_utc'] for c in strict['cases'])
    require(strict['latest_completed_utc'] == latest and strict['started_utc'] == freeze['started_utc'], 'Primary chronological endpoints')
    require(strict['elapsed_to_latest_completion_seconds'] == (stamp(latest) - stamp(freeze['started_utc'])).total_seconds(), 'Elapsed real runtime mismatch')
    require(strict['runtime_seconds_sum_of_primary_matches'] == sum(c['runtime_seconds'] for c in strict['cases']), 'Primary runtime sum mismatch')
    require(sum(m['actual_policy_calls'] for m in metrics.values()) == entry['policy_rounds'] == final['fresh_calls_per_entrypoint'], 'Real fresh policy call total')
    require(sum(m['prescribed_prefix_turns'] for m in metrics.values()) == entry['skipped_prefix_rounds'] == final['skipped_prefix_rounds'], 'Prefix total')
    expected_losses = {c['job'] for c in strict['cases'] if c['outcome'] == 'L'}
    require(len(losses['losses']) == len(expected_losses) and {x['job'] for x in losses['losses']} == expected_losses, 'Loss omission or duplicate')
    for loss in losses['losses']:
        c = cases[loss['job']]
        require(loss['condition'] == c['condition'] and loss['result_path'] == c['result_path'] and loss['replay_path'] == c['replay_path'], 'Loss case binding')
        require(loss['final_margin_candidate_first'] == c['hp_candidate_first'][0] - c['hp_candidate_first'][1], 'Loss margin mismatch')
    pairs = defaultdict(list)
    for c in strict['cases']:
        pairs[(c['condition']['scenario'], canonical(c['condition']['opponent']))].append(c)
    require(len(pairs) == len(strict['pairs']) == 48 and all(sorted(c['condition']['candidate_side'] for c in cs) == [0, 1] for cs in pairs.values()), 'Physical pair coverage')
    expected_pairs = []
    for (scenario, opponent), rows in sorted(pairs.items()):
        rows.sort(key=lambda c: c['condition']['candidate_side'])
        expected_pairs.append(dict(scenario=scenario, opponent=parse(opponent), sides=[0, 1], exactly_two_assignments=True,
            same_complete_trajectory=rows[0]['canonical_replay_sha256'] == rows[1]['canonical_replay_sha256'],
            outcomes=[x['outcome'] for x in rows], hp_candidate_first=[x['hp_candidate_first'] for x in rows]))
    require(expected_pairs == strict['pairs'], 'Paired trajectory/outcome summary')
    distinct = len({c['canonical_replay_sha256'] for c in strict['cases']})
    identical = sum(x['same_complete_trajectory'] for x in expected_pairs)
    require(distinct == strict['distinct_canonical_trajectories'] == final['distinct_canonical_trajectories'] and identical == final['identical_assignment_pairs'], 'Trajectory replication count')
    r.facts.update(metrics=metrics, conditions=96, pairs=48, distinct_canonical_trajectories=distinct,
                   campaign_started_utc=freeze['started_utc'], latest_primary_completed_utc=latest,
                   primary_elapsed_seconds=strict['elapsed_to_latest_completion_seconds'],
                   primary_runtime_seconds_sum=strict['runtime_seconds_sum_of_primary_matches'],
                   identical_assignment_pairs=identical, match_attempt_counts=actual_attempt_counts,
                   fresh_calls_per_entrypoint=entry['policy_rounds'], skipped_prefix_rounds=entry['skipped_prefix_rounds'],
                   fresh_candidate_calls_across_two_regenerations=2 * entry['policy_rounds'],
                   entrypoint_scope='Original recorded decide plus fresh direct decide and fresh default make; two API forms, not three fresh regenerations.')
    return campaign, freeze, final


def separation(r, d, freeze, final):
    name = d['campaign_name']
    audits = {kind: r.read(R / (name + '-' + kind + '-separation.json')) for kind in ('parameter', 'scenario')}
    snapshot = r.read(R / (name + '-separation-inputs') / 'manifest.json')
    require(snapshot['all_inputs_preserved'], 'Separation snapshot incomplete')
    expected = defaultdict(set)
    require(set(snapshot['audit_sha256']) == {str(R / (name + '-' + k + '-separation.json')) for k in audits}, 'Snapshot audit list')
    for kind, audit in audits.items():
        auditpath = R / (name + '-' + kind + '-separation.json')
        r.digest(auditpath, snapshot['audit_sha256'][str(auditpath)])
        require(audit['pool'] == 'D' and stamp(audit['cutoff_utc']) == stamp(freeze['started_utc']), 'Separation cutoff differs from campaign start')
        for p, h in audit['input_snapshot_sha256'].items():
            expected[(p, h)].add(str(auditpath))
    require(len(snapshot['rows']) == snapshot['input_versions'] == len(expected), 'Snapshot version count')
    require({(x['source'], x['source_sha256']) for x in snapshot['rows']} == set(expected), 'Snapshot coverage')
    blobs = {}
    for row in snapshot['rows']:
        require(set(row['audits']) == expected[(row['source'], row['source_sha256'])], 'Snapshot source/audit association')
        archive = path(row['archive'])
        r.digest(archive, row['archive_sha256'])
        if str(archive) not in blobs:
            h = hashlib.sha256(); size = 0
            with gzip.open(archive, 'rb') as stream:
                for chunk in iter(lambda: stream.read(1024 * 1024), b''):
                    h.update(chunk); size += len(chunk)
            blobs[str(archive)] = (h.hexdigest(), archive.stat().st_size, size)
        require(blobs[str(archive)] == (row['source_sha256'], row['compressed_bytes'], row['uncompressed_bytes']), 'Archived separation input changed')
    require(len(blobs) == snapshot['unique_blobs'] and sum(v[1] for v in blobs.values()) == snapshot['compressed_unique_bytes'] and sum(v[2] for v in blobs.values()) == snapshot['uncompressed_unique_bytes'], 'Snapshot byte accounting')
    parameter, scenario = audits['parameter'], audits['scenario']
    require(not scenario['preflight_only'] and scenario['candidate_or_opponent_calls'] == 0, 'Separation is preflight or called policy')
    require(parameter['no_exact_normalized_parameter_overlap_found'] == (not parameter['overlaps']) and scenario['no_exact_complete_history_overlap_found'] == (not scenario['overlaps']), 'Overlap verdict/count mismatch')
    require(final['parameter_overlap_count'] == len(parameter['overlaps']) and final['scenario_overlap_count'] == len(scenario['overlaps']), 'Published overlaps omitted')
    require(final['unresolved_parameter_inputs'] == parameter['skipped_unrecognized_inputs'] and final['unresolved_scenario_inputs'] == scenario['unresolved_inputs'], 'Published unresolved coverage omitted')
    r.facts['separation'] = dict(parameter_checked=parameter['checked'], scenario_checked=scenario['checked'],
        parameter_overlaps=len(parameter['overlaps']), scenario_overlaps=len(scenario['overlaps']),
        unresolved_parameter_inputs=parameter['skipped_unrecognized_inputs'], unresolved_scenario_inputs=scenario['unresolved_inputs'],
        undated_parameter_inputs=parameter['undated_inputs_checked_conservatively'],
        undated_scenario_inputs=scenario['undated_inputs_checked_conservatively'], archived_versions=snapshot['input_versions'],
        limit='Authenticated recorded audit coverage and retained bytes; no independent rerun of family normalization/scenario generators, no claim about unlogged executions or behavioral novelty.')


def pipeline_log(r, value, final):
    p = path(value); r.digest(p)
    events = []
    for line in p.read_text().splitlines():
        try:
            obj = parse(line)
        except ValueError:
            continue
        if isinstance(obj, dict):
            events.append(obj)
    require(any(x.get('declaration_sha256') == DECL_SHA for x in events), 'Pipeline log lacks declaration binding')
    require(any(x.get('time_and_selection_gates_passed') is True and stamp(x['time_utc']) >= GATE for x in events), 'No real time/selection gate event')
    require(any(x.get('all_completed') is True and stamp(x['time_utc']) >= stamp(final['time_utc']) for x in events), 'Pipeline log lacks final completion')
    returns = [x['pipeline_returncode'] for x in events if 'pipeline_returncode' in x]
    require(returns and returns[-1] == 0, 'Pipeline wrapper did not complete successfully')
    require(not any(x.get('returncode', 0) != 0 for x in events), 'Nonzero recorded child status')
    r.facts['pipeline'] = dict(log=str(p), complete=True, wrapper_returncode=returns[-1],
        limit='Log byte authentication and completion-event checks; not an independent process monitor.')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--campaign-and-postchecks-complete', action='store_true', help='Only supply after explicit parent authorization.')
    p.add_argument('--supplement-pre', required=True)
    p.add_argument('--supplement-post', required=True)
    p.add_argument('--pipeline-log', required=True)
    p.add_argument('--output-name', required=True, help='New simple child directory under this reader folder.')
    args = p.parse_args()
    if not args.campaign_and_postchecks_complete or datetime.now(timezone.utc) < GATE:
        p.error('Prepared only: final campaign/post-check authorization and the elapsed gate are required.')
    if not (args.output_name.replace('-', '').replace('_', '').isalnum() and '/' not in args.output_name):
        p.error('Use a simple new output directory name.')
    if not (sys.dont_write_bytecode and sys.flags.optimize == 0 and os.getpriority(os.PRIO_PROCESS, 0) == 19 and os.sched_getaffinity(0) == {29}):
        p.error('Run Python -B without optimization on core29 at nice19.')
    if not all(os.environ.get(k) == '1' for k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS')):
        p.error('All numerical thread limits must be one.')
    if Path(os.environ.get('TMPDIR', '')).resolve() != (Path.cwd() / 'bot_research/tmp').resolve():
        p.error('Use the project research temporary directory.')
    out = HERE / args.output_name
    require(not out.exists(), 'Preserve existing reader evidence; choose a new output name')
    r = Reader(); started = now()
    prepared = r.read(HERE / 'PREPARED.json')
    r.digest(HERE / 'read_final.py', prepared['reader_sha256'])
    identity = r.section('declaration_and_separate_source_supplement', lambda: source_and_selection(r, args))
    if identity is not None:
        d, supplement, post = identity
        campaign = r.section('campaign_primary_logs_replay_and_fresh_entrypoints', lambda: campaign_and_audits(r, d, supplement, post, args))
        if campaign is not None:
            _, freeze, final = campaign
            r.section('separation_and_historical_snapshot_coverage', lambda: separation(r, d, freeze, final))
            r.section('pipeline_completion_log', lambda: pipeline_log(r, args.pipeline_log, final))
    r.hash_cache.clear()
    for name, expected in list(r.inputs.items()):
        r.section('final_input_stability:' + name, lambda name=name, expected=expected: r.digest(name, expected))
    passed = not r.issues and identity is not None and 'metrics' in r.facts and 'separation' in r.facts and 'pipeline' in r.facts
    report = dict(started_utc=started, completed_utc=now(), verdict='CONFIRMED' if passed else 'OPEN',
        all_required_checks_completed=passed, actual_model='GPT-6 Astra',
        scope='Supplementary posthoc independent source/JSON reader. Not part of the predeclared D experiment; no new Engine replay or fresh policy generation.',
        reader_sha256=r.digest(HERE / 'read_final.py'), preparation_receipt_sha256=r.digest(HERE / 'PREPARED.json'),
        input_sha256=r.inputs, sections=r.sections, issues=r.issues, findings=r.facts,
        calls=dict(policy_imports=0, policy_constructors=0, policy_decisions=0, Engine_calls=0, replays=0, games=0, checker_calls=0),
        limits=['Retained checker receipts, source archives and JSON are authenticated. This reader does not independently reproduce game semantics.',
                'Recorded source identities do not prove continuous monitoring or rule out all transient historical modifications.',
                'The exact fixed 96-attempt pipeline is covered. Any recovery/retry campaign requires separately scoped review.',
                'Protected-file end inventory remains a separate team check against its actual starting state.',
                'Finite D conditions are not a random population sample, and no general superiority or optimality claim follows.'])
    out.mkdir()
    (out / 'REVIEW.json').write_text(json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + '\n')
    text = '# Supplementary terminal evidence review\n\n' + report['completed_utc'] + '\n\n'
    text += 'Verdict: ' + report['verdict'] + '. ' + report['scope'] + '\n\n'
    text += 'This reader made no policy, constructor, Engine, replay, game or checker calls.\n\n'
    if passed:
        text += 'All 96 declared conditions, three groups of 32, physical assignments, primary logs, retained replay and two fresh entry forms, source seals, failure accounting and published metrics were authenticated.\n\n'
    for issue in r.issues:
        text += '- ' + issue['section'] + ': ' + issue['diagnostic'] + '\n'
    text += '\nExact identities, per-start metrics, coverage limits and every issue are retained in REVIEW.json.\n'
    (out / 'REVIEW.md').write_text(text)
    print(json.dumps({'completed_utc': report['completed_utc'], 'verdict': report['verdict'], 'issues': len(r.issues), 'output': str(out)}))
    return 0 if passed else 2


if __name__ == '__main__':
    raise SystemExit(main())
