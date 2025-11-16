const fs = require('fs');
const lines = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// 입력값 받기
const N = parseInt(lines[0].trim());
const M = parseInt(lines[1].trim());
const numbers = lines[2].trim().split(' ').map(Number);

// 오름차순 정렬
numbers.sort((a, b) => a - b);

let count = 0;
let left = 0;
let right = N - 1;

while (left < right) {
  const sum = numbers[left] + numbers[right];
  if (sum == M) {
    count++;
    left++;
    right--;
  } else if (sum < M) {
    left++;
  } else {
    right--;
  }
}

console.log(count);
