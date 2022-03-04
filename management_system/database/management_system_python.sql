-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 04, 2022 at 03:01 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 7.3.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `management_system_python`
--

-- --------------------------------------------------------

--
-- Table structure for table `batch_management`
--

CREATE TABLE `batch_management` (
  `id` int(50) NOT NULL,
  `courseid` int(50) NOT NULL,
  `startdate` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `enddate` timestamp NULL DEFAULT NULL,
  `classtime` varchar(200) NOT NULL,
  `title` varchar(200) DEFAULT NULL,
  `isDeleted` int(50) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `batch_management`
--

INSERT INTO `batch_management` (`id`, `courseid`, `startdate`, `enddate`, `classtime`, `title`, `isDeleted`) VALUES
(2, 1, '2022-03-04 12:56:42', '2022-07-24 18:30:00', '03.04 AM', 'b1', 0),
(3, 1, '2022-08-19 12:56:46', '2022-09-25 18:30:00', '05:56 AM', 'b2', 0),
(4, 2, '2022-12-23 18:30:00', '2023-04-25 18:30:00', '08:09 AM', 'b2', 0);

-- --------------------------------------------------------

--
-- Table structure for table `course_management`
--

CREATE TABLE `course_management` (
  `id` int(90) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `fees` int(26) DEFAULT NULL,
  `duration` varchar(250) DEFAULT NULL,
  `description` varchar(250) DEFAULT NULL,
  `isDeleted` int(100) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `course_management`
--

INSERT INTO `course_management` (`id`, `title`, `fees`, `duration`, `description`, `isDeleted`) VALUES
(1, 'python', 6500, '4 months', 'good', 0),
(2, 'laravels', 7500, '7 months', 'excelling popular', 0);

-- --------------------------------------------------------

--
-- Table structure for table `lecture_management`
--

CREATE TABLE `lecture_management` (
  `id` int(50) NOT NULL,
  `teacherid` int(50) DEFAULT NULL,
  `subjectid` int(50) DEFAULT NULL,
  `batchid` int(50) DEFAULT NULL,
  `duration` varchar(255) DEFAULT NULL,
  `amount` int(100) DEFAULT NULL,
  `lecturedate` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `lecture_management`
--

INSERT INTO `lecture_management` (`id`, `teacherid`, `subjectid`, `batchid`, `duration`, `amount`, `lecturedate`) VALUES
(1, 1, 1, 2, '3 months', 5000, '2022-03-04 13:54:53'),
(2, 1, 1, 3, '3 months', 5000, '2022-09-23 18:30:00'),
(3, 1, 1, 4, '3 months', 5000, '2022-03-04 13:54:57');

-- --------------------------------------------------------

--
-- Table structure for table `subject_management`
--

CREATE TABLE `subject_management` (
  `id` int(50) NOT NULL,
  `courseid` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `rate` int(100) DEFAULT NULL,
  `isDeleted` int(50) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subject_management`
--

INSERT INTO `subject_management` (`id`, `courseid`, `title`, `rate`, `isDeleted`) VALUES
(1, '1', 'Web Scrapping', 780, 0),
(2, '2', 'controllers', 800, 0);

-- --------------------------------------------------------

--
-- Table structure for table `teacher_management`
--

CREATE TABLE `teacher_management` (
  `id` int(50) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `mobile` int(20) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `gender` varchar(200) DEFAULT NULL,
  `qualification` varchar(200) DEFAULT NULL,
  `experience` int(50) DEFAULT NULL,
  `isDeleted` int(20) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `teacher_management`
--

INSERT INTO `teacher_management` (`id`, `name`, `mobile`, `email`, `gender`, `qualification`, `experience`, `isDeleted`) VALUES
(1, 'kruti', 2147483647, 'kruti@gmail.com', 'female', 'bcom', 6, 0),
(2, 'yatri', 876789876, 'yatri@gmail.com', 'female', 'bca', 4, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `batch_management`
--
ALTER TABLE `batch_management`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `course_management`
--
ALTER TABLE `course_management`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `lecture_management`
--
ALTER TABLE `lecture_management`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `subject_management`
--
ALTER TABLE `subject_management`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `teacher_management`
--
ALTER TABLE `teacher_management`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `batch_management`
--
ALTER TABLE `batch_management`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `course_management`
--
ALTER TABLE `course_management`
  MODIFY `id` int(90) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `lecture_management`
--
ALTER TABLE `lecture_management`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `subject_management`
--
ALTER TABLE `subject_management`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `teacher_management`
--
ALTER TABLE `teacher_management`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
