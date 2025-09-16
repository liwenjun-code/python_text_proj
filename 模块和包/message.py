# 方式一
"""
import hm_message.send_message
import hm_message.receive_message

hm_message.send_message.send()
hm_message.receive_message.receive()

"""
# 方式二
"""
from hm_message import send_message,receive_message

send_message.send()
receive_message.receive()

"""
# 方式三

from hm_message.send_message import send
from hm_message.receive_message import receive

send()
receive()
