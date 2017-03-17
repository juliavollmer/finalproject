### Ideas/plan about the music to image:
### length of music piece determines the size of the final image
### Tones (frequences) determines the colors: --> further research on color organs
### Rhythm and breaks determines the position and distance of objects inside (be it geometrical or not)
### If music piece changes drastically or not will determine how much order the image has
### If possible, chords will determine the shape of objects, minor will be more sharp, while major more round 'soft'
### Volume determines the size of the objects
### A random value will determine the object itself, and thus make the image different each time
### If time allows, lyrics extraction could lead to another factor: incorparting the lyrics into the image
### Other values extracted from the music could be used to alter and manipulate the before created image.


# length of music piece determines the size of the final image XXX
# Tones (frequencies) determines the colors: XXX --> changed to Chords
# Rhythm and breaks determines the position and distance of objects inside (be it
# geometrical or not)
# If possible, major/minor will determine the shape of objects, minor will be more
# sharp, while major more round/'soft'
# A random value will be incorporated to make a different image each time
import sys
sys.path.append('..')
import librosa
from pymir import AudioFile
from pymir import Energy
from pymir import Onsets
from pymir import *

from PIL import Image, ImageDraw
import numpy
from random import randint

def visioning(name, art):
    filename = "tempaudio/%s" % name
    # filename = "tempaudio/test-stereo.mp3"
    audiofile = AudioFile.open(filename)
    y, sr = librosa.load(filename)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    # print tempo
    # print beat_times
    numberbeat = len(beat_frames)

    frames = audiofile.frames(8820, numpy.hamming)

    size = len(frames)
    width = size / randint(2, 3)
    height = size - width
    # print height
    # print width


    visual = Image.new("RGB", (height, width), "black")
    draw = ImageDraw.Draw(visual)


    frameIndex = 0
    startIndex = 0
    # getting the chords and colors from the modified pitch module
    for frame in frames:
        spectrum = frame.spectrum()
        chroma = spectrum.chroma()
        chord, coloring, mode = Pitch.getChord(chroma)
        endIndex = startIndex + len(frame)
        startTime = startIndex / frame.sampleRate
        endTime = endIndex / frame.sampleRate
        # print startTime
        x = (int(startTime), randint(1, height))
        w = (randint(1, width), int(endTime))
        start = height / randint(1,2)
        end = width / randint(1,2)
        # print "%s | %s " % (chord, coloring)
        frameIndex = frameIndex + 1
        startIndex = startIndex + len(frame)

        if mode == 0: # chord is minor
            randomnumber = randint(0,3)
            if randomnumber==0:
                draw.pieslice((x, w), start, end, fill = coloring)
            elif randomnumber==1:
                draw.line((x, w), fill = coloring)
            elif randomnumber==2:
                draw.polygon((x, w), fill = coloring)
            else:
                draw.rectangle((x, w), fill = coloring)
        elif mode == 1:
            randomnumber = randint(0,3)
            if randomnumber==0:
                draw.arc((x, w), start, end, coloring)
            elif randomnumber==1:
                draw.chord((x, w), start, end, fill = coloring)
            elif randomnumber==2:
                draw.ellipse((x, w), fill = coloring)
            else:
                draw.point((x, w), fill = coloring)

    i= 0
    while i < numberbeat:
        if i+1 > numberbeat:
            break
        x = (beat_times[i], beat_times[i])
        w = ((randint(0,10)+beat_times[i]), (randint(0,10)++beat_times[i]))
        draw.point((x, w), fill = "white")
        i += 1
    # # x= (0, 0)
    # # y= (500, 400)
    # # start = 20
    # # end = 50
    # # draw.line((0, 0) + visual.size, fill=128)
    # # draw.line((0, visual.size[1], visual.size[0], 0), fill=128)
    # #
    # # draw.arc((x, y), start, end, coloring)
    # # draw.chord((x, y), start, end, fill = coloring)
    # # draw.ellipse((x, y), fill = coloring)
    # # draw.pieslice((x, y), start, end, fill = color)
    # # draw.line((x, y), fill = color)
    # # draw.point((x, y), fill = color)
    # # draw.polygon((x, y), fill = color)
    # # draw.rectangle((x, y), fill = color)
    path= "static/picture/%s.png" % art
    visual.save(path, "PNG")
