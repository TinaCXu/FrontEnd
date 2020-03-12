var button = document.querySelector("button");
var isPurple = false;//set flag
button.addEventListener("click",function() {
    //if white
        //make it purple
    //else
        //make it white
    if(isPurple){ //equals to isPurple = true
        document.body.style.background = "white";
        //isPurple = false; (replaced by isPurple = !isPurple)    
    } else{
        document.body.style.background = "purple";
        //isPurple = true; (replaced by isPurple = !isPurple)
    }
    isPurple = !isPurple;
});

//toggle the css class:
button.addEventListener("click",function() {
    document.body.classList.toggle("purple");
});