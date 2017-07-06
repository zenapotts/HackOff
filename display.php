<!DOCTYPE html>
<html>
<link rel="stylesheet" type="text/css" href="display.css" media="screen" />
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<script>
// $(document).ready(function(){
// 	$.get(
//   		$(this).data('http://docker:4568/service/business_lookup/<city>/<country>/<profession>'),
//   		function (data) {
//     		console.log(data);
//     		app.start();
//   		}
//   	});
// );
function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

$(document).ready(function () {
	var country = getParameterByName('country'),
	city = getParameterByName('city'),
	profession = getParameterByName('profession');
	
	$.get(
		$(this).data('http://docker:4568/service/business_lookup/' + city + '/' + country + '/' + profession),
		function (data) {
			console.log(data);
		}
	);
});
</script>
</head> 
<body>
<a>
</a>
</body>
</html>