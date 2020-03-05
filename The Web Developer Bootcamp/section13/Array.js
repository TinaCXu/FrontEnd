// function printReverse()
//pre-test the logic
// var array = [1,2,3,4];
// console.log(array["length"]);
//determin the type of length -1 and 0: both number
// console.log(typeof(array["length"]-1));
//print array[length-1],array[length-2],...,array[0]
//var index = length - 1; if var index >= 0, index -= 1
// for(var index = array["length"]-1; index >= 0; index = index - 1){
    // console.log(array[index])   
// }
// Declare the function
function printReverse(array){
    for(var index = array["length"]-1; index >= 0; index = index - 1){
        console.log(array[index])   
    }
};

//function isUniform()

function isUniform(array){
    var index = array["length"]-1;
    while(array[index] === array[index - 1] && index - 1 >= 0){
        index = index - 1
    }
    if(index === 0){
        // return is very important, it could stop the function and 
        return console.log("true")
    }else{
        return console.log("false")
    }
};


//function sumArray
function sumArray(array){
    var sum = 0
    for(var index = array["length"]-1; index >= 0; index = index - 1){
        sum = sum + array[index]   
    }
    if(index === -1){
        return sum
    }
};  