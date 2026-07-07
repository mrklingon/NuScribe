from microbit import *
import random
import time
import speech
def verses():
    global i23, j316, vocab
    i23 = ["Thou",
        "wilt",
        "keep",
        "him",
        "in",
        "perfect",
        "peace",
        "whose",
        "mind",
        "is",
        "stayed",
        "on",
        "thee:",
        "because",
        "he",
        "trusteth",
        "in",
        "thee"]
    j316 = ["For",
        "God",
        "so",
        "loved",
        "the",
        "world",
        "that",
        "he",
        "gave",
        "his",
        "only",
        "begotten",
        "Son",
        "that",
        "whosoever",
        "believeth",
        "in",
        "him",
        "should",
        "not",
        "perish",
        "but",
        "have",
        "everlasting",
        "life"]
    vocab = ["because",
        "begotten",
        "believeth",
        "but",
        "everlasting",
        "For",
        "gave",
        "God",
        "have",
        "he",
        "him",
        "his",
        "in",
        "is",
        "keep",
        "life",
        "loved",
        "mind",
        "not",
        "on",
        "only",
        "peace",
        "perfect",
        "perish",
        "should",
        "so",
        "Son",
        "stayed",
        "that",
        "the",
        "thee",
        "thee:",
        "Thou",
        "trusteth",
        "whose",
        "whosoever",
        "wilt",
        "world"]


def mkWord():
    global rules, cons, vow, r, wrd, z
    rules = ["CVC", "CV", "CVCVC"]
    cons = "tdkp"
    vow = "aeiouy"
    r = random.choice(rules)
    wrd = ""
    index = 0
    while index <= len(r) - 1:
        z =r[index]
        if z == "C":
            wrd = "" + wrd + cons[random.randrange(len(cons))]
        else:
            wrd = "" + wrd + vow[random.randrange(len(vow))]
        index += 1
    return wrd

def mkLang():
    global tmax
    tmax = []
    for value4 in vocab:
        tmax.append(mkWord())

def tranWrd(src):
    return tmax[vocab.index(src)]


mode = 5
modes =["SI","SJ","MX","TI","TJ"]
SI =0
SJ =1
MX =2
TI = 3
TJ = 4

verses()
mkLang()
while True:
  if button_a.was_pressed():
      mode= mode+1
      if mode>4:
          mode = 0
      display.scroll(modes[mode])

  if button_b.was_pressed():
      if mode==SI:
          for w in i23:
              display.scroll(w,80)
      
      if mode==SJ:
          for w in j316:
              display.scroll(w,80)   
              
      if mode==TJ:
          for w in j316:
              display.scroll(tranWrd(w),80)   
              
      if mode==TI:
          for w in j316:
              display.scroll(tranWrd(w),80)   
      if mode==MX:
          display.show(Image.DIAMOND)
          mkLang()
          display.show(Image.DIAMOND_SMALL)
          time.sleep(.3)
          display.clear()
                       

              
