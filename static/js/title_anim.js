jQuery(document).ready(function(){
	jQuery(".titleWrapper").addClass("ready");

jQuery(".titleWrapper h1").each(function(){
	let fullString;
	const characters = jQuery(this).text().split("");

	let $this = jQuery(this);
	$this.empty();
	$.each(characters, function (i, el) {
		if(el === " "){el = "&nbsp;"};
    $this.append("<span>" + el + "</span");
	});

});

});