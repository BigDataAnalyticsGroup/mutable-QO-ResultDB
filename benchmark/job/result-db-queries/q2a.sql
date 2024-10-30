CREATE DATABASE job;
USE job;

-- IMPORT DATA --
CREATE TABLE company_name (
    id INT(4) NOT NULL PRIMARY KEY,
    name CHAR(74) NOT NULL,
    country_code CHAR(255) NOT NULL,
    imdb_id INT(4) NOT NULL,
    name_pcode_nf CHAR(5),
    name_pcode_of CHAR(5),
    md5sum CHAR(32)
);
IMPORT INTO company_name DSV "benchmark/job/data/company_name.csv";
CREATE TABLE keyword (
    id INT(4) NOT NULL PRIMARY KEY,
    keyword CHAR(74) NOT NULL,
    phonetic_code CHAR(5)

);
IMPORT INTO keyword DSV "benchmark/job/data/keyword.csv";
CREATE TABLE movie_companies (
    id INT(4) NOT NULL PRIMARY KEY,
    movie_id INT(4) NOT NULL,
    company_id INT(4) NOT NULL,
    company_type_id INT(4) NOT NULL,
    note CHAR(32)
);
IMPORT INTO movie_companies DSV "benchmark/job/data/movie_companies.csv";
CREATE TABLE movie_keyword (
    id INT(4) NOT NULL PRIMARY KEY,
    movie_id INT(4) NOT NULL,
    keyword_id INT(4) NOT NULL

);
IMPORT INTO movie_keyword DSV "benchmark/job/data/movie_keyword.csv";
CREATE TABLE title (
    id INT(4) NOT NULL PRIMARY KEY,
    title CHAR(334) NOT NULL,
    imdb_index CHAR(12),
    kind_id INT(4) NOT NULL,
    production_year INT(4),
    imdb_id INT(4),
    phonetic_code CHAR(5),
    episode_of_id INT(4),
    season_nr INT(4),
    episode_nr INT(4),
    series_years CHAR(49),
    md5sum CHAR(32)
);
IMPORT INTO title DSV "benchmark/job/data/title.csv";

-- SQL QUERY --
SELECT t.title
FROM company_name AS cn,
     keyword AS k,
     movie_companies AS mc,
     movie_keyword AS mk,
     title AS t
WHERE cn.country_code = "[de]"
  AND k.keyword = "character-name-in-title"
  AND cn.id = mc.company_id
  AND mc.movie_id = t.id
  AND t.id = mk.movie_id
  AND mk.keyword_id = k.id
  AND mc.movie_id = mk.movie_id;
