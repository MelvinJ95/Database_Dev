create table users
(
  uid        serial      not null
    constraint users_pkey
      primary key,
  username   varchar(25) not null,
  first_name varchar(15) not null,
  last_name  varchar(20) not null,
  upassword  varchar(20) not null,
  uphone     char(10)    not null,
  uemail     varchar(30) not null
);

create table chats
(
  cid   serial not null
    constraint chats_pkey
      primary key,
  cname varchar(50),
  uid   integer
    constraint chats_uid_fkey
      references users
);

create table posts
(
  pid      serial not null
    constraint posts_pkey
      primary key,
  pcaption varchar(140),
  pdate    char(10),
  pmedia   varchar(200),
  uid      integer
    constraint posts_uid_fkey
      references users,
  cid      integer
    constraint posts_cid_fkey
      references chats
);

create table reactions
(
  rid      serial not null
    constraint reactions_pkey
      primary key,
  rdate    char(10),
  reaction varchar(7),
  pid      integer
    constraint reactions_pid_fkey
      references posts,
  uid      integer
    constraint reactions_uid_fkey
      references users
);

create table reply
(
  post_id integer not null
    constraint reply_rp_fkey
      references posts,
  rid     integer not null
    constraint reply_rpl_fkey
      references posts,
  constraint reply_pkey
    primary key (post_id, rid)
);

create table members
(
  user_id integer not null
    constraint members_uid_fkey
      references users,
  cid     integer not null
    constraint members_cid_fkey
      references chats,
  constraint members_pkey
    primary key (user_id, cid)
);

create table contacts
(
  owner   integer not null
    constraint contacts_uid_fkey
      references users,
  contact integer not null
    constraint contacts_contact_fkey
      references users,
  constraint contacts_pkey
    primary key (owner, contact)
);

create table hashtags
(
  hid   serial not null
    constraint hashtags_pkey
      primary key,
  htext varchar(50)
);

create table tagged
(
  pid integer not null
    constraint tagged_pid_fkey
      references posts,
  hid integer not null
    constraint tagged_hid_fkey
      references hashtags,
  constraint tagged_pkey
    primary key (pid, hid)
);

create table messages
(
  pid      serial not null
    constraint messages_pkey
      primary key,
  pcaption varchar(140),
  pdate    char(10),
  uid      integer
    constraint messages_uid_fkey
      references users,
  cid      integer
    constraint messages_cid_fkey
      references chats
);

