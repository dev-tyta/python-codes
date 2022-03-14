import time, sys
indent = 0
indentIncrease = True

try:
    while True:
        print(" " * indent, end=" ")
        print("**********")
        time.sleep(0.1)

        if indentIncrease:
            indent = indent + 1
            if indent == 20:
                indentIncrease = False
        else:
            indent = indent - 1
            if indent == 0:
                indentIncrease = True
except KeyboardInterrupt:
    sys.exit()
