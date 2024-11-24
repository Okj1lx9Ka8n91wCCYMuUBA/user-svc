from fastcrud import FastCRUD
from ...models.parsed_data.grant import Grant
from ...schemas.parsed_data.grant import GrantCreate, GrantUpdate, GrantUpdateInternal, GrantDelete

CRUDGrant = FastCRUD[
    Grant,
    GrantCreate,
    GrantUpdate,
    GrantUpdateInternal,
    GrantDelete
]
crud_grant = CRUDGrant(Grant)
