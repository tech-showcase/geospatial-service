import argparse


def parse():
    parser = argparse.ArgumentParser(description='Run service')
    parser.add_argument('--port',
                        '-p',
                        dest='port',
                        default=8081,
                        help='Port which service will listen to')
    args = parser.parse_args()
    return args
