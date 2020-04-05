// prevent the defaul submit of form, using ajax
// $().ready(function(){
//     $('form').on('submit',function(event){
//         event.preventDefault()
//         alert('prevent success!')
//     })
//     new_post = request.POST.get
// })


// $('form').submit(function(){
//     preventDefault()
//     new_post = request.POST.get
//     $('button').click(function(){
//         $.ajaxSubmit({
//             type: "POST",
//             url: "localhost:8000/global",
//             data: {'new_post':new_post},
//             datatype: "JSON",
//             success: function(data){
//                 alert('success!')},
//             error: function(){
//                 alert('fail!')},
//             clearForm: true,
//             resetFrom: true,
//         })
//     })
// })
