
Buyer Beware
------------

I am working with this with my experimental branch of pinax in my spare time.  
It should also work with pinax-trunk but I haven't tried recently.

The necessary resources are here:

    http://github.com/skyl

I haven't properly packaged the young parts.


.. Note that this and the following lines are a rst comment
   I'm still not exactly sure how I want to handle the submodules.
   --> :P
   Go to your apps dir and run::
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

You can fork this repository and then::

    git clone git@github.com:yourNameHere/pinax-geo_basic.git 

Likewise, if you would like to change the source of the world, geoms or olwidget app, fork them
and edit ``.gitmodules`` to point to your forks.  Alternately, change from the form::

    git@github.com:skyl/pinax-geo_basic.git  

To::

    git://github.com/skyl/pinax-geo_basic.git 

Now, you should be able to run::

    git submodule update --init

run a ``manage.py shell`` and::

    >>> from world import load
    >>> load.run()

Now you have the sample world application.

If you want to work on the submodules, go into the directory such as::

    $ cd apps/geoms

and checkout the master branch before you start to modify the app::

    $ git checkout master

.. _check here: http://skyl.org/log/post/skyl/2009/11/nested-git-repositories-with-github-using-submodule-in-three-minutes/
