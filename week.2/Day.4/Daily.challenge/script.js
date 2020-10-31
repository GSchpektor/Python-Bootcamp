

function stars() {
	let ask = prompt("give me several words seperated by commas");
	let words = ask.split(",");
	let border = "*".repeat(words.length)
	console.log(border)
	for (var i = 0; i < words.length; i++) {
	console.log("*", words[i], " ".repeat(ask.length - words), "*")	
	}
	console.log(border)
}

stars()