from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
async def ping() -> dict[str, str]:
    return {"message": "pong"}


def main() -> None:
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
