#!/usr/bin/node
const dict = require('./101-data.js').dict;

// Initialize an empty dictionary to store user ids by occurrence
const usersByOccurrence = {};

// Iterate through the keys (occurrences) in the initial dictionary
for (const occurrence in dict) {
  const userId = dict[occurrence];

  // Check if the occurrence count is already a key in usersByOccurrence
  if (usersByOccurrence[occurrence]) {
    // If it is, push the user id to the existing array
    usersByOccurrence[occurrence].push(userId);
  } else {
    // If it is not, create a new array with the user id as the first element
    usersByOccurrence[occurrence] = [userId];
  }
}

console.log(usersByOccurrence);
