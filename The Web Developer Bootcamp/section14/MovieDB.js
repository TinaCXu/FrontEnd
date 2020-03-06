//The Javascript object exercise
var MovieDB = [
    {
        title:"In Bruges",
        rate:"5 stars",
        status:"have watched",
    },
    {
        title:"Frozen",
        rate:"4.5 stars",
        status:"have not seen",
    },
    {
        title:"Mad Max Fury Road",
        rate:"5 stars",
        status:"have seen",
    },
    {
        title:"Les Miserable",
        rate:"3.5 stars",
        status:"have not seen",
    },
]

for(var idx = 0; idx <= MovieDB.length; idx +=1){
    console.log("You " + MovieDB[idx].status + ' "' + MovieDB[idx].title + '" - '+ MovieDB[idx].rate)
} //why does the for loop run successfully, while cannot read property 'status' of undefined?

// //using forEach fuction
var Movies = [
    {
        title:"In Bruges",
        rate:"5 stars",
        status: true,
    },
    {
        title:"Frozen",
        rate:"4.5 stars",
        status: false,
    },
    {
        title:"Mad Max Fury Road",
        rate:"5 stars",
        status: true,
    },
    {
        title:"Les Miserable",
        rate:"3.5 stars",
        status: false,
    },
]

Movies.forEach(function(movie){
    var result = "You have ";
    //be careful! The array in var result should be the argument"movie", not "Movies"! Layer logic!
    if(movie.status == true){
        result += "watched "
    }else {
        result += "have not seen"
    };
    result += "\"" + movie.title + "\" - " + movie.rate;
    console.log(result);
}); // ) includes }

//using funcion to replace var and console.log
function buildString(movie){
    var result = "You have ";
    //be careful! The array in var result should be the argument"movie", not "Movies"! Layer logic!
    if(movie.status == true){
        result += "watched "
    }else {
        result += "have not seen"
    };
    result += "\"" + movie.title + "\" - " + movie.rate;
    return result;

}

Movies.forEach(function(movie){
    console.log(buildString(movie));
});