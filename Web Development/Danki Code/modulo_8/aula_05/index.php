<?php
	$pdo = new PDO('mysql:host=localhost;dbname=modulo_8','root','');

	/*
	$sql = $pdo->prepare("SELECT * FROM posts WHERE categoria_id = ?");

	$sql->execute(array($_GET['categoria_id']));

	$info = $sql->fetchAll();

	
	foreach ($info as $key => $value) {
		echo 'Titulo: '.$value['titulo'];
		echo '<br />';
		echo 'Noticia: '.$value['conteudo'];
		echo '<hr>';
	}

	*/
	

	/*
	for($i = 0; $i < count($info); $i++){
		echo 'Titulo: '.$info[$i]['titulo'];
		echo '<br />';
		echo 'Noticia: '.$info[$i]['conteudo'];
		echo '<hr>';
	}
	*/

	/*
   $sql = $pdo->prepare("SELECT * FROM categorias");

	$sql->execute();

	$info = $sql->fetchAll();
	*/

	/*
	foreach ($info as $key => $value) {
		$categoria_id = $value['id'];
		echo 'Exibindo posts de: '.$value['nome'];
		echo '<br />';
		$sql = $pdo->prepare("SELECT * FROM posts WHERE categoria_id = $categoria_id");
		$sql->execute();
		$infoPosts = $sql->fetchAll();
		foreach ($infoPosts as $key => $value) {
			echo 'Titulo: '.$value['titulo'];
			echo '<br />';
			echo 'Noticia: '.$value['conteudo'];
			echo '<hr>';
		}
	}
	*/

	$sql = $pdo->prepare("SELECT `posts`.*,`categorias`.*,`posts`.`id` AS `post_id` FROM `posts` INNER JOIN `categorias` ON `posts`.`categoria_id` = `categorias`.`id`");

	$sql->execute();

	$info = $sql->fetchAll(PDO::FETCH_ASSOC);
	
	echo '<pre>';
	print_r($info);
	echo '</pre>';
?>