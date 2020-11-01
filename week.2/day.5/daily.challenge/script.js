let starting = parseInt(prompt("starting number"))	

for (let i = 1; starting > i; i++) {
		console.log(starting + " bottles of beer on the wall\n" + starting + " bottles of beer\nTake " + i + " down, pass it arround\n" + (starting - i) + " bottles of beer on the wall");
​
    starting -= i;
​

	}
