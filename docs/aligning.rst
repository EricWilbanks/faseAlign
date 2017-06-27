.. _aligning:

Aligning
========

Basic Example
-------------

In most cases, the default options for faseAlign are sufficient and can be called with the following command:

.. code-block:: bash
	faseAlign -w input.wav -t transcript.TextGrid

The transcript file passed to the `-t` flag can be of type `.TextGrid` or `.txt`

.. note:: There are no positional arguments so you can order the flags however you want. 


Change Output Location
----------------------

The default location of the output TextGrid is your current working directory. This can be overwritten by passing an new directory (absolute or relative path) to the `-o` flag:

.. code-block:: bash
	faseAlign -w input.wav -t transcript.TextGrid -o /home/user/Desktop/project/


Missing Words
-------------

If there are words in your transcript that are not included in the dictionary, you should add them to a custom local dictionary (see :ref:`add-missing`). Then pass the path to the new file to the `-m` flag:

.. code-block:: bash
	faseAlign -w input.wav -t transcript.TextGrid -m dict.local

Stereo Options
--------------

If you have stereo audio with speakers on separate channels, alignment can be improved by separating out speakers into their respective channels. 

First, determine which speaker is in channel 1 (left) and channel 2 (right). Now, pass those speaker labels to the `-l` and `-r` flags as well as using the `-s` flag to indicate stereo.

.. code-block:: bash
	faseAlign -w input.wav -t transcript.TextGrid -s -l S1 -r S2
