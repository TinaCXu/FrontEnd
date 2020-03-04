//Print all numbers between -10 and 19
//不要忘记while的花括号，以及var的名称一定要一致
for(var i = -10; i <= 19; i += 1){
    console.log(i)
}
//Print all even numbers between 10 and 40
for(var i = 10; i <= 40; i += 2){
    console.log(i)
}
//Print all odd numbers between 300 and 333
for(var i = 301; i <= 333; i +=3){
    console.log(i)
}
//Print all numbers divisible by 5 and 3 between 5 and 50
//cannot && condition in forloops
for(var i = 5; i <= 50; i += 1){
    if(i % 15 === 0)
    console.log(i)
}
