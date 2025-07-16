from __future__ import annotations
from typing import List, Tuple
from .models import Event

class Calendar:
    """Very small in‑memory calendar with conflict detection."""

    def __init__(self) -> None:
        self._events: List[Event] = []

    @property
    def events(self) -> List[Event]:
        return list(self._events)

    def add_event(self, event: Event) -> Tuple[bool, List[Event]]:
        """Return (accepted, conflicting_events)."""
        conflicts = [e for e in self._events if e.overlaps(event)]
        if conflicts:
            return False, conflicts
        self._events.append(event)
        return True, []
