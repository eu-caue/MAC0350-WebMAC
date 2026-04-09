from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager
from sqlmodel import Session, select
from models import Problem, Category
from database import create_db_and_tables, engine
from typing import Optional
from sqlalchemy.orm import selectinload

def seed_database():
    with Session(engine) as session:
        existing = session.exec(select(Problem)).first()

        if existing:
            return

        strings = Category(name="Strings")
        dp = Category(name="Programação Dinâmica")

        session.add(strings)
        session.add(dp)
        session.commit()

        session.refresh(strings)
        session.refresh(dp)

        p1 = Problem(
            title="Palindrome Queries",
            difficulty="Difícil",
            statement="""Dado uma string inicial s e q queries com valores l e r, determine para cada query se a substring entre l e r é um palíndromo.
Restrições: |s| <= 10^5, q <= 10^5, 1 <= l, r <= |s|""",
            category_id=strings.id
        )

        p2 = Problem(
            title="Knapsack",
            difficulty="Médio",
            statement="""Um ladrão invade um museu e deseja roubar N itens. No entanto, sua mochila é limitada e consegue suportar no máximo W de peso.
Dado o valor v_i e o peso w_i de cada item, diga qual o maior valor que o ladrão consegue retirar em apenas uma viagem.
Restrições: 1 <= N, W, v_i, w_i <= 1000.""",
            category_id=dp.id
        )

        session.add(p1)
        session.add(p2)
        session.commit()

@asynccontextmanager
async def initFunction(app: FastAPI):
    # Executado antes da inicialização da API
    create_db_and_tables()
    seed_database()
    yield
    # Executado ao encerrar a API

app = FastAPI(lifespan=initFunction)

# Sintaxe recomendada: diretório como primeiro argumento posicional
templates = Jinja2Templates(directory="templates")

# Monta a pasta "static" na rota "/static"
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def index(request: Request, nome: Optional[str] = None, categoria: Optional[str] = None, dificuldade: Optional[str] = None):
    with Session(engine) as session:
        query = select(Problem).options(selectinload(Problem.category))

        if nome:
            query = query.where(Problem.title.like(f"%{nome}%"))

        if dificuldade:
            query = query.where(Problem.difficulty == dificuldade)

        if categoria:
            query = query.join(Category, Problem.category_id == Category.id).where(Category.name == categoria)
        
        problems = session.exec(query).all()
        categories = session.exec(select(Category).join(Problem, Problem.category_id == Category.id).distinct()).all()        
        # Selecionar apenas categorias que tenham algum problema associado atualmente

    return templates.TemplateResponse(request, "index.html", context={"problems": problems, "categories": categories, "nome": nome, "categoria": categoria, "dificuldade": dificuldade})

@app.get("/create", response_class=HTMLResponse)
@app.get("/create/{problem_id}", response_class=HTMLResponse)
def create(request: Request, problem_id: Optional[int] = None):
    problem = None

    if problem_id:
        with Session(engine) as session:
            problem = session.exec(select(Problem).where(Problem.id == problem_id).options(selectinload(Problem.category))).first()

    return templates.TemplateResponse(request=request, name="create.html", context={"problem": problem})

@app.delete("/deleteProblem", response_class=HTMLResponse)
def delete_problem(
    request: Request,
    id: int,
    nome: Optional[str] = None,
    categoria: Optional[str] = None,
    dificuldade: Optional[str] = None
):
    with Session(engine) as session:
        problem = session.get(Problem, id)

        if not problem:
            raise HTTPException(404, "Problema não encontrado")

        session.delete(problem)
        session.commit()

        query = select(Problem).options(selectinload(Problem.category))

        if nome:
            query = query.where(Problem.title.like(f"%{nome}%"))

        if dificuldade:
            query = query.where(Problem.difficulty == dificuldade)

        if categoria:
            query = query.join(Category).where(Category.name == categoria)

        problems = session.exec(query).all()
        categories = session.exec(select(Category).join(Problem, Problem.category_id == Category.id).distinct()).all()

    return templates.TemplateResponse(request, "index.html", context={"problems": problems, "categories": categories, "nome": nome, "categoria": categoria, "dificuldade": dificuldade})

@app.put("/updateProblem", response_class=HTMLResponse)
def update_problem(id: int = Form(...), title: str = Form(...), category_name: str = Form(...), difficulty: str = Form(...), statement: str = Form(...)):
    with Session(engine) as session:
        if not title.strip():
            raise HTTPException(400, "Título não pode ser vazio")

        if not category_name.strip():
            raise HTTPException(400, "Categoria não pode ser vazia")

        if not statement.strip():
            raise HTTPException(400, "Enunciado não pode ser vazio")

        problem = session.get(Problem, id)
        if not problem:
            raise HTTPException(404, "Problema não encontrado")
        
        category = session.exec(select(Category).where(Category.name == category_name)).first()

        if not category:
            category = Category(name=category_name)
            session.add(category)
            session.commit()
            session.refresh(category)

        problem.title = title
        problem.difficulty = difficulty
        problem.statement = statement
        problem.category_id = category.id

        session.commit()
        session.refresh(problem)

        return HTMLResponse(content=f"<p>Problema '{problem.title}' atualizado.</p>")
    
@app.post("/createProblem", response_class=HTMLResponse)
def create_problem(title: str = Form(...), category_name: str = Form(...), difficulty: str = Form(...), statement: str = Form(...)):
    with Session(engine) as session:
        if not title.strip():
            raise HTTPException(400, "Título não pode ser vazio")

        if not category_name.strip():
            raise HTTPException(400, "Categoria não pode ser vazia")

        if not statement.strip():
            raise HTTPException(400, "Enunciado não pode ser vazio")
        
        category = session.exec(select(Category).where(Category.name == category_name)).first()

        if not category:
            category = Category(name=category_name)
            session.add(category)
            session.commit()
            session.refresh(category)

        problem = Problem(
            title=title,
            difficulty=difficulty,
            statement=statement,
            category_id=category.id
        )

        session.add(problem)
        session.commit()
        session.refresh(problem)

        return HTMLResponse(content=f"<p>Problema '{problem.title}' criado.</p>")