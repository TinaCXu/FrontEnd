var cnt = 0;
   $('button').click(function(){
        $('#prevented').unbind().on('submit',function(event){
            // prevent the defaul submit of form, using ajax
            cnt += 1;
            console.log(cnt);
            event.preventDefault();
            console.log('prevent success!');
            var new_post = $('#id_post').val();
            console.log(new_post);
            $.ajax({
                type: "POST",
                url: "/global/",
                // the key-'post’ must be the same key in form, otherwise it cannot be saved in database
                data: {'post':new_post},
                datatype: "json",
                success: function(data){
                    console.log('success!')},
                error: function(){
                    console.log('fail!')},
            })
        })
   })

// define the global time variable
var latest_post_time = "1970-01-01 00:00:00"
var target_user = $('#target_user').val()
console.log(target_user)

function getUpdatePost() {
    console.log("trigger getUpdatePost")
    $.get( "/update_personal/"+target_user+latest_post_time).done(function (data) {
        //3. get posts in json format. print them out.
        //https://stackoverflow.com/questions/42570854/how-to-output-json-array-value-in-ajax-success
        console.log(data);
        console.log(typeof(data));
        // data is already a jsonObject
        console.log("get test pass");
        latest_post_time = data.timestamp;
        latest_post = data.posts;
        console.log(latest_post_time)
        console.log(latest_post)
        console.log(latest_post[0].user_id)
        

        var post_html = "";
        for (var i = 0; i<latest_post.length; i++){
            var new_post = latest_post[i];
            post_html +=
                '<li class="list-group-item">'+ new_post["post"]
                    +'<p class="card-text text-right"><small class="text-muted">'+new_post["timestamp"]}+'</small></p>'
                +'</li>'
        console.log(post_html)
        $("#postPool").prepend(post_html);
    });
}

$(document).ready(function(){
    window.setInterval(getUpdatePost, 3000);
})
