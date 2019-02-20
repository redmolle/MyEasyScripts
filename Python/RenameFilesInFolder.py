import os
from os import listdir
from os.path import isfile, join

mypath = 'W:\\Anime\\Bleach\\Bleach_e001_-_eXXX_+_Bonus_+_Manga_2004_-_2012_rus_x264_DVDRip_TVRip_HDTVRip\Bleach_e001_-_eXXX_+_Bonus_+_Manga_2004_-_2012_rus_x264_DVDRip_TVRip_HDTVRip\\BLEACH.001_062.DVDRip.x264.RUS.2X2.mp4'
pat = '.2004.x264.Nikolai.Baranov.DVDRip.AVC'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for i in range(1,len(onlyfiles)):
    s = join(mypath,onlyfiles[i])
    os.rename(s, s.replace(pat, ''))
