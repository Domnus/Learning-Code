<?php
	
	$pdo = new PDO('mysql:host=localhost;dbname=modulo_8','root','');

	$id = 5;

	//OR funciona como `ou`
	//AND funciona como `e`

	$sql = $pdo->prepare("DELETE FROM `clientes` WHERE id=?");

	if($sql->execute(array($id))){
		echo 'Meu cliente foi deletado com sucesso!';
	}

?>