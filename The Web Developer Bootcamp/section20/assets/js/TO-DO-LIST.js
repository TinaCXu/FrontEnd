// check off specific to do by clicking
$("li").click(function(){
    $(this).toggleClass("completed");
});
//delet to do when clicking span
$("span").click(function(){
    $(this).parent().fadeOut(500,function(){
        $(this).remove();
    });
    //stop triggering event on parent layer
    event.stopPropagation();
});
//add new input
$("input").keypress(function(event){
    if(event.which === 13){
        //capture the input value
        var innerHTML = $("input").val();
        //add new li and input
        $("ul").append(
            "<li></li>"
        );
        $("li:last").append(
            "<span>X</span>" + innerHTML
        );
        //add listener to new li
        $("li:last").click(function(){
            $(this).toggleClass("completed");
        });
        $("span:last").click(function(){
            $(this).parent().fadeOut(500,function(){
                $(this).remove();
            });
            event.stopPropagation(); //cannot work
        });
        //clear up input bar
        $("input").val("");

    }
});

