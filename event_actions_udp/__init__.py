'''Send UDP Message'''

import logging
logger = logging.getLogger(__name__)

#from eventmanager import Evt
#from RHUtils import catchLogExceptionsWrapper
from EventActions import ActionEffect
import socket
from RHUI import UIField, UIFieldType, UIFieldSelectOption


def register_handlers(args):
    if 'register_fn' in args:
        for effect in discover():
            args['register_fn'](effect)

def initialize(rhapi):
    rhapi.events.on('actionsInitialize', 'action_UDP_message', register_handlers, {}, 75, True)
        
def UDPMessageEffect(action, args):
    text = action['text']
    if 'node_index' in args:
        pilotNode = str(RACE.node_pilots[args['node_index']])
        text = text.replace('%PILOT_NODE%', pilotNode)

    UDP_message = text
    UDP_ipaddress = action['ipaddress']
    UDP_port = action['udpport']
    UDP_portInt = int(UDP_port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.sendto(bytes(UDP_message, "utf-8"), (UDP_ipaddress, UDP_portInt))
    #logger.debug("Sent UDP message {} to {}:{}". format(UDP_message, UDP_ipaddress, UDP_port))


def discover():
    return [
        ActionEffect(
            'udpmessage',
            'UDP Message',
            UDPMessageEffect,
            [
                UIField('udp_message', "UDP Message", UIFieldType.text),
                UIField('udp_ipaddress', "IP Address", UIFieldType.text),
                UIField('udp_port', "UDP Port", UIFieldType.text)
            ]
        )
    ]
