from blockchain import *
import utils
import random

"""
Developer Objective Task: Proof of Work

We have provided starter code for a toy implementation of a proof of work blockchain.
Please complete the following functions and look up unfamiliar concepts if needed. Office
hours will be offered, so please don't hesistate to ask us questions! Good luck!

Note: Do not import any external libraries with the exception of the ones provided.
Only the code in this file will be graded, so please do not modify any other files.
"""


def compute_merkle_root(txs):
    """
    Compute the merkle root value for the given transactions. Use utils.double_sha256
    as the hash function. Duplicate the last transaction as needed if the number of
    transactions is not a power of 2. Note: Order matters for the autograder.
    Please compute the merkle root in the order the transactions are given, using string
    concatenation to compute the hashes.
    """
    pass


def mine_next_block(chain, txs, difficulty):
    """
    Mine the next block by guessing a valid nonce given the current target
    and a chain object. For simplicity, our toy implementation defines difficulty as
    the number of leading zero bits in the target. To mine a block, find a nonce such
    that when hashed with the block, produces a resulting number that is less than or
    equal to the target.
    """
    pass


def chainwork(chain):
    """
    In the case of conflicts, proof of work accepts the "longest chain"
    as the valid one. However, you cannot determine this by simply
    counting the number of blocks. Chainwork is defined as the expected
    number of hash computations required to build that chain. The "longest chain"
    is the chain with the most chainwork. Chainwork for a single block can be
    computed using the following formula: 
    (2 ^ 256) / (CURRENT_TARGET + 1)
    """
    pass


def get_valid_chain(chains):
    """
    Given a list of conflicting chains, return the valid chain based on chainwork. Feel
    free to use the previous function in your answer! This function should be very short.
    """
    pass
