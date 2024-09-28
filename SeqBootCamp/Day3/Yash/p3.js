// 1, 4, 7, 12, 23, 42, 77, ...N

let a = 1;
let b = 4;
let c = 7;

let sum = 0;
console.log(a);
console.log(b);
console.log(c);
let n = 200;
while (sum <= n) {
  sum = a + b + c;
  console.log(sum + " ");
  a = b;
  b = c;
  c = sum;
}
