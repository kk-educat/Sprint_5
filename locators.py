# локаторы для тестирования регистрации
REGISTRATION_NAME_FIELD = "//div[contains(@class, 'input') and .//label[text()='Имя']]//input"
REGISTRATION_MAIL_FIELD = "//div[contains(@class, 'input') and .//label[text()='Email']]//input"
REGISTRATION_PSWD_FIELD = "//input[@name='Пароль']"
REGISTRATION_BUTTON = "//button[text()='Зарегистрироваться']"
REGISTRATION_WRONG_PSWD_MSG = "//p[text()='Некорректный пароль']"

# локаторы для тестирования входа в аккаунт и перехода в личный кабинет
SIGN_IN_MAIL_FIELD = "//input[@name='name']"
SIGN_IN_PSWD_FIELD = "//input[@name='Пароль']"
SIGN_IN_BUTTON = "//button[text()='Войти']"
CREATE_ORDER_BUTTON = "//button[text()='Оформить заказ']"
SIGN_IN_INTO_ACCOUNT_BUTTON = "//button[text()='Войти в аккаунт']"
PERSONAL_CABINET_BUTTON = "//a[@href='/account']"

# локаторы для тестирования перехода в конструктор
CONSTRUCTOR_LINK = "//p[text()='Конструктор']/.."
CONSTRUCTOR_HEADER = "//h1[text()='Соберите бургер']"
LOGO_LINK = "//div[contains(@class, 'AppHeader_header__logo')]/a"

# локатор для тестирования выхода по кнопке Выйти
EXIT_BUTTON = "//button[text()='Выход']"

# локаторы для тестирования переходов к разделам конструктора
BUNS_SECTION = "//span[text()='Булки']"
SAUCES_SECTION = "//span[text()='Соусы']"
FILLINGS_SECTION = "//span[text()='Начинки']"
# локатор активного раздела конструктора, где section_name может принимать 1 из значений: Булки, Соусы, Начинки
ACTIVE_SECTION = "//div[contains(@class, 'tab_tab_type_current') and .//span[text()='{section_name}']]"
