import eyed3

audiofile = eyed3.load('/home/chipdelmal/Documents/Github/pyDroid/out/08 Summer.mp3')
dir(audiofile.tag)
dir(audiofile.tag.popularities)
# audiofile.tag.save()
audiofile.tag.popularities.__class__
