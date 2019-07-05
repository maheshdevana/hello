puthan = input()

print(''.join([ puthan[x:x+2][::-1] for x in range(0, len(puthan), 2) ]))
