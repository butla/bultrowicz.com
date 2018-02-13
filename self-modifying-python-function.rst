
A self-modifying function in Python
===================================

.. post:: 
   :author: Michal Bultrowicz
   :tags: Python
   


def bla():
    global bla
    def nowa():
        print('potem')
    bla = nowa
    print('teraz')
