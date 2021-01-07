<?php
	abstract class teste{

		public $var;

		public function func1(){
			echo 'chamando funcao 1';
		}

		abstract function func2();


	}

	class Principal2{

		public static function outroMetodoEstatico(){
			echo 'meu outro metodo';
		}

	}

	class Principal extends teste{

		public function func2(){
			echo 'estou declarando oficialmente um metodo abstrato';
		}

		public static function metodoestatico(){
			echo 'metodo estatico';
		}

		public function funcao(){
			//Principal::metodoestatico();
			//self::metodoestatico();
			$principal2 = new Principal2;
			Principal2::outroMetodoEstatico();
		}
	}

	$principal = new Principal;
	$principal->funcao();
	//Principal::metodoestatico();

	//$principal->func1();

	//$principal->func2();
?>