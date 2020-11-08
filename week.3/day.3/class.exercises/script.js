//Exercise 1

// function banner() {
// 	let div = document.createElement("div")
// 	let h1 = document.createElement("h1")
// 	h1.innerHTML = "The sales end in 10min!"
// 	div.appendChild(h1)
// 	document.body.appendChild(div)
// }

// setTimeout(banner, 5000)

//Exercise 2

let div = document.createElement("div")
let h1 = document.createElement("h1")
div.appendChild(h1)
document.body.appendChild(div)
let number = 10

function banner() {
	h1.innerHTML = "The sales end in " + number -- + " min!"
	if (number < 0) {
		clearInterval(inter)
	}
}

let inter = setInterval(banner, 1000)


