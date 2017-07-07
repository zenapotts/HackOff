<!DOCTYPE html>
<html>
<link rel="stylesheet" type="text/css" href="display.css" media="screen" />
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
</head> 
<body>
<table></table>
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

	requrl = 'http://docker:4568/service/business_lookup/' + city + '/' + country + '/' + profession;


	console.log(country);
	console.log(city);
	console.log(profession);
	console.log(requrl);

	$.get(
		requrl,
		function(data) {
			console.log(data);
			
			tr = $('<tr/>');
	        tr.append("<td>Business name</td>");
			tr.append("<td>Business Phone</td>");
			tr.append("<td>Business Email</td>");
			tr.append("<td>Profession</td>");
			tr.append("<td>City</td>");
			tr.append("<td>Country</td>");
			$('table').append(tr);
			
			var tr;
	        for (var i = 0; i < data.length; i++) {
	            tr = $('<tr/>');
	            tr.append("<td>" + data[i]['name'] + "</td>");
	            tr.append("<td>" + data[i].bus_phone + "</td>");
	            tr.append("<td>" + data[i].info_email + "</td>");
				tr.append("<td>" + data[i].profession + "</td>");
				tr.append("<td>" + data[i].city + "</td>");
				tr.append("<td>" + data[i].country + "</td>");
	            $('table').append(tr);
	        }
		}
	); 

	// $.ajax({
	// 	url: requrl,
	// });
});
</script>
</body>
</html>