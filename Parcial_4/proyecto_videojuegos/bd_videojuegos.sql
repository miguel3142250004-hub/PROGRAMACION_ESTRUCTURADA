-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 09, 2026 at 06:01 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bd_videojuegos`
--

-- --------------------------------------------------------

--
-- Table structure for table `historial_precios`
--

CREATE TABLE `historial_precios` (
  `id_historial` int(11) NOT NULL,
  `id_precio` int(11) NOT NULL,
  `precio_anterior` decimal(8,2) NOT NULL,
  `fecha_anterior` date NOT NULL DEFAULT '2020-07-15',
  `precio_nuevo` decimal(8,2) NOT NULL,
  `fecha_cambio` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `historial_precios`
--

INSERT INTO `historial_precios` (`id_historial`, `id_precio`, `precio_anterior`, `fecha_anterior`, `precio_nuevo`, `fecha_cambio`) VALUES
(1, 3, 300.00, '2020-07-15', 200.00, '2026-08-05 08:27:37'),
(2, 1, 135.00, '2020-07-15', 140.00, '2026-08-05 10:03:06');

-- --------------------------------------------------------

--
-- Table structure for table `juegos`
--

CREATE TABLE `juegos` (
  `id_juego` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `genero` varchar(50) DEFAULT NULL,
  `desarrollador` varchar(100) DEFAULT NULL,
  `anio_lanzamiento` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `juegos`
--

INSERT INTO `juegos` (`id_juego`, `nombre`, `genero`, `desarrollador`, `anio_lanzamiento`) VALUES
(1, 'ELDEN RING', 'RPG', 'FROMSOFTWARE', 2022),
(2, 'STARDEW VALLEY', 'SIMULACION', 'CONCERNEDAPE', 2016),
(3, 'MORTAL KOMBAT', 'PELEAS', 'NETHERREALM STUDIOS', 1992);

-- --------------------------------------------------------

--
-- Table structure for table `plataformas`
--

CREATE TABLE `plataformas` (
  `id_plataforma` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `url_tienda` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `plataformas`
--

INSERT INTO `plataformas` (`id_plataforma`, `nombre`, `url_tienda`) VALUES
(1, 'Steam', 'https://store.steampowered.com'),
(2, 'Epic Games', 'https://store.epicgames.com'),
(3, 'GOG', 'https://www.gog.com');

-- --------------------------------------------------------

--
-- Table structure for table `precios`
--

CREATE TABLE `precios` (
  `id_precio` int(11) NOT NULL,
  `id_juego` int(11) NOT NULL,
  `id_plataforma` int(11) NOT NULL,
  `precio` decimal(8,2) NOT NULL,
  `moneda` varchar(5) DEFAULT 'USD',
  `descuento` int(11) DEFAULT 0,
  `precio_final` decimal(10,2) GENERATED ALWAYS AS (round(`precio` - `precio` * `descuento` / 100,2)) STORED,
  `fecha_actualizacion` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `precios`
--

INSERT INTO `precios` (`id_precio`, `id_juego`, `id_plataforma`, `precio`, `moneda`, `descuento`, `fecha_actualizacion`) VALUES
(1, 3, 2, 140.00, 'MXN', 0, '2026-08-05 10:03:05'),
(2, 3, 3, 200.00, 'MXN', 20, '2026-08-05 09:26:29'),
(3, 3, 1, 300.00, 'MXN', 70, '2026-08-05 09:26:54');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `historial_precios`
--
ALTER TABLE `historial_precios`
  ADD PRIMARY KEY (`id_historial`),
  ADD KEY `id_precio` (`id_precio`);

--
-- Indexes for table `juegos`
--
ALTER TABLE `juegos`
  ADD PRIMARY KEY (`id_juego`);

--
-- Indexes for table `plataformas`
--
ALTER TABLE `plataformas`
  ADD PRIMARY KEY (`id_plataforma`);

--
-- Indexes for table `precios`
--
ALTER TABLE `precios`
  ADD PRIMARY KEY (`id_precio`),
  ADD KEY `id_juego` (`id_juego`),
  ADD KEY `id_plataforma` (`id_plataforma`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `historial_precios`
--
ALTER TABLE `historial_precios`
  MODIFY `id_historial` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `juegos`
--
ALTER TABLE `juegos`
  MODIFY `id_juego` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `plataformas`
--
ALTER TABLE `plataformas`
  MODIFY `id_plataforma` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `precios`
--
ALTER TABLE `precios`
  MODIFY `id_precio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `historial_precios`
--
ALTER TABLE `historial_precios`
  ADD CONSTRAINT `historial_precios_ibfk_1` FOREIGN KEY (`id_precio`) REFERENCES `precios` (`id_precio`) ON DELETE CASCADE;

--
-- Constraints for table `precios`
--
ALTER TABLE `precios`
  ADD CONSTRAINT `precios_ibfk_1` FOREIGN KEY (`id_juego`) REFERENCES `juegos` (`id_juego`) ON DELETE CASCADE,
  ADD CONSTRAINT `precios_ibfk_2` FOREIGN KEY (`id_plataforma`) REFERENCES `plataformas` (`id_plataforma`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
