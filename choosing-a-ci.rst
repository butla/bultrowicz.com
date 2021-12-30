Choosing a CI service for your open-source project
==================================================

.. post:: 2016-09-18
   :author: Michal Bultrowicz
   :tags: Python, CI/CD

I host my code on GitHub, as probably many or you do [#1]_.
The easiest way to have it automatically tested in a clean environment (what everyone should do)
is, of course, to use one of the hosted CI services integrated with GitHub.

`One thing to note`_ - some take the label of "continuous integration",
some "continuous delivery", but their capabilities are similar.
Nevertheless there quite a few of them to choose...

Travis
------

I don't know if it actually is, but for me, it seems that Travis is the oldest,
most well known and most widely used from the bunch.
Because of that and because I didn't have any fancy requirements,
I was using it for `Mountepy`_ for some time (you'll see why this has changed).
Although it's quite simple, it can even be used for `automatic deployments to PyPI`_.

Travis has:

* Docker support, which I needed for my other project (`PyDAS`_);
* OS X builds, which I may need for Mountepy if and when I decide to support it [#2]_.

But it has one big problem - you have no easy way of debugging builds.
When I got strange test failures, it took a lot of guesswork
and a print-heavy version of my application to find their cause.
I knew that there had to be a better way, so it was time to look at other options [#3]_.

CircleCI
--------

Pros:

* You can SSH into the container that runs your builds/tests! (so there goes the debug problem)
* Docker support.
* OS X builds.

Cons:

* Hard to set up? Circle uses it's own build configuration YAML style (much like Travis).
  But I've struggled to get PyDAS tests (starting some processes, some Docker containers) working
  for about 5 or 10 minutes and I gave up [#4]_. I don't know...

Rumors(?):

* I've heard that it supports up to 4 parallel builds on the free plan but this is not what
  the `pricing page <https://circleci.com/pricing/>`_ says... [#5]_

Snap CI
-------

This is the CI I chose. It provided what I needed (Docker, debug) and is really
straightforward to work with.

Pros:

* Docker support. Although it's in beta and I had to contact support to have it enabled
  (which was done in a few hours), my builds run smoothly.
* Build debug. Not through SSH, but with browser-based snap-shell. I think I'd prefer SSH,
  but being able to do it in the browser is also nice.
* Build steps defined in Bash. No custom configuration syntax to learn, just plain old scripts!
* Ability to group build steps into stages; even ones that need to be triggered manually
  (good for manual or exploratory tests, legal checks, or whatever).

Cons:

* No OS X builds (Travis and Circle have them).
* Build pipeline definitions can't be easily copied between projects.
  With Travis you could just copy the config file,
  here it requires a bit more clicking around the web UI.
  Although you can still keep almost all of your logic in script files
  and just run different ones in different stages.

Codeship
--------

After I finished comparing Travis, Circle, and Snap I've remembered that there's one more thing
(probably way more than that, but I don't have all the time in the world) to look at - Codeship.

It's supposed to be really cool and all, but I found setting up the tests clunky
and I didn't have the initiative to try to get to know it since I was perfectly happy with Snap.
But you can find it to your liking, I don't know...

To be continued...
------------------

This whole quest for the right CI started because I wanted to implement
some cool automation for my project...
Stay tuned for the next post to find what I've set up with Snap CI.


.. rubric:: Footnotes

.. [#] It's just more convenient and "social" than Bitbucket and GitLab. But I'm kind of afraid of its monopoly...
.. [#] I think that right now Mountepy should work on OS X, but you'll have to install Mountebank yourself. If you want the feature create a GitHub issue.
.. [#] And this is why you have this article :)
.. [#] I didn't try that hard because by that point I've already taken a liking to Snap CI.
.. [#] If you're using Circle, please say how it is in the comments.

.. _another repository: https://github.com/butla/ci-helpers
.. _automatic deployments to PyPI: https://www.appneta.com/blog/pypi-deployment-with-travis-ci
.. _Mountepy: https://pypi.org/project/mountepy/
.. _One thing to note: https://blog.snap-ci.com/blog/2016/07/26/continuous-delivery-integration-devops-research/
.. _PyDAS: https://github.com/butla/pydas

