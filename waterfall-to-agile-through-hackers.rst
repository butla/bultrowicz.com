
Agile transformation of a waterfall-y organisations by hackers
==============================================================

.. post::
   :author: Michal Bultrowicz
   :tags: Python


The buzzwords
-------------

We can throw this around from time to time for people who's attention span is shorter than a full
sentence.

* Shift left
* DevSecOps
* ATDD (Acceptance-Test Driven Development)
* Visibility
* Continuous Delivery


Building the trust
------------------

We need to be seen as people who have the situation under control.
We need to understand the problems that were being solved by whatever ancient policies.

Usually, the policies forbid change or progress because:
- things stop working
- things become less performant (throughput, latency)
- security holes are introduced

All of those "robust" or "enterprise" distributions (CentOS, RedHat)
and software packages (Citrix, some weird IBM shit) try to solve these problems as well.
It's just that they sacrifice usability and agility, which is their great sin.

And do they even know what they are protecting from?
Can they show us the specific problems being solved, not just that they feel more secure?

Constant testing and deployments solve these problems as well,
while increasing the pace at which the project gets completed,
adding visibility/transparency of the progress
(oh, we didn't notice 12 months ago that the project won't fly).

Also, they're more interesting for developers, so you lure the best of them.

(TODO)


Testing
-------

We need to have some testing person working with us every sprint,
so that the security aren't the feelings of someone higher up the chain,
but a concrete checklist.
So that we can TRACK the security and put in on a nice visible burnout chart.

We know that we can never be absolutely secure.
But we can be as much secure,
as our logical minds can discern (all concrete acceptance tests passed),
which should be the only possible (and only sufficient) condition for engineering decisions.



You need a new distro for your vms? Just change that in an Infrastructure as Code system, deploy it to a staging environment or to a percentage of production (requires nice monitoring and failovers), run the tests and see if they pass. And that's it, the great migration done.

----



And there should be a well known way (a process, an acceptance test list) for getting clearence to change anything related to security and technology.

First, let's get something that they will have to agree with, but that logically change their position on a subject. E.g. let's allow us to have Ubuntu 18.04 machines in the Athena network in addition to CentOs 7.x'es.

18.04 is a stable enterprise platform for core systems. And it'll have 10 years of support (not the usual, very long 5). And we can just check for the security and application stability problems. We can, and we must, do functional and security testing throughout the process (shift left of all the steps on a time-line in waterfall).

Even if Ubuntu isn't enterprisey enough... What about Fedora? Which is the same stuff as RHEL and CentOs, but is thust newer packages? Does it have security holes? How? It's audited the same.
Is the potential problem functional? Let's have tests for it. And for the security. And let's just have them in the sprint retro.

If there are security issues, let them be identified and visible. We will have them, yes. But we will know them and eradicate them over the course of the project. Do you know exactly how secure are your other systems, though?

Maybe I can train to be a bit of a penetration tester. Along with my development and testing duties.

To reiterate - we need someone from another team that will constantly keep tabs on us regarding a functionally and metrically defined security checklist. Progress through that checklist will be visible to all.

And introducing security tests early can only help the design of the product.

-----

Or have you already laid out these points? Maybe the rhetoric was a bit different?

Should we present this letter to the outside people?

In their wildest dreams they couldn't predict how swift and valuable a skilled tester who is also proficient in Python and software engineering could be. We have that, and we need that. Do the BDD tests manage to achieve that?


-------

https://www.owasp.org/index.php/OWASP_Testing_Guide_v4_Table_of_Contents

Metasploit, all the python fast security checking tools (from podcasts).

--------


What did the continuous delivery book advise about project-defining documents?

------

Socratean method - show them that they don't know what they think they know. By asking questions.

-------

Data architect - WTF even is and how the hell is he/she supposed to help anyone? We just need data schema design skills.


Comparison with a different corporation (maybe take out this bit?)
------------------------------------------------------------------

I've been at Intel for 5 years, so I had some time to observe corporate bureaucracy.

It wasn't so different there. We also had to have Windows (although some people in States and
later on in some teams in Poland started getting Macs) laptops that were monitored and managed
by our IT.
But maybe it was assumed that people owning these laptops will be developers, because they
could install whatever they wanted on the laptops. As long as the licenses were OK.
Well, theoretically you were supposed to install only vetted (God knows how) software from some
internal stores, but nobody bothered with that. And it's good that they didn't.

Also, you could get desktops wired up to the LAB network (separate from the company's internal
network), which you could do anything you pleased with.
And while corporate laptops (which often were also the development machines)
were managed by the company's IT, the machines in the LAB network were the responsibility of
around a 100 people units (groups/teams).
And you could cut off your team's LAB network from the rest of it.

I see that here some people also have desktops on the internal network, but they are also not
as a open for development.

At Intel it was (sometimes) understood that each team was doing different things, had different requirements,
and had to do things differently.
Innovation and sharing that innovation with other teams was encouraged.
In practice it wasn't all sunshine and rainbows (e.g. the company-wide policies about using
Open-Source), but it was better than here.

Key takeaway: you need to be able to innovate, company-wide policy will be too low of a common
denominator for a product team to be productive.
