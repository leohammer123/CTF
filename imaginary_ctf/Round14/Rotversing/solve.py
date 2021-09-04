#!/usr/bin/env python3
import base64,codecs

msg = """sebz onfr64 vzcbeg o64qrpbqr nf rot42

cevag h"Jung vf gur synt?"

vs enj_vachg() == rot42(rot42(h"LIqBZSchqTkvoH13JxETqIbkBUuwZGy1GHuFMycKAJcwozk3MRESq2WhZQ0=")):
  cevag h"Pbeerpg!"
"""
msg = codecs.decode(msg,'rot13')


print(base64.b64decode(base64.b64decode(msg.split('"')[3])).decode())

