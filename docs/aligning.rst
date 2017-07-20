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

.. _missing-alert:

Missing Words During Alignment
------------------------------

By default, faseAlign generates automatic phonemicization of missing words following Spanish orthography to phoneme rules. These automatic phonemicizations are usually correct for native Spanish vocabulary, but are often incorrect for loanwords or some place names. 

If there are words in your transcript that you'd like to give a custom phonemicization, you should add them to a custom local dictionary (see :ref:`missing`). Then pass the path to the new file to the `-m` flag:

.. code-block:: bash

	faseAlign -w input.wav -t transcript.TextGrid -m dict.local

If you'd like to prevent automatic phonemicization in the first place, you can use the `-p` flag:

.. code-block:: bash

	faseAlign -w input.wav -t transcript.TextGrid -p

Now, if missing words are encountered they will be collected into an output file for you to add to your custom local dictionary.

Stereo Options
--------------

If you have stereo audio with speakers on separate channels, alignment can be improved by separating out speakers into their respective channels. 

First, determine which speaker is in channel 1 (left) and channel 2 (right). Now, pass those speaker labels to the `-l` and `-r` flags as well as using the `-s` flag to indicate stereo.

.. code-block:: bash

	faseAlign -w input.wav -t transcript.TextGrid -s -l S1 -r S2
