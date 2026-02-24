from fastapi import APIRouter
from models.users_model import SignupModel, LoginModel
from database.database_connection import mycursor, dbcon
from email_service import send_email
import random

router = APIRouter(prefix="/users", tags=["Auth"])


@router.post("/signup")
def create_users(users: SignupModel):
    # 1) توليد كود عشوائي
    verification_code = random.randint(10000, 99999)

    sql = """
        INSERT INTO users (user_name, user_email, user_password, user_phone, user_verifycode)
        VALUES (%s, %s, %s, %s, %s)
    """

    val = (
        users.user_name,
        users.user_email,
        users.user_password,
        users.user_phone,
        verification_code
    )

    mycursor.execute(sql, val)
    dbcon.commit()

    # 2) إرسال الكود عبر الإيميل
    send_email(
        to_email=users.user_email,
        subject="Your Verification Code",
        content=f"<h1>{verification_code}</h1>"
    )

    return {"state": "success", "message": "insert successfully"}


@router.post("/login")
def login(data: LoginModel):
    try:
        print("LOGIN DATA:", data)

        sql = "SELECT * FROM users WHERE user_email=%s AND user_approve=1"
        val = (data.user_email,)
        mycursor.execute(sql, val)
        user = mycursor.fetchone()

        print("USER ROW:", user)

        if not user:
            return {"state": "error", "message": "email not found"}

        print("PASSWORD IN DB:", user[2])
        print("PASSWORD SENT:", data.user_password)

        if user[2] != data.user_password:
            return {"state": "error", "message": "wrong password"}

        return {
            "state": "success",
            "message": "login successful",
            "user_id": user[0],
            "user_name": user[1],
            "user_email": user[3],
            "user_phone": user[4]
        }

    except Exception as e:
        print("LOGIN ERROR:", e)
        return {"state": "error", "message": "server error"}

