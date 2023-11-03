# IF function

def IF(cond, A, B):
# Specifies a logical test to perform
    try:
        if cond:
            return A
        else:
            return B
    except:
        return
