import math
from Crypto.Util.number import *

def nth_root(x, n):
    # Start with some reasonable bounds around the nth root.
    upper_bound = 1
    while upper_bound ** n <= x:
        upper_bound *= 2
    lower_bound = upper_bound // 2
    # Keep searching for a better result as long as the bounds make sense.
    while lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2
        mid_nth = mid ** n
        if lower_bound < mid and mid_nth < x:
            lower_bound = mid
        elif upper_bound > mid and mid_nth > x:
            upper_bound = mid
        else:
            # Found perfect nth root.
            return mid
    return mid + 1


n = 29975631800215657937493783863434112683656294942535397520359150860573029054795899767788769927839149304708188758416887641277324280355613271400904941070611372140457117747662223408542405106215206995200207640758261893896200215166153490918602741293850663257912193639687548512449008979500245369494009704210415156213039607019531327061604637859325214944011158998420893005901040659256611528987528906699903072144264608066816642440797472378250674183630413359791534413445494769269248545141877414804990036775500895937772387000305554995582804772280076985804145965150014436992291857408253869932893321744363684924634962694994879194241
c = 25500436459642209804929797892185191563830907623710642006332858273529200970795010398088408382227890912519946589217033189053728965737823533005095213744703891336518467220488636343293826730864490790395257719113114481236123260380825419591689910506682091430326705083813705483660526850065632087765588829706773397671875286624248394879538433763453533726014259942265046685464201407307353905506287805265767203343183534177579910544814435687897276972182928656556075188061661685596460591543011739810067816920839319499324897516400443823188483995275388169572500559642017660320849138514326543977310947366163719956182053261225627880926

# becasue n = q * p and p is equal to q , so just take a square root to get q

p = nth_root(n,2) #OverflowError: int too large to convert to float ,so use a custom function
q = p
print(p)
phi = (p-1)*(q-1)

d = lambda:d=1
print(d)
#lain_text = pow(c,d,n)
#print(long_to_bytes(plain_text))
