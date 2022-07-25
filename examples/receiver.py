import getpass
import time

from spade import quit_spade

from spade_bdi.bdi import BDIAgent

if __name__ == '__main__':
    server = input("XMPP Server> ")
    passwd = getpass.getpass()

    a = BDIAgent("BDIReceiverAgent@" + server, passwd, "receiver.asl")
    a.start()

    time.sleep(10)
    a.stop().result()

    quit_spade()