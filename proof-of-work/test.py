import unittest
import utils
import random
from blockchain import *
from proof_of_work import *


class TestMerkleRoot(unittest.TestCase):
    def test_merkle_root_pow_2(self):
        """
        Test merkle root computation with 4 transactions
            H(H(a, b), H(c, d))
            /            \  
            H(a, b)       H(c, d)
            /   \         /   \  
            a     b       c     d
        """
        txs = ['a', 'b', 'c', 'd']
        root = compute_merkle_root(txs)
        self.assertEqual(root, "20c12afdb2ce90da744e7f06424176c0c36f633be6cadd4eeafcda65855a7a73")


    def test_merkle_root_odd(self):
        """
        Test merkle root computation with 5 transactions (padded to a power of 2)
            H(H(H(a,b), H(c,d)), H(H(e,e), H(e,e)))
                    /                     \ 
            H(H(a,b), H(c,d))     H(H(e,e), H(e,e))
                /        \            /        \ 
            H(a,b)   H(c,d)       H(e,e)   H(e,e)
            /  \     /  \         /  \     /  \ 
            a    b   c    d       e    e   e    e
        """
        txs = ['a', 'b', 'c', 'd', 'e']
        root = compute_merkle_root(txs)
        self.assertEqual(root, "61100eb5b36ca42f9f453cd1b3d0d56e8a4c8141af3b334fd544f656197f1649")


class TestMining(unittest.TestCase):
    def test_single(self):
        """
        Test mining a single block with difficulty of 10
        """
        chain = Chain()

        difficulty = 10
        genesis_hash = chain.head
        target = utils.get_target(difficulty)
        txs = ['a', 'b', 'c', 'd']
        mr = compute_merkle_root(txs)

        mine_next_block(chain, txs, difficulty)
        hash_value = utils.hexstring_to_int(chain.head)
        mined_block = chain.blocks[chain.head]

        self.assertEqual(chain.height, 1)
        self.assertLessEqual(hash_value, target)
        self.assertEqual(mined_block.target, target)
        self.assertEqual(mined_block.merkle_root, mr)
        self.assertEqual(mined_block.prev_hash, genesis_hash)
        self.assertEqual(chain.head, mined_block.hash())

    def test_multiple(self):
        """
        Test mining multiple blocks with varying difficulty
        """
        chain = Chain()

        for i in range(1, 100):
            difficulty = random.randint(1, 10)
            prev_hash = chain.head
            txs = [str(random.random()) for _ in range(8)]
            mr = compute_merkle_root(txs)
            target = utils.get_target(difficulty)

            mine_next_block(chain, txs, difficulty)
            hash_value = utils.hexstring_to_int(chain.head)
            mined_block = chain.blocks[chain.head]

            self.assertEqual(chain.height, i)
            self.assertLessEqual(hash_value, target)
            self.assertEqual(mined_block.target, target)
            self.assertEqual(mined_block.merkle_root, mr)
            self.assertEqual(mined_block.prev_hash, prev_hash)
            self.assertEqual(chain.head, mined_block.hash())


class TestChainwork(unittest.TestCase):
    def test_single(self):
        """
        Test chainwork for chain with only one block
        """
        chain = Chain()
        work = chainwork(chain)
        self.assertEqual(work, 1)

    def test_multiple(self):
        """
        Test chainwork for chain with uniform difficulty
        """
        difficulty = 7
        target = utils.get_target(difficulty)
        chain = Chain()

        for _ in range(100):
            dummy = Block(chain.head, "", target=target)
            chain.add_block(dummy)

        self.assertEqual(chainwork(chain), 12801)

    def test_varying(self):
        """
        Test chainwork for chain with varying difficulty
        """
        chain = Chain()

        difficulty = 7
        target = utils.get_target(difficulty)
        for _ in range(10):
            dummy = Block(chain.head, "", target=target)
            chain.add_block(dummy)

        difficulty = 10
        target = utils.get_target(difficulty)
        for _ in range(10):
            dummy = Block(chain.head, "", target=target)
            chain.add_block(dummy)

        self.assertEqual(chainwork(chain), 11521)
