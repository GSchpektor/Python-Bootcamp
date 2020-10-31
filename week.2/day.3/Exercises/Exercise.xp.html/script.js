//Exercise 1

let colors = ["yellow", "red", "blue", "green"]

for (let i = 0; i < colors.length; i++) {
	console.log("My #1 choice is " + colors[i])
}

let suffix = ["st", "nd", "rd", "th"]

for (let i = 0; i < colors.length; i++) {
	if (i == 0){
	console.log("My " + (i+1) + suffix[0] + " choice is " + colors[i])
} else if (i == 1) {
	console.log("My " + (i+1) + suffix[1] + " choice is " + colors[i])
} else if (i == 2){
	console.log("My " + (i+1) + suffix[2] + " choice is " + colors[i])
} else {
	console.log("My " + (i+1) + suffix[3] + " choice is " + colors[i])
}
}



//Exercise 2

// let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
// let order = names.sort()

// for (var i = 0; i < order.length; i++) {
//   console.log(order[i][0]);
// }


//Exercise 3

// let number = prompt("gimme a number mate")
// do {
// 	number = prompt("give me a bigger number matey")
// }
// while (number < 10);
	


// Exercise 4

// let people = ["Greg", "Mary", "Devon", "James"]
// for (let i of people) {
// 	console.log(i)
// }

// let nogreg = people.shift()
// console.log(people)

// let replace = people.splice(2, 1, "Jason")
// console.log(people)

// let add = people.push("Guillaume")
// console.log(people)

// for (let i = 0; i < people.length; i++) {
// 	if (people[i]=== "Mary"){
// 		break;
// 	}
// 	console.log(people[i])
// }

// console.log(people.slice(1, 3))

// let people2 = ["Greg", "Mary", "Devon", "James"]
// console.log(people.indexOf("Mary"))

// console.log(people.indexOf("foo"))

// let last = people2.length -1
// console.log(last)


// Exercise 5

// let ask = prompt("number please")
// let number = parseInt(ask)
// var digits = number.toString().split('');
// var realDigits = digits.map(Number)
// var sum = realDigits.reduce(function(a, b){
//         return a + b;
//     }, 0);
// let divide = sum % 3 == 0
// console.log(divide)


// Exercise 6

// let age = [20,5,12,43,98,55];
// var sum = 0;
// for(i=0; i<age.length; i++){
//    sum += age[i];
// }
// console.log(sum)


 





















