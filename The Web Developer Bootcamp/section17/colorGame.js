var numSquares = 6;
var colors= [];
var pickedColor;
var squares = document.querySelectorAll(".square");
var colorDisplay = document.getElementById("colorDisplay");
var messageDisplay = document.querySelector("#message")
var h1 = document.querySelector("h1");
var resetButton = document.querySelector("#reset")
var modeButtons = document.querySelectorAll(".mode")
// var easyBtn = document.querySelector("#easyBtn");
// var hardBtn = document.querySelector("#hardBtn");
// var button = document.querySelectorAll("button")

init();

function init(){
    //mode button event listener
    for(var i = 0; i < modeButtons.length; i++){
        modeButtons[i].addEventListener("click",function(){
            modeButtons[0].classList.remove("selected");
            modeButtons[1].classList.remove("selected");
            this.classList.add("selected");
            // if(this.textContent === "Easy"){
            //     numSquares = 3;
            // }else{
            //     numSquares = 6;
            // };
            this.textContent === "Easy" ? numSquares =3: numSquares =6;
            reset();
        });
    }
    //square event listener
    for(var i = 0; i < squares.length; i++){
        //add click listener to squares
        squares[i].addEventListener("click",function(){
            //grab color of clicked square
            var clickedColor = this.style.background;
            //compare color to pickedColor
            if(clickedColor == pickedColor){
                messageDisplay.textContent = "Correct!";
                changeColors(pickedColor)
                h1.style.backgroundColor = pickedColor
                resetButton.textContent = "Play again?"
            }else{
                this.style.backgroundColor = "#232323";
                messageDisplay.textContent = "Try again";
            }
        });
    };
    //why there should be a reset?
    reset();
}


function reset(){
    //generate all new colors
    colors= generateRandomColors(numSquares);
    //picked a new random color from array
    pickedColor = pickColor();
    //change color display to match the picked color
    colorDisplay.textContent = pickedColor
    //change colors of the squares
    for(var i = 0; i < squares.length; i++){
        if(numSquares == 3){
            if(i < numSquares){
                squares[i].style.background = colors[i];
            } else{
                squares[i].style.display = "none";
            }
        }else{
            squares[i].style.background = colors[i];
            squares[i].style.display = "block";
        }
        squares[i].style.background = colors[i];
    }
    // for(var i = 0; i < squares.length; i++){
    //     if(colors[i]){
    //         squares[i].style.background = "block"; 
    //         squares[i].style.background = colors[i];
    //     }else{
    //         squares[i].style.display = "none";  
    //     }
    // }
    //reset the h1 background
    h1.style.backgroundColor = "steelblue";
    //reset the button textcontent
    resetButton.textContent = "New Colors"
    //reset the message diplay
    messageDisplay.textContent = null;
};

resetButton.addEventListener("click",function() {
    reset();
});

// easyBtn.addEventListener("click",function(){
//     easyBtn.classList.add("selected");
//     hardBtn.classList.remove("selected");
//     numSquares = 3;
//     colors = generateRandomColors(numSquares);
//     pickedColor = pickColor()
//     colorDisplay.textContent = pickedColor
//     for(var i = 0; i < squares.length; i++){
//         if(i < numSquares){
//             squares[i].style.background = colors[i];
//         } else{
//             squares[i].style.display = "none";
//         }
//     }
// });

// hardBtn.addEventListener("click",function(){
//     hardBtn.classList.add("selected");
//     easyBtn.classList.remove("selected");
//     numSquares = 6;
//     colors = generateRandomColors(numSquares);
//     pickedColor = pickColor()
//     colorDisplay.textContent = pickedColor
//     for(var i = 0; i < squares.length; i++){
//         squares[i].style.background = colors[i];
//         squares[i].style.display = "block";
//     }
// });



//Cannot work, cannot keep selected when mouseout
// for(var i = 0; i < button.length; i ++){
    // button[i].addEventListener("mouseover", function(){
        // this.style.color = "white"
        // this.style.background = "steelblue"
    // });
    // button[i].addEventListener("mouseout", function(){
        // this.style.color = "steelblue"
        // this.style.background = "white"
    // });
// };

function changeColors(color){
    //loop through all squares
    for(var i = 0; i < squares.length; i++){
        //change each square color to match given color
        squares[i].style.background = color;
    }
};

function  pickColor(){
    var random = Math.floor(Math.random()*colors.length);
    return colors[random];
};

function generateRandomColors(num){
    //make an array
    var arr = [];
    //add num random colors to arrary
    for (var i = 0; i < num; i++){
        //get random color and push into array
        arr.push(randomColor());
    }
    //return that array
    return arr;
};

function randomColor(){
    //pick a "red" from 0 -255
    var r = Math.floor(Math.random()*256);
    //pick a "green" from 0 -255
    var g = Math.floor(Math.random()*256);
    //pick a "blue" from 0 -255
    var b = Math.floor(Math.random()*256);
    return "rgb(" +  r + ", " + g + ", " + b + ")";
};