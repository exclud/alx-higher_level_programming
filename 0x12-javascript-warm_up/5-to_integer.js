#!/usr/bin/node
// Get the first argument passed to the script
const arg1 = process.argv[2];

// Use parseInt to attempt conversion to an integer
const parsedValue = parseInt(arg1);

// Check if parsedValue is a valid integer
if (!isNaN(parsedValue)) {
  console.log(`My number: ${parsedValue}`);
} else {
  console.log('Not a number');
}
