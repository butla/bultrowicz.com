"""
This module (file) is our IoC container. The values in the container are the context vars.
"""

import contextvars

# EventsRecord can just be a list, really.
# StubRecord is there so we don't need to check with an if whether there is an events_record available.
events_record: contextvars[EventsRecord] = contextvars('events_record', default=StubRecord())
