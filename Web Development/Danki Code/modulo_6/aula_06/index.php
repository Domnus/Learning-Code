<?php
	
	$conteudo = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean placerat sapien diam, malesuada mollis orci rhoncus vitae. Etiam volutpat id metus eget congue. Ut posuere massa tincidunt tincidunt scelerisque. Vivamus magna mi, facilisis ut felis in, laoreet tempor justo. Maecenas ultrices molestie turpis eget finibus. Maecenas gravida, odio sed bibendum varius, nisl lorem varius arcu, vitae pretium ligula velit non sem. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sit amet quam lacus. Integer ac semper ligula, eget lobortis magna. Nulla justo nunc, hendrerit ac lacus vitae, feugiat egestas arcu.';

	//Serve para recortar uma string.
	//echo substr($conteudo,0,20);


	$nome = 'Guilherme Cherem Grillo';

	$nomes = explode(' ',$nome);

	//print_r($nomes);

	//Serve para juntar um array com um delimitador.
	//No caso o espaco.

	$nomes = implode(' ',$nomes);

	//echo $nomes;


	//Strip_tags serve para retirar todo codigo HTML.
	$conteudo = '<h1>Guilherme</h1>Outra coisa';

	//echo strip_tags($conteudo);


	//htmlentities que mostra o codigo html na pagina.

	echo htmlentities('<div></div>');


?>