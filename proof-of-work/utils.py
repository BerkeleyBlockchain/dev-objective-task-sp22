from hashlib import sha256
from datetime import datetime


def get_target(leading_zeros=0):
    """
    The target is a 256-bit number that all Bitcoin clients share.
    The double SHA-256 hash of a block's header must be less than or equal
    to the current target for the block to be accepted by the network. The
    lower the target, the more difficult it is to generate a block.
    """
    return int('1' * (256 - leading_zeros), 2)


def double_sha256(string):
    """
    Bitcoin uses double SHA-256 (ie. hashing twice with SHA-256) as its hash
    function. This function applies double SHA-256 to a string and returns the
    result as a hex string.
    """
    encoded = string.encode('utf-8')
    return sha256(sha256(encoded).digest()).hexdigest()


def hexstring_to_int(hex_string):
    """
    Convert hex string to an int
    """
    return int(hex_string, 16)


def is_power_of_two(n):
    """
    Check whether `n` is an exponent of two
    """
    return n != 0 and ((n & (n - 1)) == 0)


def now():
    """
    Return the current time as a string
    """
    return str(datetime.now())
