# 🗓️ Guide : Astrologie Élective (Electional Astrology)

L'astrologie élective est l'art de choisir le **MEILLEUR MOMENT** pour entreprendre une action. Tu ne subis plus le timing — tu le **PROGRAMMES**.

---

## 🎯 Objectif

Déterminer le créneau temporel OPTIMAL pour lancer une action spécifique : mariage, lancement de business, signature de contrat, chirurgie, déménagement, premier rendez-vous, entretien d'embauche, lancement de produit digital, etc.

**Le but = MAXIMISER les chances de succès en choisissant une fenêtre astrologique favorable.**

---

## 📊 Principe fondamental

**Si tu choisis QUAND agir, tu choisis le thème de l'événement = tu PROGRAMMES le destin de l'action.**

Le principe est simple et brutal :

> Chaque action a un **thème de naissance**. Le moment où tu signes le contrat, où tu dis "oui", où tu cliques sur "publier" — ce moment-là a une carte du ciel. Et cette carte du ciel = le **destin de cette action**.

C'est exactement comme un thème natal, sauf que c'est pour un ÉVÉNEMENT, pas une personne.

**Conséquence directe** :
- Tu te maries un jour avec Venus rétrograde en Scorpio carré Mars → ton mariage DÉMARRE avec cette énergie de tension, de remise en question des valeurs, de conflit passion/engagement
- Tu lances ton business un jour avec Jupiter trigone MC, Lune croissante en Leo → ton business DÉMARRE avec énergie d'expansion, de visibilité, de confiance

**L'élective, c'est le HACK ULTIME de l'astrologie** : au lieu de subir les transits, tu les utilises comme OUTIL.

---

## ⚠️ Disclaimer crucial

L'astrologie élective ne GARANTIT rien. Elle met les probabilités de ton côté. C'est comme choisir de surfer quand la vague est bonne plutôt que quand c'est du flat. Ça ne fait pas de toi un surfeur pro, mais au moins t'as une vague sur laquelle rider.

**Et SURTOUT** : le thème natal de la personne qui agit reste DOMINANT. Un bon timing élective ne sauvera pas un projet de merde. Mais un bon projet avec un bon timing → c'est là que la magie opère.

---

## 🔧 Comment calculer un thème élective

```bash
# Éphémérides du mois pour repérer les fenêtres favorables
python3 scripts/ephemeris.py ephemeris --year YYYY --month MM

# Transits de l'année pour identifier les grandes tendances
python3 scripts/ephemeris.py transits --date DD.MM.YYYY --time HH:MM --lat LAT --lon LON --year YYYY

# Thème natal du moment choisi (pour vérifier la carte du ciel exacte)
python3 scripts/ephemeris.py natal --date DD.MM.YYYY --time HH:MM --lat LAT --lon LON --tz TZ
```

**Workflow** :
1. Identifie le TYPE d'action → détermine les planètes/maisons clés
2. Scanne les éphémérides du mois cible → repère les fenêtres propres
3. Vérifie la checklist universelle (voir plus bas) pour chaque fenêtre candidate
4. Calcule le thème natal du moment choisi → confirme que c'est clean
5. Recommande le créneau avec justification complète

---

## 📋 Règles fondamentales (NON NÉGOCIABLES)

Ces règles s'appliquent à **TOUTE** action élective. Pas d'exception.

### Règle 1 : La Lune N'EST PAS Void of Course ❌🌙

**Qu'est-ce que la Lune VOC ?** La Lune ne forme AUCUN aspect majeur (conjonction, sextile, carré, trigone, opposition) avec une planète avant de quitter son signe actuel.

**Pourquoi c'est mortel ?** Lune VOC = "rien ne se concrétise". Ce que tu lances pendant une Lune VOC a tendance à NE PAS aboutir, à tourner en rond, à être oublié.

**Exceptions (fragiles)** :
- Lune VOC en Cancer, Taurus, Sagittarius, Pisces → peut fonctionner (la Lune y est forte)
- Si tu veux que quelque chose ne mène NULLE PART volontairement (ex: entretien avec les flics, audit fiscal) → Lune VOC = parfait, personne ne va donner suite 😏

**Vérification** : Calcule les aspects de la Lune avant son changement de signe. Si dernier aspect = 10h avant le changement et tu agis 2h avant → tu es en VOC. **PAS BON.**

---

### Règle 2 : Planète maîtresse de l'action PAS rétrograde 🔄

**Principe** : La planète qui GOUVERNE le domaine de ton action ne doit PAS être rétrograde.

| Action | Planète maîtresse | Si rétrograde... |
|--------|-------------------|-----------------|
| Mariage / amour | **Venus** | CATASTROPHE : remise en question des valeurs, ex qui reviennent, engagement fragile |
| Contrats / communication | **Mercury** | Messages perdus, malentendus, clauses foireuses qu'on découvre après |
| Business / lancement | **Jupiter** | Expansion bloquée, surconfiance mal placée, croissance illusoire |
| Chirurgie / action physique | **Mars** | Complications, énergie mal dirigée, hémorragies, rechutes |
| Immobilier / foyer | **Moon** (+ Mercury pour les papiers) | Instabilité émotionnelle liée au lieu, regrets |
| Voyage | **Mercury** (+ Jupiter long courrier) | Retards, bagages perdus, annulations |
| Tech / digital | **Mercury** (+ Uranus) | Bugs, crashes, UX foireuse, adoption lente |

**Mercury rétrograde = le plus fréquent et le plus chiant** (3-4x/an, ~3 semaines). Vérifie TOUJOURS.

---

### Règle 3 : PAS d'éclipse ±3 jours 🌑

**Les éclipses sont des PORTAILS DE DESTIN**. Elles ouvrent et ferment des chapitres. L'énergie est CHAOTIQUE, imprévisible, et les événements lancés sous éclipse peuvent avoir des conséquences que tu n'avais absolument pas anticipées.

**Règle stricte** :
- **±3 jours** d'une éclipse (solaire OU lunaire) = NE LANCE RIEN d'important
- Les éclipses activent l'axe des Nœuds = karma, destinée → tu ne contrôles PAS ce qui se passe
- Un mariage sous éclipse → mariage karmique (peut être intense MAIS imprévisible)
- Un business sous éclipse → trajectoire totalement imprévisible

**Exception** : Si tu es volontairement prêt à ce que l'action prenne une direction INATTENDUE et potentiellement radicale. Mais c'est du poker.

---

### Règle 4 : Favoriser les aspects APPLIQUANTS harmoniques 🔺

**Aspects appliquants** = la planète rapide se RAPPROCHE de l'aspect exact (l'énergie MONTE).
**Aspects séparants** = la planète rapide S'ÉLOIGNE de l'aspect exact (l'énergie RETOMBE).

**TOUJOURS préférer les aspects appliquants** pour un lancement.

| Aspect | Effet en élective |
|--------|-------------------|
| **Trigone appliquant (120°)** | ✅ PARFAIT : harmonie, facilité, succès naturel |
| **Sextile appliquant (60°)** | ✅ BON : opportunités, mais nécessite un effort conscient |
| **Conjonction appliquante** | ⚠️ DÉPEND de la planète : Jupiter/Venus = bien, Saturn/Mars = lourd |
| **Carré appliquant (90°)** | ❌ FRICTION : obstacles, conflits, blocages au lancement |
| **Opposition appliquante (180°)** | ❌ TENSION : polarité, conflit entre deux forces |

**L'idéal** : Lune qui applique un trigone ou sextile à Jupiter ou Venus AVANT de changer de signe. C'est le GOLD STANDARD de l'élective.

---

### Règle 5 : Vérifier la dignité de la planète maîtresse 👑

La planète qui gouverne ton action doit être en BON ÉTAT (dignité).

**Dignités positives (planète FORTE)** :

| Dignité | Signification en élective |
|---------|--------------------------|
| **Domicile** (dans son propre signe) | TOP TIER : la planète est chez elle, pleine puissance |
| **Exaltation** | EXCELLENT : la planète est au sommet de sa forme |
| **Triplicité** | BON : confortable, soutenue par l'élément |

**Dignités négatives (planète FAIBLE)** :

| Dignité | Signification en élective |
|---------|--------------------------|
| **Détriment** (signe opposé au domicile) | DANGEREUX : la planète dysfonctionne |
| **Chute** (signe opposé à l'exaltation) | MAUVAIS : la planète est impuissante |
| **Pérégrine** (aucune dignité) | MÉDIOCRE : sans ressource, résultats aléatoires |

**Rappel des domiciles et exaltations** :

| Planète | Domicile | Exaltation | Détriment | Chute |
|---------|----------|------------|-----------|-------|
| Sun | Leo | Aries | Aquarius | Libra |
| Moon | Cancer | Taurus | Capricorn | Scorpio |
| Mercury | Gemini/Virgo | Virgo | Sagittarius/Pisces | Pisces |
| Venus | Taurus/Libra | Pisces | Scorpio/Aries | Virgo |
| Mars | Aries/Scorpio | Capricorn | Libra/Taurus | Cancer |
| Jupiter | Sagittarius/Pisces | Cancer | Gemini/Virgo | Capricorn |
| Saturn | Capricorn/Aquarius | Libra | Cancer/Leo | Aries |

**Exemple** : Tu veux lancer un business → Jupiter est ta planète clé. Jupiter en Sagittarius ou Pisces (domicile) ou Cancer (exaltation) = FONCE. Jupiter en Gemini ou Virgo (détriment) = attends un meilleur moment si possible.

---

## 📊 Analyse par type d'action

### a) 💍 Mariage / Engagement

**Le mariage est l'action élective la PLUS étudiée historiquement.** Les rois et reines faisaient appel à des astrologues pour choisir la date du mariage. Pas par superstition — par STRATÉGIE.

#### ✅ Favoriser

| Critère | Détail |
|---------|--------|
| **Venus forte** | Venus en Taurus (domicile), Libra (domicile), Pisces (exaltation) → IDÉAL |
| **Venus directe** | Venus PAS rétrograde — **ABSOLUMENT NON NÉGOCIABLE** |
| **Lune favorable** | Lune en Taurus, Cancer, Libra → émotions stables, nourricières, harmonieuses |
| **Lune croissante** | De la Nouvelle Lune au Premier Quartier (énergie de croissance) |
| **H7 propre** | Pas de maléfiques (Mars, Saturn, Pluto) en maison 7 |
| **Maître de H7 bien aspecté** | Le maître du signe sur la cuspide de H7 reçoit des trigones/sextiles |
| **Venus-Jupiter aspect** | Trigone ou sextile entre Venus et Jupiter = abondance en amour |
| **Venus en H7 ou H1** | Venus angulaire = l'amour est au premier plan |
| **Aspects harmoniques Lune-Venus** | Trigone/sextile Lune-Venus = émotions et amour en phase |

#### ❌ Éviter

| Critère | Pourquoi |
|---------|----------|
| **Venus rétrograde** | Tu te maries avec l'énergie de "on remet tout en question". Les ex reviennent. Les valeurs sont instables. **NON.** |
| **Lune en Scorpio** | Émotions intenses, possessivité, jalousie → pas l'énergie de départ qu'on veut |
| **Lune en Capricorn** | Émotions froides, rigides, sentiment de devoir plutôt que d'amour |
| **Lune en Aries** | Impulsivité émotionnelle, égocentrisme → mariage centré sur soi |
| **Mars carré Venus** | Conflit entre désir et amour = friction sexuelle/romantique dès le début |
| **Saturn en H7** | Restriction, lourdeur dans le partenariat. Sensation de prison |
| **Saturn carré Venus** | L'amour sera testé IMMÉDIATEMENT. Commencer par un test = pas idéal |
| **Lune VOC** | Le mariage "ne mène nulle part" → pas de construction commune |
| **Éclipse ±3 jours** | Destinée imprévisible pour l'union |

#### 🏆 Configuration IDÉALE pour un mariage

```
Venus en Taurus ou Libra (domicile) OU Pisces (exaltation)
Venus directe, bien aspectée (trigone Jupiter, sextile Lune)
Lune croissante en Taurus ou Libra
Lune applique trigone à Venus ou Jupiter
H7 vide de maléfiques (pas de Mars/Saturn/Pluto)
Maître de H7 en dignité et bien aspecté
Pas de rétrogrades Mercury/Venus/Mars
Pas d'éclipse ±3 jours
Vendredi (jour de Venus) = bonus symbolique
```

---

### b) 🚀 Lancement de business / projet

**Tu crées le thème natal de ton entreprise.** Chaque entreprise a une date de naissance. Choisis-la comme tu choisirais la meilleure génétique possible pour un enfant (métaphoriquement).

#### ✅ Favoriser

| Critère | Détail |
|---------|--------|
| **Jupiter fort** | Jupiter en Sagittarius, Pisces (domicile), Cancer (exaltation) — expansion naturelle |
| **Jupiter en H10 ou H1** | Succès visible, reconnaissance publique |
| **Lune croissante** | Phase de CROISSANCE — tu veux que le projet GRANDIT, pas qu'il décroisse |
| **MC en signe cardinal** | Aries, Cancer, Libra, Capricorn sur MC = énergie d'INITIATIVE, de leadership |
| **Sun fort et bien aspecté** | Le Sun = la vitalité du projet. Fort = projet qui a de l'énergie |
| **Mercury direct** | Communication, ventes, marketing = tout dépend de Mercury |
| **Aspects Jupiter-MC** | Trigone/sextile/conjonction = EXPANSION professionnelle |
| **H2 propre** | Maison de l'argent sans maléfiques = finances fluides |
| **Venus en H2 ou H10** | Argent qui rentre (H2) ou image de marque forte (H10) |

#### ❌ Éviter

| Critère | Pourquoi |
|---------|----------|
| **Mercury rétrograde** | Communications foireuses, contrats mal rédigés, partenariats bancals au lancement |
| **Saturn en H1** | Le business DÉMARRE avec restriction, lourdeur, obstacles. Comme naître avec du plomb aux pieds |
| **Saturn en H10** | Carrière/réputation bloquée dès le départ. Reconnaissance RETARDÉE |
| **Mars carré MC** | Conflit, agressivité dans la sphère professionnelle. Concurrents agressifs dès le jour 1 |
| **Lune décroissante** | Énergie qui DIMINUE — le contraire de ce que tu veux pour un lancement |
| **Mars rétrograde** | L'action est bloquée. Le projet stagne au lieu d'avancer |
| **Jupiter rétrograde** | L'expansion est INTERNE, pas externe. Mauvais pour la croissance visible |
| **Pluto en H10** | Crises de pouvoir, transformations forcées dans la carrière. Trop intense |

#### 🏆 Configuration IDÉALE pour un lancement business

```
Jupiter en dignité, en H10 ou H1 (ou H2 pour l'argent)
Lune croissante, de préférence en Leo (visibilité) ou Taurus (stabilité)
MC en signe cardinal (Capricorn = ambition, Aries = initiative)
Mercury direct et rapide (en Gemini ou Virgo = bonus)
Sun bien aspecté (trigone Jupiter ou MC)
H1 propre (pas de Saturn/Mars)
H10 propre (pas de Saturn maléfique)
Lundi (Moon = croissance) ou Jeudi (Jupiter = expansion)
```

---

### c) 📝 Signature de contrat

**Un contrat = Mercury.** Mercury EST le contrat : les mots, les clauses, la communication, l'accord. Si Mercury est foireux au moment de la signature, le contrat SERA foireux.

#### ✅ Favoriser

| Critère | Détail |
|---------|--------|
| **Mercury DIRECT** | **C'est le critère #1. ABSOLU. NON NÉGOCIABLE.** |
| **Mercury fort** | Mercury en Gemini ou Virgo (domicile) = contrat solide, bien rédigé, clair |
| **Lune en signe d'air** | Gemini, Libra, Aquarius = énergie intellectuelle, communication, accord rationnel |
| **Aspects Mercury-Jupiter** | Trigone/sextile = contrat AVANTAGEUX, expansion par l'accord |
| **Mercury en H3, H7 ou H10** | H3 = communication, H7 = partenariat, H10 = carrière → selon le type de contrat |
| **H7 propre** | Maison des contrats et partenariats — pas de maléfiques |
| **Lune applique aspect à Mercury** | L'énergie émotionnelle soutient la communication |

#### ❌ Éviter

| Critère | Pourquoi |
|---------|----------|
| **Mercury rétrograde** | **ABSOLUMENT INTERDIT**. Les contrats signés sous Mercury rétro sont CONNUS pour avoir des problèmes : clauses oubliées, malentendus, renégociations, annulations. C'est LE cliché de l'astrologie — et c'est un cliché parce que c'est VRAI. |
| **Lune VOC** | Le contrat ne mène à rien. Stagne. S'oublie dans un tiroir. |
| **Neptune aspects Mercury** | Neptune = illusion, confusion. Neptune carré/opposé Mercury au moment de la signature = tu NE VOIS PAS ce qui est écrit en petit. Arnaques, tromperies, mauvaise compréhension. |
| **Mercury en Pisces** | Mercury est en CHUTE et DÉTRIMENT en Pisces = la pire dignité possible. Pensée floue, communication ambiguë. |
| **Mercury en Sagittarius** | Mercury en détriment = détails négligés, surconfiance, promesses exagérées |
| **Mars carré Mercury** | Disputes, agressivité verbale, conflit dans les négociations |
| **Saturn carré Mercury** | Blocages, retards, clauses restrictives qui t'étouffent |

#### 🏆 Configuration IDÉALE pour une signature de contrat

```
Mercury DIRECT, en Gemini ou Virgo (domicile)
Mercury trigone/sextile Jupiter (contrat avantageux)
Lune en Gemini ou Libra (air = rationalité)
Lune applique trigone/sextile à Mercury
PAS de Neptune en aspect tendu à Mercury
H7 propre (pas de Saturn/Mars/Neptune)
Mercredi (jour de Mercury) = bonus symbolique
```

---

### d) 🏥 Chirurgie / Procédure médicale

**La chirurgie est l'action élective où l'astrologie a la tradition la plus ANCIENNE.** Les médecins médiévaux consultaient les éphémérides avant d'opérer. Ce n'est pas du folklore — c'est du risk management.

#### ✅ Favoriser

| Critère | Détail |
|---------|--------|
| **Lune décroissante** | Pour toute chirurgie de RÉDUCTION (ablation, extraction, réduction de tumeur). L'énergie décroissante aide la réduction |
| **Lune croissante** | UNIQUEMENT pour les chirurgies d'AJOUT (implants, greffes, reconstructions) |
| **Mars bien aspecté** | Mars = chirurgien, scalpel, énergie d'action. Trigone/sextile = intervention propre |
| **Mars DIRECT** | Mars rétrograde = action bloquée, complications chirurgicales |
| **H6 propre** | Maison de la santé — pas de maléfiques lourds |
| **Saturn trigone Mars** | Structure + action = précision chirurgicale |
| **Jupiter en H6 ou H1** | Protection de la santé, récupération facilitée |

#### ❌ Éviter (CRITIQUE)

| Critère | Pourquoi |
|---------|----------|
| **Lune dans le signe qui gouverne la partie du corps opérée** | RÈGLE D'OR HISTORIQUE. L'énergie lunaire amplifie la zone → plus de saignements, plus de sensibilité, cicatrisation plus lente |
| **Mars rétrograde** | L'énergie du chirurgien est "à l'envers" → complications, erreurs, reprises |
| **Lune VOC** | L'intervention ne mène à rien de concluant. Résultats décevants |
| **Éclipse ±3 jours** | Imprévisibilité TOTALE des résultats. Non. |
| **Mars carré/opposition Sun** | Conflit d'énergie vital + chirurgical = risque |
| **Neptune en aspect Mars** | Confusion dans l'action → erreurs médicales, anesthésie problématique |

#### 📊 Table des signes par partie du corps (Zodiac Man)

**Tradition médicale millénaire.** ÉVITE la Lune dans le signe qui gouverne la zone opérée.

| Signe | Partie du corps | Exemples de chirurgies à ÉVITER sous cette Lune |
|-------|----------------|--------------------------------------------------|
| **Aries** ♈ | Tête, crâne, visage, cerveau | Chirurgie cérébrale, dentaire (mâchoire haute), rhinoplastie, lifting facial |
| **Taurus** ♉ | Gorge, cou, thyroïde, cordes vocales | Thyroïdectomie, amygdalectomie, chirurgie cervicale |
| **Gemini** ♊ | Bras, mains, poumons, épaules | Chirurgie pulmonaire, canal carpien, épaule |
| **Cancer** ♋ | Estomac, poitrine, seins | Mastectomie, bypass gastrique, chirurgie de l'estomac |
| **Leo** ♌ | Cœur, dos (colonne haute), artères | Chirurgie cardiaque, stents, pontage, colonne vertébrale haute |
| **Virgo** ♍ | Intestins, abdomen, pancréas | Appendicectomie, chirurgie intestinale, abdominoplastie |
| **Libra** ♎ | Reins, bas du dos, vessie | Néphrectomie, chirurgie rénale, calculs |
| **Scorpio** ♏ | Organes génitaux, rectum, colon | Chirurgie gynécologique, prostate, côlon, hémorroïdes |
| **Sagittarius** ♐ | Cuisses, hanches, foie | Prothèse de hanche, chirurgie hépatique |
| **Capricorn** ♑ | Genoux, os, dents, squelette | Prothèse de genou, chirurgie orthopédique, implants dentaires |
| **Aquarius** ♒ | Chevilles, mollets, circulation sanguine | Chirurgie vasculaire, varices, ligaments cheville |
| **Pisces** ♓ | Pieds, système lymphatique | Chirurgie podologique, drainage lymphatique |

**Exemple concret** : Tu dois te faire opérer du genou → ÉVITE quand la Lune est en Capricorn. Choisis un jour où la Lune est en un signe ÉLOIGNÉ (Cancer, Leo, Virgo par exemple) ET décroissante.

---

### e) 🏠 Achat immobilier / Déménagement

**L'immobilier = Maison 4 (H4).** Le foyer, les racines, la fondation. Ce que tu veux : une H4 FORTE et protégée.

#### ✅ Favoriser

| Critère | Détail |
|---------|--------|
| **H4 forte** | Jupiter en H4 = expansion du foyer, bonheur domestique. Venus en H4 = foyer beau et harmonieux |
| **Jupiter en H4** | LE meilleur placement : chance dans l'immobilier, foyer qui s'agrandit, bonheur domestique |
| **Lune en Taurus** | Lune en exaltation = stabilité émotionnelle liée au foyer. IDÉAL pour acheter |
| **Lune en Cancer** | Lune en domicile = connexion PROFONDE au foyer. Sentiment de "chez soi" immédiat |
| **Mercury direct** (pour l'achat/signature) | Les papiers, le notaire, les clauses = Mercury. DIRECT obligatoire |
| **Moon-Jupiter aspect** | Trigone/sextile = émotions expansives, sentiment de chance dans le foyer |
| **IC bien aspecté** | IC (cuspide de H4) avec trigone de Venus/Jupiter = fondation solide |
| **Lune croissante** (déménagement) | Tu EMMÉNAGES, tu CONSTRUIS un nouveau foyer → croissance |

#### ❌ Éviter

| Critère | Pourquoi |
|---------|----------|
| **Mars en H4** | Conflit dans le foyer. Travaux interminables, voisins agressifs, problèmes de structure |
| **Saturn en H4** | Restriction, lourdeur, foyer froid, sentiment d'être prisonnier chez soi |
| **Mercury rétrograde** (pour achat) | Papiers foireux, erreurs notariales, clauses manquantes, vice caché non détecté |
| **Pluto en H4** | Transformation FORCÉE du foyer. Crises domestiques. Trop intense |
| **Lune en Scorpio** | Émotions lourdes, possessivité liée au lieu, secrets dans les murs |
| **Neptune en H4** | Illusions sur le bien → tu découvres les problèmes APRÈS l'achat. Humidité cachée, fissures invisibles |
| **Lune VOC** | L'achat ne mène nulle part, le déménagement se passe mal |

#### 🏆 Configuration IDÉALE pour un achat immobilier

```
Jupiter en H4 (ou trigone IC)
Lune en Taurus ou Cancer, croissante
Mercury DIRECT (signature du compromis/acte)
H4 propre (pas de Mars/Saturn/Neptune)
Venus en H4 ou aspect harmonique avec IC
Pas d'éclipse ±3 jours
Moon applique trigone à Jupiter
```

---

### f) ✈️ Voyage

**Voyages courts = H3. Voyages longs / à l'étranger = H9.** Jupiter est la planète du voyage par excellence (Sagittarius = l'explorateur).

#### ✅ Favoriser

| Critère | Détail |
|---------|--------|
| **H9 propre** (voyage long) | Pas de maléfiques en H9 = voyage fluide, enrichissant |
| **Jupiter fort et bien aspecté** | Jupiter = voyage, exploration, chance à l'étranger |
| **Mercury direct** | Communication, transports, réservations = Mercury. Direct = tout roule |
| **Lune en Sagittarius** | LA Lune idéale pour voyager : aventure, ouverture, exploration |
| **Lune en Gemini** | Bonne pour voyages courts, déplacements, communication en voyage |
| **Jupiter en H9** | Chance en voyage, expériences enrichissantes, rencontres internationales |
| **Sun trigone Jupiter** | Confiance, protection, expériences positives |

#### ❌ Éviter

| Critère | Pourquoi |
|---------|----------|
| **Mars en H9** | Accidents à l'étranger, conflits pendant le voyage, agressivité |
| **Saturn en H3 ou H9** | Retards, restrictions de voyage, obstacles aux frontières, lourdeur |
| **Lune en Scorpio** | Émotions intenses, paranoïa en voyage, méfiance excessive |
| **Mercury rétrograde** | Bagages perdus, réservations annulées, retards de vol, GPS foireux, malentendus de langue |
| **Mars rétrograde** | Énergie bloquée = accidents, fatigue en voyage |
| **Neptune en H9** | Tu te perds. Littéralement et figurativement. Arnaques à l'étranger, confusion de direction |

---

### g) 💘 Premier rendez-vous / Déclaration d'amour

**L'énergie du premier rendez-vous = le "thème natal" de la relation.** Tu veux que cette première impression soit MAGNÉTIQUE.

#### ✅ Favoriser

| Critère | Détail |
|---------|--------|
| **Venus-Mars aspects harmoniques** | Trigone/sextile = chimie naturelle, attraction fluide. C'est LE combo pour la séduction |
| **Lune en Taurus** | Sensualité, douceur, plaisir des sens. IDÉAL pour un dîner romantique |
| **Lune en Libra** | Harmonie, charme, équilibre. L'énergie du "couple" par excellence |
| **Lune en Leo** | Générosité, romance, théâtralité. Parfait si tu veux impressionner |
| **Venus en H1 ou H5** | H1 = charme personnel. H5 = romance, plaisir, flirt |
| **Venus trigone/sextile Jupiter** | Amour expansif, générosité, sentiment de chance romantique |
| **Lune croissante** | Énergie de croissance → la relation a envie de GRANDIR |
| **ASC en signe favorable** | Libra ASC = charme, Taurus ASC = sensualité, Leo ASC = magnétisme |
| **Vendredi soir** | Jour de Venus. C'est pas un hasard si c'est le jour des dates 😏 |

#### ❌ Éviter

| Critère | Pourquoi |
|---------|----------|
| **Saturn carré Venus** | L'amour est BLOQUÉ, lourd, froid. Le rendez-vous aura une ambiance pesante |
| **Lune en Capricorn** | Froideur émotionnelle, rigidité, le date ressemble à un entretien d'embauche |
| **Lune en Virgo** | Critique, analyse excessive, perfectionnisme → tu analyses chaque mot au lieu de profiter |
| **Venus rétrograde** | L'énergie est tournée vers le PASSÉ (les ex). Pas idéal pour du NEUF |
| **Mars carré Venus** | Attirance + frustration = premier date qui finit en conflit |
| **Lune VOC** | Le date ne mène à rien. Pas de second rendez-vous. Ghosting garanti. |
| **Saturn en H5 ou H7** | Restriction dans la romance (H5) ou le partenariat (H7) |

---

### h) 💼 Entretien d'embauche / Négociation

**L'entretien = ton thème de "naissance" dans l'entreprise.** Tu veux apparaître PUISSANT, convaincant, chanceux.

#### ✅ Favoriser

| Critère | Détail |
|---------|--------|
| **Mercury fort** | Mercury en Gemini ou Virgo = communication claire, arguments solides, éloquence |
| **Jupiter en H10** | Succès professionnel, reconnaissance, le recruteur t'aime |
| **Sun bien aspecté** | Sun trigone Jupiter = confiance, charisme, présence qui impressionne |
| **Mars en H10 ou H1** | Énergie d'action, initiative, tu apparais comme quelqu'un de DYNAMIQUE |
| **H10 propre** | Pas de maléfiques = carrière fluide, bonne réputation |
| **Mercury trigone/sextile Jupiter** | Tu dis les bons mots, tu vends bien, tu convaincs naturellement |
| **Lune en Leo** | Confiance, charisme, présence royale. Idéal pour faire bonne impression |
| **Lune en Capricorn** | Ici c'est BIEN (contrairement au rendez-vous amoureux) : sérieux, professionnel, structuré |
| **ASC en signe de terre ou feu** | Terre = fiable, compétent. Feu = dynamique, leader |

#### ❌ Éviter

| Critère | Pourquoi |
|---------|----------|
| **Mercury rétrograde** | Malentendus, tu te trompes dans ce que tu dis, le recruteur ne comprend pas ton CV |
| **Mars rétrograde** | Tu n'as pas d'énergie, tu apparais passif, tes actions sont bloquées |
| **Saturn en H10** | Le poste est bloqué, la hiérarchie est lourde, tu ne seras pas promu |
| **Neptune en H10** | Illusion professionnelle : le job n'est pas ce qu'on t'a vendu |
| **Lune en Pisces** (pour négociation) | Trop mou, trop conciliant, tu te fais rouler sur le salaire |
| **Mars carré Mercury** | Tu dis un truc agressif sans faire exprès, ça clash avec le recruteur |
| **Lune VOC** | L'entretien ne donne pas suite. Tu n'as pas de nouvelles. Ghosté par le RH. |

#### 🏆 Configuration IDÉALE pour un entretien

```
Mercury DIRECT, en Gemini ou Virgo
Jupiter en H10 ou trigone MC
Sun trigone Jupiter (confiance + charisme)
Lune en Leo ou Capricorn (impression + sérieux)
Mars en H1 (énergie, dynamisme)
H10 propre
Pas de Mercury/Mars rétrograde
Mardi (jour de Mars = action) ou Jeudi (jour de Jupiter = chance)
```

---

### i) 💻 Lancement site web / App / Produit digital

**Le digital = Mercury + Uranus.** Mercury pour la communication/tech, Uranus pour l'innovation/digital. Ce combo doit être PROPRE.

#### ✅ Favoriser

| Critère | Détail |
|---------|--------|
| **Mercury-Uranus aspects harmoniques** | Trigone/sextile = innovation fluide, tech qui fonctionne, adoption rapide |
| **Lune croissante** | Croissance, adoption, virality → tu veux que ça MONTE |
| **Aquarius actif** | Planètes en Aquarius = énergie d'innovation, de technologie, de communauté |
| **Gemini actif** | Planètes en Gemini = communication rapide, viralité, curiosité du public |
| **Mercury en Gemini ou Aquarius** | Mercury en domicile (Gemini) ou en signe tech (Aquarius) = parfait |
| **Jupiter trigone Mercury** | L'info se propage, le message est entendu, l'audience grandit |
| **H11 forte** | Maison des réseaux, communauté, audiences. Jupiter en H11 = communauté qui grandit |
| **Uranus bien aspecté** | Innovation réussie, disruption positive |
| **Mercury en H3 ou H11** | H3 = communication. H11 = réseau, communauté. |

#### ❌ Éviter

| Critère | Pourquoi |
|---------|----------|
| **Mercury rétrograde** | **CRITIQUE.** C'est le transit le plus DANGEREUX pour un lancement digital. Bugs, crashes, UX horrible, serveurs qui tombent, fonctionnalité qui marche pas, mauvaise communication marketing. Si tu lances un site/app sous Mercury rétro, prépare-toi à devoir TOUT refaire dans 3 semaines. |
| **Éclipses** | Trajectoire imprévisible. Le produit peut exploser dans une direction que tu n'avais pas prévue |
| **Uranus carré Mercury** | Tech instable, bugs inattendus, disruption NÉGATIVE |
| **Neptune carré/opposé Mercury** | Confusion dans le message, UX confuse, utilisateurs ne comprennent pas le produit |
| **Mars carré Uranus** | Accidents tech, serveurs qui crashent, perte de données |
| **Saturn carré Mercury** | La communication est bloquée : le produit ne se fait pas connaître, l'adoption est LENTE |
| **Lune VOC** | Le lancement tombe à plat. Pas d'engagement, pas de traction. |
| **Lune décroissante** | L'énergie décroît → adoption qui chute au lieu de monter |

#### 🏆 Configuration IDÉALE pour un lancement digital

```
Mercury DIRECT, en Gemini ou Aquarius ou Virgo
Mercury trigone/sextile Uranus (innovation + communication)
Lune croissante en Gemini ou Aquarius (viralité, communauté)
Jupiter en H11 ou trigone Mercury (audience qui grandit)
Pas d'éclipse ±3 jours
H3 et H11 propres
Mercredi (jour de Mercury)
```

---

## ✅ Checklist universelle (pour TOUTE action élective)

**Avant de recommander un timing, vérifie CHAQUE point. Pas de raccourci.**

### Checklist obligatoire

- [ ] **Lune PAS void of course** — La Lune fait au moins UN aspect majeur avant de changer de signe
- [ ] **Planète maîtresse de l'action PAS rétrograde** — Venus pour amour, Mercury pour contrats/digital, Mars pour chirurgie/action, Jupiter pour business
- [ ] **Pas d'éclipse ±3 jours** — Ni solaire ni lunaire
- [ ] **Lune croissante** (pour commencer quelque chose) OU **décroissante** (pour terminer/réduire quelque chose)
- [ ] **ASC et maison concernée PROPRES** — Pas de maléfiques (Saturn, Mars, Pluto) dans la maison qui gouverne l'action ou sur l'ASC
- [ ] **Au moins UN aspect harmonique majeur avec Jupiter** — Trigone ou sextile Jupiter avec une planète clé = protection et expansion
- [ ] **Mercury DIRECT** (si contrats, communication, tech, voyage sont impliqués)
- [ ] **Lune en signe compatible** avec l'action (voir les recommandations par type)
- [ ] **Aspects appliquants favorables** — La Lune ou la planète maîtresse applique un trigone/sextile (pas un carré/opposition)
- [ ] **Planète maîtresse en dignité acceptable** — Pas en détriment ni en chute

### Critères bonus (pas obligatoires mais FORTEMENT recommandés)

- [ ] **Jour de la semaine aligné** — Lundi=Lune, Mardi=Mars, Mercredi=Mercury, Jeudi=Jupiter, Vendredi=Venus, Samedi=Saturn, Dimanche=Sun
- [ ] **Heure planétaire alignée** — L'heure planétaire correspond à la planète maîtresse de l'action
- [ ] **North Node favorable** — North Node en aspect harmonique avec planète maîtresse = destinée alignée
- [ ] **Pas de carré/opposition entre luminaires** — Sun-Moon en harmonie = volonté et émotions alignées
- [ ] **Réception mutuelle** — Si deux planètes clés sont en réception mutuelle = renforcement mutuel

---

## 📊 Scoring d'un moment élective

Pour évaluer un créneau, utilise ce barème :

### Points positifs

| Critère rempli | Points |
|---------------|--------|
| Lune PAS VOC | +1 |
| Planète maîtresse directe et en dignité | +2 |
| Lune en signe idéal pour l'action | +1.5 |
| Lune croissante (pour lancements) | +1 |
| Jupiter aspect harmonique avec planète clé | +2 |
| Maison concernée propre (pas de maléfiques) | +1.5 |
| ASC propre | +1 |
| Mercury direct (si applicable) | +1 |
| Jour de la semaine aligné | +0.5 |
| Double aspect harmonique (ex: Venus trigone Jupiter ET sextile Moon) | +1 |

### Points négatifs

| Critère violé | Points |
|--------------|--------|
| Lune VOC | **-3** |
| Planète maîtresse rétrograde | **-3** |
| Éclipse ±3 jours | **-3** |
| Maléfique en maison concernée | -2 |
| Carré/opposition entre planètes clés | -1.5 |
| Lune en signe défavorable pour l'action | -1 |
| Mercury rétrograde (si communication impliquée) | **-3** |
| Neptune aspect tendu avec planète clé | -1.5 |
| Planète maîtresse en détriment/chute | -2 |

### Interprétation du score

| Score | Verdict |
|-------|---------|
| **10+** | 🏆 **EXCEPTIONNEL** — Fonce les yeux fermés. Ce créneau est un cadeau du ciel. RARE. |
| **7-9** | ✅ **TRÈS BON** — Conditions très favorables. Fonce. |
| **5-6** | ⚠️ **CORRECT** — Acceptable, mais pas parfait. Si tu peux attendre mieux, attends. |
| **3-4** | 🚨 **MÉDIOCRE** — Beaucoup de facteurs négatifs. Risqué. |
| **< 3** | ❌ **INTERDIT** — NE FAIS PAS ÇA à cette date. ATTENDS. |

---

## 📋 Format du rapport élective

```markdown
# 🗓️ ASTROLOGIE ÉLECTIVE

## Action demandée
**[Type d'action]** : [Description précise]

**Période souhaitée** : [Fenêtre dans laquelle le user veut agir]
**Lieu** : [Ville, pays → pour le calcul des maisons/ASC]

---

## Planètes et maisons clés pour cette action

| Élément | Rôle | État actuel |
|---------|------|-------------|
| **Planète maîtresse** | [Planète] | [Signe, dignité, rétrograde?] |
| **Maison concernée** | H[X] | [Signe sur cuspide, planètes présentes] |
| **Lune** | Co-significateur universel | [Signe, phase, VOC?, prochain aspect] |
| **Mercury** | Communication/contrats | [Direct/Rétrograde, signe] |

---

## Analyse des fenêtres candidates

### 🟢 FENÊTRE 1 : [Date + Heure]

**Score : X/10**

**Points positifs** :
- ✅ [Critère 1] (+X pts)
- ✅ [Critère 2] (+X pts)
- ✅ [Critère 3] (+X pts)

**Points négatifs** :
- ❌ [Critère 1] (-X pts)
- ⚠️ [Critère 2] (-X pts)

**Lune** : [Signe, phase, VOC?, dernier/prochain aspect]
**Planète maîtresse** : [État complet]
**Maison concernée** : [État complet]

**Verdict** : [Recommandation brutale]

---

### 🟡 FENÊTRE 2 : [Date + Heure]

[Même format]

---

### 🔴 FENÊTRE 3 : [Date + Heure]

[Même format]

---

## 🏆 RECOMMANDATION FINALE

### **MEILLEUR MOMENT : [Date + Heure]**

**Score : X/10**

**Pourquoi ce moment** :
[Justification complète basée sur tous les critères]

**Ce qui sera favorisé** :
- [Avantage 1]
- [Avantage 2]

**Ce qu'il faut surveiller malgré tout** :
- [Point d'attention 1]
- [Point d'attention 2]

### Moments à ÉVITER ABSOLUMENT

| Date | Raison | Risque |
|------|--------|--------|
| [Date 1] | [Mercury rétro / Éclipse / etc.] | [Conséquence concrète] |
| [Date 2] | [...] | [...] |

---

## 📋 CHECKLIST PRÉ-ACTION

- [ ] Confirmer que l'action a lieu EXACTEMENT à [heure recommandée]
- [ ] Vérifier la météo émotionnelle du jour (pas de stress externe qui pourrait saboter)
- [ ] Si possible, aligner le LIEU avec l'action (lieu qui renforce la maison concernée)
- [ ] Garder le plan de secours si la fenêtre principale est compromise

---

## ⚠️ Disclaimer

L'astrologie élective met les PROBABILITÉS de ton côté. Elle ne garantit pas le succès. Un bon timing + une bonne préparation + un bon projet = la combinaison gagnante. Le timing seul ne suffit pas. Mais un mauvais timing peut SABOTER un bon projet.
```

---

## 📚 Cas spéciaux et astuces avancées

### 🔄 Quand AUCUN bon moment n'existe dans la fenêtre

Parfois, le user a une deadline (ex: "je dois signer ce contrat cette semaine") et TOUS les jours ont des problèmes.

**Stratégie de DOMMAGE MINIMUM** :
1. Identifie le PIRE problème de chaque jour
2. Choisis le jour avec le MOINDRE pire problème
3. Compense avec ce que tu peux contrôler :
   - Si Lune VOC mais le reste est OK → agis JUSTE AVANT que la Lune devienne VOC
   - Si Mercury rétro → fais relire le contrat 3 fois par 3 personnes différentes
   - Si aspect tendu → choisis l'heure où la Lune fait un aspect harmonique transitoire

**DIS-LE au user** : "Il n'y a pas de moment parfait cette semaine. Voici le MOINS PIRE avec les précautions à prendre."

---

### 🌙 L'importance de l'heure exacte

**Le thème change chaque HEURE** (l'ASC change de signe toutes les ~2 heures).

**Conséquence** : Tu peux avoir le même JOUR avec un ASC Libra à 10h (harmonieux pour mariage) et un ASC Scorpio à 12h (trop intense pour mariage).

**Recommande toujours une HEURE précise**, pas juste un jour.

---

### ♻️ Rétrogrades : la nuance

**Mercury rétrograde n'est pas TOUJOURS mauvais en élective** :
- Si tu REFAIS quelque chose (re-lancer un projet, re-signer un contrat renégocié, re-déménager dans un ancien lieu) → Mercury rétro est FAVORABLE (l'énergie du "re-")
- Si le user a Mercury rétrograde NATAL → il gère mieux les rétrogrades que les autres

**Venus rétrograde n'est pas toujours mauvais** :
- Pour RENOUVELER des vœux de mariage avec le MÊME partenaire → OK
- Pour retrouver un ex VOLONTAIREMENT → Venus rétro est en fait alignée

**Mars rétrograde** :
- Pour la chirurgie de RÉVISION (refaire une opération précédente) → acceptable

**Mais par défaut, en élective, ÉVITE les rétrogrades.** Ces nuances sont des exceptions, pas la règle.

---

### 🌑 Éclipses : le cas des actions karmiques

Si le user est prêt à ACCEPTER une trajectoire imprévisible et karmique, une éclipse peut être utilisée volontairement. Mais il faut être TRÈS clair sur le risque :

> "Tu peux lancer sous éclipse si tu acceptes que l'univers reprenne le volant. Ce ne sera PAS ce que tu avais prévu. Ça peut être MIEUX ou PIRE — mais ça sera DIFFÉRENT. Si tu es OK avec ça, fonce."

---

### 📐 Technique avancée : la Lune comme chronomètre

**La Lune est la planète la plus RAPIDE** (~2.5 jours par signe). Elle est ton outil de timing PRÉCIS.

**Technique** :
1. Identifie le jour général (macro : planètes lentes, pas de rétrograde, etc.)
2. Affine avec la Lune (micro : quel signe, quel aspect, VOC ou pas)
3. Affine encore avec l'ASC (micro-micro : quelle heure met le bon signe sur l'ASC)

**La Lune te donne des fenêtres de ~6h à ~48h maximum.** L'ASC te donne des fenêtres de ~2h. Combinés, tu peux déterminer un créneau de 1-2h optimal.

---

## 🔧 Utilisation du script pour l'élective

### Étape 1 : Scanner les éphémérides du mois cible

```bash
# Positions quotidiennes de toutes les planètes pour le mois
python3 scripts/ephemeris.py ephemeris --year 2026 --month 06
```

Regarde :
- Quand Mercury/Venus/Mars sont DIRECTS
- Où sont les planètes lentes (Jupiter, Saturn)
- Quand la Lune change de signe
- Quelles sont les Nouvelles/Pleines Lunes

### Étape 2 : Vérifier les transits de l'année

```bash
# Vue d'ensemble des transits (rétrogrades, éclipses, conjonctions)
python3 scripts/ephemeris.py transits --date DD.MM.YYYY --time HH:MM --lat LAT --lon LON --year YYYY
```

Identifie :
- Les périodes de rétrogrades (Mercury 3-4x/an, Venus ~1x/an, Mars ~1x/2ans)
- Les éclipses (±3 jours = interdit)
- Les conjonctions rares (bonus si favorables)

### Étape 3 : Calculer le thème du moment choisi

```bash
# Thème natal du moment élective (vérifie ASC, maisons, aspects)
python3 scripts/ephemeris.py natal --date DD.MM.YYYY --time HH:MM --lat LAT --lon LON --tz TZ
```

Vérifie :
- ASC et son maître
- Maison concernée et son contenu
- Position et état de la Lune
- Aspects exacts entre planètes clés
- Présence de maléfiques dans les maisons sensibles

---

## 📊 Table récapitulative : planète maîtresse par action

| Action | Planète maîtresse | Maison clé | Lune idéale | Jour idéal |
|--------|-------------------|------------|-------------|------------|
| **Mariage** | Venus | H7 | Taurus/Cancer/Libra | Vendredi |
| **Business** | Jupiter | H10 | Leo/Taurus/Aries | Jeudi |
| **Contrat** | Mercury | H7/H3 | Gemini/Libra/Aquarius | Mercredi |
| **Chirurgie** | Mars | H6 | Décroissante, PAS dans le signe de la zone | Mardi |
| **Immobilier** | Moon (+Mercury) | H4 | Taurus/Cancer | Lundi |
| **Voyage** | Mercury/Jupiter | H9 (long) / H3 (court) | Sagittarius/Gemini | Jeudi |
| **Premier date** | Venus + Mars | H5/H7 | Taurus/Libra/Leo | Vendredi |
| **Entretien** | Mercury + Sun | H10 | Leo/Capricorn | Mardi/Jeudi |
| **Lancement digital** | Mercury + Uranus | H3/H11 | Gemini/Aquarius | Mercredi |
| **Début de régime/sport** | Mars | H6 | Aries/Virgo (décroissante pour perdre) | Mardi |
| **Investissement** | Jupiter + Venus | H2/H8 | Taurus/Cancer | Jeudi |
| **Procès / action légale** | Jupiter + Mars | H9/H7 | Leo/Sagittarius | Jeudi |
| **Début de thérapie** | Neptune + Moon | H12/H8 | Pisces/Cancer/Scorpio | Lundi |

---

## 🚨 Les 10 erreurs fatales en astrologie élective

1. **Ignorer la Lune VOC** → L'erreur la plus COURANTE. La Lune VOC tue silencieusement l'action.

2. **Se marier sous Venus rétrograde** → Classique. Les gens choisissent la "belle date" (14 février, été) sans vérifier. Si Venus est rétro ce jour-là : CHANGE DE DATE.

3. **Lancer un business sous Mercury rétrograde** → "Mais j'ai déjà réservé le lieu pour l'événement de lancement !" Tant pis. Reporte. Ou fais le soft launch en secret et l'annonce officielle APRÈS.

4. **Ne vérifier QUE la Lune** → La Lune est importante mais INSUFFISANTE. Il faut aussi vérifier la planète maîtresse, les maisons, les aspects.

5. **Oublier les éclipses** → Elles sont faciles à oublier parce qu'elles n'arrivent que 4x/an. Mais quand elles tombent pile pendant ta fenêtre, DÉCALE.

6. **Ne pas vérifier la maison concernée** → Jupiter peut être en trigone à tout, mais si Saturn est assis dans ta H7 le jour du mariage, c'est foutu.

7. **Confondre Lune croissante et décroissante** → Croissante = COMMENCER. Décroissante = TERMINER/RÉDUIRE. Un régime se lance en décroissante (tu RÉDUIS), un business en croissante (tu CROIS).

8. **Ignorer l'ASC du moment** → L'ASC change toutes les 2h. Le MÊME jour peut avoir un ASC parfait à 14h et un ASC désastreux à 16h. VÉRIFIE L'HEURE.

9. **Surcharger les critères** → Si tu veux TOUT parfait, tu n'agiras jamais. Vise 7-8 critères remplis sur 10. La perfection n'existe pas.

10. **Ne pas informer le user des limites** → L'astrologie élective n'est pas une garantie. C'est un AVANTAGE STATISTIQUE. DIS-LE.

---

## ⚠️ Points critiques

1. **Vérifie TOUJOURS la Lune VOC** — C'est la règle #1, avant tout le reste
2. **Mercury rétrograde = INTERDIT pour contrats et digital** — Pas de nuance ici, c'est binaire
3. **Venus rétrograde = INTERDIT pour mariage et premier rendez-vous** — Sauf cas de renouvellement
4. **Mars rétrograde = INTERDIT pour chirurgie et lancement** — L'action est BLOQUÉE
5. **Éclipses ±3 jours = zone d'exclusion** — Pas de décision importante
6. **Recommande toujours une HEURE précise** — Pas juste un jour
7. **Score minimum de 7/10 pour recommander** — En dessous, cherche une autre fenêtre
8. **Si aucun bon moment, DIS-LE** — Propose la stratégie de dommage minimum
9. **Le thème natal du user reste DOMINANT** — L'élective améliore, elle ne remplace pas
10. **Sois BRUTAL sur les mauvais timings** — Si le user veut agir un jour de merde, DIS-LE clairement

---

**Retourne au [SKILL.md principal](../SKILL.md) pour workflow complet.**
