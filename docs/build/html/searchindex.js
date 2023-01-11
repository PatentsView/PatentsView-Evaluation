Search.setIndex({"docnames": ["concepts", "examples", "examples/estimators/binette-2022-benchmark", "examples/estimators/lai-2011-benchmark", "examples/estimators/performance-history", "examples/hand-disambiguation/creating-inventors-benchmark", "examples/summary/summary-history", "examples/templates/templates", "index", "modules", "pv_evaluation", "pv_evaluation.benchmark", "pv_evaluation.templates", "readme"], "filenames": ["concepts.ipynb", "examples.rst", "examples/estimators/binette-2022-benchmark.ipynb", "examples/estimators/lai-2011-benchmark.ipynb", "examples/estimators/performance-history.ipynb", "examples/hand-disambiguation/creating-inventors-benchmark.ipynb", "examples/summary/summary-history.ipynb", "examples/templates/templates.ipynb", "index.rst", "modules.rst", "pv_evaluation.rst", "pv_evaluation.benchmark.rst", "pv_evaluation.templates.rst", "readme.rst"], "titles": ["Key Concepts", "Examples", "\ud83c\udfaf Performance Estimates for Binette\u2019s 2022 Benchmark", "\ud83c\udfaf Performance Estimates for Lai\u2019s 2011 Benchmark", "Disambiguation Performance History", "\u270d\ufe0f Creating Inventors Benchmark Datasets by Hand", "Summary Statistics History", "\ud83d\udcd1 HTML Report Template", "PatentsView-Evaluation\u2019s documentation", "pv_evaluation", "API Doc", "pv_evaluation.benchmark", "pv_evaluation.templates", "README"], "terms": {"thi": [0, 2, 3, 4, 5, 6, 7, 11, 12, 13], "page": [0, 5, 8, 13], "highlight": [0, 11], "terminologi": 0, "us": [0, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13], "throughout": [0, 8], "packag": [0, 5, 8, 13], "ar": [0, 4, 5, 7, 11, 12, 13], "assign": [0, 7, 11], "uspto": 0, "follow": [0, 5, 8, 11, 13], "format": [0, 5, 7, 11, 12, 13], "describ": [0, 5, 11], "here": 0, "http": [0, 2, 3, 4, 5, 6, 7, 11, 13], "www": 0, "gov": 0, "appli": 0, "onlin": [0, 11], "_": [0, 13], "note": [0, 2, 3, 5, 7, 11, 12, 13], "lead": 0, "zero": 0, "an": [0, 5, 8, 11, 13], "inventor": [0, 1, 2, 3, 4, 7, 11, 13], "": [0, 1, 5, 6, 7, 11, 12, 13], "i": [0, 2, 3, 4, 5, 6, 8, 11, 13], "refer": [0, 5, 8, 11], "specif": 0, "author": [0, 7, 13], "It": [0, 5, 13], "take": [0, 5], "u": [0, 2, 3, 5, 6, 7, 11, 13], "patent_numb": [0, 5], "sequence_numb": [0, 5], "us12345": 0, "0": [0, 2, 3, 5], "where": [0, 5, 11, 12], "authorship": [0, 11], "first": [0, 2, 3, 4, 5, 6], "1": [0, 2, 3, 5, 7, 11], "second": [0, 4, 5, 6, 7], "etc": 0, "set": [0, 3, 4, 5, 6, 7, 11, 13], "thought": 0, "same": [0, 4, 11], "person": 0, "There": [0, 11], "predict": [0, 5, 11], "which": [0, 3, 4, 5, 11], "provid": [0, 5, 11, 13], "disambigu": [0, 1, 2, 3, 5, 6, 7, 8, 11, 12], "algorithm": [0, 1, 2, 3, 5, 8, 11], "true": [0, 5, 6, 7, 12], "ground": [0, 5], "truth": 0, "A": [0, 5, 7, 11, 13], "typic": [0, 5], "repres": [0, 1, 4, 7, 11], "map": 0, "between": [0, 2, 3, 5, 11, 12], "thei": 0, "associ": [0, 5, 6, 11], "In": [0, 5, 11], "panda": [0, 2, 3, 4, 5, 6, 7, 11], "seri": [0, 3, 11], "index": [0, 3, 5, 7, 11, 13], "valu": [0, 11], "all": [0, 8, 11, 13], "result": [0, 5, 7, 11, 12], "below": [0, 5, 6, 7, 11, 13], "exampl": [0, 5, 7, 8, 11], "subset": [0, 11], "The": [0, 2, 3, 4, 5, 6, 7, 11, 13], "appear": [0, 4], "right": 0, "column": [0, 5, 7, 11, 12], "arbitrari": 0, "onli": [0, 2, 3, 4, 13], "convent": 0, "correspond": [0, 5, 11], "belong": 0, "should": [0, 5, 7, 11, 12, 13], "have": [0, 5, 11, 13], "from": [0, 1, 2, 3, 5, 6, 7, 11, 12, 13], "pv_evalu": [0, 2, 3, 4, 5, 6, 7, 13], "benchmark": [0, 4, 6, 8], "import": [0, 2, 3, 4, 5, 6, 7, 11, 13], "load_israeli_inventors_benchmark": [0, 11, 13], "mention_id": [0, 2, 3, 5, 6, 7, 11, 12], "us3858246": 0, "11797": 0, "us3858578": 0, "us3858674": 0, "16606": 0, "us3859165": 0, "13384": 0, "us3859616": 0, "9865": 0, "us6009346": 0, "12734": 0, "us6009390": 0, "7694": 0, "us6009409": 0, "2": [0, 5, 7, 11], "11416": 0, "us6009543": 0, "19168": 0, "us6009552": 0, "650": 0, "name": [0, 5, 11, 13], "unique_id": 0, "length": 0, "9156": 0, "dtype": [0, 2, 3, 4, 6, 7], "int64": 0, "binett": [1, 4, 11, 13], "2022": [1, 4, 5, 11, 13], "applic": [0, 1, 2, 3], "lai": [1, 11, 13], "2011": [1, 11, 13], "autom": 1, "html": [1, 12, 13], "report": [1, 8, 11, 12], "comparison": [1, 5, 13], "protocol": 1, "process": [0, 1, 2, 3, 5, 11], "script": [1, 5], "notebook": [2, 3, 4, 5, 6, 13], "showcas": [2, 3, 4, 6], "our": [2, 3], "dataset": [2, 3, 11], "cover": [2, 3, 4, 11], "patent": [2, 3, 4, 5, 7, 11, 12, 13], "grant": [2, 3, 4, 7, 11, 12], "befor": [2, 3], "As": [0, 2, 3, 4, 5], "we": [0, 2, 3, 4, 5, 6, 7, 11, 13], "can": [2, 3, 4, 5, 6, 7, 12, 13], "current": [2, 3, 5, 7, 13], "time": [2, 3, 4, 7, 11], "period": [2, 3, 4, 11], "sampl": [2, 3, 5, 11], "assum": [2, 3, 5], "probabl": [2, 3, 5, 11], "proport": [2, 5, 11], "cluster": [2, 3, 5, 7, 11], "size": [2, 5, 11], "becaus": [2, 3], "were": [2, 3, 5, 11], "identifi": [0, 2, 3, 5], "mention": [2, 3, 5, 11], "uniformli": [2, 5, 11], "random": [2, 5, 11], "requir": [2, 3, 7, 13], "modul": [2, 3, 8], "recov": [2, 3, 6], "rawinventor": [2, 3, 5], "tsv": [2, 3, 4, 5, 6, 7, 11, 12, 13], "filter": [2, 3], "contain": [2, 3, 4, 5, 6, 7, 11, 12], "1975": [2, 3, 11], "pd": [2, 3, 4, 5, 6, 7], "numpi": [2, 3], "np": [2, 3], "wget": [2, 3, 4, 5, 6, 7], "zipfil": [2, 3, 4, 6, 7], "o": [2, 3, 4, 5, 6, 7], "path": [2, 3, 4, 6, 7, 12], "isfil": [2, 3, 4, 6, 7], "download": [2, 3, 5, 7, 11, 12], "s3": [2, 3, 4, 5, 6, 7, 11, 13], "amazonaw": [2, 3, 4, 5, 6, 7, 11, 13], "com": [2, 3, 4, 5, 6, 7, 11, 13], "patentsview": [1, 2, 3, 5, 6, 7, 11, 12], "org": [2, 3, 4, 5, 6, 7, 11, 13], "zip": [2, 3, 4, 5, 6, 7, 13], "r": [2, 3, 4, 6, 7, 11], "zip_ref": [2, 3, 4, 6, 7], "extractal": [2, 3, 4, 6, 7], "remov": [2, 3, 4, 5, 6, 7, 11], "read_csv": [2, 3, 4, 5, 6, 7], "sep": [2, 3, 4, 6, 7], "t": [2, 3, 4, 6, 7], "str": [2, 3, 4, 6, 7, 11, 12], "usecol": [2, 3], "id": [2, 3, 7, 11], "date": [2, 3, 4, 7, 11], "patent_id": [2, 3, 4, 5, 6, 7, 11, 12], "sequenc": [0, 2, 3, 5, 7, 11], "inventor_id": [2, 3, 5, 12], "datetimeindex": [2, 3], "year": [2, 3], "astyp": [2, 3], "int": [2, 3, 11], "join": [2, 3], "merg": [2, 3, 4], "left_on": [2, 3], "right_on": [2, 3], "how": [2, 3, 4, 13], "left": [2, 3, 4, 7], "queri": [2, 3, 4, 11], "current_disambigu": [2, 3], "set_index": [2, 3, 6, 7], "now": [2, 3, 4, 6, 7], "uniform": [2, 3], "weight": [2, 3], "er_evalu": [2, 3], "pairwise_precision_design_estim": [2, 3], "pairwise_recall_design_estim": [2, 3], "summari": [2, 12], "cluster_s": 2, "load_binette_2022_inventors_benchmark": [2, 11, 13], "standard": [2, 3, 5, 11, 13], "deviat": [2, 3, 11], "9138044762074496": 2, "018549986866583854": 2, "9637111046011154": 2, "008180601394371729": 2, "2010": [3, 11], "cv": 3, "individu": 3, "would": 3, "bia": [3, 11], "toward": [3, 11], "larg": [3, 13], "load_lai_2011_inventors_benchmark": [3, 11, 13], "uniqu": [0, 3], "9061700591403344": 3, "02694415809739732": 3, "9096034933749487": 3, "05017639288406865": 3, "procedur": [5, 11], "american": [5, 13], "institut": [5, 13], "research": [5, 11, 13], "construct": 5, "ha": [0, 5, 13], "three": 5, "step": 5, "For": [5, 7, 11, 12, 13], "each": [0, 5, 6, 11], "given": [5, 11], "ad": 5, "been": [5, 11], "depend": 5, "baselin": 5, "taken": 5, "case": [5, 11], "error": [5, 11, 13], "found": [5, 11], "correct": [5, 11], "order": [0, 5], "find": [5, 11], "conveni": [5, 13], "interfac": 5, "brows": 5, "3": [5, 7, 11], "search": 5, "tool": 5, "review": [5, 8, 11], "similarli": [5, 11], "standpoint": 5, "staff": 5, "keep": [5, 12], "track": 5, "excel": 5, "spreadsheet": 5, "one": [5, 12], "row": [5, 11], "well": [5, 11], "number": [5, 11], "part": [0, 5], "add": [5, 7], "append": 5, "comma": [0, 5], "separ": [5, 11], "list": [5, 7, 12], "form": [5, 11], "shown": 5, "read_excel": 5, "07": 5, "25": [5, 7], "emma": [5, 11, 13], "xlsx": 5, "head": 5, "10": [5, 7, 11], "name_first": 5, "name_last": 5, "unnam": 5, "9": [5, 7], "6267035": 5, "fl": 5, "ca_ln": 5, "santizo": 5, "carlo": 5, "gilberto": 5, "nan": 5, "ye": 5, "4690644": 5, "ma_ln": 5, "flander": 5, "marguerita": 5, "e": [5, 11, 13], "10120759": 5, "ar_ln": 5, "gv": 5, "aravind": 5, "5290082": 5, "th_ln": 5, "mealei": 5, "thoma": 5, "p": [5, 11], "4": [5, 7], "re46143": 5, "_ln": 5, "erman": 5, "gregori": 5, "us8561841": 5, "us7475795": 5, "us9296603": 5, "us9738507": 5, "5": [5, 7], "10223669": 5, "to_ln": 5, "geniess": 5, "tom": 5, "6": [5, 7, 11], "6387460": 5, "hi_ln": 5, "yoshizawa": 5, "11": [5, 7], "hideo": 5, "us6993267": 5, "us10895827": 5, "sure": [5, 13], "about": 5, "seem": 5, "like": [5, 11], "glass": 5, "7": [5, 7], "5928343": 5, "horowitz": 5, "mark": 5, "us7736282": 5, "few": [5, 11], "abnorm": 5, "assigne": [5, 11, 13], "8": [5, 7], "11009520": 5, "st_ln": 5, "bower": 5, "stewart": 5, "v": [5, 11], "iii": 5, "5467579": 5, "si_ln": 5, "boriani": 5, "silvano": 5, "togeth": [0, 5], "file": [5, 7, 11, 12, 13], "bulk": [5, 6, 7, 11, 12], "data": [5, 6, 11, 12], "look": [5, 13], "do": 5, "exist": 5, "addition": 5, "print": [5, 11, 13], "out": [5, 7], "sheet": 5, "wai": [0, 5], "obviou": 5, "flag": 5, "done": [0, 5, 7, 11], "py": 5, "instal": [5, 8], "next": 5, "run": [5, 12, 13], "debug": 5, "mode": 5, "produc": [5, 11], "bash": 5, "pip": [5, 13], "q": 5, "git": 5, "github": [5, 7, 13], "evalu": [0, 5, 7, 11], "releas": [5, 13], "nc": 5, "nv": 5, "unzip": 5, "n": [5, 11, 13], "archiv": 5, "true_clust": 5, "csv": [5, 12], "sheet_nam": 5, "drop": 5, "remove_error": 5, "add_error": 5, "195": 5, "10455291": 5, "jo_ln": 5, "bernstein": 5, "joseph": 5, "harold": 5, "196": 5, "5057055": 5, "mi_ln": 5, "presseau": 5, "michel": 5, "197": 5, "6810399": 5, "an_ln": 5, "osborn": 5, "andrew": 5, "198": 5, "9730177": 5, "toth": 5, "stefan": 5, "karl": 5, "199": 5, "4614424": 5, "sh_ln": 5, "watanab": 5, "201": 5, "shunji": 5, "200": 5, "name_first_ad": 5, "name_last_ad": 5, "paul": 5, "227": 5, "5792879": 5, "gessner": 5, "us8963898": 5, "228": 5, "us9005705": 5, "229": 5, "us9291285": 5, "230": 5, "10474574": 5, "seung": 5, "beom": 5, "lee": 5, "us10275371": 5, "seungbeom": 5, "231": 5, "9979878": 5, "sapna": 5, "shroff": 5, "us11042034": 5, "232": [5, 11], "onc": 5, "work": [5, 13], "membership": [5, 11], "vector": [5, 11], "output": [5, 12], "chang": [5, 13], "argument": 5, "save": [5, 7], "default": [4, 5, 6, 7, 11, 12], "us7152514": 5, "us6564684": 5, "us7832315": 5, "us6267035": 5, "us6708592": 5, "6733": 5, "us5679889": 5, "6734": 5, "us7169506": 5, "6735": 5, "us6459564": 5, "6736": 5, "us7749649": 5, "6737": 5, "us8553392": 5, "6738": 5, "pleas": [5, 8], "help": [5, 13], "usag": [5, 13], "h": 5, "d": [5, 11], "hand_disambigu": 5, "posit": 5, "option": [5, 11, 12], "show": [4, 5, 6, 7], "messag": 5, "exit": 5, "two": [0, 5, 12], "document": 7, "automat": [7, 11], "perform": [0, 7, 11], "render_inventor_disambiguation_report": [7, 12, 13], "function": [4, 6, 7, 8, 11, 13], "tabl": [7, 11, 12], "inventor_not_disambigu": [6, 7, 12], "inventor_sequ": [6, 7, 12], "raw_inventor_name_first": [6, 7, 12], "raw_inventor_name_last": [6, 7, 12], "g_inventor_not_disambigu": [6, 7, 12, 13], "persist": 7, "g_persistent_inventor": [4, 6, 7, 11], "distinct": [7, 11], "disambiguation_20211230": [7, 13], "disambiguation_20220630": [7, 13], "disamb_inventor_id_20211230": [7, 11], "to_csv": 7, "disamb_inventor_id_20220630": 7, "gener": [0, 7, 13], "folder": 7, "wish": 7, "compar": [0, 7], "more": [7, 8, 11], "disambiguation_fil": [7, 12, 13], "inventor_not_disambiguated_fil": [6, 7, 12, 13], "start": [7, 8, 11], "python3": 7, "kernel": 7, "execut": [7, 12, 13], "ipynb": 7, "cell": 7, "30": [7, 11], "12": 7, "13": 7, "14": 7, "15": 7, "16": 7, "17": 7, "18": 7, "19": 7, "20": [4, 6, 7], "21": 7, "22": 7, "23": 7, "24": 7, "26": 7, "27": 7, "28": 7, "29": 7, "33mwarn": 7, "warn": 7, "diff": 7, "engin": [7, 11, 13], "No": [7, 11], "sourc": [7, 11, 12, 13], "line": 7, "avail": [7, 13], "39m": 7, "1mpandoc": 7, "22m": 7, "standalon": 7, "self": 7, "section": 7, "div": 7, "math": 7, "method": 7, "mathjax": 7, "wrap": 7, "none": [7, 11], "imag": 7, "extens": 7, "png": [7, 11], "toc": 7, "depth": 7, "1mmetadata": 7, "css": 7, "fals": [4, 6, 7, 11], "link": [7, 11, 13], "citat": 7, "long": 7, "lang": 7, "en": [7, 13], "titl": [4, 6, 7], "todai": 7, "locat": [7, 11, 13], "jupyt": [7, 12], "theme": [4, 6, 7], "cosmo": 7, "fig": [4, 6, 7], "cap": 7, "margin": [4, 6, 7], "code": [0, 7], "copi": 7, "block": 7, "border": 7, "31bae9": 7, "creat": [0, 7, 11, 12, 13], "seen": 7, "io": [4, 6, 7, 13], "python": [8, 13], "To": [8, 13], "get": [8, 11], "readm": 8, "api": [8, 9], "project": [8, 13], "discuss": 8, "ask": 8, "question": 8, "issu": [8, 13], "request": [8, 13], "featur": [8, 13], "bug": 8, "overview": [8, 13], "instruct": 8, "kei": [1, 6, 8, 11, 13], "concept": 8, "through": [8, 11, 13], "reproduc": [8, 13], "doc": [8, 9, 13], "access": [8, 13], "detail": 8, "inspect_clusters_to_merg": 11, "join_with": 11, "inspect": 11, "miss": 11, "paramet": [11, 12], "datafram": [6, 11], "return": [4, 6, 11], "accord": 11, "type": [0, 11], "inspect_clusters_to_split": 11, "erron": 11, "inventor_benchmark_plot": 11, "metric": [1, 11], "facet_col_wrap": 11, "kwarg": [11, 12], "bar": 11, "plot": 11, "dict": [4, 6, 11], "dictionari": 11, "submodul": 11, "comput": 11, "default_metr": 11, "load": 11, "default_benchmark": 11, "plotli": [4, 6, 11], "graph": 11, "object": 11, "inventor_estimates_plot": 11, "samples_weight": 11, "estim": [4, 11, 13], "timefram": 11, "match": [6, 11], "consid": 11, "popul": 11, "drawn": 11, "instanc": 11, "isra": [11, 13], "1963": 11, "1999": 11, "tupl": 11, "b": [4, 6, 11], "pass": [6, 11], "see": [11, 13], "inventors_sampl": 11, "point": 11, "default_estim": 11, "chart": 11, "load_air_umass_assignees_benchmark": [11, 13], "air": 11, "umass": 11, "assig": 11, "team": 11, "hand": 11, "label": 11, "record": 11, "univers": [11, 13], "feder": 11, "govern": 11, "entiti": [11, 13], "privat": 11, "compani": 11, "state": [0, 11], "local": 11, "agenc": 11, "those": 11, "annot": [0, 11], "other": [0, 11, 13], "member": 11, "string": [11, 12], "similar": 11, "ident": 11, "could": 11, "confirm": 11, "wa": 11, "uncertain": 11, "did": 11, "intend": 11, "larger": 11, "coverag": 11, "varieti": 11, "than": 11, "nber": 11, "difficult": 11, "attempt": [0, 11], "parent": 11, "subsidiari": 11, "child": 11, "ones": 11, "monath": [11, 13], "jone": [11, 13], "c": [11, 13], "madhavan": [11, 13], "patentsview_disambiguation_methods_document": 11, "pdf": [4, 6, 11], "load_als_inventors_benchmark": [11, 13], "academ": [11, 13], "life": [11, 13], "scienc": [11, 13], "deriv": [0, 11], "pierr": 11, "azoulai": 11, "1970": 11, "2005": 11, "At": [], "further": [], "inform": 0, "regard": [], "obtain": [4, 6, 11, 13], "mai": [0, 11], "introduc": 11, "unresolv": 11, "select": 11, "indirectli": 11, "1976": [4, 11], "decemb": [4, 11], "31": [4, 11], "2021": [4, 11, 13], "That": [], "extran": 11, "outsid": 11, "These": [0, 11], "ignor": 11, "purpos": 11, "methodologi": [11, 13], "et": [11, 13], "al": [11, 13], "arxiv": [11, 13], "ab": 11, "2210": [11, 13], "01230": [11, 13], "addit": [], "valid": [], "howev": [], "expect": 11, "due": 11, "ambigu": 11, "natur": 11, "furthermor": [], "olivi": [11, 13], "sokhna": [11, 13], "york": [11, 13], "hickerson": [11, 13], "youngsoo": [11, 13], "baek": [11, 13], "sarvo": [11, 13], "christina": [11, 13], "resolut": [11, 13], "lesson": [11, 13], "learn": [11, 13], "load_ens_inventors_benchmark": [11, 13], "linkedin": 11, "2015": 11, "workshop": 11, "ge": 11, "chunmian": 11, "ke": 11, "wei": 11, "huang": 11, "ivan": 11, "l": [4, 6, 11], "scientist": 11, "career": 11, "profil": 11, "misclassif": 11, "strateg": 11, "manag": 11, "journal": 11, "vol": 11, "37": 11, "januari": 11, "2016": 11, "253": 11, "adapt": 11, "trajenberg": 11, "shiff": [11, 13], "2008": [11, 13], "trajtenberg": [11, 13], "m": [11, 13], "g": [11, 13], "identif": [11, 13], "mobil": [11, 13], "pinha": [11, 13], "sapir": [11, 13], "center": [11, 13], "develop": [11, 13], "also": 13, "2014": 11, "li": 11, "databas": 11, "amour": 11, "doolin": 11, "sun": 11, "y": 11, "torvik": 11, "fleme": 11, "co": 11, "network": 11, "polici": 11, "43": 11, "941": 11, "955": 11, "origin": [11, 13], "manual": [0, 11], "some": 11, "load_nber_subset_assignees_benchmark": [11, 13], "nation": 11, "bureau": 11, "econom": 11, "semiautomat": 11, "corefer": 11, "decis": 11, "group": [0, 11], "four": 11, "letter": 11, "prefix": [0, 11], "focus": 11, "five": 11, "moto": 11, "amer": 11, "gene": 11, "solu": 11, "airc": 11, "both": 11, "common": 11, "load_patentsview_inventors_benchmark": [11, 13], "particularli": 11, "plot_cluster_s": 11, "figur": [11, 12], "plot_entropy_curv": 11, "entropi": 11, "curv": 11, "plot_homonimy_r": 11, "homonimi": 11, "rate": [6, 11], "plot_name_variation_r": 11, "variat": [6, 11], "style_cluster_inspect": 11, "style": 11, "altern": 11, "color": 11, "top_inventor": 11, "most": 11, "prolif": 11, "displai": 11, "top": 11, "outdir": 12, "cach": 12, "base": 12, "directori": 12, "parquet": 12, "bool": 12, "whether": 12, "chunk": 12, "filenam": [4, 6, 12], "legend": 12, "them": 12, "short": 12, "built": 13, "advanc": 13, "system": [0, 13], "er": 13, "websit": 13, "build": 13, "full": 13, "real": 13, "world": 13, "visual": 13, "monitor": 13, "templat": [4, 6, 13], "version": 13, "render": [4, 6, 13], "quarto": 13, "amount": 13, "memori": 13, "suggest": 13, "64gb": 13, "ram": 13, "complet": 13, "quick": 13, "summar": 13, "properti": 13, "collect": 13, "fork": 13, "repositori": 13, "make": 13, "your": 13, "updat": [1, 4, 6, 13], "changelog": 13, "md": 13, "pull": 13, "maintain": 13, "need": [4, 13], "branch": 13, "conda": 13, "environ": 13, "you": 13, "env": 13, "activ": 13, "pv": 13, "makefil": 13, "util": [0, 13], "black": 13, "re": 13, "aw": 13, "public": 13, "server": 13, "reflect": 13, "ensur": 13, "preserv": 13, "without": 13, "modif": 13, "minim": 13, "check": 13, "recommend": 13, "place": 13, "runnabl": 13, "testbook": 13, "within": [0, 13], "unit": [0, 13], "user": 13, "exemplifi": 13, "duke": 13, "siddharth": 13, "morrison": 13, "2017": [1, 4, 13], "harvard": 13, "version1": 13, "figshar": 13, "technic": 13, "histori": 1, "precis": [1, 4], "recal": [1, 4], "sinc": [1, 4], "statist": 1, "inventor_estimates_trend_plot": [4, 11], "easili": [4, 6], "By": 4, "restrict": 4, "g_patent": 4, "urllib": [4, 6], "pars": [4, 6], "urlpars": [4, 6], "graph_object": [4, 6], "go": [4, 6], "pio": [4, 6], "plotly_whit": [4, 6], "def": [4, 6], "download_unzip": [4, 6], "url": [4, 6], "overwrit": [4, 6], "basenam": [4, 6], "rstrip": [4, 6], "persistent_inventor_fil": [4, 6], "patent_fil": 4, "persistent_inventor": [4, 6, 11], "patent_d": 4, "01": 4, "readi": 4, "call": 4, "tweak": [4, 6], "desir": 4, "update_layout": [4, 6], "width": [4, 6], "800": [4, 6], "height": [4, 6], "300": [4, 6], "pairwis": 4, "layout": [4, 6], "60": [4, 6], "write_imag": [4, 6], "performance_trend": 4, "inventor_summary_trend_plot": [6, 11], "homonymi": [6, 11], "inplac": 6, "summary_trend": 6, "over": 11, "persisten_inventor": 11, "disamb_inventor_id_yyyymmdd": 11, "scatter": 11, "svg": [4, 6], "cell_typ": [], "markdown": [], "metadata": [], "conceptsn": [], "numbern": [], "idn": [], "clustern": [], "vectorn": [], "execution_count": [], "text": [], "plain": [], "mention_idn": [], "11797n": [], "16606n": [], "13384n": [], "9865n": [], "12734n": [], "7694n": [], "11416n": [], "19168n": [], "650n": [], "output_typ": [], "execute_result": [], "load_israeli_inventors_benchmarkn": [], "kernelspec": [], "display_nam": [], "languag": [], "language_info": [], "codemirror_mod": [], "ipython": [], "file_extens": [], "mimetyp": [], "x": [], "nbconvert_export": [], "pygments_lex": [], "ipython3": [], "orig_nbformat": [], "vscode": [], "interpret": [], "hash": [], "c6191605ccbc69ee850b3b607fa517accda1f0792654a487c9877b1d34a204e1": [], "nbformat": [], "nbformat_minor": [], "preparationn": [], "pdn": [], "npn": [], "wgetn": [], "zipfilen": [], "osn": [], "sequencen": [], "estimatesn": [], "pairwise_recall_design_estimaten": [], "cluster_sizesn": [], "135eb778a123b23717215bebe642ebc480e0ab0e1bc583cf4971f84281f0b229": [], "historyn": [], "downloadsn": [], "urlparsen": [], "gon": [], "pion": [], "themen": [], "filenamen": [], "timeframen": [], "xml": [], "class": [], "main": [], "xmln": [], "w3": [], "2000": [], "xlink": [], "700": [], "500": [], "viewbox": [], "rect": [], "fill": [], "rgb": [], "255": [], "opac": [], "9847cc": [], "clip": [], "clippath": [], "clip9847ccxyplot": [], "plotclip": [], "446": [], "360": [], "axesclip": [], "clip9847ccx": [], "80": [], "clip9847cci": [], "clip9847ccxi": [], "gradient": [], "pattern": [], "bglayer": [], "layer": [], "imagelay": [], "shapelay": [], "cartesianlay": [], "subplot": [], "xy": [], "minor": [], "gridlay": [], "xgrid": [], "crisp": [], "transform": [], "translat": [], "138": [], "m0": [], "60v360": [], "stroke": [], "235": [], "240": [], "248": [], "1px": [], "218": [], "69": [], "299": [], "379": [], "82": [], "460": [], "ygrid": [], "409": [], "52": [], "m80": [], "0h446": [], "352": [], "296": [], "239": [], "42": 11, "182": [], "72": [], "126": [], "02": [], "zerolinelay": [], "xline": [], "yline": [], "overlin": [], "xaxislay": [], "yaxislay": [], "overax": [], "scatterlay": [], "mlayer": [], "trace": [], "traceebf19d": [], "miterlimit": [], "errorbar": [], "yerror": [], "m22": [], "05": [], "95h8m": [], "0v307": [], "44m": [], "0h8": [], "effect": [], "non": [], "scale": [], "2px": [], "134": [], "m34": [], "39": [], "0v342m": [], "m52": [], "91": [], "40": [], "67h8m": [], "0v77": [], "11m": [], "m86": [], "63": [], "58": [], "71h8m": [], "0v101": [], "88m": [], "m126": [], "97": [], "61": [], "96h8m": [], "0v102": [], "58m": [], "m150": [], "39h8m": [], "0v108": [], "51m": [], "m185": [], "74": [], "84h8m": [], "0v118": [], "83m": [], "m196": [], "41": [], "73": [], "64h8m": [], "0v124": [], "95m": [], "m214": [], "92": [], "67": [], "01h8m": [], "0v114": [], "12m": [], "m234": [], "98": [], "65": [], "57h8m": [], "0v113": [], "46m": [], "m255": [], "04000000000002": [], "37h8m": [], "m275": [], "64": [], "49h8m": [], "61m": [], "m295": [], "51": [], "68h8m": [], "0v73": [], "1m": [], "m375": [], "83": [], "47": [], "0v68": [], "71m": [], "m415": [], "95": [], "50": [], "8h8m": [], "0v72": [], "j": 11, "m26": [], "245": [], "19l38": [], "269": [], "97l56": [], "89l90": [], "3l130": [], "27l154": [], "85": [], "95l189": [], "96": [], "83l200": [], "99": [], "29l218": [], "90": [], "56l238": [], "89": [], "51l259": [], "04": [], "93": [], "91l279": [], "55l299": [], "62": [], "39l379": [], "19l419": [], "45": [], "m3": [], "0a3": [], "3a3": [], "0z": [], "0px": [], "38": [], "56": [], "130": [], "154": [], "189": [], "238": [], "259": [], "279": [], "55": [], "419": [], "traceb9e223": [], "63h8m": [], "0v36": [], "17m": [], "105": [], "177": [], "21h8m": [], "0v40": [], "76h8m": [], "0v63": [], "01m": [], "35": [], "02h8m": [], "0v48": [], "38m": [], "0v39": [], "32m": [], "05h8m": [], "0v37": [], "29m": [], "28h8m": [], "88h8m": [], "0v35": [], "87m": [], "82h8m": [], "0v33": [], "32h8m": [], "0v36m": [], "09h8m": [], "0v43": [], "93h8m": [], "27m": [], "51h8m": [], "0v26": [], "15m": [], "25h8m": [], "0v34": [], "53m": [], "18h8m": [], "0v25": [], "82m": [], "9l38": [], "34": [], "71l56": [], "38l90": [], "7l130": [], "33": [], "97l154": [], "32": [], "17l189": [], "37l218": [], "35l238": [], "16l259": [], "52l279": [], "68": [], "1l299": [], "33l379": [], "89l419": [], "0l0": [], "9l": [], "9z": [], "71": [], "87": [], "overplot": [], "abov": [], "xtick": [], "anchor": [], "middl": [], "433": [], "font": [], "famili": [], "open": [], "san": [], "verdana": [], "arial": [], "serif": [], "12px": [], "white": [], "space": 0, "pre": [], "2018": [], "2019": [], "2020": [], "ytick": [], "end": [], "79": [], "199999999999999": [], "polarlay": [], "smithlay": [], "ternarylay": [], "geolay": [], "funnelarealay": [], "pielay": [], "iciclelay": [], "treemaplay": [], "sunburstlay": [], "glimag": [], "topdef": [], "legend9847cc": [], "153": [], "infolay": [], "pointer": [], "event": [], "534": [], "9200000000001": [], "bg": [], "shape": [], "crispedg": [], "scrollbox": [], "legendtitletext": [], "14px": [], "legendtext": [], "680000000000001": [], "legendfil": [], "legendlin": [], "m5": [], "0h30": [], "legendsymbol": [], "legendpoint": [], "scatterpt": [], "legendtoggl": [], "147": [], "984375": [], "scrollbar": [], "rx": [], "ry": [], "128": [], "139": [], "164": [], "gtitl": [], "xtitl": [], "303": [], "normal": [], "ytitl": [], "rotat": [], "10625": [], "display_data": [], "inventor_estimates_trend_plotn": [], "f4d347": [], "clipf4d347xyplot": [], "567": [], "187": [], "clipf4d347x": [], "57": [], "clipf4d347i": [], "clipf4d347xi": [], "60v187": [], "88": [], "335": [], "438": [], "541": [], "241": [], "m57": [], "0h567": [], "183": [], "124": [], "66": [], "trace201fb6": [], "m28": [], "89h8m": [], "0v159": [], "m43": [], "86": [], "103": [], "6h8m": [], "0v177": [], "65m": [], "m67": [], "49": [], "74h8m": [], "0v41": [], "48m": [], "m110": [], "54": [], "0v54": [], "21m": [], "m162": [], "03": [], "69h8m": [], "57m": [], "m191": [], "42h8m": [], "0v57": [], "62m": [], "m236": [], "31h8m": [], "0v62": [], "93m": [], "m250": [], "0v66": [], "07m": [], "m274": [], "36": [], "29h8m": [], "0v60": [], "5m": [], "m299": [], "54h8m": [], "16m": [], "m325": [], "5h8m": [], "73m": [], "m351": [], "99h8m": [], "76m": [], "m376": [], "41h8m": [], "42m": [], "m479": [], "34h8m": [], "m530": [], "0v38": [], "9m": [], "m32": [], "127": [], "89l47": [], "140": [], "62l71": [], "11l114": [], "12l166": [], "44": [], "13l195": [], "46": [], "02l240": [], "62l254": [], "88l278": [], "48": [], "39l303": [], "85l329": [], "12l355": [], "87l380": [], "91l483": [], "75l534": [], "114": [], "166": [], "254": [], "278": [], "329": [], "355": [], "380": [], "483": [], "75": [], "trace4f46d": [], "0v20": [], "43m": [], "85h8m": [], "0v22": [], "23m": [], "55h8m": [], "05m": [], "0v21": [], "35h8m": [], "14h8m": [], "28m": [], "0v19": [], "25m": [], "34m": [], "0v24": [], "7h8m": [], "99m": [], "0v15": [], "59m": [], "72l47": [], "68l71": [], "31l114": [], "27l166": [], "3l195": [], "38l240": [], "96l278": [], "93l303": [], "13l355": [], "85l380": [], "32l483": [], "2l534": [], "260": [], "legendf4d347": [], "635": [], "dy": [], "0em": [], "17px": [], "340": [], "287": [], "8935546875": [], "106250000000003": [], "handn": [], "practic": [], "implementationn": [], "scope": [], "tbodi": [], "tr": [], "th": [], "vertic": [], "align": [], "thead": [], "td": [], "validationn": [], "stdout": [], "stream": [], "zipn": [], "bashn": [], "releasen": [], "datasetn": [], "inventor_idn": [], "1n": [], "201n": [], "informationn": [], "hand_disambiguationn": [], "rawinventorn": [], "producen": [], "inventorn": [], "predictedn": [], "columnsn": [], "andn": [], "shouldn": [], "exitn": [], "outputn": [], "ton": [], "thisn": [], "7a2c4b191d1ae843dde5cb5f4d1f62fa892f6b79b0f9392a84691e890e33c5a4": [], "filesn": [], "namesn": [], "inventor_sequencen": [], "raw_inventor_name_lastn": [], "inventor_summary_trend_plotn": [], "null": [], "93601d": [], "clip93601dxyplot": [], "554": 11, "clip93601dx": [], "clip93601di": [], "clip93601dxi": [], "429": [], "77": [], "530": [], "0799999999999": [], "209": [], "0h554": [], "172": [], "yzl": [], "zl": [], "247": [], "trace42499f": [], "m31": [], "13l46": [], "84": [], "41l69": [], "95l111": [], "86l162": [], "25l296": [], "84l321": [], "68l346": [], "94": [], "8l371": [], "15l472": [], "53": [], "52l522": [], "111": [], "162": [], "191": [], "271": [], "321": [], "346": [], "371": [], "472": [], "522": [], "trace17ace3": [], "151": [], "78l46": [], "149": [], "24l69": [], "91l111": [], "143": [], "79l162": [], "95l235": [], "152": [], "49l248": [], "44l321": [], "27l346": [], "122": [], "77l371": [], "173": [], "67l472": [], "53l522": [], "78": [], "06": [], "trace05cd34": [], "163": [], "15l46": [], "55l69": [], "169": [], "17l111": [], "167": [], "12l162": [], "165": [], "57l296": [], "74l321": [], "79l346": [], "94l371": [], "49l472": [], "157": [], "88l522": [], "155": [], "188": [], "3h": [], "3v": [], "3h3z": [], "81": [], "76": [], "legend93601d": [], "622": [], "08": [], "160": [], "46875": [], "70": [], "334": [], "prepar": [], "reportn": [], "stderr": [], "donen": [], "u001b": [], "39mn": [], "22mn": [], "htmln": [], "truen": [], "mathjaxn": [], "nonen": [], "pngn": [], "3n": [], "1mmetadatau001b": [], "falsen": [], "longn": [], "enn": [], "todayn": [], "evaluationn": [], "leftn": [], "python3n": [], "cosmon": [], "marginn": [], "render_inventor_disambiguation_reportn": [], "consist": 0, "six": 0, "seven": 0, "eight": 0, "digit": 0, "enter": 0, "exclud": 0, "omit": 0, "countri": 0, "differ": 0, "represent": 0, "piec": 0, "combin": 0, "its": 0, "input": 0, "multipl": 0, "being": 0, "determin": 0, "usual": 0, "expert": [0, 11], "knowledg": 0, "goal": 0, "assess": 0, "accuraci": 0, "paper": 11, "referenc": 11, "graff": 11, "zivin": 11, "manso": 11, "incent": 11, "creativ": 11, "evid": 11, "rand": 11, "527": 11}, "objects": {"pv_evaluation": [[11, 0, 0, "-", "benchmark"], [12, 0, 0, "-", "templates"]], "pv_evaluation.benchmark": [[11, 1, 1, "", "inspect_clusters_to_merge"], [11, 1, 1, "", "inspect_clusters_to_split"], [11, 1, 1, "", "inventor_benchmark_plot"], [11, 1, 1, "", "inventor_estimates_plot"], [11, 1, 1, "", "inventor_estimates_trend_plot"], [11, 1, 1, "", "inventor_summary_trend_plot"], [11, 1, 1, "", "load_air_umass_assignees_benchmark"], [11, 1, 1, "", "load_als_inventors_benchmark"], [11, 1, 1, "", "load_binette_2022_inventors_benchmark"], [11, 1, 1, "", "load_ens_inventors_benchmark"], [11, 1, 1, "", "load_israeli_inventors_benchmark"], [11, 1, 1, "", "load_lai_2011_inventors_benchmark"], [11, 1, 1, "", "load_nber_subset_assignees_benchmark"], [11, 1, 1, "", "load_patentsview_inventors_benchmark"], [11, 1, 1, "", "plot_cluster_sizes"], [11, 1, 1, "", "plot_entropy_curves"], [11, 1, 1, "", "plot_homonimy_rates"], [11, 1, 1, "", "plot_name_variation_rates"], [11, 1, 1, "", "style_cluster_inspection"], [11, 1, 1, "", "top_inventors"]], "pv_evaluation.templates": [[12, 1, 1, "", "render_inventor_disambiguation_report"]]}, "objtypes": {"0": "py:module", "1": "py:function"}, "objnames": {"0": ["py", "module", "Python module"], "1": ["py", "function", "Python function"]}, "titleterms": {"kei": 0, "concept": 0, "patent": 0, "number": 0, "mention": [0, 6], "id": 0, "cluster": 0, "membership": 0, "vector": 0, "exampl": [1, 13], "estim": [1, 2, 3], "perform": [1, 2, 3, 4, 13], "summari": [1, 6, 13], "creat": [1, 5], "benchmark": [1, 2, 3, 5, 11, 13], "dataset": [1, 5, 13], "hand": [1, 5], "lai": 3, "": [2, 3, 4, 8], "2011": 3, "data": [2, 3, 4, 7, 13], "prepar": [2, 3, 7], "precis": [2, 3], "recal": [2, 3], "inventor": [5, 6], "practic": 5, "implement": 5, "valid": 5, "transform": 5, "more": 5, "inform": 5, "html": 7, "report": [7, 13], "templat": [7, 12], "render": 7, "output": 7, "patentsview": [4, 8, 13], "evalu": [8, 13], "document": [8, 11, 12, 13], "pv_evalu": [9, 11, 12], "api": 10, "doc": 10, "content": [11, 12], "readm": 13, "disambigu": [4, 13], "algorithm": 13, "submodul": 13, "instal": 13, "metric": 13, "statist": [6, 13], "repres": 13, "contribut": 13, "code": 13, "raw": 13, "test": 13, "bug": 13, "submit": 13, "feedback": 13, "contributor": 13, "refer": 13, "citat": 13, "histori": [4, 6], "step": [4, 6], "1": [4, 6], "download": [4, 6], "requir": [4, 6], "file": [4, 6], "from": 4, "bulk": 4, "2": [4, 6], "subset": 4, "timefram": 4, "3": [4, 6], "plot": [4, 6], "comput": 6, "name": 6, "binett": 2, "2022": 2}, "envversion": {"sphinx.domains.c": 2, "sphinx.domains.changeset": 1, "sphinx.domains.citation": 1, "sphinx.domains.cpp": 8, "sphinx.domains.index": 1, "sphinx.domains.javascript": 2, "sphinx.domains.math": 2, "sphinx.domains.python": 3, "sphinx.domains.rst": 2, "sphinx.domains.std": 2, "sphinx.ext.viewcode": 1, "sphinx": 57}, "alltitles": {"Examples": [[1, "examples"], [13, "examples"]], "Estimators": [[1, "estimators"]], "Performance Summaries": [[1, "performance-summaries"]], "Creating Benchmark Datasets by Hand": [[1, "creating-benchmark-datasets-by-hand"]], "PatentsView-Evaluation\u2019s documentation": [[8, "patentsview-evaluation-s-documentation"]], "pv_evaluation": [[9, "pv-evaluation"]], "README": [[13, "readme"]], "\ud83d\udcca PatentsView-Evaluation: Benchmark Disambiguation Algorithms": [[13, "patentsview-evaluation-benchmark-disambiguation-algorithms"]], "Submodules": [[13, "submodules"]], "Installation": [[13, "installation"]], "Metrics and Summary Statistics": [[13, "metrics-and-summary-statistics"]], "Benchmark Datasets": [[13, "benchmark-datasets"]], "Representative Performance Evaluation": [[13, "representative-performance-evaluation"]], "Contributing": [[13, "contributing"]], "Contribute code and documentation": [[13, "contribute-code-and-documentation"]], "Raw data": [[13, "raw-data"]], "Testing": [[13, "testing"]], "Report bugs and submit feedback": [[13, "report-bugs-and-submit-feedback"]], "Contributors": [[13, "contributors"]], "References": [[13, "references"]], "Citation": [[13, "citation"]], "Datasets": [[13, "datasets"]], "API Doc": [[10, "api-doc"]], "Key Concepts": [[0, "key-concepts"]], "Patent Number": [[0, "patent-number"]], "Mention ID": [[0, "mention-id"]], "Clusters": [[0, "clusters"]], "Membership Vector": [[0, "membership-vector"]], "\ud83c\udfaf Performance Estimates for Binette\u2019s 2022 Benchmark": [[2, "performance-estimates-for-binette-s-2022-benchmark"]], "Data Preparation": [[2, "data-preparation"], [3, "data-preparation"], [7, "data-preparation"]], "Precision and Recall Estimates": [[2, "precision-and-recall-estimates"], [3, "precision-and-recall-estimates"]], "\ud83c\udfaf Performance Estimates for Lai\u2019s 2011 Benchmark": [[3, "performance-estimates-for-lai-s-2011-benchmark"]], "Disambiguation Performance History": [[4, "disambiguation-performance-history"]], "Step 1: Download Required Files From PatentsView\u2019s Bulk Data Downloads": [[4, "step-1-download-required-files-from-patentsview-s-bulk-data-downloads"]], "Step 2: Subset Disambiguations to the Required Timeframe": [[4, "step-2-subset-disambiguations-to-the-required-timeframe"]], "Step 3: Plot Disambiguation History": [[4, "step-3-plot-disambiguation-history"]], "\u270d\ufe0f Creating Inventors Benchmark Datasets by Hand": [[5, "creating-inventors-benchmark-datasets-by-hand"]], "Practical Implementation": [[5, "practical-implementation"]], "Validation": [[5, "validation"]], "Transformation into Benchmark Dataset": [[5, "transformation-into-benchmark-dataset"]], "More Information": [[5, "more-information"]], "Summary Statistics History": [[6, "summary-statistics-history"]], "Step 1: Download Required Files": [[6, "step-1-download-required-files"]], "Step 2: Compute Inventor Mention Names": [[6, "step-2-compute-inventor-mention-names"]], "Step 3: Plot Summary Statistics History": [[6, "step-3-plot-summary-statistics-history"]], "\ud83d\udcd1 HTML Report Template": [[7, "html-report-template"]], "Rendering Report": [[7, "rendering-report"]], "Output": [[7, "output"]], "pv_evaluation.benchmark": [[11, "pv-evaluation-benchmark"]], "Contents": [[11, "contents"], [12, "contents"]], "Documentation": [[11, "module-pv_evaluation.benchmark"], [12, "module-pv_evaluation.templates"]], "pv_evaluation.templates": [[12, "pv-evaluation-templates"]]}, "indexentries": {"inspect_clusters_to_merge() (in module pv_evaluation.benchmark)": [[11, "pv_evaluation.benchmark.inspect_clusters_to_merge"]], "inspect_clusters_to_split() (in module pv_evaluation.benchmark)": [[11, "pv_evaluation.benchmark.inspect_clusters_to_split"]], "inventor_benchmark_plot() (in module pv_evaluation.benchmark)": [[11, "pv_evaluation.benchmark.inventor_benchmark_plot"]], "inventor_estimates_plot() (in module pv_evaluation.benchmark)": [[11, "pv_evaluation.benchmark.inventor_estimates_plot"]], "inventor_estimates_trend_plot() (in module pv_evaluation.benchmark)": [[11, "pv_evaluation.benchmark.inventor_estimates_trend_plot"]], "inventor_summary_trend_plot() (in module pv_evaluation.benchmark)": [[11, "pv_evaluation.benchmark.inventor_summary_trend_plot"]], "load_air_umass_assignees_benchmark() (in module pv_evaluation.benchmark)": [[11, "pv_evaluation.benchmark.load_air_umass_assignees_benchmark"]], "load_als_inventors_benchmark() (in module pv_evaluation.benchmark)": [[11, "pv_evaluation.benchmark.load_als_inventors_benchmark"]], "load_binette_2022_inventors_benchmark() (in module pv_evaluation.benchmark)": [[11, "pv_evaluation.benchmark.load_binette_2022_inventors_benchmark"]], "load_ens_inventors_benchmark() (in module pv_evaluation.benchmark)": [[11, "pv_evaluation.benchmark.load_ens_inventors_benchmark"]], "load_israeli_inventors_benchmark() (in module pv_evaluation.benchmark)": [[11, "pv_evaluation.benchmark.load_israeli_inventors_benchmark"]], "load_lai_2011_inventors_benchmark() (in module pv_evaluation.benchmark)": [[11, "pv_evaluation.benchmark.load_lai_2011_inventors_benchmark"]], "load_nber_subset_assignees_benchmark() (in module pv_evaluation.benchmark)": [[11, "pv_evaluation.benchmark.load_nber_subset_assignees_benchmark"]], "load_patentsview_inventors_benchmark() (in module pv_evaluation.benchmark)": [[11, "pv_evaluation.benchmark.load_patentsview_inventors_benchmark"]], "module": [[11, "module-pv_evaluation.benchmark"], [12, "module-pv_evaluation.templates"]], "plot_cluster_sizes() (in module pv_evaluation.benchmark)": [[11, "pv_evaluation.benchmark.plot_cluster_sizes"]], "plot_entropy_curves() (in module pv_evaluation.benchmark)": [[11, "pv_evaluation.benchmark.plot_entropy_curves"]], "plot_homonimy_rates() (in module pv_evaluation.benchmark)": [[11, "pv_evaluation.benchmark.plot_homonimy_rates"]], "plot_name_variation_rates() (in module pv_evaluation.benchmark)": [[11, "pv_evaluation.benchmark.plot_name_variation_rates"]], "pv_evaluation.benchmark": [[11, "module-pv_evaluation.benchmark"]], "style_cluster_inspection() (in module pv_evaluation.benchmark)": [[11, "pv_evaluation.benchmark.style_cluster_inspection"]], "top_inventors() (in module pv_evaluation.benchmark)": [[11, "pv_evaluation.benchmark.top_inventors"]], "pv_evaluation.templates": [[12, "module-pv_evaluation.templates"]], "render_inventor_disambiguation_report() (in module pv_evaluation.templates)": [[12, "pv_evaluation.templates.render_inventor_disambiguation_report"]]}})