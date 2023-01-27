'''Send UDP Message'''

import logging
logger = logging.getLogger(__name__)
from eventmanager import Evt
from RHUtils import catchLogExceptionsWrapper
from EventActions import ActionEffect
import socket

def registerHandlers(args):
    if 'registerFn' in args:
        for effect in discover():
            args['registerFn'](effect)

def initialize(**kwargs):
    if 'Events' in kwargs:
        kwargs['Events'].on('actionsInitialize', 'action_UDP_message', registerHandlers, {}, 75, True)
        
@catchLogExceptionsWrapper
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
    logger.debug("Sent UDP message {} to {}:{}". format(UDP_message, UDP_ipaddress, UDP_port))

def discover():
    return [
        ActionEffect(
            'udpmessage',
            'UDP Message',
            UDPMessageEffect,
            [
                {
                    'id': 'text',
                    'name': 'UDP message',
                    'type': 'text',
                },
                {
                    'id': 'ipaddress',
                    'name': 'UDP IP Address',
                    'type': 'text',
                },
                {
                    'id': 'udpport',
                    'name': 'UDP Port',
                    'type': 'text',
                }

            ]
        )
    ]