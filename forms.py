class MigrateUsersForm(FlaskForm):
    multiselect = SelectMultipleField("Utilisateurs des anciennes campagne")
    multiselect_to = SelectMultipleField("Utilisateurs de la campagne en cours")
    submit = SubmitField('Valider')

    def __init__(self, *args, **kwargs):
        super(MigrateUsersForm, self).__init__(*args, **kwargs)
        self.multiselect.choices = [(s.id, s.nom_agent+" "+s.prenoms_agent) for s in (User.query.filter(User.id!=current_user.id, User.id.in_(db.session.query(Users_Campagne.users_id).join(Campagnes).filter(Users_Campagne.campagne_id==Campagnes.campagne_id, Campagnes.isActive==0))).order_by(User.nom_agent).all())]
        self.multiselect_to.choices = [(s.id, s.nom_agent+" "+s.prenoms_agent) for s in (User.query.filter(User.id!=current_user.id, User.id.in_(db.session.query(Users_Campagne.users_id).join(Campagnes).filter(Users_Campagne.campagne_id==Campagnes.campagne_id, Campagnes.isActive==1))).order_by(User.nom_agent).all())]