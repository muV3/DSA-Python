import time


def countdown(i):
    if i >= 0:
        print(i)
        time.sleep(0.5)
        countdown(i - 1)
    else:
        return


countdown(5)
