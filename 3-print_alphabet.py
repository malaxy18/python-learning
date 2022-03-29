def listarascii():
  return [ord(i) for i in range(ord('a'),ord('z')+1)]
print(listarascii())