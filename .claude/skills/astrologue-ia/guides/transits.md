# 📅 Guide : Transits et Prévisions Astrologiques

Ce guide contient la méthodologie COMPLÈTE pour analyser les transits planétaires et donner des prévisions avec timing précis.

---

## 🎯 Objectif

Identifier les transits planétaires majeurs pour une période donnée, déterminer leur impact sur le thème natal, et fournir un calendrier chronologique avec dates exactes d'action/évitement.

---

## 📊 Méthodologie Step-by-Step

### PHASE 1 : PRÉPARATION

#### 1.1 **Collecter les données**

**Thème natal** :
- Date, heure, lieu de naissance
- Fetch le thème complet (voir guide natal-chart.md)

**Période à analyser** :
- Format : "YYYY" (ex: "2026")
- Ou "MM.YYYY-MM.YYYY" (ex: "11.2025-11.2026")

#### 1.2 **Identifier les points sensibles du thème natal**

**Les transits impactent surtout** :
- ☀️ **Sun** (identité)
- 🌙 **Moon** (émotions)
- ♀ **Venus** (amour, valeurs)
- ♂ **Mars** (action, énergie)
- ⬆️ **ASC** (personnalité visible)
- ⬆️ **MC** (carrière, réputation)
- ⬇️ **IC** (foyer, racines)
- ⬇️ **DSC** (partenariats)

**Note les degrés exacts** :
- Ex: Sun Scorpio 21°53', Moon Aries 10°46', ASC Aquarius 11°57', MC Sagittarius 3°38'

**Ces degrés seront activés par les transits !**

#### 1.3 **Calculer les éphémérides de la période**

**MÉTHODE PRINCIPALE : Script Swiss Ephemeris (le plus fiable)**

```bash
# Transits complets pour une année (inclut éclipses, rétrogrades, conjonctions, lunes)
python3 scripts/ephemeris.py transits --date DD.MM.YYYY --time HH:MM --lat LAT --lon LON --year YYYY

# Éphémérides mensuelles détaillées (positions quotidiennes)
python3 scripts/ephemeris.py ephemeris --year YYYY --month MM

# Révolution solaire
python3 scripts/ephemeris.py solar-return --date DD.MM.YYYY --time HH:MM --lat LAT --lon LON --year YYYY

# Ajouter --json pour output JSON parsable
python3 scripts/ephemeris.py transits --date DD.MM.YYYY --time HH:MM --lat LAT --lon LON --year YYYY --json
```

Le script calcule automatiquement TOUTES les données nécessaires :
- Conjonctions rares (Saturn-Neptune, Jupiter-Saturn, etc.)
- Éclipses solaires et lunaires (type, date, position)
- Rétrogrades de toutes les planètes (dates de début/fin)
- Changements de signes des planètes lentes
- Nouvelles et Pleines Lunes (dates, signes, degrés)
- Transits des planètes lentes aux points nataux (aspects exacts)

**Sources complémentaires (si données additionnelles nécessaires)** :
1. WebSearch pour dates spécifiques ou événements astrologiques
2. https://cafeastrology.com pour interprétations supplémentaires

**Données à récupérer** :

**1. PLANÈTES LENTES** (changements longs, transformateurs) :
- **♃ Jupiter** : Signe actuel, entrées dans nouveaux signes, rétrogrades
- **♄ Saturn** : Signe actuel, entrées, rétrogrades, Saturn Return (si ~29-30 ans)
- **♅ Uranus** : Signe actuel, entrées, rétrogrades
- **♆ Neptune** : Signe actuel, entrées, rétrogrades
- **♇ Pluto** : Signe actuel, entrées, rétrogrades

**2. PLANÈTES RAPIDES** (timing court terme) :
- **♂ Mars** : Signes, rétrogrades (~tous les 2 ans)
- **♀ Venus** : Signes, rétrogrades (~tous les 18 mois)
- **☿ Mercury** : Rétrogrades (3-4x par an)

**3. LUMINAIRES** :
- **🌑 Nouvelles Lunes** (dates, signes, degrés)
- **🌕 Pleines Lunes** (dates, signes, degrés)
- **🌕 Supermoons** (si présentes)

**4. ÉCLIPSES** :
- **Éclipses solaires** (dates, signes, degrés)
- **Éclipses lunaires** (dates, signes, degrés)
- **Cycle des Nœuds** (North/South Node transitent quels signes)

**5. CONJONCTIONS RARES** :
- Jupiter-Saturn (tous les 20 ans)
- Saturn-Neptune (tous les 36 ans)
- Jupiter-Uranus, Jupiter-Neptune, etc.

**6. RÉVOLUTION SOLAIRE** (si période inclut l'anniversaire) :
- Positions planétaires le jour exact de l'anniversaire
- ASC/MC de la révolution solaire

---

### PHASE 2 : TRANSITS DES PLANÈTES LENTES

**Ces transits durent des MOIS voire des ANNÉES et causent des transformations majeures.**

---

#### 2.1 **PLUTON ♇ - Transformation Radicale, Mort/Renaissance**

**Cycle** : ~248 ans (passe ~12-30 ans par signe)

**Quand Pluton transite un point natal** :
- C'est une TRANSFORMATION PROFONDE
- Processus lent (plusieurs années)
- Mort symbolique → Renaissance
- Crises qui forcent l'évolution

##### **PLUTON CONJONCTION**

**Pluto conj Sun natal** :
- **Transformation de l'IDENTITÉ**
- Crise existentielle majeure
- Mort de l'ancien ego, naissance du nouveau
- Besoin de pouvoir intense
- Peut manifester : changement radical de vie, divorce, changement de carrière
- **Durée** : 2-3 ans (rétrogrades inclus)
- **Intensité** : 10/10

**Pluto conj Moon natal** :
- **Transformation ÉMOTIONNELLE profonde**
- Crises émotionnelles intenses
- Peut manifester : perte d'un proche, fin de relation, dépression puis renaissance
- Émotions deviennent volcaniques
- **Durée** : 2-3 ans
- **Intensité** : 10/10

**Pluto conj Venus natal** :
- **Transformation de l'AMOUR et des valeurs**
- Relations intenses, obsessionnelles
- Peut manifester : rencontre transformatrice, rupture cataclysmique, redéfinition de ce qu'on valorise
- Jalousie, possessivité extrême
- **Durée** : 2-3 ans
- **Intensité** : 9/10

**Pluto conj ASC natal** :
- **Transformation totale de la PERSONNALITÉ**
- Renaissance physique possible (perte de poids, changement look radical)
- Magnétisme intense
- Peut manifester : devenir une personne complètement différente
- **Durée** : 2-3 ans
- **Intensité** : 10/10

**Pluto conj MC natal** :
- **Transformation de la CARRIÈRE**
- Mort professionnelle → Renaissance
- Peut manifester : licenciement puis ascension fulgurante, changement radical de voie
- Pouvoir professionnel intense
- **Durée** : 2-3 ans
- **Intensité** : 9/10

##### **PLUTON CARRÉ**

**Impact** : CRISE qui FORCE la transformation

**Pluto square Sun** :
- Crise d'identité, lutte de pouvoir
- Quelqu'un/quelque chose menace ton ego
- **Intensité** : 9/10

**Pluto square Moon** :
- Crises émotionnelles répétées
- Peut manifester : pertes, séparations
- **Intensité** : 9/10

##### **PLUTON TRIGONE**

**Impact** : Transformation FACILITÉE, empowerment

**Pluto trine Sun/Moon/Venus** :
- Transformation sans crise majeure
- Empowerment naturel
- **Intensité** : 7/10 (positif)

##### **PLUTON OPPOSITION**

**Impact** : Confrontation avec l'OMBRE

**Pluto opp Sun/Moon** :
- Quelqu'un/quelque chose incarne ton ombre
- Lutte de pouvoir externe
- **Intensité** : 8/10

---

#### 2.2 **NEPTUNE ♆ - Dissolution, Spiritualité, Illusion**

**Cycle** : ~165 ans (~14 ans par signe)

**Quand Neptune transite un point natal** :
- DISSOLUTION des frontières
- Spiritualisation OU confusion/illusion
- Processus lent (plusieurs années)
- Idéalisation puis désillusion

##### **NEPTUNE CONJONCTION**

**Neptune conj Sun natal** :
- **Dissolution de l'IDENTITÉ**
- Crise d'identité, confusion "qui suis-je?"
- Quête spirituelle intense
- Risque : Perte de soi, addiction, fuite
- Positif : Éveil spirituel, compassion, créativité
- **Durée** : 2-3 ans
- **Intensité** : 8/10

**Neptune conj Venus natal** :
- **Amour IDÉALISÉ**
- Rencontre qui semble parfaite
- Puis DÉSILLUSION brutale
- Risque : Tomber amoureux d'une illusion
- Positif : Amour transcendantal si partenaire authentique
- **Durée** : 2-3 ans
- **Intensité** : 8/10

**Neptune conj Mars natal** :
- **PERTE D'ÉNERGIE**
- Action floue, difficulté à agir
- Fatigue chronique possible
- Risque : Dépression, inaction
- Positif : Action spirituelle, artistique, compassionnelle
- **Durée** : 2-3 ans
- **Intensité** : 7/10

**Neptune conj ASC natal** :
- **Dissolution de l'EGO**
- Devenir invisible, éthéré
- Spiritualisation de la personnalité
- Risque : Confusion identitaire, addiction
- Positif : Médium, artiste, mystique
- **Durée** : 2-3 ans
- **Intensité** : 8/10

##### **NEPTUNE CARRÉ**

**Impact** : ILLUSIONS, tromperies

**Neptune square Sun/Venus** :
- Déceptions majeures
- Voir la réalité telle qu'elle est (douloureux)
- **Intensité** : 7/10

##### **NEPTUNE TRIGONE**

**Impact** : Inspiration SPIRITUELLE, créativité

**Neptune trine Sun/Moon/Venus** :
- Période artistique, mystique
- Intuition amplifiée
- **Intensité** : 6/10 (positif)

---

#### 2.3 **URANUS ♅ - Révolution, Changement Soudain, Liberté**

**Cycle** : ~84 ans (~7 ans par signe)

**Quand Uranus transite un point natal** :
- CHANGEMENTS SOUDAINS
- Ruptures, libérations
- Processus rapide (quelques mois, mais répété avec rétrogrades)
- Imprévisible, électrique

##### **URANUS CONJONCTION**

**Uranus conj Sun natal** :
- **RÉVOLUTION de l'identité**
- Besoin soudain de liberté
- Changement radical de vie
- Peut manifester : Quitter job stable pour startup, déménagement soudain
- **Durée** : 1-2 ans (avec rétrogrades)
- **Intensité** : 8/10

**Uranus conj Moon natal** :
- **Changements émotionnels SOUDAINS**
- Ruptures familiales possibles
- Besoin de liberté émotionnelle
- Peut manifester : Quitter foyer, séparation soudaine
- **Durée** : 1-2 ans
- **Intensité** : 8/10

**Uranus conj Venus natal** :
- **Changements amoureux RADICAUX**
- Ruptures soudaines OU rencontres électriques
- Besoin de nouvelles valeurs
- Peut manifester : Coup de foudre inattendu, divorce soudain
- **Durée** : 1-2 ans
- **Intensité** : 8/10

**Uranus conj Mars natal** :
- **Énergie ERRATIQUE**
- Accidents possibles (Mars = action, Uranus = soudain)
- Besoin d'action libératrice
- **Durée** : 1-2 ans
- **Intensité** : 7/10

**Uranus conj ASC natal** :
- **CHANGEMENT COMPLET de vie**
- Nouvelle personnalité
- Peut manifester : Changement look radical, nouvelle identité
- **Durée** : 1-2 ans
- **Intensité** : 9/10

##### **URANUS OPPOSITION** (~42 ans)

**URANUS OPPOSITION = CRISE DE LA QUARANTAINE**

**Uranus opp Sun/Moon/ASC natal** :
- Besoin soudain de changement radical
- "Je dois changer ma vie MAINTENANT"
- Peut manifester : Divorce, changement carrière, relocation
- **Durée** : 1-2 ans
- **Intensité** : 9/10

##### **URANUS CARRÉ**

**Impact** : Changements FORCÉS, instabilité

**Uranus square Sun/Moon** :
- Changements non désirés
- Instabilité, nervosité
- **Intensité** : 7/10

##### **URANUS TRIGONE**

**Impact** : Innovations FACILES, libération

**Uranus trine Sun/Venus** :
- Changements positifs
- Nouvelles opportunités
- **Intensité** : 6/10 (positif)

---

#### 2.4 **SATURN ♄ - Responsabilité, Limitation, Leçon**

**Cycle** : ~29 ans (~2.5 ans par signe)

**Quand Saturn transite un point natal** :
- TESTS, responsabilités
- Restrictions, maturation
- Processus lent (2-3 ans avec rétrogrades)
- Leçons karmiques

##### **SATURN RETURN** (~29-30 ans, ~58-59 ans)

**LE TRANSIT LE PLUS IMPORTANT DE LA VIE**

**Saturn revient à sa position natale** :
- **TEST MAJEUR de vie**
- Fin d'un cycle de 29 ans
- Début d'un nouveau cycle
- Maturation forcée

**Ce qui arrive** :
- Tout ce qui n'est pas AUTHENTIQUE s'effondre
  - Job qui ne te correspond pas → licenciement/démission
  - Relation bancale → rupture
  - Vie basée sur les attentes des autres → crise
- Responsabilités massives
- Sentiment de lourdeur, dépression possible
- MAIS : Opportunité de construire une vie VRAIE

**Timing** :
- 1er Saturn Return : 28-30 ans
- 2e Saturn Return : 57-59 ans
- 3e Saturn Return : 86-88 ans (si vécu)

**Durée du transit** : 2-3 ans (pic à 29 ans exact)

**Intensité** : 10/10 (life-changing)

##### **SATURN CONJONCTION**

**Saturn conj Sun natal** :
- **TEST de l'identité**
- Ego bridé, sentiment d'échec
- Dépression possible
- Leçon : Accepter les limites, construire patiemment
- **Durée** : 2-3 ans
- **Intensité** : 8/10

**Saturn conj Moon natal** :
- **Restriction ÉMOTIONNELLE**
- Tristesse, lourdeur émotionnelle
- Deuils possibles
- Leçon : Maturité émotionnelle
- **Durée** : 2-3 ans
- **Intensité** : 8/10

**Saturn conj Venus natal** :
- **Test du COUPLE**
- Solitude amoureuse OU test de la relation
- Si relation solide : engagement (mariage)
- Si relation bancale : rupture
- **Durée** : 2-3 ans
- **Intensité** : 8/10

**Saturn conj ASC natal** :
- **Responsabilités sur les épaules**
- Poids de la vie
- Apparence vieillie
- Leçon : Devenir adulte
- **Durée** : 2-3 ans
- **Intensité** : 8/10

**Saturn conj MC natal** :
- **Test PROFESSIONNEL**
- Ambition confrontée à la réalité
- Soit promotion (si travaillé), soit stagnation (si pas travaillé)
- **Durée** : 2-3 ans
- **Intensité** : 9/10

##### **SATURN CARRÉ**

**Impact** : OBSTACLES, blocages

**Saturn square Sun/Moon/Venus** :
- Défis, restrictions
- Sentiment d'échec
- **Intensité** : 7/10

##### **SATURN TRIGONE**

**Impact** : Structure FACILITÉE, récompense du travail

**Saturn trine Sun/MC** :
- Récolte des efforts passés
- Stabilité, reconnaissance
- **Intensité** : 6/10 (positif)

##### **SATURN OPPOSITION**

**Impact** : Confrontation avec RESPONSABILITÉS

**Saturn opp Sun** :
- Quelqu'un/quelque chose te confronte à tes limites
- **Intensité** : 7/10

---

#### 2.5 **JUPITER ♃ - Expansion, Chance, Opportunités**

**Cycle** : ~12 ans (~1 an par signe)

**Quand Jupiter transite un point natal** :
- EXPANSION, croissance
- Opportunités, chance
- Processus rapide (quelques mois)
- Le transit le plus POSITIF

##### **JUPITER RETURN** (~12, 24, 36, 48, 60 ans)

**Jupiter revient à sa position natale** :
- **Cycle de CROISSANCE**
- Nouvelles opportunités
- Expansion dans le domaine de Jupiter natal
- **Durée** : Quelques mois
- **Intensité** : 7/10 (positif)

##### **JUPITER CONJONCTION**

**Jupiter conj Sun natal** :
- **CONFIANCE maximale**
- Succès, reconnaissance
- Opportunités professionnelles
- Optimisme débordant
- **Attention** : Sur-optimisme, excès
- **Durée** : 2-3 mois (passage direct) + rétrograde
- **Intensité** : 8/10 (positif)

**Jupiter conj Moon natal** :
- **Expansion ÉMOTIONNELLE**
- Bonheur, générosité
- Peut manifester : Naissance d'un enfant, déménagement dans maison plus grande
- **Durée** : 2-3 mois
- **Intensité** : 7/10 (positif)

**Jupiter conj Venus natal** :
- **AMOUR facile, abondance**
- Rencontres faciles
- Argent qui rentre
- Plaisirs, luxe
- **Durée** : 2-3 mois
- **Intensité** : 8/10 (positif)

**Jupiter conj MC natal** :
- **SUCCÈS PROFESSIONNEL**
- Promotion, reconnaissance
- Opportunités de carrière
- **Meilleur transit pour réussite professionnelle**
- **Durée** : 2-3 mois
- **Intensité** : 9/10 (positif)

**Jupiter conj ASC natal** :
- **Nouvelle phase de vie POSITIVE**
- Expansion personnelle
- Confiance en soi
- **Durée** : 2-3 mois
- **Intensité** : 7/10 (positif)

##### **JUPITER TRIGONE**

**Impact** : Opportunités FACILES, chance

**Jupiter trine Sun/Venus/MC** :
- Opportunités sans effort
- Période chanceuse
- **Intensité** : 7/10 (positif)

##### **JUPITER CARRÉ**

**Impact** : EXCÈS, sur-optimisme

**Jupiter square Sun/Venus** :
- Trop de confiance
- Dépenses excessives
- Promettre trop
- **Intensité** : 4/10 (mineur)

##### **JUPITER OPPOSITION**

**Impact** : Expansion vs RÉALITÉ

**Jupiter opp Sun** :
- Optimisme confronté aux limites
- **Intensité** : 5/10

---

### PHASE 3 : TRANSITS DES PLANÈTES RAPIDES

**Ces transits durent des JOURS à quelques MOIS et affectent le timing court terme.**

---

#### 3.1 **MARS ♂ - Action, Énergie, Conflit**

**Cycle** : ~2 ans (passe ~1.5-2 mois par signe)

##### **MARS RÉTROGRADE** (~tous les 2 ans, ~2 mois)

**Dates à identifier** : Quand Mars devient rétrograde dans la période analysée

**Impact** :
- **Énergie BLOQUÉE**
- Frustration, colère rentrée
- **À ÉVITER** :
  - Lancer de nouveaux projets
  - Chirurgie élective
  - Compétitions sportives
  - Initier des conflits
- Frustration sexuelle possible
- Accidents plus fréquents (attention accrue nécessaire)

**Intensité** : 6/10 (bloquant)

##### **MARS CONJONCTION** (points nataux)

**Mars conj Sun natal** :
- **Énergie maximale**
- Bon moment pour ACTION
- Attention à l'agressivité
- **Durée** : 3-5 jours
- **À FAIRE** : Lancer projets, compétition, sport

**Mars conj Moon natal** :
- **Émotions BOUILLONNANTES**
- Colère émotionnelle
- Impulsivité
- **Durée** : 3-5 jours

**Mars conj Venus natal** :
- **Passion SEXUELLE**
- Rencontres possibles
- Désir intense
- **Durée** : 3-5 jours
- **À FAIRE** : Dating, séduction

**Mars conj MC natal** :
- **Action PROFESSIONNELLE**
- Bon moment pour demander promotion, négocier
- **Durée** : 3-5 jours

---

#### 3.2 **VÉNUS ♀ - Amour, Plaisir, Argent**

**Cycle** : ~1 an (passe ~3-4 semaines par signe)

##### **VÉNUS RÉTROGRADE** (~tous les 18 mois, ~40 jours)

**CRITIQUE si tu as Venus rétro natal (comme dans exemple 14.11.1994)**

**Dates à identifier** : Quand Venus devient rétrograde

**Impact** :
- **EX REVIENNENT**
- Remise en question amour/valeurs
- Relations du passé ressurgissent
- **À ÉVITER** :
  - Mariages
  - Gros achats (bijoux, luxe)
  - Chirurgie esthétique
- **Si tu as Venus rétro natal** : C'est paradoxalement une période de CLARTÉ pour toi

**Intensité** : 7/10

##### **VÉNUS CONJONCTION** (points nataux)

**Venus conj Sun natal** :
- **Charme maximal**
- Bon moment pour dating
- **Durée** : 2-3 jours

**Venus conj Venus natal** :
- **ANNIVERSAIRE de Venus**
- Amour facile
- Achats, plaisir
- **Durée** : 2-3 jours

**Venus conj MC natal** :
- **Succès dans relations publiques**
- Bon moment pour networking
- **Durée** : 2-3 jours

---

#### 3.3 **MERCURY ☿ - Communication, Mental**

**Cycle** : ~1 an (passe ~2-3 semaines par signe)

##### **MERCURY RÉTROGRADE** (3-4x par an, ~3 semaines)

**LE PLUS CONNU, LE PLUS REDOUTÉ**

**Dates à identifier** : Quand Mercury devient rétrograde (arrive 3-4 fois par an)

**Impact** :
- **Communication FOIREUSE**
- Malentendus, messages perdus
- **Problèmes tech** : ordinateurs, téléphones, voitures
- **Problèmes transports** : retards, annulations
- **À ÉVITER** :
  - Signer contrats importants
  - Acheter électronique
  - Lancer sites web
  - Voyages importants (sauf revisiter lieux passés)
- **À FAIRE** :
  - RE-visiter, RE-faire, RE-penser
  - Finir projets commencés avant
  - Retrouver anciens amis

**Si tu as Mercury rétro natal** : Tu gères mieux que les autres ce transit

**Intensité** : 5/10 (chiant mais gérable)

---

### PHASE 4 : NOUVELLES & PLEINES LUNES

**Les Lunes marquent le timing court terme (mois par mois).**

---

#### 4.1 **NOUVELLE LUNE 🌑** (Sun conjonction Moon)

**Arrive tous les 28-29 jours**

**Impact** :
- **NOUVEAUX DÉPARTS**
- Intentions, graines plantées
- Début de cycles

**Comment utiliser** :
1. Identifie la date de la Nouvelle Lune
2. Note le SIGNE et le DEGRÉ
3. Si la NL tombe sur un point natal (±3°), impact FORT

**Nouvelle Lune sur Sun natal** :
- **NOUVEL AN PERSONNEL**
- Excellent pour intentions de l'année
- Reset identitaire

**Nouvelle Lune sur Moon natal** :
- Nouveau départ ÉMOTIONNEL
- Intentions sur vie privée/famille

**Nouvelle Lune sur Venus natal** :
- Nouveau départ AMOUREUX
- Bon moment pour premier contact relationnel

**Nouvelle Lune sur MC natal** :
- Nouveau départ PROFESSIONNEL
- Lancer projets business

**Intensité** : 5/10 (subtil mais utile)

---

#### 4.2 **PLEINE LUNE 🌕** (Sun opposition Moon)

**Arrive tous les 14-15 jours après Nouvelle Lune**

**Impact** :
- **CULMINATIONS, révélations**
- Émotions fortes
- Fins, conclusions
- Énergie émotionnelle maximale

**Comment utiliser** :
1. Identifie la date de la Pleine Lune
2. Note le SIGNE et le DEGRÉ
3. Si la PL tombe sur un point natal (±3°), émotions INTENSES

**Pleine Lune sur Sun natal** :
- Culmination identitaire
- Révélation sur qui tu es

**Pleine Lune sur Moon natal** :
- **ÉMOTIONS MAXIMALES**
- Crises émotionnelles possibles
- Catharsis

**Pleine Lune sur Venus natal** :
- Culmination amoureuse
- Déclarations, ruptures

**Pleine Lune sur MC natal** :
- Culmination professionnelle
- Reconnaissance publique

**SUPERMOON** :
- Impact AMPLIFIÉ x2
- Surtout si tu as Moon importante dans ton thème

**Intensité** : 6/10 (émotions fortes)

---

### PHASE 5 : ÉCLIPSES (Portails de Destinée)

**Les éclipses sont les transits les PLUS PUISSANTS des luminaires.**

---

#### 5.1 **ÉCLIPSE SOLAIRE** (Nouvelle Lune + Nœuds)

**Arrive 2x par an (parfois 3x)**

**Impact** :
- **NOUVEAUX DÉPARTS MAJEURS**
- Portes qui S'OUVRENT
- Changements soudains
- Impact dure ~6 MOIS

**Si éclipse solaire sur point natal (±5°)** :
- **ÉVÉNEMENT MAJEUR garanti**
- Nouveau chapitre de vie commence

**Éclipse solaire sur Sun natal** :
- Nouvelle identité commence
- Changement de vie radical

**Éclipse solaire sur Moon natal** :
- Nouveau départ émotionnel/familial
- Peut manifester : Naissance, déménagement, nouvelle relation

**Éclipse solaire sur ASC natal** :
- Nouvelle personnalité émerge
- Changement look/vie complet

**Éclipse solaire sur MC natal** :
- Nouvelle carrière commence
- Opportunité majeure

**Intensité** : 9/10 (life-changing)

---

#### 5.2 **ÉCLIPSE LUNAIRE** (Pleine Lune + Nœuds)

**Arrive 2x par an (parfois 3x)**

**Impact** :
- **CULMINATIONS, révélations**
- Portes qui SE FERMENT
- Fins nécessaires
- Impact dure ~6 MOIS

**Si éclipse lunaire sur point natal (±5°)** :
- **ÉVÉNEMENT MAJEUR garanti**
- Quelque chose se termine

**Éclipse lunaire sur Sun natal** :
- Identité ancienne se termine
- Révélation sur qui tu es vraiment

**Éclipse lunaire sur Moon natal** :
- **CATHARSIS ÉMOTIONNELLE MAJEURE**
- Fin cycle émotionnel
- Peut manifester : Rupture, deuil, libération

**Éclipse lunaire sur Venus natal** :
- Fin cycle amoureux
- Rupture OU engagement (fin du flou)

**Éclipse lunaire sur MC natal** :
- Fin cycle professionnel
- Démission, licenciement, OU promotion (changement)

**Intensité** : 9/10 (life-changing)

---

#### 5.3 **CYCLE DES NŒUDS LUNAIRES** (☊☋)

**Les Nœuds changent de signes tous les 18-19 mois**

**Impact** :
- Change l'**AXE DES ÉCLIPSES**
- Nouveaux domaines de vie activés

**Exemple** :
- Nœuds en axe Aries-Libra (2023-2025) : Thèmes = soi vs autres, indépendance vs relations
- Nœuds en axe Pisces-Virgo (jan 2025-juil 2026) : Thèmes = spiritualité vs matériel, foi vs pragmatisme

**Si Nœuds transitent tes points nataux** :
- North Node conj planète = Évolution vers ce domaine
- South Node conj planète = Lâcher-prise de ce domaine

**Intensité** : 7/10 (karmique)

---

### PHASE 6 : CONJONCTIONS RARES

**Ces transits arrivent rarement et marquent des ÉPOQUES.**

---

#### 6.1 **SATURN-NEPTUNE** (tous les 36 ans)

**DERNIER** : 1989
**PROCHAIN** : **20 FÉVRIER 2026 à 0° ARIES**

**Impact** :
- **RÊVE DEVIENT RÉALITÉ** (best case)
- **GRANDE DÉSILLUSION** (worst case)
- Union du matériel (Saturn) et du spirituel (Neptune)
- Structure + Dissolution = Création de nouvelles formes

**Si cette conjonction touche ton thème** :
- Sur Sun/Moon/ASC/MC : **ÉVÉNEMENT MAJEUR DE VIE**
- Connection karmique, rencontre destinée
- Manifestation de rêves anciens
- OU désillusion sur vieux rêves

**Exemple session d'origine** :
- User né 14.11.1994, Moon Aries 10°46'
- Saturn-Neptune 20 fév 2026 à 0° Aries
- Transit la Moon de près (10° d'écart)
- = Rencontre KARMIQUE prédite ("maîtresse des ténèbres")

**Intensité** : 10/10 (arrive une fois dans la vie)

---

#### 6.2 **JUPITER-SATURN** (tous les 20 ans)

**DERNIER** : 21 décembre 2020 (0° Aquarius)
**PROCHAIN** : 2040

**Impact** :
- **"GRANDE CONJONCTION"**
- Changements SOCIÉTAUX
- Nouvelle ère commence
- Changement de paradigme

**Intensité** : 8/10 (générationnel)

---

#### 6.3 **JUPITER-PLUTO** (tous les 13 ans)

**Impact** :
- Pouvoir + Expansion
- Transformation facilitée
- Succès par transformation

**Intensité** : 7/10

---

### PHASE 7 : RÉVOLUTION SOLAIRE

**Le thème du Solar Return prédit l'année à venir.**

---

#### 7.1 **Qu'est-ce qu'une Révolution Solaire ?**

**Révolution Solaire** = Thème astrologique calculé pour le moment EXACT où le Sun transite revient à sa position natale (ton anniversaire).

**Principe** :
- Chaque année, le Sun revient au même degré (ex: 21° Scorpio)
- Mais les AUTRES planètes sont à des positions différentes
- Et surtout : ASC et MC sont différents selon OÙ tu es géographiquement

**Ce thème prédit l'année du [anniversaire N] au [anniversaire N+1]**

---

#### 7.2 **Comment analyser une Révolution Solaire**

**Éléments clés** :

1. **ASC de la RS** : Ton énergie/masque de l'année
   - Ex: ASC Aries RS = année d'action, de nouveaux départs

2. **MC de la RS** : Focus professionnel de l'année
   - Ex: MC Capricorn RS = année d'ambition, de travail acharné

3. **Planètes ANGULAIRES de la RS** (sur ASC/MC/IC/DSC) :
   - Ces planètes DOMINENT l'année
   - Ex: Venus sur ASC RS = année d'amour, de charme
   - Ex: Saturn sur MC RS = année de responsabilités pro, de tests

4. **Maison du Sun de la RS** : Domaine principal de focus
   - Sun en H1 RS : Focus sur soi, identité
   - Sun en H7 RS : Focus sur relations, partenariats
   - Sun en H10 RS : Focus sur carrière

5. **Aspects majeurs de la RS** :
   - Carrés/Oppositions = challenges de l'année
   - Trigones/Sextiles = facilités de l'année

---

#### 7.3 **Relocation du Solar Return**

**STRATÉGIE AVANCÉE** : Tu peux CHOISIR où passer ton anniversaire pour avoir un meilleur SR !

**Principe** :
- Si tu passes ton anniversaire à **Marseille**, le SR est calculé pour Marseille
- Si tu passes ton anniversaire à **Paris**, le SR est calculé pour Paris
- **ASC et MC changent** selon la localisation !

**Exemple session d'origine** :
- User demande SR Marseille vs Paris
- On compare les deux
- On recommande où passer l'anniversaire pour meilleur SR

**Comment choisir** :
- Vérifie quelle ville met les planètes BÉNÉFIQUES (Jupiter, Venus) sur les angles
- Évite les villes qui mettent Saturn/Mars/Pluto sur ASC/MC

---

### PHASE 8 : GÉNÉRATION DU RAPPORT

**Format du rapport de transits :**

```markdown
# 📅 TRANSITS & PRÉVISIONS [PÉRIODE]

## 🎯 RÉSUMÉ EXÉCUTIF

**Période analysée** : [dates]

**Top 5 dates les plus importantes** :
1. [Date] - [Événement] - [Impact]
2. [Date] - [Événement] - [Impact]
3. [...]

**Thèmes principaux de la période** :
- [Thème 1] (basé sur transits dominants)
- [Thème 2]
- [Thème 3]

---

## 📆 CALENDRIER CHRONOLOGIQUE

Liste TOUS les événements par ordre chronologique :

### **[MOIS] [ANNÉE]**

#### **[Date exacte] - [Événement astrologique]**

**Type** : [Transit planète lente / Nouvelle Lune / Éclipse / etc.]

**Impact sur ton thème** :
- [Quelle planète natale est touchée]
- [Quel aspect exact]
- [Orbe en degrés]

**Signification** :
[Interprétation brutale de ce qui va se passer]

**À FAIRE** :
- [Actions concrètes recommandées]

**À ÉVITER** :
- [Actions à ne pas faire]

**Intensité** : X/10

**Durée de l'effet** : [jours / semaines / mois]

---

[RÉPÈTE pour TOUS les événements de la période]

---

## 🎯 PÉRIODES CLÉS PAR DOMAINE

### 💕 **AMOUR & RELATIONS**

#### **Périodes FAVORABLES** :

**[Dates]** : [Transit]
- **Pourquoi c'est bon** : [...]
- **Ce qui sera facilité** : [...]
- **Action recommandée** : [...]

#### **Périodes DIFFICILES** :

**[Dates]** : [Transit]
- **Pourquoi c'est dur** : [...]
- **Ce qui sera challengé** : [...]
- **Comment naviguer** : [...]

#### **MEILLEUR MOMENT pour rencontre** :
**[Date précise]** : [Justification basée sur transits]

---

### 💼 **CARRIÈRE & ARGENT**

[Même structure]

---

### 🔮 **SPIRITUALITÉ & TRANSFORMATION**

[Même structure]

---

### 🏠 **FOYER & FAMILLE**

[Même structure]

---

### 🎲 **LUCKY DAYS** (Chance/Jeux)

**Si user demande lucky days pour gambling** :

Liste des jours avec :
- Jupiter aspects favorables (trigone/sextile natal Jupiter)
- Pleine Lune sur natal Jupiter
- Venus trigone natal Sun
- Pas de Mercury/Mars rétrogrades
- Pas d'éclipses

**[Date]** : [Transits favorables]
- **Pourquoi c'est lucky** : [...]
- **Intensité luck** : X/10

---

## ⚠️ **PÉRIODES À ÉVITER**

### **NE PAS signer contrats pendant** :
- [Dates Mercury rétrograde]

### **NE PAS se marier pendant** :
- [Dates Venus rétrograde]
- [Dates éclipses]

### **NE PAS lancer projets pendant** :
- [Dates Mars rétrograde]

### **NE PAS prendre décisions importantes pendant** :
- [Dates éclipses ±3 jours]

---

## 🔥 **TOP 5 DATES GAME-CHANGER**

### **1. [Date]** - [Événement]

**Impact** : X/10

**Ce qui va se passer** :
[Prédiction brutale et concrète]

**Ce qu'il faut faire** :
[Action précise]

**Pourquoi c'est crucial** :
[Explication astrologique]

---

[Répète pour top 5]

---

## 📊 **GRAPHIQUE D'INTENSITÉ**

Timeline visuelle de l'intensité des transits :

```
Jan 2026  ████░░░░░░ (4/10) - Calme, construction
Fév 2026  ██████████ (10/10) - INTENSE! Saturn-Neptune conj
Mar 2026  ██████░░░░ (6/10) - Intégration
Avr 2026  ████░░░░░░ (4/10) - Respiration
Mai 2026  ███████░░░ (7/10) - Jupiter actif
Jun 2026  █████████░ (9/10) - Éclipses + Jupiter
Jul 2026  █████░░░░░ (5/10) - Modéré
Aoû 2026  ████░░░░░░ (4/10) - Calme
Sep 2026  ██████░░░░ (6/10) - Préparation
Oct 2026  ██████████ (10/10) - Venus rétro TEST
Nov 2026  █████████░ (9/10) - Post-test intégration
Déc 2026  ██████░░░░ (6/10) - Clôture année
```

---

## 🎯 **STRATÉGIE GLOBALE POUR LA PÉRIODE**

**Basé sur l'ensemble des transits** :

### **Phase 1** : [Dates] - [Nom de la phase]
**Focus** : [...]
**Action** : [...]

### **Phase 2** : [Dates] - [Nom de la phase]
**Focus** : [...]
**Action** : [...]

[...]

---

## 📋 **CHECKLIST MENSUELLE**

### **[MOIS]**

- [ ] [Action 1 basée sur transit 1]
- [ ] [Action 2 basée sur transit 2]
- [ ] Éviter [action] car [rétrograde/éclipse]

[Répète pour chaque mois]

---

## ⚡ **RÉVOLUTION SOLAIRE** [si anniversaire dans période]

**Date anniversaire** : [date]

**Analyse Solar Return [Année]** :

### **ASC de la RS** : [Signe]
**Ton énergie de l'année** : [...]

### **MC de la RS** : [Signe]
**Focus professionnel** : [...]

### **Planètes angulaires RS** :
- [Planète] sur [angle] : [Signification]

### **Sun en maison RS** : H[X]
**Domaine principal** : [...]

### **Thème de l'année** :
[Interprétation globale du SR]

### **Relocation Solar Return** [si demandé] :
**Marseille vs Paris** (ou autres villes) :
- Marseille : [Analyse]
- Paris : [Analyse]
- **Recommandation** : [Où passer l'anniversaire pour meilleur SR]

```

---

## 🔍 Données de référence 2026 (vérifiées via Swiss Ephemeris)

**Saturn-Neptune conjonction exacte** : ~15 février 2026 à 0° Aries (séparation < 0.5°)
**Venus rétrograde** : 4 octobre -> 15 novembre 2026 (Scorpio 8° -> Libra 22°)
**Mercury rétrogrades 2026** : fév-mars (Pisces), juin-juil (Cancer), oct-nov (Scorpio)
**Éclipses 2026** : Solaire 17 fév (Aquarius), Lunaire 3 mars (Virgo), Solaire 12 août (Leo), Lunaire 28 août (Pisces)

---

## ⚠️ Points critiques

1. **TOUJOURS donner des DATES exactes** - Jamais "bientôt" ou "prochainement"
2. **Calculer les ORBES précis** - Transit efficace si ±3° pour Lunes, ±8° pour planètes lentes
3. **Identifier les RÉTROGRADES** - Ils changent TOUT
4. **Prioriser les transits LENTS** - Ils transforment, les rapides timing court terme
5. **Éclipses > tout** - Si éclipse sur point natal, c'est LA date game-changer
6. **Conjonctions rares = ÉPOQUE** - Saturn-Neptune 2026 arrive 1x dans la vie
7. **Relocation SR = stratégie** - On peut CHOISIR où passer son anniversaire

---

**Retourne au [SKILL.md principal](../SKILL.md) pour workflow complet.**
