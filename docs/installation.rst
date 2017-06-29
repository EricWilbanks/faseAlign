.. _installation:

Installation
============

.. warning:: faseAlign has currently only been tested on Linux (Ubuntu 16.04). 

.. note:: 

	Choose either :ref:`install-linux`, :ref:`install-mac`, or :ref:`install-windows`. 

.. _install-linux:

Linux Installation
-------------------

Making sure you have Python 3
+++++++++++++++++++++++++++++

faseAlign is developed to run using Python 3. To check to see if you have Python 3 installed, execute the following code at the command line:

.. code-block:: bash

	python3 --version

If this command fails, you need to install a newer version of python:

.. code-block:: bash

	sudo apt-get install python3.6


.. note:: faseAlign has been tested on major Python releases 3.4+.


Downloading HTK
+++++++++++++++

The HTK Toolkit is required to perform the backend acoustic modeling and alignment. Because of license requirements, HTK cannot be distributed with other software, but it is free to download for individual users. 

First, register on the `HTK website <http://htk.eng.cam.ac.uk/register.shtml>`_.

Then, download the `HTK source code <http://htk.eng.cam.ac.uk/download.shtml>`_. faseAlign was developed using the stable release 3.4.1 of HTK.


Compiling HTK
+++++++++++++

Once the zipped source code has been downloaded. Navigate to the downloaded file and execute the following command to unpack it:

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

Package installation and configuration is taken care of by pip and git.

.. code-block:: bash

	sudo apt-get install git

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

macOS Installation
-------------------

Xcode Compiler
++++++++++++++

First we have to make sure that Xcode (and included GCC compiler) are installed. Open the terminal application and call the following command:

.. code-block:: bash

	xcode-select -p

If this command is not successful, install Xcode through the terminal:

.. code-block:: bash

	xcode-select --install

And select "Install"

Homebrew Installation
+++++++++++++++++++++

Next, we need a package manager. Install Homebrew through the terminal:

.. code-block:: bash

	ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Making sure you have Python 3
+++++++++++++++++++++++++++++

Now we make sure we have a current version of Python3:

.. code-block:: bash

	brew install python3

.. _install-windows:

Downloading HTK
+++++++++++++++

Compiling HTK
+++++++++++++++


Windows Installation
--------------------



