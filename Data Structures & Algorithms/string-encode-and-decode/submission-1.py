class Solution:
  def encode(self, strs: List[str]) -> str:
    encoded_string = ""
    for s in strs:
      len_s = len(s)
      encoded_string += str(len_s) + "$" + s
    print(f"encoded: {encoded_string}")
    return encoded_string

  def decode(self, s: str) -> List[str]:
    i = 0
    decoded_string = []
    while i < len(s):
      amountChar = 0
      j = i
      while s[j] != "$":
        j += 1
      print(f"debug=== amountChar {s[i:j]}")
      amountChar = int(s[i:j])
      print(f"debug=== extracting {s[j+1:j+amountChar+1]}")
      decoded_string.append(s[j + 1 : j + amountChar + 1])
      i = j + amountChar + 1
    return decoded_string