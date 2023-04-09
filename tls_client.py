from transitions import Machine
import random

class TLSClient(object):

    # RFC 8446, A.1.  Client
    #
    #                           START <----+
    #            Send ClientHello |        | Recv HelloRetryRequest
    #       [K_send = early data] |        |
    #                             v        |
    #        /                 WAIT_SH ----+
    #        |                    | Recv ServerHello
    #        |                    | K_recv = handshake
    #    Can |                    V
    #   send |                 WAIT_EE
    #  early |                    | Recv EncryptedExtensions
    #   data |           +--------+--------+
    #        |     Using |                 | Using certificate
    #        |       PSK |                 v
    #        |           |            WAIT_CERT_CR
    #        |           |        Recv |       | Recv CertificateRequest
    #        |           | Certificate |       v
    #        |           |             |    WAIT_CERT
    #        |           |             |       | Recv Certificate
    #        |           |             v       v
    #        |           |              WAIT_CV
    #        |           |                 | Recv CertificateVerify
    #        |           +> WAIT_FINISHED <+
    #        |                  | Recv Finished
    #        \                  | [Send EndOfEarlyData]
    #                           | K_send = handshake
    #                           | [Send Certificate [+ CertificateVerify]]
    # Can send                  | Send Finished
    # app data   -->            | K_send = K_recv = application
    # after here                v
    #                       CONNECTED

    # TLS client states
    states = ['START', 'WAIT_SH', 'WAIT_EE', 'WAIT_CERT_CR', 'WAIT_CERT', 'WAIT_CV', 'WAIT_FINISHED', 'CONNECTED']

    def __init__(self):

        # Give TLS client a name
        self.name = 'Bob'

        # Initialize the state machine
        self.machine = Machine(model=self, states=TLSClient.states, initial='START')

        # Adding transitions. 

        # At some point, every superhero must rise and shine.
        self.machine.add_transition(trigger='ClientHello', source='START', dest='WAIT_SH', before='send_ClientHello')

    def send_ClientHello(self):
        print("\u2192 Bob: Sending ClientHello [K_send = early data]")


bob = TLSClient()
print("\u25cb Bob: {}".format(bob.state))

bob.ClientHello()
print("\u25cb Bob: {}".format(bob.state))