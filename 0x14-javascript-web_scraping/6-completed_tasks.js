#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node countCompletedTasks.js <API URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
    return;
  }

  const tasks = JSON.parse(body);
  const completedTasksByUser = {};

  for (const task of tasks) {
    if (task.completed) {
      if (!completedTasksByUser[task.userId]) {
        completedTasksByUser[task.userId] = 0;
      }
      completedTasksByUser[task.userId]++;
    }
  }

  for (const userId in completedTasksByUser) {
    console.log(`User ${userId}: ${completedTasksByUser[userId]} completed tasks`);
  }
});
