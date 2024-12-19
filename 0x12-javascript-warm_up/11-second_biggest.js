#!/usr/bin/node

// Retrieve command-line arguments, ignoring the first two (node and script path)
const args = process.argv.slice(2);

// Check if there are fewer than 2 arguments
if (args.length < 2) {
  console.log(0);
} else {
  // Convert arguments to integers and sort in descending order
  const nums = args.map(Number).sort((a, b) => b - a);
  console.log(nums[1]); // Print the second biggest integer
}
