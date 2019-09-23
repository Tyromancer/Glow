$(document).ready(function () {
	login.start();
});

login = {
	loginId: 'login',
	start: function () {
		$('#'+this.loginId).click(function () {
			var form_data = {
				'usr': $('#usr').val(),
				'pwd': $('#pwd').val(),
				'rmb': $('#rmb').val()
			};
			loginSubmit.createTask(form_data);
		})
	}
}

loginSubmit = {
	createTask: function(data){
		var url = "/loginForm";
		$.post(url, data, function(result){
			console.log(result)
			if (result != 'success'){
				$('form :input').val('');
			} else {
				
			}
		});
	}
};