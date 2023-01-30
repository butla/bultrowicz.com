Migrating from Wunderlist to Trello, and my beef with some API design decisions
===============================================================================

.. post::
   :author: Michal Bultrowicz
   :tags: Python

You can read my articles in parts if the title doesn't look interesting to you.
I'm gonna try out this convention for a while and see if it works.
If I get any feedback :D

These kinds of blog posts will not only present specific issues, but also show
how I do my work, research, and reasoning. So they may even be of some value if your
not exactly interested in the subject itself.

Or maybe just put that in specific posts? First about the job to be done,
the others about implications, ramblings, ideas for improvement, tool workflows.

Have this thing in chapters like:

* back in the saddle?
* Wunderlist API frustrations
* Trello API frustrations
* Trello library API frustrations
* My solution
* Advice on exploratory coding

I'm out of work again, so maybe, finally, I'll be able to write some articles for this blog.
Ideally, I'll get the hang of it so good that it won't be a problem to churn out a blog post once
every few weeks when I'm back at work again.

The Python API seems old and supports only Python 2. Also, how do you pass the tokens through it?

As for Wunderlist I was I bit puzzled that the only libraries were at like 0.1 and didn't seem
to have been touched in a long while.
The API docs seemed more confusing than Trello's (which are good, but somehow I couldn't get
a single call to work for a long while and I got unhelpful 401 messages), but luckily,
I don't need to use the API, cause I can just export everything in a single JSON.
And the less code you need to write the better. And since I'm migrating once and for good
I don't need to have the code in place to pull stuff from Wunderlist.

Hell, if I didn't have as many items, a lot of them having some notes or sublists in them,
I'd just do it manually. But right now it would probably take me a bit more to transcribe that
manually than it'll take me to write the code and this post. Although it'd be a lesser
mental effort. But then again, I'd probably need to go through the items multiple times making
sure I didn't omit anything - and that would be stressful for me.

Also, I want to keep the history of my Wunderlist (items marked as done) as archived cards,
so I don't ever need to get back to Wunderlist and can just purge it from my memory.

Broken example in the Python library docs:
https://pypi.org/project/trello/ ->
https://pythonhosted.org/trello/ ->
https://pythonhosted.org/trello/examples.html

>>> from trello import TrelloApi

>>> trello = TrelloApi('MY_KEY')

>>> trello.boards.get('MY_ID')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/butla/.virtualenvs/trello/local/lib/python2.7/site-packages/trello/boards.py", line 13, in get
    resp.raise_for_status()
  File "/home/butla/.virtualenvs/trello/local/lib/python2.7/site-packages/requests/models.py", line 939, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
HTTPError: 401 Client Error: Unauthorized for url: https://trello.com/1/boards/MY_ID?key=MY_KEY
401 Client Error: Unauthorized for url: https://trello.com/1/boards/MY_ID?key=MY_KEY

They probably didn't handle 401's properly. And the paths are a bit weird (why /1/boards/me instead of /boards?, we can always add /2 later, but until versioning comes into play there's no need of it)

That wasn't helpful. Later, in the reference (https://pythonhosted.org/trello/trello.html)
I noticed you can pass the token, and then it works, but still, debugging the simplest examples
is always a very bad experience for me as a library / tool user.
And still, the fact of having to use Python 2 remains. Yuck.

I think my trello_call function is more practical than the Trello API codebase...
OK, maybe it isn't cause you need to know the paths.
But creating the paths automatically based on some arguments could be good, so that
you don't have a lot of boiler-plate in the code, but working interactively yields
completions. But you won't get static completions, like with Jedi, Pycharm,
VS Code with the Python plugin, or whatever you are using.

Damn, the API was so big, I had to deal with checklist items, cards, lists, boards, members(?),
and everything had a slightly different interface, by that I mean paths and enpoint params
(in the query? on the path? who knows, definitely not in the POST body)
I almost got to using the Python 2 client, cause at least with ptpython I could figure out how
to do stuff without spending half a day in the documentation (paths aren't self-explanatory,
also, HATEOAS would be nice here with options like "add list to board,
"add checklist item to checklist")

It the code gets too big for your interactive session, you should check ptpython history,
check the interesting lines, open visual mode, copy everything into VIM with the code,
and then work on the code side by side checking things out in the interactive terminal.
Also, looking at the code will give you an overview of the valuable variables and functions
have in your session.
And you can extract the data retrieved interactively into constants of the script.
Write everything in code transitions that can be run very quickly and evaluated from the CLI
(have it open as one of the 3 panes in Tmux).

Use dataclasses? Don't have a class List and then add methods for that to get all the
lists for the user.
I think it's better to create functions which give you stuff for the user and are easy to
discover.
Or you can just install ``dataclasses`` with ``pip`` in python3.6 as a backport.

And hell, I used pipenv with python3.7 cause I can. I could have used virtualenvwrapper as
well, since I have python 3.7 installed with the deadsnakes PPA.

pipenv install requests --python 3.7
lub
mkvirtualenv -p python3.7 wunderlist_trello

Show how I copy between two panes - VIM and ptpython.

It took me the whole, lazy, distracted Saturday to do this, though.
I was distracted by hacking while playing heroes 3 hot seats with
some friends.

200 Status with a 404 page being returned - great!
no matter whether I specify content-type JSON.
I'm bashing their API, but no hard feelings, it's just technical.
At the same time I don't think it's gonna hurt them, and it shows
that even big players aren't perfect.

After I got main functions I was just running the whole script over and over, or starting
a new ptpython session and just pasting the whole file (yanked with a single Vim command).

Jesus, notes are separate objects to tasks, ugh.
This probably matches the database structure and I'm guessing that they didn't want to
return the note text just when getting the items, but that can be achieved with
proper SQL.
