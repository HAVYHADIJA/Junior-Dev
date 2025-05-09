console.log("Hello World");
let name = "Havy";//string literal
console.log(name);
let firstName = "Havy";
let lastName = "Nakalyowa";
let age = 23;//number literal
let isStudent = true; //boolean literal
let firstName1 = undefined;
let lastName1 = null;
// reference types
//objects,arrays,functions
//objects
let person = {
    firstName: "Havy",
    lastName: "Nakalyowa",
    age: 23
};
console.log(person);
//accessing object properties
//dot notation
person.firstName = "Havyd";
console.log(person.firstName);
//bracket notation
person["lastName"] = "Naka";
console.log(person["lastName"]);

//arrays
let numbers = [1, 2, 3, 4, 5];
console.log(numbers);
//accessing array elements
console.log(numbers[0]);

//functions
function greet(name) {
    console.log("Hello " + name);
}
greet("Havy");
greet("Nakalyowa");
//function expression
function calculateShippingCost() {
    let totalPrice = 19;
    if (totalPrice <= 10) {
        shippingCost = 5
    } else if (totalPrice <= 30) {
        shippingCost = 3
    } else {
        shippingCost = 0
    }
    return shippingCost

}

//operators
//arithmetic operators
let a = 10;
let b = 5;
let sum = a + b;
let difference = a - b;
let product = a * b;
let quotient = a / b;
let remainder = a % b;

console.log("Sum: " + sum);
console.log("Difference: " + difference);
console.log("Product: " + product);
console.log("Quotient: " + quotient);
console.log("Remainder: " + remainder);
//increment and decrement operators
let x = 10;
x++; //increment
console.log(x); //11
x--; //decrement
console.log(x); //10
//comparison operators
let y = 10;
let z = 5;
console.log(y == z); //false
console.log(y != z); //true
console.log(y > z); //true
console.log(y < z); //false

// Conditional Statements
let totalMarks = 85;
if (totalMarks >= 90) {
    console.log("Grade A");
}
else if (totalMarks >= 80) {
    console.log("Grade B");
}
else (totalMarks <= 70) {
    console.log("Grade C");
}
//logical operators
let isStudent1 = true;
let isEmployed = false;

console.log(isStudent1 && isEmployed); //false //both of them have to be true
console.log(isStudent1 || isEmployed); //true //one of them has to be true









