@login_required
def migrate_users():
    form = MigrateUsersForm()
    if request.method == "POST" and form.validate_on_submit():
        print("Here am i")
        '''multiselect = ', '.join(form.multiselect.data)
        multiselect_to = ', '.join(form.multiselect_to.data)
        print(multiselect)
        print(multiselect_to)'''
    return render_template('admin/migrate_users.html', form=form)