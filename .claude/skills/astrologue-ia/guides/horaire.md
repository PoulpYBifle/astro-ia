# ❓ Guide : Astrologie Horaire (Horary Astrology)

L'astrologie horaire est l'art de répondre à une **QUESTION PRÉCISE** en analysant le thème du moment exact où la question est posée.

---

## 🎯 Objectif

Répondre OUI/NON (ou nuancé) à une question spécifique posée par le user, avec timing et détails, en analysant le thème horaire (carte du ciel du moment de la question).

---

## 📊 Principe fondamental

**Le thème horaire = photo du ciel au moment EXACT où la question est COMPRISE par l'astrologue.**

Le principe : L'univers reflète la réponse à ta question dans la configuration céleste du moment où tu la poses. Pas de thème natal nécessaire (même si l'avoir aide).

---

## 🔧 Comment calculer un thème horaire

```bash
# Thème du moment actuel pour le lieu de l'astrologue/user
python3 scripts/ephemeris.py natal --date DD.MM.YYYY --time HH:MM --lat LAT --lon LON --tz TZ
```

**Important** : Utilise la date/heure du moment où la question est posée dans le chat, PAS l'heure de naissance du user.

---

## 📋 Types de questions

### Questions valides pour l'horaire
- ✅ "Est-ce que je devrais accepter ce job ?"
- ✅ "Est-ce que X m'aime ?"
- ✅ "Vais-je retrouver mon objet perdu ?"
- ✅ "Est-ce que ce projet va réussir ?"
- ✅ "Est-ce que je devrais déménager ?"
- ✅ "Quand vais-je trouver l'amour ?"
- ✅ "Est-ce que cette personne est honnête avec moi ?"

### Questions NON valides
- ❌ Questions testées (poser 5 fois la même question)
- ❌ Questions sans investissement émotionnel réel
- ❌ Questions sur la mort d'autrui
- ❌ Questions "pour rire"

---

## 📊 Méthodologie Step-by-Step

### PHASE 1 : VÉRIFICATION PRÉALABLE ("Radicality")

Avant d'interpréter, vérifie que le thème est **radical** (valide pour interprétation) :

#### Conditions qui INVALIDENT le thème (Strictures) :

**1. Saturn en H7** (maison de l'astrologue)
- Le thème PRÉVIENT que l'astrologue va se tromper
- **Action** : Préviens le user, interprète avec précaution

**2. Lune Void of Course (VOC)**
- La Lune ne fait AUCUN aspect majeur avant de changer de signe
- **Signification** : "Rien ne va se passer" ou "La situation va rester telle quelle"
- **Exception** : En Cancer, Taurus, Sagittarius, Pisces → la Lune VOC peut quand même fonctionner

**3. ASC à moins de 3° d'un signe (Early ASC)**
- Trop tôt pour juger, la situation n'est pas encore mûre
- **Action** : "Reviens poser la question dans quelques jours/semaines"

**4. ASC à plus de 27° d'un signe (Late ASC)**
- Trop tard, la situation est déjà résolue ou le moment est passé
- **Action** : "L'issue est déjà déterminée, tu le sais probablement déjà"

**5. Via Combusta (15° Libra - 15° Scorpio)**
- Si ASC ou Lune sont dans cette zone : DANGER, situation chaotique
- **Action** : Interprète avec extrême prudence

#### Si thème radical → continue. Sinon → préviens et nuance.

---

### PHASE 2 : IDENTIFICATION DES SIGNIFICATEURS

Les significateurs sont les planètes qui REPRÉSENTENT les parties impliquées dans la question.

#### **Le Querent (celui qui pose la question)**
- **Toujours** = Maître de H1 (planète qui gouverne le signe de l'ASC)
- **Co-significateur** = La Lune (TOUJOURS co-significateur du querent)

#### **Le Quesited (ce sur quoi porte la question)**
Dépend du SUJET de la question :

| Question sur... | Maison | Significateur |
|----------------|--------|---------------|
| **Amour / partenaire** | H7 | Maître de H7 |
| **Argent du querent** | H2 | Maître de H2 |
| **Travail / job** | H10 | Maître de H10 |
| **Travail quotidien / collègues** | H6 | Maître de H6 |
| **Maison / immobilier** | H4 | Maître de H4 |
| **Enfants** | H5 | Maître de H5 |
| **Santé** | H6 (maladie) / H1 (corps) | Maître de H6 |
| **Ennemi / compétiteur** | H7 | Maître de H7 |
| **Objet perdu** | H2 (possessions) | Maître de H2 |
| **Voyages** | H9 (long) / H3 (court) | Maître correspondant |
| **Amis** | H11 | Maître de H11 |
| **Secrets / peurs** | H12 | Maître de H12 |
| **Famille / père** | H4 | Maître de H4 |
| **Mère** | H10 | Maître de H10 |
| **Frères/sœurs** | H3 | Maître de H3 |
| **Argent de l'autre** | H8 | Maître de H8 |
| **Héritage** | H8 | Maître de H8 |

#### Table des Maîtrises (Rulerships)

| Signe | Maître traditionnel | Maître moderne |
|-------|-------------------|----------------|
| Aries | **Mars** | Mars |
| Taurus | **Venus** | Venus |
| Gemini | **Mercury** | Mercury |
| Cancer | **Lune** | Lune |
| Leo | **Soleil** | Soleil |
| Virgo | **Mercury** | Mercury |
| Libra | **Venus** | Venus |
| Scorpio | **Mars** | ~~Pluto~~ (utilise Mars en horaire) |
| Sagittarius | **Jupiter** | Jupiter |
| Capricorn | **Saturn** | Saturn |
| Aquarius | **Saturn** | ~~Uranus~~ (utilise Saturn en horaire) |
| Pisces | **Jupiter** | ~~Neptune~~ (utilise Jupiter en horaire) |

**IMPORTANT** : En astrologie horaire, on utilise les **maîtrises TRADITIONNELLES** (7 planètes classiques : Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn).

---

### PHASE 3 : DIGNITÉS ESSENTIELLES

Les dignités indiquent l'ÉTAT du significateur (fort ? faible ? bienveillant ? malveillant ?)

#### Dignités positives (la planète est FORTE)

| Dignité | Points | Signification |
|---------|--------|---------------|
| **Domicile** (dans son propre signe) | +5 | En pleine puissance, contrôle total |
| **Exaltation** (dans son signe d'exaltation) | +4 | Au sommet, grandiose, mais peut exagérer |
| **Triplicité** (maître de l'élément) | +3 | Confortable, soutenu |
| **Terme** | +2 | Aide mineure |
| **Face/Décan** | +1 | Aide minimale, "mieux que rien" |

#### Dignités négatives (la planète est FAIBLE)

| Dignité | Points | Signification |
|---------|--------|---------------|
| **Détriment** (signe opposé au domicile) | -5 | Mal à l'aise, dysfonctionnelle |
| **Chute** (signe opposé à l'exaltation) | -4 | Humiliée, impuissante |
| **Pérégrine** (aucune dignité) | -5 | Vagabonde, sans ressources, potentiellement malhonnête |

#### Table des Domiciles et Exaltations

| Planète | Domicile | Exaltation | Détriment | Chute |
|---------|----------|------------|-----------|-------|
| Sun | Leo | Aries 19° | Aquarius | Libra |
| Moon | Cancer | Taurus 3° | Capricorn | Scorpio |
| Mercury | Gemini/Virgo | Virgo 15° | Sagittarius/Pisces | Pisces |
| Venus | Taurus/Libra | Pisces 27° | Scorpio/Aries | Virgo |
| Mars | Aries/Scorpio | Capricorn 28° | Libra/Taurus | Cancer |
| Jupiter | Sagittarius/Pisces | Cancer 15° | Gemini/Virgo | Capricorn |
| Saturn | Capricorn/Aquarius | Libra 21° | Cancer/Leo | Aries |

**Interprétation des dignités** :
- Significateur du querent en domicile → Le querent est en position de FORCE
- Significateur du quesited en détriment → Le sujet de la question est en MAUVAIS état
- Significateur pérégrin → Attention, cette personne/chose n'a pas de plan clair

---

### PHASE 4 : ASPECTS ENTRE SIGNIFICATEURS

C'est ici que se joue la réponse OUI/NON.

#### **OUI = les significateurs vont former un ASPECT**

**Aspect appliquant (applying)** = la planète la plus rapide se RAPPROCHE de l'aspect exact.

| Aspect | Résultat |
|--------|----------|
| **Conjonction appliquante** | OUI FORT - union, rencontre, accomplissement |
| **Trigone appliquant** | OUI FACILE - ça va se faire sans effort |
| **Sextile appliquant** | OUI avec EFFORT - possible mais il faut agir |
| **Carré appliquant** | OUI DIFFICILE - ça va se faire mais dans la douleur |
| **Opposition appliquante** | MITIGÉ - ça se fait puis ça explose |

#### **NON = pas d'aspect entre significateurs**

**Aucun aspect appliquant** entre le maître de H1 et le maître de la maison concernée = **NON, ça ne va pas se faire.**

#### **Cas spéciaux**

**1. Translation de lumière**
- Si planète A ne voit pas planète B, mais planète C forme aspect avec les deux
- = Un INTERMÉDIAIRE va aider à réaliser la chose
- Ex: Ami, entremetteur, événement tiers

**2. Collection de lumière**
- Deux planètes appliquent vers une MÊME planète plus lente
- = Une tierce personne/chose va unir les deux parties

**3. Prohibition**
- Une planète BLOQUE l'aspect entre les deux significateurs
- = Quelqu'un/quelque chose EMPÊCHE la réalisation

**4. Refranation**
- La planète rapide devient rétrograde AVANT de compléter l'aspect
- = Le querent va CHANGER D'AVIS ou la situation va capoter

**5. Combustion**
- Significateur à moins de 8° du Soleil (invisible car brûlé par la lumière)
- = La personne/chose est INVISIBLE, cachée, impuissante
- Particulièrement grave si significateur du quesited est combust

**6. Cazimi**
- Significateur à moins de 17' du Soleil (au CŒUR du Soleil)
- = PARADOXALEMENT ultra-puissant, protégé par le roi

---

### PHASE 5 : LA LUNE (analyse cruciale)

La Lune est TOUJOURS co-significateur du querent et indique le DÉROULEMENT des événements.

#### **Dernier aspect de la Lune**
- Montre ce qui VIENT DE SE PASSER (contexte de la question)
- Ex: Lune vient de faire carré à Saturn = le querent vient de vivre une restriction/déception

#### **Prochain aspect de la Lune**
- Montre ce qui VA SE PASSER ensuite
- Ex: Lune va faire trigone à Jupiter = bonne nouvelle à venir

#### **Lune Void of Course (VOC)**
- Aucun aspect avant changement de signe
- = **"Rien ne va se passer"**
- La situation reste en l'état
- Parfois : "Ne t'inquiète pas, tout va bien sans rien faire"

#### **Phase lunaire**

| Phase | Signification |
|-------|---------------|
| Nouvelle Lune (0-45°) | Nouveau départ, énergie naissante |
| Croissant (45-90°) | Effort, construction |
| Premier Quartier (90-135°) | Crise d'action, décision nécessaire |
| Gibbeux (135-180°) | Perfectionnement, patience |
| Pleine Lune (180-225°) | Culmination, révélation, réponse claire |
| Disséminant (225-270°) | Partage, distribution |
| Dernier Quartier (270-315°) | Crise de conscience, réévaluation |
| Balsamique (315-360°) | Fin de cycle, lâcher-prise |

---

### PHASE 6 : TIMING

**Quand la chose va-t-elle se produire ?**

Le timing dépend du nombre de DEGRÉS entre le significateur et l'aspect exact, combiné au type de maison :

| Maison angulaire (1, 4, 7, 10) | Maison succédente (2, 5, 8, 11) | Maison cadente (3, 6, 9, 12) |
|------|------|------|
| **Rapide** | **Moyen** | **Lent** |

| Signe cardinal | Signe fixe | Signe mutable |
|------|------|------|
| Jours/Semaines | Mois | Semaines/Mois |

**Formule approximative** :
- Nombre de degrés avant aspect exact = nombre d'unités de temps
- Unité de temps dépend du signe et de la maison :

| | Cardinal | Fixe | Mutable |
|---|---|---|---|
| **Angulaire** | Jours | Semaines | Jours |
| **Succédente** | Semaines | Mois | Semaines |
| **Cadente** | Mois | Mois | Mois |

**Exemple** : Significateur à 5° d'un trigone, en signe cardinal, maison angulaire → **~5 jours**

---

## 📋 Format du rapport horaire

```markdown
# ❓ ASTROLOGIE HORAIRE

## Question
**"[Question exacte du user]"**

**Date/Heure** : [Date et heure de la question]
**Lieu** : [Lieu du user]

---

## Validation du thème

**ASC** : [Signe et degré] → [Early/Late/OK]
**Lune** : [Signe et degré] → [VOC ? Phase ?]
**Saturn en H7** : [Oui/Non]
**Thème radical** : [OUI/NON + explication]

---

## Significateurs

| Rôle | Planète | Signe | Dignité | État |
|------|---------|-------|---------|------|
| **Querent (H1)** | [Maître H1] | [Signe] | [Domicile/Exaltation/etc.] | [Fort/Faible] |
| **Co-significateur** | Lune | [Signe] | [Dignité] | [État] |
| **Quesited ([HX])** | [Maître HX] | [Signe] | [Dignité] | [Fort/Faible] |

---

## Analyse

### Aspect entre significateurs
[Y a-t-il un aspect appliquant ?]
[Si oui : quel type ? Combien de degrés ?]
[Si non : translation/collection possible ?]

### La Lune
- **Dernier aspect** : [Aspect] → [Ce qui vient de se passer]
- **Prochain aspect** : [Aspect] → [Ce qui va se passer]
- **VOC** : [Oui/Non]

### Facteurs supplémentaires
[Prohibition, refranation, combustion, réception mutuelle, etc.]

---

## 🎯 RÉPONSE

### **[OUI / NON / MITIGÉ]**

[Explication brutale et détaillée]

### Timing estimé
[X jours/semaines/mois - basé sur degrés et maisons]

### Conseils
[Actions concrètes basées sur l'analyse]

### ⚠️ Nuances
[Ce qui pourrait changer le résultat]
```

---

## ⚠️ Points critiques

1. **Utilise les MAÎTRISES TRADITIONNELLES** (pas Uranus/Neptune/Pluto comme maîtres)
2. **Vérifie TOUJOURS la radicalité** avant d'interpréter
3. **La Lune VOC = "rien ne se passe"** (sauf exceptions)
4. **Un seul thème par question** - pas de seconde chance si la réponse déplaît
5. **Le timing est APPROXIMATIF** - donne une fourchette, pas une date exacte
6. **Sois HONNÊTE** - si la réponse est NON, dis-le brutalement
7. **La dignité du significateur = l'état de la personne/chose** - crucial pour le contexte

---

**Retourne au [SKILL.md principal](../SKILL.md) pour workflow complet.**
