<!DOCTYPE html>
<html>
<head>
	<title>Formulario</title>
</head>
<body>
	<?php
		/*
		if(isset($_GET['acao'])){
			$nome = @$_GET['nome'];
			$email = @$_GET['email'];
			echo $nome;
			echo '<br />';
			echo $email;
		}
		*/

		/*
		if(isset($_POST['acao'])){
			echo $_POST['numero1'] + $_POST['numero2'];
		}

		*/

		if(isset($_POST['acao'])){
			foreach ($_POST['valor'] as $key => $value) {
				echo $key;
				echo '=>';
				echo $value;

				echo '<hr>';

			}
		}


	?>
	<form method="post">
		<select name="nome">
			<option value="guilherme">guilherme</option>
			<option value="joao">joao</option>
		</select>
		<input type="checkbox" name="valor[]" value="10">10
		<input type="checkbox" name="valor[]" value="20">20
		<input type="checkbox" name="valor[]" value="30">30
		<input type="checkbox" name="valor[]" value="40">40
		<input type="submit" name="acao" value="Enviar" />
	</form>
</body>
</html>