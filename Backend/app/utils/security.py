from passlib.context import CryptContext
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)
def hash_password(password: str) -> str:
    """
    Converts a plain-text password into a secure hashed password.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies whether the entered password matches the stored hashed password.
    """
    return pwd_context.verify(plain_password, hashed_password)