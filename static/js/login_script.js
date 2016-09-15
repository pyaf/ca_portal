jQuery(document).ready(function() {

  $.backstretch("/1.jpg");
	// $('.form-password').addClass('input-error');
 $('.login-form input[type="text"], .login-form input[type="password"], .login-form textarea').on('focus', function() {
    	$(this).removeClass('input-error');
    });
    

$(".sign-up-btn").click(function(e){
         e.preventDefault();
         window.location = "file:///C:/Users/ISHANT/Desktop/login2.html";    
});
$('.login-form').on('submit', function(e) {
   var next = true;
            console.log("ancd");
            $(this).find('input[type="text"], input[type="password"], textarea').each(function() {
                if( $(this).val() == "" ) {
                    e.preventDefault();
                    $(this).addClass('input-error');
                    next =false;
                }
                 else
                {
                    $(this).removeClass('input-error');
                };

                console.log("add");
            });


});

});