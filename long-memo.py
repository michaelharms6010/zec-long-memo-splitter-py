memotext = open("memotext.txt")

addyFrom=input("FROM address:")
addyTo = input("TO address:")
output = open("output-script.txt", "w")

textList = []
for i in memotext:
    textList.append(i)


for i in textList:
    hextext=i.encode("hex")
    outstring = 'zcash-cli z_sendmany "' + addyFrom + ' "[{\\"address\\" : \\"'+addyTo+ '\\",\\"amount\\": 0.00000001, \\"memo\\":\\"'+hextext+'\\"}]"'
    output.write(outstring)


    # z_sendmany "$ZADDR" "[{\"amount\": 0.8, \"address\": \"$FRIEND\"}]"

print textList