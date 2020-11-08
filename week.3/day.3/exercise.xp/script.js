// Exercise 1

// let box = document.getElementById("animate")
// let btn = document.querySelector("button")
// let number = 0

// function myMove() {
// 	let move = setInterval(
// 		function () {
// 			box.style.marginTop = number ++ + "px";
// 			box.style.marginLeft = number ++ + "px";
	
// 			if (number == 350) {
// 				clearInterval(move)

// 			}
// 		}, 5)
	
// }





// // Exercise 2

let dragbox = document.createElement("div")
let landbox = document.createElement("div")
dragbox.style.height = "50px"
dragbox.style.width = "50px"
landbox.style.height = "250px"
landbox.style.height = "250px"
dragbox.style.background = "yellow"
landbox.style.background = "red"
dragbox.style.marginBottom = "50px"
dragbox.setAttribute("draggable", true)
dragbox.setAttribute("id", "dragbox")
document.body.appendChild(dragbox)
document.body.appendChild(landbox)

dragbox.addEventListener("dragstart", function(event){
	event.dataTransfer.setData("text", event.target.id)
})

landbox.addEventListener("dragover", function(event){
	event.preventDefault()
})

landbox.addEventListener("drop", function(event){
	let me = event.dataTransfer.getData("text")
	let you = document.getElementById(me)
	landbox.appendChild(you)
})