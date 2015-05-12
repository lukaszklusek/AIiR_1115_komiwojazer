/**
 * Created by Wiktor on 2015-04-26.
 */
    //1.1 1.2 1.3 2.1 2.2 2.3 3.1 3.2 3.3


$(document).ready(function(){
    $point = $(".pointer");
    $(".algorithm").hide();
    $point.click(function(){
       $(this).next(".algorithm").slideToggle( "slow", function() {
    // Animation complete.
                                                                });
    });
    $("#next").onclick(function(){
        $(body).html("{% set tryTasks = 2 %}");
    });

});

