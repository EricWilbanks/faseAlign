.. _changelog:


Changelog
=========
#. **Version 1.1.14**: October 13, 2022

		#. Fixed issue where words in `dict_sort` whose pronunciations differ from the automatic phonemicizations would cause syllabification to fail with an IndexError.
		#. Fixed issue where syllabification could fail when custom dictionaries weren't also enabled.
		#. Fixed issue where digraphs (NY and CH) were not correctly treated when syllabifying words from custom dictionaries.

#. **Version 1.1.13**: June 12, 2021

		#. Fixed bug where custom dictionary entries (-m) did not correctly interact with automatic syllabification (-y)

#. **Version 1.1.12**: April 25, 2021

		#. New installation instructions for conda environment method

#. **Version 1.1.11**: March 30, 2021

		#. Fixed bug where -n flag was removing characters from beginning and end of argument
		#. Fixed bug where output TextGrids tiers may have been added in a random order; intended behavior is words and then phones.
		#. Fixed bug where rounding errors in HTK output could cause output textgrids to have tiny empty intervals

#. **Version 1.1.10**: October 20, 2020

		#. Changes to directory structure for more consistent distribution
		#. Bug-fixes with dictionary access and phonemicization flag
		#. Change to https git protocol (over git+git) for installation

#. **Version 1.1.9** : October 10, 2018

		#. Updates to package directory structure and creation of utils.py. 
		#. Import custom classes and functions in a Python interpreter by importing from faseAlign.utils as in the following example: `from faseAlign.utils import spanish_word`

#. **Version 1.1.8** : September 26, 2018

		#. Added -i/--tier tag to allow for aligning of individual tiers of .TextGrid transcripts

#. **Version 1.1.7** : August 20, 2018

		#. Bug fixes to .txt input transcripts and processing of speaker labels

#. **Version 1.1.6** : August 19, 2018

		#. Addition of version printout (-v flag)
		#. Change of version numbering scheme to be consistent with semantic versioning (note the jump from 0.1.5 to 1.1.6)

#. **Version 0.1.5** : March 28, 2018

		#. Sampling rate bug fixes
		#. Change in default behavior: phonemicization is no longer carried out by default, but must be chosen using the `p` flag

#. **Version 0.1.4** : October 18, 2017

		#. Dictionary encoding bug fixes

#. **Version 0.1.3** : August 22, 2017

		#. Addition of custom output name functionality (-n flag)

#. **Version 0.1.2** : July 24, 2017

		#. Addition of custom speaker tag functionality (-g flag)

#. **Version 0.1.1** : July 19, 2017

		#. Addition of syllabification functionality (-y flag)
		#. Addition of automatic phonemicization of unknown words (and prevention with -p flag)

#. **Version 0.1.0** : July 10, 2017

		#. Initial release
