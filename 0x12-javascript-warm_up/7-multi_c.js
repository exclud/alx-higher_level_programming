#!/usr/bin/node
// Get the first argument passed to the script
const arg1 = process.argv[2];

// Use parseInt to attempt conversion to an integer
const x = parseInt(arg1);

// Check if x is a valid integer
if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log("C is fun");
  }
} else {
  console.log("Missing number of occurrences");
}
