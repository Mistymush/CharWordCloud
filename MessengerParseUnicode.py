#Script which parses a facebook data file after being copied into a .txt file.
#The script will count the frequency of each word in the data and save results to a file.
#Author: August Beers

#emojies of intrest = heart, smile, kiss, heart eyes, teeth smile


import string
import re
import codecs

TokFound = []
TokCount = []

with open("charTest.txt") as f:

    header_ignore_flip = False

    for line in f:
        no_new_line = line[:-1]

        #regex = re.compile('[%s]' % re.escape(string.punctuation))

        #punc_strip_line = regex.sub('', no_new_line)

        print(no_new_line)
        #print(punc_strip_line)

        #tokens = punc_strip_line.split(' ')

        """
        if(len(punc_strip_line) == 0):
            header_ignore_flip = True
        elif header_ignore_flip == True:
            header_ignore_flip = False
        else:
            for e in tokens:

                if e in TokFound:
                    i = TokFound.index(e)
                    TokCount[i] += 1
                else:
                    TokFound.append(e)
                    TokCount.append(1)


finalTokData = zip(TokFound,TokCount)
soretedFinalTokData = sorted(finalTokData, key = lambda x:x[1], reverse = True)
for e in list(soretedFinalTokData):
    print(e)
"""