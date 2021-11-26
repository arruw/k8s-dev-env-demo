from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {
        "msg": "Hello from Service 2"
    }


if __name__ == "__main__":
    import logging
    import argparse
    import uvicorn
    from pprint import pformat

    logging.basicConfig(format='{levelname:7} {message}', style='{', level=logging.INFO)

    parser = argparse.ArgumentParser(description='Run web service')
    parser.add_argument('--reload', action='store_true')

    kwargs = vars(parser.parse_args())
    logging.info(f"Running with kwargs: {pformat(kwargs)}")
    
    uvicorn.run("app:app", host="0.0.0.0", port=80, log_config=None, **kwargs)
