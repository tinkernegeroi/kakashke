# import uuid
# from datetime import datetime
#
# from pydantic import BaseModel, EmailStr
#
#
#
# class UserBase(BaseModel):
#
#
#
# class UserCreate(UserBase):
#     password: str | bytes
#
# class UserRead(UserBase):
#     id: uuid.UUID
#     created_at: datetime
#     updated_at: datetime
#
# class UserUpdate(UserBase):
#     email: EmailStr | None = None
#     status: StatusEnum | None = None
#     password: str | bytes | None = None
#
# class UserLogin(BaseModel):
#     email: EmailStr
#     password: str
