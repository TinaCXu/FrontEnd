var age = prompt("Please enter your Age!");

if(age < 0){
    alert("error messsage")
}
if(age == 21){
    alert("Happy Birthday!")
}
if(age%2 !== 0){
    alert("Your age is odd!")
}
var root = Math.sqrt(age)
function isInteger(root){
    return Math.floor(root) ===root
}
if(isInteger(root) == true){
    alert("A perfect square!")
}