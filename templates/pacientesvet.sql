-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-07-2021 a las 19:45:24
-- Versión del servidor: 10.4.19-MariaDB
-- Versión de PHP: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `pacientesvet`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pacientesvet`
--

CREATE TABLE `pacientesvet` (
  `nombreMascota` varchar(45) NOT NULL,
  `idMascota` int(45) NOT NULL,
  `especie` varchar(45) NOT NULL,
  `raza` varchar(45) NOT NULL,
  `tamano` varchar(45) NOT NULL,
  `peso` int(45) NOT NULL,
  `color` varchar(45) NOT NULL,
  `genero` varchar(45) NOT NULL,
  `fechaNac` date NOT NULL,
  `estado` varchar(45) NOT NULL,
  `nombreDueno` varchar(45) NOT NULL,
  `apellidoDueno` varchar(45) NOT NULL,
  `direccion` varchar(45) NOT NULL,
  `telefono` int(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `pacientesvet`
--

INSERT INTO `pacientesvet` (`nombreMascota`, `idMascota`, `especie`, `raza`, `tamano`, `peso`, `color`, `genero`, `fechaNac`, `estado`, `nombreDueno`, `apellidoDueno`, `direccion`, `telefono`) VALUES
('Luna', 1, 'perro', '', 'grande', 29, 'dorado', 'hembra', '2018-02-14', 'sano', 'adriana', 'adriluna', 'Luna 1200, CABA', 1122558855);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `pacientesvet`
--
ALTER TABLE `pacientesvet`
  ADD PRIMARY KEY (`idMascota`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `pacientesvet`
--
ALTER TABLE `pacientesvet`
  MODIFY `idMascota` int(45) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
