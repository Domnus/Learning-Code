<?php
	class Pessoa{
		//Objeto pessoa

		private $nome = 'Guilherme';
		private $idade = '23';
		private $peso = '70kg';

		public function crescer(){
			$this->comer();
			echo 'estou crescendo';
		}

		private function comer(){
			echo 'estou comendo';
		}

	}

	//Instanciar
	$pessoa = new Pessoa;
	$pessoa2 = new Pessoa;

	$pessoa->crescer();

?>