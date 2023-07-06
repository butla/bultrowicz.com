# Michał Bultrowicz
**Curriculum Vitae**

## Contact
michal.bultrowicz@gmail.com

(+48) 790 467 660

https://bultrowicz.com/

https://github.com/butla


## Summary

I see myself as a holistic software engineer - I can negotiate requirements, design, plan the delivery, implement,
ensure quality, and monitor IT solutions.
I'm used to creating business-critical applications
and handling the challenges and pressure that come with that.

I have a strong belief in gradual change, continuous testing, and data-driven decision-making.
I love Python, Linux, and all software that's both elegant and resilient.
I like staying close to the state of the art in my areas of expertise,
but I've noticed that inspiration can come from pretty much anywhere, hence I have broad technical interests.

## Computer skills

- expert in Python programming
- writing understandable and testable code
- building highly available (HA) and fault-tolerant back-ends
- advanced web application testing (unit, functional, stress, load, performance)
- site reliability engineering - ensuring observability, gathering metrics, setting up alerting, optimizing performance
- cloud infrastructure automation
- Linux server management
- implementing web security (X.509 certificates, mTLS, JWT/JWK, OAuth2)
- creating data pipelines / setting up ETL
- implementing Continuous Delivery pipelines
- optimizing team's development workflows
- exposure to building front-ends with ReactJS and plain HTML+JS
- able to work with just the terminal, without a graphical environment
- driving "spikes" (in the eXtreme Programming sense) through the entire tech stack, hardware-to-frontend

## Tools (with years of experience)

- languages: Python (10: od 2013), Bash (11: od 2012), JavaScript (1.5: BT, personal), Java (5: intel), C++ (1: intel), C# (4: intel)
- clouds: AWS (3: iterio, BT ciut, Nira), GCP (1: Iterio), Digital Ocean (2: personal)
- web APIs / REST: FastAPI (0.5: swoje), AioHTTP (1.5: iterio), Falcon (0.5: swoje), Flask (2: Intel), Django (3: BT, Nira), Spring Boot (1.5: intel)
- testing: pytest (7: od 2016), Python's unittest (2: 2014-2016), selenium (1.5 BT), Mountebank / mountepy (3.5: Iterio, BT), Playwright (some experiments)
- SQL: PostgreSQL (6: Iterio, BT, Nira, Witchsoft), Citus (1: Iterio), AWS Aurora PostgreSQL (1: Nira), AWS Redshift (0.5: Iterio)
- data stores: Redis(3.5: Iterio, BT), Elasticsearch(2.5: 1.5 z Intela, Nira), S3/MinIO (3.5: Iterio, BT)
- Kafka (4.5 total):
  - Confluent Kafka (2: 1 intel, 1 BT)
  - AWS Kinesis (1.5: iterio)
  - AWS MSK (1: Nira)
  - Faust (1)
  - aiokafka (1)
- containers: Docker (7, od 2016), Kubernetes (2: BT, ciut Intel), Helm (1.5: BT), AWS ECS (2.5: Iterio, Nira)
- infrastructure management: Terraform (3: Iterio, BT), Ansible (2: scylla, Iterio, personal)
- version control: Git (10: od 2013)
- logging/monitoring: AWS CloudWatch (1.5: Iterio), DataDog (1: Nira), Prometheus (1.5: BT), ELK stack(2.5: BT, Nira)
- CI/CD: Gitlab CD (2: BT), Github Actions (1: Nira), Jenkins (4: Iterio, Intel, BT trochę), TeamCity (2: Intel)
- error tracking: Sentry (4.5: Iterio, BT, Nira)
- serverless: AWS lambda (1.5: Iterio)
- operating systems: Linux(12: od 2011), Windows (5: 2011-2016)
- front-end: HTML/CSS (1.5: BT, personal), JS (1.5: BT, personal), ReactJS (1: BT)
- data analysis: Pandas (0.5: personal, Nira), Seaborn (0.5: personal, Nira)
- GUI app development: Android (3), WPF(2), Java Swing (2)
- miscellaneous:
  - Celery (2: BT)
  - nginx (3: BT, personal)
  - Hadoop MapReduce (0.5: Intel)
  - OpenSSL (1: intel)

## Soft skills

- negotiating and defining system requirements
- leading a Scrum or Kanban team
- self-organization
- cross-team communication
- teaching developers through meticulous code reviews
- knowledge of software legal compliance and licensing issues
- analyzing teams' incentives and the tensions arising from them

## Experience

### 2023.04 -- 2023.05
Primary Software Wizard at [WitchSoft](https://witchsoft.com)
Remote

WitchSoft is my own one-man company.

I created [PITowalut.pl](https://pitowalut.pl), a website that helps with calculations for Polish PIT-38 tax from transactions on foreign exchanges.

The entire transaction with the customer takes place on a single page with only a single redirect for the payment.
The payment processor used is Przelewy24.
The front-end's made with VanillaJS and PicoCSS, served from CloudFlare Pages.
It has passwordless authentication with a code sent to e-mail.
E-mails are sent with automation using a Google Workspace service account.
The back-end is hosted on Digital Ocean.
PostgreSQL serves as the data layer.
The web API is built with async Python, FastAPI, and SQLAlchemy.

### 2022.01 -- 2022.12
Senior Back-end Engineer at [Nira](https://nira.com)
Remote

Nira is a real-time access-control system.
It analyzes who has access to what documents in an organization's cloud, and allows to perform automated bulk changes
to the access permissions.
It integrated with Google Cloud, but we were working on adding support for more systems (e.g. Microsoft).

The team was 100% remote and globally-distributed, favoring asynchronous forms of communication,
and promoting a high degree of autonomy. There were up to 25 engineers on it.
Safety and confidentiality of users' data was paramount - we were HIPAA-compliant.

My main role was the development, maintenance, and ensuring reliability of Python back-end microservices
acting as our asynchronous task queue - the "Actions" service.
The service allowed to execute policy-driven and on-demand changes to document permissions via Google Workspace APIs.

My role included:
- technical leadership of the "Actions" service code and cloud infrastructure
- analyzing and improving back-end performance
- operational support of "Actions"
- Analysis and solution design for a variety of new feature bundles, which had "Actions"
  dependencies; working from product requirements to produce engineering plans and
  effort/complexity estimates, which flowed through into implementation projects
- Review of other engineer’s code as a part of quality assurance and release processes, both for
  "Actions" and the wider back-end ecosystem
- Revising and extending CI/CD pipelines based on GitHub Actions

Notable achievements:
- taking over the "Actions" codebase in 9 days,
  as the previous maintainer was leaving the company shortly after I joined
- introducing test harnesses, and performing a gradual redesign of the "Actions" codebase that improved both reliability
  and performance, all the while delivering new features
- "Actions" was capable of conducting bulk change operations for around 10 million documents
- switched out the old implementation based on AWS SQS and synchronous Python to one based on AWS MSK (Kafka)
  and asynchronous Python (with aiokafka)
- made it so that "Actions" microservices could be brought up locally (on the developers computer) with
  a single "make" command after git-cloning the repository

### 2021.01 -- 2022.01
Working on my own software, cryptocurrency trading

I was trading cryptocurrencies to get income while I was working on my own software.
The latter included (but was not limited to):
- a multi-platform desktop Kivy app that I intend to productize in the future
- an app to keep track of and plan my finances and investments
- [scripts](https://github.com/butla/machine_setups) for setting up my OS, and keeping it updated and synced across
  computers

### 2018.11 -- 2021.01
Senior DevOps Engineer at British Telecom (BT)
Remote, with occasional meetings in London, Ipswich, and Brentwood

Main project: Vena (https://www.mediaandbroadcast.bt.com/vena.html)

I worked on a team of external contractors,
tasked with developing a web application for designing telecom infrastructure
and an automated initial configuration of Cisco and Juniper routers.
To do that we had to work intensely with BT engineers from various teams,
piecing together the knowledge about company's current processes,
and helping design the requested solution, that was supposed to fit into a grander project.

We were all supposed to be universal developers, writing code, preparing its deployments
and interacting with any hardware necessary.
We didn't have a traditional team leader, which was an interesting exercise in self-organization.
My application team had 4 to 8 persons (it was growing), but the entire project had many teams.

The whole project was also part of the organization's agile transformation,
with our contractor team leading the way.

Prominent technologies used:

- Django and Django REST Framework - most of our back-end and front-end
- PostgreSQL - our main database
- Kubernetes and Helm - deployments
- Nginx - reverse proxy
- Docker Compose - running a local, development instance of the app with its dependencies
- Minio - serving our web app's static assets, and storing media files
- Celery - running asynchronous graphs of tasks (with the "canvas" feature)
- ReactJS - a few more dynamic front-end pages
- Faust - reading streams of events from other systems from Kafka
- Redis - caching, Celery broker
- Sentry - error tracking
- Prometheus - metrics
- Junos PyEZ - managing Juniper routers
- netmiko - managing Cisco routers
- GitLab - code repository / continuous delivery pipelines
- Factory Boy - easy creation of ORM objects for tests
- terminal servers - logging in over SSH and getting a serial port terminal to the routers

My niches in the team were:

- code and infrastructure design for new features
- setting up automated tests and speeding them up
- refactoring for testability
- thorough code reviews
- teaching advanced Python and testable design to other team-members
- advocating for simple and tried OpenSource solutions we could control
  over heavier enterprise ones there wasn't enough team expertise in
- taking care of deployments and infrastructure (along with one other team member)


### 2017.05 -- 2018.09
Python Back-end Developer at Iterio Data (https://iteriodata.com/)
Remote

My main project was a data pipeline for advertisement campaign and site traffic analysis.
I worked as the main developer and the de facto architect of the system.
Later on I also took over the maintenance and design of our cloud infrastructure.
Other than that I did some ETL, the occasional simple data analysis, and polished up some old automations.

An important thing I learned here is that with the right tools and the right engineers, a small team
(4, in this case) can create a web application processing the data of millions of people.

My duties included:

- creating back-end APIs with asynchronous Python (AioHTTP) and stuffing them in Docker containers
- designing our systems on AWS (ECS, Lambda, Kinesis, S3, CloudWatch)
- encoding our infrastructure and doing deployments with Terraform
- creating test strategies and tools for our cloud applications (including chaos testing)
- maintaining the quality of our services by doing stress tests and performance testing / monitoring
- helping in the design of our CitusDB (distributed PostgreSQL) schema
- setting up logging (CloudWatch, Google Stackdriver), metrics, and alerts (Sentry, PagerDuty)
- working out our development practices (trunk-based development, zero down-time deployments, etc.)
- maintaining old scripts that used enterprise SOAP web services (introduced Zeep to make that easier)

We worked like start-ups do, so there was context-switching and were always time-starved.
Because of that the code I wrote had to be immediately understandable for me and my boss,
who isn't a senior Python developer and was even more time-starved than me.
He wanted to jump in real quick and tweak a few things from time to time,
so extending the code had to be obvious as well.

Another hard job was picking what to test and how to do it.
Tests were meant to actually save us time by not having to
"deploy and poke around to see if everything seemed fine" after a change.
We sometimes invested a lot of time in working out testing techniques for areas like
AWS Lambda and microservices, because there doesn't seem to be enough literature on the topic.
But sometimes there was just not enough time to test everything.
Luckily, some parts of the system weren't user-facing,
and putting them offline for a couple of minutes wasn't an issue (since we had queues,
payload backups, etc.).
So if anything went wrong while introducing changes to them, we'd be notified by our alerting system,
and immediately implement fixes, without the users noticing any problems.

### 2017.05 -- 2017.10
Ansible contractor at ScyllaDB (https://www.scylladb.com/)
Remote

I was contracted to develop Ansible scripts for installation of ScyllaDB database.
I managed to create automation for single instance installation.
Later I started working on scripts for the set up of an entire cluster, but I didn't finish them.
I was too overworked with this contract and a full-time job at Iterio, so I canceled the former.

The challenge here was mainly about having to base my work on existing complex shell scripts.
They did things like modifying the kernel settings for maximized performance.
The problem was that they were usually non-idempotent, and they were prone to modifying the machine's state.
So I had to propose changes to them and recombine their parts into the Ansible scripts.

### 2017.01 -- 2017.06
Software contractor at Techno Service SA (https://tspcb.pl/) / Siled (http://siled.pl/)
Remote, with a few factory visits in Gdańsk

The company had a multi-step manual process for creating PCB solder joint quality reports.
The initial board analysis was performed by specialized industrial machines.
I was hired to automate the process.

The old process looked like this:

- a person goes to the machine with a pendrive
- they run a software tool on the machine to download a set of testing results
- they copy the data to their computer
- they run a script that transforms the data into an Excel spreadsheet
- they send that spreadsheet to a person preparing a final report
- that last person manually copies fields from the sent spreadsheet into the final report

I created a desktop application through which you could specify batches of PCBs you were interested in,
fill out some info, and immediately get the final report spreadsheet.
That was possible because the PCB testing machine was connected to the network,
and was running an MS SQL Server instance with all the board test data.

Technologies used:

- Python 3.6
- Tkinter, chosen because the GUI was very minimal and the application had to be very easy to install on Windows
- openpyxl for reading and writing Excel files
- PyAutoGUI for testing the GUI
- VirtualBox running Windows XP and Microsoft SQL Server 2005 - used that to test data extraction from the PCB
  testing machine (it was running that version of SQL Server)

### 2014.03 -- 2016.04
Software Applications Developer at Intel Technology Poland
Gdańsk

Examples of assignments on this position, from the latest:

#### Leading a development team
I lead one of the teams that worked on Trusted Analytics Platform (TAP) project.
TAP is a PaaS platform with main focus on data analytics.
My team mainly did the integration of other teams' work, we overseen builds, deployments,
releases and utility tools, but we also developed some back-end microservices.

I was responsible for planning, estimating and coordinating work, also teaching and mentoring of other team members.
Furthermore I:

- acted as Python expert for all project teams
- created **mountepy** - a Python library to aid isolated microservice tests and increase our code quality
- influenced development procedures for all teams
- enforced software legal compliance and communicated with lawyers

#### Back-end microservices' development for TAP
I developed a few Spring Boot (Java) microservices and created one in Flask (Python).
It was a data set indexing and search service backed by ElasticSearch.
We used Cloud Foundry PaaS as a base for our applications.
Sometimes there was a need to fiddle with virtual machines on which Cloud Foundry cluster was based on.
I dabbled in load testing with Gatling (Scala) and Locust (Python).

#### Maintenance of a secure back-end for remote firmware updates (Intel Upgrade Service)
We had a mature distributed system, encompassing C# back-end services,
ASP.NET front-end, a C++ server and a C++ client.
The whole system was based on EPID digital signature scheme.
I had to deliver patches to almost all of the application-layer components
and do deployments to a large Windows-based infrastructure spread out geographically.

I also needed to run tests that touched everything from firmware on a client machine,
through its drivers and application level software up to multi-tier back-end services
and ending at server HSMs (Hardware Security Modules).

#### Implementing hardware-backed secure tunnels for certificate exchange
I needed to create a C++11 application for embedded Linux that could create,
manage and transfer X.509 certificates.
The certificates' private keys and the keys used to secure the connection to transfer them
were created and stored in a hardware cryptography module (TPM).
OpenSSL and TrouSerS were used for setup of MTLS (TLS with authentication of both parties) connections.

#### Researching using SIM cards as secure elements (SE)
Did that alone as my first task on the team.
Had to look into Java Micro Edition and smart cards.

It turns out that some SIM cards (or smart cards with SIM card's for factor) are capable of asymmetric cryptography,
but we couldn't use them easily.
We would either need to get SIM operator rights to be able to push our code onto the cards with OTA,
or we would need to get fresh custom cards from a smart card manufacturer.
Both options weren't feasible for us.


### 2011.05 -- 2014.02
Test Engineer Intern at Intel Technology Poland
Gdańsk

I maintained and developed a heterogeneous (Windows, Linux, Android) distributed framework
for automated software, firmware and hardware testing.
I've coded mainly in C# and Java (SE and Android versions), but I've helped myself with Python scripting.

My main focus was designing and implementing a versatile RPC-style communication between applications
on different platforms (used WCF on Windows, JAX-WS on Linux, and my own protocol for Android).
There was a tight collaboration with our clients - the validation teams.

Solving some problems required knowledge of obscure inner workings of .NET, Java and Windows system
(e.g. discrepancies in implementations of TCP sockets on both programming platforms).


## Notable talks

### Developer workflow with local tests using Docker Compose
Pykonik Tech Talks #62, 2023-03-30. https://youtu.be/hjve48cYj_U

This talk features:
- Docker Compose setup with the sample HTTP/REST app (written in Python) and a SQL database.
- High-level tests using containers.
- Reloading the app container on code file changes.
- Running tests on code file changes.
- Makefiles to describe common development tasks.
- CI setup based on local tests.

### TDD of Python microservices
EuroPython 2016 talk. https://youtu.be/d-ka10jngQQ

Presentation of tools (some implemented by me) and solutions that enable Test-Driven Development
of Python microservices.
Told from the perspective of a maintainer of a single service.

### Python microservices on PaaS done right
EuroPython 2015 talk. https://youtu.be/WYXkpiaGBms

A collection of tips and practices that allow to have a successful microservices-based project.
Concerns development, testing and work organization.

## Education

### 2016.03 -- 2016.05
Cryptography I course from Stanford (on Coursera)

### 2012 -- 2015
Master of Science in Computer Science
Gdańsk University of Technology

Overall score -- good plus
Specialized in Intelligent Interactive Systems (AI, computer vision, graphics)

#### Master thesis
*Calling remote Java methods in Android system from .NET platform*
Supervisor: Jacek Lebiedź, PhD MEng

The goal of this work was to create a set of libraries that would enable convenient remote code execution
in Android system from .NET platform.
The work was successful and had the side-effect of an upstream patch on `jsonrpc4j` library,
enabling it to work on Android.

### 2008 -- 2012
Bachelor of Science in Computer Science
Gdańsk University of Technology

Overall score -- good plus

#### Final project
A C++ application using OpenCV that could learn and recognize faces using the eigenvectors method.

## Languages

- Polish, native
- English, fluent

## Interests

- technology and engineering in general
- psychology
- mythology (mainly Slavic, Nordic, and Greek)
- history
- martial arts
