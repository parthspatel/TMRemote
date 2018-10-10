from time import sleep

from gkrequest import GKRequest


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main():
    with open('url.txt', 'r') as file:
        urls = file.read().splitlines()

    with open('msg.txt', 'r') as file:
        msg = str(file.read())

    for url in urls:
        if GKRequest().make_request(url, msg):
            print('> ' + bcolors.OKGREEN + 'Success: ' + bcolors.ENDC + '{}'.format(url))
        else:
            print('> ' + bcolors.FAIL + 'Failure: ' + '{}'.format(url) + bcolors.ENDC)
        sleep(35)

    return


if __name__ == '__main__':
    main()
