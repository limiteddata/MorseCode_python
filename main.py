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
                encodedMessage += " "
        else:
            encodedMessage += "? "
    return encodedMessage
def decodeWord(word):
    decodeedMessage = ""
    for c in word.split(" "):
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
        if (x+1) != len(words):
            encoded += " / "
    return encoded
def decodeMessage(message):
    decoded = ""
    words = message.split(" / ")
    for x, word in enumerate(words):
        decoded += decodeWord(word)
        if (x+1) != len(words):
            decoded += " "
    return decoded

msg = input("Write your message:")
enc = encodeMessage(msg)
dec = decodeMessage(enc)
print("Your message was:",msg)
print("Your message is:",enc)
print("Your decoded message is:",dec)
