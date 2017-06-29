.. _installation:

Installation
============

.. warning:: faseAlign has currently only been tested on Linux (Ubuntu 16.04). 

.. note:: 

	Choose either :ref:`_install-linux`, `Mac OS <installation#install-mac>`_, or `Windows <installation#install-windows>`_? 

.. _install-linux:

Linux Installation
-------------------

.. topic:: Requirements
	
	Before using faseAlign, you should check to make sure that you have the following requirements already installed.

	*	Python version 3.4+ 
	*	HTK Toolkit
	*	git


Making sure you have Python 3
+++++++++++++++++++++++++++++

faseAlign is developed to run using Python 3. To check to see if you have Python 3 installed, execute the following code at the command line:

.. code-block:: bash

	python --version

If your version is not Python 3, you can find a suitable distribution at the `Official Python Website <https://www.python.org/downloads/>`_. faseAlign has been tested on major Python releases 3.4+.

.. note::
	If you have multiple python versions installed but your default is <3, you can check using the following:

	.. code-block:: bash

		python3 --version

Downloading HTK
+++++++++++++++

The HTK Toolkit is required to perform the backend acoustic modeling and alignment. Because of license requirements, HTK cannot be distributed with other software, but it is free to download for individual users. 

First, register on the `HTK website <http://htk.eng.cam.ac.uk/register.shtml>`_.

Then, download the `HTK source code <http://htk.eng.cam.ac.uk/download.shtml>`_. faseAlign was developed using the stable release 3.4.1 of HTK.


Compiling HTK
+++++++++++++

Once the zipped source code has been downloaded. Locate the downloaded file and execute the following command to unpack it:

.. code-block::	bash

	tar -xvzf HTK-3.4.1.tar.gz

Now move into the newly created `htk` directory:

.. code-block:: bash

	cd htk

Finally, execute the following lines of code to compile and install HTK:

.. code-block:: bash

	export CPPFLAGS=-UPHNALG
	./configure --disable-hlmtools --disable-hslab --without-x
	make all
	sudo make install

If your installation was successful, the following command should print out the version information for the HTK toolkit:

.. code-block:: bash

	HVite -V

Installing git
++++++++++++++

Package installation and configuration is taken care of by pip and git. Follow the instructions on `git's website <https://git-scm.com/downloads>`_ to make sure you have it on your system.

Installing faseAlign
++++++++++++++++++++

Once git is installed, you can download and install the newest version of faseAlign using the following command:

.. code-block:: bash

	pip install git+git://github.com/EricWilbanks/faseAlign --upgrade


.. note:: This assumes that your default pip version is pip3+ and is associated with Python 3+ site-packages. To check your default pip version, use the following command:

	.. code-block:: bash

		pip -V

	If the version is not 3+, you should change `pip` to `pip3` in the install command:

	.. code-block:: bash

		pip3 install git+git://github.com/EricWilbanks/faseAlign --upgrade


.. _install-mac:

Mac OS Installation
-------------------


.. _install-windows:

Windows Installation
--------------------



