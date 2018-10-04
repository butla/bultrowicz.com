A simple self-modifying function in Python
==========================================

.. post:: 2018-10-04
   :author: Michal Bultrowicz
   :tags: Python
   

Replacing its own definition is a fun/horrifying thing that a Python function can do:

.. code-block:: python

    def bla():
        def new_bla():
            print('new bla')

        global bla
        bla = new_bla

        print('bla')

    bla()  # prints "bla"
    bla()  # prints "new bla"

I don't have any use for this trick, but mayyyyyybe you can use that for lazy initialization
of something, and then not wasting (a tiny bit of) time on the ``if`` check in subsequent
function calls? E.g., replacing

.. code-block:: python

    global_resource = None

    def do_something_with_lazy_initialization():
        if global_resource is None:
            global_resource = initialize_the_resource()
        print('about to do stuff')
        do_stuff_with(global_resource)

with

.. code-block:: python

    def do_something_with_lazy_initialization():
        def actually_doing_something():
            print('about to do stuff')
            do_stuff_with(global_resource)

        global_resource = initialize_the_resource()

        global do_something_with_lazy_initialization
        do_something_with_lazy_initialization = actually_doing_something

        actually_doing_something()
