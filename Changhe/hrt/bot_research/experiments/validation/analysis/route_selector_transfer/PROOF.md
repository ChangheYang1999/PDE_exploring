# Transfer of the unchanged route selector to later frozen teammates

Written 2026-10-31T16:34:09.207269+00:00, before these games.

## Exact claim and conditions

The empirical question is whether the unchanged route-gated selector avoids defeat against five additional frozen policies in standard starts: fortress38, fortress39, economy20 with the installed bot's foreign-delegate parameters, economy27 and economy29 with the economy worker's declared parameters. The exact source closures and specifications are pinned in route-transfer-001.json. This is a thirty-game development test: five opponents, adaptive plus both forced branches, and both physical assignments. These policies and their weaknesses have already been discussed, so this is transfer evidence rather than a claim of unseen-policy sampling.

## Argument and required checks

No new policy code is introduced. The public route predicate and conditional full-history identity proof in ../route_gated_selection/PROOF.md apply unchanged. The original engine must replay all submitted actions, every fresh selector decision must agree with its logged action list and preserve its input observation, and each adaptive trajectory must equal the corresponding selected forced mode. These conditions prove the recorded comparison, not future opponent-independent strength. Failure of any control leaves that comparison unresolved.

The result table must retain every target and mode, including losses and draws. The already running aggressive maze-builder challenge is a separate test of the selection rule and cannot be omitted when assessing it. The installed bot and its completed pool-C validation remain unchanged.

## Dependencies

The previous route and projection proofs, the same early/growth branches and exact JSON inputs, the five frozen target policies, current original engine, and source, data, replay and fresh-history audits. Fortress39 is frozen but still undergoing its owner's separate regression; its inclusion here is not a promotion recommendation.
