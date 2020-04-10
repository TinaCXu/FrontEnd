$('h1').click(function(){
    alert('this is global stream js')
})

// define the global time variable
var latest_post_time = 0

function getUpdatePost() {
    console.log("trigger getUpdatePost")
    // $.ajax({
    //     type: "POST",
    //     url: "/global/",
    //     datatype: "json",
    //     data: {'latest_post_time': latest_post_time},
    //     success: function(data){
    //         console.log('time send success')
    //     },
    //     error: function(){
    //         console.log('time send fail')
    //     },
    // })
    $.get( "/update_post/"+latest_post_time).done(function (data) {
        //3. get posts in json format. print them out.
        console.log("get test pass");
    });
}
$(document).ready(function(){
    window.setInterval(getUpdatePost, 3000);
})
