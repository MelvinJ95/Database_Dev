------------------ Entity tables ----------------------
-- Posts table
create table posts(pid serial primary key, pcaption varchar(140), pdate varchar(10), pmedia varchar(10),
    uid integer references users(uid), cid integer references chats(cid));
-- Messages table
create table messages(mid serial primary key, );

-- Users table
create table users(uid serial primary key, username varchar(25), first_name varchar(15), last_name varchar(20),
 upassword varchar(20), uphone varchar(10), uemail varchar(30), ubirthday varchar(10), usex varchar(1));

-- Chats table
create table chats(cid serial primary key, cname varchar(20), uid integer references users(uid));

-- Hashtags table
create table hashtags(hid serial primary key, htext varchar(50));

-- Reactions table
create table reactions(rid serial primary key, rdate varchar(10), reaction varchar(7), pid integer references
    posts(pid), uid references users(uid));

----------------- Relation tables -------------------------
-- Tagged table
create table tagged(pid integer references posts(pid), hid integer references hashtag(hid), primary key(pid, hid));

-- Contacts table
create table contacts(uid integer references users(uid), contact integer references users(uid),
    primary key(uid, contact));

-- Member table
create table member(uid integer references users(uid), cid integer refences chats(cid), primary key(uid, cid));


