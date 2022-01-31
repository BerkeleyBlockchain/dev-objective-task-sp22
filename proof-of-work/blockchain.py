import utils


class Block:
    def __init__(self, prev_hash, merkle_root, target=utils.get_target(0), nonce=0, txs=[]):
        """
        Initialize a block.
        """
        # Block header
        self.prev_hash = prev_hash      # Hash of previous block (string)
        self.merkle_root = merkle_root  # Merkle root hash (string)
        self.timestamp = utils.now()    # Time at block creation (string)
        self.target = target            # Target boundary for proof of work (integer)
        self.nonce = nonce              # Nonce for proof of work (integer)

        # Transaction data
        self.txs = txs                  # List of transactions (strings)

    def hash(self):
        """
        Return hex string of double the SHA-256 hash of the block header.
        """
        block_data = (str(self.prev_hash) +
                      str(self.merkle_root) + 
                      str(self.timestamp) + 
                      str(self.target) +
                      str(self.nonce))
        return utils.double_sha256(block_data)

    def __str__(self):
        """
        Returns a string representation of a block. Can be used to
        debug with print() statements.
        """
        template = "{} {{\n  prev_hash: {},\n  merkle_root: {},\n  timestamp: {},\n  target: {},\n  nonce: {}\n}}"
        return template.format(self.hash(), self.prev_hash, self.merkle_root, self.timestamp, self.target.to_bytes(32, 'big').hex(), self.nonce)


class Chain:
    def __init__(self):
        """
        Initialize a chain and create the genesis block.
        """
        genesis = Block(
            prev_hash="0",    # Arbitrary data
            merkle_root="0",  # Arbitrary data
        )

        self.head = genesis.hash()
        self.height = 0
        self.blocks = { self.head : genesis }

    def add_block(self, block):
        """
        Add a block to the chain.
        """
        block.prev_hash = self.head
        self.head = block.hash()
        self.blocks[self.head] = block
        self.height += 1

    def __str__(self):
        """
        Returns a string representation of a chain. Can be used to
        debug with print() statements.
        """
        curr, i, res = self.head, 0, ""
        while curr in self.blocks:
            block = self.blocks[curr]
            res += '\nBlock {}: {}'.format(str(self.height - i), str(block))
            curr = block.prev_hash
            i += 1
        return res
