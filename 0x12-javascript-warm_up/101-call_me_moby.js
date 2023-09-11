#!/usr/bin/node
// Define the executeXTimes function
function executeXTimes (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

// Export the executeXTimes function to make it visible from outside
module.exports = executeXTimes;
