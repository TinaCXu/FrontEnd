//Print all numbers between -10 and 19
//不要忘记while的花括号，以及var的名称一定要一致
var num1 = -10;
while(num1 <= 19){
    console.log(num1);
    num1 += 1;
}
//Print all even numbers between 10 and 40
var num2 = 10;
while(num2 <= 40){
    console.log(num2);
    num2 += 2;
}
//Print all odd numbers between 300 and 333
var num3 = 301;
while(num3 <= 333){
    console.log(num3);
    num3 +=2;
}
//Print all numbers divisible by 5 and 3 between 5 and 50
var i = 5;
while(i <= 50){
    if(i % 15 === 0){
        console.log(i)
    }
    i +=1
}