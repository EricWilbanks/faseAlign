.. _installation:

.. _`Berkeley Common Environment (BCE)`: http://bce.berkeley.edu/

.. _`Berkeley Phonetics Machine (BPM)`: http://linguistics.berkeley.edu/plab/guestwiki/index.php?title=Berkeley_Phonetics_Machine

.. _`faseAlign OVA image`: https://berkeley.box.com/s/v8kgr4xhb5v0tozfbeocbl34wmng6kcb

.. _`VirtualBox`: https://www.virtualbox.org

.. _`BCE Guide to Enabling Virtualization`: http://bce.berkeley.edu/enabling-virtualization-in-your-pc-bios.html

.. _`HTK website`: http://htk.eng.cam.ac.uk/register.shtml

.. _`HTK source code`: http://htk.eng.cam.ac.uk/ftp/software/HTK-3.4.1.tar.gz

.. _`conda documentation`: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

.. _`miniconda linux installation page`: https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html

.. _`miniconda macOS installation page`: https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html

Installation
============

.. note:: 

	The most user-friendly option is the :ref:`install-bpm` which has much of the required software already included. This option however takes up a large (~14GB) amount of disk space. 

	If you'd prefer to compile from source, choose either :ref:`install-linux`, :ref:`install-mac`, or :ref:`install-windows`. 

|
|
|

.. _install-bpm:

Virtual Machine Installation
----------------------------

Download BPM Image
++++++++++++++++++

The easiest way to run faseAlign on your own computer is to use a virtual machine image with the required software already included. The image we'll be using is based on the `Berkeley Phonetics Machine (BPM)`_, in turn derived from the `Berkeley Common Environment (BCE)`_. 

Download the `faseAlign OVA image`_.


Set Up Virtual Machine
++++++++++++++++++++++

First, you'll need to install `VirtualBox`_ in able to be able to run virtual machines on your computer. 

Run VirtualBox and select `File, Import Appliance...` and select the .ova file you downloaded earlier. Then adjust the amount of RAM the virtual machine is allotted (defaults are typically fine).

You can now start the virtual machine by clicking the green "Show" arrow.

.. warning:: 
	
	If you're on a Windows computer and run into errors at this step, virtualization might be disabled on your computer. 

	Follow the `BCE Guide to Enabling Virtualization`_ in order to enable virtualization. This involves editing BIOS settings, so if you don't feel comfortable making such changes consult with someone who does. 

.. note::

	The files on your virtual machine and the files on your host machine are completely separated and do not interact. 

	If you want to transfer files between the two you need to set up a *Shared Folder*.

	- Create a folder on your main computer wherever you like
	- Open up the VirtualBox application and select the virtual machine you want to add the folder to and go to *Settings*
	- Go to the *Shared Folders* tab and click the *Adds new Shared Folder* button.
	- Select the Folder you want to share and make sure you select *Auto-Mount*
	- The next time you start up the virtual machine you should find the shared folder at /media/sf_myfoldername/ or ~/Desktop/Shared/sf_myfoldername


Install HTK
+++++++++++

The HTK Toolkit is required to perform the backend acoustic modeling and alignment. Because of license requirements, HTK cannot be distributed with other software, but it is free to download for individual users. 

First, register on the `HTK website`_.

Next, open the terminal application and install/download HTK with the following code:

.. code-block:: bash

	sudo bpm-update htk

You will be prompted for the username and password from your HTK registration. 

Build the Conda env
+++++++++++++++++++

We'll be using conda to manage our python packages and prevent other version issues. For more details on conda usage, please consult the `conda documentation`_.

To build the conda environment, we'll need to download the environment.yml file, either manually or with the following command:

.. code-block:: bash

	wget https://raw.githubusercontent.com/EricWilbanks/faseAlign/master/environment.yml

Next, we'll build the environment with conda. 

.. code-block:: bash

	conda env create -f environment.yml

You should receive a success message along the lines of "Done. To activate this environment..."

Correctly Configure UTF-8
+++++++++++++++++++++++++

At this point you need to ensure that accented (UTF-8) characters are correctly interpreted. To do so, enter the following to the terminal: 

.. code-block:: bash

	echo export LC_ALL=en_US.UTF-8 >> ~/.bashrc
	echo export LC_ALL=en_US.UTF-8 >> ~/.profile
	echo export LANG=en_US.UTF-8 >> ~/.bashrc
	echo export LANG=en_US.UTF-8 >> ~/.profile
	echo export LANGUAGE=en_US.UTF-8 >> ~/.bashrc
	echo export LANGUAGE=en_US.UTF-8 >> ~/.profile

	source ~/.bashrc

Activating the fase environment
+++++++++++++++++++++++++++++++

In order to use use faseAlign on the command line, we'll now have to activate the conda environment we've just built. You have to activate this environment each time you restart the session, using the following code:

.. code-block:: bash

	conda activate fase

You should now see a `(fase)` to the left of your command line, indicating that the environment is active. To deactivate the environment, use the following:

.. code-block:: bash

	conda deactivate

For more details on conda environment usage, please consult the `conda documentation`_.

|
|
|

Build from Source
-----------------

.. note::
	
	If you'd prefer to build from the source code instead of using the Virtual Machine, choose one of the following options: :ref:`install-linux`, :ref:`install-mac`, or :ref:`install-windows`.

|
|
|

.. _install-linux:

Linux Installation
++++++++++++++++++


Downloading HTK
***************

The HTK Toolkit is required to perform the backend acoustic modeling and alignment. Because of license requirements, HTK cannot be distributed with other software, but it is free to download for individual users. 

First, register on the `HTK website`_

Then, download the `HTK source code`_. faseAlign was developed using the stable release 3.4.1 of HTK.


Compiling HTK
*************

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

Making sure you have miniconda
******************************

We'll be using conda to build an environment for faseAlign. Follow the instructions on the `miniconda linux installation page`_ and ensure that you're following the instructions for *Miniconda - Python 3.9*. 


Build the Conda env
+++++++++++++++++++

We'll be using conda to manage our python packages and prevent other version issues. For more details on conda usage, please consult the `conda documentation`_.

To build the conda environment, we'll need to download the environment.yml file, either manually or with the following command:

.. code-block:: bash

	wget https://raw.githubusercontent.com/EricWilbanks/faseAlign/master/environment.yml

Next, we'll build the environment with conda. 

.. code-block:: bash

	conda env create -f environment.yml

You should receive a success message along the lines of "Done. To activate this environment..."

Correctly Configure UTF-8
+++++++++++++++++++++++++

At this point you need to ensure that accented (UTF-8) characters are correctly interpreted. To do so, enter the following to the terminal: 

.. code-block:: bash

	echo export LC_ALL=en_US.UTF-8 >> ~/.bashrc
	echo export LC_ALL=en_US.UTF-8 >> ~/.profile
	echo export LANG=en_US.UTF-8 >> ~/.bashrc
	echo export LANG=en_US.UTF-8 >> ~/.profile
	echo export LANGUAGE=en_US.UTF-8 >> ~/.bashrc
	echo export LANGUAGE=en_US.UTF-8 >> ~/.profile

	source ~/.bashrc

Activating the fase environment
+++++++++++++++++++++++++++++++

In order to use use faseAlign on the command line, we'll now have to activate the conda environment we've just built. You have to activate this environment each time you restart the session, using the following code:

.. code-block:: bash

	conda activate fase

You should now see a `(fase)` to the left of your command line, indicating that the environment is active. To deactivate the environment, use the following:

.. code-block:: bash

	conda deactivate

For more details on conda environment usage, please consult the `conda documentation`_.

|
|
|

.. _install-mac:

macOS Installation
++++++++++++++++++

Xcode Compiler
**************

First we have to make sure that Xcode (and included GCC compiler) are installed. Open the terminal application and call the following command:

.. code-block:: bash

	xcode-select -p

If this command is not successful, install Xcode through the terminal:

.. code-block:: bash

	xcode-select --install

And select "Install"

Homebrew Installation
*********************

Next, we need a package manager. Install Homebrew through the terminal:

.. code-block:: bash

	ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Downloading HTK
***************

The HTK Toolkit is required to perform the backend acoustic modeling and alignment. Because of license requirements, HTK cannot be distributed with other software, but it is free to download for individual users. 

First, register on the `HTK website`_

Then, download the `HTK source code`_. faseAlign was developed using the stable release 3.4.1 of HTK.


Compiling HTK
*************

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

Making sure you have miniconda
******************************

We'll be using conda to build an environment for faseAlign. Follow the instructions on the `miniconda macOS installation page`_ and ensure that you're following the instructions for *Miniconda - Python 3.9*. 


Build the Conda env
+++++++++++++++++++

We'll be using conda to manage our python packages and prevent other version issues. For more details on conda usage, please consult the `conda documentation`_.

To build the conda environment, we'll need to download the environment.yml file, either manually or with the following command:

.. code-block:: bash

	wget https://raw.githubusercontent.com/EricWilbanks/faseAlign/master/environment.yml

Next, we'll build the environment with conda. 

.. code-block:: bash

	conda env create -f environment.yml

You should receive a success message along the lines of "Done. To activate this environment..."

Correctly Configure UTF-8
+++++++++++++++++++++++++

At this point you need to ensure that accented (UTF-8) characters are correctly interpreted. To do so, enter the following to the terminal: 

.. code-block:: bash

	echo export LC_ALL=en_US.UTF-8 >> ~/.bashrc
	echo export LC_ALL=en_US.UTF-8 >> ~/.profile
	echo export LANG=en_US.UTF-8 >> ~/.bashrc
	echo export LANG=en_US.UTF-8 >> ~/.profile
	echo export LANGUAGE=en_US.UTF-8 >> ~/.bashrc
	echo export LANGUAGE=en_US.UTF-8 >> ~/.profile

	source ~/.bashrc

Activating the fase environment
+++++++++++++++++++++++++++++++

In order to use use faseAlign on the command line, we'll now have to activate the conda environment we've just built. You have to activate this environment each time you restart the session, using the following code:

.. code-block:: bash

	conda activate fase

You should now see a `(fase)` to the left of your command line, indicating that the environment is active. To deactivate the environment, use the following:

.. code-block:: bash

	conda deactivate

For more details on conda environment usage, please consult the `conda documentation`_.

|
|
|

.. _install-windows:

Windows Installation
++++++++++++++++++++

Not supported. Please use the :ref:`install-bpm`.

