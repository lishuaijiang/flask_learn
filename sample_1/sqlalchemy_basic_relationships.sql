-- ----------------------------
-- Create Database
-- ----------------------------
CREATE DATABASE IF NOT EXISTS `flask_learn` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE `flask_learn`;

SET FOREIGN_KEY_CHECKS = 0;
-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `username` VARCHAR(80) NOT NULL,
  `email` VARCHAR(120) NOT NULL,
  `age` INT NOT NULL,
  `password_hash` VARCHAR(128) NOT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  -- 格式：PRIMARY KEY (列名)，用于定义单个或多个列作为主键
  PRIMARY KEY (`id`),
  -- 格式：UNIQUE (列名)，用于定义单个或多个列作为唯一键
  UNIQUE (`username`),
  UNIQUE (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` (`id`, `username`, `email`, `age`, `password_hash`, `created_at`)
VALUES
  (1, 'xiedandan', 'dan07@example.com', 14, 'hC(E6L#nDe', '2001-09-03 23:11:46'),
  (2, 'zhaishuzhen', 'qkong@example.org', 16, '(7jIOCxnwz', '2003-10-18 08:49:42'),
  (3, 'libo', 'pingfeng@example.org', 15, '05sZSVnQ*K', '2009-10-05 11:15:33'),
  (4, 'shigang', 'na29@example.org', 16, '5BHL)xfx#S', '2017-08-05 02:30:35'),
  (5, 'wulihua', 'guiying10@example.net', 15, 'PM2P6PXh(5', '2022-01-28 14:31:03'),
  (6, 'mahongxia', 'xiazhao@example.org', 16, 'mn4HJb#&K!', NOW());

-- ----------------------------
-- Table structure for profile
-- ----------------------------
DROP TABLE IF EXISTS `profile`;
CREATE TABLE `profile` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `gender` TINYINT(1) DEFAULT 0,
  `birthday` DATE NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE (`user_id`),
  FOREIGN KEY (`user_id`) REFERENCES `user`(`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of profile
-- ----------------------------
INSERT INTO `profile` (`id`, `gender`, `birthday`, `user_id`)
VALUES
  (1, 0, '1987-10-23', 1),
  (2, 0, '1996-08-12', 2),
  (3, 1, '1980-02-08', 3),
  (4, 1, '2001-04-03', 4),
  (5, 0, '1991-05-05', 5),
  (6, 0, '2004-06-28', 6);

-- ----------------------------
-- Table structure for post
-- ----------------------------
DROP TABLE IF EXISTS `post`;
CREATE TABLE `post` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `title` VARCHAR(80) NOT NULL,
  `content` TEXT NOT NULL,
  `author_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`author_id`) REFERENCES `user`(`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of post
-- ----------------------------
INSERT INTO `post` (`id`, `title`, `content`, `author_id`)
VALUES
  (1, 'Just purpose summer TV any recently.', 'Southern man region learn owner radio everybody generation. Right image plan behavior author put. Avoid increase culture environment everyone few. Pay market read wide force once. When reveal rock event sort woman pretty various. Land situation project explain. Term her close option million prevent.', 2),
  (2, 'Small race watch term business.', 'Real green win accept group newspaper box. Look home station ground air use. Stock democratic room chair film nation. Establish think pattern you role more successful stock. Plant safe concern not speech left. Avoid door task technology cell quality both. Treat view production radio. A offer often way thing call their anything. Group factor laugh eye mention. In expert race win concern visit.', 2),
  (3, 'Court feel price listen over.', 'High threat could list pass personal common. Nice big consumer continue. Can manage employee environment decision. Service leader want example open create perform. Dinner several work senior dog night admit. Board able five join. Design part if soldier serve industry.', 1),
  (4, 'Mission newspaper TV car next close candidate leave.', 'Suddenly foot PM truth. Realize film majority customer relationship card method allow. Although identify kid despite son from one forget. Student space happen ground class mother. Job contain hope talk safe together analysis nice. Order similar become senior word arrive. Quite hit pressure. Around listen information measure home fund. Something put investment light affect others happy. Mrs visit perhaps few. City war series teach base however. News start memory hour message answer investment. Relate turn serious summer car.', 6),
  (5, 'Fear decade name age only right.', 'Often democratic agree during case late care. Yes main amount participant career case. Face word first cup near. Some production wear gun there finish. Often fear away draw ask office treat. Yet government bad. Night population American turn close life.', 2),
  (6, 'Drive lot teacher claim sport.', 'Name least into another exist think box. Character it suggest soon light class camera somebody. Question company close most anything among who. Interest use have stand plant. Start return music form partner. Respond simply blood how. Society once evidence hope war talk take. Should thus listen glass our. Present remember east care ability. Federal society defense plan event more. Later hard the. Painting husband leader big authority out. All call tonight law.', 6),
  (7, 'Leg street range whole cost.', 'Director buy lot however perhaps. Glass admit place language arm use raise. Happy age sing game western recognize. This exactly case participant street. Gas color probably long. Into better wide keep dog among after consumer. Determine national its attack. Nothing language blue return. Blue follow state health. Inside half imagine between buy assume. State as adult base year nothing. Here situation a energy never get. Family part degree become late.', 4),
  (8, 'Concern partner I garden body.', 'Community if theory international. Sing billion sing not along yeah some. Themselves new half nothing contain such budget. Especially difficult behavior debate walk. Later anyone second third. Group democratic per concern perhaps especially young.', 3);

-- ----------------------------
-- Table structure for tag
-- ----------------------------
DROP TABLE IF EXISTS `tag`;
CREATE TABLE `tag` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `name` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of tag
-- ----------------------------
INSERT INTO `tag` (`id`, `name`)
VALUES
  (1, 'strategy'),
  (2, 'technology'),
  (3, 'coding'),
  (4, 'success'),
  (5, 'debugging'),
  (6, 'explore'),
  (7, 'research'),
  (8, 'development'),
  (9, 'innovation'),
  (10, 'nature'),
  (11, 'travel'),
  (12, 'discovery');

-- ----------------------------
-- Table structure for post_tag
-- ----------------------------
DROP TABLE IF EXISTS `post_tag`;
CREATE TABLE `post_tag` (
  `post_id` INT NOT NULL,
  `tag_id` INT NOT NULL,
  -- 这里需要使用联合主键，保证 post_id + tag_id 不能重复
  PRIMARY KEY (`post_id`, `tag_id`),
  -- 当 post 表删除数据时，post_tag 表中所有与该 post_id 相关的记录也会被删除
  FOREIGN KEY (`post_id`) REFERENCES `post`(`id`) ON DELETE CASCADE,
  -- 当 tag 表删除数据时，post_tag 表中所有与该 tag_id 相关的记录也会被删除
  FOREIGN KEY (`tag_id`) REFERENCES `tag`(`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of tag
-- ----------------------------
INSERT INTO `post_tag` (`post_id`, `tag_id`)
VALUES
  (1, 1),
  (1, 3),
  (1, 5),
  (1, 12),
  (2, 7),
  (2, 8),
  (3, 3),
  (4, 11),
  (5, 8),
  (5, 9),
  (5, 10),
  (6, 5),
  (6, 11),
  (7, 1),
  (7, 4),
  (8, 2),
  (8, 6);

SET FOREIGN_KEY_CHECKS = 1;
