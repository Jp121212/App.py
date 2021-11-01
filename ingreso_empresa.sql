-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-11-2021 a las 22:32:37
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ingreso_empresa`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `cliente_id` int(20) NOT NULL,
  `cliente_tipocedula` varchar(15) NOT NULL,
  `cliente_nombre` varchar(15) NOT NULL,
  `cliente_apellido` varchar(15) NOT NULL,
  `cliente_calificacioncredito` int(10) NOT NULL,
  `cliente_direccion` varchar(150) NOT NULL,
  `cliente_telefono` varchar(15) NOT NULL,
  `cliente_fechadenacimiento` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`cliente_id`, `cliente_tipocedula`, `cliente_nombre`, `cliente_apellido`, `cliente_calificacioncredito`, `cliente_direccion`, `cliente_telefono`, `cliente_fechadenacimiento`) VALUES
(1234, 'TSE', 'Alfredo', 'Pajas', 70, 'Alajuela, 25 al este Iglesia Adventista\r\n', '+506 7890-4594', '1985-09-03'),
(11822034, 'TSE', 'Pedro', 'Piedra', 80, 'Heredia, 40 al oeste de Mall Oxigeno', '+506 7890-2211', '1990-09-03'),
(12929393, 'TSE', 'Pepe', 'Jimenez', 80, 'Alajuela, 25 al este Pollos Papi', '+506 9023-4232', '2001-09-18'),
(19027384, 'TSE', 'Kiki', 'Piedra', 50, 'Alajuela, 40 norte de la consesionaria antigua Parque la paz', '+506 7890-2003', '1985-09-04');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vendedor`
--

CREATE TABLE `vendedor` (
  `vendedor_CIV` int(30) NOT NULL,
  `vendedor_nombre` varchar(20) NOT NULL,
  `vendedor_apellido` varchar(20) NOT NULL,
  `vendedor_fechadenacimiento` date NOT NULL,
  `vendedor_tipo` varchar(100) NOT NULL,
  `vendedor_salario` int(40) NOT NULL,
  `vendedor_direccion` varchar(150) NOT NULL,
  `vendedor_telefono` varchar(20) NOT NULL,
  `vendedor_porcentaje` float NOT NULL,
  `vendedor_monto` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `vendedor`
--

INSERT INTO `vendedor` (`vendedor_CIV`, `vendedor_nombre`, `vendedor_apellido`, `vendedor_fechadenacimiento`, `vendedor_tipo`, `vendedor_salario`, `vendedor_direccion`, `vendedor_telefono`, `vendedor_porcentaje`, `vendedor_monto`) VALUES
(1000897, 'Asdrual', 'Avila', '1990-02-02', 'Nissan Xtreme', 800000, 'Avenida 10 calle central, San Jose', '+506 7069-4340', 10, 200000),
(2000901, 'Carlos', 'Jimenez', '1985-10-09', 'Sedan Experto', 750000, 'Cartago', '+506 89723303', 10, 220000),
(2000933, 'Pepe', 'Alfredo', '1985-10-09', 'Sedan Todo Terreno', 739999, 'Heredia', '+506 8972345', 5, 20000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas`
--

CREATE TABLE `ventas` (
  `venta_CUV` int(11) NOT NULL,
  `venta_codigo` int(100) NOT NULL,
  `venta_numerocontrato` varchar(100) NOT NULL,
  `venta_vendedores` int(11) NOT NULL,
  `venta_clientes` int(11) NOT NULL,
  `venta_monto` float NOT NULL,
  `venta_fechaventa` date NOT NULL,
  `venta_producto` varchar(200) NOT NULL,
  `venta_marca` varchar(10) NOT NULL,
  `venta_modelo` varchar(10) NOT NULL,
  `venta_ano` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `ventas`
--

INSERT INTO `ventas` (`venta_CUV`, `venta_codigo`, `venta_numerocontrato`, `venta_vendedores`, `venta_clientes`, `venta_monto`, `venta_fechaventa`, `venta_producto`, `venta_marca`, `venta_modelo`, `venta_ano`) VALUES
(190282, 20000001, 'TRR-FDSF-SSSZX', 2000901, 1234, 200000, '2021-10-12', 'Mufla cromada', 'Toyota', 'Cromado', '2016'),
(190283, 2000330, 'PDODWEQ-EQWESD-QWEW', 2000901, 19027384, 4000000, '2021-09-12', 'Toyota Corolla, dos puertas, Acabado Elegante, Aceleracion y turbo', 'Toyota', 'Corolla', '2020'),
(190284, 20000889, 'FERO93-1232L', 2000933, 11822034, 2000, '2021-10-12', 'Toyota Cromado Full Extras,Hibrido', 'Toyota', 'Cromado', '2021'),
(190285, 20000888, 'SDAP-SDAD3-Q322', 2000901, 19027384, 500000000, '2021-10-28', 'Suzuki 4X4 2019', 'Suzuki', '4x4', '2021');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`cliente_id`),
  ADD KEY `cliente_nombre` (`cliente_nombre`),
  ADD KEY `cliente_apellido` (`cliente_apellido`),
  ADD KEY `cliente_telefono` (`cliente_telefono`);

--
-- Indices de la tabla `vendedor`
--
ALTER TABLE `vendedor`
  ADD PRIMARY KEY (`vendedor_CIV`),
  ADD KEY `vendedor_nombre` (`vendedor_nombre`),
  ADD KEY `vendedor_apellido` (`vendedor_apellido`),
  ADD KEY `vendedor_telefono` (`vendedor_telefono`);

--
-- Indices de la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD PRIMARY KEY (`venta_CUV`),
  ADD KEY `venta_clientes` (`venta_clientes`),
  ADD KEY `venta_monto` (`venta_monto`),
  ADD KEY `venta_fechaventa` (`venta_fechaventa`),
  ADD KEY `venta_marca` (`venta_marca`),
  ADD KEY `venta_modelo` (`venta_modelo`),
  ADD KEY `venta_ano` (`venta_ano`),
  ADD KEY `venta_codigo` (`venta_codigo`),
  ADD KEY `venta_vendedores` (`venta_vendedores`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `ventas`
--
ALTER TABLE `ventas`
  MODIFY `venta_CUV` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=190286;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`venta_clientes`) REFERENCES `cliente` (`cliente_id`),
  ADD CONSTRAINT `ventas_ibfk_2` FOREIGN KEY (`venta_vendedores`) REFERENCES `vendedor` (`vendedor_CIV`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
