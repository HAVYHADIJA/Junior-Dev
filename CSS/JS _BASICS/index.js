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

//fumctions
function greet(name) {
    console.log("Hello " + name);
}
greet("Havy");
greet("Nakalyowa");



