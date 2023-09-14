#!/usr/bin/node
const dict = require('./101-data.js').dict;

// Initialize an empty dictionary to store occurrences by user id
const occurrencesByUser = {};

// Iterate through the keys (user ids) in the initial dictionary
for (const userId in dict) {
  const occurrence = dict[userId];

  // Check if the user id is already a key in occurrencesByUser
  if (occurrencesByUser[occurrence]) {
    // If it is, push the user id to the existing array
    occurrencesByUser[occurrence].push(userId);
  } else {
    // If it is not, create a new array with the user id as the first element
    occurrencesByUser[occurrence] = [userId];
  }
}

console.log(occurrencesByUser);
