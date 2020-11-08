let letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for (var i = 0; i < letters.length; i++) {
	let box = document.createElement("div")
	box.style.width = "50px"
	box.style.height = "50px"
	box.style.border = "2px solid black"
	box.innerHTML = letters[i]
	box.setAttribute("class", letters[i])
	box.setAttribute("draggable", true)
	document.body.appendChild(box)

	box.addEventListener("dragstart", function(event){})

	box.addEventListener("dragend", function(event){
		console.log(event)
		let x = event.clientX;
    	let y = event.clientY;
    	event.target.style.position = "absolute";
		event.target.style.left = x + "px";
		event.target.style.top = y + "px";
		
	
	})

	
}

