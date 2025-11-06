# 🔮 Astrologue IA - Skill Complet d'Astrologie

**Expert astrologique brutal et transparent pour Claude Code**

Version 1.0.0 - Créé le 30 janvier 2025

---

## 📋 Vue d'ensemble

Ce skill transforme Claude en expert astrologique capable d'analyser :
- ✅ **Thèmes nataux complets** (stelliums, aspects, maisons, patterns)
- ✅ **Synastrie / Compatibilité** (scores /10, red flags, comparaison multiple)
- ✅ **Transits et prévisions** (dates clés, timing optimal, événements astro)
- ✅ **Astrocartographie** (meilleurs lieux de vie, scores par ville)

**Style unique** : Brutal, direct, zéro bullshit, full transparence (niveau 10/10)

---

## 🚀 Comment utiliser ce skill

### Méthode 1 : Invocation automatique

Claude détecte automatiquement quand utiliser ce skill basé sur ta requête :

```
"Peux-tu analyser mon thème natal ? 14.11.1994, 13h04, Nice"
→ Claude utilise automatiquement le skill astrologue-ia
```

### Méthode 2 : Invocation explicite (si supporté)

```
/astrologue-ia
```

---

## 📚 Structure du skill

```
astrologue-ia/
├── SKILL.md                    # Point d'entrée principal
├── README.md                   # Ce fichier
│
├── guides/                     # Méthodologies complètes
│   ├── natal-chart.md          # 6000+ mots - Analyse thème natal
│   ├── synastrie.md            # 8000+ mots - Compatibilité
│   ├── transits.md             # 10000+ mots - Prévisions/timing
│   └── astrocartographie.md    # 7000+ mots - Meilleurs lieux
│
├── reference/                  # Base de connaissance
│   └── planets-in-signs.md     # Interprétations planètes × signes
│
└── examples/                   # Analyses réelles
    └── [à venir]
```

**Total : ~45 000 mots d'expertise astrologique**

---

## 🎯 Types d'analyses disponibles

### 1. Thème Natal Complet

**Quand l'utiliser** : Compréhension de soi, analyse personnalité, mission de vie

**Ce que tu obtiens** :
- Big 3 (Sun/Moon/ASC) avec interprétation profonde
- Stelliums et dominantes planétaires
- Toutes les planètes en signes + maisons
- Aspects majeurs avec significations
- Patterns spéciaux (Grand Trigone, T-Square, Yod, etc.)
- Synthèse personnalité, amour, carrière, spiritualité
- Red flags personnels à surveiller
- Mission de vie et challenges

**Exemple de requête** :
```
"Analyse mon thème natal complet : 14.11.1994, 13h04, Nice, France.
Mode brutal niveau 10, je veux la vérité sans filtre."
```

---

### 2. Synastrie / Compatibilité

**Quand l'utiliser** : Compatibilité amoureuse/amicale, choisir entre plusieurs partenaires

**Ce que tu obtiens** :
- Score de compatibilité /10 avec justification complète
- Inter-aspects majeurs (Sun-Sun, Venus-Mars, Moon-Moon, etc.)
- Zones d'harmonie (aspects positifs)
- Zones de friction (aspects difficiles)
- Red flags et green flags relationnels
- Timing optimal de rencontre
- Scénario probable de la relation (phases)
- **Si plusieurs partenaires** : Classement avec comparaison

**Exemple de requête simple** :
```
"Suis-je compatible avec cette personne ?
Moi : 14.11.1994, 13h04, Nice
Elle : 22.11.1996, 14h10, Firminy
Mode brutal, pas de complaisance."
```

**Exemple comparaison multiple** :
```
"Compare ma compatibilité avec ces 3 personnes et classe-les.
Moi : 14.11.1994, 13h04, Nice
A : 27.07.1995, 3:00, Nice
B : 10.02.1995, 5:17, Karlsruhe, Allemagne
C : 22.11.1996, 14:10, Firminy
Qui est la meilleure ? Mode brutal."
```

---

### 3. Transits & Prévisions

**Quand l'utiliser** : Timing de décisions, prévisions, dates favorables/à éviter

**Ce que tu obtiens** :
- Calendrier chronologique de TOUS les événements astro
- Transits planétaires majeurs (Saturn, Jupiter, Uranus, Neptune, Pluton)
- Éclipses et leur impact
- Rétrogrades (Mercury, Venus, Mars)
- Nouvelles/Pleines Lunes importantes
- Révolution solaire (si période inclut anniversaire)
- Conjonctions rares (ex: Saturn-Neptune Feb 2026)
- Périodes favorables/difficiles par domaine
- Top 5 dates game-changer
- Lucky days (si demandé pour jeux)

**Exemple de requête** :
```
"Quels sont les transits importants pour moi en 2026 ?
14.11.1994, 13h04, Nice
Je veux les dates exactes et ce qui va se passer."
```

---

### 4. Astrocartographie

**Quand l'utiliser** : Déménagement, choix de lieu de vie, relocation

**Ce que tu obtiens** :
- Explication des lignes planétaires (Jupiter MC/IC, Sun IC, etc.)
- Top 10 meilleurs lieux de vie avec scores /10
- Pays/villes compatibles selon dominante du thème
- Lieux à éviter (Saturn ASC, Mars ASC, etc.)
- Récap par objectif (carrière, amour, spiritualité, etc.)
- Timing optimal pour déménagement
- Détails pratiques (coût vie, climat, langue)

**Exemple de requête** :
```
"Où devrais-je vivre astrologiquement ?
14.11.1994, 13h04, Nice
Donne-moi le top 10 des meilleurs lieux avec scores."
```

---

## 🔥 Ce qui rend ce skill unique

### 1. Style BRUTAL (niveau 10/10)

Pas de bullshit positif générique :

❌ **Autres astrologues** : "Tu as un grand potentiel d'amour dans ton thème"
✅ **Ce skill** : "Venus rétro Scorpio = l'amour c'est compliqué pour toi, accepte-le"

❌ **Autres** : "Tu pourrais avoir des challenges relationnels"
✅ **Ce skill** : "Moon carré Moon = vos besoins émotionnels sont incompatibles, ça va planter"

### 2. Scores chiffrés justifiés

Toutes les compatibilités ont un score /10 avec formule de calcul :
```
Score 8.6/10 =
  +3.0 (Moon conj Moon Aries - RARE!)
  +2.5 (MC conj MC Sagittarius)
  +2.0 (Venus trine)
  -0.5 (Venus neutral)
  +1.5 (autres aspects)
  = 8.6/10 → FONCEZ
```

### 3. Comparaison multiple de partenaires

Peut comparer jusqu'à 10 partenaires et les classer :
- Candidate M : 8.6/10 - FONCEZ
- Candidate A : 7.25/10 - POSSIBLE
- Candidate N : 6.6/10 - FUYEZ (répète pattern ex)

### 4. Timing ultra-précis

Pas "bientôt" mais **"19 novembre 2025, Nouvelle Lune Scorpio = GO TIME"**

### 5. Fetch automatique

Le skill va chercher les données sur astro-seek.com automatiquement

### 6. Base de connaissance massive

45 000+ mots d'expertise incluant :
- Toutes les interprétations planètes × signes
- Méthodologie complète de scoring synastrie
- Transits des planètes lentes expliqués
- Astrocartographie mondiale

---

## 📊 Exemples de résultats

### Scores de synastrie obtenus dans session originale

**Comparaison de 3 candidates** (user né 14.11.1994) :

| Candidate | Score | Verdict | Raison principale |
|-----------|-------|---------|-------------------|
| **M** | **8.6/10** | **FONCEZ** 🔥 | Moon conj Moon Aries (RARE!) + MC conj MC |
| **A** | 7.25/10 | POSSIBLE ⚠️ | Venus trine, mais Sun square Sun |
| **N** | 6.6/10 | FUYEZ ❌ | Sun square Sun répète pattern ex |

### Insights brutaux typiques

> "Tu as 5 planètes en Scorpio = intensité MAXIMALE. T'es pas faite pour les petites natures."

> "Moon Aries + Stellium Scorpio = PARADOXE : tu veux indépendance ET fusion. Bonne chance."

> "Venus rétrograde = tu testes toujours l'amour. En oct-nov 2026, si elle RESTE = c'est la bonne."

### Prévisions timing

> "19-20 novembre 2025 (Nouvelle Lune Scorpio) = GO TIME pour premier move."

> "20 février 2026 : Saturn conj Neptune à 0° Aries sur ta Moon = RENCONTRE KARMIQUE. Arrive tous les 36 ans."

> "Octobre 2026 Venus rétro Scorpio = TEST du couple. Si ça survit = relation solide."

---

## ⚙️ Configuration

Le skill est configuré pour :
- **Niveau de brutalité** : 10/10 (maximum)
- **Niveau de détail** : Ultra (analyses complètes)
- **Langue** : Français (mais peut être changé)
- **Fetch automatique** : Activé (astro-seek.com, cafeastrology.com)

**Permissions requises** :
- WebFetch (pour récupérer données astro)
- WebSearch (pour éphémérides)
- Read, Grep, Glob (pour lire les guides/références)
- TodoWrite (pour tracker les analyses multi-steps)

---

## 🎓 Méthodologie

### Basé sur session réelle (Nov 2024)

Ce skill encapsule 15+ heures d'analyse approfondie incluant :
- Thème natal avec Scorpio stellium (5 planètes)
- Synastrie comparative de 3 partenaires
- Transits majeurs 2025-2026 (Saturn-Neptune Feb 2026)
- Astrocartographie mondiale (Istanbul, Marrakech, etc.)
- Timing relationnel ultra-précis

### Astrologie tropicale occidentale

- Système **Placidus** pour les maisons
- Astrologie **tropicale** (pas védique/siderale)
- Orbes standards : ±8° conjonctions, ±7° carrés, ±8° trigones
- Sources : astro-seek.com, cafeastrology.com, astrotheme.com

---

## 🚨 Disclaimers importants

⚠️ **L'astrologie est un OUTIL, pas une prison**

- Le libre arbitre existe toujours
- Ces analyses sont basées sur patterns énergétiques
- Toujours vérifier avec ton ressenti personnel
- Le thème = MENU D'OPTIONS, pas destin fixe

⚠️ **Mode brutal = vérité crue**

- Peut être inconfortable
- C'est VOULU pour maximiser l'honnêteté
- Pas de complaisance excessive
- Mais jamais méchant : vérité pour AIDER

⚠️ **Domaine limité**

- Astrologue, pas psychologue/médecin
- Si issue clinique (dépression, etc.), consulter un pro
- Ne remplace pas thérapie ou médecine

---

## 🔧 Dépannage

### Claude n'utilise pas le skill ?

**Vérifications** :
1. Le dossier `.claude/skills/astrologue-ia/` existe ?
2. Le fichier `SKILL.md` est présent ?
3. Ta requête mentionne l'astrologie / thème natal / compatibilité ?

**Essaye** :
```
"Utilise le skill astrologue-ia pour analyser mon thème : [données]"
```

### Le fetch échoue ?

Le skill a des fallbacks :
1. Essaye astro-seek.com
2. Si échec, essaye cafeastrology.com
3. Si tout échoue, demande données manuelles

### Erreur de permission ?

Assure-toi que WebFetch/WebSearch sont autorisés dans tes settings Claude Code.

---

## 📖 Pour aller plus loin

### Lire les guides complets

- [guides/natal-chart.md](guides/natal-chart.md) - Méthodologie thème natal
- [guides/synastrie.md](guides/synastrie.md) - Méthodologie compatibilité
- [guides/transits.md](guides/transits.md) - Méthodologie prévisions
- [guides/astrocartographie.md](guides/astrocartographie.md) - Méthodologie lieux

### Consulter les références

- [reference/planets-in-signs.md](reference/planets-in-signs.md) - Toutes les interprétations

---

## 🎯 Cas d'usage typiques

### 1. Connaissance de soi
```
"Analyse mon thème natal complet, mode ultra-détaillé et brutal."
```

### 2. Compatibilité amoureuse
```
"Suis-je compatible avec [données partenaire] ? Pas de complaisance."
```

### 3. Timing optimal pour action
```
"Quelle est la meilleure période en 2026 pour [action] selon mon thème ?"
```

### 4. Choix de relocation
```
"Où devrais-je déménager pour maximiser mon thème ?"
```

### 5. Analyse complète (tout en un)
```
"Fais-moi une analyse ultra-complète : natal + compatibilité avec [X] +
transits 2026 + meilleurs lieux de vie. Mode brutal maximum."
```

---

## 🏆 Crédits

**Créé par** : Session IA Astrologie (Nov 2024 - Jan 2025)
**Expertise** : 15+ heures d'analyse approfondie
**Base** : Thème natal 14.11.1994, synastrie comparative, Saturn-Neptune 2026
**Version** : 1.0.0
**Date** : 30 janvier 2025

---

## 📞 Support

Le skill est auto-documenté et autonome.

Si problème :
1. Lis le [SKILL.md](SKILL.md) principal
2. Consulte les guides dans `guides/`
3. Vérifie les permissions WebFetch/WebSearch
4. Reformule ta requête pour être plus explicite

---

**Enjoy le skill, et que les astres te guident ! 🔮✨**

*"Pas de bullshit, que la vérité brute."* - Astrologue IA
