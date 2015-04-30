
$( function() {
  var bar = $('#ProgressBar1-1');
  var val = null;

  i1 = setInterval(function() {
    val = parseInt(bar.attr('aria-valuenow'));
    val += 10;
    console.log(val);
    if( val <= 100) {
      bar.attr('aria-valuenow', val);
      bar.css('width', val + '%');
    } else {
        val = 0;
        bar.attr('aria-valuenow', val);
        bar.css('width', val + '%');
    }
  }, 100);

});


$( function() {
  var bar = $('#getProgressBar');
  var val = null;

  i1 = setInterval(function() {
    val = parseInt(bar.attr('aria-valuenow'));
    val += 1;
    console.log(val);
    if( val <= 100) {
      bar.attr('aria-valuenow', val);
      bar.css('width', val + '%');
    } else {
        val = 0;
        bar.attr('aria-valuenow', val);
        bar.css('width', val + '%');
    }
  }, 100);

});


$( function() {
  var bar = $('#checkProgressBar');
  var val = null;

  i1 = setInterval(function() {
    val = parseInt(bar.attr('aria-valuenow'));
    val += 1;
    console.log(val);
    if( val <= 100) {
      bar.attr('aria-valuenow', val);
      bar.css('width', val + '%');
    } else {
        val = 0;
        bar.attr('aria-valuenow', val);
        bar.css('width', val + '%');
    }
  }, 100);

});