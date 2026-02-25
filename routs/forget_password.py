from my_app_ecommerce.models.users_model import LoginModel
from database.database_connection import mycursor, dbcon
from fastapi import APIRouter
import random
from email_service import send_email
from models.users_model import ForgetPasswordModel
router = APIRouter(prefix="/users", tags=["Auth"])

@router.post("/forgetpassword")
def forget_password(data: ForgetPasswordModel):  # نستخدم ForgetPasswordModel لأنو فيه user_email
    try:
        # 1) تحقق إذا الإيميل موجود
        sql = "SELECT * FROM users WHERE user_email=%s"
        val = (data.user_email,)
        mycursor.execute(sql, val)
        user = mycursor.fetchone()

        if not user:
            return {"state": "error", "message": "email not found"}

        # 2) توليد كود جديد
        verification_code = random.randint(10000, 99999)

        # 3) تحديث الكود في قاعدة البيانات
        sql = "UPDATE users SET user_verifycode=%s WHERE user_email=%s"
        val = (verification_code, data.user_email)
        mycursor.execute(sql, val)
        dbcon.commit()

        # 4) إرسال الكود عبر الإيميل
        send_email(
            to_email=data.user_email,
            subject="Reset Password Code",
            content=f"<h1>{verification_code}</h1>"
        )

        return {"state": "success", "message": "code sent"}

    except Exception as e:
        print("FORGET PASSWORD ERROR:", e)
        return {"state": "error", "message": "server error"}
