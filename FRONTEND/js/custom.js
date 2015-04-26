/* *************************************** */ 
/* Cart Button Drop Down */
/* *************************************** */  

$(document).ready(function() {
	$('.btn-cart-md .cart-link').click(function(e){
		e.preventDefault();
		var $dd_menu = $('.btn-cart-md .cart-dropdown')
		if ($dd_menu.hasClass('open')) {
			$dd_menu.fadeOut();
			$dd_menu.removeClass('open');
		} else {
			$dd_menu.fadeIn();
			$dd_menu.addClass('open');
		}
	});
});

/* *************************************** */ 
/* Tool Tip JS */
/* *************************************** */  

$('.my-tooltip').tooltip();

/* *************************************** */ 
/* Scroll to Top */
/* *************************************** */  
		
$(document).ready(function() {
	$(".totop").hide();
	
	$(window).scroll(function(){
	if ($(this).scrollTop() > 300) {
		$('.totop').fadeIn();
	} else {
		$('.totop').fadeOut();
	}
	});
	$(".totop a").click(function(e) {
		e.preventDefault();
		$("html, body").animate({ scrollTop: 0 }, "slow");
		return false;
	});
		
});
/* *************************************** */

/* *************************************** */
/* Contact form */
/* *************************************** */

$(document).ready(function() {
	$("#submit").click(function() {
		var name = $("#name").val();
		var email = $("#email").val();
		var message = $("#message").val();
		var contact = $("#contact").val();
		$("#returnmessage").empty(); // To empty previous error/success message.
// Checking for blank fields.
		if (name == '' || email == '' || contact == '') {
			alert("Please Fill Required Fields");
		} else {
// Returns successful data submission message when the entered information is stored in database.
			$.post("contact.php", {
				name1: name,
				email1: email,
				message1: message,
				contact1: contact
			}, function(data) {
				$("#returnmessage").append(data); // Append returned message to message paragraph.
				if (data == "Twoje pytanie zosta³o otrzymane. Niebawem skontaktujemy siê z Tob¹.") {
					$("#form")[0].reset(); // To reset form fields on success.
				}
			});
		}
	});
});
/* *************************************** */

/* *************************************** */

/* *************************************** */
/* Tooltips and popOvers */
/* *************************************** */

$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip();
});


$(document).ready(function(){
	$('[data-toggle="popover"]').popover();
});

$(document).ready(function(){
	$(".pop-top").popover({placement : 'top'});
	$(".pop-right").popover({placement : 'right'});
	$(".pop-bottom").popover({placement : 'bottom'});
	$(".pop-left").popover({ placement : 'left'});
});

/* *************************************** */