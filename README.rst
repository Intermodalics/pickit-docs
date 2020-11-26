Pickit docs
============

Build html on Docker
--------------------
A Dockerfile is included to build & host the html with the ReadTheDocs Theme locally.
The docker container runs `sphinx-autobuild` which automatically watches for changes
so you don't have to manually rebuild everytime you change something.

Build the image:

.. code-block:: bash

    docker build --tag=pickit-docs .

Run the docker container:

.. code-block:: bash

    docker run -it --rm -p 8000:8000 --name pickit-docs -v $PWD/docs:/workdir/docs pickit-docs

You can now access the documentation at http://localhost:8000.

If you want to get the static html files, you can copy them from the running container:

.. code-block:: bash

    docker cp pickit-docs:/workdir/_build /tmp/

The errors of the build process are printed on the screen.
