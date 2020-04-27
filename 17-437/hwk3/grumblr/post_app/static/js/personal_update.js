// extract user id
var user_id = $('form').attr('user_id');
console.log('user_id:'+user_id)

//fill the profile form with existing user profile 
function getPersonalData(){
    console.log("trigger fillPersonalData")
    $.get( "personal_profile/update/"+user_id).done(function(data){
        //get personal data in json format. print them out.
        console.log(data);
        // fill the form with existing user profile
        $('form p:eq(0) input').attr('value',data.first_name)
        $('form p:eq(1) input').attr('value',data.last_name)
        $('form p:eq(2) input').attr('value',data.email)
        $('form p:eq(3) input').attr('value',data.age)
        $('form p:eq(4) textarea').val(data.introduction)

    });
}

$(document).ready(function(){
    window.setTimeout(getPersonalData, 1000);
})

// add listener to post action from profile form
var cnt = 0
// $('button').click(function(){
//     alert('click!')
    $('#profile_form').unbind().on('submit',function(event){
    // prevent the default submit of form, using ajax
        cnt += 1;
        console.log(cnt);
        event.preventDefault();
        console.log('prevent success!');

        var first_name_updated = $('#id_first_name').val();
        var last_name_updated = $('#id_last_name').val();
        var email_updated = $('#id_email').val();
        var age_updated = $('#id_age').val();
        var introduction_updated = $('#id_introduction').val();
        console.log(first_name_updated);
        console.log(last_name_updated);
        console.log(email_updated);
        console.log(age_updated);
        console.log(introduction_updated);

        $.ajax({
            type: "POST",
            url: "/personal_profile/update/",
            // the key-'post’ must be the same key in form, otherwise it cannot be saved in database
            data: {'first_name':first_name_updated,
                    'last_name':last_name_updated,
                    'email':email_updated,
                    'age':age_updated,
                    'introduction':introduction_updated,
                },
            datatype: "json",
            success: function(data){
                // this data is the data return by backend
                console.log(data)
                console.log('data submit success!')},
            error: function(data){
                console.log(data)
                console.log('data submit fail!')},
        })
    })
// })
