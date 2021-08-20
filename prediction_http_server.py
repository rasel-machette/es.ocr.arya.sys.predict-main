import uvicorn

if __name__ == "__main__":
    uvicorn.run("webapp.controller.predict:app", host="0.0.0.0", reload=True)
