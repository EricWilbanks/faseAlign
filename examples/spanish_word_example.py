#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from spanish_word_class import spanish_word

# create an instantiation of the spanish_word class
my_word = spanish_word('Arroyo')

# See all properties of the word
print(my_word)

# Find specifications of these attributes
print(vars(my_word))

# Access an individual attribute

stressed_syll = my_word.stressed
n_syl = my_word.num_syllables

print(n_syl,'syllables; stressed syllable:', stressed_syll)