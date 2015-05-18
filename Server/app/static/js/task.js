/**
 * Created by Wiktor on 2015-05-18.
 */
/**
 * Created by Wiktor on 2015-04-26.
 */


$(document).ready(function() {
    initTasks();
    $("#next-1").click(function(){
        addTask();
    });

    setInterval("updateProgress()", 1000);
});


function addTask(){
        $.getJSON($SCRIPT_ROOT + '/_add_active_task', {
     }, function(data) {
            var active = data.result;
            if (active != 500){
                               active ++;
                var i = active;
                $("#active-tasks").html(active);

                $('#algorithm1:last').append("\
                    <div class=\"algorithm-in\">\
                    <div class=\"row col-md-6\">\
                    <h3>Wybierz punkty z pliku tekstowego</h3>\
                    <form action=\"tsp/add_task\" method=\"post\" enctype=\"multipart/form-data\">\
                    <h5>Wybierz plik tekstowy</h5>\
                    <p><input type=\"file\" name=\"fileToUpload\" id=\"fileToUpload1-"+ i +"\"></p>\
                    <p><input type=\"submit\" value=\"Rozpocznij algorytm\" name=\"submit1-"+i+"\"></p>\
                    </form>\
                    </div>\
                    <div class=\"row col-md-6\">\
                    <h3>Zadanie "+i+"</h3>\
                    <ul>\
                    <li>Najkrótsza droga : Czekam...</li>\
                    <li>Zobacz najkrótszą drogę: Czekam...</li>\
                    </ul>\
                    <h4>Pasek postępu</h4>\
                    <div class=\"progress\">\
                    <div class=\"progress-bar\" id=\"ProgressBar1-" +i+ "\" role=\"progressbar\" aria-valuenow=\"0\"\
                    aria-valuemin=\"0\" aria-valuemax=\"100\" style=\"width:0%\">\
                    </div>\
                    </div>\
                    </div>\
                    </div>\
                    </div>\
                    ");

            }else{
                alert("Przed dodaniem zadania musisz rozpoczac poprzednie!");
            }
          });
}

function initTasks(){
    $.getJSON($SCRIPT_ROOT + '/_active_task', {
     }, function(data) {
        var active = data.result;
            $("#active-tasks").html(active);
        for (var i = 1 ; i<= active; i++){
                    $('#algorithm1:last').append("\
        <div class=\"algorithm-in\">\
        <div class=\"row col-md-6\">\
        <h3>Wybierz punkty z pliku tekstowego</h3>\
        <form action=\"tsp/add_task\" method=\"post\" enctype=\"multipart/form-data\">\
        <h5>Wybierz plik tekstowy</h5>\
        <p><input type=\"file\" name=\"fileToUpload\" id=\"fileToUpload1-"+ i +"\"></p>\
        <p><input type=\"submit\" value=\"Rozpocznij algorytm\" name=\"submit1-"+i+"\"></p>\
        </form>\
        </div>\
        <div class=\"row col-md-6\">\
        <h3>Zadanie "+i+"</h3>\
        <ul>\
        <li>Najkrótsza droga : Czekam...</li>\
        <li>Zobacz najkrótszą drogę: Czekam...</li>\
        </ul>\
        <h4>Pasek postępu</h4>\
        <div class=\"progress\">\
        <div class=\"progress-bar\" id=\"ProgressBar1-" +i+ "\" role=\"progressbar\" aria-valuenow=\"0\"\
        aria-valuemin=\"0\" aria-valuemax=\"100\" style=\"width:0%\">\
        </div>\
        </div>\
        </div>\
        </div>\
        </div>\
        ");
        }
        if (active == 0) {
            $(".algorithm").hide();
        }
      });
    $.getJSON($SCRIPT_ROOT + '/_working_task', {
     }, function(data) {
            $("#working-tasks").html(data.result);
      });
}

function updateProgress(){


     $.getJSON($SCRIPT_ROOT + '/_update_progress', {
      }, function(data) {
         var i=1;
          $.each(data, function() {
              $.each(this, function(index, itemData) {
                  $("#ProgressBar1-"+i+"").css('width',''+itemData+'%').attr('aria-valuenow', itemData);

        //       <div class=\"progress-bar\" id=\"ProgressBar1-" +i+ "\" role=\"progressbar\" aria-valuenow=\"0\"\
        //aria-valuemin=\"0\" aria-valuemax=\"100\" style=\"width:0%\">\
        //          alert(i);
                  i++;
              });
        });
      });


}

$(document).ready(function(){



    $point = $(".pointer");
        $point.click(function(){
       $(this).next(".algorithm").slideToggle( "slow", function() {
    // Animation complete.
                                                                });
    });

});

