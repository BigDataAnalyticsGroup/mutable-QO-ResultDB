from query_utility import Relation, Join, JoinGraph


def create_q1b():
	ct = Relation(name = "company_type", alias = "ct", attributes = ['kind', 'id'], filters = ['ct.kind = "production companies"'], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['info', 'id'], filters = ['it.info = "bottom 10 rank"'], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'note', 'company_type_id'], filters = ['NOT mc.note LIKE "%(as Metro-Goldwyn-Mayer Pictures)%"'], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['movie_id', 'info_type_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id'], filters = ['t.production_year >= 2005', 't.production_year <= 2010'], projections = [])
	relations = [ct, it, mc, mi_idx, t]

	j0 = Join(ct, mc, ["id"], ["company_type_id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(mc, mi_idx, ["movie_id"], ["movie_id"])
	j3 = Join(it, mi_idx, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2a():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ['cn.country_code ="[de]"'], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['keyword', 'id'], filters = ['k.keyword ="character-name-in-title"'], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['movie_id', 'keyword_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['id'], filters = [], projections = [])
	relations = [cn, k, mc, mk, t]

	j0 = Join(cn, mc, ["id"], ["company_id"])
	j1 = Join(mc, t, ["movie_id"], ["id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(mk, k, ["keyword_id"], ["id"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q3c():
	k = Relation(name = "keyword", alias = "k", attributes = ['keyword', 'id'], filters = ['k.keyword LIKE "%sequel%"'], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['movie_id', 'info'], filters = ['(mi.info = "Sweden" OR mi.info = "Norway" OR mi.info = "Germany" OR mi.info = "Denmark" OR mi.info = "Swedish" OR mi.info = "Denish" OR mi.info = "Norwegian" OR mi.info = "German" OR mi.info = "USA" OR mi.info = "American")'], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['movie_id', 'keyword_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id'], filters = ['t.production_year > 1990'], projections = [])
	relations = [k, mi, mk, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mk, ["id"], ["movie_id"])
	j2 = Join(k, mk, ["id"], ["keyword_id"])
	joins = [j0, j1, j2]

	return JoinGraph(relations, joins)

def create_q4a():
	it = Relation(name = "info_type", alias = "it", attributes = ['info', 'id'], filters = ['it.info ="rating"'], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['keyword', 'id'], filters = ['k.keyword LIKE "%sequel%"'], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['movie_id', 'info', 'info_type_id'], filters = ['mi_idx.info > "5.0"'], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['movie_id', 'keyword_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id'], filters = ['t.production_year > 2005'], projections = [])
	relations = [it, k, mi_idx, mk, t]

	j0 = Join(t, mi_idx, ["id"], ["movie_id"])
	j1 = Join(t, mk, ["id"], ["movie_id"])
	j2 = Join(k, mk, ["id"], ["keyword_id"])
	j3 = Join(it, mi_idx, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q5c():
	ct = Relation(name = "company_type", alias = "ct", attributes = ['kind', 'id'], filters = ['ct.kind = "production companies"'], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['id'], filters = [], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'note', 'company_type_id'], filters = ['NOT mc.note LIKE "%(TV)%"', 'mc.note LIKE "%(USA)%"'], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['movie_id', 'info', 'info_type_id'], filters = ['(mi.info = "Sweden" OR mi.info = "Norway" OR mi.info = "Germany" OR mi.info = "Denmark" OR mi.info = "Swedish" OR mi.info = "Denish" OR mi.info = "Norwegian" OR mi.info = "German" OR mi.info = "USA" OR mi.info = "American")'], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id'], filters = ['t.production_year > 1990'], projections = [])
	relations = [ct, it, mc, mi, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(ct, mc, ["id"], ["company_type_id"])
	j3 = Join(it, mi, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q7a():
	an = Relation(name = "aka_name", alias = "an", attributes = ['name', 'person_id'], filters = ['an.name LIKE "%a%"'], projections = [])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['movie_id', 'person_id'], filters = [], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['info', 'id'], filters = ['it.info = "mini biography"'], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['link', 'id'], filters = ['lt.link = "features"'], projections = [])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['linked_movie_id', 'link_type_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['gender', 'name', 'name_pcode_cf', 'id'], filters = ['n.name_pcode_cf >= "A"', 'n.name_pcode_cf <= "F"', '(n.gender= "m" OR (n.gender = "f"', 'n.name LIKE "B%"))'], projections = [])
	pi = Relation(name = "person_info", alias = "pi", attributes = ['info_type_id', 'note', 'person_id'], filters = ['pi.note = "Volker Boehm"'], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id'], filters = ['t.production_year >= 1980', 't.production_year <= 1995'], projections = [])
	relations = [an, ci, it, lt, ml, n, pi, t]

	j0 = Join(n, an, ["id"], ["person_id"])
	j1 = Join(n, pi, ["id"], ["person_id"])
	j2 = Join(ci, n, ["person_id"], ["id"])
	j3 = Join(t, ci, ["id"], ["movie_id"])
	j4 = Join(ml, t, ["linked_movie_id"], ["id"])
	j5 = Join(lt, ml, ["id"], ["link_type_id"])
	j6 = Join(it, pi, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_q8a():
	an1 = Relation(name = "aka_name", alias = "an1", attributes = ['person_id'], filters = [], projections = [])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['movie_id', 'note', 'role_id', 'person_id'], filters = ['ci.note ="(voice: English version)"'], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ['cn.country_code ="[jp]"'], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'note', 'company_id'], filters = ['mc.note LIKE "%(Japan)%"', 'NOT mc.note LIKE "%(USA)%"'], projections = [])
	n1 = Relation(name = "name", alias = "n1", attributes = ['name', 'id'], filters = ['n1.name LIKE "%Yo%"', 'NOT n1.name LIKE "%Yu%"'], projections = [])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['role', 'id'], filters = ['rt.role ="actress"'], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['id'], filters = [], projections = [])
	relations = [an1, ci, cn, mc, n1, rt, t]

	j0 = Join(n1, ci, ["id"], ["person_id"])
	j1 = Join(ci, t, ["movie_id"], ["id"])
	j2 = Join(mc, cn, ["company_id"], ["id"])
	j3 = Join(ci, rt, ["role_id"], ["id"])
	j4 = Join(an1, ci, ["person_id"], ["person_id"])
	j5 = Join(ci, mc, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q9c():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id'], filters = [], projections = [])
	chn = Relation(name = "char_name", alias = "chn", attributes = ['id'], filters = [], projections = [])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['note', 'person_role_id', 'movie_id', 'role_id', 'person_id'], filters = ['(ci.note = "(voice)" OR ci.note = "(voice: Japanese version)" OR ci.note = "(voice) (uncredited)" OR ci.note = "(voice: English version)")'], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ['cn.country_code ="[us]"'], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['gender', 'name', 'id'], filters = ['n.gender ="f"', 'n.name LIKE "%An%"'], projections = [])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['role', 'id'], filters = ['rt.role ="actress"'], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['id'], filters = [], projections = [])
	relations = [an, chn, ci, cn, mc, n, rt, t]

	j0 = Join(ci, t, ["movie_id"], ["id"])
	j1 = Join(ci, mc, ["movie_id"], ["movie_id"])
	j2 = Join(mc, cn, ["company_id"], ["id"])
	j3 = Join(ci, rt, ["role_id"], ["id"])
	j4 = Join(n, ci, ["id"], ["person_id"])
	j5 = Join(chn, ci, ["id"], ["person_role_id"])
	j6 = Join(an, ci, ["person_id"], ["person_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_q10c():
	chn = Relation(name = "char_name", alias = "chn", attributes = ['id'], filters = [], projections = [])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['movie_id', 'note', 'role_id', 'person_role_id'], filters = ['ci.note LIKE "%(producer)%"'], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ['cn.country_code = "[us]"'], projections = [])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id'], filters = [], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id', 'company_type_id'], filters = [], projections = [])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id'], filters = ['t.production_year > 1990'], projections = [])
	relations = [chn, ci, cn, ct, mc, rt, t]

	j0 = Join(t, ci, ["id"], ["movie_id"])
	j1 = Join(ci, mc, ["movie_id"], ["movie_id"])
	j2 = Join(chn, ci, ["id"], ["person_role_id"])
	j3 = Join(rt, ci, ["id"], ["role_id"])
	j4 = Join(cn, mc, ["id"], ["company_id"])
	j5 = Join(ct, mc, ["id"], ["company_type_id"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q11c():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'country_code', 'id'], filters = ['cn.country_code !="[pl]"', '(cn.name LIKE "20th Century Fox%" OR cn.name LIKE "Twentieth Century Fox%")'], projections = [])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['kind', 'id'], filters = ['ct.kind != "production companies"', 'ct.kind IS NOT NULL'], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['keyword', 'id'], filters = ['(k.keyword = "sequel" OR k.keyword = "revenge" OR k.keyword = "based-on-novel")'], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['id'], filters = [], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'note', 'company_type_id', 'company_id'], filters = ['mc.note IS NOT NULL'], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['movie_id', 'keyword_id'], filters = [], projections = [])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['movie_id', 'link_type_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id'], filters = ['t.production_year > 1950'], projections = [])
	relations = [cn, ct, k, lt, mc, mk, ml, t]

	j0 = Join(lt, ml, ["id"], ["link_type_id"])
	j1 = Join(ml, t, ["movie_id"], ["id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(mk, k, ["keyword_id"], ["id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(mc, ct, ["company_type_id"], ["id"])
	j6 = Join(mc, cn, ["company_id"], ["id"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_q12a():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ['cn.country_code = "[us]"'], projections = [])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['kind', 'id'], filters = ['ct.kind = "production companies"'], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['info', 'id'], filters = ['it1.info = "genres"'], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['info', 'id'], filters = ['it2.info = "rating"'], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_type_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['movie_id', 'info', 'info_type_id'], filters = ['(mi.info = "Drama" OR mi.info = "Horror")'], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['movie_id', 'info', 'info_type_id'], filters = ['mi_idx.info > "8.0"'], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id'], filters = ['t.production_year >= 2005', 't.production_year <= 2008'], projections = [])
	relations = [cn, ct, it1, it2, mc, mi, mi_idx, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mi_idx, ["id"], ["movie_id"])
	j2 = Join(mi, it1, ["info_type_id"], ["id"])
	j3 = Join(mi_idx, it2, ["info_type_id"], ["id"])
	j4 = Join(ct, mc, ["id"], ["company_type_id"])
	j5 = Join(cn, mc, ["id"], ["company_id"])
	j6 = Join(mc, mi_idx, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_q14a():
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['info', 'id'], filters = ['it1.info = "countries"'], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['info', 'id'], filters = ['it2.info = "rating"'], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['keyword', 'id'], filters = ['(k.keyword = "murder" OR k.keyword = "murder-in-title" OR k.keyword = "blood" OR k.keyword = "violence")'], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['kind', 'id'], filters = ['kt.kind = "movie"'], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['movie_id', 'info', 'info_type_id'], filters = ['(mi.info = "Sweden" OR mi.info = "Norway" OR mi.info = "Germany" OR mi.info = "Denmark" OR mi.info = "Swedish" OR mi.info = "Denish" OR mi.info = "Norwegian" OR mi.info = "German" OR mi.info = "USA" OR mi.info = "American")'], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['movie_id', 'info', 'info_type_id'], filters = ['mi_idx.info < "8.5"'], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['movie_id', 'keyword_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['kind_id', 'production_year', 'id'], filters = ['t.production_year > 2010'], projections = [])
	relations = [it1, it2, k, kt, mi, mi_idx, mk, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mi_idx, ["id"], ["movie_id"])
	j2 = Join(mk, mi_idx, ["movie_id"], ["movie_id"])
	j3 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j4 = Join(k, mk, ["id"], ["keyword_id"])
	j5 = Join(it1, mi, ["id"], ["info_type_id"])
	j6 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_q15d():
	at = Relation(name = "aka_title", alias = "at", attributes = ['movie_id'], filters = [], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ['cn.country_code = "[us]"'], projections = [])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id'], filters = [], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['info', 'id'], filters = ['it1.info = "release dates"'], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id'], filters = [], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id', 'company_type_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['movie_id', 'note', 'info_type_id'], filters = ['mi.note LIKE "%internet%"'], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['movie_id', 'keyword_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id'], filters = ['t.production_year > 1990'], projections = [])
	relations = [at, cn, ct, it1, k, mc, mi, mk, t]

	j0 = Join(t, at, ["id"], ["movie_id"])
	j1 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j2 = Join(mi, at, ["movie_id"], ["movie_id"])
	j3 = Join(mc, at, ["movie_id"], ["movie_id"])
	j4 = Join(k, mk, ["id"], ["keyword_id"])
	j5 = Join(it1, mi, ["id"], ["info_type_id"])
	j6 = Join(cn, mc, ["id"], ["company_id"])
	j7 = Join(ct, mc, ["id"], ["company_type_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q18c():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['movie_id', 'note', 'person_id'], filters = ['(ci.note = "(writer)" OR ci.note = "(head writer)" OR ci.note = "(written by)" OR ci.note = "(story)" OR ci.note = "(story editor)")'], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['info', 'id'], filters = ['it1.info = "genres"'], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['info', 'id'], filters = ['it2.info = "votes"'], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['movie_id', 'info', 'info_type_id'], filters = ['(mi.info = "Horror" OR mi.info = "Action" OR mi.info = "Sci-Fi" OR mi.info = "Thriller" OR mi.info = "Crime" OR mi.info = "War")'], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['movie_id', 'info_type_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['gender', 'id'], filters = ['n.gender = "m"'], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['id'], filters = [], projections = [])
	relations = [ci, it1, it2, mi, mi_idx, n, t]

	j0 = Join(t, mi_idx, ["id"], ["movie_id"])
	j1 = Join(ci, mi, ["movie_id"], ["movie_id"])
	j2 = Join(ci, mi_idx, ["movie_id"], ["movie_id"])
	j3 = Join(n, ci, ["id"], ["person_id"])
	j4 = Join(it1, mi, ["id"], ["info_type_id"])
	j5 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q19a():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id'], filters = [], projections = [])
	chn = Relation(name = "char_name", alias = "chn", attributes = ['id'], filters = [], projections = [])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['note', 'person_role_id', 'movie_id', 'role_id', 'person_id'], filters = ['(ci.note = "(voice)" OR ci.note = "(voice: Japanese version)" OR ci.note = "(voice) (uncredited)" OR ci.note = "(voice: English version)")'], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ['cn.country_code ="[us]"'], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['info', 'id'], filters = ['it.info = "release dates"'], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'note', 'company_id'], filters = ['mc.note IS NOT NULL', '(mc.note LIKE "%(USA)%" OR mc.note LIKE "%(worldwide)%")'], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['movie_id', 'info', 'info_type_id'], filters = ['mi.info IS NOT NULL', '(mi.info LIKE "Japan:%200%" OR mi.info LIKE "USA:%200%")'], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['gender', 'name', 'id'], filters = ['n.gender ="f"', 'n.name LIKE "%Ang%"'], projections = [])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['role', 'id'], filters = ['rt.role ="actress"'], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id'], filters = ['t.production_year >= 2005', 't.production_year <= 2009'], projections = [])
	relations = [an, chn, ci, cn, it, mc, mi, n, rt, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(mc, ci, ["movie_id"], ["movie_id"])
	j2 = Join(mi, ci, ["movie_id"], ["movie_id"])
	j3 = Join(cn, mc, ["id"], ["company_id"])
	j4 = Join(it, mi, ["id"], ["info_type_id"])
	j5 = Join(rt, ci, ["id"], ["role_id"])
	j6 = Join(n, an, ["id"], ["person_id"])
	j7 = Join(ci, an, ["person_id"], ["person_id"])
	j8 = Join(chn, ci, ["id"], ["person_role_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8]

	return JoinGraph(relations, joins)

def create_q21a():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'country_code', 'id'], filters = ['cn.country_code !="[pl]"', '(cn.name LIKE "%Film%" OR cn.name LIKE "%Warner%")'], projections = [])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['kind', 'id'], filters = ['ct.kind ="production companies"'], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['keyword', 'id'], filters = ['k.keyword ="sequel"'], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['link', 'id'], filters = ['lt.link LIKE "%follow%"'], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'note', 'company_type_id', 'company_id'], filters = ['mc.note IS NULL'], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['movie_id', 'info'], filters = ['(mi.info = "Sweden" OR mi.info = "Norway" OR mi.info = "Germany" OR mi.info = "Denmark" OR mi.info = "Swedish" OR mi.info = "Denish" OR mi.info = "Norwegian" OR mi.info = "German")'], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['movie_id', 'keyword_id'], filters = [], projections = [])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['movie_id', 'link_type_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id'], filters = ['t.production_year >= 1950', 't.production_year <= 2000'], projections = [])
	relations = [cn, ct, k, lt, mc, mi, mk, ml, t]

	j0 = Join(lt, ml, ["id"], ["link_type_id"])
	j1 = Join(t, mk, ["id"], ["movie_id"])
	j2 = Join(mk, k, ["keyword_id"], ["id"])
	j3 = Join(mc, ct, ["company_type_id"], ["id"])
	j4 = Join(mc, cn, ["company_id"], ["id"])
	j5 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j6 = Join(ml, mi, ["movie_id"], ["movie_id"])
	j7 = Join(mc, mi, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q22c():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ['cn.country_code != "[us]"'], projections = [])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id'], filters = [], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['info', 'id'], filters = ['it1.info = "countries"'], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['info', 'id'], filters = ['it2.info = "rating"'], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['keyword', 'id'], filters = ['(k.keyword = "murder" OR k.keyword = "murder-in-title" OR k.keyword = "blood" OR k.keyword = "violence")'], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['kind', 'id'], filters = ['(kt.kind = "movie" OR kt.kind = "episode")'], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'note', 'company_type_id', 'company_id'], filters = ['NOT mc.note LIKE "%(USA)%"', 'mc.note LIKE "%(200%)%"'], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['movie_id', 'info', 'info_type_id'], filters = ['(mi.info = "Sweden" OR mi.info = "Norway" OR mi.info = "Germany" OR mi.info = "Denmark" OR mi.info = "Swedish" OR mi.info = "Danish" OR mi.info = "Norwegian" OR mi.info = "German" OR mi.info = "USA" OR mi.info = "American")'], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['movie_id', 'info', 'info_type_id'], filters = ['mi_idx.info < "8.5"'], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['movie_id', 'keyword_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['kind_id', 'production_year', 'id'], filters = ['t.production_year > 2005'], projections = [])
	relations = [cn, ct, it1, it2, k, kt, mc, mi, mi_idx, mk, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mi_idx, ["id"], ["movie_id"])
	j2 = Join(t, mc, ["id"], ["movie_id"])
	j3 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j4 = Join(mk, mi_idx, ["movie_id"], ["movie_id"])
	j5 = Join(k, mk, ["id"], ["keyword_id"])
	j6 = Join(it1, mi, ["id"], ["info_type_id"])
	j7 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	j8 = Join(ct, mc, ["id"], ["company_type_id"])
	j9 = Join(cn, mc, ["id"], ["company_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q23a():
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['movie_id', 'status_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['kind', 'id'], filters = ['cct1.kind = "complete+verified"'], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ['cn.country_code = "[us]"'], projections = [])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id'], filters = [], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['info', 'id'], filters = ['it1.info = "release dates"'], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id'], filters = [], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['kind', 'id'], filters = ['(kt.kind = "movie")'], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id', 'company_type_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['movie_id', 'note', 'info', 'info_type_id'], filters = ['mi.note LIKE "%internet%"', 'mi.info IS NULL)', '(mi.info LIKE "USA:% 199%" OR mi.info LIKE "USA:% 200%")'], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['movie_id', 'keyword_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['kind_id', 'production_year', 'id'], filters = ['t.production_year > 2000'], projections = [])
	relations = [cc, cct1, cn, ct, it1, k, kt, mc, mi, mk, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, cc, ["id"], ["movie_id"])
	j2 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j3 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j4 = Join(mi, cc, ["movie_id"], ["movie_id"])
	j5 = Join(k, mk, ["id"], ["keyword_id"])
	j6 = Join(it1, mi, ["id"], ["info_type_id"])
	j7 = Join(cn, mc, ["id"], ["company_id"])
	j8 = Join(ct, mc, ["id"], ["company_type_id"])
	j9 = Join(cct1, cc, ["id"], ["status_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q24a():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id'], filters = [], projections = [])
	chn = Relation(name = "char_name", alias = "chn", attributes = ['id'], filters = [], projections = [])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['note', 'person_role_id', 'movie_id', 'role_id', 'person_id'], filters = ['(ci.note = "(voice)" OR ci.note = "(voice: Japanese version)" OR ci.note = "(voice) (uncredited)" OR ci.note = "(voice: English version)")'], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ['cn.country_code ="[us]"'], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['info', 'id'], filters = ['it.info = "release dates"'], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['keyword', 'id'], filters = ['(k.keyword = "hero" OR k.keyword = "martial-arts" OR k.keyword = "hand-to-hand-combat")'], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['movie_id', 'info', 'info_type_id'], filters = ['mi.info IS NULL', '(mi.info LIKE "Japan:%201%" OR mi.info LIKE "USA:%201%")'], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['movie_id', 'keyword_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['gender', 'name', 'id'], filters = ['n.gender ="f"', 'n.name LIKE "%An%"'], projections = [])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['role', 'id'], filters = ['rt.role ="actress"'], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id'], filters = ['t.production_year > 2010'], projections = [])
	relations = [an, chn, ci, cn, it, k, mc, mi, mk, n, rt, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(t, mk, ["id"], ["movie_id"])
	j4 = Join(cn, mc, ["id"], ["company_id"])
	j5 = Join(it, mi, ["id"], ["info_type_id"])
	j6 = Join(n, ci, ["id"], ["person_id"])
	j7 = Join(rt, ci, ["id"], ["role_id"])
	j8 = Join(ci, an, ["person_id"], ["person_id"])
	j9 = Join(chn, ci, ["id"], ["person_role_id"])
	j10 = Join(k, mk, ["id"], ["keyword_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10]

	return JoinGraph(relations, joins)

def create_q25b():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['movie_id', 'note', 'person_id'], filters = ['(ci.note = "(writer)" OR ci.note = "(head writer)" OR ci.note = "(written by)" OR ci.note = "(story)" OR ci.note = "(story editor)")'], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['info', 'id'], filters = ['it1.info = "genres"'], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['info', 'id'], filters = ['it2.info = "votes"'], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['keyword', 'id'], filters = ['(k.keyword = "murder" OR k.keyword = "blood" OR k.keyword = "gore" OR k.keyword = "death" OR k.keyword = "female-nudity")'], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['movie_id', 'info', 'info_type_id'], filters = ['mi.info = "Horror"'], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['movie_id', 'info_type_id'], filters = [], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['movie_id', 'keyword_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['gender', 'id'], filters = ['n.gender = "m"'], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['title', 'production_year', 'id'], filters = ['t.production_year > 2010', 't.title LIKE "Vampire%"'], projections = [])
	relations = [ci, it1, it2, k, mi, mi_idx, mk, n, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(ci, mi, ["movie_id"], ["movie_id"])
	j2 = Join(ci, mi_idx, ["movie_id"], ["movie_id"])
	j3 = Join(mi_idx, mk, ["movie_id"], ["movie_id"])
	j4 = Join(n, ci, ["id"], ["person_id"])
	j5 = Join(it1, mi, ["id"], ["info_type_id"])
	j6 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	j7 = Join(k, mk, ["id"], ["keyword_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q26a():
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['movie_id', 'status_id', 'subject_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['kind', 'id'], filters = ['cct1.kind = "cast"'], projections = [])
	cct2 = Relation(name = "comp_cast_type", alias = "cct2", attributes = ['kind', 'id'], filters = ['cct2.kind LIKE "%complete%"'], projections = [])
	chn = Relation(name = "char_name", alias = "chn", attributes = ['name', 'id'], filters = ['chn.name IS NULL', '(chn.name LIKE "%man%" OR chn.name LIKE "%Man%")'], projections = [])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['movie_id', 'person_id', 'person_role_id'], filters = [], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['info', 'id'], filters = ['it2.info = "rating"'], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['keyword', 'id'], filters = ['(k.keyword = "superhero" OR k.keyword = "marvel-comics" OR k.keyword = "based-on-comic" OR k.keyword = "tv-special" OR k.keyword = "fight" OR k.keyword = "violence" OR k.keyword = "magnet" OR k.keyword = "web" OR k.keyword = "claw" OR k.keyword = "laser")'], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['kind', 'id'], filters = ['kt.kind = "movie"'], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['movie_id', 'info', 'info_type_id'], filters = ['mi_idx.info > "7.0"'], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['movie_id', 'keyword_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['kind_id', 'production_year', 'id'], filters = ['t.production_year > 2000'], projections = [])
	relations = [cc, cct1, cct2, chn, ci, it2, k, kt, mi_idx, mk, n, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mi_idx, ["id"], ["movie_id"])
	j2 = Join(mk, ci, ["movie_id"], ["movie_id"])
	j3 = Join(mk, cc, ["movie_id"], ["movie_id"])
	j4 = Join(ci, mi_idx, ["movie_id"], ["movie_id"])
	j5 = Join(chn, ci, ["id"], ["person_role_id"])
	j6 = Join(n, ci, ["id"], ["person_id"])
	j7 = Join(k, mk, ["id"], ["keyword_id"])
	j8 = Join(cct1, cc, ["id"], ["subject_id"])
	j9 = Join(cct2, cc, ["id"], ["status_id"])
	j10 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10]

	return JoinGraph(relations, joins)

def create_q27a():
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['movie_id', 'status_id', 'subject_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['kind', 'id'], filters = ['(cct1.kind = "cast" OR cct1.kind = "crew")'], projections = [])
	cct2 = Relation(name = "comp_cast_type", alias = "cct2", attributes = ['kind', 'id'], filters = ['cct2.kind = "complete"'], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'country_code', 'id'], filters = ['cn.country_code !="[pl]"', '(cn.name LIKE "%Film%" OR cn.name LIKE "%Warner%")'], projections = [])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['kind', 'id'], filters = ['ct.kind ="production companies"'], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['keyword', 'id'], filters = ['k.keyword ="sequel"'], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['link', 'id'], filters = ['lt.link LIKE "%follow%"'], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'note', 'company_type_id', 'company_id'], filters = ['mc.note IS NULL'], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['movie_id', 'info'], filters = ['(mi.info = "Sweden" OR mi.info = "Germany" OR mi.info = "Swedish" OR mi.info = "German")'], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['movie_id', 'keyword_id'], filters = [], projections = [])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['movie_id', 'link_type_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id'], filters = ['t.production_year >= 1950', 't.production_year <= 2000'], projections = [])
	relations = [cc, cct1, cct2, cn, ct, k, lt, mc, mi, mk, ml, t]

	j0 = Join(lt, ml, ["id"], ["link_type_id"])
	j1 = Join(t, mk, ["id"], ["movie_id"])
	j2 = Join(mk, k, ["keyword_id"], ["id"])
	j3 = Join(t, mc, ["id"], ["movie_id"])
	j4 = Join(mc, ct, ["company_type_id"], ["id"])
	j5 = Join(mc, cn, ["company_id"], ["id"])
	j6 = Join(cct1, cc, ["id"], ["subject_id"])
	j7 = Join(cct2, cc, ["id"], ["status_id"])
	j8 = Join(ml, mk, ["movie_id"], ["movie_id"])
	j9 = Join(ml, cc, ["movie_id"], ["movie_id"])
	j10 = Join(mi, cc, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10]

	return JoinGraph(relations, joins)

def create_q28c():
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['movie_id', 'status_id', 'subject_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['kind', 'id'], filters = ['cct1.kind = "cast"'], projections = [])
	cct2 = Relation(name = "comp_cast_type", alias = "cct2", attributes = ['kind', 'id'], filters = ['cct2.kind = "complete"'], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ['cn.country_code != "[us]"'], projections = [])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id'], filters = [], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['info', 'id'], filters = ['it1.info = "countries"'], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['info', 'id'], filters = ['it2.info = "rating"'], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['keyword', 'id'], filters = ['(k.keyword = "murder" OR k.keyword = "murder-in-title" OR k.keyword = "blood" OR k.keyword = "violence")'], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['kind', 'id'], filters = ['(kt.kind = "movie" OR kt.kind = "episode")'], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'note', 'company_type_id', 'company_id'], filters = ['NOT mc.note LIKE "%(USA)%"', 'mc.note LIKE "%(200%)%"'], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['movie_id', 'info', 'info_type_id'], filters = ['(mi.info = "Sweden" OR mi.info = "Norway" OR mi.info = "Germany" OR mi.info = "Denmark" OR mi.info = "Swedish" OR mi.info = "Danish" OR mi.info = "Norwegian" OR mi.info = "German" OR mi.info = "USA" OR mi.info = "American")'], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['movie_id', 'info', 'info_type_id'], filters = ['mi_idx.info < "8.5"'], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['movie_id', 'keyword_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['kind_id', 'production_year', 'id'], filters = ['t.production_year > 2005'], projections = [])
	relations = [cc, cct1, cct2, cn, ct, it1, it2, k, kt, mc, mi, mi_idx, mk, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(mk, mi_idx, ["movie_id"], ["movie_id"])
	j3 = Join(mi, cc, ["movie_id"], ["movie_id"])
	j4 = Join(mc, mi_idx, ["movie_id"], ["movie_id"])
	j5 = Join(mc, cc, ["movie_id"], ["movie_id"])
	j6 = Join(k, mk, ["id"], ["keyword_id"])
	j7 = Join(it1, mi, ["id"], ["info_type_id"])
	j8 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	j9 = Join(ct, mc, ["id"], ["company_type_id"])
	j10 = Join(cn, mc, ["id"], ["company_id"])
	j11 = Join(cct1, cc, ["id"], ["subject_id"])
	j12 = Join(cct2, cc, ["id"], ["status_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12]

	return JoinGraph(relations, joins)

def create_q30c():
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['movie_id', 'status_id', 'subject_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['kind', 'id'], filters = ['cct1.kind = "cast"'], projections = [])
	cct2 = Relation(name = "comp_cast_type", alias = "cct2", attributes = ['kind', 'id'], filters = ['cct2.kind ="complete+verified"'], projections = [])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['movie_id', 'note', 'person_id'], filters = ['(ci.note = "(writer)" OR ci.note = "(head writer)" OR ci.note = "(written by)" OR ci.note = "(story)" OR ci.note = "(story editor)")'], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['info', 'id'], filters = ['it1.info = "genres"'], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['info', 'id'], filters = ['it2.info = "votes"'], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['keyword', 'id'], filters = ['(k.keyword = "murder" OR k.keyword = "violence" OR k.keyword = "blood" OR k.keyword = "gore" OR k.keyword = "death" OR k.keyword = "female-nudity" OR k.keyword = "hospital")'], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['movie_id', 'info', 'info_type_id'], filters = ['(mi.info = "Horror" OR mi.info = "Action" OR mi.info = "Sci-Fi" OR mi.info = "Thriller" OR mi.info = "Crime" OR mi.info = "War")'], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['movie_id', 'info_type_id'], filters = [], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['movie_id', 'keyword_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['gender', 'id'], filters = ['n.gender = "m"'], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['id'], filters = [], projections = [])
	relations = [cc, cct1, cct2, ci, it1, it2, k, mi, mi_idx, mk, n, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(ci, mi_idx, ["movie_id"], ["movie_id"])
	j2 = Join(ci, cc, ["movie_id"], ["movie_id"])
	j3 = Join(mi, mk, ["movie_id"], ["movie_id"])
	j4 = Join(mi_idx, mk, ["movie_id"], ["movie_id"])
	j5 = Join(n, ci, ["id"], ["person_id"])
	j6 = Join(it1, mi, ["id"], ["info_type_id"])
	j7 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	j8 = Join(k, mk, ["id"], ["keyword_id"])
	j9 = Join(cct1, cc, ["id"], ["subject_id"])
	j10 = Join(cct2, cc, ["id"], ["status_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10]

	return JoinGraph(relations, joins)

def create_q31a():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['movie_id', 'note', 'person_id'], filters = ['(ci.note = "(writer)" OR ci.note = "(head writer)" OR ci.note = "(written by)" OR ci.note = "(story)" OR ci.note = "(story editor)")'], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id'], filters = ['cn.name LIKE "Lionsgate%"'], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['info', 'id'], filters = ['it1.info = "genres"'], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['info', 'id'], filters = ['it2.info = "votes"'], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['keyword', 'id'], filters = ['(k.keyword = "murder" OR k.keyword = "violence" OR k.keyword = "blood" OR k.keyword = "gore" OR k.keyword = "death" OR k.keyword = "female-nudity" OR k.keyword = "hospital")'], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['movie_id', 'info', 'info_type_id'], filters = ['(mi.info = "Horror" OR mi.info = "Thriller")'], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['movie_id', 'info_type_id'], filters = [], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['movie_id', 'keyword_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['gender', 'id'], filters = ['n.gender = "m"'], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['id'], filters = [], projections = [])
	relations = [ci, cn, it1, it2, k, mc, mi, mi_idx, mk, n, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(ci, mi_idx, ["movie_id"], ["movie_id"])
	j2 = Join(mi, mc, ["movie_id"], ["movie_id"])
	j3 = Join(mi_idx, mk, ["movie_id"], ["movie_id"])
	j4 = Join(mi_idx, mc, ["movie_id"], ["movie_id"])
	j5 = Join(n, ci, ["id"], ["person_id"])
	j6 = Join(it1, mi, ["id"], ["info_type_id"])
	j7 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	j8 = Join(k, mk, ["id"], ["keyword_id"])
	j9 = Join(cn, mc, ["id"], ["company_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q33c():
	cn1 = Relation(name = "company_name", alias = "cn1", attributes = ['country_code', 'id'], filters = ['cn1.country_code != "[us]"'], projections = [])
	cn2 = Relation(name = "company_name", alias = "cn2", attributes = ['id'], filters = [], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['info', 'id'], filters = ['it1.info = "rating"'], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['info', 'id'], filters = ['it2.info = "rating"'], projections = [])
	kt1 = Relation(name = "kind_type", alias = "kt1", attributes = ['kind', 'id'], filters = ['(kt1.kind = "tv series" OR kt1.kind = "episode")'], projections = [])
	kt2 = Relation(name = "kind_type", alias = "kt2", attributes = ['kind', 'id'], filters = ['(kt2.kind = "tv series" OR kt2.kind = "episode")'], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['link', 'id'], filters = ['(lt.link = "sequel" OR lt.link = "follows" OR lt.link = "followed by")'], projections = [])
	mc1 = Relation(name = "movie_companies", alias = "mc1", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mc2 = Relation(name = "movie_companies", alias = "mc2", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mi_idx1 = Relation(name = "movie_info_idx", alias = "mi_idx1", attributes = ['info_type_id', 'movie_id'], filters = [], projections = [])
	mi_idx2 = Relation(name = "movie_info_idx", alias = "mi_idx2", attributes = ['info_type_id', 'movie_id', 'info'], filters = ['mi_idx2.info < "3.5"'], projections = [])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['movie_id', 'linked_movie_id', 'link_type_id'], filters = [], projections = [])
	t1 = Relation(name = "title", alias = "t1", attributes = ['kind_id', 'id'], filters = [], projections = [])
	t2 = Relation(name = "title", alias = "t2", attributes = ['kind_id', 'production_year', 'id'], filters = ['t2.production_year >= 2000', 't2.production_year <= 2010'], projections = [])
	relations = [cn1, cn2, it1, it2, kt1, kt2, lt, mc1, mc2, mi_idx1, mi_idx2, ml, t1, t2]

	j0 = Join(lt, ml, ["id"], ["link_type_id"])
	j1 = Join(t1, ml, ["id"], ["movie_id"])
	j2 = Join(it1, mi_idx1, ["id"], ["info_type_id"])
	j3 = Join(t1, mi_idx1, ["id"], ["movie_id"])
	j4 = Join(kt1, t1, ["id"], ["kind_id"])
	j5 = Join(cn1, mc1, ["id"], ["company_id"])
	j6 = Join(t1, mc1, ["id"], ["movie_id"])
	j7 = Join(it2, mi_idx2, ["id"], ["info_type_id"])
	j8 = Join(t2, mi_idx2, ["id"], ["movie_id"])
	j9 = Join(kt2, t2, ["id"], ["kind_id"])
	j10 = Join(cn2, mc2, ["id"], ["company_id"])
	j11 = Join(ml, mi_idx2, ["linked_movie_id"], ["movie_id"])
	j12 = Join(mi_idx2, mc2, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12]

	return JoinGraph(relations, joins)

