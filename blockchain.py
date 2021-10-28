import block 
from typing import List
class Blockchain():
  def __init__(self) -> None:
    self.blocks = []
    self.set_genesis_block()


  def set_genesis_block(self):
    data = "Genesis\t"
    prev_hash = '0' * 64
    genesis_block = block.Block(data, prev_hash)
    self.blocks.append(genesis_block)

  def next_block(self, data):
    curr_block = block.Block(data, self.blocks[-1].hash)
    self.blocks.append(curr_block)

  def print_blockchain(self):
    for block in self.blocks:
      print(block)