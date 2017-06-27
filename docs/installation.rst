.. _installation:
Installation
============


.. warning:: faseAlign has currently only been tested on Linux (Ubuntu 16.04). It is likely compatible with OS X and likely *incompatible* with Windows at the moment. 

.. topic:: Requirements
	
	Before using faseAlign, you should check to make sure that you have the following requirements already installed.
	* Python version 3.0+ 
	* HTK Toolkit

	Making sure you have Python3
	----------------------------
	faseAlign is set to run using Python 3 if you have a compatible version installed. To check to see if you have Python 3 installed, execute the following code at the command line::

		python3 --version

	If you encounter an error, you likely need to install Python 3. You can find a suitable distribution at `Official Python Website <https://www.python.org/downloads/>`_. faseAlign was developed on Python 3.5.1 and has not yet been fully tested on all major Python3 releases.

	Downloading HTK Toolkit
	----------------------
	The HTK Toolkit is required to perform the backend acoustic modeling and alignment. Because of the license requirements, HTK cannot be distributed with other software, but it is free to download for individual users. 

	First, register on the `HTK website <http://htk.eng.cam.ac.uk/register.shtml>`_.

	Then, download the `HTK source code <http://htk.eng.cam.ac.uk/download.shtml>`_. faseAlign was developed with the stable release 3.4.1.

	Compiling HTK Toolkit
	---------------------
	Once the zipped source code has been downloaded. Locate the downloaded file and execute the following command to unpack it::
		tar -xvzf HTK-3.4.1.tar.gz
	Now move into the newly created `htk` directory::
		cd htk
	Finally, execute the following lines of code to compile and install HTK::
		export CPPFLAGS=-UPHNALG
		./configure --disable-hlmtools --disable-hslab --without-x
		make all
		sudo make install
	If your installation was successful, the following command should print out the version information for the HTK toolkit::
		HVite -V