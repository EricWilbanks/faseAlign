#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Unix allows for execution of files without .py, but Windows does not. 
# This workaround allows faseAlign to be called (without extension) from the command line in an OS-independent fashion 
import faseAlign

if __name__ == '__main__':

	# Parse arguments
	parser = argparse.ArgumentParser(description='test description')
	parser.add_argument('-w', '--wav', required = True, help = 'path to wav file')
	parser.add_argument('-s', '--stereo', action='store_true', help = 'stereo input, mono is default')
	parser.add_argument('-l', '--left', help = 'left channel speaker')
	parser.add_argument('-r', '--right', help = 'right channel speaker')
	parser.add_argument('-t', '--transcript', required = True, help = 'path to transcript')
	parser.add_argument('-o', '--outpath', help = 'directory to store output textgrid(s), default is current directory')
	parser.add_argument('-m', '--missing', help = 'custom dictionary containing missing words')
	args = parser.parse_args()

	faseAlign.main(args.wav, args.stereo, args.left, args.right, args.transcript, args.outpath, args.missing)