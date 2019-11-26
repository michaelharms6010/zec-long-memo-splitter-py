memotext = open("memotext.txt")

output = open("output-script.bat", "w")

textList = []
for i in memotext:
    textList.append(i.replace("~", ""))

addyFrom=textList[0].rstrip("\n")
addyTo=textList[1].rstrip("\n")

for i in textList:
    hextext=i.encode("hex")
    outstring = 'zcash-cli z_sendmany "' + addyFrom + '" "[{\\"address\\" : \\"'+addyTo+ '\\", \\"amount\\": 0.000, \\"memo\\":\\"'+hextext+'\\"}]" 1 0.00000001\n'
    if textList.index(i) > 1:
        output.write(outstring)
        output.write("timeout /t 150 /nobreak \n")
    

    # z_sendmany "$ZADDR" "[{\"amount\": 0.8, \"address\": \"$FRIEND\"}]"

print textList