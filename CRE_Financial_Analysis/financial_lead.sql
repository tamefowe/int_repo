-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema cre_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cre_db` DEFAULT CHARACTER SET utf8 ;
USE `cre_db` ;

-- -----------------------------------------------------
-- Table `cre_db`.`Property_Lead`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cre_db`.`Property_Lead` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Lead_Source` varchar(45) NOT NULL,
  `Lead_Source_Technique` varchar(45) NOT NULL,
  `Lead_First_Name` varchar(24) DEFAULT NULL,
  `Lead_Last_Name` varchar(24) DEFAULT NULL,
  `Lead_Phone_Number` varchar(16) DEFAULT NULL,
  `Lead_Email` varchar(32) DEFAULT NULL,
  `Lead_Address` varchar(225) DEFAULT NULL,
  `Lead_City` varchar(32) DEFAULT NULL,
  `Lead_State` varchar(32) DEFAULT NULL,
  `Lead_Zip_Code` int DEFAULT NULL,
  `Property_Type` varchar(45) NOT NULL,
  `Client_Type` varchar(45) NOT NULL,
  `Lead_Date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `Is_Client_in_Bankruptcy` varchar(10) DEFAULT NULL,
  `Is_Client_Planning_to_File_Bankruptcy` varchar(10) DEFAULT NULL,
  `Was_Client_Previously_in_Bankruptcy` varchar(10) DEFAULT NULL,
  `Asset_Type` varchar(32) NOT NULL,
  `Asset_Subtype` varchar(32) NOT NULL,
  `Property_Use` varchar(45) NOT NULL,
  `Construction_Status` varchar(32) NOT NULL,
  `Is_Property_Distressed` varchar(5) DEFAULT NULL,
  `Property_Class` varchar(45) NOT NULL,
  `Property_Condition` varchar(45) NOT NULL,
  `Location_Class` varchar(45) NOT NULL,
  `Location_Trending` varchar(45) NOT NULL,
  `Location_Type` varchar(32) NOT NULL,
  `Property_Name` varchar(32) DEFAULT NULL,
  `Complex_Name` varchar(32) DEFAULT NULL,
  `Property_Country` varchar(32) DEFAULT NULL,
  `Property_Street_Address1` varchar(225) DEFAULT NULL,
  `Property_Street_Address2` varchar(225) DEFAULT NULL,
  `Property_City` varchar(32) DEFAULT NULL,
  `Property_State` varchar(32) DEFAULT NULL,
  `Property_Zip_Code` int DEFAULT NULL,
  `Property_County` varchar(32) DEFAULT NULL,
  `Property_Municipality` varchar(32) DEFAULT NULL,
  `Property_Map_Parcel_Number` int DEFAULT NULL,
  `Property_Tax_ID_Assessor_Parcel_Number` int DEFAULT NULL,
  `Property_Listed` varchar(32) NOT NULL,
  `Commission_Split_Percent` int DEFAULT NULL,
  `Date_Property_Went_on_Market` date DEFAULT NULL,
  `Seller_Original_Purchase_Date` date DEFAULT NULL,
  `Seller_Type` varchar(20) NOT NULL,
  `Seller_Motivation_Level` varchar(20) NOT NULL,
  `Financial_Strength` varchar(20) NOT NULL,
  `Mortgage_Payments` varchar(20) NOT NULL,
  `Why_Selling` varchar(225) DEFAULT NULL,
  `Roof` varchar(10) NOT NULL,
  `Construction_Type` varchar(20) NOT NULL,
  `No_Stories` int DEFAULT NULL,
  `Foundation` varchar(225) DEFAULT NULL,
  `Exterior` varchar(225) DEFAULT NULL,
  `Floor_Covering` varchar(225) DEFAULT NULL,
  `Pipping` varchar(225) DEFAULT NULL,
  `Paving` varchar(225) DEFAULT NULL,
  `Wiring` varchar(225) DEFAULT NULL,
  `Property_Description` varchar(225) DEFAULT NULL,
  `Location_Description` varchar(225) DEFAULT NULL,
  `Year_Built` int DEFAULT NULL,
  `Year_Renovated` int DEFAULT NULL,
  `Total_Building_Size_SF` int DEFAULT NULL,
  `Net_Rentable_SF` int DEFAULT NULL,
  `Total_Lot_Size` int DEFAULT NULL,
  `No_Buildings` int DEFAULT NULL,
  `HVAC` varchar(20) NOT NULL,
  `Highlights` varchar(225) DEFAULT NULL,
  `Property_On_Ground_Lease` varchar(5) DEFAULT NULL,
  `Sale_Leaseback` varchar(5) DEFAULT NULL,
  `Parking_Type` varchar(20) NOT NULL,
  `No_of_Parking_Spaces` int DEFAULT NULL,
  `Parking_Ratio` int DEFAULT NULL,
  `Amenities_Features` varchar(225) DEFAULT NULL,
  `No_Units` int DEFAULT NULL,
  `Occupancy_Percent` int DEFAULT NULL,
  `No_Vacant` int DEFAULT NULL,
  `Efficiency` int DEFAULT NULL,
  `One_Bedroom` int DEFAULT NULL,
  `Two_Bedroom` int DEFAULT NULL,
  `Three_Bedroom` int DEFAULT NULL,
  `Four_Bedroom` int DEFAULT NULL,
  `Other_Bedroom` int DEFAULT NULL,
  `If_Yes_include_Filing_Type_and_Reasons` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

   
   
-- -----------------------------------------------------
-- Table `cre_db`.`Property_Financials`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cre_db`.`Property_Financials` (
  `id` int NOT NULL AUTO_INCREMENT,
	`idLead` int NOT NULL,
	`Projection_In_Years` int NOT NULL,
	`Monthly_Net_Operating_Income`	decimal(20,5) NOT NULL, 
	`Yearly_Net_Operating_Income` 	decimal(20,5) NOT NULL, 
	`Monthly_Mortgage_Payment`	decimal(20,5) NOT NULL, 
	`Yearly_Mortgage_Payment`	decimal(20,5) NOT NULL, 
	`Monthly_Cash_Flow`	decimal(20,5) NOT NULL, 
	`Yearly_Cash_Flow`	decimal(20,5) NOT NULL, 
	`Annual_Gross_Rental_Income`	decimal(20,5) NOT NULL, 
	`Total_Cash_Required`	decimal(20,5) NOT NULL, 
	`Down_Payment`	decimal(20,5) NOT NULL, 
	`Cap_Rate`	decimal(8,5) NOT NULL, 
	`Cash_On_Cash_Return_Renovation`	decimal(8,5) NOT NULL, 
	`Cash_On_Cash_Return_No_Renovation`	decimal(8,5) NOT NULL, 
	`Debt_Coverage_Ratio`	decimal(8,5) NOT NULL, 
	`Gross_Rent_Multiplier`	decimal(8,5) NOT NULL, 
	`Occupancy_Break_Even_Point`	decimal(8,5) NOT NULL, 
	`One_Percent_Rule`	tinyint(1) NOT NULL,
	`Two_Percent_Rule`	tinyint(1) NOT NULL,
	`Seventy_Percent_Rule`	tinyint(1) NOT NULL,
	`Expenses_Per_Unit_Rule`	tinyint(1) NOT NULL,
	`Maintenance_Repairs_Expenses_Per_Unit_Rule`	tinyint(1) NOT NULL,
	`Property_Management_Fee_Per_Unit_Rule`	tinyint(1) NOT NULL,
	`Maintenance_Supplies_Expenses_Per_Unit_Rule`	tinyint(1) NOT NULL,
	`Insurance_Expenses_Per_Unit_Rule`	tinyint(1) NOT NULL,
	`Rent_Roll_Vs_Trailing_Percent_Rule`	tinyint(1) NOT NULL,
	INDEX `fk_Property_Lead_Source2_idx` (`idLead` ASC) VISIBLE,
	CONSTRAINT `fk_Property_Lead_Source2`
    FOREIGN KEY (`idLead`)
    REFERENCES `cre_db`.`Property_Lead` (`id`)  
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
	PRIMARY KEY (`id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


-- -----------------------------------------------------
-- Table `cre_db`.`Property_Financial_inputs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cre_db`.`property_financial_inputs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idLead` int NOT NULL,
  `Projection_In_Years` int NOT NULL,
  `Asking_Price` decimal(20,5) NOT NULL,
  `Offer_Purchase_Price` decimal(20,5) NOT NULL,
  `Renovation_Expense` decimal(15,5) DEFAULT NULL,
  `Down_Payment_Amount` decimal(15,5) DEFAULT NULL,
  `Down_Payment_Percent` decimal(8,5) DEFAULT NULL,
  `Income_Time_Type` char(1) NOT NULL,
  `Gross_Rental_Income` decimal(20,5) NOT NULL,
  `Vacancy` decimal(15,5) DEFAULT NULL,
  `Non_Revenue_Units` decimal(20,5) DEFAULT NULL,
  `Bad_Debt` decimal(15,5) DEFAULT NULL,
  `Concessions` decimal(15,5) DEFAULT NULL,
  `Other_Income` decimal(15,5) DEFAULT NULL,
  `Rubs_Cam_Income` decimal(20,5) DEFAULT NULL,
  `Vacancy_Rate` decimal(8,5) DEFAULT NULL,
  `Expense_Time_Type` char(1) NOT NULL,
  `Accounting` decimal(15,5) DEFAULT NULL,
  `Advertising` decimal(15,5) DEFAULT NULL,
  `Legal` decimal(15,5) DEFAULT NULL,
  `Marketing` decimal(15,5) DEFAULT NULL,
  `Office_Supplies` decimal(15,5) DEFAULT NULL,
  `Administrative_Other` decimal(15,5) DEFAULT NULL,
  `Janitorial` decimal(15,5) DEFAULT NULL,
  `Landscaping` decimal(15,5) DEFAULT NULL,
  `Maintenance_Repair_Costs` decimal(15,5) DEFAULT NULL,
  `Maintenance_Repair_Salary` decimal(15,5) DEFAULT NULL,
  `Pool` decimal(15,5) DEFAULT NULL,
  `Supplies` decimal(15,5) DEFAULT NULL,
  `Cable` decimal(15,5) DEFAULT NULL,
  `Electric` decimal(15,5) DEFAULT NULL,
  `Gas_Oil` decimal(15,5) DEFAULT NULL,
  `Sewer_Water` decimal(15,5) DEFAULT NULL,
  `Telephone` decimal(15,5) DEFAULT NULL,
  `Trash` decimal(15,5) DEFAULT NULL,
  `Utilities_Other` decimal(15,5) DEFAULT NULL,
  `Miscellaneous` decimal(15,5) DEFAULT NULL,
  `Taxes` decimal(15,5) DEFAULT NULL,
  `Fire_Liability_Insurance` decimal(15,5) DEFAULT NULL,
  `Insurance_Other` decimal(15,5) DEFAULT NULL,
  `Property_Management_Fee` decimal(15,5) DEFAULT NULL,
  `Property_Management_Salary` decimal(15,5) DEFAULT NULL,
  `Capital_Reserve` decimal(15,5) DEFAULT NULL,
  `Principal_Loan_Balance` decimal(20,5) NOT NULL,
  `Amortization_Schedule` int NOT NULL,
  `Interest_Rate` decimal(8,5) DEFAULT NULL,
  `Number_Of_Units` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_Property_Lead_Source1_idx` (`idLead`),
  CONSTRAINT `fk_Property_Lead_Source1` FOREIGN KEY (`idLead`) REFERENCES `property_lead` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;