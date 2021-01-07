-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 19-Maio-2017 às 19:14
-- Versão do servidor: 10.1.21-MariaDB
-- PHP Version: 7.0.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `modulo_8`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `categorias`
--

CREATE TABLE `categorias` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `categorias`
--

INSERT INTO `categorias` (`id`, `nome`) VALUES
(1, 'Geral'),
(2, 'Esportes');

-- --------------------------------------------------------

--
-- Estrutura da tabela `clientes`
--

CREATE TABLE `clientes` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `sobrenome` varchar(255) NOT NULL,
  `momento_registro` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `posts`
--

CREATE TABLE `posts` (
  `id` int(11) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `categoria_id` int(11) NOT NULL,
  `conteudo` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `posts`
--

INSERT INTO `posts` (`id`, `titulo`, `categoria_id`, `conteudo`) VALUES
(1, 'Minha noticia geral', 1, 'Meu texto de exemplo'),
(2, 'Minha noticia geral 2', 1, 'Meu texto de exemplo2'),
(3, 'Noticia de esporte', 2, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi non ornare urna, quis tincidunt nunc. Cras scelerisque, metus vitae placerat finibus, libero nibh ullamcorper purus, ac molestie urna enim ut dui. Nam et ligula lacinia, tincidunt justo in, aliquet libero. Pellentesque vitae augue id augue ultricies tempus. Donec sagittis eleifend augue, in commodo augue interdum et. In porttitor sapien lectus. Nunc id enim auctor, posuere sapien vitae, interdum lacus. Ut in tellus semper purus viverra blandit ac quis odio. Nulla blandit ex quis dictum ultricies.'),
(4, 'Minha outra noticia de esporte', 2, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi non ornare urna, quis tincidunt nunc. Cras scelerisque, metus vitae placerat finibus, libero nibh ullamcorper purus, ac molestie urna enim ut dui. Nam et ligula lacinia, tincidunt justo in, aliquet libero. Pellentesque vitae augue id augue ultricies tempus. Donec sagittis eleifend augue, in commodo augue interdum et. In porttitor sapien lectus. Nunc id enim auctor, posuere sapien vitae, interdum lacus. Ut in tellus semper purus viverra blandit ac quis odio. Nulla blandit ex quis dictum ultricies.');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `categorias`
--
ALTER TABLE `categorias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
