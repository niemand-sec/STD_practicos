<?php 
	$xml = simplexml_load_file("mails.xml");
	$xml_json = json_encode($xml);
	echo $xml_json;
	return json_encode($xml);
?>