#!/usr/bin/node
const args = process.argv.slice(2); // The slice is to exclude the node and the script filename.

if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
