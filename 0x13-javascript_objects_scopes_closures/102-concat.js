#!/usr/bin/node

const fs = require('fs');

// Get file paths from command-line arguments
const [fileA, fileB, fileC] = process.argv.slice(2);

// Check if all three arguments are provided
if (!fileA || !fileB || !fileC) {
  console.error('Usage: ./102-concat.js <fileA> <fileB> <fileC>');
  process.exit(1);
}

try {
  // Read the contents of fileA and fileB
  const dataA = fs.readFileSync(fileA, 'utf8');
  const dataB = fs.readFileSync(fileB, 'utf8');

  // Write concatenated content to fileC
  fs.writeFileSync(fileC, dataA + dataB, 'utf8');
} catch (err) {
  console.error(`Error: ${err.message}`);
  process.exit(1);
}
