// $('.col-10').click(function(){
//     alert('this is persoanl_update js')
// })

var user_id = $('form').attr('user_id');
console.log(user_id)

function getPersonalData(){
    console.log("trigger getPersonalData")
    $.get( "personal_profile/update/"+user_id).done(function(data){
        //get personal data in json format. print them out.
        console.log(data);
        console.log(typeof(data));
        // fill the form with existing user profile
        $('form p:eq(0) input').attr('value',data.username)
        $('form p:eq(1) input').attr('value',data.first_name)
        $('form p:eq(2) input').attr('value',data.last_name)
        $('form p:eq(3) input').attr('value',data.email)
        $('form p:eq(4) input').attr('value',data.age)
        $('form p:eq(5) textarea').val(data.introduction)

    });
}

$(document).ready(function(){
    window.setTimeout(getPersonalData, 1000);
})
