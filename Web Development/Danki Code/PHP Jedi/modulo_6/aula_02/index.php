<?php

	//Array single.

	$arr = ['guilherme','joao'];
	$arr = array('guilherme','chave2'=>'joao');

	$arr[0] = 'guilherme';
	$arr[] = 'joao';

	//Arrays Multidimensionais

	//$arr2 = array(array('Guilherme','Joao'),array(23,45));

	//$arr2[0] = array('chave1'=>'guilherme','joao');

	$arr2[0]['chave1'] = 'Guilherme';

	echo $arr2[0]['chave1'];

?>