#!/usr/bin/node
// Get the arguments passed to the script (starting from the third argument)
const args = process.argv.slice(2);

// Convert the arguments to an array of integers
const integers = args.map(arg => parseInt(arg));

// Filter out NaN values and duplicate integers
const uniqueIntegers = integers.filter((value, index, self) => !isNaN(value) && self.indexOf(value) === index);

// Sort the unique integers in descending order
uniqueIntegers.sort((a, b) => b - a);

// Check if there are at least two unique integers
if (uniqueIntegers.length >= 2) {
  console.log(uniqueIntegers[1]);
} else {
  console.log(0);
}
