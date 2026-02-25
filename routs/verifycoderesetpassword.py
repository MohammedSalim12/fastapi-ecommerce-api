from database.database_connection import mycursor, dbcon
from fastapi import APIRouter
from models.users_model import VerifyCodeResetPasswordModel
 
router = APIRouter(prefix="/users", tags=["Auth"])
@router.post("/verifycoderesetpassword")
def verify_code(data: VerifyCodeResetPasswordModel):
    try:
        user_email = data.user_email
        verify_code = data.verify_code

        # 1) نجيب الكود من قاعدة البيانات
        sql = "SELECT user_verifycode FROM users WHERE user_email=%s"
        val = (user_email,)
        mycursor.execute(sql, val)
        user = mycursor.fetchone()

        # 2) إذا الإيميل غير موجود
        if not user:
            return {"state": "error", "message": "email not found"}

        # 3) مقارنة الكود
        if str(user[0]) != str(verify_code):
            return {"state": "error", "message": "wrong code"}

        # 4) الكود صحيح
        return {"state": "success", "message": "code verified"}

    except Exception as e:
        print("VERIFY CODE ERROR:", e)
        return {"state": "error", "message": "server error"}
