/**
 * Created by Wiktor on 2015-05-18.
 */
/**
 * Created by Wiktor on 2015-04-26.
 */
drawSpeed = 200;

$(document).ready(function() {
    initTasks();
    updateProgress();


    $("#next-1").click(function(){
        addTask();
    });
    $(".pointer").click(function(){
       $(this).next(".algorithm").slideToggle( "slow");
    });
    setInterval("updateProgress()", 1000);


    canvas(false);
    canvasDone(false);

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
                    <div id=\"date-1-"+ i+"\">\
                    <h3>Wybierz punkty z pliku tekstowego</h3>\
                    </div>\
                    <form id=\"choose1-"+ i +"\" action=\"tsp/add_task\" method=\"post\" enctype=\"multipart/form-data\">\
                    <h5>Wybierz plik tekstowy</h5>\
                    <p><input type=\"file\" name=\"fileToUpload\" id=\"fileToUpload1-"+ i +"\"></p>\
                    <p><input type=\"submit\" class=\"start\" value=\"Rozpocznij algorytm\" id=\"submit1-"+i+"\" name=\"submit1-"+i+"\"></p>\
                    </form>\
                    </div>\
                    <div class=\"row col-md-6\">\
                    <h3>Zadanie "+i+"</h3>\
                    <ul>\
                    <li id=\"path-1-"+ i+"\">Najkrótsza droga : Rozpocznij algorytm.</li>\
                    <button id=\"show-done-points-1-"+ i+"\" data-toggle=\"modal\" data-target=\"#output1-"+ i+"\">Pokaż rozwiązanie</button> \
                    <button id=\"show-points-1-"+ i+"\" data-toggle=\"modal\" data-target=\"#input1-"+ i+"\">Pokaż zaadane punkty</button> \
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
        <div id=\"date-1-"+ i+"\">\
        <h3>Wybierz punkty z pliku tekstowego</h3>\
        </div>\
        <form id=\"choose1-"+ i +"\" action=\"tsp/add_task\" method=\"post\" enctype=\"multipart/form-data\">\
        <h5>Wybierz plik tekstowy</h5>\
        <p><input type=\"file\" name=\"fileToUpload\" id=\"fileToUpload1-"+ i +"\"></p>\
        <p><input type=\"submit\" value=\"Rozpocznij algorytm\" id=\"submit1-"+i+"\" name=\"submit1-"+i+"\"></p>\
        </form>\
        </div>\
        <div class=\"row col-md-6\">\
        <h3>Zadanie "+i+"</h3>\
        <ul>\
        <li id=\"path-1-"+ i+"\">Najkrótsza droga : Rozpocznij algorytm.</li>\
        <button id=\"show-done-points-1-"+ i+"\" data-toggle=\"modal\" data-target=\"#output1-"+ i+"\">Pokaż rozwiązanie</button> \
        <button id=\"show-points-1-"+ i+"\" data-toggle=\"modal\" data-target=\"#input1-"+ i+"\">Pokaż zaadane punkty</button> \
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
    function startEvent(i){
        $("#choose1-"+i+"").remove();
        $("#date-1-"+i+"").html("<h3>Pracuje...</h3>");
    }

     $.getJSON($SCRIPT_ROOT + '/_update_progress', {
      }, function(data) {
        var prog = data['value'];
        var best = data['best'];
        var startTime = data['startTime'];
        var endTime = data['endTime'];
        var i=1;
        for (var val in prog) {
            var itemData = prog[val];
                  $("#ProgressBar1-"+i+"").css('width',''+itemData+'%').attr('aria-valuenow', itemData);
                  if (parseInt(itemData) > 0 && parseInt(itemData) < 100){
                      $("#path-1-"+i+"").html("Najkrótsza droga : Czekam...");
                      startEvent(i);
                  }else if(parseInt(itemData) == 100){
                      $("#choose1-"+i+"").remove();
                      $("#path-1-"+i+"").html("Najkrótsza droga : "+ best[val] +"");
                      $("#date-1-"+i+"").html("<h3>Zadanie zakończone</h3>Data rozpoczęcia : "+ startTime[val] +"<br> Data zakończenia : "+ endTime[val] +"");

                  }
                  i++;
        }


        //  $.each(prog, function() {
        //      $.each(this, function(index, itemData) {
        //          $("#ProgressBar1-"+i+"").css('width',''+itemData+'%').attr('aria-valuenow', itemData);
        //          if (parseInt(itemData) > 0 && parseInt(itemData) < 100){
        //              $("#path-1-"+i+"").html("Najkrótsza droga : Czekam...");
        //              startEvent(i);
        //          }else if(parseInt(itemData) == 100){
        //              $("#path-1-"+i+"").html("Najkrótsza droga : Done");
        //              startEvent(i);
        //          }
        //          i++;
        //      });
        //});
      });


}




function canvas(connect,drawId){


            $.getJSON($SCRIPT_ROOT + '/_active_task', {
      }, function(data) {
                $.getJSON($SCRIPT_ROOT + '/_user_task_points', {
          }, function(data2) {
            var activeTasks = data.result;
            drawPoints(activeTasks)
            var j = 1;
          $.each(data2, function() {
              $.each(this, function(index, itemData) {
                  if (connect == true){
                      id = drawId.substr(drawId.length-1,drawId.length);
                      if (id == index){
                          connectPointsToCanvas(id, index, itemData)
                      }
                  }else if (connect == false) {
                    drawPointsToCanvas(j,index,itemData);
                    j++;
                  }
              });
        });
        });
    });

    function drawPointsToCanvas(j, index, itemData){
                          var canvas = document.getElementById("canvas1-"+ j +"");
                  var ctx = canvas.getContext("2d");
                for (i = 0 ; i < itemData.length - 1 ; i++){
                    //x = i y = i+1
                    var x = 0
                    if (i%2 == 0) x = i;
                    ctx.fillRect(itemData[x],itemData[x+1],5,5);
                }
    }

    function connectPointsToCanvas(j, index, itemData){
                          var canvas = document.getElementById("canvas1-"+ j +"");
                  var ctx = canvas.getContext("2d");
                    ctx.strokeStyle = '#ff0000';
                    line(ctx,itemData,0);
        function line(ctx,itemData,i){
            setTimeout(function () {
               if (i%2 == 0) x = i;
                console.log(itemData[x] + " " + itemData[x+1]);
                ctx.moveTo(itemData[x],itemData[x+1]);
                ctx.lineTo(itemData[x+2],itemData[x+3]);
                ctx.stroke();
              i++;
                if (i == itemData.length - 2) {
                    ctx.moveTo(itemData[i],itemData[i+1]);
                    ctx.lineTo(itemData[0],itemData[1]);
                    ctx.stroke();
              }
              if (i < itemData.length -2) {
                 line(ctx,itemData,i);
              }
           }, drawSpeed)
        }
    }

}

function canvasDone(connect,drawId){


            $.getJSON($SCRIPT_ROOT + '/_done_task', {
      }, function(data) {
                $.getJSON($SCRIPT_ROOT + '/_user_done_task_points', {
          }, function(data2) {
            var activeTasks = data.result;
            drawPoints(activeTasks)
          $.each(data2, function() {
              $.each(this, function(index, itemData) {
                  if (connect == true){
                      id = drawId.substr(drawId.length-1,drawId.length);
                      if (id == itemData[0]){
                          connectDonePointsToCanvas(itemData)
                      }
                  }else if (connect == false) {
                    drawDonePointsToCanvas(itemData);
                  }
              });
        });
        });
    });

    function drawDonePointsToCanvas(itemData){

        var canvas = document.getElementById("canvas2-"+ itemData[0] +"");
        var ctx = canvas.getContext("2d");
        for (i = 2 ; i < itemData.length - 1 ; i++){
            console.log(canvas);
            //x = i y = i+1
            var x = 2
            if (i%2 == 0) x = i;
            ctx.fillRect(itemData[x],itemData[x+1],5,5);
        }
    }

    function connectDonePointsToCanvas(itemData){
        var canvas = document.getElementById("canvas2-"+ itemData[0] +"");
        var ctx = canvas.getContext("2d");
        ctx.strokeStyle = '#ff0000';
        line(ctx,itemData,2);
        function line(ctx,itemData,i){
            setTimeout(function () {
               if (i%2 == 0) x = i;
                console.log(itemData[x] + " " + itemData[x+1]);
                ctx.moveTo(itemData[x],itemData[x+1]);
                ctx.lineTo(itemData[x+2],itemData[x+3]);
                ctx.stroke();
              i++;
                if (i == itemData.length - 2) {
                    ctx.moveTo(itemData[i],itemData[i+1]);
                    ctx.lineTo(itemData[2],itemData[3]);
                    ctx.stroke();
              }
              if (i < itemData.length -2) {
                 line(ctx,itemData,i);
              }
           }, 200)
        }
    }

}

function drawPoints(taskCount){

    for (var i = 1 ; i<= taskCount; i++){
        $('.modals:last').append("\
        <div class=\"modal fade\" id=\"input1-"+ i +"\" tabindex=\"-1\" role=\"dialog\" aria-labelledby=\"myModalLabel\" aria-hidden=\"true\">\
        <div class=\"modal-dialog\">\
        <div class=\"modal-content\">\
        <div class=\"modal-header\">\
        <button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>\
        <h4 class=\"modal-title\" id=\"myModalLabel\">Twoje punkty wejściowe</h4>\
        </div>\
        <div class=\"modal-body\">\
        <canvas class=\"myCanvas\" id=\"canvas1-"+ i +"\" width=\"300\" height=\"300\">\
        </canvas>\
        </div>\
        <div class=\"modal-footer\">\
        <button type=\"button\" id =\"draw1-"+ i + "\" onclick=\"openInitPoints(this.id)\" class=\"btn btn-primary pull-left draw\">Rysuj ściezkę</button>\
        <button type=\"button\" class=\"btn btn-default pull-left\" onclick=\"faster()\" >Szybciej</button>\
        <button type=\"button\" class=\"btn btn-default pull-left\" onclick=\"slower()\" >Wolniej</button>\
        <button type=\"button\" class=\"btn btn-default\" data-dismiss=\"modal\">Zamknij</button>\
        </div>\
        </div>\
        </div>\
        </div>\
        <div class=\"modal fade\" id=\"output1-"+ i +"\" tabindex=\"-1\" role=\"dialog\" aria-labelledby=\"myModalLabel\" aria-hidden=\"true\">\
        <div class=\"modal-dialog\">\
        <div class=\"modal-content\">\
        <div class=\"modal-header\">\
        <button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>\
        <h4 class=\"modal-title\" id=\"myModalLabel\">Twoje rozwiazanie</h4>\
        </div>\
        <div class=\"modal-body\">\
        <canvas class=\"myCanvas\" id=\"canvas2-"+ i +"\" width=\"300\" height=\"300\">\
        </canvas>\
        </div>\
        <div class=\"modal-footer\">\
        <button type=\"button\" id =\"draw1-"+ i + "\" onclick=\"openDonePoints(this.id)\" class=\"btn btn-primary pull-left draw\">Rysuj ściezkę</button>\
        <button type=\"button\" class=\"btn btn-default pull-left\" onclick=\"faster()\" >Szybciej</button>\
        <button type=\"button\" class=\"btn btn-default pull-left\" onclick=\"slower()\" >Wolniej</button>\
        <button type=\"button\" class=\"btn btn-default\" data-dismiss=\"modal\">Zamknij</button>\
        </div>\
        </div>\
        </div>\
        </div>\
        ");
    }

}

function faster(){
    if ((drawSpeed - 10 ) > 0 ){
        drawSpeed -= 10;
    }else{
        if ((drawSpeed - 1 ) > 0 ){
            drawSpeed -= 1;
        }
    }
}

function slower(){
        drawSpeed += 10;
}

function openInitPoints(id){
    canvas(true,id);
}

function openDonePoints(id){
    canvasDone(true,id);
}
