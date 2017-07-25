.. _preparation:

Preparing your Data
===================

Transcription Files
-------------------

The input to the force aligner is a wav file and the orthographic transcription associated with it. Transcriptions can be in either .TextGrid or .txt formats.

.TextGrid transcription
+++++++++++++++++++++++

.. figure:: ex_tg.png
	:alt: TextGrid transcription example
	:figclass: align-center

	*Example TextGrid Transcription*


It is **strongly suggested** to use transcriptions in Praat TextGrid format as in the above example. This approach has many benefits over the .txt transcription approach:

#. *Each speaker on a separate tier*: more accurate alignments, especially in overlap or noisy conditions
#. *Exclusion of non-transcribed sections*: the aligner will only align where there is transcribed speech, this is helpful for ignoring speech not of interest to the analysis.
#. *Aligning in small intervals*: each interval is aligned separately, increasing accuracy.
#. *Definition of speaker labels through tier names*

.txt transcriptions
+++++++++++++++++++

.. include:: example.txt
	:literal:


faseAlign also supports transcriptions in .txt format as in the above example. This approach has the benefit of not needing any determination of turn boundaries, but suffers from slightly poorer alignments. This is due to the fact that the entire wav file is aligned to the entire transcription.  In this method, speakers cannot overlap in the output alignment (since the file is processed in one linear chunk). 

Speakers are still separated into different tiers following alignment, through the use of speaker labels (e.g., {Julia}, {Speaker1}, {Marcos}) which mark utterances belonging to that speaker. 

.. note:: Make sure to use the same speaker tags throughout the transcription. `{Julia}` and `{JULIA}` would be treated as two separate speakers. 

|
|
|

Transcription Best Practices
----------------------------

Regardless of transcription method chosen, the process of transcribing is similar; you'll want to pay attention to these key points:

#. **Be as Accurate as Possible!** - This includes transcribing false starts, repetitions, omissions, etc as accurately as possible. The aligner can't find a word if it's not in the transcription!
#. **Transcribe in Breath Groups** - While this is most helpful for the TextGrid transcriptions, I also find it helpful for the txt ones as well.

#. **Spell out all accents and tildes** - otherwise words might be not be found in the dictionary
#. **Spell out all numbers and dates** - ("El veinte de marzo" instead of "el 20 de Mar.")


Additionally, the following can be used to note various non-speech items:

- {BR} - breath
- {CG} - cough
- {SIL} - silence longer than ~ 2 seconds
- {LG} - laughter
- {NS} - random noise

.. _missing:

|
|
|

How to Add Missing Words
------------------------

You'll often run into words in your transcription that are not included in the dictionary; these may include place names, speech errors, novel words, etc. as decribed in :ref:`missing-alert`.

If you want to override the automatic phonemicization (often appropriate for words not following native Spanish orthography to phonemes), add each of the missing words to a txt file with their corresponding phones, as shown below:

.. include:: dict_ex.txt
	:literal:


The format of the dictionary is the word (in captials) following by the corresponding phones, each separated by a space. 

Phones correspond to ipa with the following exceptions:

- Palatal fricative: y
- Palatal affricatve: CH
- Palatal nasal: NY
- Alveolar tap: r
- Alveolar trill: R
- Approximants and stops are both lower-case: (b,d,g)


.. note:: Extra words in your custom dictionary won't affect alignment! I suggest keeping one dict.local and adding new words as you encounter them. 
