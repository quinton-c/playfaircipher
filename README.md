# playfaircipher
Inspired by the movie 'National Treasure', I have been having fun with Playfair Ciphers since about middle school. 
I always wanted to build an auotmated one, so now that I am learning JavaScript, I have!

Explanation on how a Playfair Cipher works can be found here: https://en.wikipedia.org/wiki/Playfair_cipher

Traditionally, a Playfair Cipher utilizes a 5x5 grid to perform the encryption. 
This forces a chosen pair of characters to share a space, as there is one less spot than there are letters of the alphabet. 
Often people combine either `I` and `J` or `Y` and `Z`. The reader then must decide which is the correct letter based on context.
This also limits the messages you can send, as it does not support numbers (though, numbers can obviously be spelled out, but who has the time?).
I have chosen to use a 6x6 grid (this concept is not my invention, by any means), offering space for 36 characters, 
which happens to perfectly fit all 26 letters, plus the 10 numerical digits 0-9.

I hope to one day build an HTML page to act as an interface for this script, but for now it just runs on its own.

To use it, change the input variable to the message you wish to encrypt (or decrypt), and the passkey variable to your secret password. 
Then, at the bottom of the code both encrypt and decrypt functions have been called, with the output being logged to the console. 
Simply uncomment the function you wish to use, and comment out the other. 
Essentially, if you wish to encrypt a message, call the encrypt function, and if you wish to decrypt a message, call the decrypt function. 
Their syntax is `(input, passkey)`.

Upon decrypting a secret message, the user must then remove any instances of the letter `q` that are out of place contextually. 
This is simply due to how Playfair Ciphers handle instances of back to back letters.

Note that the output string contains no spaces, punctuation, or special characters, and is all lowercase. 
I initially wanted to work on making the output format reflect the input format next, so punctuation etc. can be retained.
Upon further thought, however, that seems like it's actually a really bad idea cryptography-wise, 
as it would reveal more patterns and clues in the message, allowing for faster decryption.


Update version 0.1.1: In initial testing, I ran into a situation while trying to encode "secret message to encode" where the double 's' in message wound up breaking my code. The two S's were positioned so they stayed together when the input was split up into pairs. This caused an issue where the code was unable to retrieve the coordinates for the second letter, since it would always match the first, so the code couldn't get past the first `if` statement. Currently, this is solved by checking if the two characters are the same, then retreiving the coordinates for the letter and setting both output coordinates equal to that. I suspect there is a more proper way that Playfair Ciphers handle this situation, so I will be adding that to my list of items to research and develop.


Update version 0.2: I have refactored parts of the code to isolate tasks better. The code now contains separate functions for encrypting and decrypting messages, and handles all appropriate rules for coordinate manipulation as laid out on the cipher's Wikipedia page.
