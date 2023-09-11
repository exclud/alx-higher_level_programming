#!/usr/bin/node
// Get the first argument passed to the script
const arg1 = process.argv[2];

// Use parseInt to attempt conversion to an integer
const size = parseInt(arg1);

// Check if size is a valid integer
if (!isNaN(size)) {
  // Loop to print each row of the square
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
