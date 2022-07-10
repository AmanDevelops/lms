from mysql.connector import connect

databse = connect(host="localhost", username="root", password="")

mycursor = databse.cursor()

mycursor.execute("create database lms;")

databse.commit()


db = connect(host="localhost", username="root", password="", database="lms")

mycursor = db.cursor()

mycursor.execute("CREATE TABLE `books` (`BookID` int(11) NOT NULL,`Title` char(32) NOT NULL,`Author` char(32) NOT NULL,`Publisher` char(32) NOT NULL,`Price` int(6) NOT NULL,`Issue` char(10) DEFAULT NULL,`ID` int(11) DEFAULT NULL,`IssueDate` date DEFAULT NULL)")
mycursor.execute("CREATE TABLE `students` (`ID` int(11) NOT NULL,`Name` char(50) DEFAULT NULL,`Class` char(5) DEFAULT NULL,`Email` char(50) DEFAULT NULL,`Contact` bigint(10) DEFAULT NULL,`NoBook` int(11) NOT NULL)")
mycursor.execute("CREATE TABLE `userlogin` (`UserID` varchar(15) NOT NULL,`Password` varchar(64) NOT NULL,`EMail` char(64) DEFAULT NULL);")
mycursor.execute("ALTER TABLE `books` ADD PRIMARY KEY (`BookID`);")
mycursor.execute("ALTER TABLE `students` ADD PRIMARY KEY (`ID`),ADD UNIQUE KEY `Email` (`Email`),ADD UNIQUE KEY `Contact` (`Contact`);")
mycursor.execute("ALTER TABLE `userlogin`ADD PRIMARY KEY (`UserID`),ADD UNIQUE KEY `Password` (`Password`);")
mycursor.execute("INSERT INTO `userlogin` (`UserID`, `Password`, `EMail`) VALUES ('admin', '21232f297a57a5a743894a0e4a801fc3', 'amanpal2072004@gmail.com');")
db.commit()

