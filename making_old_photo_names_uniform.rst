Making old phone photo names uniform
====================================

.. post::
   :author: Michal Bultrowicz
   :tags: Linux, Python, photos, data_management

There are photo name formats that make more sense than other.
But I see a "best one" among them - the `ISO 8601 timestamp <https://en.wikipedia.org/wiki/ISO_8601>`_.

The format
----------

I might get to using the full-length, full-featured version of ISO 8601 eventually.
But right now I prefer a version of it.
Something that Samsung phones do by default, which is quite sensible - the
``<year><month><day>_<hour><minute><second>`` format (e.g. 20220401_153214).
If we get duplicates on the same second, a number can get appended, you probably get it
(if you don't, leave a comment and I'll explain :) ).

Makes sense, tells you the date up front, allows for easy chronological sorting,
doesn't loop over and produce an anachronistic mess like the ``IMG_<four digit number>`` (TODO complain about
wife's iphone).

TODO
Laugh at Iphone (link to that article help ticket about not being able to change photo name format.)

My task
-------

Within my directories I have a directory called `z_telefonu_mego` (slightly fancy version of "from my phone"),
where I have these directories:

```
2010.09.10-2013.02.24_nokia_2710c-2
2013.04.02-2014.12.27_xperia_mini_pro
2015.01.16-2016.09.04_xperia_z3_i_z5
2016.09.13-2017.10.08_xperia_z5_nowa_seria
2016.12.19-2017.01.04_samsung_s3
2017.10.20-2020.09.23_samsung_s7
2020.09.24-onward_samsung_note10
ze_starych_TODO_rozdziel
```

Shows the first and last date of the photo and the phone model.
The last one's name's translation is "from the old TODO separate out" (yeah, Polish can be compact).
And that's what I'm about to do on this memorable couch-affinitive Sunday evening.
I'll also melt these directories into a single one, with uniform informative file names composed from the date
and the phone model.

That way I'll:
- get easy chronological sorting of the photos; helps with viewing in simple image viewers;
- maintain a visual separation of the photos' "boundaries"
  - downside here is loosing the view of how many phones I had, but that can be parsed out of the names quite easily;

Trivia
------

- I'm writing the code within my CLI setup composed from Alacritty, ZSH with plugins, Tmux,
  Vim (file editor / code IDE), and Ranger (file browser).
- I have a script that allows me to interactively edit simple scripts (writing with automating testing)
  TODO: ``new_python_script``
- it's from a repo that describes my Manjaro setup which so far maintains uniformity of two Manjaro
  laptops/operating system installs. TODO ``machine_setups``
- this is a cool thing you can get when you're working with my "interactive scripts" with entr and tmux::

    import os
    from pathlib import Path


    def main():
        # some ancient dir dragged througout the years from the times of my brother's Windows
        path = Path('~/grafika/Różne/').expanduser()
        for file in path.iterdir():
            if file.is_dir():
                print('DIR FOUND', file)
                continue

            if '~' in file.name:
                new_name = file.name.replace('~', '')
                print('renaming', file.name, 'to', new_name)

        # I'm checking where I am, just to know what can happen when I make changes.
        # I'm adding that at the end, so that I'm sure I'll see the output, even in a small window,
        # because it'll be at the end of the output.
        print(os.getcwd())


    if __name__ == '__main__':
        main()
- I ran this, saved it, got the output, then it all dissapeared. The sign of success.
  Although I didn't know where my files went, really :)::

    import os
    from pathlib import Path


    def main():
        path = Path('~/grafika/Różne/').expanduser()
        for file in path.iterdir():
            if file.is_dir():
                print('DIR FOUND', file)
                continue

            if '~' in file.name:
                new_name = file.name.replace('~', '')
                print('renaming', file.name, 'or', file.absolute(), 'to', new_name)
                file.rename(new_name)
                print('new name is', file.absolute())
        print(os.getcwd())


    if __name__ == '__main__':
        main()

- yeahh, that all went into $HOME. Should've added the full path to the rename :)
- TODO embed Screenshot_2022-04-03_23-16-37_actually_its_easy_to_find_the_files_that_were_put_in_my_home.png
