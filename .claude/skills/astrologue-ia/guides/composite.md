# 💍 Guide : Thème Composite & Davison (L'Entité "Couple")

Ce guide contient la méthodologie COMPLÈTE pour analyser le thème de la RELATION elle-même. Pas juste comparer deux personnes comme en synastrie. Ici on analyse le **troisième être** : l'entité couple.

---

## 🎯 Objectif

Analyser le thème de la RELATION en tant qu'ENTITÉ autonome. Le composite, c'est le **troisième être**. Quand A et B sont ensemble, ils créent AB — une entité qui a son propre thème, sa propre personnalité, ses propres forces et faiblesses.

**Ce que ça répond** :
- Qui est ce couple en tant qu'entité ?
- Quelle est l'identité de la relation ?
- Quels sont les besoins émotionnels de la relation ?
- Où la relation est destinée à briller / souffrir ?
- Est-ce que cette relation a un destin (Davison + transits) ?

**Ce que ça ne répond PAS** :
- Comment A et B interagissent entre eux → c'est la SYNASTRIE
- Qui est A ou B individuellement → c'est le THÈME NATAL

---

## ⚡ Différence Synastrie vs Composite vs Davison

C'est le point CRUCIAL que 90% des débutants ne pigent pas. Trois outils, trois questions DIFFÉRENTES :

### 🔀 SYNASTRIE
- **Question** : Comment A et B interagissent-ils ?
- **Méthode** : Inter-aspects entre les deux thèmes nataux
- **Analogie** : Deux personnes dans une pièce — comment elles se parlent, se regardent, se frottent
- **Ce que ça montre** : La chimie, l'attraction, les frictions ENTRE les deux individus
- **Exemple** : "Venus A trigone Mars B = A est attirée par l'énergie de B"

### 🔗 COMPOSITE (méthode midpoint)
- **Question** : QUI est le couple AB en tant qu'ENTITÉ ?
- **Méthode** : Points milieux de chaque planète entre les deux thèmes
- **Analogie** : Le couple est une PERSONNE à part entière — on lit son thème comme un natal
- **Ce que ça montre** : L'identité, les besoins, le style, la mission du couple
- **Exemple** : "Sun composite en Capricorn en H10 = ce couple EST un power couple ambitieux"

### 🕰️ DAVISON (thème de la date/lieu midpoint)
- **Question** : Quel est le DESTIN de cette relation ?
- **Méthode** : Date milieu, heure milieu, lieu milieu entre les deux naissances → thème réel
- **Analogie** : La carte d'identité karmique de la relation — un vrai moment dans le temps
- **Ce que ça montre** : Le sens profond, le but, le destin de la relation
- **Avantage MAJEUR** : C'est un thème réel → on peut lui appliquer des TRANSITS

### ⚖️ QUAND UTILISER QUOI

| Situation | Outil | Pourquoi |
|-----------|-------|----------|
| "Comment on s'entend au quotidien ?" | Synastrie | Interactions A ↔ B |
| "Qui est-on en tant que couple ?" | Composite | Identité de AB |
| "Quel est le destin de notre relation ?" | Davison | Transits possibles |
| "Pourquoi on galère ensemble ?" | Composite + Synastrie | Les deux niveaux |
| "Notre relation va-t-elle évoluer en 2026 ?" | Davison + Transits | Timing de la relation |
| Première analyse de couple | Les trois | Vue complète |

**RÈGLE D'OR** : La synastrie te dit comment tu RESSENS l'autre. Le composite te dit qui vous ÊTES ensemble. Le Davison te dit OÙ VOUS ALLEZ.

---

## 📐 Thème Composite (Méthode Midpoint)

### Principe de calcul

On prend le POINT MILIEU de chaque planète entre les deux thèmes nataux.

**Formule générale** :
```
Position composite = (Position A + Position B) / 2
```

**ATTENTION** : Si les deux positions sont à plus de 180° d'écart sur le zodiaque, on prend le midpoint COURT (le plus proche), pas le midpoint long. Sinon tu te retrouves avec un point diamétralement opposé à ce qu'il devrait être.

### Exemple concret

**Personne A** : Sun à 20° Scorpio (= 230° absolu)
**Personne B** : Sun à 10° Pisces (= 340° absolu)

Écart = 340 - 230 = 110° (< 180°, donc midpoint direct)
Midpoint = (230 + 340) / 2 = 285° = **15° Capricorn**

→ Sun composite à 15° Capricorn

### Calcul pour CHAQUE facteur

On applique cette formule à :
- ☀️ Sun A + Sun B → Sun composite
- 🌙 Moon A + Moon B → Moon composite
- ☿ Mercury A + Mercury B → Mercury composite
- ♀ Venus A + Venus B → Venus composite
- ♂ Mars A + Mars B → Mars composite
- ♃ Jupiter A + Jupiter B → Jupiter composite
- ♄ Saturn A + Saturn B → Saturn composite
- ♅ Uranus A + Uranus B → Uranus composite
- ♆ Neptune A + Neptune B → Neptune composite
- ♇ Pluto A + Pluto B → Pluto composite
- ☊ North Node A + North Node B → North Node composite
- ⬆️ ASC A + ASC B → ASC composite
- 🏔️ MC A + MC B → MC composite

**IMPORTANT** : Le système de maisons du composite est calculé à partir de l'ASC composite. C'est un thème artificiel — il n'a jamais existé dans le ciel réel. C'est sa LIMITE par rapport au Davison.

### Comment calculer

```bash
# Étape 1 : Calculer le thème natal de chaque personne
python3 scripts/ephemeris.py natal --date 14.11.1994 --time 13:30 --lat 43.7102 --lon 7.2620 --tz Europe/Paris
python3 scripts/ephemeris.py natal --date 22.06.1992 --time 08:45 --lat 48.8566 --lon 2.3522 --tz Europe/Paris

# Étape 2 : Extraire les positions en degrés absolus (--json pour parsing)
python3 scripts/ephemeris.py natal --date 14.11.1994 --time 13:30 --lat 43.7102 --lon 7.2620 --tz Europe/Paris --json
python3 scripts/ephemeris.py natal --date 22.06.1992 --time 08:45 --lat 48.8566 --lon 2.3522 --tz Europe/Paris --json

# Étape 3 : Calculer les midpoints manuellement ou via script
# Pour chaque planète : (degré_A + degré_B) / 2
# Si écart > 180°, ajouter 180° au résultat
```

**Sources en ligne (fallback)** :
1. astro-seek.com → section "Composite Chart" (gratuit)
2. astro.com → section "Extended Chart Selection" → Composite Chart (Midpoint)
3. cafeastrology.com → Composite Chart Calculator

---

## 🔮 Interprétation du Composite — Planète par Planète

### ☀️ SUN COMPOSITE — L'identité du couple

**C'est LA planète la plus importante du composite.** Le Sun composite dit QUI EST ce couple. Son essence. Sa raison d'être.

**Par signe** :
- **Sun composite en Aries** : Couple de pionniers. Énergie, action, compétition. Ils s'ennuient vite → besoin d'aventure constante.
- **Sun composite en Taurus** : Couple ancré. Confort, sécurité, routine. Lent à s'installer mais solide une fois en place.
- **Sun composite en Gemini** : Couple communicant. Discussion, variété, mental. Peut manquer de profondeur.
- **Sun composite en Cancer** : Couple familial. Foyer, émotions, protection mutuelle. Risque de codépendance.
- **Sun composite en Leo** : Couple flamboyant. Ils veulent briller ENSEMBLE. Attention à l'ego commun.
- **Sun composite en Virgo** : Couple pratique. Service mutuel, détails, perfectionnisme. Peut devenir critique.
- **Sun composite en Libra** : Couple esthétique. Harmonie, diplomatie, beauté. Fuit le conflit → danger.
- **Sun composite en Scorpio** : Couple INTENSE. Transformation, secrets, passion. Tout ou rien.
- **Sun composite en Sagittarius** : Couple aventurier. Liberté, voyages, philosophie. Peut manquer d'ancrage.
- **Sun composite en Capricorn** : Couple ambitieux. Structure, objectifs, statut. Peut manquer de fun.
- **Sun composite en Aquarius** : Couple original. Liberté, innovation, amitié. Peut manquer d'intimité.
- **Sun composite en Pisces** : Couple spirituel. Compassion, rêve, fusion. Peut manquer de limites.

---

### 🌙 MOON COMPOSITE — Les besoins émotionnels du couple

**Ce que le couple a BESOIN pour se sentir en sécurité émotionnellement.** Si la Moon composite n'est pas nourrie, la relation crève de faim.

- **Moon en Aries** : Le couple a besoin d'ACTION. Pas de temps pour pleurnicher. Émotion = mouvement.
- **Moon en Taurus** : Le couple a besoin de STABILITÉ. Routine, nourriture, confort physique. Câlins > talk.
- **Moon en Gemini** : Le couple a besoin de PARLER. Communication constante. Si on arrête de parler, ça meurt.
- **Moon en Cancer** : Le couple a besoin de SÉCURITÉ. Foyer, nid, intimité. Ultra sensible aux menaces extérieures.
- **Moon en Leo** : Le couple a besoin de CÉLÉBRATION. Fête, attention, être admiré ensemble. L'ego commun doit être nourri.
- **Moon en Virgo** : Le couple a besoin d'UTILITÉ. Servir ensemble, s'améliorer mutuellement, projets pratiques.
- **Moon en Libra** : Le couple a besoin d'HARMONIE. Paix, beauté, équilibre. Le conflit est vécu comme une catastrophe.
- **Moon en Scorpio** : Le couple a besoin d'INTENSITÉ. Profondeur émotionnelle, vérité crue, pas de masques.
- **Moon en Sagittarius** : Le couple a besoin de LIBERTÉ. Voyages, aventures, expansion. Pas d'étouffement.
- **Moon en Capricorn** : Le couple a besoin de STRUCTURE. Objectifs communs, responsabilités, maturité. Les émotions sont gérées, pas déversées.
- **Moon en Aquarius** : Le couple a besoin d'ESPACE. Individualité dans la relation, amitié, originalité. Trop de fusion = mort.
- **Moon en Pisces** : Le couple a besoin de FUSION SPIRITUELLE. Rêve partagé, empathie, transcendance. Risque de se noyer ensemble.

---

### ♀️ VENUS COMPOSITE — Le style amoureux du couple

**Comment ce couple AIME. Comment il exprime l'affection, la tendresse, la beauté.**

- **Venus en Aries** : Amour passionné, impulsif. La conquête permanente. Ça s'ennuie si c'est trop calme.
- **Venus en Taurus** : Amour sensuel, stable. Cadeaux, bonne bouffe, contact physique. Le confort = l'amour.
- **Venus en Gemini** : Amour mental. Flirt verbal, humour, variété. L'amour passe par les mots.
- **Venus en Cancer** : Amour protecteur. Prendre soin de l'autre, foyer douillet, mémoire émotionnelle.
- **Venus en Leo** : Amour dramatique. Grand gestes, romance théâtrale, fierté d'être ensemble.
- **Venus en Virgo** : Amour par le service. Actes concrets > paroles. "Je t'aime" = "Je t'ai préparé ton café."
- **Venus en Libra** : Amour harmonieux. Esthétique, courtoisie, partenariat. Le couple classique.
- **Venus en Scorpio** : Amour obsessionnel. Passion, exclusivité, profondeur. Pas de demi-mesure.
- **Venus en Sagittarius** : Amour libre. Aventure ensemble, pas de possessivité, expansion.
- **Venus en Capricorn** : Amour mature. Engagement sérieux, loyauté, construction à long terme.
- **Venus en Aquarius** : Amour atypique. Amitié d'abord, liberté, couple non-conventionnel.
- **Venus en Pisces** : Amour romantique ultime. Idéalisation, sacrifice, poésie. Risque de désillusion.

---

### ♂️ MARS COMPOSITE — L'énergie et les conflits du couple

**Comment ce couple AGIT, se bat, résout les conflits, et fait l'amour.**

- **Mars en Aries** : Conflits explosifs mais COURTS. On s'engueule, on baise, c'est fini. Action directe.
- **Mars en Taurus** : Conflits LENTS. Accumulation de rancœur, puis éruption volcanique. Sexe sensuel.
- **Mars en Gemini** : Conflits VERBAUX. Débats, joutes intellectuelles, sarcasme. Risque de communication passive-agressive.
- **Mars en Cancer** : Conflits ÉMOTIONNELS. Manipulation par culpabilité, bouderie, silence punitif. Dangereux.
- **Mars en Leo** : Conflits THÉÂTRAUX. Drama, scènes, portes claquées. Mais réconciliation spectaculaire.
- **Mars en Virgo** : Conflits MINUTIEUX. Critique, reproche précis, micro-agression. Mort par mille coupures.
- **Mars en Libra** : Conflits ÉVITÉS. Le couple fuit le conflit → ça s'accumule → explosion retardée.
- **Mars en Scorpio** : Conflits NUCLÉAIRES. Vengeance, manipulation, silence glacial. Le plus destructeur.
- **Mars en Sagittarius** : Conflits PHILOSOPHIQUES. Disputes sur les valeurs, la liberté. "T'es trop étroit d'esprit."
- **Mars en Capricorn** : Conflits STRUCTURÉS. Disputes froides, calculées, sur le pouvoir et le contrôle.
- **Mars en Aquarius** : Conflits IDÉOLOGIQUES. Disputes sur les principes. Détachement émotionnel en conflit.
- **Mars en Pisces** : Conflits PASSIFS. Victimisation, fuite, "c'est pas moi c'est toi." Le plus insidieux.

---

### ♄ SATURN COMPOSITE — Les tests et l'engagement du couple

**Saturn = le prof sévère de la relation. Ce qu'il touche, il le TESTE.**

- **Saturn bien aspecté** (trigone, sextile) : Le couple DURE. Structure, maturité, engagement solide. Ils construisent quelque chose de réel.
- **Saturn mal aspecté** (carré, opposition) : Le couple SOUFFRE pour durer. Restrictions, obligations, poids. Ça peut tenir mais ça fait MAL.
- **Saturn conjoint Sun** : La relation est une LEÇON. Lourd mais formateur. L'identité du couple est testée.
- **Saturn conjoint Moon** : Les émotions sont BRIDÉES. Froideur émotionnelle dans le couple. On ne pleure pas ici.
- **Saturn conjoint Venus** : L'amour est RETARDÉ ou limité. "On s'aime mais c'est dur." Classique du couple qui dure mais souffre.
- **Saturn non-aspecté** : Pas de structure → pas de durabilité. La relation manque de colonne vertébrale.

---

### ♃ JUPITER COMPOSITE — La croissance et la chance du couple

**Jupiter = le bienfaiteur. Ce qu'il touche, il l'AMPLIFIE et le BÉNIT.**

- **Jupiter bien aspecté** : Le couple a de la CHANCE ensemble. Expansion, opportunités, joie.
- **Jupiter conjoint Sun** : Le couple rayonne. Optimisme, générosité, succès ensemble.
- **Jupiter conjoint Venus** : **LE MEILLEUR ASPECT COMPOSITE.** Amour abondant, chance en amour, générosité mutuelle. Couple béni.
- **Jupiter conjoint Moon** : Bien-être émotionnel. Le couple se sent BIEN ensemble. Chaleur, protection, confort.
- **Jupiter mal aspecté** : Excès ensemble. Trop de dépenses, trop de promesses, trop d'attentes irréalistes.

---

### ♅ URANUS COMPOSITE — L'imprévisibilité du couple

- **Uranus dominant** : Couple non-conventionnel. Relation à distance, couple ouvert, ruptures/retrouvailles.
- **Uranus carré Sun/Moon** : Instabilité chronique. "On-off" permanent.
- **Uranus trigone Venus** : Couple excitant, jamais ennuyeux, électrique.

### ♆ NEPTUNE COMPOSITE — L'illusion et la spiritualité du couple

- **Neptune dominant** : Couple spirituel OU couple dans l'illusion totale. L'un ou l'autre.
- **Neptune carré Sun** : **RED FLAG.** Le couple se MENT à lui-même. Illusion sur ce qu'il est.
- **Neptune conjoint Venus** : Amour romantique idéalisé. Magnifique au début, désillusion possible.
- **Neptune trigone Moon** : Connexion psychique, empathie profonde, rêves partagés.

### ♇ PLUTO COMPOSITE — Le pouvoir et la transformation du couple

- **Pluto dominant** : Couple transformateur. La relation CHANGE profondément les deux personnes.
- **Pluto conjoint Sun** : Relation de pouvoir. Qui contrôle qui ? Intensité max.
- **Pluto carré Venus** : **OBSESSION. MANIPULATION.** Amour qui peut devenir toxique.
- **Pluto trigone Sun** : Empowerment mutuel. Le couple devient PLUS FORT ensemble.

---

## 🏠 Interprétation par Maison du Composite

La maison où tombe chaque planète indique le DOMAINE DE VIE où le couple concentre son énergie.

### ☀️ SUN COMPOSITE PAR MAISON

| Maison | Signification | Description |
|--------|---------------|-------------|
| **H1** | Identité commune | Couple centré sur l'IMAGE qu'il projette. "Nous sommes..." est leur phrase. Très visible. |
| **H2** | Ressources | Couple focalisé sur l'argent, la sécurité matérielle. Ils construisent un patrimoine ensemble. |
| **H3** | Communication | Couple bavard. La parole est au centre. Voisinage, fratrie, échanges quotidiens. |
| **H4** | Foyer | Couple DOMESTIQUE. Le nid est sacré. Famille, racines, intimité privée. |
| **H5** | Romance/Créativité | Couple LUDIQUE. Jeu, romance, enfants, créativité. La vie est une fête. |
| **H6** | Service/Quotidien | Couple qui fonctionne. Routine, travail, santé. Utile mais pas glamour. |
| **H7** | Partenariat | Couple centré sur le PARTENARIAT lui-même. La relation est le projet. Mariage classique. |
| **H8** | Transformation | Couple INTENSE. Sexe, pouvoir, crises, transformation. Pas pour les fragiles. |
| **H9** | Expansion | Couple philosophe. Voyages, études, quête de sens. Ils grandissent ensemble. |
| **H10** | Carrière/Public | **POWER COUPLE.** Ambitieux, visibles, influents. Ils veulent réussir ensemble. |
| **H11** | Communauté | Couple social. Amis, groupes, causes. Leur relation est au service du collectif. |
| **H12** | Secret/Karma | Couple CACHÉ ou karmique. Relation secrète, sacrifice, spiritualité. Ou alors : couple qui fuit la réalité. |

### ♀️ VENUS COMPOSITE PAR MAISON

| Maison | Signification | Verdict |
|--------|---------------|---------|
| **H1** | Amour visible | Le couple RAYONNE d'amour. Tout le monde voit qu'ils s'aiment. ✅ |
| **H2** | Amour matériel | Ils s'aiment à travers l'argent, les cadeaux, le confort. |
| **H3** | Amour verbal | Mots doux, communication tendre, lettres d'amour. |
| **H4** | Amour domestique | L'amour est au foyer. Nid douillet, intimité. ✅ |
| **H5** | Amour romantique | **POSITION IDÉALE.** Romance, jeu, passion créative. 🔥 |
| **H6** | Amour pratique | "Je t'aime" = "J'ai fait la vaisselle." Moins sexy mais fiable. |
| **H7** | Amour partenarial | L'amour EST le partenariat. Équilibre, justice, engagement. ✅ |
| **H8** | Amour passionné | **PASSION INTENSE.** Sexe, profondeur, obsession. Magnétique mais dangereux. 🔥 |
| **H9** | Amour philosophique | Ils s'aiment à travers les idées, les voyages, la quête de sens. |
| **H10** | Amour public | L'amour est visible au monde. Couple admiré publiquement. |
| **H11** | Amour amical | L'amour est basé sur l'AMITIÉ. Meilleurs amis qui s'aiment. ✅ |
| **H12** | Amour caché | Amour secret, sacrificiel, ou karmique. ⚠️ Peut être magnifique ou destructeur. |

### ♂️ MARS COMPOSITE PAR MAISON

| Maison | Signification | Attention |
|--------|---------------|-----------|
| **H1** | Énergie directe | Couple énergique, combatif, impulsif. Disputes ouvertes. |
| **H2** | Conflits d'argent | Disputes sur les finances, les ressources, les valeurs matérielles. |
| **H3** | Conflits verbaux | Engueulades verbales, sarcasme, disputes de communication. |
| **H4** | **Conflits domestiques** | **DANGER.** Disputes au foyer, tensions familiales, guerre dans le nid. 🚩 |
| **H5** | Compétition ludique | Rivalité créative, compétition sexuelle, jeux de pouvoir. |
| **H6** | Conflits quotidiens | Disputes sur la vaisselle, le ménage, le quotidien. Usant. |
| **H7** | Conflits relationnels | La relation ELLE-MÊME est un combat. Lutte pour l'équilibre. |
| **H8** | Conflits de pouvoir | **DANGEREUX.** Luttes de pouvoir, manipulation, contrôle. 🚩 |
| **H10** | Conflits de carrière | Compétition professionnelle, disputes sur l'ambition. |
| **H12** | Conflits cachés | Agressivité refoulée, ressentiment secret. Le pire : rien ne se dit. 🚩 |

### ♄ SATURN COMPOSITE PAR MAISON

| Maison | Signification | Impact |
|--------|---------------|--------|
| **H1** | Identité limitée | Couple sérieux, lourd, qui se sent restreint. Pas fun mais durable. |
| **H4** | Foyer difficile | Le foyer est une épreuve. Famille compliquée, maison qui pèse. |
| **H5** | Romance bloquée | La romance est FREINÉE. Pas de fun, pas de spontanéité. ⚠️ |
| **H7** | Engagement sérieux | **CLASSIQUE.** Engagement lourd mais RÉEL. Mariage de raison/destinée. Tests relationnels. |
| **H8** | Transformation forcée | Crises profondes qui FORCENT la transformation. Pas le choix d'évoluer. |
| **H10** | Ambition structurée | Le couple construit une carrière/réputation ensemble. Discipliné. |
| **H12** | Karma lourd | Dette karmique. La relation existe pour régler des comptes du passé. |

---

## 🕰️ Thème Davison (Date/Lieu Midpoint)

### Principe

Le Davison prend le point milieu dans le TEMPS et l'ESPACE :

- **Date midpoint** : Date exactement entre les deux dates de naissance
- **Heure midpoint** : Heure exactement entre les deux heures de naissance
- **Lieu midpoint** : Coordonnées géographiques exactement entre les deux lieux de naissance

**RÉSULTAT** : Un thème qui correspond à un moment RÉEL dans le temps et l'espace. Un moment où le ciel avait VRAIMENT cette configuration.

### Exemple concret

**Personne A** : 14.11.1994, 13h30, Nice (43.71°N, 7.26°E)
**Personne B** : 22.06.1992, 08h45, Paris (48.86°N, 2.35°E)

**Calcul date** :
- A = 14.11.1994 (jour julien ≈ 2449671)
- B = 22.06.1992 (jour julien ≈ 2448794)
- Midpoint = (2449671 + 2448794) / 2 ≈ 2449232
- → **≈ 02.09.1993** (environ)

**Calcul heure** :
- A = 13h30 = 810 minutes après minuit
- B = 08h45 = 525 minutes après minuit
- Midpoint = (810 + 525) / 2 = 667.5 minutes = **11h07** environ

**Calcul lieu** :
- Latitude : (43.71 + 48.86) / 2 = **46.29°N**
- Longitude : (7.26 + 2.35) / 2 = **4.81°E**
- → Quelque part entre Nice et Paris, vers **Lyon/Mâcon**

→ **Thème Davison** : 02.09.1993, 11h07, ~46.29°N 4.81°E

### Avantage MAJEUR du Davison

**C'est un VRAI thème.** Le ciel ressemblait RÉELLEMENT à ça le 02.09.1993 à 11h07 au-dessus de Lyon.

Conséquence : **ON PEUT APPLIQUER DES TRANSITS AU DAVISON.**

C'est LE gros avantage par rapport au composite (qui est artificiel). Tu peux regarder :
- Quand Saturn transite le Sun du Davison → période de TEST pour la relation
- Quand Jupiter transite Venus du Davison → période BÉNIE pour le couple
- Quand Pluto transite le Moon du Davison → transformation émotionnelle profonde du couple
- Quand Uranus transite l'ASC du Davison → changement radical dans la dynamique

### Comment calculer le Davison

```bash
# Option 1 : Calculer la date/heure/lieu midpoint manuellement (voir formules ci-dessus)
# puis calculer le thème natal de ce moment/lieu

python3 scripts/ephemeris.py natal --date 02.09.1993 --time 11:07 --lat 46.29 --lon 4.81 --tz Europe/Paris

# Option 2 : Utiliser astro-seek.com
# → Section "Davison Relationship Chart" (gratuit)

# Option 3 : Appliquer les transits au Davison
python3 scripts/ephemeris.py transits --date DD.MM.YYYY --natal-date 02.09.1993 --natal-time 11:07 --lat 46.29 --lon 4.81 --tz Europe/Paris
```

**Sources en ligne** :
1. astro-seek.com → "Davison Relationship Chart"
2. astro.com → Extended Chart Selection → Davison Chart
3. Manuellement si besoin (formules ci-dessus)

### Interprétation du Davison

**Même méthode que le composite** (planètes en signes, maisons, aspects). MAIS avec une couche supplémentaire :

Le Davison montre le BUT PROFOND de la relation. C'est plus "karmique", plus "destiné". Si le composite dit "qui vous êtes ensemble", le Davison dit "POURQUOI vous êtes ensemble".

**Points clés à regarder dans le Davison** :
1. **Sun Davison** : Le but fondamental de la relation
2. **Moon Davison** : Le besoin émotionnel profond de la relation
3. **Saturn Davison** : Les leçons karmiques de la relation
4. **North Node Davison** : La direction d'évolution de la relation
5. **Aspects majeurs** : Les dynamiques fondamentales du destin commun

---

## 🚩 RED FLAGS dans le Composite

**Ces configurations DOIVENT être signalées. Pas de complaisance, pas d'édulcoration.**

### 🔴 RED FLAGS CRITIQUES (dealbreakers potentiels)

**1. Saturn conjoint/carré/opposition Sun composite**
- La relation est une PRISON ou une LEÇON
- L'identité du couple est écrasée par le poids, la responsabilité, la restriction
- **Ce que ça donne** : "On reste ensemble par obligation/peur, pas par amour"
- **Concrètement** : On s'ennuie, on se sent vieux ensemble, la joie est rationnée
- Sévérité : 🔴🔴🔴

**2. Pluto carré/opposition Venus composite**
- **OBSESSION ET MANIPULATION AMOUREUSE**
- L'amour du couple est empoisonné par le contrôle et la possessivité
- **Ce que ça donne** : "Je t'aime mais je veux te posséder/détruire"
- **Concrètement** : Jalousie maladive, chantage émotionnel, amour toxique
- Sévérité : 🔴🔴🔴🔴

**3. Mars opposition/carré Pluto composite**
- **VIOLENCE POSSIBLE**
- L'énergie du couple est explosive, destructrice, incontrôlable
- **Ce que ça donne** : Luttes de pouvoir PHYSIQUES, rage, destruction mutuelle
- **Concrètement** : Disputes qui dégénèrent, objets cassés, mots irréparables, violence
- Sévérité : 🔴🔴🔴🔴🔴 (le pire)

**4. Neptune carré/opposition Sun composite**
- **LE COUPLE VIT DANS L'ILLUSION**
- Ils ne savent pas qui ils sont ensemble. Ils se mentent.
- **Ce que ça donne** : "On croit être un couple génial mais tout est fake"
- **Concrètement** : Déni de réalité, addictions partagées, désillusion brutale quand la vérité émerge
- Sévérité : 🔴🔴🔴

**5. Saturn en H1 composite**
- L'identité même du couple est LOURDE
- Ça écrase tout dès le départ
- **Ce que ça donne** : "Pourquoi c'est si dur d'être ensemble ?"
- **Concrètement** : Relation qui se sent comme un devoir, pas un plaisir
- Sévérité : 🔴🔴🔴

**6. Aucun aspect majeur à Venus composite**
- **PAS D'AMOUR RÉEL**
- Venus est isolée → l'amour n'est connecté à RIEN dans la dynamique du couple
- **Ce que ça donne** : "On s'apprécie mais il n'y a pas de flamme"
- **Concrètement** : Amitié déguisée en couple, pas de passion, pas de tendresse
- Sévérité : 🔴🔴🔴

**7. Pluto conjoint/carré Moon composite**
- Les émotions du couple sont MANIPULÉES
- Chantage émotionnel, contrôle psychologique
- **Ce que ça donne** : Un des deux (ou les deux) utilise les émotions comme ARME
- Sévérité : 🔴🔴🔴🔴

**8. Mars carré Saturn composite**
- L'énergie est BLOQUÉE puis EXPLOSE
- Le couple se retient, se retient, puis pète un câble
- **Ce que ça donne** : Frustration chronique → explosion périodique
- Sévérité : 🔴🔴🔴

**9. Sun carré Moon composite**
- **TENSION FONDAMENTALE** entre ce que le couple EST et ce qu'il RESSENT
- L'identité et les émotions sont en conflit permanent
- **Ce que ça donne** : "On veut la même chose mais on le vit différemment"
- **Concrètement** : Incompréhension structurelle, frustration existentielle
- Sévérité : 🔴🔴🔴

**10. Chiron conjoint Sun/Moon/Venus composite**
- La relation EST une blessure
- Ça fait mal d'être ensemble — mais c'est censé guérir quelque chose
- **Ce que ça donne** : "Cette relation me fait souffrir mais je ne peux pas partir"
- Sévérité : 🔴🔴 (karmique, peut être transformateur si conscient)

---

## ✅ GREEN FLAGS dans le Composite

**Ces configurations sont des BÉNÉDICTIONS. Quand tu les vois, souligne-les.**

### 💚 GREEN FLAGS MAJEURES

**1. Jupiter conjoint Sun ou Venus composite**
- **RELATION BÉNIE**
- Chance, expansion, joie. Le couple grandit ensemble et le monde les soutient.
- **Ce que ça donne** : "Tout nous réussit quand on est ensemble"
- Score : ✅✅✅✅✅

**2. Venus en H5 ou H7 composite**
- **ROMANCE NATURELLE ou PARTENARIAT IDÉAL**
- H5 = l'amour est un JEU, une célébration, de la créativité
- H7 = l'amour est un ENGAGEMENT naturel, un partenariat équilibré
- Score : ✅✅✅✅

**3. Sun trigone/sextile Moon composite**
- **HARMONIE FONDAMENTALE**
- Ce que le couple EST s'harmonise avec ce qu'il RESSENT
- Identité et émotions sont ALIGNÉES
- **Ce que ça donne** : "On se comprend naturellement"
- Score : ✅✅✅✅

**4. Saturn bien aspecté (trigone/sextile) au composite**
- **DURABILITÉ**
- Le couple a une structure saine. Il TIENT dans le temps.
- Saturn sextile/trigone Venus = l'amour est STABLE et DURABLE
- Saturn sextile/trigone Sun = l'identité du couple est SOLIDE
- Score : ✅✅✅✅

**5. Moon trigone/sextile Venus composite**
- **TENDRESSE NATURELLE**
- Les émotions et l'amour coulent facilement
- Le couple se sent aimé et émotionnellement en sécurité
- Score : ✅✅✅✅

**6. Venus trigone Jupiter composite**
- **COUPLE CHANCEUX EN AMOUR**
- Abondance affective, générosité, optimisme amoureux
- **Ce que ça donne** : "L'amour entre nous est facile et généreux"
- Score : ✅✅✅✅✅

**7. Sun en H1 ou H7 composite**
- H1 = le couple A UNE IDENTITÉ forte et claire
- H7 = le couple EST un vrai partenariat
- Les deux sont excellents pour la visibilité et la cohérence du couple
- Score : ✅✅✅

**8. North Node conjoint Sun/Venus composite**
- La relation est DESTINÉE à évoluer positivement
- Le couple va dans la bonne direction karmiquement
- Score : ✅✅✅✅

**9. Mars trigone/sextile Venus composite**
- Passion ET harmonie
- Le désir et l'amour sont alignés — pas de conflit entre ce qu'on veut et ce qu'on aime
- Score : ✅✅✅✅

**10. Jupiter en H5 ou H9 composite**
- H5 = chance en romance, créativité, enfants
- H9 = expansion philosophique, voyages, sens partagé
- Le couple est béni dans ces domaines
- Score : ✅✅✅

---

## 📊 Aspects du Composite — Grille de Scoring

### Aspects POSITIFS (+points)

| Aspect composite | Points | Signification |
|------------------|--------|---------------|
| **Jupiter conj Sun** | +3.0 | Couple béni, rayonnant |
| **Jupiter conj Venus** | +3.0 | Amour abondant, chance en amour |
| **Venus trigone Jupiter** | +2.5 | Couple chanceux, généreux |
| **Sun trigone Moon** | +2.5 | Harmonie identité/émotions |
| **Moon trigone Venus** | +2.0 | Tendresse naturelle |
| **Venus trigone Mars** | +2.0 | Passion harmonieuse |
| **Saturn trigone Sun** | +2.0 | Couple solide, durable |
| **Saturn trigone Venus** | +2.0 | Amour qui dure |
| **Pluto trigone Sun** | +1.5 | Empowerment mutuel |
| **Sun sextile Moon** | +1.5 | Compréhension mutuelle |
| **Jupiter trigone Moon** | +1.5 | Bien-être émotionnel |
| **Venus en H5/H7** | +1.5 | Romance/partenariat naturel |
| **Sun en H1/H7** | +1.0 | Identité/partenariat clair |
| **North Node conj Sun/Venus** | +1.0 | Destinée positive |

### Aspects NÉGATIFS (-points)

| Aspect composite | Points | Signification |
|------------------|--------|---------------|
| **Mars opp/carré Pluto** | -4.0 | Violence, destruction |
| **Pluto carré Venus** | -3.0 | Obsession, manipulation |
| **Neptune carré Sun** | -2.5 | Illusion, mensonge |
| **Saturn conj/carré Sun** | -2.5 | Relation-prison |
| **Sun carré Moon** | -2.0 | Tension fondamentale |
| **Venus carré Saturn** | -2.0 | Amour souffrant |
| **Mars carré Saturn** | -2.0 | Frustration/explosion |
| **Pluto carré Moon** | -2.0 | Manipulation émotionnelle |
| **Saturn en H1** | -1.5 | Identité lourde |
| **Mars en H4/H8** | -1.5 | Conflits domestiques/pouvoir |
| **Venus non-aspectée** | -1.5 | Pas d'amour connecté |
| **Uranus carré Sun/Moon** | -1.5 | Instabilité chronique |
| **Chiron conj Sun/Venus** | -1.0 | Relation-blessure |
| **Neptune carré Venus** | -1.0 | Désillusion amoureuse |

---

## 📋 Format de Rapport Composite/Davison

```markdown
# 💍 ANALYSE COMPOSITE & DAVISON

## Couple
**Personne A** : [Nom], [Date], [Heure], [Lieu]
**Personne B** : [Nom], [Date], [Heure], [Lieu]

---

## 📊 SCORES DU COUPLE

| Critère | Score | Détail |
|---------|-------|--------|
| **Identité du couple** (Sun composite) | X/10 | [Signe + maison + aspects] |
| **Harmonie émotionnelle** (Moon composite) | X/10 | [Signe + maison + aspects] |
| **Amour & affection** (Venus composite) | X/10 | [Signe + maison + aspects] |
| **Énergie & conflits** (Mars composite) | X/10 | [Signe + maison + aspects] |
| **Durabilité** (Saturn composite) | X/10 | [Aspects + maison] |
| **Croissance** (Jupiter composite) | X/10 | [Aspects + maison] |
| **SCORE GLOBAL COMPOSITE** | **X.X/10** | [Moyenne pondérée] |

---

## 🔮 QUI EST CE COUPLE ?

### Identité (Sun composite en [SIGNE] en [MAISON])
[Interprétation brutale : QUI est cette entité couple]

### Besoins émotionnels (Moon composite en [SIGNE] en [MAISON])
[Ce que le couple a BESOIN pour survivre émotionnellement]

### Style amoureux (Venus composite en [SIGNE] en [MAISON])
[COMMENT ce couple aime]

### Énergie & conflits (Mars composite en [SIGNE] en [MAISON])
[Comment ce couple se bat et agit]

### Engagement (Saturn composite en [SIGNE] en [MAISON])
[Les tests et la durabilité du couple]

### Croissance (Jupiter composite en [SIGNE] en [MAISON])
[Où le couple est béni et peut grandir]

---

## 🚩 RED FLAGS
1. [Red flag 1 avec aspect exact et conséquence concrète]
2. [Red flag 2]
3. [...]

## ✅ GREEN FLAGS
1. [Green flag 1 avec aspect exact et bénéfice concret]
2. [Green flag 2]
3. [...]

---

## 🕰️ THÈME DAVISON

**Date Davison** : [Date calculée]
**Lieu Davison** : [Coordonnées]
**Sun Davison** : [Signe/Maison] → [But de la relation]
**Moon Davison** : [Signe/Maison] → [Besoin profond]

### Transits actuels sur le Davison
- [Transit 1] : [Impact sur la relation]
- [Transit 2] : [Impact]
- [...]

### Prochains transits importants
- [Date] : [Transit] → [Ce qui va se passer]
- [Date] : [Transit] → [Ce qui va se passer]

---

## 💀 DIAGNOSTIC BRUTAL

### Ce couple EST :
[1-2 phrases BRUTALES définissant l'entité couple]

### Ce couple a BESOIN de :
[Ce qui manque ou doit être nourri]

### Ce couple va GALÉRER avec :
[Les zones de friction structurelles]

### Ce couple va BRILLER dans :
[Les zones de force naturelles]

### Pronostic long terme :
[Verdict sans filtre basé sur le composite + Davison]

---

## ⚖️ COMPOSITE vs SYNASTRIE — Synthèse

| Ce que dit la synastrie | Ce que dit le composite |
|-------------------------|------------------------|
| [Comment ils interagissent] | [Qui ils sont ensemble] |
| [Chimie A↔B] | [Identité de AB] |
| [Friction A↔B] | [Problèmes de AB en tant qu'entité] |

**Cohérence** : [Est-ce que synastrie et composite racontent la même histoire ? Si non, EXPLIQUER la contradiction.]

---

## 📊 DÉTAILS DU SCORING

### Points positifs (composite) :
- [Aspect] : +X.X
- [Aspect] : +X.X
- **TOTAL : +XX.X**

### Points négatifs (composite) :
- [Aspect] : -X.X
- [Aspect] : -X.X
- **TOTAL : -XX.X**

### Calcul final :
Baseline : 5.0
+ Positifs : +XX.X
- Négatifs : -XX.X
= **SCORE : X.X/10**
```

---

## 🧠 Méthodologie Step-by-Step

### PHASE 1 : COLLECTE

1. Obtenir les données natales des deux personnes (date, heure, lieu)
2. Calculer les deux thèmes nataux complets
3. Extraire les positions en degrés absolus de chaque planète

### PHASE 2 : CALCUL COMPOSITE

4. Calculer le midpoint de chaque planète (formule ci-dessus)
5. Attention au problème des 180° — toujours prendre le midpoint COURT
6. Déterminer les maisons à partir de l'ASC composite
7. Calculer les aspects entre les planètes composites (orbes standards)

### PHASE 3 : CALCUL DAVISON

8. Calculer la date midpoint (jours juliens)
9. Calculer l'heure midpoint
10. Calculer les coordonnées midpoint (latitude et longitude)
11. Générer le thème natal de ce moment/lieu
12. Calculer les transits actuels sur le Davison

### PHASE 4 : INTERPRÉTATION

13. Interpréter chaque planète composite en signe + maison
14. Analyser tous les aspects du composite
15. Identifier RED FLAGS et GREEN FLAGS
16. Scorer chaque aspect (grille ci-dessus)
17. Interpréter le Davison avec focus sur le BUT de la relation
18. Analyser les transits sur le Davison

### PHASE 5 : SYNTHÈSE

19. Comparer composite et synastrie → cohérence ?
20. Intégrer le Davison → destin de la relation ?
21. Produire le diagnostic BRUTAL
22. Rédiger le rapport complet (format ci-dessus)

---

## ⚠️ Points Critiques à ne JAMAIS Oublier

1. **Le composite est ARTIFICIEL** — il n'a jamais existé dans le ciel. C'est un outil symbolique. Ne le traite pas comme un thème natal réel.

2. **Le Davison est RÉEL** — c'est un vrai moment dans le temps. C'est pour ça qu'on peut y appliquer des transits. C'est sa force.

3. **Composite ≠ synastrie** — Un couple peut avoir une EXCELLENTE synastrie (ils s'entendent bien) mais un composite HORRIBLE (l'entité couple est dysfonctionnelle). Et vice versa. **LES DEUX DOIVENT ÊTRE ANALYSÉS.**

4. **Sun carré Moon composite est LE red flag structurel** — C'est comme une personne dont l'ego et les émotions sont en guerre permanente. Le couple ne sait pas qui il est.

5. **Venus non-aspectée = MORT de l'amour** — Si Venus ne touche RIEN dans le composite, l'amour n'est connecté à aucune dynamique du couple. C'est une relation sans véritable amour.

6. **Saturn est AMBIVALENT** — Bien aspecté = durabilité. Mal aspecté = prison. Ne le diabolise pas automatiquement. Mais ne l'idéalise pas non plus.

7. **Jupiter peut masquer les problèmes** — Un Jupiter dominant rend le couple optimiste et chanceux, mais peut aussi les aveugler sur les vrais problèmes. "On est trop bien ensemble pour voir que ça va mal."

8. **Pluto au composite = TRANSFORMATION OBLIGATOIRE** — Le couple ne peut pas rester le même. Il évolue ou il meurt. Pas de compromis.

9. **Les transits sur le Davison > les transits sur le composite** — Parce que le Davison est réel. Les transits sur le composite sont symboliques. Les transits sur le Davison sont CONCRETS.

10. **TOUJOURS croiser composite ET synastrie** — Le composite seul ne suffit pas. La synastrie seule ne suffit pas. C'est l'ENSEMBLE qui donne le tableau complet.

---

**Retourne au [SKILL.md principal](../SKILL.md) pour workflow complet.**