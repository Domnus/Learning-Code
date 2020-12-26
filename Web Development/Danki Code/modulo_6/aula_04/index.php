<?php
	function mostrarNome($nome,$idade){
		echo '<h2>Nome e: </h2>'.$nome;
		echo '<hr>';
		echo "Idade: $idade";
	}

	function calculadora($numero1 = 10,$numero2 = 5){
		echo ($numero1+$numero2);
	}

	function verdade(){
		return true;
	}

	function retornarString(){
		return 'Guilherme';
	}

	echo retornarString();

	$variavel = verdade();

	//calculadora(20,30);
?>