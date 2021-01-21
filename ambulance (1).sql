-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 21, 2021 at 07:41 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ambulance`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `hospital_id` int(11) NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`hospital_id`, `name`, `phone`, `email`, `password`) VALUES
(1, 'admi', '9874561230', 'admi@gmail.com', '156');

-- --------------------------------------------------------

--
-- Table structure for table `patient_details`
--

CREATE TABLE `patient_details` (
  `PNO` int(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `place` varchar(255) DEFAULT NULL,
  `date_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patient_details`
--

INSERT INTO `patient_details` (`PNO`, `name`, `email`, `phone`, `address`, `place`, `date_time`) VALUES
(1, 'sumanthkumar s', 'sum@gmail.com', '2147483647', 'udupi', '9.967176.2904', '0000-00-00 00:00:00'),
(2, 'sumanthkumar s', 'sum@gmail.com', '2147483647', 'udupi', 'Ernakulam', '2001-02-21 00:00:00'),
(3, 'shrivasta', 'sh@gmail.com', '2147483647', 'None', 'Ernakulam', '2001-02-21 09:21:52'),
(4, 'sumanthkumar s', 'sum@gmail.com', '7894561230', 'udupi', 'Bengaluru', '2001-09-21 17:13:34'),
(5, 'sumanthkumar s', 'sum@gmail.com', '7894561230', 'udupi', 'Bengaluru', '2001-12-21 07:35:46'),
(6, 'sumanthkumar s', 'sum@gmail.com', '7894561230', 'udupi', 'Bengaluru', '0000-00-00 00:00:00'),
(7, 'sumanthkumar s', 'sum@gmail.com', '7894561230', 'udupi', 'Bengaluru', '0000-00-00 00:00:00'),
(8, 'sumanthkumar s', 'sum@gmail.com', '7894561230', 'udupi', 'Bengaluru', '2001-12-21 11:54:42');

-- --------------------------------------------------------

--
-- Table structure for table `request_accept`
--

CREATE TABLE `request_accept` (
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `latitude` varchar(255) DEFAULT NULL,
  `longitude` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `reqst_accept` varchar(255) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `request_accept`
--

INSERT INTO `request_accept` (`name`, `email`, `latitude`, `longitude`, `state`, `city`, `reqst_accept`, `date`, `time`) VALUES
('anm', 'ann@gmail.com', '12.9634', '77.5855', 'Karnataka', 'Bengaluru', 'Accepted', '0000-00-00', '09:21:11');

-- --------------------------------------------------------

--
-- Table structure for table `request_details`
--

CREATE TABLE `request_details` (
  `id` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `latitude` varchar(255) DEFAULT NULL,
  `longitude` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `reqst_accept` varchar(255) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `request_details`
--

INSERT INTO `request_details` (`id`, `name`, `email`, `latitude`, `longitude`, `state`, `city`, `reqst_accept`, `date`, `time`) VALUES
('1', 'sumanthkumar s', 'sum@gmail.com', '9.9671', '76.2904', 'Kerala', 'Ernakulam', 'Requesting for Ambulance', '2001-02-21', '08:45:49'),
('1', 'abcs', 'abc@gmail.com', '9.9671', '76.2904', 'Kerala', 'Ernakulam', 'Accepted', '2001-02-21', '08:46:40'),
('1', 'sumanthkumar s', 'sum@gmail.com', '9.9671', '76.2904', 'Kerala', 'Ernakulam', 'Requesting for Ambulance', '2001-02-21', '09:11:11'),
('1', 'abcs', 'abc@gmail.com', '9.9671', '76.2904', 'Kerala', 'Ernakulam', 'Accepted', '2001-02-21', '09:12:03'),
('2', 'shrivasta', 'sh@gmail.com', '9.9671', '76.2904', 'Kerala', 'Ernakulam', 'Requesting for Ambulance', '2001-02-21', '09:19:03'),
('4', 'xyz', 'xyz@gmail.com', '9.9671', '76.2904', 'Kerala', 'Ernakulam', 'Accepted', '2001-02-21', '09:21:03'),
('1', 'sumanthkumar s', 'sum@gmail.com', '12.9719', '77.5937', 'Karnataka', 'Bengaluru', 'Requesting for Ambulance', '2001-09-21', '17:09:15'),
('1', 'abcs', 'abc@gmail.com', '12.9719', '77.5937', 'Karnataka', 'Bengaluru', 'Accepted', '2001-09-21', '17:11:28'),
('1', 'sumanthkumar s', 'sum@gmail.com', '12.9719', '77.5937', 'Karnataka', 'Bengaluru', 'Requesting for Ambulance', '2001-11-21', '23:41:45'),
('1', 'abcs', 'abc@gmail.com', '12.9719', '77.5937', 'Karnataka', 'Bengaluru', 'Reject', '2001-11-21', '23:43:02'),
('1', 'sumanthkumar s', 'sum@gmail.com', '12.9719', '77.5937', 'Karnataka', 'Bengaluru', 'Requesting for Ambulance', '2001-12-21', '07:35:46'),
('1', 'abcs', 'abc@gmail.com', '12.9719', '77.5937', 'Karnataka', 'Bengaluru', 'Accepted', '2001-12-21', '07:36:43'),
('1', 'sumanthkumar s', 'sum@gmail.com', '12.9719', '77.5937', 'Karnataka', 'Bengaluru', 'Requesting for Ambulance', '2001-12-21', '07:35:46'),
('1', 'abcs', 'abc@gmail.com', '12.9719', '77.5937', 'Karnataka', 'Bengaluru', 'Reject', '2001-12-21', '07:42:30'),
('1', 'sumanthkumar s', 'sum@gmail.com', '12.9719', '77.5937', 'Karnataka', 'Bengaluru', 'Requesting for Ambulance', '0000-00-00', '11:35:23'),
('1', 'abcs', 'abc@gmail.com', '12.9719', '77.5937', 'Karnataka', 'Bengaluru', 'Accepted', '2001-12-21', '11:36:28'),
('1', 'sumanthkumar s', 'sum@gmail.com', '12.9719', '77.5937', 'Karnataka', 'Bengaluru', 'Requesting for Ambulance', '0000-00-00', '11:45:09'),
('1', 'abcs', 'abc@gmail.com', '12.9719', '77.5937', 'Karnataka', 'Bengaluru', 'Accepted', '2001-12-21', '11:45:41'),
('1', 'sumanthkumar s', 'sum@gmail.com', '12.9719', '77.5937', 'Karnataka', 'Bengaluru', 'Requesting for Ambulance', '2001-12-21', '11:53:32'),
('1', 'abcs', 'abc@gmail.com', '12.9719', '77.5937', 'Karnataka', 'Bengaluru', 'Accepted', '2001-12-21', '11:54:14'),
('2', 'shrivasta', 'sh@gmail.com', '12.9719', '77.5937', 'Karnataka', 'Bengaluru', 'Requesting for Ambulance', '2001-12-21', '13:09:39'),
('8', 'varu', 'varu@gmail.com', '12.9719', '77.5937', 'Karnataka', 'Bengaluru', 'Reject', '2001-12-21', '13:09:57'),
('4', 'ram', 'ram@gmail.com', '12.9634', '77.5855', 'Karnataka', 'Bengaluru', 'Requesting for Ambulance', '0000-00-00', '09:14:02'),
('10', 'anm', 'ann@gmail.com', '12.9634', '77.5855', 'Karnataka', 'Bengaluru', 'Accepted', '0000-00-00', '09:21:11');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(255) NOT NULL,
  `f_name` varchar(255) DEFAULT NULL,
  `l_name` varchar(255) DEFAULT NULL,
  `phone` int(10) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `f_name`, `l_name`, `phone`, `email`, `dob`, `gender`, `password`) VALUES
(1, 'sumanth', 'kumar s', 2147483647, 'sum@gmail.com', '0000-00-00', 'Male', '123'),
(2, 'shrivasta', '', 2147483647, 'sh@gmail.com', '2000-05-20', 'Male', '456'),
(4, 'aksnxkn', '', 9446131, 'aj@gmail.com', '2021-12-01', 'SELECT', '123'),
(5, 'ram', '', 2147483647, 'ram@gmail.com', '2021-12-01', 'Male', '123');

-- --------------------------------------------------------

--
-- Table structure for table `user_info`
--

CREATE TABLE `user_info` (
  `user_id` int(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_info`
--

INSERT INTO `user_info` (`user_id`, `name`, `phone`, `email`, `dob`, `gender`, `address`) VALUES
(1, 'sumanthkumar s', '7894561230', 'sum@gmail.com', '2000-03-20', 'Male', 'udupi'),
(2, 'shrivasta', '8965785412', 'sh@gmail.com', '2000-05-20', 'Male', NULL),
(3, 'aksnxkn', '9446131', 'aj@gmail.com', '2021-12-01', 'SELECT', NULL),
(4, 'ram', '8569854782', 'ram@gmail.com', '2021-12-01', 'Male', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `worker`
--

CREATE TABLE `worker` (
  `id` int(255) NOT NULL,
  `f_name` varchar(255) DEFAULT NULL,
  `l_name` varchar(255) DEFAULT NULL,
  `phone` int(10) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `worker`
--

INSERT INTO `worker` (`id`, `f_name`, `l_name`, `phone`, `email`, `dob`, `gender`, `password`) VALUES
(3, 'abc', 's', 2147483647, 'abc@gmail.com', '2000-03-20', 'male', '123'),
(4, 'xy', 'z', 2147483647, 'xyz@gmail.com', '2000-03-15', 'Male', '456'),
(5, 'rh', '', 2147483647, 'rh@gmail.com', '2000-03-20', 'Male', '123'),
(12, 'aak', '', 2147483647, 'ak@gmail.com', '2021-11-01', 'Female', '156'),
(13, 'varu', '', 994616161, 'varu@gmail.com', '2021-12-01', 'SELECT', '123'),
(14, 'bars', '', 986785412, 'barv@gmail.com', '2021-12-01', 'Male', '123'),
(15, 'anm', '', 944452111, 'ann@gmail.com', '2021-12-01', 'Male', '122');

-- --------------------------------------------------------

--
-- Table structure for table `worker_manage`
--

CREATE TABLE `worker_manage` (
  `worker_id` int(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `gender` enum('male','female','others','') DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `worker_manage`
--

INSERT INTO `worker_manage` (`worker_id`, `name`, `phone`, `email`, `dob`, `gender`, `address`) VALUES
(1, 'abcs', '9874563210', 'abc@gmail.com', '2021-11-01', 'male', 'mandares'),
(2, 'xyz', '9856785412', 'xyz@gmail.com', '2000-03-15', 'male', NULL),
(5, 'rh', '9874563210', 'rh@gmail.com', '2000-03-20', 'male', NULL),
(7, 'aak', '9856785412', 'ak@gmail.com', '2021-11-01', 'female', 'manglore\n'),
(8, 'varu', '994616161', 'varu@gmail.com', '2021-12-01', 'male', 'manglore'),
(9, 'bars', '986785412', 'barv@gmail.com', '2021-12-01', 'male', NULL),
(10, 'anm', '944452111', 'ann@gmail.com', '2021-12-01', 'male', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`hospital_id`);

--
-- Indexes for table `patient_details`
--
ALTER TABLE `patient_details`
  ADD PRIMARY KEY (`PNO`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_info`
--
ALTER TABLE `user_info`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `worker`
--
ALTER TABLE `worker`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `worker_manage`
--
ALTER TABLE `worker_manage`
  ADD PRIMARY KEY (`worker_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `hospital_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `patient_details`
--
ALTER TABLE `patient_details`
  MODIFY `PNO` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `user_info`
--
ALTER TABLE `user_info`
  MODIFY `user_id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `worker`
--
ALTER TABLE `worker`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `worker_manage`
--
ALTER TABLE `worker_manage`
  MODIFY `worker_id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
