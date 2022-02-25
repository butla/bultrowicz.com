Replace REPL (ptpython) with an editor (neovim) and entr
========================================================

.. post::
   :author: Michal Bultrowicz
   :tags: Python, CLI, entr

I love to use Ptpython for some quick Python experimentation.
But I want it to be simpler to make scripts out of my interactive sessions.
My solution? Make the editor interactive :) Well, give it an interactive buddy - `entr`.

(TODO pypi link, I recommend installing with pipx, and then injecting libs to test into
it, thus making it our playground) 

When using `ptpython` it's a bit of a hassle to copy the command history (press F3) from your
interactive session and into a script. I mean, you can copy the history into an editor,
but then you have to get through all the mess you've made (all the evals) and clean it up.

I'd like but I want to experiment easily and quickly, but

Whether I want to see how something simple works, or maybe when I want to check out a library.
I also want to play with libs in virtualenvs, and maybe run parts of my projects interactively,
so I often add `ptpython` to my "dev" dependencies.

Repl is still snappier with suggestions and autocompletes. How can I make my NeoVim setup faster, people?

I start with `from pprint import pprint as p` (there should be a way to fill it in the Vim pane),
though it'd be nicer to have the print expression here.

My alternative to Python Notebooks that need JS and Web and are bad for Git.

And you can have your autoformatters (isort, black - if you're into it) in Vim is well.

 `entr <https://github.com/eradman/entr>`_
