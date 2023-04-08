---
blogpost: true
author: Michał Bultrowicz
language: English
tags: Python, quality_assurance, Docker
date: 2023-04-08
---

Developer workflow with local tests using Docker Compose
========================================================

Recently, I did a presentation about my development workflow for back-end applications.

English version of the video:
<iframe id="odysee-iframe" width="560" height="315"
src="https://odysee.com/$/embed/@michal.bultrowicz:c/dev_workflow_with_local_tests_using_docker_compose:8?r=52LTaohq65dxC4k1i52CHhK5UAXrDqQ8"
allowfullscreen></iframe>

[YouTube link.](https://youtu.be/hjve48cYj_U)

Polish version of the video:
<iframe id="odysee-iframe" width="560" height="315"
src="https://odysee.com/$/embed/@michal.bultrowicz:c/lokalne_testy_z_docker_compose_a_praca_programisty:4?r=52LTaohq65dxC4k1i52CHhK5UAXrDqQ8"
allowfullscreen></iframe>

[YouTube link.](https://youtu.be/Ob-3YNgXYZc)

Slides are [here](https://github.com/butla/presentations/tree/master/2023-03_developer_workflow_with_local_tests_using_docker-compose).
The sample code is [here](https://github.com/butla/experiments/tree/master/testing__quality_assurance/sample_backend_app).

## Contents summary

- Docker Compose setup with the sample HTTP/REST app (written in Python) and a SQL database
- High-level tests using containers.
- Reloading the app container on code file changes.
- Running tests on code file changes.
- Makefiles to describe common development tasks.
- CI setup based on local tests.

## Abstract

Containers have revolutionized many aspects of software development. In particular - testing.

Testing applications with the same data bases (e.g. Postgres, Redis), queues (e.g. Kafka), etc.
that they'll rely on in production grants a substantially higher degree of confidence in the software,
than tests with mocks or in-memory fakes of real connectors.

In this presentation I'll show how I use docker-compose for local running and testing of the app being developed.
How to adjust the code and set the configuration to make your work faster, ease on-boarding of new team members,
and, above all, to increase the quality.
The presented techniques emerged from working on a couple projects across the last 5 years.

The example code will be a Python back-end app, but the techniques will apply in other programming languages,
and not only for back-end applications.

The presentation assumes at least a passing familiarity with Docker and docker-compose.

The subjects covered will include:
- separation of unit, integrated, and functional tests
- organizing the project so that a local instance of the app can be run with two commands: `git clone && make run`
- not resetting the test environment between tests
- local and CI test parity
- debugging code running in containers
- using "Docker mounts" to enable fast application reloading while editing code
- changes to the production code that make testing easier
