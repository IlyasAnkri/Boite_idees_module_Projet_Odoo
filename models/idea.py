from odoo import models, fields, api

class IdeaBox(models.Model):
    _name = "idea.box"
    _description = "Boîte à Idées"

    name = fields.Char(string="Titre de l'idée", required=True)
    author = fields.Char(string="Auteur", required=True)
    
    category = fields.Selection([
        ('office', 'Amélioration Bureau'),
        ('tech', 'Technologie'),
        ('fun', 'Loisirs & Détente'),
        ('hr', 'Ressources Humaines')
    ], string="Catégorie", required=True)

    submission_date = fields.Date(string="Date", default=fields.Date.context_today)
    vote_count = fields.Integer(string="Votes", default=0, readonly=True) # Readonly pour empêcher la triche manuelle

    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('confirmed', 'Confirmée'),
        ('done', 'Réalisée'),
        ('cancelled', 'Annulée')
    ], string="Statut", default='draft', group_expand='_expand_states')

    description = fields.Text(string="Détails")
    
    # --- CRÉATIVITÉ : Fonctions pour les boutons ---
    
    def action_vote(self):
        """Ajoute +1 vote quand on clique sur le bouton"""
        for rec in self:
            rec.vote_count += 1

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancelled'

    # --- CRÉATIVITÉ : Pour afficher toutes les colonnes Kanban même si vides ---
    @api.model
    def _expand_states(self, states, domain, order):
        return [key for key, val in type(self).state.selection]