# =============================
#   SEARCHES SCRIPTS
# =============================

def linearSearchBool(L, target):
    '''
    Returns True if target element is in list L
    '''
    for e in L:
        if e == target:
            return True
    return False

def linearSearch(L, target):
    '''
    Returns index of target element. Returns -1 if element not in list L
    '''
    for idx, e in enumerate(L):
        if e == target:
            return idx
    return -1