---
blogpost: true
author: Michał Bultrowicz
language: English
tags: Python, quality_assurance
---

Separating different kinds of tests
===================================

When I work on a project I differentiate three kinds of tests: unit, integrated, and external.
In this post I'll explain how I think about them.

FYI unit is the lowest level of tests, integrated is higher, external is even higher.
The idea of "level height" comes from the
[test pyramid](https://en.wikipedia.org/wiki/Test_automation#Testing_at_different_levels), I think.

OK, there's one more test category, but it doesn't apply to self-contained projects - "end-to-end" tests for systems
compromised of multiple applications.
I won't go into them yet, but one day this article might get expanded with them.

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

### Unit
The most well-known of the three.

They should be fast, operate only in-memory, don't require the network, the file system, or external applications.
Well, I allow file system usage in my unit tests as it's predictable and dependable.
Even if it's orders of magnitude slower than in-memory code.

#### Using app code's internal interfaces
The unit tests are expected to use the internal interfaces of the code under tests - meaning they can create
objects, call functions, etc.

In some contexts, usually when using test facilities provided by libraries or
[frameworks](https://fastapi.tiangolo.com/tutorial/testing/),
you can have unit tests that use what look to be external interfaces, though.

It looks like you're calling the app from the outside, but it's not.
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

#### App and test code in a single process
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

### Integrated

Like the unit tests, the integrated tests can still use internal interfaces.
The thing that separates them is the ability to use more "complicated" things, like the network,
or other applications (e.g. [databases](https://www.postgresql.org/),
[persistent queues](https://redpanda.com/)).

Remember, if your application uses other applications, they are effectively part of your system.
You have less control over them, but sometimes it's a good thing.

TODO 
Here's a good description
https://martinfowler.com/articles/microservice-testing/#testing-integration-introduction

Also within the application's process. Tests run the application code, they're in a single process.

Though I prefer the term "integrated" rather than "integration" testing.
I don't feel strong about this, but "integrated" imply that the tests are integrated with something,
like a database.
"Integration" can be a broad thing. Like integration between two applications in a microservice architecture.

#### Using app code's internal interfaces
Like the unit tests, the integrated tests can still use internal interfaces.

#### App and test code in a single process
Generally similar to how it is with the unit tests.
The tests still run within the same process as the app code.

Because the integrated tests use external systems and the network,
they might provide more challenge when ensuring their reliability.
By "test reliability" I mean the inverse of
[flakiness](https://testing.googleblog.com/2020/12/test-flakiness-one-of-main-challenges.html)

External systems (which are used in integrated tests) will often be asynchronous (like the real world),
so ensuring reliability might require awaiting, e.g. waiting for an operation started with a call
to propagate throughout the external system.

### External (TODO)

Try the application from "the outside", using only the interfaces that the application exposes (HTTP, GUI, CLI).

Uses real application artifacts that will be shipped. E.g. a built app binary, or a Docker image.
Production configuration (or as close to that as possible).

During these tests, you can only affect working of the app by changing things

External is a name I came up with. Functional or component, or end-to-end might be ambiguous (why are they ambiguous).

Where do the names come from?
Integrated - I've taken from martin fowler (TODO that presentation)

## Why to separate them? (TODO)

I can run them independently.
Also, it makes the distinction explicit.

A test should be the lowest level that fulfills the job.
If you can check what you want to check about the code without poking a database, then do it
(meaning write a unit test instead of an integrated test).

There are no absolute rules, though.
If you're short on time, and you can cover lots of ground (code)
by creating many external tests (e.g. running a bunch of calls against the REST interface of Docker container),
then do it. Just aware that you're taking on a technical debt.
You might need to push some tests to lower levels (integrated, unit) later, when the test suite starts taking
too much time.

## Additional stuff (TODO)

### The test pyramid

I don't subscribe to the idea of a "test pyramid", meaning you should always have more lower level tests
than higher level ones. While that might be true for a lot of "standard" projects, it won't be true always.
E.g. if you're testing hardware, the majority of your tests might be integrated or external.

https://martinfowler.com/articles/practical-test-pyramid.html
https://testandcode.com/31

No, I don't subscribe to the "test pyramid" (link). I think that when you write a new feature you should start with external tests,
and only write lower levels of tests when there are uncovered cases or code paths.
Sometimes that should be integrated test, sometimes unit.

### Other

TODOOOOOOOOOOOOOO make that into an internal link
I have an [old talk (and an article)](../tdd-of-microservices) where the idea of three separate kinds of tests also makes an appearance

That martin fowler's presentation has some good summary of describing various classes of tests.
https://martinfowler.com/articles/microservice-testing/#testing-integration-introduction
He generally has a lot of good material on testing.
