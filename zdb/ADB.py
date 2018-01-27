



################################################
def adbForward(dev):
    port = "23946"
    str = "tcp:{}".format(port)
    print ("adb forward {}".format(str))
    dev.forward(str, str)
################################################
def adbForwardJdwp(dev, uid, port):
    #port = "8800"
    str = "tcp:{}".format(port)
    uids = "jdwp:{}".format(uid)
    print ("adb forward {} {}".format(str, uids))
    dev.forward(str, uids)