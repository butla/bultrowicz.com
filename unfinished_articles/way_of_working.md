---
blogpost: true
author: Michał Bultrowicz
language: English
tags: Python, workflow, quality_assurance
date: 2025-04-xx
---

Notki
=====
[test pyramid](https://en.wikipedia.org/wiki/Test_automation#Testing_at_different_levels), I think.

   [^mountepy],
   and then configure that to act the way you want it to during the test.

[^mountepy]: I've written [a library](https://github.com/butla/mountepy) to manipulate Mountebank from Python test code.

TODOs
=====

parse the notes at the end

przejrzyj mój i google code style

Links to my articles about testing

Link to my portfolio project. Portfolio should also link to this article.

Copy this article to Confluence.

set date with: 




Way of Working
==============

This document is my proposal for how software developers can work together efficiently on teams of any size.

Code style
==========

Ground rules
------------

For many elements of style we rely on the Ruff linter and formatter rules. But there's a lot more that a linter can't enforce.

All code introduces maintenance costs. You could say all code is tech debt.
Minimize the amount of code to comprehend. Optimize for code readability (ease of comprehension)first, performance second (or like fourth).

Namespacing
-----------

"Namespaces are a honking great idea" TODO

Calling methods of internal/property objects is usually a bad sign.
E.g. `the_object.object_field.public_method(bla)`. Looks like we need to create a better interface.

Python file structure
---------------------

- module docstring, if needed
- imports
- most important things (constants, then functions and classes) in the file, used from outside of the file
- more "protected" / "private" things

Imports
-------

Limit importing objects into the local namespace of a file (e.g. `from logging import Formatter`), if Your file needs many imports from different namespaces.
If these are few very common ones (e.g. `FrozenSet`),  then fine.
TODO check approach in Google Code style.

Also, if some module is tightly related to another module (e.g. our logs config module will be tightly related to Python's `logging` module),
then we can import classes and functions directly into our module.

Inheritance and composition
---------------------------

Favor composition over inheritance. Inheritance is harder to read because You need to jump across a couple files.
With composition everything's explicit. And explicit is better than implicit.
Even if you need to write a bit more code (define a method that then runs a method) to include, the increased readability is worth it.

Avoid using inheritance for code reuse.

TODO code reuse example

Classes for usecases. Class should be algorithms + state. If there's no state, then let just use pure functions.

If You have complex state, do state machines: inputs, states, transitions

Pure functions are useful.

Length
------

Try to keep files below 300-500 lines of code.

Code philosophy / coding heuristics / modes of working with code
---------------

split code into orthogonal functions/capabilities.

Strive for functianol programs

Proving correctness helps testing.

Context managers, async iterators to compose pipelines of processing.

explicit is better than implicit

Think in yerms of actor model.

Functional design. Ensuring correctness in addition to scrupulous testing

Random
------

**locality of behavior**
Definition as close to usage as possible. If thing is only used once, keep definition close.
Move definition up to a more common place only when the need arises, or when You want to actively encourage the use in other parts of the code.

Minimize the amount you need to jump around the code to understand something.
Let's keep definition as close to usage as possible.

**evolutionary approach / yagni / 80-20 rule**
Don't future-proof everything. Predictions of the future are usually way off.
Do the most impactful things when short on time.

**composition over inheritance / higher order functions / algebraic types**

**State** is the source of many bugs. Keep it only when necessary.
Use immutable objects unless You have a very good reason.
frozen dataclasses, and variables marked with Final.


Code solutions (code style)
===========================

- constant numbers need explanations. "Magic numbers". Isn't there a ruff rule for that?

Tabular data queries (SQL, dataframes)
--------------------------------------

Prefer efficient queries, when working with tabular data.
Do as many JOINs as You need to get all the data that Your Usecase needs.
Take enough data to fulfill at least some usecases without fetching more data, if possible.

Fetching data with many small queries is very slow compared to computation in Python.
That the ORM will happily do hundreds of small SELECTs for You (the n+1 ORM problem - TODO link)
Network round-trips are slow (TODO numbers every programmer should know).
The link is not super accurate, but shows the orders of magnitude about right.

Unless You tame it with plugins (Django) or use with async in case of SQLAlchemy (or any other async ORM).
asyncSQLalchemy naturally doesn't have that problem, because You need to do an explicit await on any network calls,
so You see that a query is happening in code.

Approach to testing (way of working)
====================================

Kinds of tests that I see. We should have a common vocabulary.
I'd say in our context, we should have: (TODO links)
- unit (TODO link to my doc),
- journey (same as unit, but multiple interactions, to test the framework) (link to our test)
- integrated - we don't have an explicit group for these, but all the tests that use the DB, or any other container in Docker Compose, are what's called integrated tests
- component - I call them "external tests", but we already use "component" in this project.
- We have them in various forms, but they can be unified.

Do double loop TDD. When starting work an a new feature, start with a happy-path component test.
This will make sure You think about the interface.
Also, the test will show You when Your code starts working.
You can make it auto-run on file edits with IDE plugins or [`entr`](https://bultrowicz.com/continous_validation_with_make_and_entr/))
Then, start, and theStart with a component test Double loop TDD, link here.
We can add the kinds of tests with pytest markers.

Test pyramid isn't always good. The finer grain of the test, the more chance it'll have to change with refactoring.
Start with high-level test that prove the functionality is working. Then do a general high-level failure test.
Then do smaller scoped tests to prove that components of the system behave correctly in different circumstances.

Test isolation isn't that important. If a test fail, You know you have issues to investigate.
There can be tests that use the production code for test setup.
That's acceptable, as long as You make false positives in all tests highly unlikely.

Testability is a feature of the code. Make the code easy to validate. If the code is hard to test - change it.
Some inspiration: [refactoring Falcon API apps for testability](https://falcon.readthedocs.io/en/stable/user/tutorial.html#refactoring-for-testability)


Code reviews (way of working)
============

If something is complicated and would take a lot of time to do a back-and-forth over text it might be best to have a 1:1 call about the issue.
If that happens, comment in the MR that You need to talk about it, so that other reviewers know that something is happening in a particular area of the code.
Message the person directly. After the chat, put the conclusion in the MR comment.

Always be constructive. If you can't be constructive, point out something that You don't like with the reasons why.
Leave TODOs in the code explaining the problem. Maybe You can solve it later, maybe someone else will.
Also, You can ask other people for input.
Just mind that Gitlab notifications can get spammy. Ping people in the communicator

If an idea is complicated, or You don't have a full vision yet, just talk about where You both want to go.

Go through the code, leave notes in the code, create a branch from the session with todo notes and code snippets.

If something feels weird or wrong but You can't put your finger on it - ask a question about the bit of code.
Don't assume it's wrong. 

Work organization
=================

Keep momentum

Don't get spread too thin

Do exploration and estimation of the problem (big unknown task) first

Have focus time. You won't solve everybody's problems, nor should You.
You should primarily focus on what was agreed on sprint start.
But when You can spare a moment, helping is great for everyone :)

(optional) keep a notepad.
What are Your TODOs?
What needs to be handled later?
A digital notepad makes the notes easier to share, but a physical one can be handy during meetings, and can be more relaxing for the brain ;)

Make progress, show progress, to keep stakeholders calm.

Chat / meeting etiquette
------------------------

Stay on topic in shared chats and meetings. Think about how much time is spent in total on a 5 minute conversation between 10 people. Imagine having that time for focused work alone.
That's the impact we're not gonna have because of those 5 minutes, so make them count.

Collaborate on notes from the meeting in the chat.
AI notes are usually too noisy.
Start side conversations (Slack / Teams thread) to handle that.

Bullet points for next steps are needed.

Tech debt
=========

Tech debt - have a stable bandwidth reservation, if that doesn't work plug the holes that slow you down.
Don't let them fester. But you need to keep moving forward

Philosophy
==========

Boy scout rule vs the broken window effect. One is a force pulling everything up towards a better state, the other is pulling down.

Zen of Python

Eveolutionary Architecture (book link) - do gradual changes. Big bangs are hard to execute in a distributed environment.

Continuous Delivery - focus on delivering working increments of work often.
Move from a proven-working state (proven with tests and other quality checks like linter, type check, etc.)

Maintain momentum

Leave some bandwidth for creative impulses. Don't waste them. It would be energy lost.
Balance that with maintaining momentum.

Also remember to be accountable. It's better to give a longer time estimate, but be reliable and predictable.
It makes it easier to work with You then and create timelines around your work.

Work towards Your management. It's an interface. It's an often very suboptimal thing. But "it is what it is".
Remember, all workplaces are a game. Play nice with others.
It's just reality, people "above" You can't see all the complexity. They need to reduce it.
But maintain enough points so that nobody wayyyy up top without a detailed picture won't let You go because "too few points next to that name on the spreadsheet".

So do good stuff that escapes metrics. But also satisfy the metrics that are expected of You.

Management should be open and transparent about success metrics, though.



FROM ANOTHER NOTE:
Ways of Working
===============

[Rapid local development of distributed applications with testing, double-loop TDD, and Docker Compose](https://youtu.be/hjve48cYj_U?si=58yYzylb2g75yYt7)

Communicate and try to win as a team
------------------------------------

Pierwszy to communicate. Think You're hunting a mammoth together, or something ;) You're a team.
Your score should be mainly evaluated on a team level to foster cooperation.

Make it fun in a non-forced, and engaging way.


Code style
----------

Don't use django signals - use usecases.

Follow the patterns from the standard lib. E.g. if you're implementing `__eq__` and you get an incomparable type in the argument, then return False.
Don't include the type in the name of a class. So no "Enum" at the end of enum classes.
Everybody should understand they're enums from their names and from the way they look like in autocomplete.

(philosophy) Egoless development
Try to always be constructive in conversations.
Spotting issues is good and makes the whole project better, but pointers towards a solution are even better 🙂

(philosophy) Don't try to make your idea win intact. It's not about winning, it's about the most pragmatic/utilitarian solution.
See if seemingly opposite approaches cover different real usecases.
Then come up with a solution that fulfills as many of the usecases as possible
"Thesis, antithesis, synthesis".

(way of working)
How to approach a code task. Figure out how to check that the thing you have is really working. Does it break if somebody uses it "the wrong way"? Talk to your LD about your approach early on

Poczytaj swoje ostatnie komentarze.

Daj przykłady dobrych review.



Tricks
------

Use async generators if you need to patch a process. Think of composing pipelines.


Clean architecture
------------------

Arch - rd pools as business usecase, then implemented concretely by the connector

keeping the balance is always hard - don't create too small Usecase classes, don't create god objects that do everything.
  Apply evolutionary approach - build stuff and factor things out only when they become unwieldy.

Good namespaces.

Which namespace can import which?
TODO mermaid
usecases -> interface.schemas ->
interface.endpoints -> interface.schemas
interface.endpoints -> usecases
usecases -> entity
orm?
all import core

Clean code will make db consistency easy. E.g. a usecase modifies as many DB tables as necessary, in a single transaction.
The usecase doesn't do that directly, though - it delegates to repository-type connectors.


Philosophy
----------
Game theory - let's be mindful of it: let's reward the things we want, cut points for things we don't want.
And let's gamify this somehow so that people actually enjoy the growth that's happening.

(way of working)
No sarcasm, only constructive criticism.
No ad-hominem attacks.
At least say why You don't like something. 

Be egoless.
