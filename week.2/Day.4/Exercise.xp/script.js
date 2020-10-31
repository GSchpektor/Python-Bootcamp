//Exercise 1


// function checkDriverAge() {
// 	let age = prompt("What is your age?");
// 	if (Number(age) < 18) {
//     alert("Sorry, you are too yound to drive this car. Powering off");
// } else if (Number(age) > 18) {
//     alert("Powering On. Enjoy the ride!");
// } else if (Number(age) === 18) {
//     alert("Congratulations on your first year of driving. Enjoy the ride!");
// }
// }
// checkDriverAge()


// function checkDriverAge(age) {
	
// 	if (Number(age) < 18) {
//     alert("Sorry, you are too yound to drive this car. Powering off");
// } else if (Number(age) > 18) {
//     alert("Powering On. Enjoy the ride!");
// } else if (Number(age) === 18) {
//     alert("Congratulations on your first year of driving. Enjoy the ride!");
// }
// }
// checkDriverAge(92)


//Exercise 2

// function blank() {
// 	let str = prompt(" ")
// 	if (str.length <= 0) {
// 		console.log(true)
// 	} else {
// 		console.log(false)
// 	}
// }

// blank()


//Exercise 3

// function abbrev_name() {
// 	let name = prompt("name")
// 	let array = name.split(" ")
// 	console.log(array[0], array[1].charAt(0))
// }

// abbrev_name()


// Exercise 4


// function cap_name(sentence) {
// 	let array = sentence.split("")
// 	let newarray = []

// 	for (let item of array) {
// 		if (item == item.toUpperCase()) {
// 			newarray.push(item.toLowerCase())
// 		} else {
// 			newarray.push(item.toUpperCase())
// 		}
// 	}
// 	console.log(newarray.join(""))
// }

// cap_name("The Quick Brown Fox")


// Exercise 5


// let amazonBasket = {
//     glasses: 1,
//     books: 2,
//     floss: 100
// }


// function checkBasket() {
// 	let item = prompt("item")
// 		if (item in amazonBasket) {
// 			alert(item + " is in basket")
// 		} else {
// 			alert(item + " is not in basket")
// 		}
// }

// checkBasket()


// Exercise 6

//Exercise 7

// let stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// let prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 

// let shoppingList = ["banana", "orange", "apple"]
// let sum_of_prices = 0


// function myBill() {
// 	for (let i of shoppingList) {
// 		if (stock[i] > 0){
// 			  sum_of_prices += prices[i]
// 			  console.log(stock[i]-1)
// 	}}
// 	return(sum_of_prices)
// }	

// myBill()

// console.log(sum_of_prices)

// Exercise 7 & 10


// gold exercise 2














