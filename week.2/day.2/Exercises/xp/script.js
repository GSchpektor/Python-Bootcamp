// // Exercise 1

// let variable1 = 7
// let variable2 = 21

// if (variable1 > variable2){
// 	console.log("this is not the biggest number");
// } else {
// 	console.log(variable2, "is the biggest number");
// }


// Excercise 2

// let newDog = "Chihuahua"
// console.log(newDog.length)
// console.log(newDog.toLowerCase());
// console.log(newDog.toUpperCase());
// if (newDog === "Chihuahua"){
// 	console.log("I love Chihuahua, it's my favorite dog breed")
// } else {
// 	console.log("I don't care, I prefer cats")
// }


//Exercise 3

// let number = prompt("give me a number")

// if (number % 2 == 0){
// 	console.log(number, "is an even number")
// } else {
// 	console.log(number, "is not an even number")
// }


// Exercise 4

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]


if (users.length == 0){
	console.log("no one is online");
} else if (users.length == 1){
	console.log(users [0]);
} else if (users.length == 2) {
	console.log(users[0, 0][0, 1]);
} else {
	console.log(users[0, 0], "and", users[0, 1], "and", users.length-2, "are online")
}