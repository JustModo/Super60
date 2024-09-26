// Write a program to accept a student’s name and scores in three subject. Display the 1 st, 2nd average and total.
// Display whether the s has secured 1 st , 2nd , pass class or has failed.
// 1 st class is for a score of 60 and above, 2 nd class is for a score of 50 and above, while pass class is for a score of 35 and above.
// If the score is less than 35, then the s fails.

let s = { name: "Rahul", a: 35, b: 35, c: 35 };

let average = (s.a + s.b + s.c) / 3;
let total = s.a + s.b + s.c;

console.log("Average: " + average);
console.log("Total: " + total);

if (s.a < 35 || s.b < 35 || s.c < 35) {
  console.log("Fail");
  return;
}
if (average >= 60) console.log("First Class");
else if (average >= 50) console.log("Second Class");
else console.log("Pass");
