from datetime import datetime
from uuid import uuid4
from app.models import Event
from app.calendar import Calendar

def test_conflict_detection():
    cal = Calendar()
    e1 = Event(uuid4(), "Math", datetime(2025, 7, 16, 14), datetime(2025, 7, 16, 15))
    ok, _ = cal.add_event(e1)
    assert ok

    e2 = Event(uuid4(), "Soccer", datetime(2025, 7, 16, 14, 30), datetime(2025, 7, 16, 16))
    ok, conflicts = cal.add_event(e2)
    assert not ok
    assert len(conflicts) == 1 and conflicts[0] is e1
