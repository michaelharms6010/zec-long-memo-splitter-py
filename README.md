# ZEC Long Memo Splitter

This is an app for splitting long Zcash memos (greater than 512 characters). For the foreseeable future, this will be done using 0 ZEC transactions with no fee. 

## Instructions

In its current implementation, you must be running zcashd locally. 

* Put your zcash FROM address on line one of memotext.txt
* Put your zcash TO address on line two of memotext.txt
* Type your message in memotext.txt on the lines below.
* (For now that means 512 characters per line. Text splitting is a planned upgrade)
* Run long-memo.py
* Move the output script to the same folder as your zcash-cli installation (if you don't have zcash-cli in your $PATH variable. You probably don't.)
* Run the script. All the lines of text will be sent in separate memos, at ZERO cost to you. Nice!

### Contact

I can be reached at @michaelharms70 on twitter or via shielded memo at zs1zxeehvq02nf0javeygdxnj6a78quvvlu7gsgg0e39n4uvp9hpdnyy3l4e494vt5kp4wjgrm7mtr