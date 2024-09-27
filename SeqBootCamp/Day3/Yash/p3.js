// 1, 4, 7, 12, 23, 42, 77, ...N

let a = 1;
let b = 4;
let c = 7;

let sum;
console.log(a);
console.log(b);
console.log(c);
for (let i = 0; i < 20; i++) {
  sum = a + b + c;
  a = b;
  b = c;
  c = sum;
  console.log(sum + " ");
}
