
if __name__ == '__main__':
    app.run()

# from matcha import models, routes, forms

# with app.app_context():
#     @app.before_request
#     def before_request():
#         g.db = connect_db()
#
#
#     @app.teardown_request
#     def tear_down_request(exception):
#         if hasattr(g, 'db'):
#             g.db.close()
#
#
#     def query_db(query, args=(), one=False):
#         cur = g.db.execute(query, args)
#         rv = [dict((cur.desciption[idx][0], value)
#                    for idx, value in enumerate(row)) for row in cur.fetchall()]
#         return (rv[0] if rv else None) if one else rv
#
#
#     for user in query_db("SELECT * FROM users"):
#         print(f"'{user['username']}', '{user['email']}'")
