// Helper: sanitize input for letters only (uppercase)
function sanitizeInput(text) {
  return text.toUpperCase().replace(/[^A-Z]/g, '');
}

// Caesar cipher encode function
function caesarEncode(text, shift) {
  shift = shift % 26;
  let result = '';

  for (let char of text) {
    const c = char.toUpperCase();
    if (c >= 'A' && c <= 'Z') {
      let code = c.charCodeAt(0) - 65;
      code = (code + shift + 26) % 26;
      result += String.fromCharCode(code + 65);
    } else {
      result += char; // non-letters unchanged
    }
  }
  return result;
}

// Caesar cipher decode function (shift backwards)
function caesarDecode(text, shift) {
  return caesarEncode(text, -shift);
}

// Vigenère encode
function vigenereEncode(plainText, key) {
  plainText = plainText.toUpperCase();
  key = key.toUpperCase();
  let result = '';
  let keyIndex = 0;

  for (let char of plainText) {
    if (char >= 'A' && char <= 'Z') {
      const pChar = char.charCodeAt(0) - 65;
      const kChar = key[keyIndex % key.length].charCodeAt(0) - 65;
      const encodedChar = String.fromCharCode(((pChar + kChar) % 26) + 65);
      result += encodedChar;
      keyIndex++;
    } else {
      result += char;
    }
  }
  return result;
}

// Vigenère decode
function vigenereDecode(cipherText, key) {
  cipherText = cipherText.toUpperCase();
  key = key.toUpperCase();
  let result = '';
  let keyIndex = 0;

  for (let char of cipherText) {
    if (char >= 'A' && char <= 'Z') {
      const cChar = char.charCodeAt(0) - 65;
      const kChar = key[keyIndex % key.length].charCodeAt(0) - 65;
      const decodedChar = String.fromCharCode(((cChar - kChar + 26) % 26) + 65);
      result += decodedChar;
      keyIndex++;
    } else {
      result += char;
    }
  }
  return result;
}

// Setup event listeners on DOM load
document.addEventListener('DOMContentLoaded', () => {
  // Caesar elements
  const caesarShift = document.getElementById('caesar-shift');
  const caesarInput = document.getElementById('caesar-input');
  const caesarOutput = document.getElementById('caesar-output');
  const caesarEncodeBtn = document.getElementById('caesar-encode');
  const caesarDecodeBtn = document.getElementById('caesar-decode');

  caesarEncodeBtn.addEventListener('click', () => {
    const shift = parseInt(caesarShift.value, 10);
    if (isNaN(shift) || shift < 1 || shift > 25) {
      alert('Please enter a valid shift between 1 and 25.');
      return;
    }
    const encoded = caesarEncode(caesarInput.value, shift);
    caesarOutput.value = encoded;
  });

  caesarDecodeBtn.addEventListener('click', () => {
    const shift = parseInt(caesarShift.value, 10);
    if (isNaN(shift) || shift < 1 || shift > 25) {
      alert('Please enter a valid shift between 1 and 25.');
      return;
    }
    const decoded = caesarDecode(caesarInput.value, shift);
    caesarOutput.value = decoded;
  });

  // Vigenère elements
  const vigenereKey = document.getElementById('vigenere-key');
  const vigenereInput = document.getElementById('vigenere-input');
  const vigenereOutput = document.getElementById('vigenere-output');
  const vigenereEncodeBtn = document.getElementById('vigenere-encode');
  const vigenereDecodeBtn = document.getElementById('vigenere-decode');

  vigenereEncodeBtn.addEventListener('click', () => {
    const key = sanitizeInput(vigenereKey.value);
    if (!key) {
      alert('Please enter a valid key (letters only).');
      return;
    }
    const encoded = vigenereEncode(vigenereInput.value, key);
    vigenereOutput.value = encoded;
  });

  vigenereDecodeBtn.addEventListener('click', () => {
    const key = sanitizeInput(vigenereKey.value);
    if (!key) {
      alert('Please enter a valid key (letters only).');
      return;
    }
    const decoded = vigenereDecode(vigenereInput.value, key);
    vigenereOutput.value = decoded;
  });
});
