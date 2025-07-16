from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

@dataclass
class Event:
    id: UUID
    title: str
    start: datetime
    end: Optional[datetime] = None
    location: Optional[str] = None
    notes: Optional[str] = None
    is_confirmed: bool = True
    is_reminded: bool = False
    was_shared: bool = False

    def overlaps(self, other: "Event") -> bool:
        """Time‑range overlap (open intervals)."""
        latest_start  = max(self.start, other.start)
        earliest_end  = min(self.end or self.start, other.end or other.start)
        return latest_start < earliest_end
