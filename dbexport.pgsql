--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.16
-- Dumped by pg_dump version 9.5.16

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: chats; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE public.chats (
    cid integer NOT NULL,
    cname character varying(50),
    user_id integer
);


ALTER TABLE public.chats OWNER TO appusr;

--
-- Name: chats_cid_seq; Type: SEQUENCE; Schema: public; Owner: appusr
--

CREATE SEQUENCE public.chats_cid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.chats_cid_seq OWNER TO appusr;

--
-- Name: chats_cid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: appusr
--

ALTER SEQUENCE public.chats_cid_seq OWNED BY public.chats.cid;


--
-- Name: contacts; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE public.contacts (
    user_id integer NOT NULL,
    contact integer NOT NULL
);


ALTER TABLE public.contacts OWNER TO appusr;

--
-- Name: hashtags; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE public.hashtags (
    hid integer NOT NULL,
    htext character varying(50)
);


ALTER TABLE public.hashtags OWNER TO appusr;

--
-- Name: hashtags_hid_seq; Type: SEQUENCE; Schema: public; Owner: appusr
--

CREATE SEQUENCE public.hashtags_hid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hashtags_hid_seq OWNER TO appusr;

--
-- Name: hashtags_hid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: appusr
--

ALTER SEQUENCE public.hashtags_hid_seq OWNED BY public.hashtags.hid;


--
-- Name: member; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE public.member (
    uid integer NOT NULL,
    cid integer NOT NULL
);


ALTER TABLE public.member OWNER TO appusr;

--
-- Name: messages; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE public.messages (
    mid integer NOT NULL,
    message character varying(140),
    mdate character(10),
    mhashtag boolean,
    uid integer,
    cid integer
);


ALTER TABLE public.messages OWNER TO appusr;

--
-- Name: messages_mid_seq; Type: SEQUENCE; Schema: public; Owner: appusr
--

CREATE SEQUENCE public.messages_mid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.messages_mid_seq OWNER TO appusr;

--
-- Name: messages_mid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: appusr
--

ALTER SEQUENCE public.messages_mid_seq OWNED BY public.messages.mid;


--
-- Name: posts; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE public.posts (
    pid integer NOT NULL,
    pcaption character varying(140),
    pdate character(10),
    pmedia character varying(200),
    uid integer,
    cid integer
);


ALTER TABLE public.posts OWNER TO appusr;

--
-- Name: posts_pid_seq; Type: SEQUENCE; Schema: public; Owner: appusr
--

CREATE SEQUENCE public.posts_pid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.posts_pid_seq OWNER TO appusr;

--
-- Name: posts_pid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: appusr
--

ALTER SEQUENCE public.posts_pid_seq OWNED BY public.posts.pid;


--
-- Name: reactions; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE public.reactions (
    rid integer NOT NULL,
    rdate character(10),
    reaction character varying(7),
    pid integer,
    uid integer
);


ALTER TABLE public.reactions OWNER TO appusr;

--
-- Name: reactions_rid_seq; Type: SEQUENCE; Schema: public; Owner: appusr
--

CREATE SEQUENCE public.reactions_rid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reactions_rid_seq OWNER TO appusr;

--
-- Name: reactions_rid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: appusr
--

ALTER SEQUENCE public.reactions_rid_seq OWNED BY public.reactions.rid;


--
-- Name: reply; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE public.reply (
    post_id integer NOT NULL,
    rid integer NOT NULL
);


ALTER TABLE public.reply OWNER TO appusr;

--
-- Name: tagged; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE public.tagged (
    pid integer NOT NULL,
    hid integer NOT NULL
);


ALTER TABLE public.tagged OWNER TO appusr;

--
-- Name: users; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE public.users (
    uid integer NOT NULL,
    username character varying(25),
    first_name character varying(15),
    last_name character varying(20),
    upassword character varying(20),
    uphone character varying(10),
    uemail character varying(30),
    ubirthday character(10),
    usex character(1)
);


ALTER TABLE public.users OWNER TO appusr;

--
-- Name: users_uid_seq; Type: SEQUENCE; Schema: public; Owner: appusr
--

CREATE SEQUENCE public.users_uid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_uid_seq OWNER TO appusr;

--
-- Name: users_uid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: appusr
--

ALTER SEQUENCE public.users_uid_seq OWNED BY public.users.uid;


--
-- Name: cid; Type: DEFAULT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.chats ALTER COLUMN cid SET DEFAULT nextval('public.chats_cid_seq'::regclass);


--
-- Name: hid; Type: DEFAULT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.hashtags ALTER COLUMN hid SET DEFAULT nextval('public.hashtags_hid_seq'::regclass);


--
-- Name: mid; Type: DEFAULT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.messages ALTER COLUMN mid SET DEFAULT nextval('public.messages_mid_seq'::regclass);


--
-- Name: pid; Type: DEFAULT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.posts ALTER COLUMN pid SET DEFAULT nextval('public.posts_pid_seq'::regclass);


--
-- Name: rid; Type: DEFAULT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.reactions ALTER COLUMN rid SET DEFAULT nextval('public.reactions_rid_seq'::regclass);


--
-- Name: uid; Type: DEFAULT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.users ALTER COLUMN uid SET DEFAULT nextval('public.users_uid_seq'::regclass);


--
-- Data for Name: chats; Type: TABLE DATA; Schema: public; Owner: appusr
--

COPY public.chats (cid, cname, user_id) FROM stdin;
1	test	1
2	test_2	1
3	test_3	2
4	test_4	2
\.


--
-- Name: chats_cid_seq; Type: SEQUENCE SET; Schema: public; Owner: appusr
--

SELECT pg_catalog.setval('public.chats_cid_seq', 1, false);


--
-- Data for Name: contacts; Type: TABLE DATA; Schema: public; Owner: appusr
--

COPY public.contacts (user_id, contact) FROM stdin;
1	2
2	1
1	3
\.


--
-- Data for Name: hashtags; Type: TABLE DATA; Schema: public; Owner: appusr
--

COPY public.hashtags (hid, htext) FROM stdin;
\.


--
-- Name: hashtags_hid_seq; Type: SEQUENCE SET; Schema: public; Owner: appusr
--

SELECT pg_catalog.setval('public.hashtags_hid_seq', 1, false);


--
-- Data for Name: member; Type: TABLE DATA; Schema: public; Owner: appusr
--

COPY public.member (uid, cid) FROM stdin;
1	1
\.


--
-- Data for Name: messages; Type: TABLE DATA; Schema: public; Owner: appusr
--

COPY public.messages (mid, message, mdate, mhashtag, uid, cid) FROM stdin;
\.


--
-- Name: messages_mid_seq; Type: SEQUENCE SET; Schema: public; Owner: appusr
--

SELECT pg_catalog.setval('public.messages_mid_seq', 1, false);


--
-- Data for Name: posts; Type: TABLE DATA; Schema: public; Owner: appusr
--

COPY public.posts (pid, pcaption, pdate, pmedia, uid, cid) FROM stdin;
1	YOLO	3-12-2019 	URL	1	1
2	YOLOO BRO 	3-12-2019 	URL	2	1
3	Diablo loco esta cabron	3-12-2019 	URL	2	1
\.


--
-- Name: posts_pid_seq; Type: SEQUENCE SET; Schema: public; Owner: appusr
--

SELECT pg_catalog.setval('public.posts_pid_seq', 1, false);


--
-- Data for Name: reactions; Type: TABLE DATA; Schema: public; Owner: appusr
--

COPY public.reactions (rid, rdate, reaction, pid, uid) FROM stdin;
1	3/12/2019 	like	1	1
2	3/12/2019 	like	1	2
\.


--
-- Name: reactions_rid_seq; Type: SEQUENCE SET; Schema: public; Owner: appusr
--

SELECT pg_catalog.setval('public.reactions_rid_seq', 2, true);


--
-- Data for Name: reply; Type: TABLE DATA; Schema: public; Owner: appusr
--

COPY public.reply (post_id, rid) FROM stdin;
1	2
1	3
\.


--
-- Data for Name: tagged; Type: TABLE DATA; Schema: public; Owner: appusr
--

COPY public.tagged (pid, hid) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: appusr
--

COPY public.users (uid, username, first_name, last_name, upassword, uphone, uemail, ubirthday, usex) FROM stdin;
1	zap	melvin	malave	password	44444444	@gmail.com	1         	M
2	Hobby	J	cole\ncole	pw	3423423	@gmail.com	1         	M
3	bastardo	Jon	Snow	Targaryen	32323	@gmail.com	1         	F
\.


--
-- Name: users_uid_seq; Type: SEQUENCE SET; Schema: public; Owner: appusr
--

SELECT pg_catalog.setval('public.users_uid_seq', 1, false);


--
-- Name: chats_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.chats
    ADD CONSTRAINT chats_pkey PRIMARY KEY (cid);


--
-- Name: contacts_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.contacts
    ADD CONSTRAINT contacts_pkey PRIMARY KEY (user_id, contact);


--
-- Name: hashtags_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.hashtags
    ADD CONSTRAINT hashtags_pkey PRIMARY KEY (hid);


--
-- Name: member_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.member
    ADD CONSTRAINT member_pkey PRIMARY KEY (uid, cid);


--
-- Name: messages_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_pkey PRIMARY KEY (mid);


--
-- Name: posts_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pkey PRIMARY KEY (pid);


--
-- Name: reactions_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.reactions
    ADD CONSTRAINT reactions_pkey PRIMARY KEY (rid);


--
-- Name: reply_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.reply
    ADD CONSTRAINT reply_pkey PRIMARY KEY (post_id, rid);


--
-- Name: tagged_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.tagged
    ADD CONSTRAINT tagged_pkey PRIMARY KEY (pid, hid);


--
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (uid);


--
-- Name: chats_uid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.chats
    ADD CONSTRAINT chats_uid_fkey FOREIGN KEY (user_id) REFERENCES public.users(uid);


--
-- Name: contacts_contact_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.contacts
    ADD CONSTRAINT contacts_contact_fkey FOREIGN KEY (contact) REFERENCES public.users(uid);


--
-- Name: contacts_uid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.contacts
    ADD CONSTRAINT contacts_uid_fkey FOREIGN KEY (user_id) REFERENCES public.users(uid);


--
-- Name: member_cid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.member
    ADD CONSTRAINT member_cid_fkey FOREIGN KEY (cid) REFERENCES public.chats(cid);


--
-- Name: member_uid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.member
    ADD CONSTRAINT member_uid_fkey FOREIGN KEY (uid) REFERENCES public.users(uid);


--
-- Name: messages_cid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_cid_fkey FOREIGN KEY (cid) REFERENCES public.chats(cid);


--
-- Name: messages_uid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_uid_fkey FOREIGN KEY (uid) REFERENCES public.users(uid);


--
-- Name: posts_cid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_cid_fkey FOREIGN KEY (cid) REFERENCES public.chats(cid);


--
-- Name: posts_uid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_uid_fkey FOREIGN KEY (uid) REFERENCES public.users(uid);


--
-- Name: reactions_pid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.reactions
    ADD CONSTRAINT reactions_pid_fkey FOREIGN KEY (pid) REFERENCES public.posts(pid);


--
-- Name: reactions_uid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.reactions
    ADD CONSTRAINT reactions_uid_fkey FOREIGN KEY (uid) REFERENCES public.users(uid);


--
-- Name: reply_rp_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.reply
    ADD CONSTRAINT reply_rp_fkey FOREIGN KEY (post_id) REFERENCES public.posts(pid);


--
-- Name: reply_rpl_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.reply
    ADD CONSTRAINT reply_rpl_fkey FOREIGN KEY (rid) REFERENCES public.posts(pid);


--
-- Name: tagged_hid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.tagged
    ADD CONSTRAINT tagged_hid_fkey FOREIGN KEY (hid) REFERENCES public.hashtags(hid);


--
-- Name: tagged_pid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY public.tagged
    ADD CONSTRAINT tagged_pid_fkey FOREIGN KEY (pid) REFERENCES public.posts(pid);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

