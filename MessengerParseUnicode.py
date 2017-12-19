#Script which parses a facebook data file after being copied into a .txt file.
#The script will count the frequency of each word in the data and save results to a file.
#Author: August Beers

#emojies of intrest = heart, smile, kiss, heart eyes, teeth smile

import string
import re

TokFound = []
TokCount = []

with open("CharUnicodeData.txt", encoding='utf-8') as f:

    #allways ignore first line
    msg_label_ignore_flip = True

    for line in f:
        no_new_line = line[:-1]

        #regex to match punctuation for removal
        regex = re.compile('[%s]' % re.escape(string.punctuation))
        smileRegex = re.compile(re.escape(':)'))
        heartRegex = re.compile(re.escape('<3'))

        no_new_line = smileRegex.sub('666', no_new_line)
        no_new_line = heartRegex.sub('999', no_new_line )
        punc_strip_line = regex.sub('', no_new_line)

        #print(no_new_line)
        #print(line)
        #print(punc_strip_line)
        #print(len(punc_strip_line))

        tokens = punc_strip_line.split(' ')

        if(len(punc_strip_line) == 0):
            msg_label_ignore_flip = True
        elif msg_label_ignore_flip == True:
            msg_label_ignore_flip = False
        else:
            for e in tokens:
                if e in TokFound:
                    i = TokFound.index(e)
                    TokCount[i] += 1
                else:
                    TokFound.append(e)
                    TokCount.append(1)

f.close()

with open('WordCountData.txt', encoding='utf-8', mode='w+') as f:
    finalTokData = zip(TokFound,TokCount)
    soretedFinalTokData = sorted(finalTokData, key = lambda x:x[1], reverse = True)

    f.write(u'Word,Count\n')

    for e in list(soretedFinalTokData):
        f.write(u'' + str(e[0]) + ',' + str(e[1]) + '\n')
        print(e)

f.close()