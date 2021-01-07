<?php
	/**
	* Esta classe e de exemplo!
	*/

	//Public funciona em qualquer lugar!
	//Private so conseguimos acessar dentro da classe!

	class Exemplo
	{
		private $var1;
		public $var2;
		//public static $var3 = 'statico';
		/*
		public function metodo(){

		}

		public static function metodoEstatico(){
			//echo 'metodo estatico';
		}

		private function metodo2(){

		}
		*/

		public function setVar1($var1){
			$this->var1 = $var1;
		}

		public function pegaVar1(){
			return $this->var1;
		}

	}
?>