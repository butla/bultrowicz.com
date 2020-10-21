decision_makers.py

class PureProgressivist:

    def is_new_thing_ok(the_thing):
        return True

    def is_old_thing_still_ok(the_thing):
        return False

class PureConservatist:

    def is_new_thing_ok(the_thing):
        return False

    def is_old_thing_still_ok(the_thing):
        return True

# We might have implemented some extreme versions of the decision making algorithms here.
# True, they'll be right sometimes, but it'll be pretty random.
# I think we need to add more logic to make them more sophisticated.
# Or we put the logic outside of the classes in a wrapper that switches between them?
# But then we could also get rid of the function arguments, since they aren't used anyway.


# This is what happens when I don't silence my shower thoughts and publish them because I'm not having a lazy day.
