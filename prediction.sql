DROP TABLE IF EXISTS 予想;
CREATE TABLE 予想 (
  予想番号 INTEGER PRIMARY KEY,
  レースID TEXT NOT NULL,
  本命馬番 INTEGER NOT NULL,
  対抗馬番 INTEGER NOT NULL,
  単穴馬番 INTEGER NOT NULL,
  投稿日付  DATE
);

DROP TABLE IF EXISTS レース;
CREATE TABLE レース (
  レースID  TEXT PRIMARY KEY REFERENCES 予想(レースID),
  日付  DATE,
  会場  TEXT,
  レース番号  INTEGER,
  レース名  TEXT,
  種別 TEXT CHECK(種別 IN('芝','ダート','障害')),
  距離 INTEGER
);



INSERT INTO レース(レースID,日付,会場,レース番号,レース名,種別,距離)
VALUES
  ('HN01050201','2023-01-05','阪神',2,'3歳未勝利','ダート',1200),
  ('CK01051001','2023-01-05','中京',10,'万葉ステークス','芝',3000),
  ('CK01051201','2023-01-05','中京',12,'4歳以上2勝クラス','芝',2000);

INSERT INTO 予想(予想番号,レースID,本命馬番,対抗馬番,単穴馬番,投稿日付)
VALUES
  (1,'HN01050201',5,2,10,'2023-01-02'),
  (2,'CK01051001',13,12,1,'2023-01-02');



