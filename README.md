# Reuel Dejmal - generátor e-shopů
Nejprve vysavětlím, jak bude software vypadat z uživatelského pohledu a poté z programátorského hlediska.

## Z uživatelského pohledu:
Při objednávce e-shopu uživatel nejprve určí, na jak dlouho e-shop zatím objednává a platí. V dalším kroku základní parametry e-shopu, jako jsou možnosti dopravy, ceny těchto možností a styl grafiky, který bude společný pro celý e-shop. Pokud uživatel nebude chtít vytvářet vlastní grafiku, bude moci využít šablonu. Tu může buď použít tak, jak je, nebo si ji upravit podle svých potřeb. Poté může upravit jednotlivé obrazovky e-shopu, které generátor automaticky vygeneruje podle globálního stylu grafiky. Pří posledním kroku uživatel objednávku zaplatí.
Do takto vygenerovaného e-shopu může uživatel přidat kategorie zboží, součástí každé kategorie budou i možnosti parametrů, podle kterých bude možné zboží filtrovat nebo i řadit. Poté půjde přidat zboží do jednotlivých kategorií. Dále může do e-shopu přidávat slevové programy.

## Z programátorského pohledu (popis jednotlivých datových objektů):

### Uživatel generátoru


### Objednávka e-shopu
Atributy:
- Uživatel
- Všechny parametry e-shopu: viz uživatelský pohled

### Globální styl grafiky


### Grafika jednotlivých e-shopových obrazovek
Zatím nevím.


### E-shop
Atributy: viz uživatelský pohled

### Objdnávka zboží z e-shopu
Atributy:
- Seznam zboží
- Seznam použitých slevových programů
- Způsob dopravy
- Místo doručení
- Uživatel

### Kategorie
Atributy:


### Parametr


### Položka



### Uživatel e-shopu
