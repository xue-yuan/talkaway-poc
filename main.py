import sys
from local.poc import LocalPoc
from remote.poc import RemotePoc


def main(poc: LocalPoc | RemotePoc):
    poc.run()


def help():
    print("python main.py [local|remote]")


if __name__ == '__main__':
    poc = None

    if len(sys.argv) != 2:
        help()
        exit()

    if sys.argv[1] == "local":
        print("[!] Running on Local.")
        poc = LocalPoc()
    elif sys.argv[1] == "remote":
        print("[!] Running on Remote.")
        poc = RemotePoc()
    else:
        help()

    main(poc)
