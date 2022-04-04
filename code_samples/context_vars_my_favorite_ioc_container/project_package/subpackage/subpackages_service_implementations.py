# could be dataclass from pydantic
from dataclasses import dataclass
from typing import Any, List

@dataclass
class EventsRecord:
    _events: List[Event]
    # TODO a method to construct the record from a EventsRecord.
    # We should have a specific (and maybe the only) constructor for that.
    #
    # That could describe complex actions that have subactions.


# this should have a better implementation, of course
@dataclass
class Event:
    whatever: Any
