# we have to be weary of circular imports as our packages are dependent on each other
from project_package import internal_services
from project_package.subpackage.subpackages_service_implementations import EventsRecord, Event


def some_functionality():
    """
    This is where we start some processing.
    """
    existing_record = internal_services.events_record.get()
    current_processing_level_record = EventsRecord(existing_record)
    # will apply for all the code in this thread or asyncio Task.
    internal_services.events_record.set(current_processing_level_record)

    for stuff in other_stuff:
        do_stuff(stuff)


def do_stuff():
    stuff_to_do = Event(a=x, b=y)
    really_run_stuff(a=stuff_to_do.a, b=stuff_to_do.b)
    internal_services.events_record.get().record(stuff_to_do)
