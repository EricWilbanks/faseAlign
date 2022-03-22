.. _development:
.. _dev_slides: https://ericwilbanks.github.io/files/wilbanks_nwav_2015.pdf
.. _michnowicz: https://chass.ncsu.edu/people/jcmichno/
.. _ronquest: https://chass.ncsu.edu/people/reronque/

Model Development
=================

Monophones
----------

.. figure:: monophones.png
	:alt: Table of monophone symbols
	:figclass: align-center

	*Monophone symbols*

For the most part, phones correspond to their IPA symbols. Exceptions are noted in the table with symbols in parentheses. This phonemic inventory corresponds to many varieties of Latin American Spanish, but notably does not include theta. Additionally, palatal laterals are not included. 

Notes on Development
--------------------

The acoustic models used in this tool are triphone-HMMs trained using the HTK on data from 20 spontaneous interviews from the Corpus del Español de Raleigh-Durham (CERD) created and maintained by Drs. :_michnowicz:`Jim Michnowicz` and :ronquest:`Rebecca Ronquest`. A detailed description of the development of this tool can be found in the slides from our :_dev_slides:`2015 NWAV presentation`.
