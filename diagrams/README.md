# Diagrammes UML - Boîte à Idées

Ce dossier contient les diagrammes UML du module "Boîte à Idées" d'Odoo.

## Fichiers

### 1. use_case_diagram.puml
**Diagramme de Cas d'Utilisation**
- Acteurs: Utilisateur et Administrateur
- Cas d'utilisation principaux:
  - Créer une idée
  - Voter pour une idée
  - Consulter les idées
  - Modifier une idée
  - Changer le statut d'une idée
  - Voir les statistiques
  - Gérer les catégories

### 2. sequence_diagram.puml
**Diagramme de Séquence**
- Montre le flux d'interactions pour:
  - La création d'une nouvelle idée
  - Le processus de vote
- Participants: Utilisateur, Interface Web, Contrôleur Odoo, Modèle, Base de Données

### 3. class_diagram.puml
**Diagramme de Classes**
- Classe principale: IdeaBox (modèle Odoo)
- Classes liées: vues, actions, permissions
- Relations entre les composants du module

## Comment visualiser les diagrammes

Pour visualiser ces diagrammes PlantUML:

1. Installer une extension PlantUML dans votre éditeur (VS Code, IntelliJ, etc.)
2. Ou utiliser un outil en ligne comme [PlantUML Online](https://plantuml.com/)
3. Ou installer PlantUML localement et utiliser la commande:
   ```bash
   plantuml diagram.puml
   ```

## Description fonctionnelle

Le module "Boîte à Idées" permet:
- De proposer des idées innovantes dans différentes catégories
- De voter pour les idées proposées
- De suivre l'évolution des idées (brouillon → confirmé → réalisé)
- De visualiser des statistiques par catégorie
- D'utiliser différentes vues (kanban, liste, formulaire, graphique)