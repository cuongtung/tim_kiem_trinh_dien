$(document).ready(function(){
	$('body').on('click','.text', function(){
	    $('.modal').modal('show')
	    var ct = $(this).prev().text()
	    $('.modal-ct').text(ct)
	})
})