from fastcrud import FastCRUD
from ...models.docs.passport import Passport
from ...schemas.docs.passport import PassportCreate, PassportUpdate, PassportDelete

CRUDPassport = FastCRUD[
    Passport,
    PassportCreate,
    PassportUpdate,
    PassportUpdate,
    PassportDelete
]
crud_passport = CRUDPassport(Passport)
