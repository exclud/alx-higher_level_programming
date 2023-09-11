#!/usr/bin/node
// Use 'const' for variables that won't be reassigned.
const pi = 3.14159;
const maxAttempts = 5;

// Use 'let' for variables that may be reassigned.
let counter = 0;
let username = 'user123';

// Use 'function' for declaring functions.
function greet(name) {
  return `Hello, ${name}!`;
}

// Use 'arrow functions' for concise function expressions.
const add = (a, b) => a + b;

// Use single quotes for string literals.
const message = 'This is a message';

// Use double slashes for comments.
// This is a comment.

// Use 'camelCase' for variable and function names.
function calculateAreaOfCircle(radius) {
  return pi * radius * radius;
}

// Use 'PascalCase' for class names (if applicable).
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
}

// Use '===', not '==', for equality comparisons.
if (counter === 0) {
  console.log('Counter is zero.');
}

// Use '4 spaces' for indentation.
function exampleFunction() {
    if (true) {
        console.log('Indented with 4 spaces.');
    }
}

// Use 'const' or 'let' for variable declaration; avoid 'var'.
