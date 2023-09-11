#!/usr/bin/node
// Define a recursive function to compute factorial
function computeFactorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n <= 1) {
    return 1;
  } else {
    return n * computeFactorial(n - 1);
  }
}

// Get the first argument passed to the script and cast it as an integer
const arg1 = parseInt(process.argv[2]);

// Compute and print the factorial
const factorial = computeFactorial(arg1);
console.log(factorial);
