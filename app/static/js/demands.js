$(document).ready(function () {
	selection.start();
});

selection = {
	data: {'state': 'None'},
	start: function () {
		$('.city').click(function () {
			selection.data['state'] = $(this).attr('state');
			city = $(this).text()
			$.post('/stateCode', selection.data, function(result){
				window.location.href = '../'+result+"/"+city;
			})
		})
	}
}