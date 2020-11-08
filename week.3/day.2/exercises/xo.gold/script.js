// Exercise 1

// let opt = document.getElementById("genres")
// console.log(opt)
// let slectopt = opt.options[opt.selectedIndex];
// console.log(slectopt.text)
// console.log(slectopt.value)



// let option = document.createElement("option")
// opt.appendChild(option)
// option.setAttribute("value", "rap")
// option.innerHTML = "Rap"
// slectopt.removeAttribute("selected")
// option.setAttribute("selected", "selected")

// Exercise 2


// let colors = document.getElementById("colorSelect")
// let x = colors.selectedIndex
// let y = colors.options
// let btn = document.querySelector("input")

// console.log(colors)
// console.log(x)
// console.log(y)
// console.log(btn)

// btn.addEventListener("click", function removecolors() {
// 	y[x].remove()
// });

// Exercise 3
	
let shoppingitem = document.createElement("input")
shoppingitem.setAttribute("type", "text")
shoppingitem.setAttribute("placeholder", "item")
document.body.appendChild(shoppingitem)
let amount = document.createElement("input")
amount.setAttribute("type", "text")
amount.setAttribute("placeholder", "amount")
document.body.appendChild(amount)
let btn = document.createElement("input")
btn.setAttribute("type", "button")
btn.setAttribute("value", "add")
document.body.appendChild(btn)
let clear = document.createElement("input")
clear.setAttribute("type", "button")
clear.setAttribute("value", "Clear All")
document.body.appendChild(clear)
let items = document.createElement("input")
items.setAttribute("type", "button")
items.setAttribute("value", "Number of items")
document.body.appendChild(items)
let list = document.createElement("p")
document.body.appendChild(list)

function shopping_list() {
	let shopping = document.getElementById("root")
	shoppingitem = shoppingitem.value
	amount = amount.value
	shopping.innerHTML = shoppingitem + " " + amount
	console.log(shopping)
}

btn.addEventListener("click", shopping_list)





