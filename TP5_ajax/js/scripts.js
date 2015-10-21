$.getJSON( "../test.json", function( data ) {
	var items = [];
	$.each( data, function( key, val ) {
		items.push( "<li id='" + key + "'>" + val + "</li>" );
	});

	$( "<ul/>", {
		"class": "my-new-list",
		html: items.join( "" )
	}).appendTo( "body" );
})
	.done(function() {
		console.log( "success" );
	})
	.fail(function() {
		console.log( "error" );
	})
	.always(function() {
		console.log( "complete" );
});


function showItems(){
	// clear table body first
	$("#item-table > tbody").empty();
	// fill table with items
	console.log('21312312ssssssssssssssss');
	for(var i=0; i < allItems.length; i++){
		var tr = $("<tr>");
		tr.addClass("entry-" + allItems[i].id);

		var name = $("<td>");
		var namep = $("<p>");

		namep.append("<a href='#'>" + allItems[i].filename + "</a>");
		name.append(namep);
		name.addClass("filenames");

		// create td elements for size, type, creation wrt. their current activation status!!
		var id = $("<td>").append($("<p>").html(allItems[i].id)).addClass("id_file");

		var type = $("<td>").append($("<p>").html(allItems[i].mimetype)).addClass("type_col");
		if($(".visited[name='type_toggle']").size() == 0) type.addClass("no-show");
		var creation = $("<td>").append($("<p>").html(niceDateFormat(new Date(allItems[i].creation_date)))).addClass("creation_col");
		if($(".visited[name='creation_toggle']").size() == 0) creation.addClass("no-show");

		// append all td elements
		name.appendTo(tr);
		id.appendTo(tr);
		type.appendTo(tr);
		creation.appendTo(tr);
		// "Actions" menu:
		var menuP = $("<p>");
		// disable preview for text elements
		menuP.append("<i class='fa fa-eye icon-cog-green thumbnail-clic'></i>");

		menuP.append("<i class='fa fa-share icon-cog-green'></i>");
		menuP.append(" | ");
		menuP.append("<i class='fa fa-pencil icon-cog-green'></i>");
		menuP.append("<i class='fa fa-lock icon-cog-green'></i>");
		menuP.append("<i class='fa fa-trash-o icon-cog-green'></i>");
		var tablemenu = $("<td>").append(menuP);
		$(tablemenu).appendTo(tr);
		// add the row
		$("#item-table > tbody").append(tr);
	}
	// change page links
}

