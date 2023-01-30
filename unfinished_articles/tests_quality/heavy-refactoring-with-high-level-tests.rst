Heavy refactoring? Functional tests help.
=========================================

.. post::
   :author: Michal Bultrowicz
   :tags: Python, quality_assurance, refactoring

I'm about shuffle around a bigger chunk of code around in an app I'm maintaining.
You might say I'll be doing heavy refactoring. I might say I'll gut it (but the patient will be better afterwards).
The code's quite messy with nested loops, conditional branches etc, and not covered with tests
(that's how I received it).
How do I keep myself from inadvertently breaking some complicated/convoluted logical flow, and thus, some functionality?
I'm gonna create a high-level test harness around the app [#1]_.

I could also say functional or maybe "component" tests (TODO link do piramidy Fowlera).
Although I'll be testing two components (or "apps", or "microservices", or just "programs") as a whole.
It's a web API app and a worker (task queue processor).

Why "high-level" and not "functional" or "end-to-end"? Or "service tests" (aka. out-of-process
component tests)
Also, I like the name "external", to emphasize the fact, that we're approaching the app from outside,
not touching its internals.
Or maybe it is functional. I'm only using the programs external functions.
And also, I'm treating it a bit like a function, with defined inputs and expected outputs.

The plan is:
- set up tests
- run them to make sure the old code is working.
  At the same time you can observe **how** it's working.
- do the code changes
- see that the tests are still passing, so the app is still working as intended.

To people that are averse to high level tests: I'm doing it like that, because it's way simpler
(and quicker, less brittle, doesn't require changing as often with the code)
than a reliable test harness done with unit tests. Also, unit tests (without the real external dependencies) never really tell
you if the app's gonna work if you run it the way it'll run for real, as a whole (instead of just bits of the code).
And those high level tests describe the app. They should immediately show what the app is doing.
What are its inputs and outputs.

My test - how it's arranged.
Just one test with some variations. The app works well with that, yours might not.
Don't care about execution speed.
The test doesn't even need to run in CI (there's not testing there anyway at the moment),
so it doesn't even need to be fully automated.
It just needs to make you confident (to a degree that satisfies you in your current situation)
that you didn't break the code.

Set up the data that the app will use. Understand what it needs.
I copied a doc in ES which I don't fully understand, but the app needs it.

You need to be able to configure your app.
In my case, I make it so that there are vars in docker-compose's environment for my two apps.
The config is then read in the app code.
In production it takes prod values, locally it takes local values, but it's the same code running
in both places, without any special cases.

I just set up one very coarse grained test, set it up for all the combinations I want to check.
It's inefficient in terms of execution time, but very good with my time - I just have one test
with parameters, essentially.

And when I'm done with the refactor the tests can be changed (fewer functional, more unit)

Stacktraces from the container are guiding me, but also -
PRINT DEBUGGING
of course, with such high level tests failing, I'm not getting a lot of detailed info.
But I'm watching stacktraces in the logs of the container, and I'm just adding prints... ¯\_(ツ)_/¯
The most important thing is that I covered a lot of ground, with tests that will actually
tell me if the service is working.

I'm not gonna check all the kinks right now with those large-grain tests.
But it's gonna be wayyyyy easier to make the code more testable with unit tests now
that I have the harness. Also, the number of those crude tests in the harness will
decrease, I'll only leave the ones needed for the major paths through the app,
rest will be thoroughly covered with unit tests, because the code will change
to make that easier (also, it'll be way easier to reason about)
TODO - refactoring for testability post will follow.

Yup, rerunning these tests takes a bit (a couple of seconds) but is way
less mentally tasking then remembering about checking every little thing
(and arranging the data for those checks) manually.

Making progress a few tests at a time (I have like 11).
They have a messy separation of concerns. Trying to check as many things as I can at once.
Although I don't duplicate checks that I don't think are necessary.

I have this function that runs the job, simulates the other system to check off the tasks.
I have a conditional to not do that, for one special case.

TODO show simplified code for run_job and for sqs and elasticsearch setups.

Show how I'm setting up the env with a test in the makefile for the time being.
We'll have code for setting up everything in the central makefile, or in some container
(maybe daemon, maybe running once before all services).

Also the messy test that actually sets up the env for the app (show the bit of makefile).

dk restart <container> and dk logs -f <container> between adding prints.
I have a tmux window with two panes where I run these.
With my ZSH setup I just run the previous command on both of them.

When I'm fixing unit tests I broke (one of the subprojects has them, but only
because I added them).
I'm just running them from the last in the file, because that's
for which the error I can see at the end of the pytest output :)

Fixing the unit tests is a bit tedious, but it's not tiring mentally.
Later, with beter designed internal APIs my unit tests won't require changing as often.
And there'll be fewer unit tests on any single thing (now I've been doing coarse-grained unit tests)

But I also get to delete some of those unit tests when they don't make sense anymore :)

Side notes
----------

I'm trying to add some tests (also lower-level: unit and "integrated")
here and there to make my quality checks faster.
Why check your work and not rely on immaculate code authorship?
Well, it's really good to know if the thing I wrote really does what it's supposed to,
and doesn't do anything weird if I play with it (exploratory part of testing).

If you're starting development of an app, or just a new feature, you can start with tests like this.
I'm a huge fan of the "double loop TDD" (TODO link do mojego artykułu i do TDD z obey the testing goat) in general.

With tests like this I can do major changes to the app, like switching frameworks.

TODO add an image of the app, inputs and outputs (with numbers to show order).
obrazek z przezroczystym tłem

.. rubric:: Footnotes

.. [#] Also could be envisioned as setting up a fortified perimiter around the app to keep tabs on it.
