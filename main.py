import eel
import signal
import os
import time


def main():

    signal.signal(signal.SIGUSR1, receiveSignal)

    signal.signal(signal.SIGTERM, terminateProcess)
    print('my pid is:', os.getpid())
    while True:
        print('Waiting...')
        time.sleep(3)
        # eel.init('web')
        # eel.start('main.html', block=False)

        # while True:
        # eel.sleep(10)
    eel._detect_shutdown()


def receiveSignal(signalNumber, frame):
    print('Received:', signalNumber)
    raise SystemExit('Exiting')
    return


def terminateProcess(signalNumber, frame):
    print('(SIGTERM) terminating the process')
    os._exit(os.EX_OK)


def goodbye():
    print("killing function")


main()
