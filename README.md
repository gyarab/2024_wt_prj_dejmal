# Reuel Dejmal - generátor e-shopů
Nejprve vysvětlím, jak bude software vypadat z uživatelského hlediska a poté z programátorského hlediska.

## Z uživatelského pohledu:
Při objednávce e-shopu uživatel nejprve určí, na jak dlouho e-shop zatím objednává a platí. V dalším kroku základní parametry e-shopu, jako jsou možnosti dopravy, ceny těchto možností a styl grafiky, který bude společný pro celý e-shop. Pokud uživatel nebude chtít vytvářet vlastní grafiku, bude moci využít šablonu. Tu může buď použít tak, jak je, nebo si ji upravit podle svých potřeb. Poté může upravit jednotlivé obrazovky e-shopu, které generátor automaticky vygeneruje podle globálního stylu grafiky. Pří posledním kroku uživatel objednávku zaplatí.
Do takto vygenerovaného e-shopu může uživatel přidat kategorie zboží, součástí každé kategorie budou i možnosti parametrů, podle kterých bude možné zboží filtrovat nebo i řadit. Poté půjde přidat zboží do jednotlivých kategorií. Dále může do e-shopu přidávat slevové programy.

## Z programátorského pohledu (popis jednotlivých datových objektů):

### Uživatel generátoru
Atributy:
- Jméno
- Hash hesla
- E-shop

### Objednávka e-shopu
Atributy:
- Uživatel
- Všechny parametry e-shopu

### Globální styl grafiky
Zatím nevím.

### Grafika jednotlivých e-shopových obrazovek
Zatím nevím.

### E-shop
Atributy:
- Tvůrce
- Seznam uživatelů
- Další: viz uživatelský pohled

### Objdnávka zboží z e-shopu
Atributy:
- Seznam zboží
- Seznam použitých slevových programů
- Způsob dopravy
- Místo doručení
- Uživatel

### Kategorie
Atributy:
- Název
- Seznam parametrů
- Seznam podkategorií
- Seznam nadkategoríí
- Seznam zboží

### Parametr
Atributy:
- Název
- Typ hodnoty
- Hodnota

### Položka (zboží)
Atributy:
- Název
- Seznam kategorií
- Cena
- Seznam množstevních slev
- Seznam parametrů
- Popis

### Uživatel e-shopu
Atributy:
- Uživatelské jméno
- Hash hesla
- Seznam zboží v košíku
- Historie objednávek
- Seznam aktuálních slevových programů

## Wireframy
![](uvod-mobile.jpeg)
![](uvod-desktop.jpeg)
![](prhl_reg-mobile.jpeg)
![](prihl_reg-desktop.jpeg)
![](novy_eshop-mobile.jpeg)
![](novy_eshop-desktop.jpeg)
![](administrace-mobile.jpeg)
![](administrace-desktop.jpeg)
![](pridat_upr_kateg-mobile-okno.jpeg)
![](pridat_upr_kateg-desktop-okno.jpeg)
![](pridat_upr_zbozi-desktop-okno.jpeg)
![](pridat_upr_zbozi-mobile-okno.jpeg)
![](nastaveni_eshopu-desktop.jpeg)
![](nastaveni_eshopu-mobile.jpeg)
![](obnoveni_hesla-mobile.jpeg)
![](obnoveni_hesla-desktop.jpeg)
![](obnoveni_hesla-okno.jpeg)
![](overeni_emailu-mobile.jpeg)
![](overeni_emailu-desktop.jpeg)
