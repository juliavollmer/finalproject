"""
Tests of different onset detection methods
Currently under development
Last updated: 9 December 2012
"""
import sys
sys.path.append('..')

from pymir import AudioFile
from pymir import Energy
from pymir import Onsets

import matplotlib.pyplot as plt

import numpy

filename = "../tempaudio/test.mp3"

print "Opening File: " + filename
audiofile = AudioFile.open(filename)

#plt.plot(audiofile)
#plt.show()

frames = audiofile.frames(2048, numpy.hamming)

print len(frames)
