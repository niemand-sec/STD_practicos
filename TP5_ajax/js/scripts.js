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
		var from = $('<td class="from">' + allItems[i].from + '</td>');
		var to = $('<td class="to">' + allItems[i].to  + '</td>');
		var subject = $('<td class="subject">' + allItems[i].subject + '</td>');
		var timestamp = $('<td class="timestamp">' + allItems[i].timestamp + '</td>');
		var temperatura = $('<td class="temperatura">' + allItems[i].temperatura + '</td>');
		var tension = $('<td class="tension">' + allItems[i].tension + '</td>');
		var corriente = $('<td class="corriente">' + allItems[i].corriente + '</td>');
		var potencia = $('<td class="potencia">' + allItems[i].potencia + '</td>');
		var presion = $('<td class="presion">' + allItems[i].presion + '</td>');


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


jQuery(document).ready(function() {

	$.ajax({

                type: "GET",
                url: 'https://raw.githubusercontent.com/BlackSwann/STD_practicos/master/TP3_mail_xml_server/mails.xml',
                dataType: "xml",

                success: function(xml) {
                	var i = 0;
                    $(xml).find("mail").each(function () {
	                        	var value_from = $(this).find('From').text();
	                            var value_to = $(this).find('To').text();
	                            var value_subject = $(this).find('Subject').text();
	                           	var value_timestamp = $(this).find('timestamp').text();
	                           	var value_temperatura = $(this).find('temperatura').text();
	                           	var value_tension = $(this).find('tension').text();
	                           	var value_corriente = $(this).find('corriente').text();
	                           	var value_potencia = $(this).find('potencia').text();
	                           	var value_presion = $(this).find('presion').text();
	                           	var intern_obj = Object.create({}, {

	                           		from: {
	                           			value: value_from.split(": ")[1],
	                           			writable: true,
	                           			enumerable: true,
	                           			configurable: true
	                           		},
	                           		to: {
	                           			value: value_to.split(": ")[1],
	                           			writable: true,
	                           			enumerable: true,
	                           			configurable: true
	                           		},
	                           		subject: {
	                           			value: value_subject.split(": ")[1],
	                           			writable: true,
	                           			enumerable: true,
	                           			configurable: true
	                           		},
	                           		timestamp: {
	                           			value: value_timestamp,
	                           			writable: true,
	                           			enumerable: true,
	                           			configurable: true
	                           		},
	                           		temperatura: {
	                           			value: value_temperatura,
	                           			writable: true,
	                           			enumerable: true,
	                           			configurable: true
	                           		},
	                           		tension: {
	                           			value: value_tension,
	                           			writable: true,
	                           			enumerable: true,
	                           			configurable: true
	                           		},
	                           		corriente: {
	                           			value: value_corriente,
	                           			writable: true,
	                           			enumerable: true,
	                           			configurable: true
	                           		},
	                           		potencia: {
	                           			value: value_potencia,
	                           			writable: true,
	                           			enumerable: true,
	                           			configurable: true
	                           		},
	                           		presion: {
	                           			value: value_presion,
	                           			writable: true,
	                           			enumerable: true,
	                           			configurable: true
	                           		}

	                           	});

	                            //console.log(intern_obj.to);
	                            //console.log(intern_obj.presion);
	                            //console.log(intern_obj.temperatura);
	                            //console.log(intern_obj.timestamp);

	                            allItems[i] = intern_obj;
	                            i++;
                    });
					showItems();
                }

            });

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