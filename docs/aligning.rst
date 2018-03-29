.. _aligning:

.. _`Brief Tutorial`: https://computers.tutsplus.com/tutorials/navigating-the-terminal-a-gentle-introduction--mac-3855

Aligning
========

Command Line
------------

.. note::
	
	All faseAlign calls are carried out via the command line or terminal. It may be useful for you to review basic terminal commands used by Linux and OSX when interacting with files. I'd suggest finding a short introduction such as this `Brief Tutorial`_. 

|
|
|

Basic Example
-------------

In most cases, the default options for faseAlign are sufficient and can be called with the following command:

.. code-block:: bash

	faseAlign -w input.wav -t transcript.TextGrid

The transcript file passed to the `-t` flag can be of type `.TextGrid` or `.txt`

.. note:: There are no positional arguments so you can order the flags however you want. 

|
|
|

Additional Options
------------------

On top of the basic aligning call, there is additional functionality available. Examples for each of these additional features are shown below. 


Change Output Location
++++++++++++++++++++++

The default location of the output TextGrid is your current working directory. This can be overwritten by passing an new directory (absolute or relative path) to the `-o` flag:

.. code-block:: bash

	faseAlign -w input.wav -t transcript.TextGrid -o /home/user/Desktop/project/


Specify Output Name
+++++++++++++++++++

The default name for output files can be changed with the `-n` flag: 

.. code-block:: bash

	faseAlign -w input.wav -t transcript.TextGrid -n new_file_name

.. _missing-alert:

Missing Words During Alignment
++++++++++++++++++++++++++++++

If you encounter words in your transcript which are not included in the default dictionary, you can choose to generate automatic phonemicizations for these missing words following Spanish orthography to phoneme rules. These automatic phonemicizations are usually correct for native Spanish vocabulary, but are often incorrect for loanwords or some place names. 

To use these automatic phonemicizations, you can use the `-p` flag: 

.. code-block:: bash

        faseAlign -w input.wav -t transcript.TextGrid -p


If there are words in your transcript that you'd like to give a custom phonemicization, you should add them to a custom local dictionary (see :ref:`missing`). Then pass the path to the new file to the `-m` flag:

.. code-block:: bash

	faseAlign -w input.wav -t transcript.TextGrid -m dict.local

Speaker Tags for txt Transcriptions
+++++++++++++++++++++++++++++++++++

Recall that .txt transcriptions have speaker tags in between braces (e.g., {Julia}, {S10}). To use these speaker tags, you have to use the `-g` flag:

.. code-block:: bash

	faseAlign -w input.wav -t transcript.txt -g Julia Marco S4

This command will correctly match the speaker tags `{Julia}`, `{Marco}`, and `{S4}`. 


Stereo Options
++++++++++++++

If you have stereo audio with speakers on separate channels, alignment can be improved by separating out speakers into their respective channels. 

First, determine which speaker is in channel 1 (left) and channel 2 (right). Now, pass those speaker labels to the `-l` and `-r` flags as well as using the `-s` flag to indicate stereo.

.. code-block:: bash

	faseAlign -w input.wav -t transcript.TextGrid -s -l S1 -r S2
