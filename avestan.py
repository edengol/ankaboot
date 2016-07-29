# -*- coding: utf-8 -*-
"""
Transcribes text from proprietary encoding found on avesta.org using avesta.orgtranscription.otf
or ave_bl_l4.otf into Unicode encoding.
"""
transcription = {
    'a':u'𐬀', 'A':u'𐬁', 'b':u'𐬠', 'B':u'𐬡', 'c':u'𐬗', 'C':u'𐬴', 'd':u'𐬛', 'D':u'𐬜', 'e':u'𐬈',
    'E':u'𐬉', 'f':u'𐬟', 'F':u'𐬒', 'g':u'𐬔', 'G':u'𐬖', 'h':u'𐬵', 'i':u'𐬌', 'I':u'𐬍', 'j':u'𐬘',
    'k':u'𐬐', 'K':u'𐬳', 'l':u'𐬃', 'L':u'𐬄', 'm':u'𐬨', 'M':u'𐬢', 'n':u'𐬥', 'N':u'𐬧', 'o':u'𐬊',
    'O':u'𐬋', 'p':u'𐬞', 'q':u'𐬚', 'Q':u'𐬜', 'r':u'𐬭', 'R':u'𐬮', 's':u'𐬯', 'S':u'𐬱', 't':u'𐬙',
    'T':u'𐬝', 'u':u'𐬎', 'U':u'𐬏', 'v':u'𐬆', 'V':u'𐬇', 'w':u'𐬎𐬎', 'W':u'𐬬', 'x':u'𐬑', 'X':u'𐬓',
    'y':u'𐬌𐬌', 'Y':u'𐬫', 'z':u'𐬰', 'Z':u'𐬲', '&':u'𐬅', '.':u'𐬼'
    }

def transcribe(input):
    return u''.join([transcription.get(c,c) for c in input])

def sample_texts():
    print transcribe('aCvm WohU WahiStvm astI')
    print transcribe('uStA astI uStA ahmAi')
    print transcribe('hyaT aCAi WahiStAi aCvm.')
    print transcribe('0 pa n&m i Yazd&, hOrmvzd i XadAe aBazUnI gurz Xarahe aBazAyAT, srOS i aSO i tagI i tan farm&n i Skaft zIn i zIn aBazAr i sA1Ar i d&m& i hOrmvzd bV rasAT. vZ hamA gunAh patit paSVm&nOm, vZ haraWistIn duSmat duZUxt duZWarvSt mvn pa gVqI minIT Waem guft Waem kard Waem jast Waem bun bUT vstvT vZ & gunAhihA maniSnI gaBvSnI kuniSnI tanI rw&nI gVqI mainyu&nI Oxe aBaxS paSVm& pa sv gaBvSnI pa patit hOm.')
