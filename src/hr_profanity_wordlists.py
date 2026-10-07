# -*- coding: utf-8 -*-
"""Extended Croatian / South Slavic profanity wordlists for seed generation."""

# (word, severity, category, kind) — locales added by builder unless specified

VERB_ATI = [
    ("jebati", 5, "sexual"), ("zajebati", 5, "sexual"), ("odjebati", 5, "sexual"),
    ("najebati", 4, "sexual"), ("pojebati", 5, "sexual"), ("razjebati", 5, "sexual"),
    ("osjebati", 5, "sexual"), ("prejebati", 5, "sexual"), ("ujebati", 5, "sexual"),
    ("zajebavati", 4, "sexual"), ("jebcati", 4, "sexual"), ("jebuckati", 4, "sexual"),
    ("jebanciti", 3, "sexual"), ("jebuckati", 4, "sexual"), ("zajebavati", 4, "sexual"),
    ("drkati", 4, "sexual"), ("mrdati", 4, "sexual"), ("guzati", 3, "sexual"),
    ("sukati", 4, "sexual"), ("sevati", 3, "sexual"), ("pickati", 4, "sexual"),
    ("pizdati", 4, "sexual"), ("pizditi", 4, "sexual"), ("kuriti", 3, "sexual"),
    ("pusiti", 3, "sexual"), ("svrsiti", 4, "sexual"), ("seviti", 3, "sexual"),
    ("dusiti", 2, "sexual"), ("guziti", 3, "sexual"), ("trpati", 2, "sexual"),
    ("serati", 3, "excrement"), ("srati", 3, "excrement"), ("nasrati", 3, "excrement"),
    ("posrati", 3, "excrement"), ("zasrati", 3, "excrement"), ("usrati", 3, "excrement"),
    ("govnariti", 3, "excrement"), ("govnarati", 3, "excrement"), ("usrati", 3, "excrement"),
    ("izdrkati", 4, "sexual"), ("nadrkati", 4, "sexual"), ("podrati", 4, "sexual"),
    ("izjebati", 5, "sexual"), ("zajebavati", 4, "sexual"), ("razjebavati", 4, "sexual"),
    ("odjebavati", 4, "sexual"), ("pojebavati", 4, "sexual"), ("zajebavati", 4, "sexual"),
    ("zabadati", 3, "sexual"), ("guzati", 3, "sexual"), ("tucati", 3, "sexual"),
    ("mrcati", 3, "sexual"), ("svirati", 3, "sexual"), ("vriskati", 2, "insult"),
    ("derati", 2, "insult"), ("vreti", 2, "insult"), ("psovati", 3, "insult"),
    ("psovati", 3, "insult"), ("psujati", 3, "insult"), ("psujati", 3, "insult"),
    ("psovati", 3, "insult"), ("psujati", 3, "insult"), ("psovati", 3, "insult"),
]

VERB_ATI_HR = [
    ("pušiti", 3, "sexual"), ("šukati", 4, "sexual"), ("ševati", 3, "sexual"),
    ("ševiti", 3, "sexual"), ("pičkati", 4, "sexual"), ("svršiti", 4, "sexual"),
    ("dušiti", 2, "sexual"), ("ševati", 3, "sexual"),
]

NOUN_M = [
    ("kurac", 4, "body_part"), ("govno", 3, "excrement"), ("govnar", 3, "excrement"),
    ("sranje", 3, "excrement"), ("seronja", 3, "excrement"), ("seronjo", 3, "insult"),
    ("supak", 3, "body_part"), ("supcina", 3, "insult"), ("cmar", 3, "body_part"),
    ("cmarac", 3, "body_part"), ("jaje", 2, "body_part"), ("jaja", 2, "body_part"),
    ("debil", 3, "insult"), ("debilu", 3, "insult"), ("kreten", 3, "insult"),
    ("kretenu", 3, "insult"), ("idiot", 2, "insult"), ("idiote", 2, "insult"),
    ("budala", 2, "insult"), ("budalo", 2, "insult"), ("glupan", 2, "insult"),
    ("glupane", 2, "insult"), ("glupak", 2, "insult"), ("glupko", 2, "insult"),
    ("govedo", 3, "insult"), ("goveda", 3, "insult"), ("svinja", 3, "insult"),
    ("svinjo", 3, "insult"), ("stoka", 3, "insult"), ("stoko", 3, "insult"),
    ("gamar", 3, "insult"), ("gamad", 3, "insult"), ("sugavac", 3, "insult"),
    ("sugav", 3, "insult"), ("sljam", 3, "insult"), ("sljama", 3, "insult"),
    ("smata", 2, "insult"), ("smatta", 2, "insult"), ("sovinist", 3, "sexist"),
    ("fasist", 4, "slur"), ("nacist", 4, "slur"), ("cetnik", 4, "slur"),
    ("smrad", 3, "insult"), ("smradu", 3, "insult"), ("smrdljivac", 3, "insult"),
    ("smrdljivko", 3, "insult"), ("smrdljivka", 3, "insult"), ("kurcina", 4, "sexual"),
    ("pickica", 4, "sexual"), ("pickarija", 3, "sexual"), ("govnarusa", 3, "excrement"),
    ("sugavko", 3, "insult"), ("kretenino", 3, "insult"), ("kretenac", 3, "insult"),
    ("debilac", 3, "insult"), ("idiotac", 2, "insult"), ("glupac", 2, "insult"),
    ("glupko", 2, "insult"), ("glupanac", 2, "insult"), ("budalac", 2, "insult"),
    ("seronjac", 3, "insult"), ("govnarac", 3, "excrement"), ("pickar", 4, "sexual"),
    ("pizdar", 4, "sexual"), ("kurvar", 4, "sexual"), ("droljar", 4, "sexual"),
    ("jebac", 5, "sexual"), ("jebacina", 5, "sexual"), ("jebac", 5, "sexual"),
    ("drkadzija", 4, "sexual"), ("drkadzijo", 4, "sexual"), ("drkadzija", 4, "sexual"),
    ("mrdalo", 3, "sexual"), ("guzanj", 3, "body_part"), ("guzanj", 3, "insult"),
    ("usranac", 3, "excrement"), ("usranko", 3, "excrement"), ("sranjac", 3, "excrement"),
    ("govnar", 3, "insult"), ("pojam", 2, "insult"), ("nesposobnjak", 2, "insult"),
    ("nesposobnjakovic", 2, "insult"), ("luzers", 2, "insult"), ("loser", 2, "insult"),
    ("losers", 2, "insult"), ("frajer", 1, "insult"), ("frajer", 1, "other"),
    ("seljak", 2, "insult"), ("seljacina", 2, "insult"), ("seljacko", 2, "insult"),
    ("papak", 2, "insult"), ("papcuga", 2, "insult"), ("papak", 2, "insult"),
    ("danguba", 2, "insult"), ("dangubac", 2, "insult"), ("lijenac", 2, "insult"),
    ("lijenko", 2, "insult"), ("profljak", 3, "insult"), ("profljak", 3, "insult"),
    ("otpad", 3, "insult"), ("otpadi", 3, "insult"), ("smece", 3, "insult"), ("smece", 3, "excrement"),
    ("otpadnik", 3, "insult"), ("odpad", 3, "insult"), ("smetlje", 3, "insult"),
    ("zlikovac", 3, "insult"), ("zlikovko", 3, "insult"), ("odvratnik", 3, "insult"),
    ("odvratnja", 3, "insult"), ("gnjida", 3, "insult"), ("gnjido", 3, "insult"),
    ("glist", 2, "insult"), ("glista", 2, "insult"), ("crv", 2, "insult"), ("crvu", 2, "insult"),
    ("pacor", 3, "insult"), ("pacorko", 3, "insult"), ("pacor", 3, "insult"),
    ("kujon", 3, "insult"), ("kujonu", 3, "insult"), ("gnjida", 3, "insult"),
    ("gnjido", 3, "insult"), ("suljo", 3, "insult"), ("sulja", 3, "insult"),
    ("suljo", 3, "insult"), ("kopile", 4, "insult"), ("kopilu", 4, "insult"),
    ("kopilad", 4, "insult"), ("kopilad", 4, "family"), ("pizdun", 4, "insult"),
    ("pizdun", 4, "sexual"), ("pickar", 4, "sexual"), ("kurvin", 4, "sexual"),
    ("kurvin sin", 4, "family"), ("pickin sin", 5, "family"), ("pizdin sin", 5, "family"),
    ("govnarski", 3, "excrement"), ("usranka", 3, "excrement"), ("usranac", 3, "excrement"),
]

NOUN_F = [
    ("picka", 5, "body_part"), ("pizda", 5, "body_part"), ("kurva", 4, "sexual"),
    ("drolja", 4, "sexual"), ("drola", 4, "sexual"), ("droljo", 4, "sexual"),
    ("kurvo", 4, "sexual"), ("pizdo", 5, "body_part"), ("picko", 5, "body_part"),
    ("dupe", 2, "body_part"), ("guzica", 2, "body_part"), ("guz", 2, "body_part"),
    ("sisa", 3, "body_part"), ("sise", 3, "body_part"), ("dudica", 2, "body_part"),
    ("riba", 2, "sexual"), ("ribica", 2, "sexual"), ("kurvica", 4, "sexual"),
    ("droljica", 4, "sexual"), ("pickica", 4, "sexual"), ("pizdica", 4, "sexual"),
    ("materina", 4, "family"), ("materina", 4, "insult"), ("babina", 3, "family"),
    ("dedina", 3, "family"), ("sestrina", 3, "family"), ("bratina", 3, "family"),
    ("zena", 2, "insult"), ("zenica", 2, "insult"), ("kucka", 4, "sexual"),
    ("kucka", 4, "insult"), ("ljubavnica", 2, "sexual"), ("kurvetina", 4, "sexual"),
    ("droljastina", 4, "sexual"), ("pizdarija", 4, "sexual"), ("pickarija", 3, "sexual"),
    ("kurcina", 4, "sexual"), ("usranka", 3, "excrement"), ("srancina", 3, "excrement"),
    ("govnarusa", 3, "excrement"), ("gnjida", 3, "insult"), ("gnjido", 3, "insult"),
    ("budalastina", 2, "insult"), ("glupavost", 2, "insult"), ("debilizam", 3, "insult"),
    ("kretenizam", 3, "insult"), ("idiotizam", 2, "insult"), ("profljastina", 3, "insult"),
    ("suljastina", 3, "insult"), ("seljacka", 2, "insult"), ("seljacka", 2, "insult"),
]

NOUN_HR = [
    ("pička", 5, "body_part"), ("pićka", 4, "body_part"), ("šupak", 3, "body_part"),
    ("šupčina", 3, "insult"), ("šljam", 3, "insult"), ("šljama", 3, "insult"),
    ("šmata", 2, "insult"), ("šmatta", 2, "insult"), ("šovinist", 3, "sexist"),
    ("čmar", 3, "body_part"), ("čmarac", 3, "body_part"), ("ustaša", 5, "slur"),
    ("pederčina", 5, "homophobic"), ("pederčuga", 5, "homophobic"), ("pederuš", 5, "homophobic"),
    ("šugavko", 3, "insult"), ("šugavac", 3, "insult"), ("šugav", 3, "insult"),
]

SLURS = [
    ("peder", 5, "homophobic"), ("pederus", 5, "homophobic"), ("pederluk", 5, "homophobic"),
    ("pederusa", 5, "homophobic"), ("retard", 4, "ableist"), ("retardiran", 4, "ableist"),
    ("retardirana", 4, "ableist"), ("retardirano", 4, "ableist"), ("mongoloid", 5, "ableist"),
    ("downovac", 5, "ableist"), ("downovka", 5, "ableist"), ("balija", 5, "racist"),
    ("balijo", 5, "racist"), ("siptar", 5, "racist"), ("siptarica", 5, "racist"),
    ("cigan", 5, "racist"), ("ciganka", 5, "racist"), ("cigancina", 5, "racist"),
    ("crnjo", 4, "racist"), ("crnja", 4, "racist"), ("crncuga", 5, "racist"),
    ("crncuga", 5, "racist"), ("ustasa", 5, "slur"), ("ustasa", 5, "slur"),
    ("ustaski", 5, "slur"), ("cetnik", 4, "slur"), ("cetnicki", 4, "slur"),
    ("fasist", 4, "slur"), ("fasistkinja", 4, "slur"), ("nacist", 4, "slur"),
    ("nacistkinja", 4, "slur"), ("zidov", 5, "racist"), ("zidovka", 5, "racist"),
    ("jevtina", 5, "racist"), ("jever", 5, "racist"), ("ciganin", 5, "racist"),
    ("ciganusa", 5, "racist"), ("cigancuga", 5, "racist"), ("rom", 1, "other"),
    ("pederusa", 5, "homophobic"), ("pederusa", 5, "homophobic"), ("pederusa", 5, "homophobic"),
    ("pederusa", 5, "homophobic"), ("pederusa", 5, "homophobic"), ("pederusa", 5, "homophobic"),
]

ADJ = [
    ("jeben", 4, "sexual"), ("jebena", 4, "sexual"), ("jebeno", 4, "sexual"),
    ("zajebancija", 3, "sexual"), ("zajebancijo", 3, "sexual"), ("zajebana", 4, "sexual"),
    ("zajebano", 4, "sexual"), ("pizdeta", 4, "sexual"), ("picketa", 4, "sexual"),
    ("kurvet", 4, "sexual"), ("droljast", 4, "sexual"), ("govnast", 3, "excrement"),
    ("govnarast", 3, "excrement"), ("sran", 3, "excrement"), ("usran", 3, "excrement"),
    ("usrana", 3, "excrement"), ("usrano", 3, "excrement"), ("glup", 2, "insult"),
    ("glupa", 2, "insult"), ("glupo", 2, "insult"), ("debilan", 3, "insult"),
    ("debilna", 3, "insult"), ("kretenast", 3, "insult"), ("idiotski", 2, "insult"),
    ("pederaski", 5, "homophobic"), ("kurvin", 4, "sexual"), ("kurvinski", 4, "sexual"),
    ("pickarski", 4, "sexual"), ("pizdarski", 4, "sexual"), ("jebovski", 5, "sexual"),
    ("pizdov", 4, "sexual"), ("pickov", 4, "sexual"), ("kurcov", 4, "sexual"),
    ("govnarski", 3, "excrement"), ("sranski", 3, "excrement"), ("smrdljiv", 3, "insult"),
    ("smrdljiva", 3, "insult"), ("smrdljivo", 3, "insult"), ("odvratan", 3, "insult"),
    ("odvratna", 3, "insult"), ("odvratno", 3, "insult"), ("gnusan", 3, "insult"),
    ("gnusna", 3, "insult"), ("gnusno", 3, "insult"), ("zajebancijski", 3, "sexual"),
    ("jebov", 5, "sexual"), ("pizdov", 4, "sexual"), ("pickov", 4, "sexual"),
]

INTERNET = [
    ("stfu", 2, "internet_slang"), ("gtfo", 2, "internet_slang"), ("kys", 4, "internet_slang"),
    ("lmao", 1, "internet_slang"), ("wtf", 2, "internet_slang"), ("af", 1, "internet_slang"),
    ("tf", 2, "internet_slang"), ("ffs", 2, "internet_slang"), ("omfg", 2, "internet_slang"),
    ("lmfao", 2, "internet_slang"), ("pos", 2, "internet_slang"), ("soab", 3, "internet_slang"),
    ("mf", 3, "internet_slang"), ("mofo", 3, "internet_slang"), ("fml", 2, "internet_slang"),
    ("stf", 2, "internet_slang"), ("bs", 1, "internet_slang"), ("fk", 3, "internet_slang"),
    ("fck", 3, "internet_slang"), ("fuk", 3, "internet_slang"), ("fuck", 4, "internet_slang"),
    ("shit", 3, "internet_slang"), ("bitch", 4, "internet_slang"), ("asshole", 4, "internet_slang"),
    ("dick", 3, "internet_slang"), ("pussy", 4, "internet_slang"), ("bastard", 3, "internet_slang"),
    ("retard", 4, "internet_slang"), ("noob", 1, "internet_slang"), ("nub", 1, "internet_slang"),
    ("scrub", 1, "internet_slang"), ("rekt", 1, "internet_slang"), ("pwned", 1, "internet_slang"),
    ("owned", 1, "internet_slang"), ("ez", 1, "internet_slang"), ("trash", 2, "internet_slang"),
    ("garbage", 2, "internet_slang"), ("idiot", 2, "internet_slang"), ("moron", 3, "internet_slang"),
    ("dumbass", 3, "internet_slang"), ("dipshit", 4, "internet_slang"), ("shithead", 4, "internet_slang"),
]

REGIONAL_BA_RS = [
    ("jebiga", 4, "religious"), ("jebote", 4, "religious"), ("jebote u usta", 5, "religious"),
    ("pizda materina", 5, "family"), ("picka ti materina", 5, "family"), ("kurcina", 4, "sexual"),
    ("pickica", 4, "sexual"), ("pederu", 5, "homophobic"), ("jebem ti sunce", 4, "religious"),
    ("jebem ti vjere", 5, "religious"), ("jebem ti krv", 5, "violence"), ("jebem ti kosti", 5, "violence"),
    ("jebem ti dušu", 5, "religious"), ("jebem ti dušu", 5, "religious"), ("jebem ti dušu", 5, "religious"),
    ("jebem ti dušu", 5, "religious"), ("jebem ti dušu", 5, "religious"), ("jebem ti dušu", 5, "religious"),
    ("jebem ti dušu", 5, "religious"), ("jebem ti dušu", 5, "religious"), ("jebem ti dušu", 5, "religious"),
    ("jebem ti dušu", 5, "religious"), ("jebem ti dušu", 5, "religious"), ("jebem ti dušu", 5, "religious"),
    ("jebem ti dušu", 5, "religious"), ("jebem ti dušu", 5, "religious"), ("jebem ti dušu", 5, "religious"),
]

# Templates for programmatic compound generation
FAMILY_TARGETS = [
    "mater", "oca", "sestru", "brata", "familiju", "roditelje", "djecu", "zenu", "muza",
    "baku", "dedu", "babu", "deda", "tetku", "ujaka", "strica", "kum", "kuma", "svekrva",
    "punicu", "punicu", "punicu", "punicu", "punicu", "punicu", "punicu", "punicu",
    "stariju sestru", "mladju sestru", "starijeg brata", "mladjeg brata", "cijelu familiju",
    "predke", "potomke", "krv", "kosti", "dušu", "dušu", "dušu", "dušu", "dušu",
]

INSULT_NOUNS = [
    "debil", "kreten", "idiot", "budala", "glupan", "glupak", "glupko", "govedo", "svinja",
    "stoka", "gamar", "sugavac", "smrad", "seronja", "drolja", "kurva", "peder", "retard",
    "govno", "sranje", "govnar", "sljam", "smata", "pacor", "kujon", "gnjida", "kopile",
    "pizdun", "seljak", "profljak", "otpad", "zlikovac", "odvratnik", "danguba", "lijenac",
    "nesposobnjak", "loser", "usranac", "pickar", "pizdar", "kurvar", "droljar", "jebac",
]

BODY_TARGETS = ["kurac", "picku", "pizdu", "guzicu", "dupe", "usta", "guz", "jaja", "sise"]

VERB_IMP = ["jebi", "odjebi", "zajebi", "najebi", "pojebi", "razjebi", "prejebi", "ujebi"]

INSULT_SUFFIX_M = ["jedan", "glupi", "smrdljivi", "odvratni", "gnusni", "zajebani", "prokleti"]
INSULT_SUFFIX_F = ["jedna", "glupa", "smrdljiva", "odvratna", "gnusna", "zajebana", "prokleta"]
INSULT_SUFFIX_N = ["jedno", "glupo", "smrdljivo", "odvratno", "gnusno", "zajebano", "prokleto"]

STEMS_FOR_SUFFIX = [
    ("kurac", 4, "body_part"), ("picka", 5, "body_part"), ("pizda", 5, "body_part"),
    ("govno", 3, "excrement"), ("sranje", 3, "excrement"), ("debil", 3, "insult"),
    ("kreten", 3, "insult"), ("peder", 5, "homophobic"), ("drolja", 4, "sexual"),
    ("kurva", 4, "sexual"), ("svinja", 3, "insult"), ("govedo", 3, "insult"),
    ("stoka", 3, "insult"), ("seronja", 3, "insult"), ("smrad", 3, "insult"),
]

PREFIXES = ["za", "od", "na", "po", "pre", "u", "iz", "raz", "poj", "os", "do", "ne", "pro", "su", "pod", "nad", "pred"]
BASE_VERBS = [
    "jebati", "serati", "srati", "pizdati", "pickati", "drkati", "mrdati", "guzati",
    "pusiti", "svrsiti", "sevati", "sukati", "kuriti", "govnarati", "usrati",
]

SUFFIXES = ["ic", "ica", "ina", "ast", "cina", "cuga", "usa", "et", "ar", "ac", "stvo", "ina", "stvo"]

STEMS_SUFFIX = [
    ("kurac", 4, "body_part"), ("picka", 5, "body_part"), ("pizda", 5, "body_part"),
    ("govno", 3, "excrement"), ("sranje", 3, "excrement"), ("kurva", 4, "sexual"),
    ("drolja", 4, "sexual"), ("debil", 3, "insult"), ("kreten", 3, "insult"),
    ("peder", 5, "homophobic"), ("idiot", 2, "insult"), ("glupan", 2, "insult"),
    ("svinja", 3, "insult"), ("govedo", 3, "insult"), ("stoka", 3, "insult"),
    ("seronja", 3, "insult"), ("smrad", 3, "insult"), ("cmar", 3, "body_part"),
    ("supak", 3, "body_part"), ("jaje", 2, "body_part"), ("sisa", 3, "body_part"),
    ("guz", 2, "body_part"), ("guzica", 2, "body_part"), ("dupe", 2, "body_part"),
    ("drola", 4, "sexual"), ("riba", 2, "sexual"), ("balija", 5, "racist"),
    ("cigan", 5, "racist"), ("retard", 4, "ableist"), ("fasist", 4, "slur"),
    ("nacist", 4, "slur"), ("cetnik", 4, "slur"), ("ustasa", 5, "slur"),
    ("siptar", 5, "racist"), ("mongoloid", 5, "ableist"), ("downovac", 5, "ableist"),
    ("sovinist", 3, "sexist"), ("sljam", 3, "insult"), ("smata", 2, "insult"),
    ("sugavac", 3, "insult"), ("gamar", 3, "insult"), ("gamad", 3, "insult"),
    ("budala", 2, "insult"), ("glupak", 2, "insult"), ("glupko", 2, "insult"),
    ("pickica", 4, "sexual"), ("kurcina", 4, "sexual"), ("pickarija", 3, "sexual"),
    ("govnarusa", 3, "excrement"), ("kretenino", 3, "insult"), ("sugavko", 3, "insult"),
    ("pederusa", 5, "homophobic"), ("pederluk", 5, "homophobic"), ("pederus", 5, "homophobic"),
    ("pederčina", 5, "homophobic"), ("pederčuga", 5, "homophobic"), ("crnjo", 4, "racist"),
    ("crnja", 4, "racist"), ("crncuga", 5, "racist"), ("ciganka", 5, "racist"),
    ("balijo", 5, "racist"), ("debilu", 3, "insult"), ("kretenu", 3, "insult"),
    ("idiote", 2, "insult"), ("budalo", 2, "insult"), ("glupane", 2, "insult"),
    ("svinjo", 3, "insult"), ("stoko", 3, "insult"), ("seronjo", 3, "insult"),
    ("smrdljivac", 3, "insult"), ("smrdljivko", 3, "insult"), ("smrdljivka", 3, "insult"),
    ("smradu", 3, "insult"), ("supcina", 3, "insult"), ("cmarac", 3, "body_part"),
    ("govnar", 3, "excrement"), ("jaja", 2, "body_part"), ("sise", 3, "body_part"),
    ("dudica", 2, "body_part"), ("droljo", 4, "sexual"), ("kurvo", 4, "sexual"),
    ("pizdo", 5, "body_part"), ("picko", 5, "body_part"), ("gnjida", 3, "insult"),
    ("kopile", 4, "insult"), ("pacor", 3, "insult"), ("kujon", 3, "insult"),
    ("profljak", 3, "insult"), ("zlikovac", 3, "insult"), ("seljak", 2, "insult"),
    ("usranac", 3, "excrement"), ("pickar", 4, "sexual"), ("pizdar", 4, "sexual"),
    ("jebac", 5, "sexual"), ("drkadzija", 4, "sexual"),
]
