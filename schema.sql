------------------ Entity tables ----------------------



-- Users table
create table users(uid serial primary key, username varchar(25), first_name varchar(15), last_name varchar(20),
    upassword varchar(20), uphone varchar(10), uemail varchar(30));

-- Chats table
create table chats(cid serial primary key, cname varchar(50), user_id integer references users(uid));

-- Posts table
create table posts(pid serial primary key, pcaption varchar(140), pdate char(10), pmedia varchar(200),
    uid integer references users(uid), cid integer references chats(cid));

-- Hashtags table
create table hashtags(hid serial primary key, htext varchar(50));

-- Reactions table
create table reactions(rid serial primary key, rdate char(10), reaction varchar(7), pid integer references
    posts(pid), uid integer references users(uid));


----------------- Relation tables -------------------------
-- Tagged table
create table tagged(pid integer references posts(pid), hid integer references hashtags(hid), primary key(pid, hid));

-- Contacts table
create table contacts(user_id integer references users(uid), contact integer references users(uid),
    primary key(user_id, contact));

-- Member table
create table member(uid integer references users(uid), cid integer references chats(cid), primary key(uid, cid));

-- Reply table
create table reply(post_id integer references posts(pid), rid integer references posts(pid),
    primary key(post_id, rid));