

const numbers = [5,12,9,1,7,4,2,6,3,8];
// let str = numbers.toString().split(",")
// let str1 = str.join("")

let ordered = []

for (let i = 0; i < numbers.length; i++) {
	ordered.push(numbers[i]) //5 in temp
		for (let j = 0; j < ordered.length; j++) { 
			if (ordered[j] < numbers[i]) {            // is 5 > 
				numbers.push(ordered[j])
			} 
		}
	}
