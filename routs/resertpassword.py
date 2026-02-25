from database.database_connection import mycursor, dbcon
from fastapi import APIRouter
from models.users_model import VerifyCodeResetPasswordModel

router = APIRouter(prefix="/users", tags=["Auth"])

@router.post("/resetpassword")
def reset_password(data: VerifyCodeResetPasswordModel):
    try:
        user_email = data.user_email
        new_password = data.new_password

        # تحديث كلمة المرور
        sql = "UPDATE users SET user_password=%s WHERE user_email=%s"
        val = (new_password, user_email)
        mycursor.execute(sql, val)
        dbcon.commit()

        return {"state": "success", "message": "password updated"}

    except Exception as e:
        print("RESET PASSWORD ERROR:", e)
        return {"state": "error", "message": "server error"}
