import functools
# atribuir permissoes consoante o tipo de user
user = {"username": "Jose", "access_level": "user"}
# user = {"username": "jose", "access_level": "admin"}


def make_secure(access_level):      # Permite passar parametros nos decoradores
    def decorator(func):            # Decorador simples de permissoes
        @functools.wraps(func)      # Mantem a documentacao e nome da funcao com @make_secure
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No admin permission for {user['username']}"
        return secure_function
    return decorator


@make_secure("admin")
def get_admin_password():
    return "admin: 1234"


@make_secure("user")
def get_dashboard_password():
    return "user: user_password"


##get_admin_password = make_secure(get_admin_password())
print(get_admin_password())
print(get_dashboard_password())


user = {"username": "Jose", "access_level": "admin"}

print(get_admin_password())
print(get_dashboard_password())
