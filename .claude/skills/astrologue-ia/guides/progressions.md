# 🔄 Guide : Progressions, Profections & Directions d'Arc Solaire

Ce guide contient la méthodologie COMPLÈTE pour analyser l'**évolution interne** (progressions secondaires), le **timing annuel** (profections) et les **événements externes** (directions d'arc solaire). Ce sont les techniques PRÉDICTIVES les plus puissantes de l'astrologie traditionnelle et moderne.

---

## 🎯 Objectif

Déterminer **où en est la personne dans son évolution personnelle**, quel domaine de vie est activé CETTE ANNÉE, et quand les événements majeurs vont se manifester concrètement. Les transits te disent ce qui ARRIVE de l'extérieur. Les progressions te disent ce qui CHANGE à l'intérieur. Les profections te disent QUEL DOMAINE est au centre. Les arcs solaires te disent QUAND ça pète.

**Combinés ensemble = prédiction CHIRURGICALE.**

---

# PARTIE 1 : PROGRESSIONS SECONDAIRES 🌀

## 📐 Principe fondamental

**1 jour après la naissance = 1 AN de vie.**

C'est pas de la poésie, c'est de la mécanique céleste. Pour connaître ton thème progressé à 30 ans, tu regardes les positions planétaires **30 jours après ta naissance**. Point.

**Pourquoi ça marche ?** Parce que le ratio jour/an reflète la relation Terre-Soleil (la Terre tourne sur elle-même en 1 jour, autour du Soleil en 1 an). C'est le même principe que les fractales : le micro reflète le macro.

### Comment calculer concrètement

```bash
# Progressions : calculer le thème pour [date_naissance + âge_en_jours]
# Ex: né 14.11.1994, progressions à 30 ans = thème du 14.12.1994 (30 jours après)
python3 scripts/ephemeris.py natal --date 14.12.1994 --time 13:04 --lat 43.71 --lon 7.26 --tz 1

# Progressions à 25 ans = thème du 09.12.1994 (25 jours après)
python3 scripts/ephemeris.py natal --date 09.12.1994 --time 13:04 --lat 43.71 --lon 7.26 --tz 1

# Progressions à 40 ans = thème du 24.12.1994 (40 jours après)
python3 scripts/ephemeris.py natal --date 24.12.1994 --time 13:04 --lat 43.71 --lon 7.26 --tz 1
```

**⚠️ L'HEURE COMPTE** : Garde la même heure de naissance. Le Moon progressé bouge VITE (~13° par jour = ~13° par an en progressions), donc une erreur d'heure de naissance = erreur de MOIS sur le Moon progressé.

---

## ☀️ SOLEIL PROGRESSÉ - Transformation d'Identité

**Vitesse** : Avance d'environ **1° par an**
**Change de signe** : Tous les **~30 ans** (dépend du signe natal)

### Pourquoi c'est CRUCIAL

Le Soleil progressé qui change de signe = **TRANSFORMATION D'IDENTITÉ PROFONDE**. C'est pas un transit qui passe, c'est un changement de NATURE. Tu deviens littéralement une version différente de toi-même.

### Tableau des changements de signe du Sun progressé

| Sun natal | → Sun progressé à ~30 ans | Transformation |
|-----------|--------------------------|----------------|
| ♈ Aries | → Taurus | De l'impulsion → la stabilisation |
| ♉ Taurus | → Gemini | De la sécurité → la curiosité |
| ♊ Gemini | → Cancer | De la dispersion → l'ancrage émotionnel |
| ♋ Cancer | → Leo | Du cocon familial → l'expression de soi |
| ♌ Leo | → Virgo | Du drama → l'humilité et le service |
| ♍ Virgo | → Libra | Du perfectionnisme → l'harmonie relationnelle |
| ♎ Libra | → Scorpio | De la politesse → la profondeur brute |
| ♏ Scorpio | → Sagittarius | De l'intensité obsessionnelle → l'expansion et la liberté |
| ♐ Sagittarius | → Capricorn | De l'aventure → la structure et l'ambition |
| ♑ Capricorn | → Aquarius | De la tradition → la révolution |
| ♒ Aquarius | → Pisces | Du détachement → la dissolution et la compassion |
| ♓ Pisces | → Aries | De la dissolution → la renaissance guerrière |

### Exemple concret

**Sun natal Scorpio 21°53'** (né 14.11.1994) :
- Scorpio fait 30° → il reste ~8° avant Sagittarius
- Sun progressé avance ~1°/an → **changement vers Sagittarius à ~8 ans** (très tôt !)
- Mais attention : le degré exact dépend de la vitesse réelle du Sun ce jour-là

**Ce que ça signifie** :
- **Avant le changement** : Identité Scorpio pure → intensité, contrôle, secrets, profondeur
- **Après passage en Sagittarius** : L'identité COMMENCE à vouloir de l'expansion, de la liberté, du voyage, de la philosophie
- **C'est un SHIFT progressif**, pas un switch brutal. Tu gardes ton Sun natal Scorpio (toujours ta base), mais la COUCHE SUPÉRIEURE change
- C'est comme si tu mettais une nouvelle veste par-dessus ton armure Scorpio

### ⚡ Dates critiques du Sun progressé

**Sun progressé entre dans un nouveau signe** :
- **Intensité** : 9/10
- **Durée de l'effet** : Se ressent ~1-2 ans avant et après le changement exact
- **Manifestation** : Changement profond de valeurs, de priorités, de ce qui te fait vibrer
- **Conseil** : ACCUEILLE le changement, résister = dépression

**Sun progressé conjoint une planète natale** :
- **Intensité** : 8/10
- **Durée** : Actif quand l'orbe est ≤1°, soit ~1-2 ans
- **Effet** : ACTIVATION MAJEURE de l'énergie de cette planète

| Sun progressé conjoint... | Effet |
|--------------------------|-------|
| Moon natale | Alignement ego/émotions, période de CLARTÉ intérieure |
| Mercury natal | Éveil intellectuel, nouvelles idées, écriture, communication transformée |
| Venus natale | Éveil amoureux, nouvelles valeurs, rencontre significative possible |
| Mars natal | Explosion d'énergie, nouveau projet de vie, action décisive |
| Jupiter natal | Expansion, optimisme, opportunité majeure, voyage transformateur |
| Saturn natal | Test de maturité, responsabilités, structure de vie redéfinie |
| Uranus natal | Révolution personnelle soudaine, besoin de liberté radical |
| Neptune natal | Quête spirituelle intense, confusion possible, dissolution d'illusions |
| Pluto natal | Transformation TOTALE, mort/renaissance symbolique, pouvoir |
| ASC natal | Nouveau chapitre de vie visible par tous |
| MC natal | CARRIÈRE transformée, succès ou réorientation majeure |

---

## 🌙 LUNE PROGRESSÉE - Le Cycle Émotionnel Maître

**Vitesse** : Avance d'environ **1° par mois** (~12-13° par an)
**Change de signe** : Tous les **~2.5 ans**
**Cycle complet** : **~27-28 ans** (retour au point natal)

### Pourquoi c'est LE PLUS IMPORTANT des progressions

La Moon progressée est le **métronome émotionnel de ta vie**. Chaque changement de signe = nouveau CHAPITRE émotionnel. C'est comme si ton "filtre émotionnel" changeait tous les 2.5 ans.

**Tu te demandes pourquoi tu te sens DIFFÉRENT(E) ces derniers temps ?** Regarde où est ta Moon progressée. C'est probablement la réponse.

### Cycle de la Moon progressée par signe

| Moon progressée en... | Climat émotionnel | Durée |
|-----------------------|-------------------|-------|
| ♈ **Aries** | Impatience, besoin d'action, émotions brutes, indépendance émotionnelle forcée | ~2.5 ans |
| ♉ **Taurus** | Besoin de stabilité, sensualité, confort, attachement aux plaisirs simples | ~2.5 ans |
| ♊ **Gemini** | Curiosité émotionnelle, papillonnage, besoin de stimulation mentale, superficialité émotionnelle | ~2.5 ans |
| ♋ **Cancer** | Hypersensibilité, besoin de famille/cocon, nostalgie, émotions amplifiées x10 | ~2.5 ans |
| ♌ **Leo** | Besoin de reconnaissance émotionnelle, drama, générosité, fierté | ~2.5 ans |
| ♍ **Virgo** | Analyse des émotions, critique de soi, besoin d'ordre émotionnel, anxiété possible | ~2.5 ans |
| ♎ **Libra** | Besoin de relation, diplomatie émotionnelle, co-dépendance possible, recherche d'harmonie | ~2.5 ans |
| ♏ **Scorpio** | Intensité émotionnelle MAXIMALE, obsessions, purges émotionnelles, transformation intérieure | ~2.5 ans |
| ♐ **Sagittarius** | Optimisme émotionnel, besoin de liberté/voyage, enthousiasme, fuite émotionnelle possible | ~2.5 ans |
| ♑ **Capricorn** | Froideur apparente, maturité émotionnelle, dépression possible, construction intérieure | ~2.5 ans |
| ♒ **Aquarius** | Détachement émotionnel, besoin de liberté, intellectualisation des émotions | ~2.5 ans |
| ♓ **Pisces** | Dissolution des frontières émotionnelles, spiritualité, compassion, vulnérabilité maximale | ~2.5 ans |

### 🔥 Moon progressée conjoint planète natale = ÉVÉNEMENT ÉMOTIONNEL

| Moon progressée conjoint... | Événement | Durée |
|----------------------------|-----------|-------|
| Sun natal | Alignement cœur/âme, clarté sur l'identité, **nouvelle lune intérieure** | ~2 mois |
| Venus natale | Rencontre amoureuse, moment de beauté/plaisir, nouvelle valeur émotionnelle | ~2 mois |
| Mars natal | Explosion émotionnelle, conflit puis libération, passion soudaine | ~2 mois |
| Jupiter natal | Joie profonde, expansion émotionnelle, voyage émotionnel | ~2 mois |
| Saturn natal | Tristesse, maturité émotionnelle forcée, deuil possible, construction | ~2 mois |
| Uranus natal | Choc émotionnel, libération soudaine, besoin de changement radical | ~2 mois |
| Neptune natal | Confusion émotionnelle, dissolution, rêves éveillés, connexion spirituelle | ~2 mois |
| Pluto natal | Purge émotionnelle INTENSE, crise puis renaissance, confrontation avec l'ombre | ~2 mois |
| North Node natal | Sentiment de destinée, événement karmique, alignement avec la mission de vie | ~2 mois |

### Moon progressée : phases clés du cycle de 27-28 ans

**Comme le cycle lunaire mensuel, mais sur ~28 ANS** :

| Phase | Quand | Signification |
|-------|-------|---------------|
| 🌑 **Nouvelle Lune progressée** | Moon prog conj Sun prog | **RESET TOTAL** - Nouveau cycle émotionnel de 28 ans commence. Introspection profonde, graines plantées |
| 🌓 **Premier quartier** | Moon prog square Sun prog (~7 ans après NL) | **CRISE D'ACTION** - Les graines rencontrent des obstacles, il faut AGIR ou mourir |
| 🌕 **Pleine Lune progressée** | Moon prog opp Sun prog (~14 ans après NL) | **CULMINATION** - Ce qui a été planté à la NL porte ses fruits. Révélation. Émotions au MAX |
| 🌗 **Dernier quartier** | Moon prog square Sun prog (~21 ans après NL) | **CRISE DE CONSCIENCE** - Lâcher-prise, élimination, préparation au nouveau cycle |

**⚠️ La Nouvelle Lune progressée est un des événements les PLUS IMPORTANTS en astrologie prédictive.** Si tu en vis une → prépare-toi à un RESET émotionnel complet. C'est pas agréable sur le moment, mais c'est NÉCESSAIRE.

---

## ☿♀♂ AUTRES PLANÈTES PROGRESSÉES

### Mercury progressé

**Vitesse** : Variable (peut être quasi-stationnaire si proche d'une rétrogradation)
**Change de signe** : Rare mais significatif

**Mercury progressé change de signe** :
- Nouvelle façon de PENSER
- Style de communication transformé
- Intérêts intellectuels qui évoluent
- **Intensité** : 5/10

### Venus progressée

**Vitesse** : Variable (environ 1.2°/an max)
**Change de signe** : Rare (1x tous les ~25-30 ans parfois)

**Venus progressée change de signe** :
- **Nouvelle façon d'AIMER**
- Ce qui te plaît change profondément
- Valeurs esthétiques transformées
- Style relationnel différent
- **Intensité** : 7/10

### Mars progressé

**Vitesse** : QUASI IMMOBILE (~0.5°/an)
**Change de signe** : EXTRÊMEMENT RARE (peut ne jamais arriver dans une vie)

**Si Mars progressé change de signe** :
- **Révolution dans ta façon d'AGIR**
- Nouvelle énergie, nouveau mode d'action
- **Intensité** : 8/10 (justement parce que c'est rare)

---

## 🔄 CHANGEMENTS DE DIRECTION (Rétrograde ↔ Direct)

**C'est le truc que tout le monde oublie et c'est MASSIF.**

Quand une planète progressée change de direction (passe de rétrograde à directe ou inversement), c'est un **SHIFT ÉNERGÉTIQUE COLOSSAL**. La planète est STATIONNAIRE pendant des années en progressions (elle bouge à peine), ce qui concentre toute l'énergie.

### Venus progressée passe Directe (si rétrograde natale)

**LIBÉRATION AMOUREUSE** 🔓

- Si tu es né(e) avec Venus rétrograde (amour compliqué, self-worth issues, relations karmiques)
- Et que Venus progressée passe directe → **C'EST LA LIBÉRATION**
- Tu commences ENFIN à comprendre l'amour, à t'aimer toi-même
- Les relations deviennent plus faciles, plus fluides
- Le self-worth se débloque
- **Intensité** : 9/10
- **Durée de l'effet** : Se ressent ~2-3 ans avant/après (la planète est quasi-stationnaire)

**Exemple** : Né(e) avec Venus R à 15° Scorpio → Venus progressée ralentit, s'arrête, puis repart en direct vers ~20-25 ans. TOUTE la dynamique amoureuse change.

### Venus progressée passe Rétrograde (si directe natale)

**INTÉRIORISATION AMOUREUSE** 🔒

- Période de questionnement profond sur l'amour et les valeurs
- Ex reviennent (thématiquement, pas forcément physiquement)
- Remise en question de ce qu'on valorise VRAIMENT
- **Intensité** : 7/10

### Mercury progressé passe Rétrograde

**INTÉRIORISATION MENTALE** 🧠

- La pensée se tourne vers l'intérieur
- Moins de besoin de communiquer, plus de réflexion profonde
- Peut correspondre à une période d'écriture, de recherche intérieure
- Communication qui devient plus mesurée
- **Intensité** : 6/10

### Mercury progressé passe Direct (si rétrograde natal)

**LIBÉRATION DE LA PAROLE** 🗣️

- Si né(e) avec Mercury rétrograde (pensée décalée, communication compliquée)
- La parole se DÉBLOQUE
- Nouvelles facilités d'expression
- Idées qui trouvent enfin leur forme
- **Intensité** : 7/10

### Mars progressé passe Direct (si rétrograde natal)

**EXPLOSION D'ÉNERGIE** 💥

- Si né(e) avec Mars rétrograde (action bloquée, colère refoulée, frustration chronique)
- L'énergie se DÉBLOQUE d'un coup
- Capacité d'action retrouvée
- Affirmation de soi qui s'affirme enfin
- **Intensité** : 9/10 (parce que Mars rétro natal c'est une PRISON d'énergie)

### Mars progressé passe Rétrograde (si direct natal)

**BLOCAGE D'ACTION** 🚫

- L'énergie se retourne vers l'intérieur
- Frustration, colère rentrée
- Période de passivité forcée
- **Intensité** : 7/10

---

## 📊 ASPECTS PROGRESSÉS

### Hiérarchie d'importance

1. **Sun progressé aspect planète natale** = LE PLUS IMPORTANT (durée ~2 ans)
2. **Moon progressée aspect planète natale** = Événement émotionnel (durée ~2 mois)
3. **Planète progressée aspect planète natale** = Évolution lente (durée variable)
4. **Aspects entre planètes progressées** = Très lent, fond de scène

### Orbes pour aspects progressés

| Aspect | Orbe recommandé |
|--------|----------------|
| Conjonction (0°) | ±1° |
| Opposition (180°) | ±1° |
| Carré (90°) | ±1° |
| Trigone (120°) | ±1° |
| Sextile (60°) | ±1° |

**Pourquoi des orbes si serrées ?** Parce que les progressions bougent LENTEMENT. 1° = ~1 an pour le Sun. Donc ±1° = l'aspect est actif pendant ~2 ans. C'est déjà beaucoup.

---

# PARTIE 2 : PROFECTIONS ANNUELLES 🏛️

## 📐 Principe fondamental

**Technique traditionnelle vieille de 2000 ans. Simple. Brutale. Efficace.**

Chaque année de vie, à partir de ton anniversaire, une **MAISON SPÉCIFIQUE** est activée. Cycle de 12 ans. La planète qui **GOUVERNE** le signe sur la cuspide de cette maison devient le **TIME LORD** (Maître du Temps) de l'année.

**Tout transit qui touche le Time Lord = ÉVÉNEMENT AMPLIFIÉ.**

C'est comme si le Time Lord portait un mégaphone pendant toute l'année. Tout ce qui lui arrive résonne x10.

---

## 🔄 Cycle des profections

| Âge | Maison | Thème de l'année |
|-----|--------|-----------------|
| 0, 12, 24, 36, 48, 60, 72 | **H1** | 🔥 Identité, corps, nouveau cycle personnel, renouveau |
| 1, 13, 25, 37, 49, 61, 73 | **H2** | 💰 Argent, valeurs, possessions, self-worth |
| 2, 14, 26, 38, 50, 62, 74 | **H3** | 🗣️ Communication, fratrie, apprentissage, courts voyages |
| 3, 15, 27, 39, 51, 63, 75 | **H4** | 🏠 Famille, foyer, racines, vie privée, héritage familial |
| 4, 16, 28, 40, 52, 64, 76 | **H5** | 🎨 Créativité, romance, enfants, plaisir, jeux, spéculation |
| 5, 17, 29, 41, 53, 65, 77 | **H6** | 🏥 Santé, travail quotidien, routine, service, animaux |
| 6, 18, 30, 42, 54, 66, 78 | **H7** | 💍 Relations, mariage, partenariats, contrats, ennemis ouverts |
| 7, 19, 31, 43, 55, 67, 79 | **H8** | 💀 Transformation, mort/renaissance, sexe, crises, héritage, dettes |
| 8, 20, 32, 44, 56, 68, 80 | **H9** | ✈️ Voyages lointains, spiritualité, études supérieures, philosophie |
| 9, 21, 33, 45, 57, 69, 81 | **H10** | 👑 Carrière, réputation, ambition, statut social, reconnaissance |
| 10, 22, 34, 46, 58, 70, 82 | **H11** | 👥 Amis, espoirs, projets collectifs, communauté, réseaux |
| 11, 23, 35, 47, 59, 71, 83 | **H12** | 🌊 Solitude, spiritualité profonde, inconscient, auto-sabotage, secrets, isolation |

---

## 🎯 Comment utiliser les profections CONCRÈTEMENT

### Étape 1 : Calcule l'âge et la maison

```
Âge modulo 12 = numéro de la maison (avec H1 = reste 0)

Ex: 30 ans → 30 ÷ 12 = 2 reste 6 → H7 (Relations)
Ex: 25 ans → 25 ÷ 12 = 2 reste 1 → H2 (Argent/Valeurs)
Ex: 33 ans → 33 ÷ 12 = 2 reste 9 → H10 (Carrière)
```

### Étape 2 : Identifie le signe sur la cuspide de cette maison

```bash
# D'abord, récupère le thème natal avec les cuspides des maisons
python3 scripts/ephemeris.py natal --date 14.11.1994 --time 13:04 --lat 43.71 --lon 7.26 --tz 1
```

Le script te donne les cuspides des 12 maisons. Note le signe de la maison activée.

### Étape 3 : Identifie le Time Lord

**Le Time Lord = la planète qui GOUVERNE le signe sur la cuspide**

| Signe sur la cuspide | Time Lord (Maître) |
|----------------------|-------------------|
| ♈ Aries | ♂ **Mars** |
| ♉ Taurus | ♀ **Venus** |
| ♊ Gemini | ☿ **Mercury** |
| ♋ Cancer | 🌙 **Moon** |
| ♌ Leo | ☀️ **Sun** |
| ♍ Virgo | ☿ **Mercury** |
| ♎ Libra | ♀ **Venus** |
| ♏ Scorpio | ♂ **Mars** (trad) / ♇ **Pluto** (moderne) |
| ♐ Sagittarius | ♃ **Jupiter** |
| ♑ Capricorn | ♄ **Saturn** |
| ♒ Aquarius | ♄ **Saturn** (trad) / ♅ **Uranus** (moderne) |
| ♓ Pisces | ♃ **Jupiter** (trad) / ♆ **Neptune** (moderne) |

**🔥 CONSEIL** : Utilise les maîtrises TRADITIONNELLES pour les profections. La technique est traditionnelle, les résultats sont meilleurs avec les maîtres traditionnels. Mais note aussi le maître moderne pour nuance.

### Étape 4 : Surveille TOUT transit au Time Lord

**Tout transit majeur (conjonction, carré, opposition, trigone) d'une planète lente au Time Lord = ÉVÉNEMENT DE L'ANNÉE.**

```
Ex: Année H7 (relations), Time Lord = Venus
→ Jupiter transite Venus natale = RENCONTRE SIGNIFICATIVE
→ Saturn transite Venus natale = TEST DE COUPLE MAJEUR
→ Uranus transite Venus natale = COUP DE FOUDRE ou RUPTURE SOUDAINE
```

### Étape 5 : Regarde aussi les transits à la maison activée

Toute planète qui transite la maison de la profection annuelle = **amplification du thème de l'année**.

---

## ⚡ ANNÉES CRITIQUES (Les années qui changent ta vie)

### 🔥 Années H1 : 0, 12, 24, 36, 48, 60

**RENOUVEAU PERSONNEL COMPLET**

- Retour au point de départ du cycle de 12 ans
- Coïncide avec le **cycle de Jupiter** (~12 ans) = même fréquence !
- À 12 ans : adolescence, découverte de soi
- À 24 ans : Jupiter Return = expansion + nouveau cycle personnel
- À 36 ans : 3e cycle Jupiter = maturité + renouveau
- À 48 ans : 4e cycle Jupiter = crise de sens + nouveau départ
- À 60 ans : 5e cycle Jupiter = sagesse + libération

**Intensité** : 8/10 (surtout si Jupiter transite le Time Lord en même temps)

### 💀 L'année des 29-30 ans : H6 + SATURN RETURN = DOUBLE CRISE

**LA COMBINAISON LA PLUS REDOUTÉE**

- 29 ans = Profection H6 = **Santé, travail quotidien, routine**
- 29-30 ans = **SATURN RETURN** (Saturn revient à sa position natale)
- **RÉSULTAT** : Double crise → le travail/la santé/la routine sont testés EN MÊME TEMPS que tout le reste de ta vie

**Ce qui arrive typiquement** :
- Burnout / problèmes de santé (H6)
- Remise en question professionnelle totale (Saturn Return)
- Le corps dit STOP si tu vis mal (H6)
- Tu réalises que ta routine te tue (H6 + Saturn)

**Intensité** : 10/10 (putain de combo)

### 🌪️ L'année des 42 ans : H7 + URANUS OPPOSITION = MIDLIFE CRISIS RELATIONNELLE

**LA CRISE DE LA QUARANTAINE VERSION COSMIQUE**

- 42 ans = Profection H7 = **Relations, mariage, partenariats**
- 42 ans ≈ **Uranus opposition Uranus natal** (crise de liberté)
- **RÉSULTAT** : Les relations sont au centre + besoin URGENT de liberté

**Ce qui arrive typiquement** :
- "Je veux TOUT changer dans ma vie amoureuse" (H7 + Uranus)
- Divorce / affaire extraconjugale (Uranus = rupture soudaine)
- Ou au contraire : rencontre qui LIBÈRE d'un schéma (Uranus positif)
- Remise en question des partenariats business aussi

**Intensité** : 9/10

### 🔮 Autres années remarquables

| Âge | Profection | Coïncidence | Effet |
|-----|-----------|-------------|-------|
| 21 | H10 (carrière) | Uranus carré Uranus | Crise de vocation, besoin d'indépendance professionnelle |
| 27 | H4 (famille) | Progression Moon return (~27-28 ans) | Retour aux racines, questionnement familial profond |
| 33 | H10 (carrière) | - | Deuxième grande poussée de carrière |
| 36 | H1 (identité) | 3e Jupiter Return | RENOUVEAU MAJEUR, nouvelle phase de vie |
| 44 | H9 (spiritualité) | - | Quête de sens, voyage initiatique possible |
| 47 | H12 (inconscient) | - | Confrontation avec l'ombre, retraite spirituelle |
| 58-59 | H11 (amis/espoirs) | 2e Saturn Return | Restructuration des amitiés, nouveaux projets collectifs |

---

## 🔗 COMBINER PROFECTIONS + TRANSITS = LA VRAIE PUISSANCE

**C'est ICI que la magie opère. Les profections seules = utiles. Combinées avec les transits = PRÉDICTION LASER.**

### Méthode de combinaison

1. **Identifie la maison de l'année** (profection)
2. **Identifie le Time Lord** (maître de la maison activée)
3. **Regarde les transits au Time Lord** cette année-là
4. **Regarde les transits à la maison activée** cette année-là
5. **Le transit le plus puissant au Time Lord = L'ÉVÉNEMENT PRINCIPAL de l'année**

### Exemples concrets de combinaison

**Exemple 1 : Année H7 (relations) + Jupiter transite le Time Lord**

```
Profection : H7 (relations, partenariats)
Signe sur cuspide H7 : Leo
Time Lord : Sun (maître de Leo)
Transit : Jupiter conjoint Sun natal en mars

→ PRÉDICTION : Rencontre significative / engagement / mariage en mars
→ Intensité : 9/10
→ Fiabilité : TRÈS HAUTE (profection + transit concordent)
```

**Exemple 2 : Année H10 (carrière) + Saturn transite le Time Lord**

```
Profection : H10 (carrière, ambition)
Signe sur cuspide H10 : Sagittarius
Time Lord : Jupiter (maître de Sagittarius)
Transit : Saturn carré Jupiter natal en septembre

→ PRÉDICTION : Test professionnel majeur / obstacle à l'expansion / restructuration
→ Intensité : 8/10
→ Conseil : Patience, construire lentement, pas de risques inconsidérés en septembre
```

**Exemple 3 : Année H8 (transformation) + Pluto transite le Time Lord**

```
Profection : H8 (mort/renaissance, crises, transformation)
Signe sur cuspide H8 : Virgo
Time Lord : Mercury (maître de Virgo)
Transit : Pluto carré Mercury natal

→ PRÉDICTION : Crise mentale profonde / transformation de la pensée / mort d'une façon de voir le monde
→ Intensité : 10/10
→ ⚠️ ATTENTION : Combinaison H8 + Pluto = TRANSFORMATION RADICALE inévitable
```

**Exemple 4 : Année H5 (romance) + Venus transite la H5**

```
Profection : H5 (créativité, romance, enfants)
Transit : Venus entre en H5 natale en avril

→ PRÉDICTION : Début d'idylle / projet créatif / grossesse possible si contexte
→ Intensité : 6/10 (transit rapide mais amplifié par la profection)
```

---

# PARTIE 3 : DIRECTIONS D'ARC SOLAIRE ☀️➡️

## 📐 Principe fondamental

**Toutes les planètes avancent au même rythme que le Soleil progressé (~1° par an).**

C'est comme si TOUT le thème natal avançait d'1° par an. Chaque planète, chaque angle. Même vitesse.

**La différence avec les progressions secondaires** :
- Progressions → chaque planète bouge à sa propre vitesse (Moon vite, Mars quasi-immobile)
- Arcs solaires → TOUT bouge à ~1°/an (uniformément)

### Pourquoi utiliser les arcs solaires ?

**Les arcs solaires sont PLUS PUISSANTS que les progressions pour les ÉVÉNEMENTS EXTERNES.**

- Progressions = évolution INTERNE (comment tu te sens, ce que tu deviens)
- Arcs solaires = événements EXTERNES (ce qui t'ARRIVE concrètement)
- Transits = la météo extérieure
- Arcs solaires = le pont entre l'intérieur et l'extérieur

---

## 📊 Comment calculer

```
Position arc solaire = Position natale + (âge × ~1°)

Plus précisément :
Arc solaire = Différence entre Sun progressé et Sun natal
→ Ajouter cette différence à TOUTES les positions natales
```

**Exemple** :
```
Sun natal : 21°53' Scorpio
Sun progressé à 30 ans : ~22° Sagittarius (avancé de ~30°)
Arc solaire = 30° (environ)

Mars natal : 15° Leo
Mars arc solaire à 30 ans = 15° Leo + 30° = 15° Virgo

MC natal : 3° Sagittarius
MC arc solaire à 30 ans = 3° Sagittarius + 30° = 3° Capricorn
```

```bash
# Pour calculer les positions d'arc solaire :
# 1. Calcule le Sun progressé pour l'âge voulu
python3 scripts/ephemeris.py natal --date 14.12.1994 --time 13:04 --lat 43.71 --lon 7.26 --tz 1

# 2. Calcule la différence Sun progressé - Sun natal = arc
# 3. Ajoute cet arc à TOUTES les positions natales
# (calcul manuel nécessaire pour l'instant)
```

---

## ⚡ Quand un arc solaire touche un point natal = ÉVÉNEMENT

**Orbe : ±1° MAXIMUM (soit une fenêtre de ~2 ans)**

**C'est THE règle des arcs solaires.** Quand une planète en arc solaire arrive à ±1° d'un point natal (par conjonction, carré, ou opposition) = ÉVÉNEMENT dans la vie.

### Aspects d'arc solaire les plus puissants

| Arc solaire | Touche point natal | Événement |
|-------------|-------------------|-----------|
| ☀️ Sun arc | conj MC natal | **SUCCÈS PROFESSIONNEL MAJEUR**, reconnaissance publique |
| ☀️ Sun arc | conj ASC natal | **NOUVEAU CHAPITRE DE VIE** visible, changement d'image |
| ☀️ Sun arc | conj Venus natale | **RENCONTRE AMOUREUSE SIGNIFICATIVE** ou engagement |
| ☀️ Sun arc | conj Jupiter natal | **EXPANSION**, opportunité majeure, chance |
| ☀️ Sun arc | conj Saturn natal | **TEST DE VIE**, responsabilités, maturité forcée |
| MC arc | conj Sun natal | **Carrière atteint un SOMMET** |
| MC arc | conj Jupiter natal | **PROMOTION / SUCCÈS PRO** retentissant |
| MC arc | conj Saturn natal | **Restructuration de carrière**, test professionnel |
| Venus arc | conj ASC natal | **MARIAGE** possible, embellissement de la vie |
| Venus arc | conj MC natal | **Succès par charme**, relations pros facilitées |
| Mars arc | conj MC natal | **ACTION PROFESSIONNELLE** décisive, conflit pro possible |
| Mars arc | conj ASC natal | **Énergie nouvelle**, accident possible si mal aspecté |
| Saturn arc | conj Sun natal | **ÉPREUVE D'IDENTITÉ**, dépression possible, maturité |
| Saturn arc | conj Moon natale | **Restriction émotionnelle**, deuil possible |
| Saturn arc | conj MC natal | **Chute ou construction** professionnelle (selon le thème) |
| Uranus arc | conj Sun natal | **RÉVOLUTION SOUDAINE**, changement radical |
| Uranus arc | conj ASC natal | **CHOC DE VIE** → nouvelle identité |
| Pluto arc | conj Sun natal | **TRANSFORMATION TOTALE**, mort/renaissance |
| Pluto arc | conj MC natal | **Pouvoir professionnel** ou destruction de carrière |

### Arcs solaires par carré et opposition

**Carré (90°) d'arc solaire** :
- Crise, friction, obstacle qui FORCE l'action
- Moins puissant que la conjonction mais très significatif
- **Intensité** : 7/10

**Opposition (180°) d'arc solaire** :
- Confrontation avec l'extérieur, quelque chose/quelqu'un te confronte
- Prise de conscience par le miroir
- **Intensité** : 7/10

---

## 🔥 Exemples concrets d'arcs solaires

### Exemple 1 : MC arc solaire conjoint Sun natal = Succès pro

```
Thème natal : Sun 21° Scorpio, MC 3° Sagittarius
MC doit avancer de : 21° Scorpio - 3° Sagittarius = impossible en conjonction directe
MAIS : MC arc avance d'1°/an
MC arc conjoint Venus natale en Scorpio 3° → quand ? MC natal 3° Sag + X° = Venus
(calcul spécifique au thème)

Résultat : L'année où ça arrive = ÉVÉNEMENT CONCRET dans la carrière/relations
```

### Exemple 2 : Venus arc solaire conjoint ASC natal

```
Venus natale : 12° Scorpio
ASC natal : 11° Aquarius
Distance : ~89° (quasi-carré !)

Venus arc à l'âge 1 = 13° Scorpio (carré ASC = carré arc solaire à ~1 an)
→ C'est un aspect natal ACTIVÉ très tôt
→ Mais Venus arc conj ASC = Venus doit parcourir ~89° = ~89 ans (trop vieux)
→ MAIS Venus arc CARRÉ ASC = activé dès la naissance (aspect natal)

NOTE : Les arcs solaires les plus intéressants sont ceux qui activent
des aspects qui N'EXISTENT PAS dans le natal (nouvelles connexions)
```

---

# PARTIE 4 : COMBINER LES TROIS TECHNIQUES 🎯

## La méthode ULTIME de prédiction

**Quand progressions + profections + arcs solaires convergent sur le même thème = ÉVÉNEMENT GARANTI.**

### Protocole d'analyse combinée

```
ÉTAPE 1 : Profections → Identifie la maison et le Time Lord de l'année
ÉTAPE 2 : Progressions → Où est le Sun progressé ? Où est la Moon progressée ?
ÉTAPE 3 : Arcs solaires → Y a-t-il un arc exact (±1°) cette année ?
ÉTAPE 4 : Transits → Les transits confirment-ils le thème ?
ÉTAPE 5 : Synthèse → TOUT pointe dans la même direction ?
```

### Niveaux de fiabilité

| Techniques qui concordent | Fiabilité |
|--------------------------|-----------|
| 1 seule technique | 40% → Tendance, pas certitude |
| 2 techniques concordent | 70% → Fort probable |
| 3 techniques concordent | 90% → Quasi certain |
| 4 techniques concordent | 95%+ → **ÉVÉNEMENT GARANTI** |

### Exemple complet de combinaison

```
SUJET : Femme née 14.11.1994, 13h04, Nice
QUESTION : Que se passe-t-il à 31 ans (novembre 2025 - novembre 2026) ?

ÉTAPE 1 - PROFECTION :
→ 31 ans = H8 (transformation, crises, sexe, héritage)
→ Cuspide H8 = ? (dépend du thème exact)
→ Time Lord = ? (dépend du signe sur H8)
→ THÈME DE L'ANNÉE : Transformation profonde, mort/renaissance

ÉTAPE 2 - PROGRESSIONS :
→ Sun progressé = ~22° Sagittarius (expansion, voyage, philosophie)
→ Moon progressée = ? (calculer position exacte)
→ Y a-t-il un changement de signe ou aspect exact ? → Vérifier

ÉTAPE 3 - ARCS SOLAIRES :
→ Arc = ~31° (Sun natal 21° Scorpio → Sun prog ~22° Sagittarius)
→ MC arc = MC natal + 31° = ?
→ Venus arc = Venus natale + 31° = ?
→ Y a-t-il un contact ±1° avec un point natal ? → Vérifier

ÉTAPE 4 - TRANSITS :
→ Saturn-Neptune conjonction 0° Aries (fév 2026) → près de Moon natale Aries ?
→ Éclipses 2026 → touchent-elles des points nataux ?
→ Jupiter → où transite-t-il par rapport au Time Lord ?

ÉTAPE 5 - SYNTHÈSE :
→ Si H8 (profection) + Moon progressée en Scorpio (progressions) + Pluto arc conj Sun
  (arc) + Saturn-Neptune touche Moon natale (transit)
  = TRANSFORMATION MAJEURE GARANTIE
→ 4 techniques concordent = 95%+ de fiabilité
```

---

# PARTIE 5 : FORMAT DE RAPPORT 📋

## Template de rapport Progressions + Profections

```markdown
# 🔄 PROGRESSIONS, PROFECTIONS & ARCS SOLAIRES - [NOM] [PÉRIODE]

## 🎯 RÉSUMÉ EXÉCUTIF

**Période analysée** : [anniversaire N → anniversaire N+1]
**Âge** : [X] ans
**Profection annuelle** : Maison [X] - [Thème]
**Time Lord** : [Planète] en [Signe] [Maison]

**Les 3 événements progressés les plus importants** :
1. [Sun/Moon/planète progressé(e)] [aspect] [point natal] → [signification]
2. [...]
3. [...]

**Arc solaire exact cette année** : [Oui/Non - si oui, lequel]

---

## 🌀 PROGRESSIONS SECONDAIRES

### ☀️ Sun progressé
**Position actuelle** : [Degré] [Signe]
**Changement de signe récent ou à venir** : [Oui/Non - quand]
**Aspect exact en cours** : [Si applicable]
**Signification** : [Interprétation brutale]

### 🌙 Moon progressée
**Position actuelle** : [Degré] [Signe]
**Signe actuel depuis** : [Date approximative]
**Prochain changement de signe** : [Date approximative]
**Phase du cycle lunaire progressé** : [Nouvelle Lune / Croissante / Pleine / Décroissante]
**Signification** : [Interprétation du climat émotionnel]

### Changements de direction
**Venus progressée** : [Directe/Rétrograde - changement prévu ?]
**Mercury progressé** : [Directe/Rétrograde - changement prévu ?]
**Mars progressé** : [Directe/Rétrograde - changement prévu ?]

### Aspects progressés actifs (±1° d'orbe)
| Planète progressée | Aspect | Point natal | Exactitude | Signification |
|-------------------|--------|-------------|------------|---------------|
| [Sun prog] | [conj/carré/etc] | [planète/angle] | [mois/année exact] | [interprétation] |
| [Moon prog] | [conj/carré/etc] | [planète/angle] | [mois/année exact] | [interprétation] |

---

## 🏛️ PROFECTIONS ANNUELLES

### Maison de l'année : H[X] - [THÈME]
**Signe sur la cuspide** : [Signe]
**Time Lord** : [Planète]
**Position natale du Time Lord** : [Degré] [Signe] [Maison]
**État du Time Lord** : [Direct/Rétrograde, bien/mal aspecté]

### Ce que ça signifie concrètement
[Interprétation brutale du thème de l'année]

### Transits au Time Lord cette année
| Date | Transit | Aspect au Time Lord | Effet |
|------|---------|--------------------|-------|
| [date] | [planète] | [conj/carré/etc] | [événement prédit] |

### Planètes natales dans la maison activée
[Si des planètes natales sont en H[X], elles sont DOUBLEMENT ACTIVÉES]

---

## ☀️➡️ DIRECTIONS D'ARC SOLAIRE

### Arc solaire de l'année : ~[X]°
### Contacts exacts (±1°)

| Planète/angle arc | Contact natal | Aspect | Date exacte | Événement |
|------------------|---------------|--------|-------------|-----------|
| [MC arc] | [planète natale] | [conj] | [mois/année] | [événement] |

---

## 🔗 SYNTHÈSE COMBINÉE

### Convergence des techniques

**Profection** : H[X] → [thème]
**Moon progressée** : en [signe] → [climat émotionnel]
**Sun progressé** : en [signe] → [évolution identitaire]
**Arc solaire actif** : [oui/non → quel contact]
**Transit majeur au Time Lord** : [oui/non → lequel]

### Niveau de convergence : [X]/4 techniques concordent
### Fiabilité de la prédiction : [X]%

### PRÉDICTION PRINCIPALE DE L'ANNÉE :
[Prédiction brutale, concrète, avec timing si possible]

### ÉVÉNEMENTS PROBABLES PAR MOIS :
| Mois | Événement probable | Techniques en jeu | Intensité |
|------|-------------------|-------------------|-----------|
| [mois] | [événement] | [profection + transit / etc] | [X/10] |

---

## ⚠️ MISES EN GARDE

1. [Point d'attention basé sur les défis identifiés]
2. [Timing à respecter]
3. [Ce qu'il faut éviter cette année]

## ✨ OPPORTUNITÉS

1. [Opportunité basée sur les aspects positifs]
2. [Fenêtre de timing favorable]
3. [Domaine à exploiter]

---

## 🎯 STRATÉGIE DE L'ANNÉE

**Phase 1** : [Mois X - Mois Y] → [Focus]
**Phase 2** : [Mois Y - Mois Z] → [Focus]
**Phase 3** : [Mois Z - Mois W] → [Focus]
```

---

## ⚠️ Points critiques

1. **TOUJOURS calculer les positions EXACTES** - Ne jamais estimer à la louche. 1° d'erreur = 1 AN de décalage en progressions
2. **L'HEURE DE NAISSANCE est CRITIQUE** - Surtout pour la Moon progressée (elle bouge ~1°/mois). Pas d'heure = pas de Moon progressée fiable
3. **Les profections commencent à L'ANNIVERSAIRE** - Pas au 1er janvier. Année profection = anniversaire N → anniversaire N+1
4. **Le Time Lord en rétrograde natal** = L'année peut être plus intériorisée, avec des retards et des révisions dans le domaine de la maison
5. **Les arcs solaires sont EXACTS** - ±1° max. Si tu élargis l'orbe tu perds la fiabilité
6. **COMBINER les techniques** - Une seule technique = indication. Trois techniques qui concordent = CERTITUDE
7. **Les changements de signe de la Moon progressée** sont des turning points émotionnels → les dater avec précision
8. **Ne confonds pas progressions et transits** - Les progressions = évolution interne LENTE. Les transits = stimuli externes. Les deux se complètent
9. **Les changements de direction progressés (rétro ↔ direct)** sont RARES et donc MASSIFS quand ils arrivent
10. **TOUJOURS remettre dans le contexte du natal** - Un transit au Time Lord est puissant, mais COMMENT il se manifeste dépend du thème natal entier

---

**Retourne au [SKILL.md principal](../SKILL.md) pour workflow complet.**
