from fastapi import APIRouter, HTTPException
#from database.database_connection import mycursor, dbcon


# نحدد الراوتر ومساره الأساسي
router = APIRouter(prefix="/users", tags=["Users"])


# ---------------------------------------------------------
# 1) جلب كل المستخدمين
# ---------------------------------------------------------
@router.get("/")
def get_all_users():
    sql = "SELECT * FROM users"
    mycursor.execute(sql)
    users = mycursor.fetchall()
    return users


# ---------------------------------------------------------
# 2) جلب مستخدم واحد حسب ID
# ---------------------------------------------------------
@router.get("/{user_id}")
def get_user_by_id(user_id: int):
    sql = "SELECT * FROM users WHERE id=%s"
    #mycursor.execute(sql, (user_id,))
    #user = mycursor.fetchone()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


# ---------------------------------------------------------
# 3) حذف مستخدم حسب ID
# ---------------------------------------------------------
@router.delete("/{user_id}")
def delete_user(user_id: int):
    sql = "DELETE FROM users WHERE id=%s"
    #mycursor.execute(sql, (user_id,))
    #dbcon.commit()

    return {"state": "success", "message": "User deleted successfully"}


# ---------------------------------------------------------
# 4) تحديث بيانات مستخدم (اختياري)
# ---------------------------------------------------------
@router.put("/{user_id}")
def update_user(user_id: int, data: dict):
    sql = """
        UPDATE users 
        SET user_name=%s, user_email=%s, user_phone=%s 
        WHERE id=%s
    """
    val = (data["user_name"], data["user_email"], data["user_phone"], user_id)

   # mycursor.execute(sql, val)
  #  dbcon.commit()

    return {"state": "success", "message": "User updated successfully"}
