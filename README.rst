
Buyer Beware
------------

I am working with this with my experimental branch of pinax in my spare time.  
It should also work with pinax-trunk but I haven't tried recently.

The necessary resources are here:

    http://github.com/skyl

I haven't properly packaged the young parts.


.. Go to your apps dir and run::
   git clone git://github.com/skyl/django-geoms.git geoms
   git clone git://github.com/skyl/django-world.git world
   git clone git://github.com/skyl/django-olwidget.git olwidget


You must have geodjango, only tested with postgis (and lightly at that).

If you don't have the permissions to push/pull these repositories, 
you will have to edit the .gitmodules file to point at the public branches.
Alternately, fork the apps and the project.
Or, ask me to add you as a committer.  
(Maybe this submodule business is not the way to go).
To understand more about the setup, `check here`_


Check out this source and run::

    git submodule update --init

run a ``manage.py shell`` and::

    >>> from world import load
    >>> load.run()

as can be found in the `great GeoDjango docs`_.  
Now you have the sample world application.

.. _great GeoDjango docs: http://geodjango.org/docs/tutorial.html#id8
.. _check here: http://skyl.org/log/post/skyl/2009/11/nested-git-repositories-with-github-using-submodule-in-three-minutes/
