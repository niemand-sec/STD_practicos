var allItems = new Array();

function showItems(){
	// clear table body first
	$("#item-table > tbody").empty();
	// fill table with items
	//console.log('allItems');

	for(var i=0; i < allItems.length; i++){
		var tr = $("<tr>");
		var trend = $("</tr>");

		var number = $('<td class="number">' + i + '</td>');
		var from = $('<td class="from">' + allItems[i].From.split(": ")[1] + '</td>');
		var to = $('<td class="to">' + allItems[i].To.split(": ")[1] + '</td>');
		var subject = $('<td class="subject">' + allItems[i].Subject.split(": ")[1] + '</td>');
		var timestamp = $('<td class="timestamp">' + allItems[i].trama.timestamp + '</td>');
		var temperatura = $('<td class="temperatura">' + allItems[i].trama.temperatura + '</td>');
		var tension = $('<td class="tension">' + allItems[i].trama.tension + '</td>');
		var corriente = $('<td class="corriente">' + allItems[i].trama.corriente + '</td>');
		var potencia = $('<td class="potencia">' + allItems[i].trama.potencia + '</td>');
		var presion = $('<td class="presion">' + allItems[i].trama.presion + '</td>');


		//console.log(presion);
		//console.log("ASSSSSSSSSSSSSss");
		//$("#item-table > tbody").append(tr).append(number).append(from).append(to).append(subject).append(timestamp).append(temperatura).append(tension).append(corriente).append(potencia).append(presion).append(trend);
		//$("#item-table > tbody").append(tr).append(number).append(from).append(to).append(subject).append(timestamp).append(temperatura).append(tension).append(corriente).append(potencia).append(presion).append(trend);
		number.appendTo(tr);
		from.appendTo(tr);
		to.appendTo(tr);
		subject.appendTo(tr);
		timestamp.appendTo(tr);
		temperatura.appendTo(tr);
		tension.appendTo(tr);
		corriente.appendTo(tr);
		potencia.appendTo(tr);
		presion.appendTo(tr);
		$("#item-table > tbody").append(tr)
		//console.log(tr);
	}
	// change page links
};




function loadDoc(){
	    showItems()
		setInterval("showItems()", 6000);
		console.log("Actualizado");
	}


function loadXml() {

$.getJSON("http://localhost/server-email.php", function( data ){
		console.log("Entro por aca");
		console.log(data);
		console.log(data.mail);
		allItems = data.mail;

		showItems();

		if ($("#filter_from").val().length > 0) filter_from('tbody tr', $("#filter_from").val()) ;
		if ($("#filter_temperatura").val().length > 0) filter_temperatura('tbody tr', $("#filter_temperatura").val());
		if ($("#filter_tension").val().length > 0) filter_tension('tbody tr', $("#filter_tension").val());
		if ($("#filter_corriente").val().length > 0) filter_corriente('tbody tr', $("#filter_corriente").val());
		if ($("#filter_potencia").val().length > 0) filter_potencia('tbody tr', $("#filter_potencia").val());
		if ($("#filter_presion").val().length > 0) filter_presion('tbody tr', $("#filter_presion").val());
	});

}


jQuery(document).ready(function(){

	loadXml();

		setInterval("loadXml()", 6000);








	//default each row to visible
  $('tbody tr').addClass('visible');

  $('#filter_from').keyup(function(event) {
    //if esc is pressed or nothing is entered
    if (event.keyCode == 27 || $(this).val() == '') {
      //if esc is pressed we want to clear the value of search box
      $(this).val('');

      //we want each row to be visible because if nothing
      //is entered then all rows are matched.
      $('tbody tr').removeClass('visible').show().addClass('visible');
    }
    //if there is text, lets filter
    else {
      filter_from('tbody tr', $(this).val());
    }
	});
	$('#filter_temperatura').keyup(function(event) {
    //if esc is pressed or nothing is entered
    if (event.keyCode == 27 || $(this).val() == '') {
      //if esc is pressed we want to clear the value of search box
      $(this).val('');

      //we want each row to be visible because if nothing
      //is entered then all rows are matched.
      $('tbody tr').removeClass('visible').show().addClass('visible');
    }
    //if there is text, lets filter
    else {
      filter_temperatura('tbody tr', $(this).val());
    }
	});
	$('#filter_tension').keyup(function(event) {
    //if esc is pressed or nothing is entered
    if (event.keyCode == 27 || $(this).val() == '') {
      //if esc is pressed we want to clear the value of search box
      $(this).val('');

      //we want each row to be visible because if nothing
      //is entered then all rows are matched.
      $('tbody tr').removeClass('visible').show().addClass('visible');
    }
    //if there is text, lets filter
    else {
      filter_tension('tbody tr', $(this).val());
    }
	});
	$('#filter_corriente').keyup(function(event) {
    //if esc is pressed or nothing is entered
    if (event.keyCode == 27 || $(this).val() == '') {
      //if esc is pressed we want to clear the value of search box
      $(this).val('');

      //we want each row to be visible because if nothing
      //is entered then all rows are matched.
      $('tbody tr').removeClass('visible').show().addClass('visible');
    }
    //if there is text, lets filter
    else {
      filter_corriente('tbody tr', $(this).val());
    }
	});
	$('#filter_potencia').keyup(function(event) {
    //if esc is pressed or nothing is entered
    if (event.keyCode == 27 || $(this).val() == '') {
      //if esc is pressed we want to clear the value of search box
      $(this).val('');

      //we want each row to be visible because if nothing
      //is entered then all rows are matched.
      $('tbody tr').removeClass('visible').show().addClass('visible');
    }
    //if there is text, lets filter
    else {
      filter_potencia('tbody tr', $(this).val());
    }
	});
    $('#filter_presion').keyup(function(event) {
    //if esc is pressed or nothing is entered
    if (event.keyCode == 27 || $(this).val() == '') {
      //if esc is pressed we want to clear the value of search box
      $(this).val('');

      //we want each row to be visible because if nothing
      //is entered then all rows are matched.
      $('tbody tr').removeClass('visible').show().addClass('visible');
    }
    //if there is text, lets filter
    else {
      filter_presion('tbody tr', $(this).val());
    }

});
});


function filter_from(selector, query) {
  query =   $.trim(query);
  query = query.replace(/ /gi, '|');

  $(".from").each(function() {
		if ($(this).text().search(new RegExp(query, "i")) < 0)
		{
			//console.log($(this));
			$(this).parent().hide().removeClass('visible');
		} else {
			//console.log("FALSE");
			$(this).parent().show().addClass('visible');
		}
  });

}



function filter_temperatura(selector, query) {
  query =   $.trim(query);
  query = query.replace(/ /gi, '|');
  sign = query.substring(0,1);
  query = query.replace(sign,'');

  $(".temperatura").each( function(){comparation($(this), query, sign);});

}


function filter_tension(selector, query) {
  query =   $.trim(query);
  query = query.replace(/ /gi, '|');
  sign = query.substring(0,1);
  query = query.replace(sign,'');
  $(".tension").each( function(){comparation($(this), query, sign);});

}


function filter_corriente(selector, query) {
  query =   $.trim(query);
  query = query.replace(/ /gi, '|');
  sign = query.substring(0,1);
  query = query.replace(sign,'');

  $(".corriente").each( function(){comparation($(this), query, sign);});

}


function filter_potencia(selector, query) {
  query =   $.trim(query);
  query = query.replace(/ /gi, '|');
  sign = query.substring(0,1);
  query = query.replace(sign,'');


  $(".potencia").each( function(){comparation($(this), query, sign);});

}



function filter_presion(selector, query) {
  query =   $.trim(query);
  query = query.replace(/ /gi, '|');
  sign = query.substring(0,1);
  query = query.replace(sign,'');

  $(".presion").each( function(){comparation($(this), query, sign);});

}




function comparation(obj, query, sign) {
		switch(sign) {
			case ">":
				if (obj.text() > query)
				{
					obj.parent().show().addClass('visible');
				} else {
					obj.parent().hide().removeClass('visible');
				}
				break;
			case "<":
				if (parseInt(obj.text()) < query)
				{
					obj.parent().show().addClass('visible');
				} else {
					obj.parent().hide().removeClass('visible');
				}
				break;
			case "=":
				if (obj.text() == query)
				{
					obj.parent().show().addClass('visible');
				} else {
					obj.parent().hide().removeClass('visible');
				}
				break;
			default:
				alert("Not valid sign")
				break;
		}

  }