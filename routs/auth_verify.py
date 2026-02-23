from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database.database_connection import mycursor, dbcon   # تأكد من المسار الصحيح

router = APIRouter()

class VerifyCodeModel(BaseModel):
    user_email: str
    verify_code: int

@router.post("/users/verify")
def verify_user_code(data: VerifyCodeModel):
    # 1) جلب الكود الحقيقي من قاعدة البيانات
    sql = "SELECT user_verifycode FROM users WHERE user_email = %s"
    val = (data.user_email,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if not result:
        raise HTTPException(status_code=404, detail="User not found")

    real_code = result[0]

    # 2) مقارنة الكود
    if real_code != data.verify_code:
        raise HTTPException(status_code=400, detail="Invalid verification code")

    # 3) تحديث حالة المستخدم
    update_sql = "UPDATE users SET user_approve = 1 WHERE user_email = %s"
    mycursor.execute(update_sql, val)
    dbcon.commit()

    return {"status": "success", "message": "User verified successfully"}
