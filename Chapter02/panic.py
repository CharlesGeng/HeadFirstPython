phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# BEGIN transform into on tap
plist.remove('D')
plist.remove('\'')
for i in range(4):
    plist.pop()
plist.insert(2, plist.pop(3))
plist.extend([plist.pop(), plist.pop()])
# END transform into on tap

new_phrase = ''.join(plist)
print(new_phrase)
print(plist)