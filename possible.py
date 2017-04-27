import math
#haathi
def possible_haathi(current,end):
    if(((end-current)%8==0) or ((current-end)%8==0) or ((math.floor(current/8)*8)<end<=(math.ceil(current/8)*8))):
        return "true"
    else:
        return "false"
#pyada
def possible_pyada(current,end):
    if((end-current)==8 or (current-end)==8):
        return "true"
    else:
        return "false"
#oontth
def possible_oontth(current,end):
    if((end-current)%9==0 or (end-current)%7==0):
        return "true"
    else:
        return "false"
#ghoda
def possible_ghoda(current,end):
    if(abs(end-current) in [6,10,15,17]):
        return "true"
    else:
        return "false"
#raja
def possible_raja(current,end):
    if(abs(end-current) in [1,7,8,9]):
        return "true"
    else:
        return "false"

def possible_rani(current,end):
    if((possible_oontth(current,end) == 'true') or (possible_haathi(current,end) == 'true')):
        print("true")
    else:
        print("false")
possible_rani(1,57)
