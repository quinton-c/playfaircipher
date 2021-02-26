/*Playfair Cipher using a 6x6 grid to support numbers*/
//Get input and passkey
let input = 'hdvoeytpdcdiwabdotlbvaroljcpledlskljyoq1';
let passkey = 'old tavern';
let output = '';

// Clean input
    input = input.replace(/\s+/g,'');
    input = input.replace(/[^a-zA-Z0-9]/g, '');
    input = input.toLowerCase();
if (input.length%2 != 0) {
    input += 'z';
};

//Group characters into pairs for encoding
let inputArray = [];
for (let i = 0; i < input.length; i += 2) {
    let subArray = [input[i], input[i+1]];
    inputArray.push(subArray);
};

//Removes duplicate characters from string. Will need this function later.
const removeDuplicateCharacters = (string) => {
    return string
        .split('')
        .filter(function(item, pos, self) {
        return self.indexOf(item) == pos;
        })
        .join('');
       }

//Clean passkey (needs no spaces, special characters, or duplicate characters)
const acceptedChars = 'abcdefghijklmnopqrstuvwxyz0123465789';
    passkey = passkey.replace(/\s+/g,'');
    passkey = passkey.replace(/[^a-z0-9]/g,'');
    passkey = passkey.toLowerCase();
    passkey = passkey += acceptedChars;
    passkey = removeDuplicateCharacters(passkey);

//Generates playfair grid
let playfairArray = [];
for (let i = 0; i < passkey.length; i += 6) {
    let subArray = [passkey[i], passkey[i+1], passkey[i+2], passkey[i+3], passkey[i+4], passkey[i+5]];
    playfairArray.push(subArray);
}

// need to find playfair coordinates of input character pairs stored in each input subarray, stay in same playfair subarray and switch indexes
for (i = 0; i < inputArray.length; i++) {
    let char1 = inputArray[i][0];
    let char2 = inputArray[i][1];
    let pos1;
    let pos2;
    let row1;
    let row2;
    for (y = 0; y < playfairArray.length; y++) {
        for (x = 0; x < playfairArray[y].length; x++) {
            if (char1 === playfairArray[y][x]) {
                pos2 = x;
                row1 = y;
            } else if (char2 === playfairArray[y][x]) {
                pos1 = x;
                row2 = y;
            }
        }
    }
    output += playfairArray[row1][pos1] + playfairArray[row2][pos2];
}

console.log(output);