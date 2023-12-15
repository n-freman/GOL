from gol.entrypoints.cli import app

try:
    app()
except TypeError as e:
    print(e)
    print(type(e))
    import uvicorn
    uvicorn.run(app)

