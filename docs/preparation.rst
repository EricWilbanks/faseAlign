.. _preparation:

Preparing your Data
===================

Transcription Files
-------------------

The input to the force aligner is a wav file and the orthographic transcription associated with it. Transcriptions can be in either .TextGrid or .txt formats.

.TextGrid transcription
++++++++++++++++++++++

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

Speakers are still separated into their separate tiers following alignment, through the use of speakers labels (e.g., {S1} and {S2}) which mark utterances belonging to that speaker. 

.. note:: Currently only speaker labels {S1}-{S99} are available for .txt transcriptions

Transcription Best Practices
----------------------------

Regardless of transcription method chosen, the process of transcribing is nearly identical.

- types of inputs allowed
- examples
- special symbols
- transcription best practices
- dictionary entries

.. _missing:

How to Add Missing Words
------------------------

How to add missing words