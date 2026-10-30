from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Building:
    x: int
    y: int
    type: str


@dataclass(frozen=True)
class RosterEntry:
    id: int
    type: str
    bought_round: int
    expires_after_round: int | None

    def active(self, round_number: int) -> bool:
        return self.bought_round <= round_number and (
            self.expires_after_round is None or round_number <= self.expires_after_round
        )


@dataclass
class PlayerState:
    name: str
    hp: int
    gold: int
    n_factories: int = 0
    buildings: list[Building] = field(default_factory=list)
    roster: list[RosterEntry] = field(default_factory=list)
    next_roster_id: int = 0
