---
blogpost: true
author: Michał Bultrowicz
language: English
tags: Python, quality_assurance
date: 2023-03-27
---

Separating different kinds of tests
===================================

When I work on a project I differentiate three kinds of tests: unit, integrated, and external.
In this post I'll explain how I think about them.

FYI unit is the lowest level of tests, integrated is higher, external is even higher.
Thinking about the kinds of tests in terms of levels and height comes from the
[test pyramid](https://en.wikipedia.org/wiki/Test_automation#Testing_at_different_levels), I think.

Actually, I see one more test category, but it doesn't apply to self-contained projects - "end-to-end" tests for
systems compromised of multiple applications.
I won't go into them here.

Each of the three "base categories" gets its own folder in the "tests" directory in the project's root:

```
project_root/
├── app_code
│   └── ...
├── pyproject.toml
├── ...
└── tests
    ├── __init__.py
    ├── external
    │   ├── __init__.py
    │   ├── test_XXX.py
    │   └── ...
    ├── integrated
    │   ├── __init__.py
    │   ├── test_db_integration.py
    │   └── ...
    └── unit
        ├── __init__.py
        ├── test_YYY.py
        └── ...
```


## Categories explained

### Unit tests
The most well-known of the three.

They should be fast, operate only in-memory, don't require the network, the file system, or external applications.

Well, I actually allow file system usage in my unit tests as it's predictable and dependable.
Even if it's orders of magnitude slower than in-memory code.

#### Using app code's internal interfaces
The unit tests are expected to use the internal interfaces of the code under tests - meaning they can create
objects, call functions, etc.

In some contexts, usually when using test facilities provided by libraries or
[frameworks](https://fastapi.tiangolo.com/tutorial/testing/),
you can have unit tests that use what look to be external interfaces.
It looks like you're calling the app from the outside, but you're not.
In reality, the test helpers in frameworks usually side-step stuff like the network,
and allow your tests to inject themselves directly into your framework-integrated code.
So you're not really using the network ("the network" being an example of a real life external interface),
but the code under tests has no way of telling that it was called in an unusual way.

Tricks like that allow for [separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns)
in tests - having independent (aka. "orthogonal") tests, for independent aspects of the code.
You can still have separation of concerns in higher level tests, though, but they'll usually hit more code,
making a "wider" path through the system under test.
So separate higher level tests will usually overlap more when it comes to
[code coverage](https://en.wikipedia.org/wiki/Code_coverage).

#### App and test code are together in a single process
Generally, the "code under test" and the test itself run within the same process,
because the test exercises/runs the application code.
Well, OK, you can have multi-process apps (e.g. with the
[multiprocessing lib](https://docs.python.org/3/library/multiprocessing.html)),
or spawn new processes in tests and still call them "unit tests".
It's still all fast, simple, and predictable.

#### Single assertion rule
Some sources state that unit tests should only use a single function or method at a time - I don't subscribe to
that idea.
The unit should be small, but I'm not strict about "one function/method/object" rule.
The test can touch as much code as it needs, as long as its failure tells you precisely what's wrong.
And as long as the test doesn't get too slow, or convoluted.

I also don't think they can only ever have a single assertion.
If it's more practical for a single test to have multiple assertions, then go for it.
Sometimes duplicating a lot of setup or assertion code across multiple tests just to have that clear
division with a single assertion per test just isn't worth it, in my opinion.

#### More context

[More info on unit tests, from Martin Fowler.](https://martinfowler.com/bliki/UnitTest.html)


### Integrated tests

Like the unit tests, the integrated tests can still use internal interfaces.
The thing that separates them is the ability to use more "complicated" things, like the network,
or other applications (e.g. [databases](https://www.postgresql.org/),
[persistent queues](https://redpanda.com/)).

Remember, if your application uses other applications, they are effectively a part of your system.
You have less control over them, though. This has good and bad sides.

#### Using app code's internal interfaces
Like the unit tests, the integrated tests can still use internal interfaces.

#### App and test code are together in a single process
Generally similar to how it is with the unit tests.
The tests still run within the same process as the app code.

#### Test reliability

Because the integrated tests use external systems and the network,
they might provide more challenge when ensuring their reliability.
By "test reliability" I mean the inverse of
[flakiness](https://testing.googleblog.com/2020/12/test-flakiness-one-of-main-challenges.html).

External systems (which are used in integrated tests) will often be asynchronous (like the real world),
so ensuring reliability might require awaiting, e.g. waiting for an operation started with a call
to propagate throughout the external system.

#### The name "integrated tests" vs. "integration tests"

I prefer the term "integrated" rather than "integration" tests.
I don't feel strong about this, but "integrated" imply that the tests are integrated with something,
like a database.
"Integration" can be a broad thing. Like integration between two applications in a microservice architecture.


### External tests

These tests interact with the application from "the outside",
using only the external interfaces that the application exposes (e.g. HTTP, GUI, CLI).

They should use application artifacts that will be shipped. E.g. a built app binary, or a Docker image.
The application should be configured with settings that are as close to production as possible.

#### Affecting the app's behavior during external tests

When setting up "classic" tests that use internal interfaces you can modify the application's behavior by dependency
injection and [monkey-patching](https://www.geeksforgeeks.org/monkey-patching-in-python-dynamic-behavior/).
That can't be done with external tests.

There are two ways you can affect the behavior of the app during external tests:
1. Change the external state the app reads.

   That can mean changing the contents of the database it talks to or modifying files that it reads.
   Also, if your application relies on an external HTTP service, you can replace it with a test double like
   [Mountebank](http://www.mbtest.org/)[^mountepy],
   and then configure that to act the way you want it to during the test.

2. Add an external interface to the app that enables manipulation of the internal state needed by the test.

   If an external test is what you want, and there's no other way to trigger the test conditions,
   then you need to add some code to the app.
   If you're working on a web API, then that additional code might be a new endpoint.
   I think it's fine to add features to the code that are only there for the sake of testability.
   It's important that these features are disabled on production releases.

#### The name "external"

I haven't seen the name in literature. I came up with it, because it seems more precise than other, more "standard"
names, like "functional", "component", or "end-to-end" tests.


## Why to separate the tests by their kind?

Separation makes the distinction explicit.
It makes the team mindful about the category that each test falls under.

We need to be mindful of the categories, because the higher levels of tests are more time-consuming.
When you need to make the test suite faster, the starting point can be looking at the higher level tests and checking
whether they can't be replaced with lower level tests.

A test should be the lowest level that fulfills the job.
If you can check what you want about the code without poking a database, then do it
(meaning write a unit test instead of an integrated test).

Another small benefit to the separation of test categories into separate directories is the ability to run them
independently. E.g. I can only run the unit tests for a quick check when I'm in the middle of some implementations.


## When to use the different kinds of tests?

I think that when you write a new feature you should start with an external test,
and only write lower levels of tests when there are uncovered cases or code paths left.

If you're writing code that talks to an internal system, have at least one happy-path integrated test for it
(unless that same path is already covered by an external test).
Cover the rest of the code paths with unit tests. If that's not feasible, add more integrated tests.

There are no absolute rules, though.
If you're short on time, and you can cover lots of ground (code)
by creating many external tests (e.g. running a bunch of calls against the REST interface of Docker container),
then do it. Just be aware that you're taking on a technical debt.
You might need to push some tests to lower levels (integrated, unit) later, when the test suite starts taking
too much time.


## My thoughts on the "test pyramid"

I don't subscribe to the idea of a "test pyramid", meaning you should always have more lower level tests
than higher level ones. While that might be true for a lot of "standard" projects, it won't be true always.
E.g. if you're testing hardware, the majority of your tests might be integrated or external.

Here's some more thoughts from [Martin Fowler](https://martinfowler.com/articles/practical-test-pyramid.html),
and [Brian Okken](https://testandcode.com/31)


## Random remarks

I have an [old talk (and an article)](../tdd-of-microservices) where the idea of three separate kinds of tests also
makes an appearance.

Martin Fowler (again) has [a presentation about types of tests for microservices](https://martinfowler.com/articles/microservice-testing/#testing-integration-introduction).
I drew inspiration from there when I was coming up my definitions.
He generally has a lot of good material on testing.

This article isn't thought through and laid out as well as I'd like, but I wanted to push it out quickly.
I plan to gradually tweak and expand it in the future.

[^mountepy]: I've written [a library](https://github.com/butla/mountepy) to manipulate Mountebank from Python test code.
