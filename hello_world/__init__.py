"""
When you install this package you find the function in this file at hello_world.other_greeting()
"""


# defines what is available when we do a `from hello_world import *`
__all__ = ['other_greeting']

def other_greeting():
    print("Evening comrade")


def secret_greeting():
    """This greeting will only be shown to people that know about it, anyone using a import * will not see this"""
    print("Very secret greeting!)
