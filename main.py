from fastapi import FastAPI, Response


app = FastAPI()


@app.get("/")
def main():
    return Response('<a href="/init.txt"></>', media_type="text/html")

