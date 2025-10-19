# 🧱 Proyecto `kit_utiles`
### Repositorio de utilidades en Python con CI/CD, tests y cobertura automática

![CI](https://github.com/<USUARIO>/<REPO>/actions/workflows/ci.yml/badge.svg)

---

## 📘 Descripción general

`kit_utiles` es un paquete educativo desarrollado en el marco de la asignatura **Programación e Inteligencia Artificial / Entornos de Desarrollo**.  
El objetivo es aplicar buenas prácticas de **desarrollo profesional en Python**, incorporando:

- Estructura modular con `src/`
- Tests automatizados (20 casos)
- Cobertura de código con `pytest-cov`
- Integración continua con **GitHub Actions**
- Control de versiones con **Git y Git LFS**

---

## 🧩 Fases del proyecto

| Fase | Contenido | Resultado principal |
|------|------------|---------------------|
| **Fase 1** | Creación del paquete `kit_utiles` con módulos `strings`, `numbers`, `files`, `cli`. | Código funcional en `src/kit_utiles/`. |
| **Fase 2** | Implementación y ampliación de tests (E01–E20). | Carpeta `/tests` con 20 pruebas automatizadas. |
| **Fase 3** | Configuración de **Git LFS** para ficheros grandes (`data/`, `models/`). | `.gitattributes` y LFS activo. |
| **Fase 4** | Integración Continua (CI/CD) con **GitHub Actions**. | Pipeline que ejecuta tests y mide cobertura (mínimo 80%). |

---

## 🧱 Estructura del proyecto

```
kit_utiles/
├─ src/
│  └─ kit_utiles/
│     ├─ __init__.py
│     ├─ strings.py
│     ├─ numbers.py
│     ├─ files.py
│     └─ cli.py
├─ tests/
│  ├─ conftest.py
│  ├─ test_e01_...py
│  ├─ ...
│  └─ test_e20_grade_edges_more.py
├─ .github/
│  └─ workflows/
│     └─ ci.yml
├─ .coveragerc
├─ pyproject.toml
├─ requirements.txt
├─ README.md
└─ .gitattributes
```

---

## ⚙️ Instalación local

```bash
# 1️⃣ Clona el repositorio
git clone https://github.com/<USUARIO>/<REPO>.git
cd kit_utiles

# 2️⃣ Crea y activa entorno virtual
python -m venv .venv
source .venv/bin/activate    # En Windows: .venv\Scripts\activate

# 3️⃣ Instala dependencias
pip install -r requirements.txt

# 4️⃣ (Opcional) Instala el paquete en modo editable
pip install -e .
```

---

## 🧪 Ejecución de tests

Ejecuta todos los tests:

```bash
pytest
```

### Con cobertura de código
```bash
pytest --cov=src/kit_utiles --cov-report=term-missing
```

### Generar informe HTML de cobertura
```bash
coverage html
start htmlcov/index.html   # Abre el informe en el navegador
```

---

## 🧰 Cobertura mínima exigida

El proyecto requiere una **cobertura ≥ 80%**.  
El control se aplica automáticamente en **GitHub Actions** mediante:

```bash
pytest --cov=src/kit_utiles --cov-fail-under=80
```

Archivo `.coveragerc`:

```ini
[run]
branch = True
source = src/kit_utiles
omit = tests/*
```

---

## 🧩 CI/CD con GitHub Actions

El flujo de integración continua está definido en:

```
.github/workflows/ci.yml
```

### 🚀 Qué hace automáticamente el pipeline:
1. Instala Python 3.11  
2. Instala dependencias (`pytest`, `pytest-cov`, `coverage`)  
3. Ejecuta todos los tests (`pytest`)  
4. Falla si la cobertura < 80%  
5. Genera y sube los artefactos `coverage-html` y `coverage.xml`

### ✅ Activación automática
Solo tienes que subir (`git push`) el archivo `ci.yml`.  
GitHub lo detecta sin configuración adicional.

Accede a los resultados desde la pestaña **Actions** del repositorio.

---

## 🧠 Tests automáticos incluidos (E01–E20)

| Grupo | Módulo | Ejemplos de funciones testeadas |
|--------|---------|--------------------------------|
| **Strings** | `strings.py` | `normalize_whitespace`, `is_palindrome`, `join_chars`, `snake_to_camel`, `word_count`, `validate_email` |
| **Numbers** | `numbers.py` | `sum_list`, `unique_sorted`, `safe_divide`, `mean`, `grade`, `clamp` |
| **Files** | `files.py` | `save_lines`, `load_lines`, `file_size`, `read_lines` |
| **CLI** | `cli.py` | `main(argv)` con CSV vacío, con espacios y mixto |

📋 Los tests están ubicados en `tests/` y cubren los **20 escenarios funcionales**, incluyendo casos límite y errores esperados.

---

## 📊 Resultados y cobertura

Tras ejecutar los tests localmente o en GitHub Actions, puedes consultar:
- Cobertura global en terminal  
- Detalle de líneas no cubiertas en el informe HTML (`htmlcov/index.html`)  
- Artefactos descargables desde Actions (`coverage-html`, `coverage.xml`)

---

## 🧩 Control de versiones y Git LFS

Para activar **Git LFS** (Fase 3):

```bash
git lfs install
git add .gitattributes
git commit -m "Activa Git LFS para data/models"
```

Ejemplo de `.gitattributes`:

```gitattributes
data/** filter=lfs diff=lfs merge=lfs -text
models/** filter=lfs diff=lfs merge=lfs -text
*.csv filter=lfs diff=lfs merge=lfs -text
```

---

## 🔄 Flujo completo del proyecto

```text
src/kit_utiles/ (código fuente)
        ↓
pytest + pytest-cov (tests)
        ↓
GitHub Actions (CI/CD)
        ↓
coverage.html + artifact XML
        ↓
Badge de estado en README.md
```

---

## 🏷️ Badge de estado

Añade al inicio del README:

```markdown
![CI](https://github.com/<USUARIO>/<REPO>/actions/workflows/ci.yml/badge.svg)
```

---

## 📚 Créditos y autoría

Proyecto desarrollado en el contexto docente del **Curso de Especialización en Inteligencia Artificial y Big Data (FP en Euskadi)**.  
Aplicación práctica de herramientas de desarrollo profesional:

- **Python 3.11**
- **pytest / pytest-cov**
- **GitHub Actions**
- **Git LFS**
- **Cobertura ≥ 80%**

---

## 🧭 Próximas fases sugeridas

| Fase | Contenido | Herramienta |
|-------|------------|-------------|
| **5** | Despliegue del paquete con Docker y push a Docker Hub | Docker + GitHub Actions |
| **6** | Publicación del paquete en PyPI (entorno formativo) | Twine / build |
| **7** | Integración con MLflow o Hugging Face | MLOps |

---
