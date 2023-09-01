from local.poc import LocalPoc
from remote.poc import RemotePoc


def main(poc: LocalPoc | RemotePoc):
    poc.run()


if __name__ == '__main__':
    poc = LocalPoc()
    main(poc)
