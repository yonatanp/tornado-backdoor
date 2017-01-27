import sys
import signal

from tornado.ioloop import IOLoop
from tornado_backdoor import BackdoorServer


def handle_SIGINT(signum, frame):
    io_loop = IOLoop.instance()
    io_loop.add_callback(io_loop.stop)

if __name__ == '__main__':
    if sys.argv[1:]:
        port = int(sys.argv[1])
    else:
        port = 1234
    print "Interpreter listening for TCP connections on port %s..." % port
    signal.signal(signal.SIGINT, handle_SIGINT)
    server = BackdoorServer()
    server.listen(port)
    IOLoop.instance().start()

