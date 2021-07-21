-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-07-2021 a las 17:25:44
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
  `nombre_mascota` varchar(45) NOT NULL,
  `id_mascota` int(45) NOT NULL,
  `especie` varchar(45) NOT NULL,
  `raza` varchar(45) NOT NULL,
  `tamaño` varchar(45) NOT NULL,
  `peso_actual` int(45) NOT NULL,
  `color` varchar(45) NOT NULL,
  `genero` varchar(45) NOT NULL,
  `fecha_nac` date NOT NULL,
  `estado` varchar(45) NOT NULL,
  `nombre_dueño` varchar(45) NOT NULL,
  `apellido_dueño` varchar(45) NOT NULL,
  `direccion` varchar(45) NOT NULL,
  `telefono` int(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `pacientesvet`
--

INSERT INTO `pacientesvet` (`nombre_mascota`, `id_mascota`, `especie`, `raza`, `tamaño`, `peso_actual`, `color`, `genero`, `fecha_nac`, `estado`, `nombre_dueño`, `apellido_dueño`, `direccion`, `telefono`) VALUES
('Luna', 1, 'perro', '', 'grande', 29, 'dorado', 'hembra', '2018-02-14', 'sano', 'adriana', 'adriluna', 'Luna 1200, CABA', 1122558855);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `pacientesvet`
--
ALTER TABLE `pacientesvet`
  ADD PRIMARY KEY (`id_mascota`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `pacientesvet`
--
ALTER TABLE `pacientesvet`
  MODIFY `id_mascota` int(45) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
