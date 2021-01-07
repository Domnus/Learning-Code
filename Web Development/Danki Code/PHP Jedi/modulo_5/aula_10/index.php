<?php
	$valor = 10;
	$valor2 = '10';


	//Um sinal de igual quer dizer que estamos atribuindo um valor.
	//Sempre retorna verdadeiro.
	/*
	if($nome = $nome2){
		echo 'verdade';
	}
	*/

	//Apenas confere se o valor eh igual.
	/*
	if($nome == $nome2){
		echo 'verdade';
	}

	//Conferimos para ver se e diferente.
	if($nome != $nome2){
		echo 'e diferente.';
	}
	*/

	//Confere se sao identicos ou seja. Mesmo valor e mesmo tipo.
	/*
	if($valor === $valor2){
		echo 'verdade';
	}else{
		echo 'nao sao identicos';
	}
	*/

	//Comparamos para ver se sao diferentes(tipo e valor)
	if($valor !== $valor2){
		echo 'verdade';
	}


?>