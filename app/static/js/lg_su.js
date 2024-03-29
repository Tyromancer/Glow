$(document).ready(function () {
	login.start();
	signup.start();
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
			var result = JSON.parse(result)
			console.log(result)
			if (result.re){
				window.location.href = result.action
			} else {
				$('form :input').val('');
				$('#form-bot').prepend("<b style='color:white;'>"+result.action+"</b>");
			}
		});
	}
};

signup = {
	signupId: 'signup',
	start: function () {
		$('#'+this.signupId).click(function () {
			if (!signup.verifyPWD()) {
				$("input[type='password']").val('')
			} else {
				var form_data = {
					'usr': $('#usr').val(),
					'pwd': $('#pwd').val()
				};
				signupSubmit.createTask(form_data);
			}
		})
	},
	verifyPWD: function () {
		return $("input[type='password']:eq(0)").val() == $("input[type='password']:eq(1)").val();
	}
}

signupSubmit = {
	createTask: function(data){
		var url = "/signupForm";
		$.post(url, data, function(result){
			var result = JSON.parse(result)
			console.log(result)
			if (result.re){
				window.location.href = result.action
			} else {
				$('form :input').val('');
				$('#form-bot').prepend("<b style='color:white;'>"+result.action+"</b>");
			}
		});
	}
};
