#!/usr/bin/node
// Define the add function
function add (a, b) {
  return a + b;
}

// Get the first and second arguments passed to the script
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

// Check if both arguments are valid integers
if (!isNaN(arg1) && !isNaN(arg2)) {
  const result = add(arg1, arg2);
  console.log(result);
} else {
  console.log('Invalid input. Please provide two integers.');
}
