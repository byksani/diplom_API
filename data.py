class Urls:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api"
    REGISTER = f"{BASE_URL}/auth/register"
    LOGIN = f"{BASE_URL}/auth/login"
    USER = f"{BASE_URL}/auth/user"
    ORDERS = f"{BASE_URL}/orders"

class Ingredients:
    DEFAULT_INGREDIENTS = ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa6f']
    INVALID_INGREDIENTS = ['61c0c5a71d1f82001bdooo6d', '61c0c5a71d1f82001bdnnn6f']

class SystemMessages:
    UNAUTHORIZED = "You should be authorised"
    USER_ALREADY_EXISTS = "User already exists"
    REQUIRED_FIELDS_MISSING = "Email, password and name are required fields"
    INVALID_EMAIL_OR_PASSWORD = "email or password are incorrect"
