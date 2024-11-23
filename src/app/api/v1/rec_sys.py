from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from ...core.db.database import SessionLocal
from ...models.startup import Startup
from ...models.program import Program
from ...schemas.startup import StartupCreate, StartupRead, StartupUpdate, StartupDelete
from fastcrud import FastCRUD
from sentence_transformers import SentenceTransformer, util
import pandas as pd

app = FastAPI()

CRUDStartup = FastCRUD[
    Startup,
    StartupCreate,
    StartupUpdate,
    StartupRead,
    StartupDelete
]
crud_startup = CRUDStartup(Startup)

def find_top_grants_for_startup(startup, grants):
    """
    This function finds the top 5 grants that are most similar to a given startup based on their descriptions.
    It uses the SentenceTransformer model to generate embeddings for both the startup and grants,
    and then calculates the cosine similarity between them.

    Parameters:
    startup (dict): A dictionary containing the startup's information, with 'Описание' as a key for the description.
    grants (list): A list of dictionaries, where each dictionary represents a grant and contains 'title', 'url', and 'description' keys.

    Returns:
    list: A list of dictionaries, where each dictionary represents a top grant and contains 'title', 'url', 'description', and 'similarity' keys.
    """
    model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')

    startup_embedding = model.encode(startup['Описание'], convert_to_tensor=True)
    grant_embeddings = model.encode([grant['description'] for grant in grants], convert_to_tensor=True)

    similarities = util.pytorch_cos_sim(startup_embedding, grant_embeddings).squeeze()

    top_k = similarities.topk(5)
    top_grants = []
    for idx, similarity in zip(top_k.indices, top_k.values):
        grant = grants[idx]
        top_grants.append({
            'title': grant['title'],
            'url': grant['url'],
            'description': grant['description'],
            'similarity': round(similarity.item(), 4)
        })

    return top_grants


@app.get("/rec_sys/{startup_id}")
def update_startup(startup_id: int, startup: StartupUpdate, db: Session = SessionLocal()):
    startup = crud_startup.read(startup_id, db)
    if not startup:
        raise HTTPException(status_code=404, detail="Startup not found")

    grants = db.query(Program).all()
    if not grants:
        raise HTTPException(status_code=404, detail="No grants available")

    recommended_grants = find_top_grants_for_startup(startup.description, grants)
    return {
        "startup": startup.startup_id,
        "recommended_grants": recommended_grants
    }