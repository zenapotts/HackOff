<html>
<link rel="stylesheet" type="text/css" href="home.css" media="screen" />
<body>
<pre><input id="small-business-search-field" type="text" class="ui-input country" src="/_themes/freshbooks/smux-assets/img/icons/search.svg" placeholder="Enter Country"> <input id="small-business-search-field" type="text" class="ui-input city" placeholder="Enter City"> <input id="small-business-search-field" type="text" class="ui-input profession" placeholder="Enter Industry"> <a href="#" class="submit" style="text-decoration:none"><button class="button">Search</button></a>
</pre>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<script type="text/javascript">
	$('.submit').click(function () {
		var country = $('.country').val(),
			city = $('.city').val(),
			profession = $('.profession').val();

		window.location.href = 'display.php?city=' + city + '&country=' + country + '&profession=' + profession;
	});
</script>
</body>
</html>
