$(document).ready(function() {


    $("#startup-task-modal").modal("show");
    $("#accordion").addClass('blurring');
    // $("#modal-content").blur();
$("#banner").addClass('blurring');
  $("#notification-panel").addClass('blurring');

   $(".modal-close-btn").on("click",function(){
     $("#accordion").removeClass('blurring');
    // $("#modal-content").blur();
    $("#task-panel").removeClass('blurring');
$("#banner").removeClass('blurring');
 $(".notification-panel").removeClass('blurring');
 $("#settings").removeClass("navbartip");
$("#Logout").removeClass("navbartip");
$("#leaderboard").removeClass("navbartip");  
   });

$("#startup-task-next").on("click",function(){
     $("#startup-task-modal").removeClass('fade');

 $("#startup-task-modal").modal("hide");
$(".notification-panel").removeClass('blurring');
$('#task-panel').addClass('blurring');
$("#accordion").addClass('blurring');
    $("#startup-notifications-modal").modal("show");

});
$("#startup-notifications-next").on("click",function(){
     $("#startup-notifications-modal").removeClass('fade');
$("#startup-notifications-modal").modal("hide");
$(".notification-panel").addClass('blurring');
$('#task-panel').addClass('blurring');
$("#accordion").removeClass('blurring');
$("#settings").addClass("navbartip");
$("#Logout").addClass("navbartip");
$("#leaderboard").removeClass("navbartip");
// $("#Logout").addClass("navbartip");

// $('.tech').addClass("blurring");
// $('.settings').addClass("blurring");
// $('.Logout').addClass("blurring");

console.log("ijidnnidnid");
// $("#leaderboard").addClass("noblur");
$("#startup-leaderboard-modal").modal("show");

});
$("#startup-leaderboard-next").on("click",function(){
$("#startup-leaderboard-modal").modal("hide");
$(".notification-panel").addClass('blurring');
$('#task-panel').addClass('blurring');
$("#accordion").removeClass('blurring');
$("#settings").removeClass("navbartip");
$("#Logout").addClass("navbartip");
$("#leaderboard").addClass("navbartip");
// $('.tech').addClass("blurring");
// $('.settings').addClass("blurring");
// $('.Logout').addClass("blurring");

console.log("ijidnnidnid");
// $("#leaderboard").addClass("noblur");
$("#startup-settings-modal").modal("show");

});
$("#startup-settings-next").on("click",function(){
     $("#accordion").removeClass('blurring');
    // $("#modal-content").blur();
    $("#task-panel").removeClass('blurring');
$("#banner").removeClass('blurring');
 $(".notification-panel").removeClass('blurring');
 $("#settings").removeClass("navbartip");
$("#Logout").removeClass("navbartip");
$("#leaderboard").removeClass("navbartip");  
   
   });


    $('.tasks a').click(function() {
        $('#banner').css('display', 'none');
        var id = $(this).attr('href');
        $('.dial').css('display', 'none');
        $(id).css('display', 'block');
    });

    if( $('#glyddpro')[0].style.width == '100%'){
        $('#glydd').css('display', 'inline-block');
    }
    if( $('#glysbdpro')[0].style.width == '100%'){
        $('#glysbd').css('display', 'inline-block');
    }
    if( $('#glyfbcpro')[0].style.width == '100%'){
        $('#glyfbc').css('display', 'inline-block');
    }
    if( $('#glyfblpro')[0].style.width == '100%'){
        $('#glyfbl').css('display', 'inline-block');
    }


// sojswbjdwhodwdwhoohidwodheo8yeyedbhbjldwhdwuougodbwbo jwbuodugowubgodw

window.onclick = function(event) {
   if(event.target == document.getElementById('startup-task-modal') || event.target == document.getElementById('startup-settings-modal') || event.target == document.getElementById('startup-notifications-modal') || event.target == document.getElementById('startup-leaderboard-modal'))
{
     $("#accordion").removeClass('blurring');
    // $("#modal-content").blur();
    $("#task-panel").removeClass('blurring');
$("#banner").removeClass('blurring');
 $(".notification-panel").removeClass('blurring');
 $("#settings").removeClass("navbartip");
$("#Logout").removeClass("navbartip");
$("#leaderboard").removeClass("navbartip");  

    console.log("jdjdjdj");
}    
}









});