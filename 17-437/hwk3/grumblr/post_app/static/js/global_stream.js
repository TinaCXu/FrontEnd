$('h1').click(function(){
    alert('this is global stream js')
})

// define the global time variable
var latest_post_time = "1970-01-01 00:00:00"

function getUpdatePost() {
    console.log("trigger getUpdatePost")
    // $.ajax({
    //     type: "POST",
    //     url: "/update_post/"+latest_post_time,
    //     datatype: "json",
    // })
    $.get( "/update_post/"+latest_post_time).done(function (data) {
        //3. get posts in json format. print them out.
        //https://stackoverflow.com/questions/42570854/how-to-output-json-array-value-in-ajax-success
        console.log(data);
        console.log("get test pass");
        var html = "";
        for (var i =0; i<length(data); i++){
            var new_post = data[i];
            html +=
            //     <li class="list-group-item">
            //     <div class="card w-90"> 
            //         <div class="card-body">
            //             <a href=#>
            //                 <h5 class="card-title">{{ posts.user }}</h5>
            //             </a>
            //             <div class="container">
            //                 <div class="row">
            //                     <div class="col-2">
            //                         <a href="#">
            //                             <img src="C:\Users\xucha\Documents\前端网课\17-437\hwk1\素材\user3.jpg" width="col-3" height="col-3" class="card-img-top" alt="User2">
            //                         </a>
            //                     </div>
            //                     <div class="col-10">
            //                         {{ posts.post }}
            //                     </div>
            //                 </div>
            //             </div>
            //             <p class="card-text text-right"><small class="text-muted" id="postTime">{{ posts.post_time|date:"Y-m-d H:i:s" }}</small></p>
            //         </div>
            //     </div>
            // </li>

        }
        latest_post_time = data.timestamp

    });
}

function insertUpdatePost(){

}

$(document).ready(function(){
    window.setInterval(getUpdatePost, 3000);
})
