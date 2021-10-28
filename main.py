from blockchain import Blockchain

blockchain = Blockchain()

blockchain.next_block("First Block")
blockchain.next_block("Second Block")
blockchain.next_block("Third Block")
blockchain.next_block("Fourth Block")
blockchain.next_block("Fifth Block")
blockchain.next_block("Sixth Block")

blockchain.print_blockchain()
