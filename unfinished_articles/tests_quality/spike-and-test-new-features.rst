New app feature? Spike and test first.
======================================

.. post::
   :author: Michal Bultrowicz
   :tags: Python, quality_assurance


Z TRELLO
--------

Celery, robienie czegoś asynchronicznie w tle,


0. THE APP
----------

Introducing - the dockerized hello server.
Zakładam, że nasza aplikacja będzie dystrybuowana, stawiana przy pomocy dockera.
(to pod kątem prezentacji) docker daje tę zajebistą rzecz, że po prostu odpalamy kontener
i aplikacja działa.

1. THE SPIKE
------------

It's all async. Maybe we don't know whether it'll work. Let's check.

- We look at the docs for redis (for the operations) and aredis (for specifics)
- spin up redis in docker
- look up the port
- try to connect
- try to write something and retrieve it
- It works! We know that this approach will work - great.
  So we should have a vision for the code we're
  about to implement. And with that, we should be able to write a test for it.


.. code-block:: python

    import aredis
    import asyncio

    redis = aredis.StrictRedis(port=32784)
    loop = asyncio.get_event_loop()

    loop.run_until_complete(redis.ping())
    loop.run_until_complete(redis.lpush('bla', 'sraka'))
    loop.run_until_complete(redis.lpush('bla', 'eeeee'))
    # indexing of lists works like in Python
    loop.run_until_complete(redis.lrange('bla', 0, -1))


2. THE TEST
-----------

Hey, we don't need the unit tests when we have this one (TODO coverage).
Of course we can have branching logic, etc, but often this can be handled by unit tests.
But what we have right now is a very useful automated test that can stay with us
and help us in the turmoil of a new project.

3. THE COVERAGE
---------------

TODO

4. Additional stuff, or the end?
--------------------------------

TODO

THE TEXT
--------

This will show two things - how I usually approach feature implementation (which I think is
an approach some people will benefit from), and how to write Python tests employing real systems,
dockerized. Oh and they will be some tricks. So that's three things.

Maybe spiking and testing is a single blog post, all the testing tricks is another?

This will show a way you can work on new features. It's not only for web apps.
Also, sometimes the spiking part may be really long in complex feature, and can be a quest on it's
own, that will require writing tests and multiple commits along the way.
But nevertheless, that's my sort of approach to writing code.

First show a simple web app returning hello world.

Then we want a new feature that will return something.
Let's check out if we can hack on it real quick.
Works like a charm. But hm... Since our web app has multiple instances in production
(of course it does!), it can't store stuff in memory.

Anyway, from our functional test, the system / queue / DB we're using is a hidden implementation
detail. We're only interacting with the API of our own system, or with the APIs, that the
external systems will interact with (sometimes you share a database, sorry).
TODO show that the system needs to be introspectable.
Or maybe, if we can't


So we'll need to make it async. OK then, let's assume that we know Celery and can rely on it, so
we don't need to spike it.
We don't seem to have any big unknowns now, so we can have a draft of the code in our head.
We don't know what the code will look like precisely, what'll be it's
cyclomatic complexity, how precisely we'll arrange it in functions (OK, here it's simple and without 
any if statements, but I'm talking more about the general case now).
But we do know how we want the interactions with it to look like. So we can write a high-level,
functional (or system, or integrated, or component) test.


TODO: say something about coverage of the tests as well
write about getting that from containers.
After all, measurability and debugability is a good feature of whatever system you're creating
to have. So putting coverage, a library without any other dependencies in your production
image shouldn't be a problem. After all, when it's off, it's off.

TODO: a functional_test_methods project in experiments that will be linked to the
presentation and the blog post.

Jeśli chcecie sobie zobaczyć czemu mój fork nie jest zintegrowany, to popatrzcie na dyskusję
na temat jednego issuesa na pytest-docker.

Tests design philosophy?
------------------------

web apka przyjmuje i może być odpytywana o wynik - bardzo ważne jest, żeby system dawał możliwość
sprawdzenia, czy coś się stało - to kwestia dobrego designu;
testy nie mają żyć w izolacji, powinny wpływać na to,
żeby system stał się bardziej testowalny, mniej magiczny, lepszy;

założenie, że nie trzeba testować takich "prostych rzeczy", jak to że apka wstanie jest błędne).
Polecam książki - TDD in Python, Continuous Delivery

Test system requirements
------------------------

- non-obvious, so we need to do a spike (but maybe only for a single one?) (postgres)
- using external system (postgres)
- best if we couldn't detect immediately that the operation succeeded, maybe need some indirection?
  Maybe that's not as necessary? (postgres)

Testing tricks to employ
------------------------

- (TODO) nie odwołuj się do kodu w testach funkcjonalnych, żeby wyłapać zmiany w interfejsach
  Coś z jakąś bardziej skomplikowaną funkcją? Jakiś test, w którym jakby się używało jakiejś
  produkcyjnej funkcji, to błąd nie zostałby wyłapany.
- (async cleanup) Opcje na zmniejszanie stałych związanych z czekaniem.
- (postgres - upgrade) Spraw, żeby system nadawał się do introspekcji. 
- (postgres) Korzystaj tylko z zewnętrznych interfejsów aplikacji,
  no chyba że ktoś inny będzie się integrował np. przez bazę danych,
  albo będzie jej dotykał człowiek. Wtedy używaj też tego, jak najbardziej.

Test system ideas
-----------------

MAYBE THERE CAN BE MORE THAN ONE FEATURE?

- queuing something up
- getting all the greeted names?
- something async that requires ordering?
- hello again - expiring cache with redis
- call me back with a request after a while?

Features to implement
---------------------

* auditing what names were called for - postgres
  We just want that exposed over SQL
  (I know 12 factor says that each app should have it's own data store. That's a nice assumption,
  but it doesn't work in things like Big Data storages).
  Auditing endpoint will be added.
* Cleaning up the names after a time - async
  Czyszczenie nazwy po czasie?
  (możemy założyć, błędnie, że aplikacja, nawet w wielu instancjach nie będzie padać)
  Przy okazji rewrite na inny framework - hej, to też może się wydarzyć.

