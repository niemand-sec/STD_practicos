var allItems = new Array();

function showItems(){
	// clear table body first
	$("#item-table > tbody").empty();
	// fill table with items
	console.log('allItems');

	for(var i=0; i < allItems.length; i++){
		var tr = $("<tr>");
		var trend = $("</tr>");

		var number = $('<td id="number">' + i + '</td>');
		var from = $('<td id="from">' + allItems[i].from + '</td>');
		var to = $('<td id="to">' + allItems[i].to  + '</td>');
		var subject = $('<td id="subject">' + allItems[i].subject + '</td>');
		var timestamp = $('<td id="timestamp">' + allItems[i].timestamp + '</td>');
		var temperatura = $('<td id="temperatura">' + allItems[i].temperatura + '</td>');
		var tension = $('<td id="tension">' + allItems[i].tension + '</td>');
		var corriente = $('<td id="corriente">' + allItems[i].corriente + '</td>');
		var potencia = $('<td id="potencia">' + allItems[i].potencia + '</td>');
		var presion = $('<td id="presion">' + allItems[i].presion + '</td>');


		console.log(presion);
		console.log("ASSSSSSSSSSSSSss");
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
		console.log(tr);
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
	                           			value: value_from,
	                           			writable: true,
	                           			enumerable: true,
	                           			configurable: true
	                           		},
	                           		to: {
	                           			value: value_to,
	                           			writable: true,
	                           			enumerable: true,
	                           			configurable: true
	                           		},
	                           		subject: {
	                           			value: value_subject,
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

	                            console.log(intern_obj.to);
	                            console.log(intern_obj.presion);
	                            console.log(intern_obj.temperatura);
	                            console.log(intern_obj.timestamp);

	                            allItems[i] = intern_obj;
	                            i++;
                    });

                }

            });

            showItems();

});