$(document).ready(function () {
	login.start();
});

login = {
	loginId: 'login',
	start: function () {
		$('#'+this.loginId).click(function () {
			var form_data = JSON.stringify({
				'usr': $('#usr').val(),
				'pwd': $('#pwd').val(),
				'rmb': $('#rmb').val()
			});
			loginSubmit.createTask(form_data);
		})
	}
}

loginSubmit = {
	createTask: function(data){
		var url = "/loginForm";
		$.post(url, data, function(result){
			console.log(result)
			if (result.code != 'success'){
				console.log("failed to create a new api.")
			} else {
				console.log("succ");
			}
		});
	}
};