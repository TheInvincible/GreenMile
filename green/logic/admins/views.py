# import os
# from flask import Flask
# from flask_admin import Admin, BaseView, expose

# from . import admins
# from ... import create_app, db
# from ...models import User

# class AdminView(BaseView):
#     @expose('/')
#     def dashboard():
#         return render_template('/home/dashboard.html')

# def create_users():
# 	with app.app_context():
# 		db.metadata.create_all(db.engine)
# 		if User.query.all():
# 			print('A user already exists! Create another? (y/n):'),
# 			create = input()
# 			if create == 'n':
# 				return

# 			print('Enter username: '),
# 			email = input()
# 			password = getpass()
# 			assert password == getpass('Confirm password: ')

# 			user = User(
# 				username=username,
# 				password=bcrypt.generate_pass_hash(password))
# 			db.session.add(user)
# 			db.session.commit()
# 			print('User added')


# if __name__ == '__main__':
# 	sys.exit(main())