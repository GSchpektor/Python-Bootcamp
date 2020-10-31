let word = ""
let stars = []
let letters = []
let array = []
let guessed = []

function player1(secret) {
	word = prompt("input the word to be guessed");
	letters = word.split("");
	test = letters.slice();
	for (var i = 0; i < letters.length; i++) {
		stars.push(letters[i] = "*");
	}	
	console.log(stars)
}

player1()

function player2() {
		let guess = prompt("guess a letter")
			if (letters.includes(guess) == true) {
				console.log(letters.indexOf(guess));
				array.push(guess);
				console.log(array);
			} else {
				guessed.push(guess);
				console.log(guessed);
			}
}

player2()

