// insert CSRF token into ajax
$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
 
    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});


$().ready(function(){
    $('button').click(function(){
        $('#prevented').on('submit',function(event){
            // prevent the defaul submit of form, using ajax
            event.preventDefault();
            alert('prevent success!');
            var new_post = $('#id_post').val();
            console.log(new_post);
            $.ajax({
                type: "POST",
                url: "/global/",
                // the key-'post’ must be the same key in form, otherwise it cannot be saved in database
                data: {'post':new_post},
                datatype: "json",
                success: function(data){
                    alert('success!')},
                error: function(){
                    alert('fail!')},
                clearForm: true,
                resetFrom: true,
            })
        })
    })
})




