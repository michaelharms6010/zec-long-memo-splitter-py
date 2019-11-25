memotext = open("memotext.txt")

output = open("output-script.txt", "w")

textList = []
for i in memotext:
    textList.append(i)

addyFrom=textList[0].rstrip("\n")
addyTo=textList[1].rstrip("\n")

for i in textList:
    hextext=i.encode("hex")
    outstring = 'zcash-cli z_sendmany "' + addyFrom + ' "[{\\"address\\" : \\"'+addyTo+ '\\",\\"amount\\": 0.00000001, \\"memo\\":\\"'+hextext+'\\"}]"\n'
    if textList.index(i) > 1:
        output.write(outstring)
    

    # z_sendmany "$ZADDR" "[{\"amount\": 0.8, \"address\": \"$FRIEND\"}]"

print textList