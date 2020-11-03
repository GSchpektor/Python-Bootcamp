let solar = document.querySelector("body")

let planets = ["Earth", "Jupiter", "Neptune", "Mars", "Venus", "Saturn", "Mercury", "Uranus"]


let div = document.createElement("div")
console.log(div)



for (var i = 0; i < planets.length; i++) {
	var newdiv = document.createElement("div") // creating a div
	newdiv.innerHTML = planets[i]  // each planet will have a div
	div.appendChild(newdiv)  // putting the new div inside parent div
	newdiv.setAttribute("class", "planet")  // setting a class to each div
	if (newdiv.innerText == "Earth") {
	newdiv.style.backgroundColor = "blue"
} else if (newdiv.innerText == "Jupiter") {
	newdiv.style.backgroundColor = "orange"
} else if (newdiv.innerText == "Neptune") {
	newdiv.style.backgroundColor = "pink"
} else if (newdiv.innerText == "Mars") {
	newdiv.style.backgroundColor = "purple"
} else if (newdiv.innerText == "Venus") {
	newdiv.style.backgroundColor = "green"
} else if (newdiv.innerText == "Saturn") {
	newdiv.style.backgroundColor = "yellow"
} else if (newdiv.innerText == "Mercury") {
	newdiv.style.backgroundColor = "red"
} else if (newdiv.innerText == "Uranus") {
	newdiv.style.backgroundColor = "grey"
} 

}

solar.appendChild(div)

