#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const fileAPath = process.argv[2];
const fileBPath = process.argv[3];
const fileCPath = process.argv[4];

try {
  const contentA = fs.readFileSync(fileAPath, 'utf-8');
  const contentB = fs.readFileSync(fileBPath, 'utf-8');

  const concatenatedContent = contentA + '\n' + contentB;

  fs.writeFileSync(fileCPath, concatenatedContent);
  console.log(`Content of ${fileAPath} and ${fileBPath} concatenated and saved to ${fileCPath}`);
} catch (error) {
  console.error('Error:', error.message);
  process.exit(1);
}
