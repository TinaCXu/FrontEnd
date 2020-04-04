$('button').click(function(){
    $.ajax({
        type: "POST"
    })
})

function submit(){
    var new_post = $("form").val();
    $.ajax({
        type: "POST",
        url: "localhost:8000/global",
        data: {'new_post':new_post},
        datatype: "jason",
    })
}