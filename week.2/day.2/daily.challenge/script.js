let sentence = "you're not too bad looking"
let array = sentence.split(" ")
let first = array.indexOf("not")
let second = array.indexOf("bad") 

let difference = second - first
if (second > first){
	array.splice(first, difference+1, "good")
	console.log(array.join(" "))
} else {
	console.log(sentence)
}

