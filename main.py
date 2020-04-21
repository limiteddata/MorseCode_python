wordSeparator = "||"
letterSeparator = "|"

fractionated_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
fractionated_Table = ['...','..-','..|','.-.','.--','.-|','.|.','.|-','.||','-..','-.-','-.|','--.','---','--|','-|.','-|-','-||','|..','|.-','|.|','|-.','|--','|-|','||.','||-']

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','0','!','@','&','(',')','-','_','=','+','.',',','/','?',';',':','\'','"']
morse = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','.----','..---','...--','....-','-....','--...','---..','----.','-----','-.-.--','.--.-.', '.....', '.-...', '-.--.', '-.--.-', '-....-', '..--.-', '-...-', '.-.-.', '.-.-.-', '--..--', '-..-.', '..--..', '-.-.-.', '---...', '.----.', '.-..-.']
def encodeWord(word):
    encodedMessage = ""
    word = word.lower()
    ch = list(word)
    for x,c in enumerate(ch):
        if c in alphabet:
            encodedMessage += morse[alphabet.index(c)]
            if (x+1) != len(ch):
                encodedMessage += letterSeparator
        else:
            encodedMessage += "? "
    return encodedMessage
def decodeWord(word):
    decodeedMessage = ""
    for c in word.split(letterSeparator):
        if c in morse:
            decodeedMessage += alphabet[morse.index(c)]
        else:
            decodeedMessage += "? "
    return decodeedMessage
def encodeMessage(message):
    encoded = ""
    words = message.split(" ")
    for x, word in enumerate(words):
        encoded += encodeWord(word)
        if (x+1) != len(word):
            encoded += wordSeparator
    return encoded
def decodeMessage(message):
    decoded = ""
    words = message.split(wordSeparator)
    for x, word in enumerate(words):
        decoded += decodeWord(word)
        if (x+1) != len(words):
            decoded += " "
    return decoded

def fractionEncode(message):
    msg = ""
    for i in range(0, len(message), 3):
        char = message[i:i+3]
        for i in range(len(char),3):
            char +="."
        if char in fractionated_Table:
            msg += fractionated_alphabet[fractionated_Table.index(char)]
    return msg

def fractionDecode(message):
    msg = ""
    ch = list(message)
    for x,c in enumerate(ch):
        if c in fractionated_alphabet:
            msg += fractionated_Table[fractionated_alphabet.index(c)]
    msg = decodeMessage(msg)
    return msg


msg = input("Write your message:")
key = input("Write your key(default:ABCDEFGHIJKLMNOPQRSTUVWXYZ press enter to skip):")
wSeparator = input("Write your word separator (default: || press enter to skip):")
lSeparator = input("Write your letter separator (default: | press enter to skip):")

if(key != ""):
    fractionated_alphabet = list(key)
if(wSeparator != ""):
    wordSeparator = wSeparator
if(lSeparator != ""):
    letterSeparator = lSeparator
    fractionated_Table = ['...','..-','..'+letterSeparator,'.-.','.--','.-'+letterSeparator,'.'+letterSeparator+'.','.'+letterSeparator+'-','.'+letterSeparator+letterSeparator,'-..','-.-','-.'+letterSeparator,'--.','---','--'+letterSeparator,'-'+letterSeparator+'.','-'+letterSeparator+'-','-'+letterSeparator+letterSeparator,letterSeparator+'..',letterSeparator+'.-',letterSeparator+'.'+letterSeparator,letterSeparator+'-.',letterSeparator+'--',letterSeparator+'-'+letterSeparator,letterSeparator+letterSeparator+'.',letterSeparator+letterSeparator+'-']


enc = encodeMessage(msg)
fracEnc = fractionEncode(enc)
dec = decodeMessage(enc)
fracDec = fractionDecode(fracEnc)



print("Your message was:",msg)
print("Your encoded message in morse is:",enc)
print("Your fractioned message is:",fracEnc)
print("Your decoded message from morse is:",dec)
print("Your fractioned decoded message is:",fracDec)
