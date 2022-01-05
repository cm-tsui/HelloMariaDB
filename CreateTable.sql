--
-- Database Setting
--
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+08:00";

--
-- Database: `test`
-- Table structure for table `test`
--
CREATE TABLE `test` (
  `id` bigint(10) UNSIGNED NOT NULL,
  `test_name` varchar(256) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Indexes for table `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for table `test`
--
ALTER TABLE `test`
  MODIFY `id` bigint(10) UNSIGNED NOT NULL AUTO_INCREMENT;
COMMIT;