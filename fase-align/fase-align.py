#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re
import wave
import codecs
import subprocess
import argparse
import shutil
import audiolabel
import sox



def correction(x):
	"""	
	Correct the rounding error for the 11025hz sampling rate. 
	See Yuan and Liberman (2008) or P2FA.readme for details.
	"""
	x = float(x)
	x = x - (x % 10) # Round down to deal with strangeness
	x = x/10000000
	if x > 0:
		x = (x + 0.0125) * (11000.0/11025.0) # correction

	return x



def makeSections(f):
	 ''' This is a generator function. It will return successive sections
		 of f until EOF.

		 Sections are every line from a 'Name:' line to the first blank line.
		 Sections are returned as a list of lines with line endings stripped.

		 Original makeSections() function from Kent Johnson (https://mail.python.org/pipermail/tutor/2004-December/033767.html)
	 '''
	 currSection = []
	 for line in f:
		 line = line.strip()
		 if re.match('"(.*?)"', line) is not None:
			 # Start of a new section
			 if currSection:
				 yield currSection
				 currSection = []
			 currSection.append(line)
		 elif not line:
			 # Blank line ends a section
			 #if currSection:
			 if line == ".": 
				 yield currSection
				 currSection = []
		 else:
			 # Accumulate into a section
			 currSection.append(line)
	 # Yield the last section
	 if currSection:
		 yield currSection



def sectionizeMLF(mlf):

	currSection = []
	for line in mlf:
		line = line.strip().split()
		if len(line) == 5:
			if currSection:
				yield currSection
				currSection = []
			currSection.append(line)
		elif not line:
			if line == ".":
				yield currSection
				currSection = []
		else:
			currSection.append(line)
	if currSection:
		yield currSection



def prep_dir(tmppath,basename,dict_include):
 	

	if os.path.exists(tmppath):
		shutil.rmtree(tmppath)	
	os.mkdir(tmppath)
	os.mkdir(tmppath+'/chunks/')
	#subprocess.Popen(['chmod','a+w',tmppath + 'chunks/'], stdout=subprocess.PIPE)

	if dict_include == True:

		# Check to see if any illegal characters are in dictionary
		unwanted = ['\?', '¿', '¡', '!', '%','\"', '/', '#', '&', '\(', '\)', '\'', '\+', '@','\^', ',', '\-', '\.', '\\\\', ':', ';', '_', 'á', 'í', 'ú', 'é', 'ó']
		matches = []

		with codecs.open(args.missing, 'r', 'utf-8') as custom_dict:
			lines = custom_dict.readlines()
			for line in lines:
				for character in unwanted:
					if re.search(character,line.encode('utf-8')) is not None:
						matches.append(character)
				
			if len(matches) > 0:
				matches = list(set(matches))
				print("ERROR! Illegal characters in custom dictionary. Please remove them and resubmit. : ")
				for char in matches:
					print('"' + char + '", ')
				sys.exit()

		os.system('cat ' + repos + 'dict_sort ' + args.missing + ' | sort | uniq > ' + tmppath + 'new_dict.txt')
		#subprocess.Popen(['cat',repos+"dict_sort",tmppath + basename + '.missing', '|', 'sort', '|', 'uniq', '>', tmppath + 'new_dict.txt'], stdout=subprocess.PIPE)	
		dict_path = tmppath + 'new_dict.txt'	
	else:
		dict_path = repos + "dict_sort"

	return dict_path



def process_wav(audio,tmppath,basename,channel_type):

	wav_file = wave.open(audio, 'r')
	sr = wav_file.getframerate()
	wav_file.close()

	if sr < 11025:
		print("WARNING - Sampling rate is lower than necessary 11025hz. Alignment will suffer!")
		#sys.exit()

	elif sr == 11025:
		pass
	
	else: # sr > 11025
		subprocess.check_call(['mv',audio,tmppath+basename+ "_original.wav"])
		subprocess.check_call(['sox',tmppath+basename+ "_original.wav",'-r','11025', audio])

	if channel_type == "stereo":
		subprocess.check_call(['sox',audio,tmppath+basename+"_c1.wav",'remix','1'])
		subprocess.check_call(['sox',audio,tmppath+basename+"_c2.wav",'remix','2'])



def clean_words_str(content):

	l = []
	unwanted = ['\*','?', '¿', '¡', '!', '%','\"', '/', '#', '&', '(', ')', '\'', '+', '@','^', ',', '-', '.', '\\', ':', ';', '_', '\n', '\t']
	rx = '[' + re.escape(''.join(unwanted)) + ']'
	unwanted_ext = [u'\u2026',u'\u2010',u'\u2011',u'\u2012',u'\u2013',u'\u2014',u'\u2015',u'\u2018',u'\u2019',u'\u201C',u'\u201D'] 
	
	# Process string type content from textgrids
	new_content = re.sub(rx, ' ', content)

	# Remove other unwanted characters. For some reason this doesn't work if you copy and paste the character into 'unwanted' above, likely an encoding thing.
	#new_line = new_line.replace(u'\u2026', ' ')
	#new_line = new_line.replace(u'\u201C', ' ')
	for char in unwanted_ext:
		new_content = new_content.replace(char, ' ')

	# Add padding around tabs
	new_content = re.sub('\{', ' {', new_content)
	new_content = re.sub('\}', '} ', new_content)

	# Clear out multiple spaces
	new_content = re.sub('  ', ' ', new_content)
	new_content = re.sub('  ', ' ', new_content)
	new_content = re.sub('  ', ' ', new_content)

	for word in new_content.split():
		l.append(word.upper())

	return l



def clean_words_list(l,content):
	unwanted = ['\*','?', '¿', '¡', '!', '%','\"', '/', '#', '&', '(', ')', '\'', '+', '@','^', ',', '-', '.', '\\', ':', ';', '_', '\n', '\t']
	rx = '[' + re.escape(''.join(unwanted)) + ']'

	for line in content:
		new_line = re.sub(rx, ' ', line)
		# Remove other unwanted characters. For some reason this doesn't work if you copy and paste the character into 'unwanted' above, likely an encoding thing.
		unwanted_ext = [u'\u2026',u'\u2010',u'\u2011',u'\u2012',u'\u2013',u'\u2014',u'\u2015',u'\u2018',u'\u2019',u'\u201C',u'\u201D']
		for char in unwanted_ext:
			new_line = new_line.replace(char, ' ')

		content_split = new_line.split()

		for elem in content_split:
			l.append(elem.upper().strip())

	return l



def identify_speakers(l):

	speaker_list = []
	speaker_words = {}
	speaker_indices = {}

	first_speaker = ""
	index_edit = 0

	for index,line in enumerate(l):
		speaker_match = re.search('\{[SI][0-9]*?\}',line)

		# Populate speaker list
		if speaker_match != None:
			speaker = line[speaker_match.start()+1:speaker_match.end()-1]
			
			# If a speaker hasn't yet been assigned, assign one and record which speaker was first
			try:
				current_speaker
			except NameError:
				current_speaker = speaker
				first_speaker = speaker
		
			# Note speaker changes
			if current_speaker != speaker:
				current_speaker = speaker
		
			# Add speakers to list of speakers
			speaker_list.append(current_speaker)
		
			# Ensure that the speaker labels aren't appended
			continue 

		# Populate speaker keys
		if current_speaker not in speaker_words.keys():
			speaker_words[current_speaker] = []
		
		# Add line to speaker dictionary
		speaker_words[current_speaker].append(line)
		
		# Construct dictionary which links word indices to speakers
		speaker_indices[index_edit] = current_speaker
		index_edit += 1

	# Clean up output	
	speaker_list = sorted(set(speaker_list))
	if len(speaker_list) > 0:

		pass
	else:
		print("Warning: No speaker labels found. If you have more than one speaker, make sure your speaker labels are in the correct format.")
		print("Processing all text as single speaker.")

	return speaker_list,speaker_indices,speaker_words,first_speaker



def make_mlf_from_txt(audio,words,mfc,wav_mfc,actual_transcript,dict_sort,tmppath,basename):
	
	
	content = actual_transcript.readlines()
	actual = []
	actual = clean_words_list(actual,content)
	dict_all = dict_sort.readlines()
	dict_split = []
	all_words = []
	missing = []
	i = 0

	speaker_list, speaker_indices, speaker_words, first_speaker = identify_speakers(actual)

	all_words.append('#!MLF!#\n"*/' + basename +'.lab"\nSIL\n')

	for elem in dict_all:
		if len(elem.split()) > 0:
			dict_split.append(elem.split()[0])

	for iter, value in enumerate(actual):
		if re.search('\{[SI][0-9]*?\}',value) is None:
			if i == 0:
				all_words.append(value+"\n")
			else:
				all_words.append("sp\n" + value +"\n")

			if value not in dict_split:
				missing.append(value)
			i += 1

	all_words.append('SIL\n.')
						

	for iter2 in all_words:
		words.write(iter2)

	words.write('\n')
	mfc.write(tmppath + basename + '.mfc')	
	wav_mfc.write(audio + ' ' + tmppath + basename + '.mfc' )	

	if len(missing) > 0:
		with codecs.open(tmppath + 'missing_words', 'w', 'utf-8') as words_to_add:
			for word in sorted(set(missing)):
				words_to_add.write(word + '\n')
		
		sys.exit('There were missing words in your transcript! Saved to- ' + tmppath + 'missing_words')


	return speaker_words, speaker_indices, speaker_list, first_speaker



def make_mlf_from_tg(dict_sort,audio,tmppath,basename,textgrid,channel_type,chan_1,chan_2):

	# Prep files to filter missing items
	missing = []
	dict_split = []
	dict_all = dict_sort.readlines()
	all_words = {}
	chunk_index = {}

	for elem in dict_all:
		if len(elem.split()) > 0:
			dict_split.append(elem.split()[0])
	total_chunks = 0


	# Read in TextGrid
	lm = audiolabel.LabelManager(from_file = textgrid, from_type = 'praat', codec ='utf-8')


	for speaker in lm.names:
		chunk_index[speaker] = {}
		all_words[speaker] = []
		all_words[speaker].append('#!MLF!#\n')

		# Determine proper speakers and channels
		if channel_type == "mono":
			current_wav = audio
		else:
			if speaker == chan_1:
				current_wav = tmppath+basename+'_c1.wav'
			elif speaker == chan_2:
				current_wav = tmppath+basename+'_c2.wav'
			else:
				print("Couldn't find a matching speaker for " + speaker + ". Reverting to mono.")
				current_wav = audio


		for interval in lm.tier(speaker):

			# Counter for start of list
			i = 0

			# Process chunk text
			chunk_name = 'chunk_' + str(total_chunks)
			chunk_start = interval.t1
			chunk_end = interval.t2
			chunk_txt = clean_words_str(interval.text)

			# Exclude turns including {CS},{OP},XXX,HHH,and hhh
			if re.search('\{CS\}', ' '.join(chunk_txt)) is None and re.search('\{OP\}', ' '.join(chunk_txt)) is None and re.search('XXX', ' '.join(chunk_txt)) is None and re.search('HHH', ' '.join(chunk_txt)) is None and re.search(' hhh', ' '.join(chunk_txt)) is None:

				# Recover chunk start and end time for after aligning
				chunk_index[speaker][chunk_name] = (chunk_start,chunk_end)


				all_words[speaker].append('"*/' + chunk_name + '.lab"\nSIL\n')

				for iter, value in enumerate(chunk_txt):
					if i == 0:
						all_words[speaker].append(value + "\n")
					else:
						all_words[speaker].append("sp\n" + value + "\n")
					
					if value not in dict_split:
						missing.append(value)

					i += 1

				all_words[speaker].append('.\n')

				# Extract Chunk Audio
				tfm = sox.Transformer()
				tfm.trim(chunk_start,chunk_end)
				tfm.build(current_wav,tmppath+'chunks/'+chunk_name+'.wav')
				
				# Write files
				with open(tmppath + 'speaker_'+speaker+'_mfc.scp', 'a') as mfc:
					with open(tmppath + 'speaker_'+speaker+'_wav_mfc.scp', 'a') as wav_mfc:
						mfc.write(tmppath+'chunks/'+chunk_name+'.mfc\n')
						wav_mfc.write(tmppath+'chunks/'+chunk_name+'.wav ' + tmppath+'chunks/'+chunk_name+'.mfc\n')

				total_chunks += 1

		# Append a speaker's turns
		with open(tmppath + 'speaker_'+speaker+'_words.mlf', 'a') as words:
			for iter2 in all_words[speaker]:
				words.write(iter2)



	return missing, chunk_index , total_chunks
	


def call_htk(tmppath,name,dict_path):


	subprocess.Popen(['chmod','a+w',tmppath + name + 'mfc.scp'], stdout=subprocess.PIPE)
	subprocess.Popen(['chmod','a+w',tmppath + name + 'wav_mfc.scp'], stdout=subprocess.PIPE)
	subprocess.Popen(['chmod','a+w',tmppath + name + 'words.mlf'], stdout=subprocess.PIPE)

	HCopy_call = ["/usr/local/bin/HCopy", "-T", "1", "-C", repos+"/config_HCopy", "-S", tmppath + name + "wav_mfc.scp"]
	#subprocess.call(HCopy_call,stdin=DEVNULL,stdout=DEVNULL,stderr=DEVNULL)#.wait()
	#print(' '.join(HCopy_call)+'\n')
	subprocess.check_call(HCopy_call, stdout=subprocess.PIPE)
	#subprocess.check_call(HCopy_call,stdin=PIPE,stdout=DEVNULL,stderr=STDOUT)

	subprocess.Popen(["chmod","a+w",tmppath+name+".mfc"], stdout=subprocess.PIPE)

	HVite_call = ["/usr/local/bin/HVite", "-A", "-D", "-T", "1", "-l", "'*'", "-a", "-m", "-C", repos+"/config", "-H", repos+"/globals", "-H", repos+"/hmmdefs", "-m", "-t", "250.0", "150.0", "1000.0", "-I", tmppath + name + "words.mlf", "-i", tmppath + name + "aligned.mlf", "-S", tmppath + name + "mfc.scp", dict_path, repos+"/monophones1"]
	#HVite_call = ["/usr/local/bin/HVite", "-A", "-D", "-T", "1", "-l", "'*'", "-a", "-m", "-C", repos+"/config", "-H", repos+"/globals", "-H", repos+"/hmmdefs", "-m", "-t", "250.0", "150.0", "1000.0", "-I", tmppath + name + "words.mlf", "-i", tmppath + name + "aligned.mlf", "-S", tmppath + name + "mfc.scp", repos+"dict_tri", repos+"/tiedlist"]

	#print(' '.join(HVite_call)+'\n')
	#subprocess.check_call(HVite_call, stdout=subprocess.PIPE)
	subprocess.call(HVite_call)



def process_mlf_output(section,speak):

	for sec in sectionizeMLF(section):
		for phone_block in sec:
			current = phone_block

			if len(current) > 3:
				# Test for no-duration sp
				intset = current[0:2]
				integers = list(map(int, intset))
				test_begin = float(integers[0])/10000000
				test_end = float(integers[1])/10000000

				if test_begin != test_end:

					# Correct 11025 rounding error
					begin = correction(integers[0])
					end = correction(integers[1])

					# Get current phone
					phone = current[2]
					# Extract true phone from context triphones
					#if re.match('(.+)\-(.+)\+', phone) is not None:
					#	true_phone = re.findall('\-(.+?)\+', phone, re.DOTALL)[0]
					#elif re.match('(.+)\-(.+)', phone) is not None:
					#	true_phone = re.findall('\-(.+)', phone, re.DOTALL)[0]
					#elif re.match('(.+)\+(.+)', phone) is not None:
					#	true_phone = re.findall('(.+)\+', phone, re.DOTALL)[0]
					#else:
					#	true_phone = phone					

					output_intervals[speak]["phones"].append(tuple([begin+offset,end+offset,phone]))


		# Get word information
		word_begin = correction(sec[0][0])
		
		# Ignore erroneous '.'
		if len(sec[-1]) > 3:
			word_end = correction(sec[-1][1])
		else:
			word_end = correction(sec[-2][1])

		if word_begin != word_end:
			word = bytes(sec[0][4],encoding='latin-1').decode('unicode-escape') # Escape and convert hex decimals output from HVite
			word = word.encode('latin-1').decode('utf-8') # Convert these strings back to correct utf-8
			if word != "sp" and word != "SIL":
				# If we're processing a txt file input and using speaker_indices
				try:
					speak = speaker_indices[word_index] # Compare to word indices mapped to speakers. 
					word_index += 1
				except NameError:
					pass
			output_intervals[speak]["words"].append((word_begin+offset,word_end+offset,word))



def align_from_tg(chunk_index, total_chunks, tmppath, dict_path, basename):

	output_intervals = {}

	for speaker in chunk_index:

		output_intervals[speaker] = {}
		output_intervals[speaker]["phones"] = []
		output_intervals[speaker]["words"] = []
	
		curr = "speaker_" + speaker + "_"

		call_htk(tmppath,curr,dict_path)

		with codecs.open(tmppath + curr + 'aligned.mlf', 'r', 'utf-8') as input:
			f = input.readlines()[1:]
			for section in makeSections(f):
				# Get chunk name from .rec header
				result = re.search('chunk_(.*)\.rec\"',section[0])
				chunk_name = 'chunk_' + str(result.group(1))

				# Calculate each chunk's offset from original time
				offset = chunk_index[speaker][chunk_name][0]

				# Ignore chunk headers
				section = [x for x in section if "rec" not in x]

				# Process aligned mlf and add intervals to output_intervals dictionary
				process_mlf_output(section,speaker)

	return output_intervals



def align_from_txt(speaker_indices,speaker_list,first_speaker,tmppath,basename,dict_path):
	
	call_htk(tmppath,basename+"_",dict_path)
	word_index = 0
	current_speaker = first_speaker

	all_lines = []

	with codecs.open(tmppath + basename + '_aligned.mlf', 'r','utf-8') as input: 
		f = input.readlines()[2:]

		for section in makeSections(f):
					
			output_intervals = {}

			# Populate dictionaries with speaker keys
			for speaker in speaker_list:
				output_intervals[speaker] = {}
				output_intervals[speaker]["phones"] = []
				output_intervals[speaker]["words"] = []
			
			process_mlf_output(section,first_speaker)



def process_tg_intervals(tmppath,basename,output_intervals):

	out_tg = audiolabel.LabelManager(codec='utf-8')

	for speaker in output_intervals:
		for tier_type in output_intervals[speaker]:
			tier_name = speaker + ' : ' + tier_type
			t = audiolabel.IntervalTier(name=tier_name)
			for i in output_intervals[speaker][tier_type]:
				t.add(audiolabel.Label(text=i[2],t1=i[0],t2=i[1]))
			out_tg.add(t)


	return out_tg



def main(audio, transcript, tmppath, basename, transcript_type, channel_type, chan_1, chan_2, dict_include):

	dict_path = prep_dir(tmppath,basename,dict_include)
	process_wav(audio,tmppath,basename,channel_type)

	###########################
	if transcript_type == "txt":

		with codecs.open(tmppath + basename + '_words.mlf', 'a', 'utf-8') as words:
			with codecs.open(dict_path, 'r', 'utf-8') as dict_sort:
				with open(tmppath + basename + '_mfc.scp', 'a') as mfc:
					with open(tmppath + basename + '_wav_mfc.scp', 'a') as wav_mfc:
						try:
							with codecs.open(transcript, 'r', 'utf-8') as actual_transcript:
								speaker_words,speaker_indices,speaker_list,first_speaker = make_mlf_from_txt(audio,words,mfc,wav_mfc,actual_transcript,dict_sort,tmppath,basename)

						except UnicodeError:
							try:
								with codecs.open(transcript, 'r', 'utf-16') as actual_transcript:
									speaker_words,speaker_indices,speaker_list,first_speaker = make_mlf_from_txt(audio,words,mfc,wav_mfc,actual_transcript,dict_sort,tmppath,basename)

							except UnicodeError:
								with codecs.open(transcript, 'r', 'iso-8859-1') as actual_transcript:
									speaker_words,speaker_indices,speaker_list,first_speaker = make_mlf_from_txt(audio,words,mfc,wav_mfc,actual_transcript,dict_sort,tmppath,basename)
			
	###########################
			
	else:
		with codecs.open(dict_path, 'r', 'utf-8') as dict_sort:
			missing, chunk_index, total_chunks= make_mlf_from_tg(dict_sort,audio,tmppath,basename,transcript,channel_type,chan_1,chan_2)
			# Exit if missing words!
			if len(missing) > 0:
				with codecs.open(tmppath + 'missing_words', 'w', 'utf-8') as words_to_add:
					for word in sorted(set(missing)):
						words_to_add.write(word+'\n')
				sys.exit('There were missing words in your transcript! Saved to- ' + tmppath + 'missing_words')
				
	###########################

	if transcript_type == "txt":
		align_from_txt(speaker_indices,speaker_list,first_speaker,tmppath,basename,dict_path)
	else:
		output_intervals = align_from_tg(chunk_index, total_chunks,tmppath,dict_path,basename)
	out_tg = process_tg_intervals(tmppath,basename,output_intervals)
	with codecs.open(outpath+basename+'_aligned.TextGrid','w','utf-8') as o:
		o.write(out_tg.as_string('praat_short'))

	shutil.rmtree(tmppath)



############################################
############################################
# Parse Arguments

parser = argparse.ArgumentParser(description='test description')
parser.add_argument('-w', '--wav', required = True, help = 'path to wav file')
parser.add_argument('-s', '--stereo', action='store_true', help = 'stereo input, mono is default')
parser.add_argument('-l', '--left', help = 'left channel speaker')
parser.add_argument('-r', '--right', help = 'right channel speaker')
parser.add_argument('-t', '--transcript', required = True, help = 'path to transcript')
parser.add_argument('-o', '--outpath', help = 'directory to store output textgrid(s), default is current directory')
parser.add_argument('-m', '--missing', help = 'custom dictionary containing missing words')
args = parser.parse_args()

repos = "/home/ubuntu/Desktop/Shared/sf_fase_dev/testing/m5_monomix/" # TO-DO: map this correctly from setup.py

# Check stereo options
if ((args.stereo is True and args.left is None) or (args.stereo is True and args.right is None)):
	parser.error('Stereo option requires --left and --right speaker arguments.')

# Check transcript type
file_ext = os.path.splitext(args.transcript)[1]

if file_ext == '.txt':
	transcript_type = 'txt'
elif file_ext in ['.TextGrid','.Textgrid','.textgrid','.textGrid']:
	transcript_type = 'tg'
else:
	parser.error('Transcript file must be .txt or .TextGrid.')

# Check missing
if args.missing is not None:
	dict_include = True
else:
	dict_include = False

# Establish basename and directories
basename = '/' + os.path.basename(args.wav).replace('.wav','')
if args.outpath is not None:
	outpath = args.outpath + '/'
else:
	outpath = os.getcwd()

tmppath = outpath + '/tmp/'


# Channel options
if args.stereo is True:
	channel_type = 'stereo'
	if ((args.left is not None) and (args.right is not None)):
		chan_1 = '{' + args.left + '}' # TO-DO: improve flexibility and parsing of possible inputs (in addition to custom speaker tags)
		chan_2 = '{' + args.right + '}'
	else:
		chan_1 = None
		chan_2 = None
else:
	channel_type = 'mono'
	chan_1 = None
	chan_2 = None

main(args.wav, args.transcript, tmppath, basename, transcript_type, channel_type, chan_1, chan_2, dict_include)
