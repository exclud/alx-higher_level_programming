#!/usr/bin/node
const firstArgument = process.argv.slice[2];

// Check to see if the First Argument is undefined
if (firstArgument === undefined) {
  console.log('No argument');
} else {
  console.log(firstArgument);
}
