def enough(cap, on, wait):
    free = cap - on
    toomuch = wait - free
    if free >= wait:
        return 0
    else:
        return toomuch
