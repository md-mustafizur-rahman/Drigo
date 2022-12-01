-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 30, 2022 at 08:27 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `drigo`
--

-- --------------------------------------------------------

--
-- Table structure for table `failed_jobs`
--

CREATE TABLE `failed_jobs` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `uuid` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `connection` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `queue` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `payload` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `exception` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `failed_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `migrations`
--

CREATE TABLE `migrations` (
  `id` int(10) UNSIGNED NOT NULL,
  `migration` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `batch` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `migrations`
--

INSERT INTO `migrations` (`id`, `migration`, `batch`) VALUES
(13, '2014_10_12_000000_create_users_table', 1),
(14, '2014_10_12_100000_create_password_resets_table', 1),
(15, '2019_08_19_000000_create_failed_jobs_table', 1),
(16, '2019_12_14_000001_create_personal_access_tokens_table', 1),
(17, '2022_11_19_120143_create_seller_table', 1),
(18, '2022_11_27_133245_create_product_table', 1);

-- --------------------------------------------------------

--
-- Table structure for table `password_resets`
--

CREATE TABLE `password_resets` (
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `token` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `personal_access_tokens`
--

CREATE TABLE `personal_access_tokens` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `tokenable_type` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tokenable_id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `token` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `abilities` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `last_used_at` timestamp NULL DEFAULT NULL,
  `expires_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `product_id` bigint(20) UNSIGNED NOT NULL,
  `seller_id` int(255) UNSIGNED DEFAULT NULL,
  `product_name` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `product_size` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `product_details` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `product_price` int(255) UNSIGNED DEFAULT NULL,
  `product_Image` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `seller_name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `seller_category` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `shopname` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `shop_latitude` double DEFAULT NULL,
  `shop_longitude` double DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`product_id`, `seller_id`, `product_name`, `product_size`, `product_details`, `product_price`, `product_Image`, `seller_name`, `seller_category`, `shopname`, `shop_latitude`, `shop_longitude`, `created_at`, `updated_at`) VALUES
(21, 4, '7up', '2 liter', 'Up (stylized as 7up outside North America) is a lemon-lime-flavored non-caffeinated soft drink owned by Keurig Dr Pepper although the beverage is ...', 120, '1669636471-drigo.png', 'MD. MUSTAFIZU RAHMAN', 'Cafe', 'sabbir store', 23.82160226373146, 90.34676931905017, '2022-11-28 05:51:50', '2022-11-28 05:54:31'),
(22, 4, 'coca cola', '2 liter', '7 Up (stylized as 7up outside North America) is a lemon-lime-flavored non-caffeinated soft drink owned by Keurig Dr Pepper although the beverage is ...', 120, '1669636343-drigo.jpg', 'MD. MUSTAFIZU RAHMAN', 'Cafe', 'sabbir store', 23.82160226373146, 90.34676931905017, '2022-11-28 05:52:24', '2022-11-28 05:52:24'),
(23, 4, 'mr twist', '250 kg', 'Potato', 15, '1669710002-drigo.jpg', 'MD. MUSTAFIZU RAHMAN', 'Cafe', 'sabbir store', 23.82160226373146, 90.34676931905017, '2022-11-28 05:58:24', '2022-11-29 02:20:02'),
(24, 4, 'cone', '5 ml', 'ice cream', 70, '1669636805-drigo.png', 'MD. MUSTAFIZU RAHMAN', 'Cafe', 'sabbir store', 23.82160226373146, 90.34676931905017, '2022-11-28 06:00:05', '2022-11-28 06:00:05'),
(25, 4, 'Harpic', '200 ml', 'Harpic toilate cliner', 45, '1669638076-drigo.jpg', 'MD. MUSTAFIZU RAHMAN', 'Cafe', 'sabbir store', 23.82160226373146, 90.34676931905017, '2022-11-28 06:21:16', '2022-11-28 06:21:16'),
(26, 4, 'Rin white', '1 kg', 'Rin', 120, '1669652189-drigo.jpeg', 'MD. MUSTAFIZU RAHMAN', 'Cafe', 'sabbir store', 23.82160226373146, 90.34676931905017, '2022-11-28 06:24:02', '2022-11-28 10:16:29'),
(27, 5, 'Crispy KFC', '500 g', 'Looking for a quick snack recipe? Yummy KFC Chicken Fry recipe with easy procedure. Very very ...', 500, '1669649143-drigo.jpg', 'MD. MUSTAFIZU RAHMAN', 'Cafe', 'KFC', 23.724340855774862, 90.38742162066357, '2022-11-28 09:25:43', '2022-11-28 09:25:43'),
(28, 5, 'Birayni', '500 g', 'Haji Birayni', 350, '1669649256-drigo.jpg', 'MD. MUSTAFIZU RAHMAN', 'Cafe', 'KFC', 23.724340855774862, 90.38742162066357, '2022-11-28 09:27:36', '2022-11-28 09:27:36'),
(29, 5, 'Pasta', '250 g', 'Craving some authentic Italian-style pasta? No need to order it from the market when you can make it ...\r\nIngredients\r\n350 grams pasta penne\r\n1 tablespoon extra virgin olive oil\r\n1 tablespoon butter\r\n1 teaspoon thyme\r\n5 cloves garlic chopped', 200, '1669649327-drigo.jpg', 'MD. MUSTAFIZU RAHMAN', 'Cafe', 'KFC', 23.724340855774862, 90.38742162066357, '2022-11-28 09:28:47', '2022-11-28 09:28:47'),
(30, 5, 'noodles', '100 g', '... is the best ramen noodle recipe made easy at home with a simple and super flavorful sauce! Make ...\r\nIngredients\r\n2 3 Ounce Packages of Ramen Noodles, (Seasoning Packet Discarded)\r\n2 Teaspoons Sesame Oil\r\n2 Cloves Garlic, (Minced)\r\n1/4 Cup Soy Sauce** (Low Sodium is Best)\r\n1 Teaspoon Brown Sugar', 80, '1669649397-drigo.jpg', 'MD. MUSTAFIZU RAHMAN', 'Cafe', 'KFC', 23.724340855774862, 90.38742162066357, '2022-11-28 09:29:57', '2022-11-28 09:29:57');

-- --------------------------------------------------------

--
-- Table structure for table `seller`
--

CREATE TABLE `seller` (
  `seller_id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `username` varchar(60) COLLATE utf8mb4_unicode_ci NOT NULL,
  `category` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `shopname` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `latitude` double NOT NULL,
  `longitude` double NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `seller`
--

INSERT INTO `seller` (`seller_id`, `name`, `username`, `category`, `shopname`, `email`, `latitude`, `longitude`, `password`, `created_at`, `updated_at`) VALUES
(4, 'MD. MUSTAFIZU RAHMAN', 'sabbirpegon', 'Cafe', 'sabbir Store', 'Sabbir343@gmail.com', 23.82160226373146, 90.34676931905017, '204c75bb2bbe7ed6aad32b9b2760cef1', '2022-11-27 10:05:31', '2022-11-27 10:05:31'),
(5, 'TASIN', 'sabbirpegon1', 'Cafe', 'KFC', 'Sabbir343@gmail.com', 23.724340855774862, 90.38742162066357, '204c75bb2bbe7ed6aad32b9b2760cef1', '2022-11-27 10:05:31', '2022-11-27 10:05:31');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email_verified_at` timestamp NULL DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `remember_token` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `failed_jobs`
--
ALTER TABLE `failed_jobs`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `failed_jobs_uuid_unique` (`uuid`);

--
-- Indexes for table `migrations`
--
ALTER TABLE `migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `password_resets`
--
ALTER TABLE `password_resets`
  ADD KEY `password_resets_email_index` (`email`);

--
-- Indexes for table `personal_access_tokens`
--
ALTER TABLE `personal_access_tokens`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `personal_access_tokens_token_unique` (`token`),
  ADD KEY `personal_access_tokens_tokenable_type_tokenable_id_index` (`tokenable_type`,`tokenable_id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `seller`
--
ALTER TABLE `seller`
  ADD PRIMARY KEY (`seller_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_email_unique` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `failed_jobs`
--
ALTER TABLE `failed_jobs`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `migrations`
--
ALTER TABLE `migrations`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `personal_access_tokens`
--
ALTER TABLE `personal_access_tokens`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `product_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `seller`
--
ALTER TABLE `seller`
  MODIFY `seller_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
