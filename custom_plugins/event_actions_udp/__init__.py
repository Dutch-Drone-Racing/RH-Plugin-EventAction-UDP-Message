'''Send UDP Message'''

import logging
logger = logging.getLogger(__name__)
import RHData
from eventmanager import Evt
from EventActions import ActionEffect
import socket
from RHUI import UIField, UIFieldType, UIFieldSelectOption

class ActionsUDP():
    def __init__(self, rhapi):
        self._rhapi = rhapi

    def UDPMessageEffect(self, action, args):
        text = RHData.doReplace(self._rhapi, action['udp_message'], args)
        UDP_message = text
        UDP_ipaddress = action['udp_ipaddress']
        UDP_port = action['udp_port']
        UDP_portInt = int(UDP_port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        sock.sendto(bytes(UDP_message, "utf-8"), (UDP_ipaddress, UDP_portInt))
        logger.debug("Sent UDP message {} to {}:{}". format(UDP_message, UDP_ipaddress, UDP_port))

    def register_handlers(self, args):
        if 'register_fn' in args:
            for effect in [
                ActionEffect(
                    'UDP Message',
                    self.UDPMessageEffect,
                    [
                        UIField('udp_message', "UDP Message", UIFieldType.TEXT),
                        UIField('udp_ipaddress', "IP Address", UIFieldType.TEXT),
                        UIField('udp_port', "UDP Port", UIFieldType.TEXT)
                    ]
                )
            ]:
                args['register_fn'](effect)

def initialize(rhapi):
    actions = ActionsUDP(rhapi)
    rhapi.events.on(Evt.ACTIONS_INITIALIZE, actions.register_handlers)