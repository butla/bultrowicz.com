Say it with style in CLI
========================

.. post:: 2020-04-26
   :author: Michal Bultrowicz
   :tags: CLI, Linux

So I glued some awesome software together into a shell one-liner and
now I can make my announcements with a rainbow tortoise on the CLI :)

.. raw:: html

    <script id="asciicast-4PYsHosPFHEVcL41voUl30afN" src="https://asciinema.org/a/4PYsHosPFHEVcL41voUl30afN.js" async></script>

A pointless story trying to give more context than there really is
------------------------------------------------------------------

.. raw:: html

    <img src="https://res.cloudinary.com/format-magazine-production/image/upload/c_crop,h_844,w_1500,x_0,y_0,f_jpg,f_auto/design-development-witch-109"></img>

My home is on the frontier of the CLI-Land. It's a tough but honest life - without any limitations,
but also without some conveniences.
I also work from my home, but sometimes you gotta make trips to the crowded and loud GUI-Town for some basic supplies.
Like your vital YouTube fix.

Image taken from this `article about The VVitch`_:

The code
--------

The ZSH function (should be compatible with Bash) looks like this:

.. code-block:: bash

    function say()
    {
        clear
        # I know, it's a tortoise, ugh :) Upstream problems
        cowsay -f turtle "$@" | lolcat --freq 0.2 --seed 900 --speed 300 --animate
    }

and can be found in my `configs' and scripts' repo`_.


.. _article about The VVitch: https://www.format.com/magazine/features/design/the-witch-robert-eggers-movie-interview
.. _configs' and scripts' repo: https://github.com/butla/configs_and_scripts/blob/master/home/.config/zsh/functions.zsh
