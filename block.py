from hashlib import sha256
from datetime import date, datetime
class Block:
  def __init__(self, data: str, prev_hash:str):
    self.timestamp = datetime.utcnow()
    self.data = data
    self.prev_hash = prev_hash
    self.calc_valid_hash()

  def __repr__(self) -> str:
    return self.to_string()

  def is_valid_hash(self, hash):
    return (hash.startswith('0' * 3))

  def to_string(self) -> str :
    return f"{self.data}\t{self.timestamp}\t{self.prev_hash}"

  def calc_valid_hash(self):
    nonce = 0
    hash = ''
    while(not self.is_valid_hash(hash)):
      temp = self.to_string() + str(nonce)
      hash = sha256(temp.encode()).hexdigest()
      nonce += 1

    self.hash = hash