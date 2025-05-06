from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from webapp.models.newsmodels import NewsItem
from webapp.models.modelmanager import FakeNewsModelManager
from config import models_isot_path
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="webapp/templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


model_manager = FakeNewsModelManager(
    model_paths={
        "logistic_regression": f"{models_isot_path}/logistic_regression.pkl",
        "svc_linear_kernel": f"{models_isot_path}/svc_linear_kernel.pkl",
        "random_forest": f"{models_isot_path}/random_forest.pkl",
        "naive_bayes": f"{models_isot_path}/naive_bayes.pkl",
        "bi_lstm": f"{models_isot_path}/bi_lstm.h5",
        "lstm": f"{models_isot_path}/lstm.h5",
        "gru": f"{models_isot_path}/gru.h5",
    },
    vectorizer_path=f"{models_isot_path}/tokenizer_isot.joblib"
)

def result_serializer(model, result) -> dict:
    if isinstance(result, tuple):
        return {
        "model": str(model),
        "model_output": str(result[0][0][0]),
        "prediction": str(result[1])
    }
    
    return {
            "model": str(model),
            "prediction": str(result)
        }


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
def predict_news(req: NewsItem):
    try:
        result = model_manager.predict(req.text, req.model)
        return result_serializer(req.model, result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

