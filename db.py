import sqlite3


class Database:
    def __init__(self, db_file):
        self.conection = sqlite3.connect(db_file)
        self.cursor = self.conection.cursor()

    def add_user(self, user_id):
        with self.conection:
            self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))

    def user_exists(self, user_id):
        with self.conection:
            result = self.cursor.execute("SELECT * from users WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(result))

    def set_pole(self, user_id, pole):
        with self.conection:
            return self.cursor.execute("""UPDATE users SET game_pole = ? WHERE user_id = ?""", (pole, user_id,))

    def output_pole(self, user_id):
        with self.conection:
            change = self.cursor.execute("""SELECT game_pole from users WHERE user_id = ?""", (user_id,)).fetchall()
            for c in change:
                r = str(c[0])
                return r


class Database_settings:
    def __init__(self, db_file):
        self.conection = sqlite3.connect(db_file)
        self.cursor = self.conection.cursor()

    def add_all(self, user_id, mode_search, mode_page):
        with self.conection:
            self.cursor.execute("INSERT INTO users_settings (user_id, advanced_search, full_page) VALUES (?, ?, ?)", (user_id, mode_search, mode_page))

    def add_user(self, user_id):
        with self.conection:
            self.cursor.execute("INSERT INTO users_settings (user_id) VALUES (?)", (user_id,))

    def user_exists(self, user_id):
        with self.conection:
            result = self.cursor.execute("""SELECT * from users_settings WHERE user_id = ?""", (user_id,)).fetchall()
            return bool(len(result))

    def set_mode_search(self, user_id, mode):
        with self.conection:
            self.cursor.execute("""UPDATE users_settings SET advanced_search = ? WHERE user_id = ?""",(mode, user_id,))

    def give_mode_search(self, user_id):
        with self.conection:
            return self.cursor.execute("""SELECT advanced_search FROM users_settings WHERE user_id = ?""",
                                       (user_id,)).fetchall()[0][0]

    def set_mode_page(self, user_id, mode):
        with self.conection:
            self.cursor.execute("""UPDATE users_settings SET full_page = ? WHERE user_id = ?""", (mode, user_id,))

    def give_mode_page(self, user_id):
        with self.conection:
            return self.cursor.execute("""SELECT full_page FROM users_settings WHERE user_id = ?""",
                                       (user_id,)).fetchall()[0][0]