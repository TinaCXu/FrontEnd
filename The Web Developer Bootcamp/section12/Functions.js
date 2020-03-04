// function isEven(num){
//     if(num % 2 == 0){
//         return true;
//     }else{
//         return false;
//     }
// }

function isEven(num){
    return num % 2 === 0;
}
function factorial(num){
    //define a result variable
    var j = 1
    // calculate and store the result
    if(num >= 0){
        for(i = 1; i <= num; i +=1){
            j *= i
        }
        //return the result
        return j
    }
    if(num < 0){
        return "error"
        }
}

function kebabToSnake(str){
    var Newstr= str.replace(/-/g,"_"); 
    return Newstr
}
