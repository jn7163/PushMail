------------------------------------
--项目名称：
--对象：
--用途：创建username表
--时间：20016/3/2 10:47:54
--作者: Liuker lt@liuker.xyz
------------------------------------
DROP TABLE IF EXISTS username;
CREATE TABLE IF NOT EXISTS username(
  'Char_Id' char(20) NOT NULL,
  'VChar_Name' varchar(30) DEFAULT NULL,
  'VChar_Email' varchar(50) NOT NULL,
  'Bool_IsSend' tinyint  NOT NULL,
  'VChar_GithubUName' varchar(30) DEFAULT NULL,
  'VChar_Github' varchar(30) DEFAULT NULL,
  'VChar_Address' varchar(50) DEFAULT NULL,
  'Text_Oranizations' text DEFAULT NULL,
  PRIMARY KEY ('Char_Id')
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

