# Curriculum Vitae

## Contact
michal.bultrowicz@gmail.com
(+48) 790 467 660

## Summary

I'm a passionate senior software engineer with a drive for constant improvement
and a curiosity about inner workings of technologies.
I love Python, Linux, and creating robust distributed systems.
I have a strong belief in continuous testing and gradual change.

You can check out my blog at https://bultrowicz.com/ and my GitHub account at https://github.com/butla.

## Computer skills

- expert in Python programming
- secondary programming languages: Bash, Java, C++, C#
- writing understandable and testable code
- web development with AioHTTP, Falcon, Flask, and Django
- advanced web application testing (including microservices)
- ensuring high availability (HA)
- good knowledge of optimizing SQL for PostgreSQL (and scaling it out with CitusDB)
- working with various data stores: Redis, Kafka (and AWS Kinesis), ElasticSearch, S3/MinIO, Amazon Redshift
- using containers for deployments and testing (Docker, Kubernetes, Helm)
- implementing web security (X.509, mTLS, JWT, OAuth2)
- automated infrastructure management with Terraform and Ansible
- data engineering (building data pipelines and ETL systems)
- working with AWS, GCP, and DigitalOcean clouds
- implementing Continuous Delivery with the help of Gitlab CD (Jenkins in the past)
- proficiency in GIT
- exposure to building front-end with ReactJS
- able to work within just the terminal, without a graphical environment
- Linux system administration

## Soft skills

- working in and coordinating a Scrum or Kanban team
- teaching developers through thorough code reviews
- knowledge of software legal compliance and licensing issues
- analyzing tensions between teams within a project (do the teams have incentive to really cooperate?)

## Experience

November 2019 - January 2021
Senior DevOps Engineer at British Telecom (BT) (remote, meetings in London and Ipswich)

pełniłem funkcje starszego inżyniera trochę od wszystkiego. Najwięcej udzielałem się przy projektowaniu aplikacji i tworzeniu dla niej testów.
Uczyłem innych członków zespołu pisać bardziej czytelny i testowalny kod (dużo cierpliwych i skrupulatnych code review)
Ustawiałem nasze CI i lokalne testy.
Współtworzyłem nasze deploymenty do Kubernetesa przy użyciu Helm chartów.
Zadbałem, żebyśmy mogli developować (uruchamiać i testować) nasz kod bez dostępu do korporacyjnej sieci, co zwiększało naszą produktywność.
Czasem trochę pisałem templateów Djangowych w HTML i JS. Też pracowałem przy apce w Reactcie
Przedstawiałem pomysły na design i broniłem ich przed szerszą publiką z różnych stron managementu.

\cventry{May 2017 -- September 2018}{Python back-end developer}{\textsc{Iterio Data}}{Remote}{}{
My main project was a data pipeline for advertisement campaign and site traffic analysis.
I worked as the main developer and the de facto architect of the system.
Later on I also took over the maintenance and design of our cloud infrastructure.
Other than that I did some ETL and occasional simple data analysis.
My duties included:
\begin{itemize}
    \item creating back-end APIs with Python and stuffing them in Docker containers;
    \item designing our systems on AWS (ECS, Lambda, Kinesis, S3, SSM);
    \item encoding our infrastructure and doing deployments with Terraform;
    \item creating test strategies and tools for our cloud applications;
    \item helping in the design of our CitusDB (distributed PostgreSQL) schema;
    \item setting up logging, metrics, and alerts;
    \item working out our development practices (trunk-based development, zero down-time deployments, etc.);
\end{itemize}}

My duties included:
- creating back-end APIs with Python and stuffing them in Docker containers;
- encoding our infrastructure and doing deployments with Terraform;
- designing our systems on AWS (ECS, Lambda, Kinesis, S3);
- helping in the design of our CitusDB (distributed PostgreSQL) schema;
- setting up centralised logging (Google Stackdriver, AWS CloudWatch), metrics, and alerts (PagerDuty);
- trying not to create glaring security risks;
- setting up our development practices (trunk-based development, zero down-time deployments, etc.);

We worked like start-ups do, so we were context-switching and were always time-starved.
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
payload backups, etc.). So if anything went wrong, we'd be notified by our alerting system,
and immediately implement fixes.

Iterio:

- was the main python guy.
 First made some scripts more maintainable, 
 rewrote them with proper python restructured for testability and added the tests.
- I learned a lot about silicon valley-type tech startup business (and what the "data" companies make money on)
- learned the value of good services and tools - being able to run this whole huge thing with just 3 people.
- Zeep, SOAP,

%------------------------------------------------

\cventry{March 2017 -- September 2017}{Freelance projects}{}{}{}{
\begin{itemize}
\item Python 3.6 Windows GUI application for reporting of manufacturing faults in PCB boards. It merged data from Excel spreadsheets and Microsoft Access databases.
\item Developing Ansible scripts for the deployment of ScyllaDB.
\end{itemize}}

%------------------------------------------------

\cventry{March 2014 -- April 2016}{Software Applications Developer}{\textsc{Intel Technology Poland}}{Gdańsk}{}{
Examples of assignments on this position, from the latest:
\begin{itemize}
\item \emph{Leading a development team} I lead one of the teams that worked on Trusted Analytics Platform (TAP) project. TAP is a PaaS platform with main focus on data analytics.
My team mainly did the integration of other teams' work, we overseen builds, deployments, releases and utility tools, but we also developed some back-end microservices.
I was responsible for planning, estimating and coordinating work, also teaching and mentoring of other team members.
Furthermore I:
\begin{itemize}
    \item acted as Python expert for all project teams;
    \item created \texttt{mountepy} Python library to aid isolated microservice tests and increase our quality;
    \item influenced development procedures for all teams;
    \item enforced software legal compliance and communicated with lawyers.
\end{itemize}
\item \emph{Back-end microservices' development for TAP} I developed a few Spring Boot (Java) microservices and created one in Python. It was a data set indexing and search service backed by ElasticSearch. We used Cloud Foundry PaaS as a base for our applications. Sometimes there was a need to fiddle with virtual machines on which Cloud Foundry cluster was based on.
\item \emph{Maintenance of a secure back-end for remote firmware updates} We had a quite mature distributed system, encompassing C\# back-end services, ASP.NET front-end, a C++ server and a C++ client.
The whole system was based on EPID digital signature scheme.
I had to deliver patches to almost all of the application-layer components and do deployments to a large infrastructure spread out geographically. I also needed to run tests that touched everything from firmware on a client machine, through its drivers and application level software up to multi-tier back-end services and ending at server HSMs (Hardware Security Modules).
\item \emph{Implementing hardware-backed secure tunnels for certificate exchange} I needed to create a C++11 application for embedded Linux that could create, manage and transfer X.509 certificates. The certificates' private keys and the keys used to secure the connection to transfer them were created and stored in a hardware cryptography module (TPM). OpenSSL and TrouSerS were used for setup of MTLS (TLS with authentication of both parties) connections.
\end{itemize}}

I was a part of a team developing secure distributed applications. I dealt with a broad spectrum of system components, like client middleware (C++ 11), server applications (Java), hardware security modules (using OpenSSL with plugins) and embedded platforms.

During the latter period of this job I was leading a team of developers responsible for integration and delivery of a microservices-based cloud platform (Trusted Analytics Platform).

Tutaj też się musiałem jebać z tymi licencjami wszystkimi, patrzeć, czy nie mamy jakiś copy leftów, gadać z prawnikiem o intepretacjach dynamicznego linkowania dla LGPL czy tam GPL.

%------------------------------------------------

\cventry{May 2011 -- February 2014}{Test Engineer Intern}{\textsc{Intel Technology Poland}}{Gdańsk}{}{
I maintained and developed a heterogeneous (Windows, Linux, Android) distributed framework for automated software, firmware and hardware testing. I've coded mainly in C\# and Java (SE and Android versions), but I've helped myself with Python scripting.
My main focus was designing and implementing a versatile RPC-style communication between applications on different platforms (used WCF, JAX-WS and my own protocol for Android). There was a tight collaboration with our client - the validation teams.
Solving some problems required knowledge of obscure inner workings of .NET, Java and Windows system (e.g. discrepancies in implementations of TCP sockets on both programming platforms).}

I maintained and developed a heterogeneous (Windows, Linux, Android) distributed framework for automated software, firmware and hardware testing. I've coded mainly in C# and Java (SE and Android versions), but I've helped myself with Python scripting.
My main focus was designing and implementing a versatile RPC-style communication between applications on different platforms (used WCF, JAX-WS and my own protocol for Android). There was a tight collaboration with our client - the validation teams.
Solving some problems required knowledge of obscure inner workings of .NET, Java and Windows system (e.g. discrepancies in implementations of TCP sockets on both programming platforms).

## notki

CV
====

CV musi zawierać przy pracach te rzeczy, których się nauczyłem lub które badałem.

Soft skillsy - non-threatening communication (mimo, że pracuje z wieloma osobami o różnym poziomie trzeba przedstawiać ludziom wszystko pozytywnie dla nich, aby ich nie odciąć).

W BT nauczyłem się też pracy z internal politics, gdzie są grupy o różnych interesach.

U webstera AWS i GCP. Logowanie centralne do stackdrivera, metryki wyciągane z niego dzięki structlogowi. Szybki async python. Bez ORM. Optymalizacja query pod rozproszonego postgresa, w ogóle poznanie dobrze optymalizacji postgresa. Wygodny cacheing z aiocache.

Zrobiłem agenta androidowego. Ponieważ WCF był używany jako mechanizm remote calli stworzyłem most do javoeym soap serwisów oraz prostszy mechanizm dla Androida (nie było kodu dla serwerów soap).

U webstera używałem soapa też, ale już z pythonem, do enterpriseoeych web serviceów od rozmów konsultantów.

pomagać też w rekrutacji programistów różnych szczeblów do utrzymania danego systemu. Oferować ziomkom, że jak podejmą się linuxa, to ich płaca będzie wyglądała tak, po roku tak, potem tak. Sprawdzać regularnie jak im idzie.

Jak syf z mikroserwisami doprowadził mnie do poważnego zastanowienia się nad testami.

Lista przeczytanych książek, kursów (crypto) i publikacje (w książce z konferencji), ważniejsze prezentacje (youtuby konferencyjne) i link do bloga (może dodaj te kilka artykułów).

Summary tego, kim teraz jestem i jakie usługi oferuję na początku. Consultation, setting up and improving software and data delivery pipelines.
Znajdowanie złych struktur.

Dostaję kasę za wdrożenie konkretnych rzeczy, za podszkolenie pracowników. Potem za support tego wszystkiego, jeśli chcecie. Jak nie, to wszystko zostaje w waszych rękach, możecie robić z tym co chcecie i możecie też płacić komuś innemu za utrzymanie.

CV po angielsku i po polsku.

Kontrakt dla Żydów.

Kontrakt dla siledu.

Opisać, że Secure Element dało by się zrobić na urządzeniach typu karta SIM (a tym bardziej chipach z kart kredytowych, które mają możliwość robienia kryptografii asynchronicznej), ale jest bardzo mało informacji online, jest to raczej hermetyczny rynek, no i trzeba być zarejestrowanym operatorem kart SIM, żeby móc coś do nich dodawać przez OTA upgrades. Ale pewnie możnaby zamówić chipy od producenta, ale to już większa zabawa.

## Noteable conference talks

\cventry{July 2016}{TDD of Python microservices}{\textsc{EuroPython 2016}}{}{}{Presentation of tools (some implemented by me) and solutions that enable Test-Driven Development of Python microservices. Told from the perspective of a maintainer of a single service. Available on YouTube.}
\cventry{July 2015}{Python microservices on PaaS done right}{\textsc{EuroPython 2015}}{}{}{A a collection of tips and practices that allow to have a successful microservices-based project. Concerns development, testing and work organization. There's a slight focus on Python. Available on YouTube.}

## Education

DODAĆ ten kurs z coursery/stanforda - Cryptography I
Kiedy on był?

\cventry{2012--2015}{Master of Science in Computer Science}{Gdańsk University of Technology}{}{\textit{Overall score -- good plus}}{Specialized in Intelligent Interactive Systems}  % Arguments not required can be left empty
Napisz, że pracą było uczenie i rozpoznawanie twarzy metodą eigenvectors przy pomocy OpenCV
\cventry{2008--2012}{Bachelor of Science in Computer Science}{Gdańsk University of Technology}{}{\textit{Overall score -- good plus}}{}

TODO wsadź to do magisterki
\section{Masters Thesis}

\cvitem{Title}{\emph{Calling remote Java methods in Android system from .NET platform}}
\cvitem{Supervisor}{Jacek Lebiedź, PhD MEng}
\cvitem{Description}{The goal of this work was to create a set of libraries that would enable convenient remote code execution in Android system from .NET platform. The work was successful and had the side-effect of an upstream patch on \texttt{jsonrpc4j} library, enabling it to work on Android.}


## Languages

- Polish, native
- English, fluent

## Interests

- Technology
- Evolutionary Psychology
- History
- Mythology (mainly Slavic, Nordic and Greek)
- Martial arts
