





/*              function checkform(pform)
{


   next_step = true;
   $(this).find('input[type="text"], input[type="password"], textarea').each(function() {
    console.log("l,sl,s,l");
                if( $(this).val() == "" ) {

                    console.log("klkaklakl");
                    $(this).addClass('input-error');
                      next_step =false;

                }
                else
                {
                    $(this).removeClass('input-error');
                };
                return next_step;
              });
              if(next_step)
              {
                next_step = emailvalidation();
              }
              if(next_step)
              {
                next_step = validatePassword();
              }
              if(next_step)
              {
                next_step = phnvalidation();
              }
              return next_step;
            };
*/

jQuery(document).ready(function() {

   // $('#submit-btn').trigger('click');

    /*
        Fullscreen background
    */
   /* var FillWhatsapp  = function(f){
                                          $('.form-whatsapp').val($('.form-mobile-number').val()) ;


                                                }
    */
    //var password = document.getElementById("password")
      //, confirm_password = document.getElementById("confirm_password");


    //password.onchange= validatePassword;
    //confirm_password.onkeyup= validatePassword;


function phnvalidation()
    {
        var num = $('.form-mobile-number').val();

        console.log(num.length);
        if((num.length!==10) || (isNaN(parseInt(num))) || (parseInt(num).toString().length  != num.length))
           {
           // document.getElementById("form-mobile").setCustomValidity("Invalid Phone no");
            // console.log("here");
            $("#mobile-error").html("Invalid Mobile No");
            return false;
        }
        else
        {
            $("#mobile-error").html("");
            return true;
        }
    }


    function pinvalidation()
    {
        var num = $('.form-pincode').val();

        console.log(num.length);
        if((num.length!==6) || (isNaN(parseInt(num))) || (parseInt(num).toString().length != num.length))
           {
            //document.getElementById("form-mobile").setCustomValidity("Invalid Phone no");
            console.log("here");
            $("#pincode-error").html("Invalid Pin No");
            return false;
        }
        else
        {
            $("#pincode-error").html("");
            return true;
        }
    }


 function wpvalidation()
    {
        var num = $('.form-whatsapp').val();

        console.log(num.length);
        if((num.length!==10) || (isNaN(parseInt(num))) || (parseInt(num).toString().length != num.length))
           {
            // document.getElementById("form-mobile").setCustomValidity("Invalid Phone no");
            console.log("here");
            $("#whatsapp-error").html("Invalid Whatsapp No");
            return false;
        }
        else
        {
            $("#pincode-error").html("");
            return true;
        }
    }




    function emailvalidation()
    {

        var email = $('.form-email').val();
        var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        console.log(email);

        if(re.test(email) == false)
        {
             console.log("here")
             //document.getElementById("laluram").setCustomValidity("Invalid");
             $("#email-error").html("Invalid Email Address");
             return false;
        }
        else
        {
              //   document.getElementById("laluram").setCustomValidity("");
              $("#email-error").html("");
              return true;
        }

    }

function validatePassword(){
        var password = document.getElementById("password");
        confirm_password = document.getElementById("confirm_password");

      if((password.value != confirm_password.value) || (password.value == "") || (confirm_password.value=="")) {
        // $('.form-repeat-password').attr("background-color","red");
        //confirm_password.setCustomValidity("Passwords Don't Match");
        $("#confirm-password-error").html("Password didn't match!");
        return false;
      } else {
        $("#confirm-password-error").html("");
        return true;
      }
    }







    $("input[type=checkbox]").on("click", function()
    {

         if($('#mybox').is(":checked"))
        {$('.form-whatsapp').val($('.form-mobile-number').val()) ;
         }
         else
         {
            $('.form-whatsapp').val('');
         }
    });
    $.backstretch("assets/img/backgrounds/1.jpg");

    $('#top-navbar-1').on('shown.bs.collapse', function(){
        $.backstretch("resize");
    });
    $('#top-navbar-1').on('hidden.bs.collapse', function(){
        $.backstretch("resize");
    });

    /*
        Form
    */
    $('.registration-form fieldset:first-child').fadeIn('slow');

    $('.registration-form input[type="text"], .registration-form input[type="password"], .registration-form textarea').on('focus', function() {
        $(this).removeClass('input-error');
    });

    // next step
    //var k=0;
    $('#btn-next').on('click', function() {
      // k=1;
        var parent_fieldset = $(this).parents('fieldset');
        var next_step = true;

        parent_fieldset.find('input[type="text"], input[type="password"], textarea').each(function() {
            if( $(this).val() == "" ) {
                $(this).addClass('input-error');
                //$(this).setCustomValidity("Field cannot be empty");
                next_step = false;
            }});
              if(next_step){
            next_step = (emailvalidation() && validatePassword());
            console.log("jdjdjdkkdkdkdkdjd");
            console.log(next_step);
            //console.log(next_step, validatePassword(), emailvalidation());
        }

        if( next_step ) {

            parent_fieldset.fadeOut(400, function() {
                $(this).next().fadeIn();
                $($(this).next()).find('input[type="text"], input[type="password"], textarea').each(function()
                {
                $(this).removeClass('input-error');
                });

            });
            //document.getElementById("form-mobile").setCustomValidity("iNPUT A VALID PHN NO");
        }

    });

    // previous step
    $('.registration-form .btn-previous').on('click', function() {
        $(this).parents('fieldset').fadeOut(400, function() {
            $(this).prev().fadeIn();
        });
    });

    // submit



/*    $('submit-btn').on('click',function(){
        var parent_fieldset = $(this).parents('fieldset');
        var next_step = true;
        parent_fieldset.find('input[type="text"], input[type="password"], textarea').each(function() {
            if( $(this).val() == "" ) {
                $(this).addClass('input-error');
                next_step = false;

           }});
           if(next_step)
           {
            next_step = phnvalidation();
           }
           if(next_step){
            return true;
            }
            else
            {

            }
    });
   */

//  $('#form-mobile').on("change paste keyup", function()
//  {

// if($('#mybox').is(":checked"))
//          {$('.form-whatsapp').val($('.form-mobile-number').val()) ;
//      //document.getElementById("form-whatsapp").setCustomValidity("");
//        $("#whatsapp-error").html("");
//           }



//  });



    $('#form-mobile').keyup(function(e){
        var code = (e.keyCode ? e.keyCode : e.which);
        if(code !==13)
        //document.getElementById("form-mobile").setCustomValidity("");
         $("#mobile-error").html("");
    // if($('#mybox').is(":checked"))
    //     {$('.form-whatsapp').val($('.form-mobile-number').val()) ;
    // document.getElementById("form-whatsapp").setCustomValidity("");
    //      }

    });

$('#laluram').keyup(function(e){
    var code = (e.keyCode ? e.keyCode : e.which);
        if(code !==13)
        //document.getElementById("laluram").setCustomValidity("");
        $("#email-error").html("");

    });
$('#confirm_password').keyup(function(e){
    var code = (e.keyCode ? e.keyCode : e.which);
        if(code !==13)
       // document.getElementById("confirm_password").setCustomValidity("");
       $("#confirm-password-error").html("");

    });
$('#form-whatsapp').keyup(function(e){
    var code = (e.keyCode ? e.keyCode : e.which);
        if(code !==13)
        //document.getElementById("form-whatsapp").setCustomValidity("");
        $("#whatsapp-error").html("");

    });
$('#form-pincode').keyup(function(e){
    var code = (e.keyCode ? e.keyCode : e.which);
        if(code !==13)
        //document.getElementById("form-pincode").setCustomValidity("");
        $("#pincode-error").html("");

    });

   // $('#submit-btn').click(
   //  function()
   //  {
   //       if(!phnvalidation())
   //       {
   //          document.getElementById("form-mobile").setCustomValidity("iNPUT A VALID PHN NO");
   //       }

   //  });






       $('.registration-form').on('submit', function(e) {

        // if($('.form-first-name').value.length==0)
        // {
        //     $('#form-first-name').setCustomValidity("Field Cannot be left Empty");
        //     e.preventDefault();
        // }


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

                                                if(next)
                                                {
                                                next = !phnvalidation();
                                                if(next)
                                                {

                                                    //document.getElementById("form-mobile").setCustomValidity("iNPUT A VALID PHN NO");


                                                    e.preventDefault();




                                                console.log(next);

                                               }

                                                next = !wpvalidation();
                                                if(next)
                                                {
                                                    //document.getElementById("form-whatsapp").setCustomValidity("iNPUT A VALID whatsapp NO");


                                                    e.preventDefault();




                                                console.log(next);

                                               }




                                               next = !pinvalidation();

                                                   if(next)
                                                   {
                                                   // document.getElementById("form-pincode").setCustomValidity("iNPUT A VALID Pin NO");
                                                    e.preventDefault();
                                                   }





                                                }


//}
});




});
