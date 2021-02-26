# playfaircipher
Inspired by the movie 'National Treasure', I have been having fun with Playfair Ciphers since about middle school. I always wanted to build an auotmated one, so now that I am learning JavaScript, I have!

Explanation on how a Playfair Cipher works can be found here: https://en.wikipedia.org/wiki/Playfair_cipher

Traditionally, a Playfair Cipher utilizes a 5x5 grid to perform the encryption. This forces a chosen pair of characters to share a space, as there is one less spot than there are letters of the alphabet. Often people combine either `I` and `J` or `Y` and `Z`. The reader then must decide which is the correct letter based on context.
This also limits the messages you can send, as it does not support numbers.
I have chosen to use a 6x6 grid (this concept is not my invention, by any means), offering space for 36 characters, which happens to perfectly fit all 26 letters, plus the 10 numerical digits 0-9.

I hope to one day build an HTML page to act as an interface for this script, but for now it just runs on its own.

To use it, change the input variable to the message you wish to encode, and the passkey variable to your secret password. The code will output your encrypted message. 
To decrypt the secret message, just run it back through the code. The encryption and decryption use the same process, so as long as you have the correct passkey, the code works both ways.
Note that the output string contains no spaces, punctuation, or special characters, and is all lowercase. I would like to work on making the output format reflect the input format next, so punctuation etc. can be retained.

I suppose I could simply use a larger grid to support punctuation and special characters, though my inital thought was to perform a function on the output that loops through the input string and grabs the special characters then inserts them at the same index in the output string, however, using the larger grid would have the added functionality of using the special characters in the encryption, maybe making it more robust? I guess I'll just have to tinker with that and see what I find out.
More things I would like to add to this code as I develop it would be more rules on how to handle characters in the same row or columm. If you look at the Wikipedia article linked above, you'll see there are different rules for how to encypt the output based on how the input letters are arranged in the grid. This code currently treats all input pairs as if they form a rectangle, and simply switches the index numbers. This presents a weakness, in that if two characters are in the same column of the grid (ie. they have the same index number), that pair will not be changed in the output, and letters which share a row are simply flipped, but are still the same two letters.

Going forward, I may package the whole thing up as a function which accepts arguments of `input message` and `passkey`. This may allow me to create an encode version and a decode version, to account for the encrypt and decrypt rules being different when a pair of letters is in the same row or column, unlike when they form a rectangle.
