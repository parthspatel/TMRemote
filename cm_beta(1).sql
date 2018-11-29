-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 28, 2018 at 04:39 PM
-- Server version: 5.5.60-MariaDB
-- PHP Version: 7.1.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cm_beta`
--

-- --------------------------------------------------------

--
-- Table structure for table `api_tokens`
--

CREATE TABLE `api_tokens` (
  `id` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_id` int(10) UNSIGNED NOT NULL,
  `ip_address` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_agent` text COLLATE utf8mb4_unicode_ci,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `expires_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `bot_logs`
--

CREATE TABLE `bot_logs` (
  `id` int(10) UNSIGNED NOT NULL,
  `user_id` int(11) NOT NULL,
  `char_id` int(11) NOT NULL,
  `char_name` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `world_id` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `channel` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `level` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `mesos` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `map_id` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `nodes` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `item_data` text COLLATE utf8mb4_unicode_ci,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `countries`
--

CREATE TABLE `countries` (
  `id` int(10) UNSIGNED NOT NULL,
  `capital` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `citizenship` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `country_code` varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `currency` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `currency_code` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `currency_sub_unit` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `currency_symbol` varchar(3) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `full_name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `iso_3166_2` varchar(2) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `iso_3166_3` varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `region_code` varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `sub_region_code` varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `eea` tinyint(1) NOT NULL DEFAULT '0',
  `calling_code` varchar(3) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `flag` varchar(6) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `countries`
--

INSERT INTO `countries` (`id`, `capital`, `citizenship`, `country_code`, `currency`, `currency_code`, `currency_sub_unit`, `currency_symbol`, `full_name`, `iso_3166_2`, `iso_3166_3`, `name`, `region_code`, `sub_region_code`, `eea`, `calling_code`, `flag`) VALUES
(4, 'Kabul', 'Afghan', '004', 'afghani', 'AFN', 'pul', '؋', 'Islamic Republic of Afghanistan', 'AF', 'AFG', 'Afghanistan', '142', '034', 0, '93', 'AF.png'),
(8, 'Tirana', 'Albanian', '008', 'lek', 'ALL', '(qindar (pl. qindarka))', 'Lek', 'Republic of Albania', 'AL', 'ALB', 'Albania', '150', '039', 0, '355', 'AL.png'),
(10, 'Antartica', 'of Antartica', '010', '', '', '', '', 'Antarctica', 'AQ', 'ATA', 'Antarctica', '', '', 0, '672', 'AQ.png'),
(12, 'Algiers', 'Algerian', '012', 'Algerian dinar', 'DZD', 'centime', 'DZD', 'People’s Democratic Republic of Algeria', 'DZ', 'DZA', 'Algeria', '002', '015', 0, '213', 'DZ.png'),
(16, 'Pago Pago', 'American Samoan', '016', 'US dollar', 'USD', 'cent', '$', 'Territory of American', 'AS', 'ASM', 'American Samoa', '009', '061', 0, '1', 'AS.png'),
(20, 'Andorra la Vella', 'Andorran', '020', 'euro', 'EUR', 'cent', '€', 'Principality of Andorra', 'AD', 'AND', 'Andorra', '150', '039', 0, '376', 'AD.png'),
(24, 'Luanda', 'Angolan', '024', 'kwanza', 'AOA', 'cêntimo', 'Kz', 'Republic of Angola', 'AO', 'AGO', 'Angola', '002', '017', 0, '244', 'AO.png'),
(28, 'St John’s', 'of Antigua and Barbuda', '028', 'East Caribbean dollar', 'XCD', 'cent', '$', 'Antigua and Barbuda', 'AG', 'ATG', 'Antigua and Barbuda', '019', '029', 0, '1', 'AG.png'),
(31, 'Baku', 'Azerbaijani', '031', 'Azerbaijani manat', 'AZN', 'kepik (inv.)', 'ман', 'Republic of Azerbaijan', 'AZ', 'AZE', 'Azerbaijan', '142', '145', 0, '994', 'AZ.png'),
(32, 'Buenos Aires', 'Argentinian', '032', 'Argentine peso', 'ARS', 'centavo', '$', 'Argentine Republic', 'AR', 'ARG', 'Argentina', '019', '005', 0, '54', 'AR.png'),
(36, 'Canberra', 'Australian', '036', 'Australian dollar', 'AUD', 'cent', '$', 'Commonwealth of Australia', 'AU', 'AUS', 'Australia', '009', '053', 0, '61', 'AU.png'),
(40, 'Vienna', 'Austrian', '040', 'euro', 'EUR', 'cent', '€', 'Republic of Austria', 'AT', 'AUT', 'Austria', '150', '155', 1, '43', 'AT.png'),
(44, 'Nassau', 'Bahamian', '044', 'Bahamian dollar', 'BSD', 'cent', '$', 'Commonwealth of the Bahamas', 'BS', 'BHS', 'Bahamas', '019', '029', 0, '1', 'BS.png'),
(48, 'Manama', 'Bahraini', '048', 'Bahraini dinar', 'BHD', 'fils (inv.)', 'BHD', 'Kingdom of Bahrain', 'BH', 'BHR', 'Bahrain', '142', '145', 0, '973', 'BH.png'),
(50, 'Dhaka', 'Bangladeshi', '050', 'taka (inv.)', 'BDT', 'poisha (inv.)', 'BDT', 'People’s Republic of Bangladesh', 'BD', 'BGD', 'Bangladesh', '142', '034', 0, '880', 'BD.png'),
(51, 'Yerevan', 'Armenian', '051', 'dram (inv.)', 'AMD', 'luma', 'AMD', 'Republic of Armenia', 'AM', 'ARM', 'Armenia', '142', '145', 0, '374', 'AM.png'),
(52, 'Bridgetown', 'Barbadian', '052', 'Barbados dollar', 'BBD', 'cent', '$', 'Barbados', 'BB', 'BRB', 'Barbados', '019', '029', 0, '1', 'BB.png'),
(56, 'Brussels', 'Belgian', '056', 'euro', 'EUR', 'cent', '€', 'Kingdom of Belgium', 'BE', 'BEL', 'Belgium', '150', '155', 1, '32', 'BE.png'),
(60, 'Hamilton', 'Bermudian', '060', 'Bermuda dollar', 'BMD', 'cent', '$', 'Bermuda', 'BM', 'BMU', 'Bermuda', '019', '021', 0, '1', 'BM.png'),
(64, 'Thimphu', 'Bhutanese', '064', 'ngultrum (inv.)', 'BTN', 'chhetrum (inv.)', 'BTN', 'Kingdom of Bhutan', 'BT', 'BTN', 'Bhutan', '142', '034', 0, '975', 'BT.png'),
(68, 'Sucre (BO1)', 'Bolivian', '068', 'boliviano', 'BOB', 'centavo', '$b', 'Plurinational State of Bolivia', 'BO', 'BOL', 'Bolivia, Plurinational State of', '019', '005', 0, '591', 'BO.png'),
(70, 'Sarajevo', 'of Bosnia and Herzegovina', '070', 'convertible mark', 'BAM', 'fening', 'KM', 'Bosnia and Herzegovina', 'BA', 'BIH', 'Bosnia and Herzegovina', '150', '039', 0, '387', 'BA.png'),
(72, 'Gaborone', 'Botswanan', '072', 'pula (inv.)', 'BWP', 'thebe (inv.)', 'P', 'Republic of Botswana', 'BW', 'BWA', 'Botswana', '002', '018', 0, '267', 'BW.png'),
(74, 'Bouvet island', 'of Bouvet island', '074', '', '', '', 'kr', 'Bouvet Island', 'BV', 'BVT', 'Bouvet Island', '', '', 0, '47', 'BV.png'),
(76, 'Brasilia', 'Brazilian', '076', 'real (pl. reais)', 'BRL', 'centavo', 'R$', 'Federative Republic of Brazil', 'BR', 'BRA', 'Brazil', '019', '005', 0, '55', 'BR.png'),
(84, 'Belmopan', 'Belizean', '084', 'Belize dollar', 'BZD', 'cent', 'BZ$', 'Belize', 'BZ', 'BLZ', 'Belize', '019', '013', 0, '501', 'BZ.png'),
(86, 'Diego Garcia', 'Changosian', '086', 'US dollar', 'USD', 'cent', '$', 'British Indian Ocean Territory', 'IO', 'IOT', 'British Indian Ocean Territory', '', '', 0, '246', 'IO.png'),
(90, 'Honiara', 'Solomon Islander', '090', 'Solomon Islands dollar', 'SBD', 'cent', '$', 'Solomon Islands', 'SB', 'SLB', 'Solomon Islands', '009', '054', 0, '677', 'SB.png'),
(92, 'Road Town', 'British Virgin Islander;', '092', 'US dollar', 'USD', 'cent', '$', 'British Virgin Islands', 'VG', 'VGB', 'Virgin Islands, British', '019', '029', 0, '1', 'VG.png'),
(96, 'Bandar Seri Begawan', 'Bruneian', '096', 'Brunei dollar', 'BND', 'sen (inv.)', '$', 'Brunei Darussalam', 'BN', 'BRN', 'Brunei Darussalam', '142', '035', 0, '673', 'BN.png'),
(100, 'Sofia', 'Bulgarian', '100', 'lev (pl. leva)', 'BGN', 'stotinka', 'лв', 'Republic of Bulgaria', 'BG', 'BGR', 'Bulgaria', '150', '151', 1, '359', 'BG.png'),
(104, 'Yangon', 'Burmese', '104', 'kyat', 'MMK', 'pya', 'K', 'Union of Myanmar/', 'MM', 'MMR', 'Myanmar', '142', '035', 0, '95', 'MM.png'),
(108, 'Bujumbura', 'Burundian', '108', 'Burundi franc', 'BIF', 'centime', 'BIF', 'Republic of Burundi', 'BI', 'BDI', 'Burundi', '002', '014', 0, '257', 'BI.png'),
(112, 'Minsk', 'Belarusian', '112', 'Belarusian rouble', 'BYR', 'kopek', 'p.', 'Republic of Belarus', 'BY', 'BLR', 'Belarus', '150', '151', 0, '375', 'BY.png'),
(116, 'Phnom Penh', 'Cambodian', '116', 'riel', 'KHR', 'sen (inv.)', '៛', 'Kingdom of Cambodia', 'KH', 'KHM', 'Cambodia', '142', '035', 0, '855', 'KH.png'),
(120, 'Yaoundé', 'Cameroonian', '120', 'CFA franc (BEAC)', 'XAF', 'centime', 'FCF', 'Republic of Cameroon', 'CM', 'CMR', 'Cameroon', '002', '017', 0, '237', 'CM.png'),
(124, 'Ottawa', 'Canadian', '124', 'Canadian dollar', 'CAD', 'cent', '$', 'Canada', 'CA', 'CAN', 'Canada', '019', '021', 0, '1', 'CA.png'),
(132, 'Praia', 'Cape Verdean', '132', 'Cape Verde escudo', 'CVE', 'centavo', 'CVE', 'Republic of Cape Verde', 'CV', 'CPV', 'Cape Verde', '002', '011', 0, '238', 'CV.png'),
(136, 'George Town', 'Caymanian', '136', 'Cayman Islands dollar', 'KYD', 'cent', '$', 'Cayman Islands', 'KY', 'CYM', 'Cayman Islands', '019', '029', 0, '1', 'KY.png'),
(140, 'Bangui', 'Central African', '140', 'CFA franc (BEAC)', 'XAF', 'centime', 'CFA', 'Central African Republic', 'CF', 'CAF', 'Central African Republic', '002', '017', 0, '236', 'CF.png'),
(144, 'Colombo', 'Sri Lankan', '144', 'Sri Lankan rupee', 'LKR', 'cent', '₨', 'Democratic Socialist Republic of Sri Lanka', 'LK', 'LKA', 'Sri Lanka', '142', '034', 0, '94', 'LK.png'),
(148, 'N’Djamena', 'Chadian', '148', 'CFA franc (BEAC)', 'XAF', 'centime', 'XAF', 'Republic of Chad', 'TD', 'TCD', 'Chad', '002', '017', 0, '235', 'TD.png'),
(152, 'Santiago', 'Chilean', '152', 'Chilean peso', 'CLP', 'centavo', 'CLP', 'Republic of Chile', 'CL', 'CHL', 'Chile', '019', '005', 0, '56', 'CL.png'),
(156, 'Beijing', 'Chinese', '156', 'renminbi-yuan (inv.)', 'CNY', 'jiao (10)', '¥', 'People’s Republic of China', 'CN', 'CHN', 'China', '142', '030', 0, '86', 'CN.png'),
(158, 'Taipei', 'Taiwanese', '158', 'new Taiwan dollar', 'TWD', 'fen (inv.)', 'NT$', 'Republic of China, Taiwan (TW1)', 'TW', 'TWN', 'Taiwan, Province of China', '142', '030', 0, '886', 'TW.png'),
(162, 'Flying Fish Cove', 'Christmas Islander', '162', 'Australian dollar', 'AUD', 'cent', '$', 'Christmas Island Territory', 'CX', 'CXR', 'Christmas Island', '', '', 0, '61', 'CX.png'),
(166, 'Bantam', 'Cocos Islander', '166', 'Australian dollar', 'AUD', 'cent', '$', 'Territory of Cocos (Keeling) Islands', 'CC', 'CCK', 'Cocos (Keeling) Islands', '', '', 0, '61', 'CC.png'),
(170, 'Santa Fe de Bogotá', 'Colombian', '170', 'Colombian peso', 'COP', 'centavo', '$', 'Republic of Colombia', 'CO', 'COL', 'Colombia', '019', '005', 0, '57', 'CO.png'),
(174, 'Moroni', 'Comorian', '174', 'Comorian franc', 'KMF', '', 'KMF', 'Union of the Comoros', 'KM', 'COM', 'Comoros', '002', '014', 0, '269', 'KM.png'),
(175, 'Mamoudzou', 'Mahorais', '175', 'euro', 'EUR', 'cent', '€', 'Departmental Collectivity of Mayotte', 'YT', 'MYT', 'Mayotte', '002', '014', 0, '262', 'YT.png'),
(178, 'Brazzaville', 'Congolese', '178', 'CFA franc (BEAC)', 'XAF', 'centime', 'FCF', 'Republic of the Congo', 'CG', 'COG', 'Congo', '002', '017', 0, '242', 'CG.png'),
(180, 'Kinshasa', 'Congolese', '180', 'Congolese franc', 'CDF', 'centime', 'CDF', 'Democratic Republic of the Congo', 'CD', 'COD', 'Congo, the Democratic Republic of the', '002', '017', 0, '243', 'CD.png'),
(184, 'Avarua', 'Cook Islander', '184', 'New Zealand dollar', 'NZD', 'cent', '$', 'Cook Islands', 'CK', 'COK', 'Cook Islands', '009', '061', 0, '682', 'CK.png'),
(188, 'San José', 'Costa Rican', '188', 'Costa Rican colón (pl. colones)', 'CRC', 'céntimo', '₡', 'Republic of Costa Rica', 'CR', 'CRI', 'Costa Rica', '019', '013', 0, '506', 'CR.png'),
(191, 'Zagreb', 'Croatian', '191', 'kuna (inv.)', 'HRK', 'lipa (inv.)', 'kn', 'Republic of Croatia', 'HR', 'HRV', 'Croatia', '150', '039', 1, '385', 'HR.png'),
(192, 'Havana', 'Cuban', '192', 'Cuban peso', 'CUP', 'centavo', '₱', 'Republic of Cuba', 'CU', 'CUB', 'Cuba', '019', '029', 0, '53', 'CU.png'),
(196, 'Nicosia', 'Cypriot', '196', 'euro', 'EUR', 'cent', 'CYP', 'Republic of Cyprus', 'CY', 'CYP', 'Cyprus', '142', '145', 1, '357', 'CY.png'),
(203, 'Prague', 'Czech', '203', 'Czech koruna (pl. koruny)', 'CZK', 'halér', 'Kč', 'Czech Republic', 'CZ', 'CZE', 'Czech Republic', '150', '151', 1, '420', 'CZ.png'),
(204, 'Porto Novo (BJ1)', 'Beninese', '204', 'CFA franc (BCEAO)', 'XOF', 'centime', 'XOF', 'Republic of Benin', 'BJ', 'BEN', 'Benin', '002', '011', 0, '229', 'BJ.png'),
(208, 'Copenhagen', 'Danish', '208', 'Danish krone', 'DKK', 'øre (inv.)', 'kr', 'Kingdom of Denmark', 'DK', 'DNK', 'Denmark', '150', '154', 1, '45', 'DK.png'),
(212, 'Roseau', 'Dominican', '212', 'East Caribbean dollar', 'XCD', 'cent', '$', 'Commonwealth of Dominica', 'DM', 'DMA', 'Dominica', '019', '029', 0, '1', 'DM.png'),
(214, 'Santo Domingo', 'Dominican', '214', 'Dominican peso', 'DOP', 'centavo', 'RD$', 'Dominican Republic', 'DO', 'DOM', 'Dominican Republic', '019', '029', 0, '1', 'DO.png'),
(218, 'Quito', 'Ecuadorian', '218', 'US dollar', 'USD', 'cent', '$', 'Republic of Ecuador', 'EC', 'ECU', 'Ecuador', '019', '005', 0, '593', 'EC.png'),
(222, 'San Salvador', 'Salvadoran', '222', 'Salvadorian colón (pl. colones)', 'SVC', 'centavo', '$', 'Republic of El Salvador', 'SV', 'SLV', 'El Salvador', '019', '013', 0, '503', 'SV.png'),
(226, 'Malabo', 'Equatorial Guinean', '226', 'CFA franc (BEAC)', 'XAF', 'centime', 'FCF', 'Republic of Equatorial Guinea', 'GQ', 'GNQ', 'Equatorial Guinea', '002', '017', 0, '240', 'GQ.png'),
(231, 'Addis Ababa', 'Ethiopian', '231', 'birr (inv.)', 'ETB', 'cent', 'ETB', 'Federal Democratic Republic of Ethiopia', 'ET', 'ETH', 'Ethiopia', '002', '014', 0, '251', 'ET.png'),
(232, 'Asmara', 'Eritrean', '232', 'nakfa', 'ERN', 'cent', 'Nfk', 'State of Eritrea', 'ER', 'ERI', 'Eritrea', '002', '014', 0, '291', 'ER.png'),
(233, 'Tallinn', 'Estonian', '233', 'euro', 'EUR', 'cent', 'kr', 'Republic of Estonia', 'EE', 'EST', 'Estonia', '150', '154', 1, '372', 'EE.png'),
(234, 'Tórshavn', 'Faeroese', '234', 'Danish krone', 'DKK', 'øre (inv.)', 'kr', 'Faeroe Islands', 'FO', 'FRO', 'Faroe Islands', '150', '154', 0, '298', 'FO.png'),
(238, 'Stanley', 'Falkland Islander', '238', 'Falkland Islands pound', 'FKP', 'new penny', '£', 'Falkland Islands', 'FK', 'FLK', 'Falkland Islands (Malvinas)', '019', '005', 0, '500', 'FK.png'),
(239, 'King Edward Point (Grytviken)', 'of South Georgia and the South Sandwich Islands', '239', '', '', '', '£', 'South Georgia and the South Sandwich Islands', 'GS', 'SGS', 'South Georgia and the South Sandwich Islands', '', '', 0, '44', 'GS.png'),
(242, 'Suva', 'Fijian', '242', 'Fiji dollar', 'FJD', 'cent', '$', 'Republic of Fiji', 'FJ', 'FJI', 'Fiji', '009', '054', 0, '679', 'FJ.png'),
(246, 'Helsinki', 'Finnish', '246', 'euro', 'EUR', 'cent', '€', 'Republic of Finland', 'FI', 'FIN', 'Finland', '150', '154', 1, '358', 'FI.png'),
(248, 'Mariehamn', 'Åland Islander', '248', 'euro', 'EUR', 'cent', NULL, 'Åland Islands', 'AX', 'ALA', 'Åland Islands', '150', '154', 0, '358', NULL),
(250, 'Paris', 'French', '250', 'euro', 'EUR', 'cent', '€', 'French Republic', 'FR', 'FRA', 'France', '150', '155', 1, '33', 'FR.png'),
(254, 'Cayenne', 'Guianese', '254', 'euro', 'EUR', 'cent', '€', 'French Guiana', 'GF', 'GUF', 'French Guiana', '019', '005', 0, '594', 'GF.png'),
(258, 'Papeete', 'Polynesian', '258', 'CFP franc', 'XPF', 'centime', 'XPF', 'French Polynesia', 'PF', 'PYF', 'French Polynesia', '009', '061', 0, '689', 'PF.png'),
(260, 'Port-aux-Francais', 'of French Southern and Antarctic Lands', '260', 'euro', 'EUR', 'cent', '€', 'French Southern and Antarctic Lands', 'TF', 'ATF', 'French Southern Territories', '', '', 0, '33', 'TF.png'),
(262, 'Djibouti', 'Djiboutian', '262', 'Djibouti franc', 'DJF', '', 'DJF', 'Republic of Djibouti', 'DJ', 'DJI', 'Djibouti', '002', '014', 0, '253', 'DJ.png'),
(266, 'Libreville', 'Gabonese', '266', 'CFA franc (BEAC)', 'XAF', 'centime', 'FCF', 'Gabonese Republic', 'GA', 'GAB', 'Gabon', '002', '017', 0, '241', 'GA.png'),
(268, 'Tbilisi', 'Georgian', '268', 'lari', 'GEL', 'tetri (inv.)', 'GEL', 'Georgia', 'GE', 'GEO', 'Georgia', '142', '145', 0, '995', 'GE.png'),
(270, 'Banjul', 'Gambian', '270', 'dalasi (inv.)', 'GMD', 'butut', 'D', 'Republic of the Gambia', 'GM', 'GMB', 'Gambia', '002', '011', 0, '220', 'GM.png'),
(275, NULL, 'Palestinian', '275', NULL, NULL, NULL, '₪', NULL, 'PS', 'PSE', 'Palestinian Territory, Occupied', '142', '145', 0, '970', 'PS.png'),
(276, 'Berlin', 'German', '276', 'euro', 'EUR', 'cent', '€', 'Federal Republic of Germany', 'DE', 'DEU', 'Germany', '150', '155', 1, '49', 'DE.png'),
(288, 'Accra', 'Ghanaian', '288', 'Ghana cedi', 'GHS', 'pesewa', '¢', 'Republic of Ghana', 'GH', 'GHA', 'Ghana', '002', '011', 0, '233', 'GH.png'),
(292, 'Gibraltar', 'Gibraltarian', '292', 'Gibraltar pound', 'GIP', 'penny', '£', 'Gibraltar', 'GI', 'GIB', 'Gibraltar', '150', '039', 0, '350', 'GI.png'),
(296, 'Tarawa', 'Kiribatian', '296', 'Australian dollar', 'AUD', 'cent', '$', 'Republic of Kiribati', 'KI', 'KIR', 'Kiribati', '009', '057', 0, '686', 'KI.png'),
(300, 'Athens', 'Greek', '300', 'euro', 'EUR', 'cent', '€', 'Hellenic Republic', 'GR', 'GRC', 'Greece', '150', '039', 1, '30', 'GR.png'),
(304, 'Nuuk', 'Greenlander', '304', 'Danish krone', 'DKK', 'øre (inv.)', 'kr', 'Greenland', 'GL', 'GRL', 'Greenland', '019', '021', 0, '299', 'GL.png'),
(308, 'St George’s', 'Grenadian', '308', 'East Caribbean dollar', 'XCD', 'cent', '$', 'Grenada', 'GD', 'GRD', 'Grenada', '019', '029', 0, '1', 'GD.png'),
(312, 'Basse Terre', 'Guadeloupean', '312', 'euro', 'EUR', 'cent', '€', 'Guadeloupe', 'GP', 'GLP', 'Guadeloupe', '019', '029', 0, '590', 'GP.png'),
(316, 'Agaña (Hagåtña)', 'Guamanian', '316', 'US dollar', 'USD', 'cent', '$', 'Territory of Guam', 'GU', 'GUM', 'Guam', '009', '057', 0, '1', 'GU.png'),
(320, 'Guatemala City', 'Guatemalan', '320', 'quetzal (pl. quetzales)', 'GTQ', 'centavo', 'Q', 'Republic of Guatemala', 'GT', 'GTM', 'Guatemala', '019', '013', 0, '502', 'GT.png'),
(324, 'Conakry', 'Guinean', '324', 'Guinean franc', 'GNF', '', 'GNF', 'Republic of Guinea', 'GN', 'GIN', 'Guinea', '002', '011', 0, '224', 'GN.png'),
(328, 'Georgetown', 'Guyanese', '328', 'Guyana dollar', 'GYD', 'cent', '$', 'Cooperative Republic of Guyana', 'GY', 'GUY', 'Guyana', '019', '005', 0, '592', 'GY.png'),
(332, 'Port-au-Prince', 'Haitian', '332', 'gourde', 'HTG', 'centime', 'G', 'Republic of Haiti', 'HT', 'HTI', 'Haiti', '019', '029', 0, '509', 'HT.png'),
(334, 'Territory of Heard Island and McDonald Islands', 'of Territory of Heard Island and McDonald Islands', '334', '', '', '', '$', 'Territory of Heard Island and McDonald Islands', 'HM', 'HMD', 'Heard Island and McDonald Islands', '', '', 0, '61', 'HM.png'),
(336, 'Vatican City', 'of the Holy See/of the Vatican', '336', 'euro', 'EUR', 'cent', '€', 'the Holy See/ Vatican City State', 'VA', 'VAT', 'Holy See (Vatican City State)', '150', '039', 0, '39', 'VA.png'),
(340, 'Tegucigalpa', 'Honduran', '340', 'lempira', 'HNL', 'centavo', 'L', 'Republic of Honduras', 'HN', 'HND', 'Honduras', '019', '013', 0, '504', 'HN.png'),
(344, '(HK3)', 'Hong Kong Chinese', '344', 'Hong Kong dollar', 'HKD', 'cent', '$', 'Hong Kong Special Administrative Region of the People’s Republic of China (HK2)', 'HK', 'HKG', 'Hong Kong', '142', '030', 0, '852', 'HK.png'),
(348, 'Budapest', 'Hungarian', '348', 'forint (inv.)', 'HUF', '(fillér (inv.))', 'Ft', 'Republic of Hungary', 'HU', 'HUN', 'Hungary', '150', '151', 1, '36', 'HU.png'),
(352, 'Reykjavik', 'Icelander', '352', 'króna (pl. krónur)', 'ISK', '', 'kr', 'Republic of Iceland', 'IS', 'ISL', 'Iceland', '150', '154', 0, '354', 'IS.png'),
(356, 'New Delhi', 'Indian', '356', 'Indian rupee', 'INR', 'paisa', '₹', 'Republic of India', 'IN', 'IND', 'India', '142', '034', 0, '91', 'IN.png'),
(360, 'Jakarta', 'Indonesian', '360', 'Indonesian rupiah (inv.)', 'IDR', 'sen (inv.)', 'Rp', 'Republic of Indonesia', 'ID', 'IDN', 'Indonesia', '142', '035', 0, '62', 'ID.png'),
(364, 'Tehran', 'Iranian', '364', 'Iranian rial', 'IRR', '(dinar) (IR1)', '﷼', 'Islamic Republic of Iran', 'IR', 'IRN', 'Iran, Islamic Republic of', '142', '034', 0, '98', 'IR.png'),
(368, 'Baghdad', 'Iraqi', '368', 'Iraqi dinar', 'IQD', 'fils (inv.)', 'IQD', 'Republic of Iraq', 'IQ', 'IRQ', 'Iraq', '142', '145', 0, '964', 'IQ.png'),
(372, 'Dublin', 'Irish', '372', 'euro', 'EUR', 'cent', '€', 'Ireland (IE1)', 'IE', 'IRL', 'Ireland', '150', '154', 1, '353', 'IE.png'),
(376, '(IL1)', 'Israeli', '376', 'shekel', 'ILS', 'agora', '₪', 'State of Israel', 'IL', 'ISR', 'Israel', '142', '145', 0, '972', 'IL.png'),
(380, 'Rome', 'Italian', '380', 'euro', 'EUR', 'cent', '€', 'Italian Republic', 'IT', 'ITA', 'Italy', '150', '039', 1, '39', 'IT.png'),
(384, 'Yamoussoukro (CI1)', 'Ivorian', '384', 'CFA franc (BCEAO)', 'XOF', 'centime', 'XOF', 'Republic of Côte d’Ivoire', 'CI', 'CIV', 'Côte d\'Ivoire', '002', '011', 0, '225', 'CI.png'),
(388, 'Kingston', 'Jamaican', '388', 'Jamaica dollar', 'JMD', 'cent', '$', 'Jamaica', 'JM', 'JAM', 'Jamaica', '019', '029', 0, '1', 'JM.png'),
(392, 'Tokyo', 'Japanese', '392', 'yen (inv.)', 'JPY', '(sen (inv.)) (JP1)', '¥', 'Japan', 'JP', 'JPN', 'Japan', '142', '030', 0, '81', 'JP.png'),
(398, 'Astana', 'Kazakh', '398', 'tenge (inv.)', 'KZT', 'tiyn', 'лв', 'Republic of Kazakhstan', 'KZ', 'KAZ', 'Kazakhstan', '142', '143', 0, '7', 'KZ.png'),
(400, 'Amman', 'Jordanian', '400', 'Jordanian dinar', 'JOD', '100 qirsh', 'JOD', 'Hashemite Kingdom of Jordan', 'JO', 'JOR', 'Jordan', '142', '145', 0, '962', 'JO.png'),
(404, 'Nairobi', 'Kenyan', '404', 'Kenyan shilling', 'KES', 'cent', 'KES', 'Republic of Kenya', 'KE', 'KEN', 'Kenya', '002', '014', 0, '254', 'KE.png'),
(408, 'Pyongyang', 'North Korean', '408', 'North Korean won (inv.)', 'KPW', 'chun (inv.)', '₩', 'Democratic People’s Republic of Korea', 'KP', 'PRK', 'Korea, Democratic People\'s Republic of', '142', '030', 0, '850', 'KP.png'),
(410, 'Seoul', 'South Korean', '410', 'South Korean won (inv.)', 'KRW', '(chun (inv.))', '₩', 'Republic of Korea', 'KR', 'KOR', 'Korea, Republic of', '142', '030', 0, '82', 'KR.png'),
(414, 'Kuwait City', 'Kuwaiti', '414', 'Kuwaiti dinar', 'KWD', 'fils (inv.)', 'KWD', 'State of Kuwait', 'KW', 'KWT', 'Kuwait', '142', '145', 0, '965', 'KW.png'),
(417, 'Bishkek', 'Kyrgyz', '417', 'som', 'KGS', 'tyiyn', 'лв', 'Kyrgyz Republic', 'KG', 'KGZ', 'Kyrgyzstan', '142', '143', 0, '996', 'KG.png'),
(418, 'Vientiane', 'Lao', '418', 'kip (inv.)', 'LAK', '(at (inv.))', '₭', 'Lao People’s Democratic Republic', 'LA', 'LAO', 'Lao People\'s Democratic Republic', '142', '035', 0, '856', 'LA.png'),
(422, 'Beirut', 'Lebanese', '422', 'Lebanese pound', 'LBP', '(piastre)', '£', 'Lebanese Republic', 'LB', 'LBN', 'Lebanon', '142', '145', 0, '961', 'LB.png'),
(426, 'Maseru', 'Basotho', '426', 'loti (pl. maloti)', 'LSL', 'sente', 'L', 'Kingdom of Lesotho', 'LS', 'LSO', 'Lesotho', '002', '018', 0, '266', 'LS.png'),
(428, 'Riga', 'Latvian', '428', 'euro', 'EUR', 'cent', 'Ls', 'Republic of Latvia', 'LV', 'LVA', 'Latvia', '150', '154', 1, '371', 'LV.png'),
(430, 'Monrovia', 'Liberian', '430', 'Liberian dollar', 'LRD', 'cent', '$', 'Republic of Liberia', 'LR', 'LBR', 'Liberia', '002', '011', 0, '231', 'LR.png'),
(434, 'Tripoli', 'Libyan', '434', 'Libyan dinar', 'LYD', 'dirham', 'LYD', 'Socialist People’s Libyan Arab Jamahiriya', 'LY', 'LBY', 'Libya', '002', '015', 0, '218', 'LY.png'),
(438, 'Vaduz', 'Liechtensteiner', '438', 'Swiss franc', 'CHF', 'centime', 'CHF', 'Principality of Liechtenstein', 'LI', 'LIE', 'Liechtenstein', '150', '155', 0, '423', 'LI.png'),
(440, 'Vilnius', 'Lithuanian', '440', 'euro', 'EUR', 'cent', 'Lt', 'Republic of Lithuania', 'LT', 'LTU', 'Lithuania', '150', '154', 1, '370', 'LT.png'),
(442, 'Luxembourg', 'Luxembourger', '442', 'euro', 'EUR', 'cent', '€', 'Grand Duchy of Luxembourg', 'LU', 'LUX', 'Luxembourg', '150', '155', 1, '352', 'LU.png'),
(446, 'Macao (MO3)', 'Macanese', '446', 'pataca', 'MOP', 'avo', 'MOP', 'Macao Special Administrative Region of the People’s Republic of China (MO2)', 'MO', 'MAC', 'Macao', '142', '030', 0, '853', 'MO.png'),
(450, 'Antananarivo', 'Malagasy', '450', 'ariary', 'MGA', 'iraimbilanja (inv.)', 'MGA', 'Republic of Madagascar', 'MG', 'MDG', 'Madagascar', '002', '014', 0, '261', 'MG.png'),
(454, 'Lilongwe', 'Malawian', '454', 'Malawian kwacha (inv.)', 'MWK', 'tambala (inv.)', 'MK', 'Republic of Malawi', 'MW', 'MWI', 'Malawi', '002', '014', 0, '265', 'MW.png'),
(458, 'Kuala Lumpur (MY1)', 'Malaysian', '458', 'ringgit (inv.)', 'MYR', 'sen (inv.)', 'RM', 'Malaysia', 'MY', 'MYS', 'Malaysia', '142', '035', 0, '60', 'MY.png'),
(462, 'Malé', 'Maldivian', '462', 'rufiyaa', 'MVR', 'laari (inv.)', 'Rf', 'Republic of Maldives', 'MV', 'MDV', 'Maldives', '142', '034', 0, '960', 'MV.png'),
(466, 'Bamako', 'Malian', '466', 'CFA franc (BCEAO)', 'XOF', 'centime', 'XOF', 'Republic of Mali', 'ML', 'MLI', 'Mali', '002', '011', 0, '223', 'ML.png'),
(470, 'Valletta', 'Maltese', '470', 'euro', 'EUR', 'cent', 'MTL', 'Republic of Malta', 'MT', 'MLT', 'Malta', '150', '039', 1, '356', 'MT.png'),
(474, 'Fort-de-France', 'Martinican', '474', 'euro', 'EUR', 'cent', '€', 'Martinique', 'MQ', 'MTQ', 'Martinique', '019', '029', 0, '596', 'MQ.png'),
(478, 'Nouakchott', 'Mauritanian', '478', 'ouguiya', 'MRO', 'khoum', 'UM', 'Islamic Republic of Mauritania', 'MR', 'MRT', 'Mauritania', '002', '011', 0, '222', 'MR.png'),
(480, 'Port Louis', 'Mauritian', '480', 'Mauritian rupee', 'MUR', 'cent', '₨', 'Republic of Mauritius', 'MU', 'MUS', 'Mauritius', '002', '014', 0, '230', 'MU.png'),
(484, 'Mexico City', 'Mexican', '484', 'Mexican peso', 'MXN', 'centavo', '$', 'United Mexican States', 'MX', 'MEX', 'Mexico', '019', '013', 0, '52', 'MX.png'),
(492, 'Monaco', 'Monegasque', '492', 'euro', 'EUR', 'cent', '€', 'Principality of Monaco', 'MC', 'MCO', 'Monaco', '150', '155', 0, '377', 'MC.png'),
(496, 'Ulan Bator', 'Mongolian', '496', 'tugrik', 'MNT', 'möngö (inv.)', '₮', 'Mongolia', 'MN', 'MNG', 'Mongolia', '142', '030', 0, '976', 'MN.png'),
(498, 'Chisinau', 'Moldovan', '498', 'Moldovan leu (pl. lei)', 'MDL', 'ban', 'MDL', 'Republic of Moldova', 'MD', 'MDA', 'Moldova, Republic of', '150', '151', 0, '373', 'MD.png'),
(499, 'Podgorica', 'Montenegrin', '499', 'euro', 'EUR', 'cent', '€', 'Montenegro', 'ME', 'MNE', 'Montenegro', '150', '039', 0, '382', 'ME.png'),
(500, 'Plymouth (MS2)', 'Montserratian', '500', 'East Caribbean dollar', 'XCD', 'cent', '$', 'Montserrat', 'MS', 'MSR', 'Montserrat', '019', '029', 0, '1', 'MS.png'),
(504, 'Rabat', 'Moroccan', '504', 'Moroccan dirham', 'MAD', 'centime', 'MAD', 'Kingdom of Morocco', 'MA', 'MAR', 'Morocco', '002', '015', 0, '212', 'MA.png'),
(508, 'Maputo', 'Mozambican', '508', 'metical', 'MZN', 'centavo', 'MT', 'Republic of Mozambique', 'MZ', 'MOZ', 'Mozambique', '002', '014', 0, '258', 'MZ.png'),
(512, 'Muscat', 'Omani', '512', 'Omani rial', 'OMR', 'baiza', '﷼', 'Sultanate of Oman', 'OM', 'OMN', 'Oman', '142', '145', 0, '968', 'OM.png'),
(516, 'Windhoek', 'Namibian', '516', 'Namibian dollar', 'NAD', 'cent', '$', 'Republic of Namibia', 'NA', 'NAM', 'Namibia', '002', '018', 0, '264', 'NA.png'),
(520, 'Yaren', 'Nauruan', '520', 'Australian dollar', 'AUD', 'cent', '$', 'Republic of Nauru', 'NR', 'NRU', 'Nauru', '009', '057', 0, '674', 'NR.png'),
(524, 'Kathmandu', 'Nepalese', '524', 'Nepalese rupee', 'NPR', 'paisa (inv.)', '₨', 'Nepal', 'NP', 'NPL', 'Nepal', '142', '034', 0, '977', 'NP.png'),
(528, 'Amsterdam (NL2)', 'Dutch', '528', 'euro', 'EUR', 'cent', '€', 'Kingdom of the Netherlands', 'NL', 'NLD', 'Netherlands', '150', '155', 1, '31', 'NL.png'),
(531, 'Willemstad', 'Curaçaoan', '531', 'Netherlands Antillean guilder (CW1)', 'ANG', 'cent', NULL, 'Curaçao', 'CW', 'CUW', 'Curaçao', '019', '029', 0, '599', NULL),
(533, 'Oranjestad', 'Aruban', '533', 'Aruban guilder', 'AWG', 'cent', 'ƒ', 'Aruba', 'AW', 'ABW', 'Aruba', '019', '029', 0, '297', 'AW.png'),
(534, 'Philipsburg', 'Sint Maartener', '534', 'Netherlands Antillean guilder (SX1)', 'ANG', 'cent', NULL, 'Sint Maarten', 'SX', 'SXM', 'Sint Maarten (Dutch part)', '019', '029', 0, '721', NULL),
(535, NULL, 'of Bonaire, Sint Eustatius and Saba', '535', 'US dollar', 'USD', 'cent', NULL, NULL, 'BQ', 'BES', 'Bonaire, Sint Eustatius and Saba', '019', '029', 0, '599', NULL),
(540, 'Nouméa', 'New Caledonian', '540', 'CFP franc', 'XPF', 'centime', 'XPF', 'New Caledonia', 'NC', 'NCL', 'New Caledonia', '009', '054', 0, '687', 'NC.png'),
(548, 'Port Vila', 'Vanuatuan', '548', 'vatu (inv.)', 'VUV', '', 'Vt', 'Republic of Vanuatu', 'VU', 'VUT', 'Vanuatu', '009', '054', 0, '678', 'VU.png'),
(554, 'Wellington', 'New Zealander', '554', 'New Zealand dollar', 'NZD', 'cent', '$', 'New Zealand', 'NZ', 'NZL', 'New Zealand', '009', '053', 0, '64', 'NZ.png'),
(558, 'Managua', 'Nicaraguan', '558', 'córdoba oro', 'NIO', 'centavo', 'C$', 'Republic of Nicaragua', 'NI', 'NIC', 'Nicaragua', '019', '013', 0, '505', 'NI.png'),
(562, 'Niamey', 'Nigerien', '562', 'CFA franc (BCEAO)', 'XOF', 'centime', 'XOF', 'Republic of Niger', 'NE', 'NER', 'Niger', '002', '011', 0, '227', 'NE.png'),
(566, 'Abuja', 'Nigerian', '566', 'naira (inv.)', 'NGN', 'kobo (inv.)', '₦', 'Federal Republic of Nigeria', 'NG', 'NGA', 'Nigeria', '002', '011', 0, '234', 'NG.png'),
(570, 'Alofi', 'Niuean', '570', 'New Zealand dollar', 'NZD', 'cent', '$', 'Niue', 'NU', 'NIU', 'Niue', '009', '061', 0, '683', 'NU.png'),
(574, 'Kingston', 'Norfolk Islander', '574', 'Australian dollar', 'AUD', 'cent', '$', 'Territory of Norfolk Island', 'NF', 'NFK', 'Norfolk Island', '009', '053', 0, '672', 'NF.png'),
(578, 'Oslo', 'Norwegian', '578', 'Norwegian krone (pl. kroner)', 'NOK', 'øre (inv.)', 'kr', 'Kingdom of Norway', 'NO', 'NOR', 'Norway', '150', '154', 0, '47', 'NO.png'),
(580, 'Saipan', 'Northern Mariana Islander', '580', 'US dollar', 'USD', 'cent', '$', 'Commonwealth of the Northern Mariana Islands', 'MP', 'MNP', 'Northern Mariana Islands', '009', '057', 0, '1', 'MP.png'),
(581, 'United States Minor Outlying Islands', 'of United States Minor Outlying Islands', '581', 'US dollar', 'USD', 'cent', '$', 'United States Minor Outlying Islands', 'UM', 'UMI', 'United States Minor Outlying Islands', '', '', 0, '1', 'UM.png'),
(583, 'Palikir', 'Micronesian', '583', 'US dollar', 'USD', 'cent', '$', 'Federated States of Micronesia', 'FM', 'FSM', 'Micronesia, Federated States of', '009', '057', 0, '691', 'FM.png'),
(584, 'Majuro', 'Marshallese', '584', 'US dollar', 'USD', 'cent', '$', 'Republic of the Marshall Islands', 'MH', 'MHL', 'Marshall Islands', '009', '057', 0, '692', 'MH.png'),
(585, 'Melekeok', 'Palauan', '585', 'US dollar', 'USD', 'cent', '$', 'Republic of Palau', 'PW', 'PLW', 'Palau', '009', '057', 0, '680', 'PW.png'),
(586, 'Islamabad', 'Pakistani', '586', 'Pakistani rupee', 'PKR', 'paisa', '₨', 'Islamic Republic of Pakistan', 'PK', 'PAK', 'Pakistan', '142', '034', 0, '92', 'PK.png'),
(591, 'Panama City', 'Panamanian', '591', 'balboa', 'PAB', 'centésimo', 'B/.', 'Republic of Panama', 'PA', 'PAN', 'Panama', '019', '013', 0, '507', 'PA.png'),
(598, 'Port Moresby', 'Papua New Guinean', '598', 'kina (inv.)', 'PGK', 'toea (inv.)', 'PGK', 'Independent State of Papua New Guinea', 'PG', 'PNG', 'Papua New Guinea', '009', '054', 0, '675', 'PG.png'),
(600, 'Asunción', 'Paraguayan', '600', 'guaraní', 'PYG', 'céntimo', 'Gs', 'Republic of Paraguay', 'PY', 'PRY', 'Paraguay', '019', '005', 0, '595', 'PY.png'),
(604, 'Lima', 'Peruvian', '604', 'new sol', 'PEN', 'céntimo', 'S/.', 'Republic of Peru', 'PE', 'PER', 'Peru', '019', '005', 0, '51', 'PE.png'),
(608, 'Manila', 'Filipino', '608', 'Philippine peso', 'PHP', 'centavo', 'Php', 'Republic of the Philippines', 'PH', 'PHL', 'Philippines', '142', '035', 0, '63', 'PH.png'),
(612, 'Adamstown', 'Pitcairner', '612', 'New Zealand dollar', 'NZD', 'cent', '$', 'Pitcairn Islands', 'PN', 'PCN', 'Pitcairn', '009', '061', 0, '649', 'PN.png'),
(616, 'Warsaw', 'Polish', '616', 'zloty', 'PLN', 'grosz (pl. groszy)', 'zł', 'Republic of Poland', 'PL', 'POL', 'Poland', '150', '151', 1, '48', 'PL.png'),
(620, 'Lisbon', 'Portuguese', '620', 'euro', 'EUR', 'cent', '€', 'Portuguese Republic', 'PT', 'PRT', 'Portugal', '150', '039', 1, '351', 'PT.png'),
(624, 'Bissau', 'Guinea-Bissau national', '624', 'CFA franc (BCEAO)', 'XOF', 'centime', 'XOF', 'Republic of Guinea-Bissau', 'GW', 'GNB', 'Guinea-Bissau', '002', '011', 0, '245', 'GW.png'),
(626, 'Dili', 'East Timorese', '626', 'US dollar', 'USD', 'cent', '$', 'Democratic Republic of East Timor', 'TL', 'TLS', 'Timor-Leste', '142', '035', 0, '670', 'TL.png'),
(630, 'San Juan', 'Puerto Rican', '630', 'US dollar', 'USD', 'cent', '$', 'Commonwealth of Puerto Rico', 'PR', 'PRI', 'Puerto Rico', '019', '029', 0, '1', 'PR.png'),
(634, 'Doha', 'Qatari', '634', 'Qatari riyal', 'QAR', 'dirham', '﷼', 'State of Qatar', 'QA', 'QAT', 'Qatar', '142', '145', 0, '974', 'QA.png'),
(638, 'Saint-Denis', 'Reunionese', '638', 'euro', 'EUR', 'cent', '€', 'Réunion', 'RE', 'REU', 'Réunion', '002', '014', 0, '262', 'RE.png'),
(642, 'Bucharest', 'Romanian', '642', 'Romanian leu (pl. lei)', 'RON', 'ban (pl. bani)', 'lei', 'Romania', 'RO', 'ROU', 'Romania', '150', '151', 1, '40', 'RO.png'),
(643, 'Moscow', 'Russian', '643', 'Russian rouble', 'RUB', 'kopek', 'руб', 'Russian Federation', 'RU', 'RUS', 'Russian Federation', '150', '151', 0, '7', 'RU.png'),
(646, 'Kigali', 'Rwandan; Rwandese', '646', 'Rwandese franc', 'RWF', 'centime', 'RWF', 'Republic of Rwanda', 'RW', 'RWA', 'Rwanda', '002', '014', 0, '250', 'RW.png'),
(652, 'Gustavia', 'of Saint Barthélemy', '652', 'euro', 'EUR', 'cent', NULL, 'Collectivity of Saint Barthélemy', 'BL', 'BLM', 'Saint Barthélemy', '019', '029', 0, '590', NULL),
(654, 'Jamestown', 'Saint Helenian', '654', 'Saint Helena pound', 'SHP', 'penny', '£', 'Saint Helena, Ascension and Tristan da Cunha', 'SH', 'SHN', 'Saint Helena, Ascension and Tristan da Cunha', '002', '011', 0, '290', 'SH.png'),
(659, 'Basseterre', 'Kittsian; Nevisian', '659', 'East Caribbean dollar', 'XCD', 'cent', '$', 'Federation of Saint Kitts and Nevis', 'KN', 'KNA', 'Saint Kitts and Nevis', '019', '029', 0, '1', 'KN.png'),
(660, 'The Valley', 'Anguillan', '660', 'East Caribbean dollar', 'XCD', 'cent', '$', 'Anguilla', 'AI', 'AIA', 'Anguilla', '019', '029', 0, '1', 'AI.png'),
(662, 'Castries', 'Saint Lucian', '662', 'East Caribbean dollar', 'XCD', 'cent', '$', 'Saint Lucia', 'LC', 'LCA', 'Saint Lucia', '019', '029', 0, '1', 'LC.png'),
(663, 'Marigot', 'of Saint Martin', '663', 'euro', 'EUR', 'cent', NULL, 'Collectivity of Saint Martin', 'MF', 'MAF', 'Saint Martin (French part)', '019', '029', 0, '590', NULL),
(666, 'Saint-Pierre', 'St-Pierrais; Miquelonnais', '666', 'euro', 'EUR', 'cent', '€', 'Territorial Collectivity of Saint Pierre and Miquelon', 'PM', 'SPM', 'Saint Pierre and Miquelon', '019', '021', 0, '508', 'PM.png'),
(670, 'Kingstown', 'Vincentian', '670', 'East Caribbean dollar', 'XCD', 'cent', '$', 'Saint Vincent and the Grenadines', 'VC', 'VCT', 'Saint Vincent and the Grenadines', '019', '029', 0, '1', 'VC.png'),
(674, 'San Marino', 'San Marinese', '674', 'euro', 'EUR', 'cent', '€', 'Republic of San Marino', 'SM', 'SMR', 'San Marino', '150', '039', 0, '378', 'SM.png'),
(678, 'São Tomé', 'São Toméan', '678', 'dobra', 'STD', 'centavo', 'Db', 'Democratic Republic of São Tomé and Príncipe', 'ST', 'STP', 'Sao Tome and Principe', '002', '017', 0, '239', 'ST.png'),
(682, 'Riyadh', 'Saudi Arabian', '682', 'riyal', 'SAR', 'halala', '﷼', 'Kingdom of Saudi Arabia', 'SA', 'SAU', 'Saudi Arabia', '142', '145', 0, '966', 'SA.png'),
(686, 'Dakar', 'Senegalese', '686', 'CFA franc (BCEAO)', 'XOF', 'centime', 'XOF', 'Republic of Senegal', 'SN', 'SEN', 'Senegal', '002', '011', 0, '221', 'SN.png'),
(688, 'Belgrade', 'Serb', '688', 'Serbian dinar', 'RSD', 'para (inv.)', NULL, 'Republic of Serbia', 'RS', 'SRB', 'Serbia', '150', '039', 0, '381', NULL),
(690, 'Victoria', 'Seychellois', '690', 'Seychelles rupee', 'SCR', 'cent', '₨', 'Republic of Seychelles', 'SC', 'SYC', 'Seychelles', '002', '014', 0, '248', 'SC.png'),
(694, 'Freetown', 'Sierra Leonean', '694', 'leone', 'SLL', 'cent', 'Le', 'Republic of Sierra Leone', 'SL', 'SLE', 'Sierra Leone', '002', '011', 0, '232', 'SL.png'),
(702, 'Singapore', 'Singaporean', '702', 'Singapore dollar', 'SGD', 'cent', '$', 'Republic of Singapore', 'SG', 'SGP', 'Singapore', '142', '035', 0, '65', 'SG.png'),
(703, 'Bratislava', 'Slovak', '703', 'euro', 'EUR', 'cent', 'Sk', 'Slovak Republic', 'SK', 'SVK', 'Slovakia', '150', '151', 1, '421', 'SK.png'),
(704, 'Hanoi', 'Vietnamese', '704', 'dong', 'VND', '(10 hào', '₫', 'Socialist Republic of Vietnam', 'VN', 'VNM', 'Viet Nam', '142', '035', 0, '84', 'VN.png'),
(705, 'Ljubljana', 'Slovene', '705', 'euro', 'EUR', 'cent', '€', 'Republic of Slovenia', 'SI', 'SVN', 'Slovenia', '150', '039', 1, '386', 'SI.png'),
(706, 'Mogadishu', 'Somali', '706', 'Somali shilling', 'SOS', 'cent', 'S', 'Somali Republic', 'SO', 'SOM', 'Somalia', '002', '014', 0, '252', 'SO.png'),
(710, 'Pretoria (ZA1)', 'South African', '710', 'rand', 'ZAR', 'cent', 'R', 'Republic of South Africa', 'ZA', 'ZAF', 'South Africa', '002', '018', 0, '27', 'ZA.png'),
(716, 'Harare', 'Zimbabwean', '716', 'Zimbabwe dollar (ZW1)', 'ZWL', 'cent', 'Z$', 'Republic of Zimbabwe', 'ZW', 'ZWE', 'Zimbabwe', '002', '014', 0, '263', 'ZW.png'),
(724, 'Madrid', 'Spaniard', '724', 'euro', 'EUR', 'cent', '€', 'Kingdom of Spain', 'ES', 'ESP', 'Spain', '150', '039', 1, '34', 'ES.png'),
(728, 'Juba', 'South Sudanese', '728', 'South Sudanese pound', 'SSP', 'piaster', NULL, 'Republic of South Sudan', 'SS', 'SSD', 'South Sudan', '002', '015', 0, '211', NULL),
(729, 'Khartoum', 'Sudanese', '729', 'Sudanese pound', 'SDG', 'piastre', NULL, 'Republic of the Sudan', 'SD', 'SDN', 'Sudan', '002', '015', 0, '249', NULL),
(732, 'Al aaiun', 'Sahrawi', '732', 'Moroccan dirham', 'MAD', 'centime', 'MAD', 'Western Sahara', 'EH', 'ESH', 'Western Sahara', '002', '015', 0, '212', 'EH.png'),
(740, 'Paramaribo', 'Surinamese', '740', 'Surinamese dollar', 'SRD', 'cent', '$', 'Republic of Suriname', 'SR', 'SUR', 'Suriname', '019', '005', 0, '597', 'SR.png'),
(744, 'Longyearbyen', 'of Svalbard', '744', 'Norwegian krone (pl. kroner)', 'NOK', 'øre (inv.)', 'kr', 'Svalbard and Jan Mayen', 'SJ', 'SJM', 'Svalbard and Jan Mayen', '150', '154', 0, '47', 'SJ.png'),
(748, 'Mbabane', 'Swazi', '748', 'lilangeni', 'SZL', 'cent', 'SZL', 'Kingdom of Swaziland', 'SZ', 'SWZ', 'Swaziland', '002', '018', 0, '268', 'SZ.png'),
(752, 'Stockholm', 'Swedish', '752', 'krona (pl. kronor)', 'SEK', 'öre (inv.)', 'kr', 'Kingdom of Sweden', 'SE', 'SWE', 'Sweden', '150', '154', 1, '46', 'SE.png'),
(756, 'Berne', 'Swiss', '756', 'Swiss franc', 'CHF', 'centime', 'CHF', 'Swiss Confederation', 'CH', 'CHE', 'Switzerland', '150', '155', 0, '41', 'CH.png'),
(760, 'Damascus', 'Syrian', '760', 'Syrian pound', 'SYP', 'piastre', '£', 'Syrian Arab Republic', 'SY', 'SYR', 'Syrian Arab Republic', '142', '145', 0, '963', 'SY.png'),
(762, 'Dushanbe', 'Tajik', '762', 'somoni', 'TJS', 'diram', 'TJS', 'Republic of Tajikistan', 'TJ', 'TJK', 'Tajikistan', '142', '143', 0, '992', 'TJ.png'),
(764, 'Bangkok', 'Thai', '764', 'baht (inv.)', 'THB', 'satang (inv.)', '฿', 'Kingdom of Thailand', 'TH', 'THA', 'Thailand', '142', '035', 0, '66', 'TH.png'),
(768, 'Lomé', 'Togolese', '768', 'CFA franc (BCEAO)', 'XOF', 'centime', 'XOF', 'Togolese Republic', 'TG', 'TGO', 'Togo', '002', '011', 0, '228', 'TG.png'),
(772, '(TK2)', 'Tokelauan', '772', 'New Zealand dollar', 'NZD', 'cent', '$', 'Tokelau', 'TK', 'TKL', 'Tokelau', '009', '061', 0, '690', 'TK.png'),
(776, 'Nuku’alofa', 'Tongan', '776', 'pa’anga (inv.)', 'TOP', 'seniti (inv.)', 'T$', 'Kingdom of Tonga', 'TO', 'TON', 'Tonga', '009', '061', 0, '676', 'TO.png'),
(780, 'Port of Spain', 'Trinidadian; Tobagonian', '780', 'Trinidad and Tobago dollar', 'TTD', 'cent', 'TT$', 'Republic of Trinidad and Tobago', 'TT', 'TTO', 'Trinidad and Tobago', '019', '029', 0, '1', 'TT.png'),
(784, 'Abu Dhabi', 'Emirian', '784', 'UAE dirham', 'AED', 'fils (inv.)', 'AED', 'United Arab Emirates', 'AE', 'ARE', 'United Arab Emirates', '142', '145', 0, '971', 'AE.png'),
(788, 'Tunis', 'Tunisian', '788', 'Tunisian dinar', 'TND', 'millime', 'TND', 'Republic of Tunisia', 'TN', 'TUN', 'Tunisia', '002', '015', 0, '216', 'TN.png'),
(792, 'Ankara', 'Turk', '792', 'Turkish lira (inv.)', 'TRY', 'kurus (inv.)', '₺', 'Republic of Turkey', 'TR', 'TUR', 'Turkey', '142', '145', 0, '90', 'TR.png'),
(795, 'Ashgabat', 'Turkmen', '795', 'Turkmen manat (inv.)', 'TMT', 'tenge (inv.)', 'm', 'Turkmenistan', 'TM', 'TKM', 'Turkmenistan', '142', '143', 0, '993', 'TM.png'),
(796, 'Cockburn Town', 'Turks and Caicos Islander', '796', 'US dollar', 'USD', 'cent', '$', 'Turks and Caicos Islands', 'TC', 'TCA', 'Turks and Caicos Islands', '019', '029', 0, '1', 'TC.png'),
(798, 'Funafuti', 'Tuvaluan', '798', 'Australian dollar', 'AUD', 'cent', '$', 'Tuvalu', 'TV', 'TUV', 'Tuvalu', '009', '061', 0, '688', 'TV.png'),
(800, 'Kampala', 'Ugandan', '800', 'Uganda shilling', 'UGX', 'cent', 'UGX', 'Republic of Uganda', 'UG', 'UGA', 'Uganda', '002', '014', 0, '256', 'UG.png'),
(804, 'Kiev', 'Ukrainian', '804', 'hryvnia', 'UAH', 'kopiyka', '₴', 'Ukraine', 'UA', 'UKR', 'Ukraine', '150', '151', 0, '380', 'UA.png'),
(807, 'Skopje', 'of the former Yugoslav Republic of Macedonia', '807', 'denar (pl. denars)', 'MKD', 'deni (inv.)', 'ден', 'the former Yugoslav Republic of Macedonia', 'MK', 'MKD', 'Macedonia, the former Yugoslav Republic of', '150', '039', 0, '389', 'MK.png'),
(818, 'Cairo', 'Egyptian', '818', 'Egyptian pound', 'EGP', 'piastre', '£', 'Arab Republic of Egypt', 'EG', 'EGY', 'Egypt', '002', '015', 0, '20', 'EG.png'),
(826, 'London', 'British', '826', 'pound sterling', 'GBP', 'penny (pl. pence)', '£', 'United Kingdom of Great Britain and Northern Ireland', 'GB', 'GBR', 'United Kingdom', '150', '154', 1, '44', 'GB.png'),
(831, 'St Peter Port', 'of Guernsey', '831', 'Guernsey pound (GG2)', 'GGP (GG2)', 'penny (pl. pence)', NULL, 'Bailiwick of Guernsey', 'GG', 'GGY', 'Guernsey', '150', '154', 0, '44', NULL),
(832, 'St Helier', 'of Jersey', '832', 'Jersey pound (JE2)', 'JEP (JE2)', 'penny (pl. pence)', NULL, 'Bailiwick of Jersey', 'JE', 'JEY', 'Jersey', '150', '154', 0, '44', NULL),
(833, 'Douglas', 'Manxman; Manxwoman', '833', 'Manx pound (IM2)', 'IMP (IM2)', 'penny (pl. pence)', NULL, 'Isle of Man', 'IM', 'IMN', 'Isle of Man', '150', '154', 0, '44', NULL),
(834, 'Dodoma (TZ1)', 'Tanzanian', '834', 'Tanzanian shilling', 'TZS', 'cent', 'TZS', 'United Republic of Tanzania', 'TZ', 'TZA', 'Tanzania, United Republic of', '002', '014', 0, '255', 'TZ.png'),
(840, 'Washington DC', 'American', '840', 'US dollar', 'USD', 'cent', '$', 'United States of America', 'US', 'USA', 'United States', '019', '021', 0, '1', 'US.png'),
(850, 'Charlotte Amalie', 'US Virgin Islander', '850', 'US dollar', 'USD', 'cent', '$', 'United States Virgin Islands', 'VI', 'VIR', 'Virgin Islands, U.S.', '019', '029', 0, '1', 'VI.png'),
(854, 'Ouagadougou', 'Burkinabe', '854', 'CFA franc (BCEAO)', 'XOF', 'centime', 'XOF', 'Burkina Faso', 'BF', 'BFA', 'Burkina Faso', '002', '011', 0, '226', 'BF.png'),
(858, 'Montevideo', 'Uruguayan', '858', 'Uruguayan peso', 'UYU', 'centésimo', '$U', 'Eastern Republic of Uruguay', 'UY', 'URY', 'Uruguay', '019', '005', 0, '598', 'UY.png'),
(860, 'Tashkent', 'Uzbek', '860', 'sum (inv.)', 'UZS', 'tiyin (inv.)', 'лв', 'Republic of Uzbekistan', 'UZ', 'UZB', 'Uzbekistan', '142', '143', 0, '998', 'UZ.png'),
(862, 'Caracas', 'Venezuelan', '862', 'bolívar fuerte (pl. bolívares fuertes)', 'VEF', 'céntimo', 'Bs', 'Bolivarian Republic of Venezuela', 'VE', 'VEN', 'Venezuela, Bolivarian Republic of', '019', '005', 0, '58', 'VE.png'),
(876, 'Mata-Utu', 'Wallisian; Futunan; Wallis and Futuna Islander', '876', 'CFP franc', 'XPF', 'centime', 'XPF', 'Wallis and Futuna', 'WF', 'WLF', 'Wallis and Futuna', '009', '061', 0, '681', 'WF.png'),
(882, 'Apia', 'Samoan', '882', 'tala (inv.)', 'WST', 'sene (inv.)', 'WS$', 'Independent State of Samoa', 'WS', 'WSM', 'Samoa', '009', '061', 0, '685', 'WS.png'),
(887, 'San’a', 'Yemenite', '887', 'Yemeni rial', 'YER', 'fils (inv.)', '﷼', 'Republic of Yemen', 'YE', 'YEM', 'Yemen', '142', '145', 0, '967', 'YE.png'),
(894, 'Lusaka', 'Zambian', '894', 'Zambian kwacha (inv.)', 'ZMW', 'ngwee (inv.)', 'ZK', 'Republic of Zambia', 'ZM', 'ZMB', 'Zambia', '002', '014', 0, '260', 'ZM.png');

-- --------------------------------------------------------

--
-- Table structure for table `gm_status`
--

CREATE TABLE `gm_status` (
  `id` int(10) UNSIGNED NOT NULL,
  `scania` int(11) NOT NULL DEFAULT '0',
  `bera` int(11) NOT NULL DEFAULT '0',
  `windia` int(11) NOT NULL DEFAULT '0',
  `khroa` int(11) NOT NULL DEFAULT '0',
  `grazed` int(11) NOT NULL DEFAULT '0',
  `mybckn` int(11) NOT NULL DEFAULT '0',
  `rebootna` int(11) NOT NULL DEFAULT '0',
  `luna` int(11) NOT NULL DEFAULT '0',
  `rebooteu` int(11) NOT NULL DEFAULT '0',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `migrations`
--

CREATE TABLE `migrations` (
  `id` int(10) UNSIGNED NOT NULL,
  `migration` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  `batch` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `migrations`
--

INSERT INTO `migrations` (`id`, `migration`, `batch`) VALUES
(1, '2014_10_12_100000_create_password_resets_table', 1),
(2, '2015_08_25_172600_create_settings_table', 1),
(3, '2015_09_19_191655_setup_countries_table', 1),
(4, '2015_10_10_170827_create_users_table', 1),
(5, '2015_10_10_171049_create_social_login_table', 1),
(6, '2015_12_24_080704_setup_authorization_tables', 1),
(7, '2015_12_24_152327_create_sessions_table', 1),
(8, '2015_12_29_224252_create_user_activity_table', 1),
(9, '2015_12_30_171734_add_foreign_keys', 1),
(10, '2017_04_13_200254_create_api_tokens_table', 1),
(11, '2018_08_27_231605_create_gm_status_table', 2),
(12, '2018_09_10_034355_create_bot_logs_table', 3);

-- --------------------------------------------------------

--
-- Table structure for table `password_resets`
--

CREATE TABLE `password_resets` (
  `email` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  `token` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `permissions`
--

CREATE TABLE `permissions` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  `display_name` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `description` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `removable` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `permissions`
--

INSERT INTO `permissions` (`id`, `name`, `display_name`, `description`, `removable`, `created_at`, `updated_at`) VALUES
(1, 'users.manage', 'Manage Users', 'Manage users and their sessions.', 0, '2018-08-05 06:41:19', '2018-08-05 06:41:19'),
(2, 'users.activity', 'View System Activity Log', 'View activity log for all system users.', 0, '2018-08-05 06:41:19', '2018-08-05 06:41:19'),
(3, 'roles.manage', 'Manage Roles', 'Manage system roles.', 0, '2018-08-05 06:41:19', '2018-08-05 06:41:19'),
(4, 'permissions.manage', 'Manage Permissions', 'Manage role permissions.', 0, '2018-08-05 06:41:19', '2018-08-05 06:41:19'),
(5, 'settings.general', 'Update General System Settings', '', 0, '2018-08-05 06:41:19', '2018-08-05 06:41:19'),
(6, 'settings.auth', 'Update Authentication Settings', 'Update authentication and registration system settings.', 0, '2018-08-05 06:41:19', '2018-08-05 06:41:19'),
(7, 'settings.notifications', 'Update Notifications Settings', '', 0, '2018-08-05 06:41:19', '2018-08-05 06:41:19'),
(8, 'gm.status', 'GM Status', 'Get GM Statuses from API & View GM Statuses on Dashboard.', 1, '2018-08-28 06:16:39', '2018-08-28 06:16:39'),
(9, 'user.upload_avatar', 'User Upload Avatar', 'Allow users to upload/change their avatar', 1, '2018-09-10 09:56:23', '2018-09-10 09:56:23'),
(10, 'app.download', 'TMRemote Download', 'Can view & download TMRemote', 1, '2018-09-13 18:07:34', '2018-09-13 18:07:34');

-- --------------------------------------------------------

--
-- Table structure for table `permission_role`
--

CREATE TABLE `permission_role` (
  `permission_id` int(10) UNSIGNED NOT NULL,
  `role_id` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `permission_role`
--

INSERT INTO `permission_role` (`permission_id`, `role_id`) VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 1),
(5, 1),
(6, 1),
(7, 1),
(8, 1),
(8, 2),
(8, 4),
(9, 1),
(10, 1),
(10, 2);

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  `display_name` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `description` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `removable` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`id`, `name`, `display_name`, `description`, `removable`, `created_at`, `updated_at`) VALUES
(1, 'Admin', 'Admin', 'System administrator.', 0, '2018-08-05 06:41:19', '2018-08-05 06:41:19'),
(2, 'User', 'User', 'Default system user.', 0, '2018-08-05 06:41:19', '2018-08-05 06:41:19'),
(4, 'Prime', 'Prime', 'Prime user who has paid for ban detection', 1, '2018-09-11 20:58:33', '2018-09-11 21:00:09'),
(6, 'Restricted', 'Restricted', NULL, 1, '2018-09-13 21:03:20', '2018-09-13 21:03:20');

-- --------------------------------------------------------

--
-- Table structure for table `sessions`
--

CREATE TABLE `sessions` (
  `id` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `ip_address` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_agent` text COLLATE utf8mb4_unicode_ci,
  `payload` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_activity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `settings`
--

CREATE TABLE `settings` (
  `id` int(10) UNSIGNED NOT NULL,
  `key` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  `value` text COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `settings`
--

INSERT INTO `settings` (`id`, `key`, `value`) VALUES
(1, 'app_name', 'Terminal Manager Remote'),
(2, 'remember_me', '1'),
(3, 'forgot_password', '0'),
(4, 'login_reset_token_lifetime', '1440'),
(5, 'throttle_enabled', '1'),
(6, 'throttle_attempts', '5'),
(7, 'throttle_lockout_time', '2'),
(8, 'registration.captcha.enabled', '1'),
(9, 'reg_enabled', '1'),
(10, 'tos', '0'),
(11, 'reg_email_confirmation', '1'),
(12, 'enable_bots', '1');

-- --------------------------------------------------------

--
-- Table structure for table `social_logins`
--

CREATE TABLE `social_logins` (
  `id` int(10) UNSIGNED NOT NULL,
  `user_id` int(10) UNSIGNED NOT NULL,
  `provider` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `provider_id` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  `avatar` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(10) UNSIGNED NOT NULL,
  `email` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  `username` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `password` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `last_name` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `phone` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `avatar` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `address` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `country_id` int(10) UNSIGNED DEFAULT NULL,
  `role_id` int(10) UNSIGNED NOT NULL,
  `birthday` date DEFAULT NULL,
  `last_login` timestamp NULL DEFAULT NULL,
  `confirmation_token` varchar(60) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `two_factor_country_code` int(11) DEFAULT NULL,
  `two_factor_phone` int(11) DEFAULT NULL,
  `two_factor_options` text COLLATE utf8mb4_unicode_ci,
  `remember_token` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `email`, `username`, `password`, `first_name`, `last_name`, `phone`, `avatar`, `address`, `country_id`, `role_id`, `birthday`, `last_login`, `confirmation_token`, `status`, `two_factor_country_code`, `two_factor_phone`, `two_factor_options`, `remember_token`, `created_at`, `updated_at`) VALUES
(3, 'scarlion.me@gmail.com', 'Scarlion', '$2y$10$UxrPQoMs1ez4nLvPNph9H.J7KtYlZCMqumZRnbWpEGagjcxYvB./S', 'Scarlion', NULL, NULL, 'D9He2jCc3NABDBo4.png', NULL, 840, 1, '2006-08-11', '2018-11-09 05:22:41', NULL, 'Active', NULL, NULL, NULL, 'jyHKsDl7b0PO0EjMd2BimtjpVyAzRWlRob2UQnkqQoEVUJhG0GrisAH25ZED', '2018-08-11 00:57:58', '2018-11-09 05:22:41'),
(4, 'MehodinGK@gmail.com', 'Mehodin', '$2y$10$T59v7pcErOcGIQqsjTiiBu/nh6UtmY2v/OmWENDDytXA6b4A7aybm', 'Mehodin', NULL, NULL, 'LXmgLPqPAsrLN5mU.png', NULL, NULL, 1, '2000-05-02', '2018-11-08 01:40:56', NULL, 'Active', NULL, NULL, NULL, 'mmJF9vA1X7pXeg7NDgf7Ebz4i04DDFWA49fhiBROqGfsfgOEWw7xn5Vf1N14', '2018-08-11 00:58:00', '2018-11-08 01:40:56'),
(7, 'korpys123@gmail.com', 'kamil', '$2y$10$pmynaEexQBG304sM6jyunu72t/tHyEkwWahsWkbksU7MfJwd.dOAi', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, NULL, NULL, 'Active', NULL, NULL, NULL, NULL, '2018-09-10 20:23:12', '2018-09-10 20:23:12'),
(10, 'jokr416@gmail.com', 'joker', '$2y$10$5QgzFUD.oANkWzZIy28aE.FnCSF96psyPv1u3HThBFUt75K4vrK2.', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-09-18 11:45:54', NULL, 'Active', NULL, NULL, NULL, NULL, '2018-09-11 01:34:41', '2018-09-18 11:45:54'),
(11, 'Amer.ki@hotmail.com', 'Kappa', '$2y$10$hc4pv4u4X/qUVQ.IR0.K0eSGiRTgN7DnEs/2SWgO2KKhs61JSDsGK', NULL, NULL, NULL, 'r1M9JJaPRq7Lt0Xn.png', NULL, NULL, 2, NULL, '2018-09-16 20:28:51', NULL, 'Active', NULL, NULL, NULL, 'VZNQjNExjYKJd5CtVuw1Jvwd1HqqznlA2tuBZaUDOCuQApqfDetsDr5EuZHD', '2018-09-11 01:45:55', '2018-09-16 20:29:13'),
(12, 'parthspatel.nj@gmail.com', 'Parth', '$2y$10$jVhCMTfEGVf1PffsIEjvUu770aKlbNTi4QWQhX70YZQmoZMOU2Fdm', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-09-13 23:15:54', NULL, 'Active', NULL, NULL, NULL, NULL, '2018-09-13 18:05:48', '2018-09-13 23:16:38'),
(13, 'dusa9797@gmail.com', 'dusa97', '$2y$10$qHu2mwi/q/J81oEGyEBJp.Kknpx7XkE6nScM6ZiSF5GpplEsIhFJq', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-10-04 06:43:56', NULL, 'Active', NULL, NULL, NULL, NULL, '2018-09-13 19:54:05', '2018-10-04 06:43:56'),
(14, 'desktopapple1@gmail.com', 'kevinzzz', '$2y$10$A/QB5cCRC3EM7D7Hz/9.SOrdEQUOlhVWVoh5Gk7j9shpqw9e/QXdW', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-09-13 19:55:08', NULL, 'Active', NULL, NULL, NULL, NULL, '2018-09-13 19:55:01', '2018-09-13 19:55:08'),
(15, 'Scaniamesos@gmail.com', 'Joon', '$2y$10$NwaO4s7F16UzcSq5PWkVeO3CfTd/1J0NNAaB3xrJYaqtNy4M14xIW', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-09-13 20:10:20', NULL, 'Active', NULL, NULL, NULL, NULL, '2018-09-13 20:10:09', '2018-09-13 20:10:20'),
(16, 'noobtra@gmail.com', 'rain', '$2y$10$/OrOItBp7xM1Lzs8E9PUQujp1lVijQ8wclPsX1KGkcDZ3oshmmWNm', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-09-14 02:15:20', NULL, 'Active', NULL, NULL, NULL, NULL, '2018-09-13 20:10:44', '2018-09-14 02:15:20'),
(19, 'JTagTeamDeluxe@gmail.com', 'Ally', '$2y$10$Tlpu9jv8olhWbWm50M1ZdepI78IHWix4h.ufCuQPt.XbPURPiIZUO', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-09-14 02:48:10', NULL, 'Active', NULL, NULL, NULL, 'W9u8PAKrnL5T4dl9aEHCK8XoDL1rGzRp0l5kMlzQ5ISybQCa24zyzcNJiGir', '2018-09-13 20:18:43', '2018-09-14 02:48:10'),
(20, 'tooeasy@aol.com', 'beast', '$2y$10$GLGaylPZSkZornGOnN7H8.JAwbpPPDAb1V2pOw38SRhZYj4B7wYrC', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-11-25 06:29:25', NULL, 'Active', NULL, NULL, NULL, 'pXT85ctT8AJHvdEEvnLaMsRXeHxYrpYaA4cPLHirFBS5uYO1i05WJJiUmvHI', '2018-09-13 20:22:06', '2018-11-25 06:29:25'),
(21, 'unknownghost123@yahoo.com', 'Unknownghost', '$2y$10$BwKoGYC8E6Oe5ES.0ksGo.Al0k8fZZnN8ujFiHY7yuXB0DTxP8dgO', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-09-28 02:11:13', NULL, 'Active', NULL, NULL, NULL, 'UISQuXj5BeSpS7di0fY8tII7fv1PTtXjjAFOtDAXjwJOJAYA7VKQRIGEaeUh', '2018-09-13 20:28:54', '2018-09-28 02:11:13'),
(22, 'pagmeet.singh@gmail.com', 'MadManMax', '$2y$10$KzC7UWSngzBUaZbWUX5dDeQO2UFulzkwC1Kf8tOdqIRai9Ks3O29G', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-09-13 21:01:40', NULL, 'Active', NULL, NULL, NULL, 'vVXrXxrr3N9mGAQUlojtfxFjDOznSILfQurweVnbMRrr1I9WwQ3rFPYPmJUs', '2018-09-13 20:35:15', '2018-09-13 21:01:40'),
(23, 'ericark64@gmail.com', 'Lyfted', '$2y$10$E..IOn0LJV0qoaycCNqvyeHCt3bF4Y09jFtc0V/pg5sCsM89w0yhG', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-09-20 06:57:52', NULL, 'Active', NULL, NULL, NULL, NULL, '2018-09-13 20:36:12', '2018-09-20 06:57:52'),
(24, 'bobmandanstan@gmail.com', 'bobmandanstan', '$2y$10$k/PGMSOzSix9WTsVBatJjeD4UuOgCCs5sB2aSuIFeMdoKtJvdpDcy', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-11-24 01:41:07', NULL, 'Active', NULL, NULL, NULL, 'JCDBg3HyQeBWaqpnrO1CsXitNewDkRceonPTDkB7LHSxhrokN1ZJq7yeWvqm', '2018-09-13 20:48:48', '2018-11-24 01:41:07'),
(25, 'yegor141@hotmail.c', 'yegor141', '$2y$10$YNCpfRQkXY2xVt0F91oqHuSVgeBEsVH/qTf/qVfG3cHbkTr3ZkGnm', NULL, NULL, NULL, NULL, NULL, NULL, 6, NULL, '2018-09-13 20:49:40', NULL, 'Banned', NULL, NULL, NULL, NULL, '2018-09-13 20:49:33', '2018-09-13 21:04:19'),
(26, 'r43dd@hotmail.com', 'fdsh3', '$2y$10$bpB487kdeMU8Oo1DiWo17OOSd8NeD2m8pjZUFuk7MYBH6sqDvydui', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, NULL, NULL, 'Active', NULL, NULL, NULL, NULL, '2018-09-13 21:08:47', '2018-09-13 21:08:47'),
(28, 'hhhhhh@hotmail.com', 'aa33', '$2y$10$FJxuYYVUaqfNdADMg8g7J.ORAZC7NionGlyZEnQaGJPMNJ1A65u7W', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-09-13 21:10:24', NULL, 'Active', NULL, NULL, NULL, NULL, '2018-09-13 21:10:19', '2018-09-13 21:10:24'),
(29, 'ChaoZKillerZ@gmail.com', 'Deception', '$2y$10$GpWUfIguGoOw2hrOfcMRuOgY7PlOa5WSBsJKupedhHOfnx1A0xCxu', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-11-01 15:45:53', NULL, 'Active', NULL, NULL, NULL, 'Qrq8JScj53jurf88DP2SPbG9uVcUCADTxqrgAz4sPDPW3rImvCrLoEVY6w3y', '2018-09-13 21:19:58', '2018-11-01 15:45:53'),
(30, 'marco.psv@hotmail.com', 'markietje24', '$2y$10$apqd2UTrqwZuxmEZj6Ox8OpcqIv9lwq5lCMvuYLuONoU5kY2TAeae', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-09-20 13:15:05', NULL, 'Active', NULL, NULL, NULL, 'WG1HRW7SOQz0m0egG8bfA2DFJxWQ2wl1MI2ogJ2jfRmIZd9jxuAMkukUmjIc', '2018-09-13 22:22:40', '2018-09-20 13:15:05'),
(31, 'destin.adamski@gmail.com', 'pbnjealous', '$2y$10$DsItYEGrZZSsTq110DzJbeARHAOzI7rmGWh7IvVKdXhPhgzsSufi6', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-09-14 00:35:23', NULL, 'Active', NULL, NULL, NULL, 'ZMZlZesSGYHhbYIFUTKlTIbQ1PcfEuazdpsNxmH36bYQ4POH2QfTfXfXXjqs', '2018-09-14 00:30:18', '2018-09-14 00:35:23'),
(32, 'msilveriopaulus@gmail.com', 'rnoises', '$2y$10$O2zuedQ7wnigVa.YES4S.eNiXcPtAKObS.AJe9kEGuUkLCHlvR99K', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, NULL, 'rkjo6S1V2VjnJm6Vcnnfy0LKJ25R3eh1OjpjulCEPac481O1uw16CA34AXqh', 'Active', NULL, NULL, NULL, NULL, '2018-09-14 00:32:56', '2018-09-14 02:45:49'),
(33, 'juniorteenworldwide@gmail.com', 'PreOverkill', '$2y$10$y4AJ/ve8wbP7cH4A1vOfUumQfDuEPdkAyzPgpYfa3qLdwtJxAVJJO', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-09-14 07:23:34', NULL, 'Active', NULL, NULL, NULL, 'cRRMqNpPyDlZpZjPage0Pfhi8pO4jZvsOThkWQ5pDBwqh71nlPkM0yhqIO8P', '2018-09-14 00:41:24', '2018-09-14 07:23:34'),
(36, 'bran.stew+poke@gmail.com', 'poke', '$2y$10$y8kB8TDTCUUx1uX8VVsuZemMOS5jtHp4wWnbop8WgUWU.Rv.sH1LS', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, NULL, NULL, 'Active', NULL, NULL, NULL, NULL, '2018-09-14 01:06:09', '2018-09-14 01:06:38'),
(37, 'mustprotectsmile@gmail.com', 'mustprotect', '$2y$10$LDVFodfiIZ1WJASufh7H5OjaiCCCTddQfwTmSZZu3D9z4xtTvCLQK', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-09-17 01:48:18', NULL, 'Active', NULL, NULL, NULL, NULL, '2018-09-14 02:07:30', '2018-09-17 01:48:18'),
(38, 'juanavendano@outlook.com', 'splitone', '$2y$10$uPVtjbyYZR3wusy0huUAbONOrQOxR8dWSTCfrkYkrEuNPpjzlSXyu', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-09-14 02:40:07', NULL, 'Active', NULL, NULL, NULL, 'uFIqhxBlsXijSbIaxADbvNDszrycZTMNaIhzo8DimDsUlFepQJR1XkQJItFY', '2018-09-14 02:39:41', '2018-09-14 02:40:07'),
(39, 'jzhoubetonline@gmail.com', 'jayzizzy', '$2y$10$Crl8/oyoQXmAuF3sVbCaSu2e5cfbycrKzIy5QjfDDhuaPXmlbLd8a', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, NULL, 'kSPXstpoLfCdKzrLXqIXv8LBfP1hYXeZqluAGxNHcUunJxiOtVJdl9nu70rk', 'Unconfirmed', NULL, NULL, NULL, NULL, '2018-09-14 02:41:00', '2018-09-14 02:41:00'),
(40, 'christrahan7@gmail.com', '13thExplorer', '$2y$10$AIJy.mFF9XNSiG/Kbpe67us.Y4AtPDpHczsEPVfKxbIzHfeaYd6Ta', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-09-14 03:03:39', NULL, 'Active', NULL, NULL, NULL, 'JCk1jXlaVzikOYtKRWL6MnYn68UfCHKaHXFCxqWqFLIuGOLHCtcgZk4Wu5Wp', '2018-09-14 02:56:59', '2018-09-14 03:03:39'),
(41, 'glueydew3@gmail.com', 'glueydew', '$2y$10$BGYGpdqB9sK0e94jP0fVk.oPOJgLc5JGwO4eU4E8EGva37xQ9ve1e', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-10-03 01:25:04', NULL, 'Active', NULL, NULL, NULL, 'alNd3HvoOSzaxp9PJWuVfJwGmwGxaVBCIHPW7x8is5RfS4ZrirhRWfVbQP4E', '2018-09-14 04:50:50', '2018-10-03 01:25:04'),
(42, 'mayplex123@gmail.com', 'mayplex', '$2y$10$fkJK5P5EU/GbzEpoa.aXEektSQUhbYaHp19CcYZVt8U7ZnUHHR03a', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-10-11 09:34:07', NULL, 'Active', NULL, NULL, NULL, '2afAGRPOj5nlBtEgALs7aAI0OFPR9Oh2kYpdAjLvOiECYW8GKM9cdmxpvrwH', '2018-09-17 13:00:16', '2018-10-11 09:34:07'),
(43, 'crazyforpotato@gmail.com', 'Kaiserslimer', '$2y$10$sxyrl6FYVJvVzGU8zsPXB.ddVp1FmvwIO.F852Frss9/6wmuOSzeC', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-09-18 05:53:18', NULL, 'Active', NULL, NULL, NULL, NULL, '2018-09-18 05:52:59', '2018-09-18 05:53:18'),
(44, 'tyler@abstract.kr', 'soowan', '$2y$10$T3Y/l8giQAqOYUfwodEXIuqaEXfbAgH.uvOTkpYb33NF6Jlsjf3zG', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-10-04 02:53:22', NULL, 'Active', NULL, NULL, NULL, 'MStpMREBs9goSkIlmvhr0ch6tvLnLW3vix2U81x4cniMGjMHYgytl3Pl9xPm', '2018-09-18 05:56:02', '2018-10-04 02:53:22'),
(45, 'dvymin@gmail.com', 'dvymin', '$2y$10$4BUCzMBy9W4yZImr69EbteNpHkJjPyB2a2wgg7sLChJ5e7cjnSUFy', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-09-21 06:57:41', NULL, 'Active', NULL, NULL, NULL, 'yNCFSsEDOnxjmZnXUZe7MZY3xGLlb0ohfuzgtBRPI9FmHZ7sKwAODryXySeG', '2018-09-18 11:29:10', '2018-09-21 06:57:41'),
(46, 'romangramirez707@icloud.com', 'Rome', '$2y$10$pkR0grSm9bQdn5ThebAsIeCyZaqj5L2/3qBGrBo85S5fcYTqWf.Pi', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-10-01 07:52:34', NULL, 'Active', NULL, NULL, NULL, 'qKmYlyj45zFY573dIFiRBhxvZmLJE6ecotjL6nFl121rCTo3zkt67R0LcHAH', '2018-09-18 19:09:14', '2018-10-01 07:52:34'),
(47, 'elumannak1@gmail.com', 'marik', '$2y$10$pOtOjugUIUHbqAXdjpwrTO08U.gQtA0/Srqx3NjimTqRznC7tBOEC', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-09-20 14:10:36', NULL, 'Active', NULL, NULL, NULL, NULL, '2018-09-20 14:10:16', '2018-09-20 14:10:36'),
(49, 'bimbx1@gmail.com', 'sep1z', '$2y$10$9hNyDIqunYOek25hZlzuyuLUYWt6UStGQUf2EGia/PXmw5h5DyybW', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-09-29 22:29:54', NULL, 'Active', NULL, NULL, NULL, 'cxtpIZVxexLoxQZjfdYn4uAiDN9awuyL1r6TFl9CwA09sFW7ZtVjDe5P21J9', '2018-09-28 15:18:51', '2018-09-29 22:29:54'),
(50, 'HrayrMatossian@gmail.com', 'Ray', '$2y$10$0HqVygP9AM/Mi4HLFNi3U.ga4twbWw1wCqJsGFfYj/qrVkR7wHFf6', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-10-31 19:28:07', NULL, 'Active', NULL, NULL, NULL, 'Nh3vuIUPmt6qalAvdWRxS0AMWIZuPfnmvJBwc7UH6CkUPFapQxx0puz0acLX', '2018-09-30 00:31:33', '2018-10-31 19:28:07'),
(51, 'brohul8841@gmail.com', 'hyung', '$2y$10$zkQ49xLV7WTs6W/.Mg.Sd.nLh45f7bSFP6FvJGZlK9xhIPw/9a7ZS', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-10-06 23:15:25', NULL, 'Active', NULL, NULL, NULL, '5vQ7yEwywq3s99Jp1GfcKEDIiDczlxyHE7tz08nI37QHYfFnBKuIpPRwGyHZ', '2018-09-30 02:12:36', '2018-10-06 23:15:25'),
(52, 'Kihsudn443233@mail.com', 'bigcock', '$2y$10$h/xFu1g/VAholyKrfz9DQOdYR6uMbSMn4F2HKIWb95A5nc2I2NI02', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, NULL, 'MKDB00ThwRgq3Wa7DgaQEOwgzPcM4xf5YGynQwlSKN2sPsDxJkF66uZL2iZo', 'Unconfirmed', NULL, NULL, NULL, NULL, '2018-10-01 07:50:00', '2018-10-01 07:50:00'),
(53, 'pandadogxd@gmail.com', 'PandaEd', '$2y$10$18h0ext7vaAinl1xaeOsNuCBiqw2nQ/oh2GLdrtSm0vkopBeFV6/a', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-10-24 11:21:33', NULL, 'Active', NULL, NULL, NULL, 'NaRzCH6H6bUga5F4ixIboGry3V0jVgj0LtgkZBgla01Tb3HMW620KdLlDS5T', '2018-10-02 10:20:30', '2018-10-24 11:21:33'),
(54, 'marusalex1@gmail.com', 'Kiki', '$2y$10$ZfYLSyPdNo2M21G6Q7UW0O5TTwLLSP0mQvFaxfF5pRT9miiz8G6/O', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-10-25 10:40:17', NULL, 'Active', NULL, NULL, NULL, 'LuEk8Jcv2FCHTH5MLPcDdzQbdyPknWUUPsC1RjRxSyhdqfIq4d251mnhS8fs', '2018-10-02 22:39:11', '2018-10-25 10:40:17'),
(55, 'x.swizsle@gmail.com', '2011coolkid4', '$2y$10$rEnBdNuWF9UFpTaNm/wDkOKSO6hNZiQQ2XSozG9rAjMcmLN47ksju', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-10-04 08:58:28', NULL, 'Active', NULL, NULL, NULL, '0JIiHxCcVCqwMgB0qb6m0r0DUeFSajF5B7mqHHUiVyzDeqjzByHlQtgFczxx', '2018-10-04 07:59:03', '2018-10-04 08:58:28'),
(56, 'selimaydogan51@gmail.com', 'Mello22', '$2y$10$EBcS7DQXsJP10n1wWUWRtubM0Sz41w0yFFoml5EHbi/V2V4GxTR9.', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-10-07 19:01:42', NULL, 'Active', NULL, NULL, NULL, NULL, '2018-10-07 18:59:07', '2018-10-07 19:01:42'),
(57, 'tonyngo1398@gmail.com', 'Tony4444', '$2y$10$DTFXues85Zoe6T42RlHPrewtFnnP7Fqmsqry5kGPYn1VqgH6H5Ew6', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-10-08 20:25:58', NULL, 'Active', NULL, NULL, NULL, '6EtloJ4vT0bZaLD4YrVRTSnTg553d9Qgb0zZGQtcfNkJ6gViS7n7H1MH5l7B', '2018-10-08 20:08:03', '2018-10-08 20:25:58'),
(58, 'imhere63@hotmail.com', 'Zaui', '$2y$10$VP7IQUJAERTrM0yHdgOnG.pDptBz4wyaUeQzIzjY1uOjDlrKfz/ga', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-11-23 05:10:39', 'gfIoy9fIzY0sM4CqmSO09O2ZtYcDxiXvDK7nOWwPs7ZdxTc6kz1TOBmlR9fb', 'Active', NULL, NULL, NULL, '6LSR9RVSKAHm2FVPG1NfQAnn6XP9boAUxoFzJroD8T7BJGTeQVisATlrdSfR', '2018-10-09 03:26:43', '2018-11-23 05:10:39'),
(59, 'ninjutsu562@gmail.com', 'MattyGK', '$2y$10$i1M4XN4Z9FGH4PcOYcAeou8SeodjHEsZPRK2dNL8muKFlUSHU0h4i', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-10-10 10:06:55', NULL, 'Active', NULL, NULL, NULL, '2cWewOZriYiYbB5PlxREBTRgdFe9V6KSJShA9PUkGgz8phGmBcuM0xaqdaL5', '2018-10-09 10:55:22', '2018-10-10 10:06:55'),
(60, 'Minhquang2408@yahoo.com', 'Jolybean132', '$2y$10$1VWA6dWjqAYxrMGwhaUUqOa0qy0BgFdSsmKyP6wEWGL4b5/BBphte', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, NULL, NULL, 'Active', NULL, NULL, NULL, NULL, '2018-10-09 23:04:31', '2018-10-09 23:07:20'),
(61, 'Greenpos2408@gmail.com', 'Jolybean1232', '$2y$10$kCzqzgNKBEeaTpbigYytluo4GHUrgVP43j8WOT7ZnQGEe590XHMEq', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, NULL, '3YCByr031TodhzdRmkxXq484NGuDguxlYYAuUS6AqiF791lPyfM6Su531ZdY', 'Unconfirmed', NULL, NULL, NULL, NULL, '2018-10-09 23:05:57', '2018-10-09 23:05:57'),
(62, 'stevenchu1206@gmail.com', 'schu', '$2y$10$eAKz1E8.qb4nku2/PZYpAum2TFPF2T/GZ.pmqg.UuqyIpcrflEBG2', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-10-16 20:10:42', NULL, 'Active', NULL, NULL, NULL, NULL, '2018-10-10 09:09:12', '2018-10-16 20:10:42'),
(63, 'gachip1159@yahoo.com', 'Joly11599', '$2y$10$HlHHITFNBMwIbR.FPseh/.nDY7xQ/IWlLOanWurdOGaw6fGFjNlXC', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-10-15 23:50:24', NULL, 'Active', NULL, NULL, NULL, 'kLVFj4Mr5Vk2z6mMzfk7sZuoTJai5szdkxIeFx6iwaC7N3G3bDAkiPUvHw25', '2018-10-11 19:24:59', '2018-10-15 23:50:24'),
(64, 'aerigetic@gmail.com', 'nightRhyme', '$2y$10$dfrxw1Z1mG/V0Py4l5pGA.CVG1KQ.oKRQDyeSDTzNatfIiAbl8Wle', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-11-01 00:52:06', NULL, 'Active', NULL, NULL, NULL, 'js2N44LKoHldHJnqXSzeCsMNZvY4MTtCGv9wkXKPLZ8malawCG3kVhd6f0Nw', '2018-10-22 00:19:05', '2018-11-01 00:52:06'),
(65, 'leowongsk99@gmail.com', 'whiteshoes', '$2y$10$aB9zHokBYUhxwytUnizw5ugwNcY/JMqLNhAsnIFOiHH3YieDHQU1y', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-10-24 11:56:15', NULL, 'Active', NULL, NULL, NULL, NULL, '2018-10-24 11:23:36', '2018-10-24 11:56:15'),
(66, 'ty.hiscocks@yahoo.com', 'Calmosiity', '$2y$10$6iXDE/Mr/VvCzSBUwTW3DuuPntvheMbdIEGYoukPhOUSn4ciYYbGC', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-11-13 09:03:41', NULL, 'Active', NULL, NULL, NULL, 'lQeugvkECgUhSfbfkTtP6gIsBt8nxvHYhGv8HDVdKqkIZqJISibsC1L2xYUd', '2018-10-27 01:49:32', '2018-11-13 09:03:41'),
(68, 'jake.kappes99@gmail.com', 'TymeGyzmo', '$2y$10$unBtSOOmKGmfpo6aqVGOMeqRes9ykGgYyywzUGznRIGkFXs4ipsPe', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, NULL, 's2zqxhU4eNs1Jq7Hm0o7qUZRop88uJNq5EuEmumVyyOjrMV1hFBR7qKq2WwY', 'Unconfirmed', NULL, NULL, NULL, NULL, '2018-11-02 01:49:40', '2018-11-02 01:49:40'),
(69, 'jake.kappes00@icloud.com', 'Newb', '$2y$10$8TIpPZUae4XmjeRy614qkeeFxjTsJLN47Mk9eJOK2dMw.qdHguSoS', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-11-08 18:25:01', NULL, 'Active', NULL, NULL, NULL, NULL, '2018-11-02 01:52:40', '2018-11-08 18:25:02'),
(70, 'tnsgk215@gmail.com', 'TamirN', '$2y$10$QeKnjHWv9.0U6Cc4B81YY.XIRmIMLsqJoWprjmiLdkpwV/D2TO5SS', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-11-02 01:53:28', NULL, 'Active', NULL, NULL, NULL, 'yFoEBKJj0OPD7IWEDGkeef8srV0QlYNS6uRZZrX2oJWuyCPO3UThUJwEQtAG', '2018-11-02 01:52:45', '2018-11-02 01:53:28'),
(71, 'mbuivydas@hotmail.com', 'Magika', '$2y$10$9zaWplijEwbhSpqDKdIKOOCmowg6LmFXHKog7WfG8jLvxoiEJhRPO', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, NULL, '6Osnvu4RLU6uQ12eKXfTg1SUsXvNgUNvL84L5DI590XZIxgTc1lsnFxfb3Ln', 'Active', NULL, NULL, NULL, NULL, '2018-11-02 02:07:28', '2018-11-02 02:18:44'),
(72, 'jasonnguyen159@gmail.com', 'Jaytee', '$2y$10$WSJwfzxVU43b8kWTUyJJeuVAcr3ChDBjA0lGEtuxYCZljGbvDW9v6', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-11-06 04:59:32', NULL, 'Active', NULL, NULL, NULL, 'V7iRMncM2LCVipt8IENDMyQ8xuXpYJF1XjqbT9xMRtshPxZvHECHX4Dvz2ds', '2018-11-06 04:58:30', '2018-11-06 04:59:32'),
(73, 'edweun@gmail.com', 'Jimin', '$2y$10$GjZ/znwTvt6heNUtaiNRDeKBzQkgBwsqU.YFTnf/g95LmBCdWfLDe', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-11-12 01:32:05', NULL, 'Active', NULL, NULL, NULL, 'nVAGMXRuSXWOpqhM9yBJGHTyOb07trna2Capk1Koh8ptkA32SpRncALFGP05', '2018-11-07 04:54:02', '2018-11-12 01:32:05'),
(74, 'Enticejason@gmail.com', 'Jason', '$2y$10$TQeC0mRBnwjvU9fzil96UeK6Q6i7wodfA0YoFL5vQKYgL8O52UBIe', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-11-09 12:12:48', NULL, 'Active', NULL, NULL, NULL, NULL, '2018-11-09 06:19:58', '2018-11-09 12:12:48'),
(75, 'chltmdgus130@daum.net', 'chltmdgus98', '$2y$10$uLvNJFiTqGZKhNDsDTDDHuWYieRsU.yggU8F57eT2ZD0U7bu.IRD.', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-11-24 14:17:14', NULL, 'Active', NULL, NULL, NULL, NULL, '2018-11-09 06:32:09', '2018-11-24 14:17:14'),
(76, 'ynott789@gmail.com', 'ynott', '$2y$10$LIT.xbbjkIP2VjrsBXOfIOaSpskIhRQBFwAtvFVFRgJUTOBaLoxg6', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-11-09 09:40:39', NULL, 'Active', NULL, NULL, NULL, 'eYZkImi2GP6YaVu6RdrooPJS4iprywkW5neb02P64hPL8UsmDDxMfBftFoVL', '2018-11-09 09:39:43', '2018-11-09 09:40:39'),
(77, 'crazypeanuts5@gmail.com', 'buffz0r', '$2y$10$it8lpMuVDvmYdQzGTyfXNedpsoSES2pgEYOLXwLnQ/GkCRBetTuse', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-11-09 12:18:05', NULL, 'Active', NULL, NULL, NULL, 'LmjUbHVTThgxQ0Qle1JmhP66uFS49lO0BduO9cisiSl8gpHzAJdb1pphvVtA', '2018-11-09 12:00:52', '2018-11-09 12:18:05'),
(78, 'sharilsamsuri@gmail.com', 'sharilhack', '$2y$10$1N728v7eiGnjvrOdI.3NIeSPaTmFc1PphyDpYYJIK/ZDmfYVD33QK', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, NULL, NULL, 'Active', NULL, NULL, NULL, NULL, '2018-11-09 13:39:34', '2018-11-09 13:53:40'),
(79, 'nathanryan2000@hotmail.com', 'Mono', '$2y$10$feq9lupuyQIYVLoVqc.dCOuZR3iHiGfkBfkgEP41m3V9xvNQ3J0bS', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, NULL, 'KVMQRDOh10e205OBmuV3sQS7Y7F1aORCAGIUeGCBMEzjJcZR6eTzFvGNEYMk', 'Unconfirmed', NULL, NULL, NULL, NULL, '2018-11-09 14:02:18', '2018-11-09 14:02:18'),
(80, 'mariakrupnik2@gmail.com', 'Mahorori', '$2y$10$OfNC4xRjztdcI/TC9nluK.HdL3/HhBVsLkf88SUh6xhzouiXf46T2', NULL, NULL, NULL, NULL, NULL, NULL, 6, NULL, '2018-11-11 22:49:45', NULL, 'Banned', NULL, NULL, NULL, NULL, '2018-11-11 22:49:30', '2018-11-12 19:33:25'),
(81, 'ng.jaden12@gmail.com', 'Kirbyboi123', '$2y$10$QLFAXPTuChozhivl1/MjJuJAqIubjbzlw97QB7f766ikNGeRWvrRm', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-11-14 21:53:00', NULL, 'Active', NULL, NULL, NULL, 'EmN3w1y5mTjYw5iqIBmPgeHmdJWeLvYmfNg495gn8pDqmeExZ3ryaExKbZw6', '2018-11-14 21:51:11', '2018-11-14 21:53:00'),
(82, 'rinoiswierd@gmail.com', 'rushman7', '$2y$10$WSdtxcQpIFVcN21wwX.MmuYn12ZrzYTsLv0.witKnyiVVTUhctSB6', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, '2018-11-20 02:06:41', NULL, 'Active', NULL, NULL, NULL, 'icelawwZVe340n37wE2SEKkkd4D0HG14FtR6YS00UKHCSlsfABezHWwJnfLI', '2018-11-20 02:03:40', '2018-11-20 02:06:41');

-- --------------------------------------------------------

--
-- Table structure for table `user_activity`
--

CREATE TABLE `user_activity` (
  `id` int(10) UNSIGNED NOT NULL,
  `description` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_id` int(10) UNSIGNED NOT NULL,
  `ip_address` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_agent` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `api_tokens`
--
ALTER TABLE `api_tokens`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_tokens_id_expires_at_index` (`id`,`expires_at`),
  ADD KEY `api_tokens_user_id_foreign` (`user_id`);

--
-- Indexes for table `bot_logs`
--
ALTER TABLE `bot_logs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `countries`
--
ALTER TABLE `countries`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `gm_status`
--
ALTER TABLE `gm_status`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `migrations`
--
ALTER TABLE `migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `password_resets`
--
ALTER TABLE `password_resets`
  ADD KEY `password_resets_email_index` (`email`),
  ADD KEY `password_resets_token_index` (`token`);

--
-- Indexes for table `permissions`
--
ALTER TABLE `permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `permissions_name_unique` (`name`);

--
-- Indexes for table `permission_role`
--
ALTER TABLE `permission_role`
  ADD PRIMARY KEY (`permission_id`,`role_id`),
  ADD KEY `permission_role_role_id_foreign` (`role_id`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `roles_name_unique` (`name`);

--
-- Indexes for table `sessions`
--
ALTER TABLE `sessions`
  ADD UNIQUE KEY `sessions_id_unique` (`id`);

--
-- Indexes for table `settings`
--
ALTER TABLE `settings`
  ADD PRIMARY KEY (`id`),
  ADD KEY `settings_key_index` (`key`);

--
-- Indexes for table `social_logins`
--
ALTER TABLE `social_logins`
  ADD PRIMARY KEY (`id`),
  ADD KEY `social_logins_user_id_foreign` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_email_unique` (`email`),
  ADD KEY `users_created_at_index` (`created_at`),
  ADD KEY `users_username_index` (`username`),
  ADD KEY `users_status_index` (`status`),
  ADD KEY `users_country_id_foreign` (`country_id`),
  ADD KEY `users_role_id_foreign` (`role_id`);

--
-- Indexes for table `user_activity`
--
ALTER TABLE `user_activity`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_activity_user_id_foreign` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bot_logs`
--
ALTER TABLE `bot_logs`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `countries`
--
ALTER TABLE `countries`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=895;

--
-- AUTO_INCREMENT for table `gm_status`
--
ALTER TABLE `gm_status`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `migrations`
--
ALTER TABLE `migrations`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `permissions`
--
ALTER TABLE `permissions`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `settings`
--
ALTER TABLE `settings`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `social_logins`
--
ALTER TABLE `social_logins`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=83;

--
-- AUTO_INCREMENT for table `user_activity`
--
ALTER TABLE `user_activity`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `api_tokens`
--
ALTER TABLE `api_tokens`
  ADD CONSTRAINT `api_tokens_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `permission_role`
--
ALTER TABLE `permission_role`
  ADD CONSTRAINT `permission_role_permission_id_foreign` FOREIGN KEY (`permission_id`) REFERENCES `permissions` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `permission_role_role_id_foreign` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `social_logins`
--
ALTER TABLE `social_logins`
  ADD CONSTRAINT `social_logins_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_country_id_foreign` FOREIGN KEY (`country_id`) REFERENCES `countries` (`id`) ON DELETE SET NULL,
  ADD CONSTRAINT `users_role_id_foreign` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`);

--
-- Constraints for table `user_activity`
--
ALTER TABLE `user_activity`
  ADD CONSTRAINT `user_activity_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
