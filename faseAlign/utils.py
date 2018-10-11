#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

class spanish_word(object):

	# class level attributes
	phones = ['a', 'e', 'i', 'o', 'u', 'p', 't', 'k', 'f', 's', 'x', '2', 'CH', 'l', 'b', 'd', 'g', 'm', 'n', '1', 'NY', 'y', 'R', 'r']
	unstressed_high_vowels = ['i','u']
	vowels = ['a','e','i','o','u','á','é','í','ó','ú']
	consonants = ['p', 't', 'k', 'f', 's', 'x', '2', 'CH', 'l', 'b', 'd', 'g', 'm', 'n', '1', 'NY', 'y', 'R', 'r']
	legal_clusters = ['pr','br','tr','dr','kr','gr','fr','pl','bl','kl','gl','fl'] # note: not including 'tl'
	x_exception = ['mexicano', 'méxico', 'mexico', 'mexicanos', 'mexicana', 'mexicanas'] # note: lots of other place/proper names could be included here
	y_exception = ['ay' , 'buey' , 'caray' , 'disney' , 'doy' , 'eloy' , 'estoy' , 'ey' , 'guay' , 'güey' , 'hay' , 'hoy' , 'ley' , 'muy' , 'paraguay' , 'rey' , 'soy' , 'uruguay' , 'uy' , 'virrey' , 'voy', 'y']
	corr_tups = [('ll','y'), ('qu','k'), ('ce','se'), ('cé','sé'), ('ci','si'), ('cí','sí'), ('ge','xe'), ('gé','xé'), ('gi','xi'), ('gí','xí'), ('j','x'), ('v','b'), ('z','s'), ('w','u'), ('rr','R'), ('\\br','R'), ('ñ','1'), ('ch','2'), ('c','k'), ('h',''), ('ü','u'), ('gui','gi'), ('gue','ge'), ('guí','gí'), ('gué','gé')]
	corr_tups2 = [('ú','u'), ('ó','o'), ('í','i'), ('é','e'), ('á','a')]

	def __init__(self, word):
		self.orth = word.lower()
		self.phones = self.to_phones()
		self.syllables = self.process_syllables()
		# Transform numbers back to digraphs
		self.phones[:] = [re.sub('1','NY',p) for p in self.phones] 
		self.phones[:] = [re.sub('2','CH',p) for p in self.phones]
		for key in self.syllables:
			self.syllables[key][:] = [re.sub('1','NY',entry) for entry in self.syllables[key]]
			self.syllables[key][:] = [re.sub('2','CH',entry) for entry in self.syllables[key]]

	def __str__(self):
		return '\nWord: ' + self.orth + '\nPhones: ' + str(self.phones) + '\nSyllables: ' + str(self.syllables) + '\nStressed Syllable: ' + str(self.stressed) + '\nNumber of Syllables: ' + str(self.num_syllables)

	def to_phones(self):

		current = self.orth

		if current not in spanish_word.x_exception:
			current = re.sub('x','ks',current)

		if current in spanish_word.y_exception:
			current = re.sub('y','i',current)

		for pair in spanish_word.corr_tups:
			match, repl = pair
			current = re.sub(match,repl,current)

		return list(current)

	def syllabify(self):

		# convert to cv skeleton
		cv = ''.join(['c' if p in spanish_word.consonants else 'v' for p in self.phones])

		# first parse of groups with maximal onsets
		l = re.findall('(?:c*v+c+$)|(?:c*v+)|(?:v+c+)|(?:^c+$)', cv)
		
		syllables_c = {}
		syll_n = 0
		phones = self.phones
		
		if len(phones) != len(''.join(l)):
			print('Error! Investigate! - ' + str(self.orth) + ' - ' + str(self.phones) + ' - ' + str(cv))

		###################
		# assign consonants
		for group in l:
			syll_n += 1
			syllables_c[syll_n] = []

			if group[0] == 'v':
				# add entire group to syllable
				syllables_c[syll_n].extend(phones[:len(group)])
				phones = phones[len(group):] # after adding group to main dict, remove it

			elif group[0] == 'c':
				c_len = len(re.match('c+(?!=v+c*)',group).group(0))
				cluster = ''.join(phones[:c_len])

				# key of previous syllable
				if syll_n > 1:
					prev_syll = syll_n - 1
				else:
					prev_syll = syll_n

				# split up clusters as needed
				if c_len == 4:
					syllables_c[prev_syll].extend(phones[:2]) # first two consonants to previous syllable
					syllables_c[syll_n].extend(phones[2:len(group)]) # remaining phones in group to current syllable
				elif c_len == 3:
					if cluster[1:c_len] not in spanish_word.legal_clusters: # x-sibilant-x
						syllables_c[prev_syll].extend(phones[:2]) # first two consonants to previous syllable
						syllables_c[syll_n].extend(phones[2:len(group)]) # remaining phones in group to current syllable
					else:
						syllables_c[prev_syll].extend(phones[:1]) # first consonant to previous syllable
						syllables_c[syll_n].extend(phones[1:len(group)]) # remaining phones in group to current syllable
				elif c_len == 2:
					if cluster not in spanish_word.legal_clusters:
						syllables_c[prev_syll].extend(phones[:1]) # first consonant to previous syllable
						syllables_c[syll_n].extend(phones[1:len(group)]) # remaining phones in group to current syllable
					else:
						syllables_c[syll_n].extend(phones[:len(group)]) # all phones to current syllable
				elif c_len == 1:
					syllables_c[syll_n].extend(phones[:len(group)]) # all phones to current syllable
				else:
					print("Incorrect specification of cluster: " + str(cluster) + ' - ' + str(self.orth))
				
				#remove phones from this group 
				phones = phones[len(group):]

		###############################
		# correctly assign vowel hiatus
		syllables = {}

		syll_n = 0
		for syll in syllables_c.keys():
			syll_n += 1
			syllables[syll_n] = []

			phones = ''.join(syllables_c[syll])
			cv = ''.join(['c' if p in spanish_word.consonants else 'v' for p in syllables_c[syll]]) #cv framework
			v_match = re.search('vv+',cv) # find adjacent vowels

			if v_match is not None:
				syllables[syll_n].extend(phones[:v_match.start()]) # append any onset consonants to syllable
				cluster = phones[v_match.start():v_match.end()] # extract vowel cluster
				while len(cluster) > 1:
					block = cluster[:2] # only consider two vowels at a time
					if ((block[0] not in spanish_word.unstressed_high_vowels) and (block[1] not in spanish_word.unstressed_high_vowels)) or ((block[0] == block [1]) and (block[0] in spanish_word.unstressed_high_vowels)): # adjacent (non-high or stressed high) or (identical high) = hiatus
						syllables[syll_n].extend(block[0]) # add first vowel to current syllable
						syll_n += 1 # create new syllable for hiatus
						syllables[syll_n] = []
						cluster = cluster[1:]
					else: 
						syllables[syll_n].extend(block[0]) # add first vowel and try again
						cluster = cluster[1:]
				syllables[syll_n].extend(cluster) # catch any trailing singletons
				syllables[syll_n].extend(phones[v_match.end():]) # catch any coda consonants
			else: 
				syllables[syll_n].extend(phones) # no vowel cluster so append entire syllable
		
		# NOTE: not currently dealing with lexically exceptional hiatus class words such as du.eto (cf. duelo)

		# add attribute containing number of syllables
		self.num_syllables = syll_n

		return syllables



	def process_syllables(self):

		syllables = self.syllabify()

		stressed = 0
		# determine stressed syllable
		for syll in syllables.keys():
			stress_match = re.search('(á|é|í|ó|ú)',''.join(syllables[syll]))
			if stress_match is not None:
				stressed = int(syll)

		if self.num_syllables == 1:
			stressed = 1

		if stressed == 0: # normal rules, no orthographic accent
			if self.orth[-1] in spanish_word.vowels + ['n','s']:
				stressed = self.num_syllables - 1 # penultimate stress since no orthographic accent
			else: 
				stressed = self.num_syllables # final stress since no orthographic accent 

		# remove accent marks
		for syll in syllables.keys(): 
			for pair in spanish_word.corr_tups2:
				match, repl = pair
				syllables[syll][:] = [re.sub(match,repl,x) for x in syllables[syll]] # whole list slice
		for pair in spanish_word.corr_tups2:
			match, repl = pair
			self.phones[:] = [re.sub(match,repl,x) for x in self.phones]

		self.stressed = stressed

		return syllables

