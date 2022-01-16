Python's ContextVars - my favorite IoC container
================================================

.. post::
   :author: Michal Bultrowicz
   :tags: Python

Using ContextVars from the Python's standard library for dependency injection is a better development experience
then using anything that the web framework creators are offering, in my estimate.

What's an IoC container? What's dependency injection?
-----------------------------------------------------

IoC container (TODO link) is this pattern allowing you to do dependency injection (TODO link).
Instead of passing everything (a bit of configuration information, or a object that connects to something external,
usually) down the call stack, you just keep it in some container object.
The code that's going to use it will get it from the source.

Where does it appear?
---------------------

This is way better than using the shitty, untyped objects from Flask,
Django or even my beloved AioHTTP
(which I'm cheating on with Responder, because it got that brilliant Falcon HTTP method handler API).

You might have seen that in web frameworks (Django, Flask, AioHTTP, Falcon examples).

You could have the classic dict on the app object, but then you need to either know the key strings,
or keep them in constants somewhere.

What are context vars?
----------------------

Czy to potrzebne? może

Why is it better to use ContextVars?
------------------------------------

These have problems.

A better solution, in my opinion, is using a ContextVar (TODO link)
With ContextVars you get editor help with completions, types can also be checked.

In your app you can have a "services" module, or "ioc", or whatever, and that can have context vars that you can
change. External connectors.

Aiohttp też jest spoko z przekazywaniem obiektu. Obiekt można przekazać do contextvarsa.

When not to use ContextVars?
----------------------------

When you need to update the configuration of live components.
But gracefully recreating them with new configs is just simpler, easier, and less error-prone.
And it's more functional (in the functional programming sense) to just fire a function with some initial data
that can't be mutated.
