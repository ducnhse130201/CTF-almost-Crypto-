#!/usr/bin/python
import SocketServer
import logging
from ciphers import vn_x931, names


ADDRESS = 'localhost'
PORT = 33338
TIMEOUT = 300.0
logger = None
flag = "flag"


def read_message(s):
    return s.recv(33)[0:32]


def send_message(s, message):
    send_buffer = message + "\n"
    s.sendall(send_buffer)


class ForkingTCPServer(SocketServer.ForkingMixIn, SocketServer.TCPServer):
    pass


class ServiceServerHandler(SocketServer.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        SocketServer.BaseRequestHandler.__init__(
            self, request, client_address, server)

    def play(self, data):
        cs, s = vn_x931()
        send_message(
            self.request, "Do you know throughout our history, there were many names used to refer to Vietnam?")
        send_message(self.request, 'Since the early 1940s, the use of {0} has been widespread. Oops, I mean "{1}" :)'.format(
            s, names[0]))
        send_message(
            self.request, 'Can you guess some of my previous names? What is your guess?')
        i = 0
        for c in reversed(cs):
            i += 1
            m = read_message(self.request)
            if m != c:
                send_message(self.request, 'Nah, it is not one of my names')
                return
            else:
                send_message(
                    self.request, 'Good guess. My previous name was "{0}"'.format(names[i]))
                if i < len(cs):
                    send_message(
                        self.request, 'Now try to guess another name: ')
        send_message(
            self.request, 'Bingo. You guessed all the names correctly. Here is your award: {0}.'.format(data))

    def handle(self):
        logger.info('Accepted connection from {0}'.format(
            self.client_address[0]))
        self.request.settimeout(TIMEOUT)
        try:
            with open(flag, 'rb') as f:
                data = f.read()
                self.play(data)
        except Exception as ex:
            logger.error(str(ex), exc_info=True)
        finally:
            logger.info('Processed connection from {0}'.format(
                self.client_address[0]))
        return


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)
    address = (ADDRESS, PORT)
    server = ForkingTCPServer(address, ServiceServerHandler)
    server.serve_forever()
